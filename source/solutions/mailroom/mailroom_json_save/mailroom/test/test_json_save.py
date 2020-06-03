#!/usr/bin/env python

"""
Test code for saving data to/from json with json_save
"""


import pytest

from json_save import json_save_dec as js

from mailroom.model import Donor, DonorDB


def test_one_donor():
    """
    creates an new donor with a couple donations
    """
    donor = Donor("Fred Flintstone", [34, 56])

    # save to a dict:
    jd = donor.to_json_compat()

    # recreate it
    donor2 = Donor.from_json_dict(jd)

    assert donor == donor2
    # Just to be extra sure:
    assert donor.name == donor2.name
    assert donor.donations == donor2.donations


def test_donor_db(sample_db):
    # Save the sample_db to a dict:

    dbd = sample_db.to_json_compat()

    # recreate it
    db2 = DonorDB.from_json_dict(dbd)

    # See if it's the same:
    assert db2 == sample_db


def test_donor_db_not_equal(sample_db, sample_db2):
    """
    makes sure that two DBs aren't equal if you change something.

    __eq__ is provided by json_save
    """
    # They should be equal initially

    assert sample_db == sample_db2

    # now make a change in one
    jeff_bezos = sample_db2.find_donor('jeff bezos')
    jeff_bezos.add_donation(2000)

    assert sample_db != sample_db2


def test_save(sample_db):
    # save out the DB
    sample_db.save()

    # Make a new one from the file
    with open(sample_db.db_file) as js_file:
        DB = js.from_json(js_file)

    # are they the same?
    assert sample_db == DB


def test_save_changed(sample_db):
    donor = sample_db.find_donor("paul allen")

    sample_db.save()

    donor.add_donation(500)

    sample_db.save()

    # Make a new one from the file
    with open(sample_db.db_file) as js_file:
        DB = js.from_json(js_file)

    donor1 = sample_db.find_donor("paul allen")
    donor2 = DB.find_donor("paul allen")
    assert donor1 == donor2
    assert donor2.num_donations == 4


def test_save_on_change_donor(sample_db):
    """
    tests the DB gets saved automatcially when it's changed
    """
    sample_db.save()  # make sure it's saved before we change it.
    donor = sample_db.find_donor("paul allen")

    donor.add_donation(500)
    # note: not explicitly saving it !

    # Make a new one from the file
    with open(sample_db.db_file) as js_file:
        DB = js.from_json(js_file)

    donor1 = sample_db.find_donor("paul allen")
    donor2 = DB.find_donor("paul allen")
    print(donor1)
    assert donor1 == donor2
    assert donor2.num_donations == 4


def test_save_on_add_donor(sample_db):
    """
    tests the DB gets saved automatcially when it's changed
    """
    sample_db.save()  # make sure it's saved before we change it.

    sample_db.add_donor("Fred Jones")
    # note: not explicitly saving it !

    # Make a new one from the file
    with open(sample_db.db_file) as js_file:
        DB = js.from_json(js_file)

    assert sample_db == DB





