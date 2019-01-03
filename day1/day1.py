# day1.py

# In-line list comprehension
print([number for number in range(3)])
# Has its own scope
# First variable can have transformations
print([str(even) for even in range(10) if even % 2 == 0])


# Dictionaries
# key-value pair "hash" table
my_dic = {
    "cheese" : "mouse",
    "wood" : "tree",
}

print(my_dic)
print(my_dic["cheese"])


# Objects
# self makes not-classwide
class student:
    def __init__(self,name):
        self.name = name
        pass
    
    def __str__(self):
        return self.name

    def __eq__(self):
        return True

vince = student("Vince")

print(vince)


class math_student(student):
    favorite_class = "math"

becky = math_student("becky")

print(becky)
print(becky.favorite_class)



# TODO: Install Jupyter
