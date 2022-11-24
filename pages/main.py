#!/usr/bin/python3
import introduction_page
import main_page
import credential_page
import strategy_page
import value


print(introduction_page.introduction())

continue_from_introduction = input("Do you want to continue y/n ?").lower()
if continue_from_introduction == 'y':
    print(credential_page.take_credentials())
    print(main_page.display_main(main_page.user_name))
else:
    print("Goodbye then")
    quit()


navigate = input("Where do you want to go? ").lower()

while navigate != 'e':
    if navigate == 's':
        print(strategy_page.display_strategies())
        navigate = input("Where do you want to go? ").lower()
    elif navigate == 'a':
        print(value.display_average())
        navigate = input("Where do you want to go? ").lower()
    elif navigate == 'm':
        print(main_page.display_main(main_page.user_name))
        navigate = input("Where do you want to go? ").lower()

    elif navigate == '1':
        print(value.display_subject_details(subject_name=value.curiosity.name, module_name=value.curiosity.module,
                                            user_score=value.curiosity.score, module_average=value.learning_process_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '2':
        print(value.display_subject_details(subject_name=value.learning_goals.name, module_name=value.learning_goals.module,
                                            user_score=value.learning_goals.score, module_average=value.learning_process_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '3':
        print(value.display_subject_details(subject_name=value.self_assessment.name, module_name=value.self_assessment.module,
                                            user_score=value.self_assessment.score, module_average=value.learning_process_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '4':
        print(value.display_subject_details(subject_name=value.navigating_ambiguity.name, module_name=value.navigating_ambiguity.module,
                                            user_score=value.navigating_ambiguity.score, module_average=value.learning_process_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '5':
        print(value.display_subject_details(subject_name=value.process_thinking.name, module_name=value.process_thinking.module,
                                            user_score=value.process_thinking.score, module_average=value.learning_process_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '6':
        print(value.display_subject_details(subject_name=value.sourcing_discerningly.name, module_name=value.sourcing_discerningly.module,
                                            user_score=value.sourcing_discerningly.score, module_average=value.learning_process_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '7':
        print(value.display_subject_details(subject_name=value.documenting.name, module_name=value.documenting.module,
                                            user_score=value.documenting.score, module_average=value.learning_process_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '8':
        print(value.display_subject_details(subject_name=value.organizing_with_principles.name, module_name=value.organizing_with_principles.module,
                                            user_score=value.organizing_with_principles.score, module_average=value.learning_process_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '9':
        print(value.display_subject_details(subject_name=value.motivation.name, module_name=value.motivation.module,
                                            user_score=value.motivation.score, module_average=value.reflective_thinking_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '10':
        print(value.display_subject_details(subject_name=value.procrastination.name, module_name=value.procrastination.module,
                                            user_score=value.procrastination.score, module_average=value.reflective_thinking_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '11':
        print(value.display_subject_details(subject_name=value.reflective_practice.name, module_name=value.reflective_practice.module,
                                            user_score=value.reflective_practice.score, module_average=value.reflective_thinking_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '12':
        print(value.display_subject_details(subject_name=value.articulating_purpose.name, module_name=value.articulating_purpose.module,
                                            user_score=value.articulating_purpose.score, module_average=value.reflective_thinking_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '13':
        print(value.display_subject_details(subject_name=value.portfolio_building.name, module_name=value.portfolio_building.module,
                                            user_score=value.portfolio_building.score, module_average=value.reflective_thinking_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '14':
        print(value.display_subject_details(subject_name=value.teaching_forward.name, module_name=value.teaching_forward.module,
                                            user_score=value.teaching_forward.score, module_average=value.reflective_thinking_average()))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '15':
        print(value.display_subject_details(subject_name=value.articulating_process.name, module_name=value.articulating_process.module,
                                            user_score=value.articulating_process.score, module_average=value.reflective_thinking_average()))
        navigate = input("Where do you want to go? ").lower()

    elif navigate == '16':
        print(value.display_module_overview(module_name=value.learning_processes_summative.name,
              user_summative_score=value.learning_processes_summative.score, module_average=value.learning_processes_summative.avarage))
        navigate = input("Where do you want to go? ").lower()
    elif navigate == '17':
        print(value.display_module_overview(module_name=value.reflective_thinking_summative.name,
              user_summative_score=value.reflective_thinking_summative.score, module_average=value.reflective_thinking_summative.avarage))
        navigate = input("Where do you want to go? ").lower()
    else:
        break
print('Good bye, come back soon')
