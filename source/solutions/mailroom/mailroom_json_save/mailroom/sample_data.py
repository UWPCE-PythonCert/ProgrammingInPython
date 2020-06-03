#!/usr/bin/env python

"""
sample data for testing, etc.

This is a python list of Donor objects, suitable for loading into a

DonorDB instance:

DB = DonorDB(sample_donor_data)

"""

from .model import Donor


def sample_donor_data():
    return [Donor("William Gates III", [653772.32, 12.17]),
            Donor("Jeff Bezos", [877.33]),
            Donor("Paul Allen", [663.23, 43.87, 1.32]),
            Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
            ]
