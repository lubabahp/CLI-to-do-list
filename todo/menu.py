# functions that show menu and get user input

def show_menu():   # this is our menu, we can call the funtion so the user sees their options.
  print("Your To-do List")
  print("1. View tasks")
  print("2. Add tasks")
  print("3. Complete task")
  print("4. Delete task")
  print("5. Exit")

def user_picks_option():
  return input("Pick an option from 1 to 5: ")
  # return means the input goes back to the function and will come when the function is called
