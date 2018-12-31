1. What’s a class?
   A class is a data structure that can be replicated. 
2. What’s an instance?
   An instance is a copy of a class with its own information. 
3. What’s the relationship between a class and an instance?
   An instance is a specific use of a class.
4. What’s the Python syntax used for defining a new class?
   ```python3
   class MyClass:
       def __init__(self):
           # do stuff
   ```
5. What’s the spelling convention for a class name?
   pep says that we should use the "CapWords" convention. 
6. How do you instantiate, or create an instance of, a class?
   `myInstance = MyClass()`
7. How do you access the attributes and behaviors of a class instance?
   `myInstance.attribute = x`
   `myInstance.myMethod()`
8. What’s a method?
   A method is a function tied to a class. 
9. What’s the purpose of self?
   Self refers to the specific instance, as opposed to the class.
10. What’s the purpose of the __init__ method?
    `__init__` is ran when the instance is initiated. 
11. Describe how inheritance helps prevent code duplication.
    Inheritence helps us not have to rewrite code for a similar/more-specific structure. 
12. Can child classes override properties of their parents?
    I'm gonna go with yes.
