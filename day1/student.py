# student.py

class student:
    def __init__(self,name,classes):
        self.name = name
        self.classes = classes

    def __repr__(self):
        return_str = self.name
        for single_class in self.classes:
            return_str += " " + single_class

    def __str__(self):
        return self.name

    def __len__(self):
        return len(classes)

    def __getitem__(self,position):
        if position < len(self):
            return self.classes[position]

    def __reversed__(self):
        return reversed(self.classes)

    def __eq__(self,other):
        return repr(self) == repr(other)

    def __lt__(self,other):
        return self.name < other.name

    def __add__(self,other):
        self.classes += other.classes

    
        
