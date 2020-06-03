#!/usr/bin/env python

"""
unit tests for the models in the mailroom program

$ pytest

will run the tests.

$ pytest py.test --cov=mailroom mailroom/test/

will run the tests and show a coverage report.

$ pytest --cov=mailroom --cov-report html mailroom/test/

will generate an html report.

NOTE: when I first ran it, I got 97% coverage -- it was missing tests
      of creating a Donor and DonorDB empty.

      This prompted me to write tests for these, and then I discoverd
      that I got an error when you tried to get the last_donation from
      a Donor that did not have any donations.

"""

import os
import pytest
from mailroom import model, data_dir


@pytest.fixture
def sample_db():
    """
    creates a clean sample database for the tests to use
    """
    return model.DonorDB.load_from_file(data_dir / "sample_data.json")


def test_empty_db():
    """
    tests that you can initilize an empty DB
    """
    db = model.DonorDB()

    donor_list = db.list_donors()
    print(donor_list)
    # no donors
    assert donor_list.strip() == "Donor list:"


def test_new_empty_donor():
    """
    creates an new donor with no donations
    """
    donor = model.Donor("Fred Flintstone")

    assert donor.name == "Fred Flintstone"
    assert donor.last_donation is None


def test_add_donation(sample_db):
    # fixme: there should be a better way to get an arbitrary donor
    donor = sample_db.donor_data.popitem()[1]

    donor.add_donation(3000)

    assert donor.last_donation == 3000


def test_add_donation_negative(sample_db):
    # fixme: there should be a better way to get an arbitrary donor
    donor = sample_db.donor_data.popitem()[1]

    with pytest.raises(ValueError):
        donor.add_donation(-100)

    with pytest.raises(ValueError):
        donor.add_donation(0.0)


def test_list_donors(sample_db):
    listing = sample_db.list_donors()

    # hard to test this throughly -- better not to hard code the entire
    # thing. But check for a few aspects -- this will catch the likely
    # errors
    assert listing.startswith("Donor list:\n")
    assert "Jeff Bezos" in listing
    assert "William Gates III" in listing
    assert len(listing.split('\n')) == 5


# fixme: add more odd serch test cases -- extra whitespace, etc.
def test_find_donor(sample_db):
    """ checks a donor that is there, but with odd case and spaces"""
    donor = sample_db.find_donor("jefF beZos ")

    assert donor.name == "Jeff Bezos"


def test_find_donor_not(sample_db):
    "test one that's not there"
    donor = sample_db.find_donor("Jeff Bzos")

    assert donor is None


def test_gen_letter(sample_db):
    """ test the donor letter """

    # create a sample donor
    donor = model.Donor("Fred Flintstone", [432.45, 65.45, 230.0])
    letter = sample_db.gen_letter(donor)
    # what to test? tricky!
    assert letter.startswith("Dear Fred Flintstone")
    assert letter.endswith("-The Team\n")
    assert "donation of $230.00" in letter


def test_add_donor(sample_db):
    name = "Fred Flintstone  "

    donor = sample_db.add_donor(name)
    donor.add_donation(300)
    assert donor.name == "Fred Flintstone"
    assert donor.last_donation == 300
    assert sample_db.find_donor(name) == donor


def test_generate_donor_report(sample_db):

    report = sample_db.generate_donor_report()

    print(report)  # printing so you can see it if it fails
    # this is pretty tough to test
    # these are not great, because they will fail if unimportant parts of the
    # report are changed.
    # but at least you know that code's working now.
    assert report.startswith("Donor Name                | Total Given | Num Gifts | Average Gift")

    assert "Jeff Bezos                  $    877.33           1   $     877.33" in report


def test_save_letters_to_disk(sample_db):
    """
    This only tests that the files get created, but that's a start

    Note that the contents of the letter was already
    tested with test_gen_letter
    """

    # FIXME: this should create a temp dir to save to.
    sample_db.save_letters_to_disk()

    assert os.path.isfile('Jeff_Bezos.txt')
    assert os.path.isfile('William_Gates_III.txt')
    # check that it's not empty:
    with open('William_Gates_III.txt') as f:
        size = len(f.read())
    assert size > 0


# if __name__ == "__main__":
#     # this is best run with a test runner, like pytest
#     # But if not, at least this will run them all.
#     test_list_donors()
#     test_find_donor()
#     test_find_donor_not()
#     test_gen_letter()
#     test_add_donor()
#     test_generate_donor_report()
#     test_save_letters_to_disk()
#     print("All tests Passed")
