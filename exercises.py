# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

# Call the function and print each element
example_list_function()

# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # your code here

  #list named students = [ 3 elements ]
  students = ['CJ', 'Ali', 'Johnny']
  #create variable first_student for the second students name in the element
  first_student = students[1]
  #create variable last_student for the last student
  last_student = students[-1]
  return first_student, last_student


# Call the function and print the result
print('Exercise 1:', manage_students())



# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

foods = ('pizza', 'mac & cheese', 'chicken')

def combine_foods():
    # your code here
#tuple foods = ( food1, food2, food3)
  
#empty_meal= ""
  meal = ''
  #loop over foods to add it to meals
  for food in foods:
     meal += food + ' '

  #had to look up lines 58 + 61
  return meal.strip()
  
# Call the function and print the result
print('Exercise 2:', combine_foods())


# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    # your code here
  #tuple for last_two_foods = ()
  last_two_foods = foods[-2:]
  
  #slice method
  return last_two_foods
# Call the function and print the result
print('Exercise 3:', slice_foods())




# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

#moved home_town dictionary above function to use globally for 4 & 5.. should I have done this a different way?
home_town = {
      'city': 'Taunton',
      'state': 'Massachusetts',
      'population': 60000,
      }

def hometown_info():
    # your code here

    #dictionary home_town {city state population}
    
    # home_town_message = home_town
    #home_town_message = home_town
    home_town_message = f'I was born in {home_town["city"]}, {home_town["state"]}, population of {home_town["population"]:,.0f} people.'
    # home_town_message = 'message'
    return home_town_message
# Call the function and print the result
print('Exercise 4:', hometown_info())


# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

def list_home_town_items():
    # your code here
    #define home_town dictionary from above in new function?

  #home_town_items = []
  home_town_items = []
  for key, value in home_town.items():  
    home_town_items.append(f'{key} = {value}')

  return home_town_items
  #for loop over hometown dictionary .append to home_town_items: 'key = value'
# Call the function and print the result
print('Exercise 5:', list_home_town_items())
