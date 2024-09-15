#1. List Manipulations (L = [11, 12, 13, 14])
#(i) Add 50 and 60 to L:
L = [11, 12, 13, 14]
L.append(50)
L.append(60)
print(L)

#(ii) Remove 11 and 13 from L:
L.remove(11)
L.remove(13)
print(L)

#(iii) Sort L in ascending order:
L.sort()
print(L) 

#(iv) Sort L in descending order:
L.sort(reverse=True)
print(L)

# (v) Search for 13 in L:
if (13 in L):
    print("13 in L")
else :
    print("13 not in L")
    
    
#(vi) Count the number of elements in L:

print(len(L))


#(vii) Sum all the elements in L:
total = 0
for i in L:
    total += i
print(total)

#(viii) Sum all ODD numbers in L:
odd_sum = 0
for i in L:
    if i % 2 != 0:
        odd_sum += i
print(odd_sum)

#(ix) Sum all EVEN numbers in L:
even_sum = 0
for i in L:
    if i % 2 == 0:
        even_sum += i
print(even_sum)


#x) Sum all PRIME numbers in L:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_sum = 0
for i in L:
    if is_prime(i):
        prime_sum += i
print(prime_sum)

#(xi) Clear all the elements in L:
L.clear()
print(L)

# (xii) Delete L:
del L


#2. Sum all items in a list without using inbuilt functions:
def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total

print(sum_list([1, 2, 3]))


#3. Multiply all items in a list without using inbuilt functions:
def multiply_list(lst):
    result = 1
    for i in lst:
        result *= i
    return result

print(multiply_list([1, 2, 3])) 

#4


#5. Dictionary Operations (
D = {1: 5.6, 2: 7.8, 3: 6.6, 4: 8.7, 5: 7.7}
#(i) Add new entry (key=8, value=8.8):
D[8] = 8.8
print(D)

#(ii) Remove key=2:
D.pop(2)
print(D)

#(iii) Check if key=6 is present:
print(6 in D)

#(iv) Count the number of elements in D:
print(len(D))

#(v) Sum all the values in D:
total = 0
for value in D.values():
    total += value
print(total)

#(vi) Update the value of key=3 to 7.1:
D[3] = 7.1
print(D)

#(vii) Clear the dictionary:
D.clear()
print(D)

#6. Set Operations (
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}
#(i) Add 55 and 66 to S1:
S1.add(55)
S1.add(66)
print(S1)

#(ii) Remove 10 and 30 from S1:
S1.remove(10)
S1.remove(30)
print(S1)

#(iii) Check if 40 is present in S1:
print(40 in S1)

#(iv) Find union of S1 and S2:
print(S1.union(S2))


#(v) Find intersection of S1 and S2:
print(S1.intersection(S2))

#(vi) Find S1 - S2:
print(S1.difference(S2))


#7 (ii) Print all prime numbers between 600 and 800:
for num in range(600, 801):
    if is_prime(num):
        print(num)


#(iii) Print numbers between 100 and 1000 divisible by 7 and 9:
for num in range(100, 1001):
    if num % 7 == 0 and num % 9 == 0:
        print(num)
        
        
#8. Display examination schedule from tuple
exam_st_date = (11, 12, 2014)
print(f"The examination will start from: {exam_st_date[0]}-{exam_st_date[1]}-{exam_st_date[2]}")


#9. Print numbers divisible by 5 from a list:
numbers = [10, 20, 33, 45, 55]
for num in numbers:
    if num % 5 == 0:
        print(num)
        
        
#10. Check if a number is even or odd using boolean variables:
def is_even(n):
    return n % 2 == 0

n = 10
print(is_even(n))


#11. Count occurrences of "Emma" in a string:
string = "Emma is a good developer. Emma loves Python."
count = 0
index = 0

while index < len(string):
    index = string.find("Emma", index)
    if index == -1:
        break
    count += 1
    index += len("Emma")

print(count)


#12. Create a new list with odd numbers from the first list and even numbers from the second list:
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

new_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]
print(new_list)