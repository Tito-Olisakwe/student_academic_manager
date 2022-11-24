#!/usr/bin/python3
import value

user_name = 'Tito-Paris'


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

Learning processes overview    -- to go here type 16
Reflective practice overview   -- to go here type 17


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

Your overall average is {value.overall_gpa()} 
To see more information on average, type a

To come back to the main page from anywhere, type m
To end program, type e
""")
