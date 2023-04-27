# 1:

'''
Most commonly use datatypes in python:-
1) Int
2) string
3) Float
4) Dictionary
'''

# 2:-

'''
Creating variables along with datatype:-
'''

# Python is a smart language and we dont need to declare the datatype explicitly as it catches automatically
a = 10  #int
b = "Srushti" #string
c = 40.02 #float
d = {             
    "name": "Srushti",
    "roll no":40
}  #dictionary


# 3:- 

'''
Use of print function:-
'''

print(f"Int: {a}")
print(f"String: {b}")
print(f"Float: {c}")
print(f"Dictionary: {d}")

# Note:- Here 'f' means formatter in python use to print the variables and string according to user. It is most widely user everywhere. So srushti you are going to use it from today onwards.


# 4: 

'''
Creating a function
'''

# For creating a function always use 'def' keyword

def propose(name):
    print(f"I love you {name} ji")

# 5:

'''
Passing the values and printing
'''

name = "Srushti"
propose(name)



