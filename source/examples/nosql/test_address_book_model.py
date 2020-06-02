#!/usr/bin/env python

"""
test code for address book model code
if testing mongo, remember to start database first
$ mongod --dbpath=mongo_data/
"""

import address_book_model as model
# import address_book_zodb as model
# import address_book_mongo as model


a_book = model.create_sample()


def test_name_search():
    """find a single person by first name"""

    people = a_book.find_people('chris')

    assert len(people) == 1
    assert people[0].first_name == 'Chris'
    assert people[0].last_name == 'Barker'


def test_name_search2():
    people = a_book.find_people('barKer')
    first_names = [p.first_name for p in people]

    assert 'Chris' in first_names
    assert 'Emma' in first_names
    assert 'Donna' in first_names


def test_zip_search():
    locations = a_book.find_zip_codes(98105)

    assert len(locations) == 1
    assert locations[0].name == 'Python Certification Program'


def test_state_search():
    locations = a_book.find_state('WA')
    names = [l.name for l in locations]

    assert "The Barkers" in names
    assert "Python Certification Program" in names
