# useroop.py
"""
Desiree Thompson - Module 2 - January 23, 2023

Objective is to practice using Object-Oriented Programming using the PyBuddies included in the code. 

I will include differnt attributes that share common methods to make changes to the PyBuddies. 

The domain I am focused on is dogs. 


"""
# first, import helpful modules to make our job easier

import datetime
from enum import Enum
import random
import statistics



class Species(Enum):
    DOG = 1
    CAT = 2
    ELF = 3
    ORC = 4


class PyBuddy:
    """ PyBuddy class for creating a study buddy."""

    def __init__(self, name, species, num_legs, color, weight_kgs, is_available, skill_list, children_number, home_area, average):
        """ Built-in method to create a new instance."""
        self.name = name
        self.species = species
        self.num_legs = num_legs
        self.color = color
        self.weight_kgs = weight_kgs
        self.is_available = is_available
        self.skill_list = skill_list
        self.create_date = datetime.datetime.now()
        self.children_number = children_number
        self.home_area = home_area
        self.average = average

    def __str__(self):
        """Built-in method to return a string describing this instance"""
        s0 = f"I'm {self.name}.\n"
        s1 = f"I'm a {self.species} with {self.num_legs} legs.\n"
        s2 = f"I weigh {self.weight_kgs:.2f} kgs.\n"
        s3 = f"I'm the color {self.color}.\n"
        s4 = f"I've been alive for {self.get_age_string()}.\n"
        s5 = f"I've been alive for {self.color}.\n"
        if self.is_available:
            s5 = "I'm available for tutoring.\n"
        else:
            s5 = "I'm already helping others learn Python.\n"

        s6 = "I know:\n"

        s7 = ""
        for skill in self.skill_list:
            s7 = s7 + f"  - {skill}\n"
            
        s8 = f"I have {self.get_children_number()} child(ren).\n"
        s9 = f"My home has an area of {self.get_home_area()} feet.\n"
        s10 = f"On average I train {self.get_mean():.0f} {self.species}'s per day.\n"      

        s = s0 + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10
        return s

    def get_age_string(self):
        """Return the age as a string."""
        start = self.create_date
        end = datetime.datetime.now()
        duration = end - start
        ageString = str(duration)
        return ageString
    
    def get_children_number(self):
        """Returns a random number of children"""
        for children in range(1):
            children_number = random.randrange(1, 9)
            return children_number
        
    def get_home_area(self):
        """Returns the area of a rectangle"""
        length = random.randrange(1, 100)
        width = random.randrange(1, 100)
        home_area = length * width
        return home_area      
    
    def get_mean(self):
        """Returns the average number of people helped each day"""
        totals = [2, 5, 6, 3, 7 , 8, 1]
        average = statistics.mean(totals)
        return average
        
                
    def display_welcome(self):
        print()
        print("Welcome, I'm a new PyBuddy.\n")
        # print using our built-in to string method
        print(self.__str__())

        final_message = """

        You'll need curiousity, the ability to search the web,
        and the tenacity and resourcefulness
        to solve all kinds of challenges.

        Let's get started!

        """
        print(final_message)
        
        
        
        
        
        
        
        
        


# -------------------------------------------------------------
# Call some functions and execute code!

# if this is the main file being run

if __name__ == "__main__":
    # Create an instance of a PyBuddy
    alice = PyBuddy(
        "Alice",
        Species.DOG,
        4,
        "brown",
        8.123456,
        True,
        ["Git", "GitHub", "Python", "Markdown", "VS Code"],
        "",
        "",
        ""        
    )

    # Call the buddy's welcome() method
    alice.display_welcome()


    # Create another instance of a PyBuddy
    # using named arguments so it's clear what we're doing
    rex = PyBuddy(
        name="Rex",
        species=Species.DOG,
        num_legs=4,
        color="black",
        weight_kgs=10.437241,
        is_available=True,
        skill_list=["Git", "GitHub", "Python", "Markdown", "VS Code"],
        children_number="",
        home_area="",
        average=""
    )

    rex.display_welcome()
    
    
    
    
    
    
    
    
    
    
    
    
    