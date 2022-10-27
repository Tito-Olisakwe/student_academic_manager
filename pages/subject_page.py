#!/usr/bin/python3

# This page will be displayed when the user navigates from the main page to a particular subject.

# some variables to test things out
subject_name = 'course'
module_name = 'module'
user_score = 50
user_summative_score = 2.5
module_average = 2.5
overall_average = 2.5
recommended_strategy = 'strategy'
updated_score = False


# class for micro-courses
class MicroCourse:
    def __init__(self, name, module, score, average, strategy):
        self.name = name
        self.module = module
        self.score = score
        self.average = average
        self.strategy = strategy


# class for summatives
class Summative:
    def __init__(self, name, score, average):
        self.name = name
        self.score = score
        self.avarage = average


# function that displays what the user will see for each micro course
def display_subject_details(subject_name, module_name, user_score, module_average=module_average, overall_average=overall_average):
    print('\n\n')
    print(
        f'                {subject_name.upper()}      ---{module_name.upper()}\n')

    if updated_score == False:
        print('The default score for each micro-course is 50%, update it with what you scored on lumen\n')

    print(f'Your score for {subject_name} is: {user_score}%')
    print(f'Your GPA for {module_name} is: {module_average}\n\n')
    print(f'Your overall GPA is: {overall_average}\n\n')
    print('The following strateg(y/ies) has been recommended to you based on your performance:\n')
    print(f'{recommended_strategy}\n')
    print(f'To go back to the main page, type: m')
    print(f'To view {module_name} overview, type: s')


# function for displaying module overview
def display_module_overview(module_name, user_summative_score, module_average):
    print('\n\n')
    print(f'                     {module_name.upper()}\n')

    if updated_score == False:
        print('The default score for the summative is 2.5, update it after your summative has been graded by your learning coach\n')

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

    print(f'Your summative score is {user_summative_score}\n\n')
    print(f'Your GPA for {module_name} is: {module_average}\n')
    print(f'Your overall GPA is: {overall_average}\n\n')
    print(f'To go back to the main page, type: m')


# micro-courses objects
# Learning Processes
curiosity = MicroCourse(name='Curiosity', module='Learning Processes',
                        score=user_score, average=overall_average, strategy=recommended_strategy)

learning_goals = MicroCourse(name='Learning Goals', module='Learning Processes',
                             score=user_score, average=overall_average, strategy=recommended_strategy)

self_assessment = MicroCourse(name='Self Assessment', module='Learning Processes',
                              score=user_score, average=overall_average, strategy=recommended_strategy)

navigating_ambiguity = MicroCourse(name='Navigating Ambigiuty', module='Learning Processes',
                                   score=user_score, average=overall_average, strategy=recommended_strategy)

process_thinking = MicroCourse(name='Process Thinking', module='Learning Processes',
                               score=user_score, average=overall_average, strategy=recommended_strategy)

sourcing_discerningly = MicroCourse(name='Sourcing Discerningly', module='Learning Processes',
                                    score=user_score, average=overall_average, strategy=recommended_strategy)

documenting = MicroCourse(name='Documenting', module='Learning Processes',
                          score=user_score, average=overall_average, strategy=recommended_strategy)

organizing_with_principles = MicroCourse(name='Organizing with Principles', module='Learning Processes',
                                         score=user_score, average=overall_average, strategy=recommended_strategy)

# Reflective Thinking
motivation = MicroCourse(name='Motivation', module='Reflective Thinking',
                         score=user_score, average=overall_average, strategy=recommended_strategy)

procrastination = MicroCourse(name='Procrastination', module='Reflective Thinking',
                              score=user_score, average=overall_average, strategy=recommended_strategy)

reflective_practice = MicroCourse(name='Reflective Practice', module='Reflective Thinking',
                                  score=user_score, average=overall_average, strategy=recommended_strategy)

articulating_purpose = MicroCourse(name='Articulating Purpose', module='Reflective Thinking',
                                   score=user_score, average=overall_average, strategy=recommended_strategy)

portfolio_building = MicroCourse(name='Portfolio Building', module='Reflective Thinking',
                                 score=user_score, average=overall_average, strategy=recommended_strategy)

teaching_forward = MicroCourse(name='Teaching Forward', module='Reflective Thinking',
                               score=user_score, average=overall_average, strategy=recommended_strategy)

articulating_process = MicroCourse(name='Articulating process', module='Reflective Thinking',
                                   score=user_score, average=overall_average, strategy=recommended_strategy)


# summative objects
learning_processes_summative = Summative(
    name='Learning Processes', score=user_summative_score, average=module_average)  # remember to change score and average

reflective_thinking_summative = Summative(
    name='Reflective Thinking', score=user_summative_score, average=module_average)


# test
""" display_module_overview(module_name=reflective_thinking_summative.name,
                        user_summative_score=reflective_thinking_summative.score, module_average=reflective_thinking_summative.avarage)
 """
