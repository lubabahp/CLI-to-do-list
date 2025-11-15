# this is the main functions that executes everything, the whole program, by calling functions from our other scripts of code.
# main() will be used a lot during the creation of actual python apps.
# tasks.py and menu.py are in separate files: this is writing clean, modular code.
# a global variable is one defined outside the function.

from tasks import *
from menu import *
 
def main():
  tasks = []  # tasks is empty.

  while True:    # while loop.
    show_menu()
    choice = user_picks_option()
    # we called two functions

    if choice == "1":
      view_tasks(tasks)
    elif choice == "2":
      add_tasks(tasks)  # tasks is the argument
    elif choice == "3":
      complete_tasks(tasks)
    elif choice == "4":
      delete_task(tasks)  
    elif choice == "5":
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")  
main()      
