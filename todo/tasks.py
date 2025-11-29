# functions that manage the tasks, the task-related functions for the application.

def add_task(tasks):   # this function will as it says, add tasks when called
  task = input("Enter a new task")   # this is the argument, which is the value put in the function
  tasks.append(task)
  print(f"Added: {task}")   # helps user understand task is added

# i didn't know functions can literally be that small, i learnt now the point of functions is so we don't need to write the same code over and over

# "pass" placeholder for future code, it basically tells python to ignore the function so an error message doesn't show up

def view_tasks(tasks):
  if len(tasks) == 0:
    print("There are no tasks.")
  else:
    print("Your tasks: ")
    for i in range(len(tasks)):    # this finds how many tasks there are in the list for us
      print(f"{i + 1}. {tasks[i]}")
      # this numbers the tasks
      # basically starts printing tasks from beginning to end in order with the [i]   

def complete_tasks(tasks):
  view_tasks(tasks)
  if len(tasks) == 0:
    return
  else:
    num = int(input("Enter task number to mark as done. "))
    if 1 <= num <= len(tasks):
       print("Task marked as done.")   # basically making sure that the user actually picked a valid task number from the list
    else:
      print("Invalid task number")
       
def delete_tasks(tasks):
  view_tasks(tasks)
  if len(tasks) == 0:
    return
  num = int(input("Enter task number to delete. "))
  if 1 <= num <= len(tasks):
     removed = tasks.pop(num - 1)   # .pop() removes it. minus one because python starts counting from 0, but the list visible to the user starts from 1. so it's to ensure it removes the correct task.
     print(f"Deleted {removed}.")    # f strings are called that cause they are used for formatting
  else:
     print("Invalid task number")

# parameter is the variable in the (). argument is the value that are sent to the function when it's called.

def edit_tasks(tasks):
  view_tasks(tasks)
  num = int(input("Which task do you want to edit? "))
  
  if 1 <= num <= len(tasks):
    tasks[int(num) - 1] = input("Insert your edited text: ")
  else:
    print("Invalid task number")
    
  # let user pick the task by indexing on the list (users number - 1)
  # allow them to edit it?
  # then resubmit to list?
  
  def prioritise_tasks(tasks):
    priority = int(input("Which task number do you want to prioritise? "))    # int cause it needs to be a number
    if 1 <= priority <= len(tasks):
      priority_task = tasks.pop(priority - 1)   # minus 1 cause python starts at 0 
      tasks.insert(0, priority_task)   # .insert basically pushes to front of list w/out replacing
    else:
      print("Invalid task number.")  

def reorder_tasks(tasks):
  # take the list make the user pick which task they wanna put somewhere else
  # somehow change the index ig
  # like pop() the task or whatever
  # then use .insert() to put it where user wants
