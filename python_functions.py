# Function Definition 
def newfunc(str):
    "This should print a passed string into this function"
    print(str)
    return
# Calling the newfunc function
newfunc("1st fuction call")
newfunc("2nd function call") 

# Function 2
def changeme(mylist):
    "This changes a passed list into this function"
    mylist.append([1, 2, 3, 4])
    print("Values inside the fuction are ", mylist)
    return
# Calling the changeme function
mylist = [20, 6, 8, 9, 17]
changeme(mylist)
print("Values outside the function are", mylist)

###########################################################
