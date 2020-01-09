## Introduction to Python

Github Classroom Assignment Link : https://classroom.github.com/a/oUE_Og9m

Tasks Definition : https://docs.google.com/document/d/1V1gYEKLtOPYzZL7F9koaDVdgIlOXl_ALspjyzOZJN7Q/edit?usp=sharing

## Understanding Solid Principles
####Single Responsibility Principle 
A class should have one, and only one, reason to change. This implies that the class will have only one reason to change if it has only one responsibility.

#### Open-Closed Principle
Software entities such as classes, modules, functions e.t.c, should be open for extension, but closed for modification.  
For instance, a parent class(say Shapes) can be created with some attributes(sides) and methods(e.g getArea()) from which actual shape classes such as Rectangle or Circle can inherit from by extending the Shapes class. That way, the Shapes class will not be modified.  
#### Liskov Substitution Principle
It states Objects of a superclass shall be replaceable with objects of its sub classes without breaking the application. This principle extends the Open-Closed principle  described above.  
#### Interface Segregation Principle
Clients should not be forced to  depend upon interfaces that they do not use The goal of this principle is to reduce the side effects and frequency of required changes by splitting the software into multiple independent parts.  
#### Dependency Inversion Principle
High-level modules, which provide complex logic, should be easily reusable and unaffected by changes in low-level modules, which provide utility features. In order for this to be achieved, one needs to introduce an abstraction that decouples the high-level and low-level modules from each other.