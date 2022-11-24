#!/usr/bin/python3
import time
import introduction_page
import main_page
import credential_page
import strategy_page


print(introduction_page.introduction())

continue_from_introduction = input("Do you want to continue y/n ?").lower()
if continue_from_introduction == 'y':
    print(credential_page.take_credentials())
    time.sleep(5.0)
    print(main_page.display_main(main_page.user_name))
else:
    print("Goodbye then")

navigate = input("Where do you want to go? ").lower()
if navigate == 's':
    print(strategy_page.display_strategies())
