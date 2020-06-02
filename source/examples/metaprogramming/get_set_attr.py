#!/usr/bin/env python3

"""
Manipulating attributes

Example code for manipulating attributes
"""


# A simple class for a person
class Person:
    def __init__(self, first_name="", last_name="", phone=""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __str__(self):
        msg = ["Person:"]
        for name, val in vars(self).items():
            msg.append("{}: {}".format(name, val))
        return "\n".join(msg)


def update_person(person):
    while True:
        att = input("What would you like to update for:\n"
                    "{}\n"
                    '(type "quit" to quit) >> '.format(person)
                    )
        if att.strip().lower() == "quit":
            break
        if not hasattr(person, att):
            ans = input("This person does not have that attribute.\n"
                        "Would you like to add it? Y,[N] >> ")
            if not ans.lower().startswith('y'):
                continue
        ans = input("What would you like to set it to? >> ")
        setattr(person, att, ans)


if __name__ == "__main__":
    # a little test code:

    # create a couple people:
    p1 = Person("Fred", "Jones", "206-555-1234")
    update_person(p1)


