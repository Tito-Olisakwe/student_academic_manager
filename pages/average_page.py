#!/usr/bin/python3

# This page will be displayed when a user wants to calculate their average

# the GPA for learning processes

class learning_processes:

    studentScore = curiosity.score + learning_goals.score + \
        self_assessment.score + navigating_ambiguity.score
    + process_thinking.score + sourcing_discerningly.score + \
        documenting.score + organizing_with_principles.score

    def GPA():
        MicroCourses_P = (studenScore * 70) / 800
        Summative_P = (studentScore * 30) / 5
        Total = MicroCourses_p + Summative_p
        average = (Total * 5) / 100
        print(f"The learning process GPA = {average.GPA()}")


# the GPA for Reflective thinking
class reflective_thinking:
    userScore = motivation.score + procrastination.score + reflective_practice.score + \
        articulating_process.score + portofolia_building.score + \
        teaching_forward.score + articulating_process.score

    def Averag():
        microcourse_per = (userScore * 70) / 700
        summative_per = (userScore * 30) / 5
        total = microcourse_per + summative_per
        gpa = (total * 5) / 100

        print(f"the reflective thinking GPA = {gpa.Averag()}")


# The total GPA
Overall_gpa = (average.GPA() + gpa.Averag()) / 2
print(f"Your overall gpa is {Overall_gpa}")
