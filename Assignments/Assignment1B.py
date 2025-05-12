#Assignment 1B
#take a no. of list and print even and odd count
numbers = input("Enter numbers separated by space: ").split()
numbers = [int(num) for num in numbers]
even =0
odd =0 

for n in numbers:
    if int(n) % 2:
        even +=1 
    else:
        odd +=1

print(f"{even}")
print(f"{odd}")