#!/usr/bin/env python

"""
test code for the mongo specific addressbook model
remember to start mongo database first

$ mongod --dbpath=mongo_data/
"""

import pytest

import address_book_mongo as model


@pytest.fixture
def chris():
    chris = model.Person(last_name='Barker',
                         first_name='Chris',
                         middle_name='H',
                         cell_phone='(123) 555-7890',
                         email='PythonCHB@gmail.com',
                         )
    return chris


@pytest.fixture
def fred():
    fred = model.Person(last_name='Jones',
                        first_name='Fred',
                        middle_name='B',
                        cell_phone='(123) 555-7890',
                        email='FredJones@gmail.com',
                        )
    return fred


def test_person_to_dict(chris):
    dct = chris.to_dict()

    assert dct['last_name'] == "Barker"
    assert dct['email'] == 'PythonCHB@gmail.com'


def test_person_to_from_dict(chris):

    dct = chris.to_dict()
    chris2 = model.Person.from_dict(dct)

    print(chris2)

    assert chris2.last_name == 'Barker'
    assert chris2.first_name == 'Chris'
    assert chris2.middle_name == 'H'
    assert chris2.cell_phone == '(123) 555-7890'
    assert chris2.email == 'PythonCHB@gmail.com'


def test_household_to_dict(chris):
    home = model.Household(name="The Barkers",
                           people=(chris,),
                           address=model.Address(line_1='123 Some St',
                                                 line_2='Apt 1234',
                                                 city='Seattle',
                                                 state='WA',
                                                 zip_code='98000',),
                           phone='123-456-8762',
                           )

    home_dct = home.to_dict()

    assert home_dct['name'] == "The Barkers"
    assert home_dct['address']['city'] == 'Seattle'


def test_household_to_dict_to_object(chris, fred):

    home = model.Household(name="The Barkers",
                           people=(chris, fred),
                           address=model.Address(line_1='123 Some St',
                                                 line_2='Apt 1234',
                                                 city='Seattle',
                                                 state='WA',
                                                 zip_code='98000',),
                           phone='123-456-8762',
                           )

    home2 = model.Household.from_dict(home.to_dict())

    assert home2.name == home.name
    assert home2.phone == home.phone
    assert home2.address.line_1 == home.address.line_1
    assert home2.address.line_2 == home.address.line_2
    assert home2.people == home.people
