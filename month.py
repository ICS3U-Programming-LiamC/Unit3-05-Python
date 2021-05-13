#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 13, 2021
# This program determines month based on the users
# month input

def find_month(month_num):
    # the complexity that is pythons makeshift switches
    # depending on the number the user inputs
    # match that to a result, then return that result to
    # be printed back to the user
    months = {
        1: "{} represents January.".format(month_num),
        2: "{} represents February.".format(month_num),
        3: "{} represents March.".format(month_num),
        4: "{} represents April.".format(month_num),
        5: "{} represents May.".format(month_num),
        6: "{} represents June.".format(month_num),
        7: "{} represents July.".format(month_num),
        8: "{} represents August.".format(month_num),
        9: "{} represents September.".format(month_num),
        10: "{} represents October.".format(month_num),
        11: "{} represents Novermber.".format(month_num),
        12: "{} represents December.".format(month_num)
    }
    # returns the result to be printed
    return months.get
    (month_num, "Error. {} does not represent a month.".format(month_num))


if __name__ == "__main__":
    # get the month number from the user
    month_num = int(input("What is the number of the month: "))
    # prints the retured result
    print(find_month(month_num))
