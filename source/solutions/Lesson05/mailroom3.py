#!/usr/bin/env python
"""
mailroom assignment

This version uses a dict for the main db, and a dict to"switch" on the user's
input choices.

it also write the thank you letters to files.

"""

import sys
import math
from operator import itemgetter

# handy utility to make pretty printing easier
from textwrap import dedent


# In memory representation of the donor database
# using a tuple for each donor
# -- kind of like a record in a database table
# using a dict with a lower case version of the donor's name as the key
# This makes it easier to have a 'normalized' key.
#  you could get a bit fancier by having each "record" be a dict, with
#   "name" and "donations" as keys.

def get_donor_db():
    return {'william gates iii': ("William Gates III", [653772.32, 12.17]),
            'jeff bezos': ("Jeff Bezos", [877.33]),
            'paul allen': ("Paul Allen", [663.23, 43.87, 1.32]),
            'mark zuckerberg': ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            }


def list_donors():
    """
    Create a list of the donors as a string, so they can be printed

    Not calling print from here makes it more flexible and easier to
    test
    """
    listing = ["Donor list:"]
    for donor in donor_db.values():
        listing.append(donor[0])
    return "\n".join(listing)


def print_donor_list():
    """
    Doesn't do much, but keeps the printing separate
    """
    print(list_donors())
    print()


def find_donor(name):
    """
    Find a donor in the donor db

    :param: the name of the donor
    :returns: The donor data structure -- None if not in the donor_db
    """
    key = name.strip().lower()
    return donor_db.get(key)


def add_donor(name):
    """
    Add a new donor to the donor db

    :param: the name of the donor
    :returns: the new Donor data structure
    """
    name = name.strip()
    donor = (name, [])
    donor_db[name.lower()] = donor
    return donor


def gen_letter(donor):
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
          '''.format(donor[0], donor[1][-1]))


def take_donation():
    """
    Ask user for donation amount, and then add it  to the DB
    """
    # Now prompt the user for a donation amount to apply. Since this is
    # also an exit point to the main menu, we want to make sure this is
    # done before mutating the db.
    print("in take_donation")
    name = input("Enter a donor name (new or existing): \n >")
    while True:
        amount_str = input("Enter a donation amount (or <enter> to exit)> ").strip()
        if not amount_str:
            # if they provide no input, go back to previous menu
            return
        # Make sure amount is a valid amount before leaving the input loop
        try:
            amount = float(amount_str)
            # extra check here -- unlikely that someone will type "NaN", but
            # it IS possible, and it is a valid floating point number:
            # http://en.wikipedia.org/wiki/NaN
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                raise ValueError
        except ValueError:
            print("error: donation amount is invalid\n")
            continue
        else:
            break

    donor = find_donor(name)
    # If the donor is not found, it's a new donor
    if donor is None:
        # add the new donor to the database
        donor = add_donor(name)

    # Record the donation
    donor[1].append(amount)
    # print the thank you letter
    print(gen_letter(donor))


def sort_key(item):
    # used to sort on name in donor_db
    return item[1]


def generate_donor_report():
    """
    Generate the report of the donors and amounts donated.

    :returns: the donor report as a string.
    """
    # First, reduce the raw data into a summary list view
    report_rows = []
    for (name, gifts) in donor_db.values():
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    # sort the report data
    report_rows.sort(key=itemgetter(1), reverse=True)
    report = []
    report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                            "Total Given",
                                                            "Num Gifts",
                                                            "Average Gift"))
    report.append("-" * 66)
    for row in report_rows:
        report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
    return "\n".join(report)


def save_letters_to_disk():
    """
    make a letter for each donor, and save it to disk.
    """
    for donor in donor_db.values():
        letter = gen_letter(donor)
        # I don't like spaces in filenames...
        filename = donor[0].replace(" ", "_") + ".txt"
        print("writing letter to:", donor[0])
        open(filename, 'w').write(letter)


def print_donor_report():
    print(generate_donor_report())


def return_to_menu():
    ''' Return True to trigger exit out of sub-loop'''
    return True


def send_thank_you():
    """
    Execute the logic to record a donation and generate a thank you message.
    """
    # Read a valid donor to send a thank you from, handling special commands to
    # let the user navigate as defined.
    prompt = ("To send a thank you, select one:\n\n"
              "(1) Update donor and send thank-you\n"
              "(2) List all existing DONORS\n"
              "(3) Return to main menu\n > ")
    selection_dict = {"1": take_donation,
                      "2": print_donor_list,
                      "3": return_to_menu,
                      }
    run_menu(prompt, selection_dict)

def main_menu():
    """
    Run the main menu for mailroom
    """
    prompt = dedent('''
                    Choose an action:

                    (1) - Send a Thank You
                    (2) - Create a Report
                    (3) - Send letters to everyone
                    (4) - Quit

                    > ''')

    selection_dict = {"1": send_thank_you,
                      "2": print_donor_report,
                      "3": save_letters_to_disk,
                      "4": quit}

    run_menu(prompt, selection_dict)


def run_menu(prompt, selection_dict):
    """
    run an interactive menu

    :param prompt: What you want to ask the user

    :param selection_dict: Dict of possible user impots mapped to
                           the actions to take.
    """
    while True:
        selection = input(prompt).strip().lower()
        try:
            if selection_dict[selection]():
                # break out of the loop if action returns True
                break
        except KeyError:
            print("error: menu selection is invalid!")


if __name__ == "__main__":
    donor_db = get_donor_db()
    main_menu()
