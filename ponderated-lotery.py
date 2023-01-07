"""
This program does a "ponderated lotery" to select a person between multiple people, giving more posibilities to win to the person with "more weight".
Some code was taken from the internet and adapted acordingly to the necessities I considered I had.
"""

import random
from datetime import datetime

# Time seed for random number generation (try to make it more "random")
random.seed(datetime.now().timestamp())

# All the participants
people_dict = {
    1: "Juan",
    2: "Peter",
    3: "John",
    4: "Gohan",
    5: "Sara",
    6: "Daniel",
    7: "Paula",
    8: "Erika",
    9: "Bernard",
    10: "Zuko",
    11: "Liliana",
    12: "Luis"
}
  
# Keys for the people_dict and weights of each person (from 1 to 10)
sampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
weights_tuple = (8, 8, 9, 9, 9, 8, 8, 9, 9, 10, 9, 10)
  

# Get most frecuent element from a generated list
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num


# Select the winner
def make_choice():
    randomList = random.choices(
      sampleList, weights=weights_tuple, k=len(weights_tuple))
      
    chosen_number = most_frequent(randomList)
    print(people_dict[chosen_number])


make_choice()
