#!/usr/bin/python3
# This page will display list of all strategies

subject_name = 'course'
module_name = 'module'
user_score = 50
user_summative_score = 2.5
module_average = 2.5
overall_average = 2.5
recommended_strategy = 'strategy'
updated_score = False


class Strategies:
    def __init__(self, name, description, overall_average, user_score):
        self.name = name
        self.description = description
        self.overall_average = overall_average
        self.user_score = user_score


def suggest_strategy_subject(user_score):
    if user_score <= 19:
        print('suggest strategy')
    elif user_score <= 39:
        print('suggest strategy')
    elif user_score <= 49:
        print('suggest strategy')
    elif user_score <= 59:
        print('suggest strategy')
    elif user_score <= 64:
        print('suggest strategy')
    elif user_score <= 69:
        print('suggest strategy')
    elif user_score >= 70:
        print('suggest strategy')


def suggest_strategy_overall(overall_average):
    if overall_average <= 1:
        print('suggest strategy')
    elif overall_average <= 2:
        print('suggest strategy')
    elif overall_average <= 3:
        print('suggest strategy')
    elif overall_average <= 4:
        print('suggest strategy')
    elif overall_average >= 4.5:
        print('suggest strategy')


# Strategies
time_management = Strategies(name='Time Management',
                             overall_average=overall_average, user_score=user_score,
                             description='''
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
                       overall_average=overall_average, user_score=user_score,
                       description='''
Journaling offer a good way to pen down their thought and experience for later use,
This helps students to track their progress through writing down what they have done.
Also can help them to know their strengths and weaknesses.

''')

self_regulation = Strategies(name='Self Regulation',
                             overall_average=overall_average, user_score=user_score,
                             description='''
Achieving excellence takes practice. It takes planning, effort, and persistence over time. 
Self-regulating learning aids this process. It allows students to become independent learners 
who can pursue their own interests.
Developing this skill set allows students to learn more effectively because they can set clear 
goals and track their progress against their goals and strategies. Self-regulation allows 
students to become less reactive and more active in learning.

''')

procrastination = Strategies(name='Procrastination',
                             overall_average=overall_average, user_score=user_score,
                             description=""" 
Lack of motivation, fatigue, anxiety and similar emotions can cause Procrastination. 
This is because we tend to rely on our willpower to carry out tasks, so when we don't feel 
like doing something our willpower fails us and we start procrastinating. It's possible to want 
to do something but also not feel like doing it, you know it's important but you just don't have 
the motivation to carry out the task. If you find yourself in this situation often, you need to stop 
relying on willpower and create a system for doing your work. A simple and effective system that will 
enable you to do your work even when you lack motivation is forming Tiny Habits.

To do this:
1. Determine the tiny habit you want to form. (e.g Doing micro courses)
2. Pick an existing habit that you can do your tiny habit immediately after. (e.g watching anime)
3. Decide on a small celebration to do each time you complete your tiny habit. (e.g a high-five)
4. Use this formula: After I [existing habit] I will [new tiny behaviour], then I will [small celebration].

For example, your tiny habit statement could be:
After I watch an episode of Jujutsu Kaisen I will do one section of a micro-course, and then I will 
give myself a high-five.

""")

personal_study = Strategies(name='Personal Study',
                            overall_average=overall_average, user_score=user_score,
                            description="""
An individual should have their own private time scheduled where they can sit down and personally 
reflect and go through everything that they didn’t understand before. This will not only help them 
understand concepts better but also give them time to do more research and test their knowledge.

"""
                            )


external_extensive_research = Strategies(name='External and Extensive Research',
                                         overall_average=overall_average, user_score=user_score,
                                         description="""
A student should not only take the information given to them but also make time to find 
their own information by making research.

"""
                                         )


reflective_practice = Strategies(name='Reflective Practice',
                                 overall_average=overall_average, user_score=user_score,
                                 description="""
Reflective practice is a process of constantly reflecting on one's own actions and thoughts in 
order to improve upon them. It is a way of constantly learning from one's own experiences and 
growing as a result. Reflective practice is an important part of being a successful learner, as 
it allows individuals to identify areas in which they need to improve and then take steps to address 
those areas.

"""
                                 )
team_work = Strategies(name='Team Work',
                       overall_average=overall_average, user_score=user_score,
                       description="""
Teamwork is an important skill that students need to learn in order to be successful in school and 
in their future careers. When students work together in teams, they can accomplish more than they 
could alone. Teamwork also helps students to develop important social skills, such as communication 
and cooperation. Working in teams can be challenging at times, but it is also a lot of fun. Students 
who are able to work together effectively can learn a lot from each other and build strong relationships.

"""
                       )


process_thinking = Strategies(name=' Process Thinking',
                              overall_average=overall_average, user_score=user_score,
                              description="""
All results are based on Process to get better results students needs to think about their learning process, 
so students needs to analyze, modify and follow an efficient process
"""
                              )

action_plan = Strategies(name='Having Action Plan',
                         overall_average=overall_average, user_score=user_score,
                         description="""
It is a checklist for the steps or tasks you need to complete to achieve your goals. 
This can help students to know how it started and will be ended.

"""
                         )
self_assessment = Strategies(name='Self-Assessment',
                             overall_average=overall_average, user_score=user_score,
                             description="""
It is good for everyone's goal, especially students, as it can help them evaluate their knowledge, skills, 
and qualities in their learning process.

"""
                             )
feedback = Strategies(name='Feedback',
                      overall_average=overall_average, user_score=user_score,
                      description="""
The purpose of feedback in the assessment and learning process is to improve rather than reduce student performance. 
It is important that the process of giving feedback is a positive or at least a neutral learning experience for students.
Effective and relevant feedback also helps learners reflect on their learning styles and learning strategies so they can 
make adjustments to better progress through their learning stages. Effective feedback is now designed to determine how 
understanding learners differ for each individual and the rate at which skills are developing so they can plan next steps 
to achieve their learning goals. Determined.

"""
                      )

# Print all strategies
print(f"""
{time_management.name}
{time_management.description}

{jornaling.name}
{jornaling.description}

{self_regulation.name}
{self_regulation.description}

{procrastination.name}
{procrastination.description}

{personal_study.name}
{personal_study.description}

{external_extensive_research.name}
{external_extensive_research.description}

{reflective_practice.name}
{reflective_practice.description}

{team_work.name}
{team_work.description}

{process_thinking.name}
{process_thinking.description}

{action_plan.name}
{action_plan.description}

{self_assessment.name}
{self_assessment.description}

{feedback.name}
{feedback.description}


To go back to the main page, type m
""")
