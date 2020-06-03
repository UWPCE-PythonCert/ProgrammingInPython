# test-mailroom.py

import pytest
from random import randint, SystemRandom
from string import ascii_letters as letters

# from mailroom_mfr import (
from mailroom_parallel import (
    load_donordb,
    add_donation,
    tally_report,
)


@pytest.fixture(scope='module')
def db():
    return load_donordb()


def test_add_donation(db):
    random_donor_name = ''.join(SystemRandom().choice(letters) for _ in range(20))

    random_amount_1 = randint(0, 999999)
    add_donation(db, random_donor_name, random_amount_1)

    random_amount_2 = randint(0, 999999)
    add_donation(db, random_donor_name, random_amount_2)

    assert random_donor_name in db.keys()
    assert random_amount_1 in db[random_donor_name]
    assert random_amount_2 in db[random_donor_name]


def test_tally_report(db):
    doner = 'Aristotle'
    donation_total, num_gifts, average_gift = tally_report(db[doner])

    assert donation_total == sum(db[doner])
    assert num_gifts == len(db[doner])
    assert average_gift == donation_total / num_gifts
