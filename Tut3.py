# 1. Difference between a number and 17:

def difference(n):
    if n > 17:
        return 2 *(n - 17)
    else:
        return 17-n

print(difference(10))  
print(difference(20))  

# 2. Test if a number is within 100 to 1000 or 2000:
def test_range(n):
    if 100 <= n <= 1000 or n == 2000:
        return True
    else:
        return False

print(test_range(540))  
print(test_range(1503))  



#3. Reverse a string:

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("hello"))


# 4. Count the number of upper and lower case letters:
def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if 'A' <= char <= 'Z':
            upper_count += 1
        elif 'a' <= char <= 'z':
            lower_count += 1
    print("uppercase =",upper_count , "lowercase =",lower_count)
    return upper_count, lower_count

upper, lower = count_case("HelloWorld")


#5. Return a list with distinct elements:

def distinct_elements(lst):
    distinct_list = []
    for element in lst:
        if element not in distinct_list:
            distinct_list.append(element)
    return distinct_list

print(distinct_elements([1, 2, 2, 3, 4, 4, 5])) 


#6. Print even numbers from a list:

def even_numbers(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))



# 7. Access a function inside a function:

def outer_function():
    def inner_function():
        return "Hello from the inner function!"
    
    return inner_function()

print(outer_function())


#8. Function attributes to display argument names:

def student(name, age):
    return

student.names = ['name', 'age']
print("Function argument names:", student.names) 

#9. Student class with new attribute:

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None

    def display_attributes(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.student_name}")
        print(f"Class: {self.student_class}")

student = Student(1, "John")
student.student_class = "10th Grade"
student.display_attributes()


#10. Student instances with attributes:

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student1 = Student(1, "John")
student2 = Student(2, "Jane")

print(f"Student 1: ID: {student1.student_id}, Name: {student1.student_name}")
print(f"Student 2: ID: {student2.student_id}, Name: {student2.student_name}")


#11. Circle class to compute area and perimeter:

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.1416 * self.radius

circle = Circle(5)
print(f"Area: {circle.area()}")       
print(f"Perimeter: {circle.perimeter()}")


#12. Class with methods to get and print a string:

class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def get_String(self):
        self.input_string = input("Enter a string: ")

    def print_String(self):
        print(self.input_string.upper())

string_obj = StringManipulator()
string_obj.get_String()  
string_obj.print_String()