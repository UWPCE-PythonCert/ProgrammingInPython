#!/usr/bin/env python

"""
Sample data for NOSQL examples

This version uses mongoDB to store the data.

NOTE: you need to start up the DB first:

$ mongod --dbpath=mongo_data/

"""

# ObjectID provides a new unique ID when you need one.
from bson import ObjectId


class PersistObject:
    """
    mix-in class for object you want to be able to put in a mongoDB

    defines the basic to_dict and from_dict methods

    This could be a metaclass, or class decorator, or...
    """
    def to_dict(self):
        """
        returns a dictionary of all the data in the object

        pretty simple in this case, but might be more to it
        for a more complicated class
        """
        return self.__dict__

    @classmethod
    def from_dict(cls, dct):
        """
        Returns a new object initialized from the values in dct

        Just calls the usual __init__ in this case. but could be more
        to it in a more complex case.
        """
        return cls(**dct)


class Person(PersistObject):
    """
    class to represent an individual person
    """
    def __init__(self,
                 last_name,
                 first_name='',
                 middle_name='',
                 cell_phone='',
                 email='',
                 _id=None,
                 ):
        """
        initialize a Person object:
        """
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.middle_name = middle_name.strip()
        self.cell_phone = cell_phone.strip()
        self.email = email.strip()
        self._id = ObjectId() if _id is None else _id

    @property
    def name(self):
        return " ".join([self.first_name, self.middle_name, self.last_name])

    def __str__(self):
        msg = '{first_name} {middle_name} {last_name}'.format(**self.__dict__)
        return msg

    def __repr__(self):
        """
        Not a good ___repr__, but want to have something here
        """
        return self.__str__()


class Address(PersistObject):
    """
    class that represents an address
    """
    def __init__(self,
                 line_1='',
                 line_2='',
                 city='',
                 state='',
                 zip_code='',
#                  **kwargs
                 ):
        """
        Initialize an address
        """

        self.line_1 = line_1.strip()
        self.line_2 = line_2.strip()
        self.city = city.strip()
        self.state = state.strip().upper()
        self.zip_code = str(zip_code).strip()

    def __str__(self):
        msg = "{line_1}\n{line_2}\n{city} {state} {zip_code}\n".format(**self.__dict__)
        return msg


class Household(PersistObject):
    """
    Class that represents a Household.

    A household has one or more people, and a Location
    """

    def __init__(self,
                 name = '',
                 people=(),
                 address=None,
                 phone='',
                 **kwargs
                 ):

        self.name = name.strip()
        # if it's already a ObjectID, then don't need to extract it.
        try:
            self.people = [p._id for p in people]
        except AttributeError:
            self.people = people
        self.address = address
        self.phone = phone.strip()

    def to_dict(self):
        """
        convert to dict -- stores ids of people
        """
        dct = self.__dict__
        dct['address'] = self.address.to_dict()
        return dct

    @classmethod
    def from_dict(cls, dct):
        """
        creates a household object from a dict representation
        unpacks the people _ids and address.
        """
        dct['address'] = Address(**dct['address'])
        return cls(**dct)

    def __str__(self):
        msg = [self.name + ":"]
        msg += [str(self.address)]
        return "\n".join(msg)

    def __repr__(self):
        return self.__str__()


class Business(Household):
    """
    Class that represents a Business

    A business has one or more people,
    and address and a phone number
    """
    # Same as household now, but you never know.
    pass


