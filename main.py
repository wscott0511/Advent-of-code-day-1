# these are probably useless
import sys
import math
import os

# open the input file as read only
input_file = open("input1.txt","r")

# initialize a total at 0
total = 0

# go through the file and for every line take the number and do the shit
for line in input_file:
  # input files store everything as a string so we have to change to int
  temp = int(line)
  #Round down 
  temp = math.floor(temp / 3) - 2
  
  # save the temp but copy it to be used below
  temps_gas = temp

  # while temps_gas isn't less than or equal to zero we still have more gas to find
  while temps_gas > 0:
    # math bitch
    temps_gas = math.floor(temps_gas / 3) - 2
    if temps_gas <= 0:
      #if the temp gas is greater than 0 continue to run this code
      temps_gas = 0
    else:
      # if the temps_gas is less than 0 add it to total
      temp += temps_gas
  
  #add temp to the total
  total += temp
  
#print the total
print(total)