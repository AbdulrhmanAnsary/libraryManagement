#!/bin/python

import sys
sys.path.append("/data/data/com.termux/files/home/projects/myCodes/pythonCodes")
from programInterface import *

class LibraryManagement(Interface):
  catalog = {}
  ISBN = "" # International Standard Book Number
  title = ""
  author = ""
  available = True

  def __init__(self):
    pass

  def print_minue(self):
    print(" Minue:")
    print("  1. Add Book")
    print("  2. Check out Book")
    print("  3. Check In Book")
    print("  4. List Books")
    print("  5. Exit")

  def add_book(self):
    self.ISBN = input("\n Enter ISBN: ")
    self.title = input(" Enter title: ")
    self.author = input(" Enter author: ")

    if self.ISBN not in self.catalog.keys():
      self.catalog[self.ISBN] = [self.title, self.author, self.available]
    else:
      print(f"\n The ISBN '{self.ISBN}' is not available")

  def print_addition(self):
    print(f"\n Book '{self.catalog[self.ISBN][0]}'", end=" ")
    print(f"by {self.catalog[self.ISBN][1]}", end=" ")
    print(f"added to the catalog with ISBN {self.ISBN}")

  def print_catalog(self):
    print("\n Library Catalog:")

    for key in self.catalog:
      print(f"  ISBN: {key}, Title: {self.catalog[key][0]}, Author: {self.catalog[key][1]}, Available: {self.catalog[key][2]}")

  def check_out_book(self):
    ISBN = input("\n Enter ISBN to check out: ")

    if self.catalog[ISBN][2] == True:
      self.catalog[ISBN][2] = False
      print(f"\n Book '{self.catalog[ISBN][0]}' checked out successfully.")
    else:
      print("\n Sory, the book is currently checked out.")

  def check_in_book(self):
    ISBN = input("\n Enter ISBN to check in: ")

    if self.catalog[ISBN][2] == False:
      self.catalog[ISBN][2] = True
      print(f"\n Book '{self.catalog[ISBN][0]}' checked in successfully.")
    else:
      print("\n The book is already checked in.")

my_library = LibraryManagement()
user_choice = 0

while user_choice != 5:
  try:
    my_library.print_title("Library Management")
    my_library.print_minue()
    user_choice = int(input("\n "))
    user_continue = ""
    my_library.clear_screen()

    # Add book
    if user_choice == 1:
      while user_continue != "n":
        my_library.add_book()
        my_library.print_addition()
        user_continue = input(" Do you want to add another book? (y/n): ").strip(" ").lower()

        if user_continue not in ["y", "n"]:
          raise NameError(f"\n NameError: name '{user_continue}' is not defined")
        my_library.clear_screen()
    # Check out book
    elif user_choice == 2:
      while user_continue != "n":
        my_library.check_out_book()
        user_continue = input(" Do you want to check out another book? (y/n): ").strip(" ").lower()

        if user_continue not in ["y", "n"]:
          raise NameError(f"\n NameError: name '{user_continue} is not defined")
        my_library.clear_screen()
    # Check in book
    elif user_choice == 3:
      while user_continue != "n":
        my_library.check_in_book()
        user_continue = input(" Do you want to check in another book? (y/n): ").strip(" ").lower()

        if user_continue not in ["y", "n"]:
          raise NameError(f"\n NameError: name '{user_continue} is not defined")
        my_library.clear_screen()
    # Print the catalog
    elif user_choice == 4:
      my_library.print_catalog()
    # User choice not in (1-5)
    elif user_choice > 5:
      raise IndexError(f"\n IndexError: '{user_choice}' is out of range")
  except ValueError as VE:
    print("\n ValueError: ", VE)
  except IndexError as ID:
    print(ID)
  except NameError as NE:
    print(NE)
  except KeyError:
    print("\n Book not found in the catalog")

print(" Exit the program...")
time.sleep(2)
