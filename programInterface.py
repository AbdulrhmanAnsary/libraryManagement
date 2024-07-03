#!/bin/python

import os
import time

class Interface:
  def __init__(self):
    pass

  def clear_screen(self, seconds=0):
    time.sleep(seconds)
    os.system("cls" if os.name == "nt" else "clear")

  def print_title(self, title):
    print("\n\t", end="")

    for i in range(len(str(title))):
      print("=", end="")
    print(f"\n\t{title}")
    print("\t", end="")

    for i in range(len(str(title))):
      print("=", end="")
    print("\n")
