#!/usr/bin/python3
# This page will display list of all strategies


class Strategies:
    def __init__(self, name, description, overall_average, user_score):
        self.name = name
        self.description = description
        self.overall_average = overall_average
        self.user_score = user_score
     
     
     
        
def suggest_strategy_subject(user_score):
    if user_score <= 25:
        print(f'{time_management.name}')
        print(f'{time_management.description}')
    elif user_score <= 50:
        print(f'{jornaling.name}')
        print(f'{jornaling.description}')
    elif user_score <= 75: 
        print(f'{self_regulation.name}')
        print(f'{self_regulation.description}')
    else:
        print("congratulation keep it up")
    
    
def suggest_strategy_overall(overall_average):
    if user_score <= 1.6:
        print(f'{time_management.name}')
        print(f'{time_management.description}')
    elif user_score <= 2.6:
        print(f'{jornaling.name}')
        print(f'{jornaling.description}')
    elif user_score <= 4.6: 
        print(f'{self_regulation.name}')
        print(f'{self_regulation.description}')
    else:
        print("congratulation keep it up")



# Strategies
time_management = Strategies(name='Time Management', 
overall_average = overall_average, user_score = user_score,
description=
'''
If you've observed that your time wanders while studying, a time management tool should be
implemented during study sessions. The Pomodoro technique will help you become more self-aware 
of how you spend your time and also help you stay focused. 

To use this technique:
1. Determine the total time you want to spend studying.
2. Set a duration for concentrated work.
3. Set a duration for intermediate rest.

The default is 25mins for focused work and 5mins for rest before starting another 25mins of 
concentrated work. You can adjust the duration based on what is suitable for you. 

For example; If your total study time is 3 hours, you will completely focus on studying for 
25mins and then rest for 5mins over and over again until the 3 hours is up.
''')


jornaling = Strategies(name='Journaling', 
overall_average = overall_average, user_score = user_score,
description=
'''
Journaling offer a good way to pen down their thought and experience for later use,
This helps students to track their progress through writing down what they have done.
Also can help them to know their strengths and weaknesses.

''')

self_regulation = Strategies(name='Self Regulation', 
overall_average = overall_average, user_score = user_score,
description=
'''
Achieving excellence takes practice. It takes planning, effort, and persistence over time. 
Self-regulating learning aids this process. It allows students to become independent learners 
who can pursue their own interests.
Developing this skill set allows students to learn more effectively because they can set clear 
goals and track their progress against their goals and strategies. Self-regulation allows 
students to become less reactive and more active in learning.

''') 
