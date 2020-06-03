#!/usr/bin/env python
"""
models for the mailroom program.

This is where the program logic is.

This version has been made Object Oriented.
"""

# handy utility to make pretty printing easier
from textwrap import dedent
from pathlib import Path

import json_save.json_save_dec as js
import json

from . import data_dir


@js.json_save
class Donor:
    """
    class to hold the information about a single donor
    """
    name = js.String()
    donations = js.List()

    # reference to the DB its in -- this will be set in the instance
    # when added to the DonorDB
    _donor_db = None

    def __init__(self, name, donations=None):
        """
        create a new Donor object

        :param name: the full name of the donor

        :param donations=None: iterable of past donations
        """

        self.norm_name = self.normalize_name(name)
        self.name = name.strip()
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)

    def __str__(self):
        msg = (f"Donor: {self.name}, with {self.num_donations:d} "
               f"donations, totaling: ${self.total_donations:.2f}")
        return msg

    def mutating(method):
        """
        Decorator that saves the DB when a change is made

        It should be applied to all mutating methods, so the
        data will be saved whenever it's been changed.

        NOTE: This requires that the donor object is in a DonorDB.
        """

        # note that this is expecting to decorate a method
        # so self will be the first argument
        def wrapped(self, *args, **kwargs):
            print("wrapped method called")
            print(self)
            print(self._donor_db)
            res = method(self, *args, **kwargs)
            if self._donor_db is not None:
                self._donor_db.save()
            return res
        return wrapped

    @staticmethod
    def normalize_name(name):
        """
        return a normalized version of a name to use as a comparison key

        simple enough to not be in a method now, but maybe you'd want to make it fancier later.
        """
        return name.lower().strip()

    @property
    def last_donation(self):
        """
        The most recent donation made
        """
        try:
            return self.donations[-1]
        except IndexError:
            return None

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def average_donation(self):
        return self.total_donations / self.num_donations

    @mutating
    def add_donation(self, amount):
        """
        add a new donation
        """
        print("add_donation called")
        amount = float(amount)
        if amount <= 0.0:
            raise ValueError("Donation must be greater than zero")
        self.donations.append(amount)

    def gen_letter(self):
        """
        Generate a thank you letter for the donor

        :param: donor tuple

        :returns: string with letter

        note: This doesn't actually write to a file -- that's a separate
              function. This makes it more flexible and easier to test.
        """
        return dedent('''Dear {0:s},

              Thank you for your very kind donation of ${1:.2f}.
              It will be put to very good use.

                             Sincerely,
                                -The Team
              '''.format(self.name, self.last_donation)
                      )


@js.json_save
class DonorDB:
    """
    Encapsulation of the entire database of donors and data associated with them.
    """
    # specify a json_save dict as the data structure for the data.
    donor_data = js.Dict()

    _frozen = False

    def __init__(self, donors=None, db_file=None):
        """
        Initialize a new donor database

        :param donors=None: iterable of Donor objects

        :param db_file=None: path to file to store the datbase in.
                             if None, the data will be stored in the
                             package data_dir
        """
        if db_file is None:
            self.db_file = data_dir / "mailroom_data.json"
        else:
            self.db_file = Path(db_file)

        self.donor_data = {}

        if donors is not None:
            # you can set _frozen so that it won't save on every change.
            self._frozen = True
            for d in donors:
                self.add_donor(d)
            self.save  # save resets _frozen

    def mutating(method):
        """
        Decorator that saves the DB when a change is made

        It should be applied to all mutating methods, so the
        data will be saved whenever it's been changed.

        NOTE: This is not very efficient -- it will re-write
              the entire file each time.
        """

        # note that this is expecting to decorate a method
        # so self will be the first argument
        def wrapped(self, *args, **kwargs):
            res = method(self, *args, **kwargs)
            if not self._frozen:
                self.save()
            return res
        return wrapped

    @classmethod
    def load_from_file(cls, filename):
        """
        loads a donor database from a raw json file
        NOTE: This is not a json_save format file!
              -- it is a simpler, less flexible format.
        """
        with open(filename) as infile:
            donors = json.load(infile)
        db = cls([Donor(*d) for d in donors])
        return db

    @classmethod
    def load(cls, filepath):
        """
        loads a donor database from a json_save format file.
        """
        with open(filepath) as jsfile:
            db = js.from_json(jsfile)
        db.db_file = filepath

    def save(self):
        """
        Save the data to a json_save file
        """
        # if explicitly called, you want to do it!
        self._frozen = False
        with open(self.db_file, 'w') as db_file:
            self.to_json(db_file)

    @property
    def donors(self):
        """
        an iterable of all the donors
        """
        return self.donor_data.values()

    def list_donors(self):
        """
        creates a list of the donors as a string, so they can be printed

        Not calling print from here makes it more flexible and easier to
        test
        """
        listing = ["Donor list:"]
        for donor in self.donors:
            listing.append(donor.name)
        return "\n".join(listing)

    def find_donor(self, name):
        """
        find a donor in the donor db

        :param: the name of the donor

        :returns: The donor data structure -- None if not in the self.donor_data
        """
        return self.donor_data.get(Donor.normalize_name(name))

    @mutating
    def add_donor(self, donor):
        """
        Add a new donor to the donor db

        :param donor: A Donor instance, or the name of the donor

        :returns: The new or existing Donor object
        """

        if not isinstance(donor, Donor):
            donor = Donor(donor)
        self.donor_data[donor.norm_name] = donor
        donor._donor_db = self
        return donor

    @staticmethod
    def sort_key(item):
        # used to sort on name in self.donor_data
        return item[1]

    def generate_donor_report(self):
        """
        Generate the report of the donors and amounts donated.

        :returns: the donor report as a string.
        """
        # First, reduce the raw data into a summary list view
        report_rows = []
        for donor in self.donor_data.values():
            name = donor.name
            gifts = donor.donations
            total_gifts = donor.total_donations
            num_gifts = len(gifts)
            avg_gift = donor.average_donation
            report_rows.append((name, total_gifts, num_gifts, avg_gift))

        # sort the report data
        report_rows.sort(key=self.sort_key)
        report = []
        report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                                "Total Given",
                                                                "Num Gifts",
                                                                "Average Gift"))
        report.append("-" * 66)
        for row in report_rows:
            report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
        return "\n".join(report)

    def save_letters_to_disk(self):
        """
        make a letter for each donor, and save it to disk.
        """
        print("Saving letters:")
        for donor in self.donor_data.values():
            print("donor:", donor.name)
            letter = donor.gen_letter()
            # I don't like spaces in filenames...
            filename = donor.name.replace(" ", "_") + ".txt"
            open(filename, 'w').write(letter)
