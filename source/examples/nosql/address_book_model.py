#!/usr/bin/env python

"""
sample data for NOSQL examples

This version has a not completely-trival data model
"""


class Person(object):
    """
    class to represent an individual person
    """

    def __init__(self,
                 last_name,
                 first_name='',
                 middle_name='',
                 cell_phone='',
                 email='',
                 ):
        """
        initialize a Person object:
        """
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.middle_name = middle_name.strip()
        self.cell_phone = cell_phone.strip()
        self.email = email.strip()

    @property
    def name(self):
        return " ".join([self.first_name, self.middle_name, self.last_name])

    def __str__(self):
        msg = '{first_name} {middle_name} {last_name}'.format(**self.__dict__)
        return msg

    def __repr__(self):
        """
        not a good ___repr__, but want to have something here
        """
        return self.__str__()


class Address(object):
    """
    class that represents an address
    """

    def __init__(self,
                 line_1='',
                 line_2='',
                 city='',
                 state='',
                 zip_code='',
                 ):
        """
        initialize an address
        """

        self.line_1 = line_1.strip()
        self.line_2 = line_2.strip()
        self.city = city.strip()
        self.state = state.strip()
        self.zip_code = str(zip_code).strip()

    def __str__(self):
        msg = "{line_1}\n{line_2}\n{city} {state} {zip_code}\n".format(**self.__dict__)
        return msg


class Household(object):
    """
    Class that represents a Household.

    A household has one or more people, and a Location
    """

    def __init__(self,
                 name='',
                 people=(),
                 address=None,
                 phone=''
                 ):
        self.name = name.strip()
        self.people = list(people)
        self.address = address
        self.phone = phone.strip()

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


class AddressBook(object):
    """
    And address book -- has people, households, businesses.

    All fully cross-referenced
    """

    def __init__(self,
                 people=(),
                 businesses=(),
                 households=(),
                 ):
        self.people = list(people)
        self.businesses = list(businesses)
        self.households = list(households)

    def add_person(self, person):
        self.people.append(person)

    def add_household(self, household):
        self.households.append(household)

    def add_business(self, business):
        self.businesses.append(business)

    def __str__(self):
        msg = ["An Address Book:"]
        msg += ["People:"]
        msg += ["  " + person.name for person in self.find_people()]
        msg += ["Households:"]
        msg += ["  " + house.name for house in self.find_households()]
        msg += ["Businesses:"]
        msg += ["  " + bus.name for bus in self.find_businesses()]

        return "\n".join(msg)

    @property
    def locations(self):
        return self.households + self.businesses

    def find_people(self, name=''):
        """
        find all the people with name in their name somewhere
        """
        return [person for person in self.people if name.lower() in person.name.lower()]

    def find_zip_codes(self, zip_code):
        """
        find all the locations with this zip_code
        """
        zip_code = str(zip_code).strip()
        return [loc for loc in self.locations if loc.address.zip_code == zip_code]

    def find_state(self, state):
        """
        find all the locations in this state
        """
        return [location for location in self.locations if location.address.state == state]


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


