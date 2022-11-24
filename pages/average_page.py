#!/usr/bin/python3
# This page will be displayed when a user wants to calculate their average


user_goal = 4.5

learning_process_score = curiosity.score + learning_goals.score + \
    self_assessment.score + navigating_ambiguity.score \
    + process_thinking.score + sourcing_discerningly.score + \
    documenting.score + organizing_with_principles.score

reflective_thinking_score = motivation.score + procrastination.score + reflective_practice.score + \
    articulating_process.score + portfolio_building.score + \
    teaching_forward.score + articulating_process.score


# the GPA for learning processes
def learning_process_average():
    micro_courses_score = (learning_process_score * 70) / 800
    summative_score = (
        learning_processes_summative.score * 30) / 5
    Total = micro_courses_score + summative_score
    average = (Total * 5) / 100
    return average


# the GPA for Reflective thinking
def reflective_thinking_average():
    micro_courses_score = (reflective_thinking_score * 70) / 700
    summative_score = (
        reflective_thinking_summative.score * 30) / 5
    total = micro_courses_score + summative_score
    average = (total * 5) / 100
    return average


# The total GPA
Overall_gpa = round((learning_process_average() +
                    reflective_thinking_average()) / 2, 2)
print(f"Your overall gpa is {Overall_gpa}")
