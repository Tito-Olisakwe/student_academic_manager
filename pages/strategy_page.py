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

procrastination = Strategies(name='procrastination',
overall_average = overall_average, user_score = user_score,
description = """ 
Lack of motivation, fatigue, anxiety and similar emotions can cause Procrastination. 
This is because we tend to rely on our willpower to carry out tasks, so when we don't feel 
like doing something our willpower fails us and we start procrastinating. It's possible to want to do something
 but also not feel like doing it, you know it's important but you just don't have the motivation 
 to carry out the task. If you find yourself in this situation often, you need to stop relying on willpower 
 and create a system for doing your work. A simple and effective system that will enable you to do
  your work even when you lack motivation is forming Tiny Habits.

To do this:
1. Determine the tiny habit you want to form. (e.g Doing micro courses)
2. Pick an existing habit that you can do your tiny habit immediately after. (e.g watching anime)
3. Decide on a small celebration to do each time you complete your tiny habit. (e.g a high-five)
4. Use this formula: After I [existing habit] I will [new tiny behaviour], then I will [small celebration].

For example, your tiny habit statement could be:
After I watch an episode of Jujutsu Kaisen I will do one section of a micro-course, and then I will give myself a high-five.
""")

personalstudy = Strategies(name='personal study',
overall_average = overall_average, user_score = user_score,
description = """
An individual should have their own private time scheduled where they can sit down and personally reflect and go through everything that they didn’t understand before.
This will not only help them understand concepts better but also give them time to do more research and test their knowledge.

"""
)

