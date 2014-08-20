# We'll start off by grabbing your names from the last file

from A_defining_strings import your_first_name, your_last_name

import A_defining_strings as A

# Using string methods
## We're updating our administrative system, so we need to capitalize your last
## name. There's a simple way to do that with a string "method" called .upper()

## Set cap_last_name to an uppercase version of your_last_name

cap_last_name = A.your_last_name.upper()

## You can print it to see how it looks

print cap_last_name


## And we'll need to check how long your name is to make sure there's enough
## space in our database! Be sure to count a space between your first and last
## name, and use the len() function to compute the lengths


## Put the total length of your name in name_len. You can use multiple steps if
## you like.

name_len = len(cap_last_name) + len(A.your_first_name) + 1

print "We'll need", name_len, "characters for my name"


## Note that we've been using print with commas. This puts a space between each
## string or variable. But what if we don't want a space? In this case, we can
## append two strings (including variables) using +. See if you can create a
## "last name first" version of your name, with a comma separating the two.
## For example, I'd be "CLARK, Dav"

print "CLARK, Dav... wait, that's not right!"
print cap_last_name + ", " + A.your_first_name