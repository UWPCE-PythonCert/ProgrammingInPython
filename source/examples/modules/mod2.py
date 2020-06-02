#!/usr/bin/env python3

import mod1

print(f"In mod2: mod1.x = {mod1.x}")

input("pausing (hit enter to continue >")

print("importing mod3")

import mod3

print(f"Still in mod2: mod1.x = {mod1.x}")

print("mod3 changed the value in mod1, and that change shows up in mod2")
