#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
lst = [0,1]
even = []
repeats = input("How many digits?: ")
repeats = int(repeats)
x = 0

while(repeats > x):
    x += 1
    lst.append(lst[-1] + lst[-2])
lst.pop(0)
lst.pop(0)
print(lst)
x = 0
while(x < len(lst)):
    if(lst[x] % 2 == 0):
        even.append(lst[x])
    x += 1
print(sum(even))
        
    
    