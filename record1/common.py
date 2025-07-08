#write a program that takes 2 list and return true if they have atleast one common member. 

def iscommon(l1,l2):
    for i in l1:
        if i in l2:
            return True

print("Enter lists of numbers separated by spaces.")
l1 = input("first list: ").split()
l2 = input("second list: ").split()

if iscommon(l1, l2):
    print("The lists have at least one common member.")
else:
    print("The lists do not have any common members.")