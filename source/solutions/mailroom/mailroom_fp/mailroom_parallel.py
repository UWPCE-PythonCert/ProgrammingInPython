#!/usr/bin/env python3

#  http://uwpce-pythoncert.github.io/IntroToPython/exercises/mailroom-fp.html

import glob
import pickle
import ipyparallel as ipp


def print_usage():
    print(
        '''
        mailroom>>
        a: Add a donor and donation
        c: run a Challenge fundraiser
        h: Help (this message)
        l: List donors
        r: print Report
        s: Show database
        t: Thank donors
        q: quit
        '''
    )


def load_donordb():
    try:
        with open('mailroom.pickle', 'rb') as db_handle:
            donor_db = pickle.load(db_handle)
    except IOError:
        donor_db = {
            "Aristotle": [384.0, 322.0],
            "Kant": [1724.0, 1804.0, 1785.0],
            "Locke": [1632.0],
            "Russell": [1872.0, 1970.0, 1950.0],
            "Dennett": [1942.0],
        }
    return donor_db


def save_donordb(db):
    try:
        with open('mailroom.pickle', 'wb') as db_handle:
            pickle.dump(db, db_handle)
    except IOError:
        raise "Error: Unable to save donor database."


def add_donation(db, donor, contribution):

    # Validate user input as numeric
    try:
        float(contribution)
    except ValueError as my_except:
        print("mailroom>> Input validation error: {}".format(my_except))
        return None

    # Catch embezzlement
    try:
        assert float(contribution) >= 0.0
    except AssertionError as my_except:
        print("mailroom>> Donations must be greater than $0.00: {}".format(my_except))
        return None

    if donor in db.keys():
        db[donor].append(float(contribution))
    else:
        db[donor] = [float(contribution)]

    return db


def multiplier_factory(factor):
    '''
    A closure to create the multiplier function

    Args:
        factor (int): the multiplier to close into the returned function

    Returns:
        a function which will multiply its arguments by factor
    '''

    # Catch embezzlement
    try:
        assert int(factor) > 0
    except AssertionError as my_except:
        print("mailroom>> Challenge multipliers must be > 0: {}".format(my_except))
        return None

    def func(value):
        return int(factor) * value

    return func


def challenge(db, factor):
    """ Run a fund raising challenge

    Args:
        db (dict): the donor database
        factor (int): challenge multiplier

    Returns:
        dict: a new, updaated donor database
    """

    challenge_multiplier = multiplier_factory(factor)

    # Distributed map operation via ipyparallel
    for donor in db:
        c = ipp.Client()
        c[:].apply_sync(challenge_multiplier, db[donor])
    return db


def print_db(db):
    for name, donations in db.items():
        print(name, donations)


def tally_report(values):
    donation_total = sum(values)
    num_gifts = len(values)
    average_gift = donation_total / num_gifts
    return donation_total, num_gifts, average_gift


def print_report(db):
    # Print a header
    print("Donor Name                | Total Given | Num Gifts | Average Gift")

    # Print each row
    for names, values in db.items():
        donation_total, num_gifts, average_gift = tally_report(values)

        print("{} | {:11,.2f} | {} | ${:11,.2f}".format(
            names.ljust(25),
            donation_total,
            str(num_gifts).rjust(9),
            average_gift,
        ))


def thank_donor(donor, amount):
    with open('mailroom-thankyou-{}.txt'.format(donor), 'w') as f:
        f.write("Thank you, {}, for your generous donations totaling ${}.\nSincerly, The Mailroom Team\n".format(donor, amount))


def thank_donors(db):
    for name, values in db.items():
        thank_donor(name, sum(values))


def list_donor_files():
    print(glob.glob("mailroom-thankyou-*.txt"))


def main():
    '''
    Handle user interaction in the main event loop
    '''

    donor_db = load_donordb()

    while True:
        user_input = input("mailroom>> ")

        if user_input == 'quit' or user_input == 'q':
            save_donordb(donor_db)
            break

        elif user_input == 'add' or user_input == 'a':
            donor = input("mailroom: What is the name of the donor? ")
            contribution_amount = input("mailroom>> How much is {} contributing? ".format(donor))
            add_donation(donor_db, donor, contribution_amount)

        elif user_input == 'challenge' or user_input == 'c':
            factor = input("mailroom: Challenge! By what factor will donations be multiplied? ")
            donor_db = challenge(donor_db, factor)

        elif user_input == 'help' or user_input == 'h':
            print_usage()

        elif user_input == 'list' or user_input == 'l':
            print(sorted(set(donor_db.keys())))

        elif user_input == 'show' or user_input == 's':
            print_db(donor_db)

        elif user_input == 'report' or user_input == 'r':
            print_report(donor_db)

        elif user_input == 'thanks' or user_input == 't':
            thank_donors(donor_db)
            list_donor_files()


if __name__ == '__main__':
    print_usage()
    main()
