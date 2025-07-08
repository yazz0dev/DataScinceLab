l=input("Enter Numbers seperated by space: ").split()
uniq = [] 
for x in l:
    if x not in uniq:
        uniq.append(x)
print("Unique elements are:", uniq)