class AddressBook:
    """
    An address book -- has people, households, businesses.

    All cross-referenced (normalized)
    """

    def __init__(self,
                 people=(),
                 businesses=(),
                 households=(),
                 fresh=True,
                 ):

        # create the DB
        from pymongo import MongoClient

        client = MongoClient('localhost', 27017)
        db = client.address_book
        if fresh:
            ## clean out old one
            db.people.drop()
            db.businesses.drop()
            db.households.drop()

        # Use the DB to hold the data
        self.people = db.people
        self.businesses = db.businesses
        self.households = db.households

    def add_person(self, person):
        self.people.insert(person.to_dict())

    def add_household(self, household):
        self.households.insert(household.to_dict())

    def add_business(self, business):
        self.businesses.insert(business.to_dict())

    def __str__(self):
        msg = ["An Address Book:"]
        msg += ["People:"]
        msg += ["  " + person.name for person in self.find_people()]
        msg += ["Households:"]
        msg += ["  " + house.name for house in self.find_households()]
        msg += ["Businesses:"]
        msg += ["  " + bus.name for bus in self.find_businesses()]

        return "\n".join(msg)

    def find_people(self, name=''):
        """
        Find all the people with name in their name somewhere
        """
        # fixme -- can this query be combined?
        # like this:
        #   db.inventory.find( { $or: [ { qty: { $lt: 20 } }, { sale: true } ] } )

        cursor = self.people.find({"first_name": {'$regex': '.*' + name + '.*',
                                                  '$options': 'i'}})
        results = [Person.from_dict(p) for p in cursor]

        cursor = self.people.find({"last_name": {'$regex': '.*' + name + '.*',
                                                 '$options': 'i'}})

        return results + [Person.from_dict(p) for p in cursor]

    def find_households(self):
        cursor = self.households.find()
        return [Household.from_dict(p) for p in cursor]

    def find_businesses(self):
        cursor = self.businesses.find()
        return [Business.from_dict(p) for p in cursor]

    def find_zip_codes(self, zip_code):
        """
        find all the locations with this zip_code
        """
        zip_code = str(zip_code).strip()
        cursor = self.households.find({"addresses.zip_code": zip_code})
        results = [Household.from_dict(dct) for dct in cursor]

        cursor = self.businesses.find({"address.zip_code": zip_code})
        results += [Business.from_dict(dct) for dct in cursor]

        return results

    def find_state(self, state):
        """
        find all the locations in this state
        """
        state = state.strip().upper()
        cursor = self.households.find({"address.state": state})
        results = [Household.from_dict(dct) for dct in cursor]

        cursor = self.businesses.find({"address.state": state})
        results += [Business.from_dict(dct) for dct in cursor]

        return results


def create_sample():
    """
    Create a sample Address Book
    """
    chris = Person(last_name='Barker',
                   first_name='Chris',
                   middle_name='H',
                   cell_phone='(123) 555-7890',
                   email='PythonCHB@gmail.com',
                   )

    emma = Person(last_name='Barker',
                  first_name='Emma',
                  middle_name='L',
                  cell_phone='(345) 555-9012',
                  email='emma@something.com',
                  )

    donna = Person(last_name='Barker',
                   first_name='Donna',
                   middle_name='L',
                   cell_phone='(111) 555-1111',
                   email='dbarker@something.com',
                   )

    barker_address = Address(line_1='123 Some St',
                             line_2='Apt 1234',
                             city='Seattle',
                             state='WA',
                             zip_code='98000',)

    the_barkers = Household(name="The Barkers",
                            people=(chris, donna, emma),
                            address=barker_address)

    joseph = Person(last_name='Sheedy',
                    first_name='Joseph',
                    cell_phone='(234) 555-8910',
                    email='js@some_thing.com',
                    )

    cris = Person(last_name='Ewing',
                  first_name='Cris',
                  cell_phone='(345) 555-6789',
                  email='cris@a_fake_domain.com',
                  )

    fulvio = Person(last_name='Casali',
                    first_name='Fulvio',
                    cell_phone='(345) 555-1234',
                    email='fulvio@a_fake_domain.com',
                    )

    fred = Person(first_name="Fred",
                  last_name="Jones",
                  email='FredJones@some_company.com',
                  cell_phone="403-561-8911",
                  )

    python_cert_address = Address('UW Professional and Continuing Education',
                                  line_2='4333 Brooklyn Ave. NE',
                                  city='Seattle',
                                  state='WA',
                                  zip_code='98105',
                                  )

    python_cert = Business(name='Python Certification Program',
                           people=(chris, joseph, cris, fulvio),
                           address=python_cert_address
                           )


    address_book = AddressBook()

    address_book.add_person(chris)
    address_book.add_person(donna)
    address_book.add_person(emma)
    address_book.add_person(cris)
    address_book.add_person(joseph)
    address_book.add_person(fulvio)
    address_book.add_person(fred)

    address_book.add_household(the_barkers)

    address_book.add_business(python_cert)

    return address_book


if __name__ == "__main__":
    address_book = create_sample()

    print("Here is the address book")
    print(address_book)


