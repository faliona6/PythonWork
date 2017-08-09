Author: Mikayla Konst
Date: 8-3-2017

Contents:

random_keys.txt
  File of randomly generated keys - one for each pair of students.
  This file is required by the key.py script.
random_keys.py
  The script that was used to generate the file random_keys.txt
key.py
  Run this script to find out the key two students should use.
  The order of the students doesn't matter.
  This script must be located in the same folder as random_keys.txt to work.
  key.py [Student 1] [Student 2]
conversions.py
  How to convert letters <--> ascii <--> binary.
  For the project, you'll probably want a function that converts directly
  between letters and binary without having to go through ascii.
xor.py
  My solution to the problem. Feel free to run it to see what is supposed to
  happen, but DO NOT look at the source code until you have solved the problem
  for yourself. Use the -e option for encryption, the -d option for encryption.
  To run:
  key.py [Student 1] [Student 2] | xor.py [input-file] -[e|d] > [output-file]
