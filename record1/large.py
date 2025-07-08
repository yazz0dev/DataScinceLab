print("Enter a list of numbers separated by spaces:")
l = input()
l=[int(x) for x in l.split()] 
m=l[0] 
for i in l:
    if i > m:
        m = i 
print("The largest number is:", m)
print("The largest number using max():", max(l))