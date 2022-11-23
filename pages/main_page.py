#!/usr/bin/python3
# This page will display list of all subjects
# This page will display list of profiles
# This page will display list of all strategies
# This page will display list of average
# This page will display list of users to navigate all pages.

user_name = 'Stella Umwari'


def display_main(user_name):
    print(f"""
Hello {user_name}, 
This is the list of all your subjects:

Curiosity               -- to go here type 1
Learning goals          -- to go here type 2
Self assessment         -- to go here type 3
Navigating ambiguity    -- to go here type 4
Process thinking        -- to go here type 5
Sourcing discerningly   -- to go here type 6
Documenting             -- to go here type 7
Organizing with principles    -- to go here type 8
Motivation              -- to go here type 9
Procrastination         -- to go here type 10
Reflective practice     -- to go here type 11
Articulating purpose    -- to go here type 12
Portfolio building      -- to go here type 13
Teaching forward        -- to go here type 14
Articulating process    -- to go here type 15


This is the list of all the strategies:

Time Management
Procrastination
Personal Study
External and Extensive Research
Reflective Practice
Team Work
Process Thinking
Journaling
Having Action Plan
Self-Assessment
Feedback
Self-Regulation

To see the description of each strategy, type s

Your overall average is XX 
To see more information on average, type a

To come back to the main page from anywhere, type m
""")


display_main(user_name)
