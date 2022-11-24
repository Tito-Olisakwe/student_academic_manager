#!/usr/bin/python3
import strategy_page

# variables

updated_score = False
reflective_thinking_score = 0
learning_process_score = 0
reflective_thinking_summative_score = 0
learning_process_summative_score = 0

user_goal = 4.5


# class for micro-courses
class MicroCourse:
    def __init__(self, name, module, score, average):
        self.name = name
        self.module = module
        self.score = score
        self.average = average


# class for summatives
class Summative:
    def __init__(self, name, score, average):
        self.name = name
        self.score = score
        self.avarage = average


# the GPA for learning processes
def learning_process_average():

    micro_courses_score = (learning_process_score * 70) / 800
    summative_score = (
        learning_process_summative_score * 30) / 5
    Total = micro_courses_score + summative_score
    average = (Total * 5) / 100
    return round(average, 2)


# the GPA for Reflective thinking
def reflective_thinking_average():

    micro_courses_score = (reflective_thinking_score * 70) / 700
    summative_score = (
        reflective_thinking_summative_score * 30) / 5
    total = micro_courses_score + summative_score
    average = (total * 5) / 100
    return round(average, 2)


# The total GPA
def overall_gpa():
    overall_gpa = round((learning_process_average() +
                         reflective_thinking_average()) / 2, 2)
    return overall_gpa


# micro-courses objects
# Learning Processes
curiosity = MicroCourse(name='Curiosity', module='Learning Processes',
                        score=70, average=overall_gpa)

learning_goals = MicroCourse(name='Learning Goals', module='Learning Processes',
                             score=97, average=overall_gpa)

self_assessment = MicroCourse(name='Self Assessment', module='Learning Processes',
                              score=80, average=overall_gpa)

navigating_ambiguity = MicroCourse(name='Navigating Ambigiuty', module='Learning Processes',
                                   score=56, average=overall_gpa)

process_thinking = MicroCourse(name='Process Thinking', module='Learning Processes',
                               score=87, average=overall_gpa)

sourcing_discerningly = MicroCourse(name='Sourcing Discerningly', module='Learning Processes',
                                    score=98, average=overall_gpa)

documenting = MicroCourse(name='Documenting', module='Learning Processes',
                          score=75, average=overall_gpa)

organizing_with_principles = MicroCourse(name='Organizing with Principles', module='Learning Processes',
                                         score=84, average=overall_gpa)

# Reflective Thinking
motivation = MicroCourse(name='Motivation', module='Reflective Thinking',
                         score=40, average=overall_gpa)

procrastination = MicroCourse(name='Procrastination', module='Reflective Thinking',
                              score=65, average=overall_gpa)

reflective_practice = MicroCourse(name='Reflective Practice', module='Reflective Thinking',
                                  score=86, average=overall_gpa)

articulating_purpose = MicroCourse(name='Articulating Purpose', module='Reflective Thinking',
                                   score=59, average=overall_gpa)

portfolio_building = MicroCourse(name='Portfolio Building', module='Reflective Thinking',
                                 score=100, average=overall_gpa)

teaching_forward = MicroCourse(name='Teaching Forward', module='Reflective Thinking',
                               score=68, average=overall_gpa)

articulating_process = MicroCourse(name='Articulating process', module='Reflective Thinking',
                                   score=99, average=overall_gpa)


# summative objects
learning_processes_summative = Summative(
    name='Learning Processes', score=4.6, average=learning_process_average())

reflective_thinking_summative = Summative(
    name='Reflective Thinking', score=3.7, average=reflective_thinking_average())

reflective_thinking_summative_score = reflective_thinking_summative.score
learning_process_summative_score = learning_processes_summative.score

# user scores
learning_process_score = curiosity.score + learning_goals.score + \
    self_assessment.score + navigating_ambiguity.score \
    + process_thinking.score + sourcing_discerningly.score + \
    documenting.score + organizing_with_principles.score

reflective_thinking_score = motivation.score + procrastination.score + reflective_practice.score + \
    articulating_process.score + portfolio_building.score + \
    teaching_forward.score + articulating_process.score


# function that displays what the user will see for each micro course
def display_subject_details(subject_name, module_name, user_score, module_average, overall_gpa=overall_gpa()):
    print('\n\n')
    print(
        f'                {subject_name.upper()}      ---{module_name.upper()}\n')

    # if updated_score == False:
    #     print('The default score for each micro-course is 50%, update it with what you scored on lumen\n')

    print(f'Your score for {subject_name} is: {user_score}%')
    print(f'Your GPA for {module_name} is: {module_average}\n\n')
    print(f'Your overall GPA is: {overall_gpa}\n\n')
    print('The following strateg(y/ies) has been recommended to you based on your performance:\n')
    print(f'{strategy_page.suggest_strategy_subject(user_score= user_score)}\n')
    print(f'{strategy_page.suggest_strategy_overall(overall_average= overall_gpa)}\n')
    print(f'''
To see the description of every strategy, type s
To see more information on average, type a
To go back to the main page, type m
To end program, type e''')


# function for displaying module overview
def display_module_overview(module_name, user_summative_score, module_average):
    print('\n\n')
    print(f'                     {module_name.upper()}\n')

    # if updated_score == False:
    #     print('The default score for the summative is 2.5, update it after your summative has been graded by your learning coach\n')

    print('This is a list of all the micro-courses in this module and your scores:')

    if module_name == learning_processes_summative.name:
        print(f'''
    1. Curiosity                    ---{curiosity.score}%
    2. Learning goals               ---{learning_goals.score}%
    3. Self assessment              ---{self_assessment.score}%
    4. Navigating ambiguity         ---{navigating_ambiguity.score}%
    5. Process thinking             ---{process_thinking.score}%
    6. Sourcing discerningly        ---{sourcing_discerningly.score}%
    7. Documenting                  ---{documenting.score}%
    8. Organizing with principles   ---{organizing_with_principles.score}%
        ''')
        module_average = learning_process_average()
    elif module_name == reflective_thinking_summative.name:
        print(f'''
    1. Motivation                   ---{motivation.score}%
    2. Procrastination              ---{procrastination.score}%
    3. Reflective practice          ---{reflective_practice.score}%
    4. Articulating purpose         ---{articulating_process.score}%
    5. Portfolio building           ---{portfolio_building.score}%
    6. Teaching forward             ---{teaching_forward.score}%
    7. Articulating process         ---{articulating_process.score}%
        ''')
        module_average = reflective_thinking_average()

    print(f'Your summative score is {user_summative_score}\n\n')
    print(f'Your GPA for {module_name} is: {module_average}\n')
    print(f'Your overall GPA is: {overall_gpa()}\n\n')
    print(f'''
To see the description of every strategy, type s
To see more information on average, type a
To go back to the main page, type m
To end program, type e''')


def display_average():
    return f""""
Your overall gpa is {overall_gpa()}
Your learning processes gpa is {learning_process_average()}
Your reflective thinking gpa is {reflective_thinking_average()}

The goal you set for yourself at the begining of the term is {user_goal},
and your current average is {overall_gpa()}. 

Here are a few strategies that can assist you in your learning journey:
{strategy_page.self_assessment.name}
{strategy_page.self_assessment.description}

{strategy_page.process_thinking.name}
{strategy_page.process_thinking.description}

{strategy_page.personal_study.name}
{strategy_page.personal_study.description}

To see the description of every strategy, type s
To go back to the main page, type m
To end program, type e
"""
