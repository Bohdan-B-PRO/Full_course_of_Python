print('Hello World')
print(1 + 2, 10 - 2, 10 - 20, 10 + 20, 10 / 2, 10 // 2, 1.5 + 2.7, 10 / 3, 10 // 3)
print(2 + 2 * 2, 20 + 10 - 5, (1 + 2) * (3 + 4), 13 / 4, 13 // 4, 13 % 4, 20 / 7, 20 % 7)
print('Hello ' + 'Wprld')
print('Hello ' + ' ' + 'World')
print("Hello World " * 2)
my_var = 42
a = 1
b = 2
c = a + b
word = "Hello"
name = "Bob"
line = word + " " + name
condition = True

print(my_var, c, word + ' ' + "John", word + ' ' + name, line, a > b, a == 1, b == 2, "hello" == "Hello")

print("Hi")
if condition:
    print("condition is True", end=" ")
    print("____")
print("Bye")

MIN_AGE = 18
age = 15

if age >= MIN_AGE:
    print("Okd enough")
else:
    print("too young")

MIN_AGE = 18
age = 25

if age >= 21:
    print("evething allpw")
elif age >= 18:
    print("good to go")
else:
    print("too young")

percentage = 101
if percentage > 100:
    print("Is not possible")
elif percentage == 100:
    print("100% is unbelievable")
elif percentage >= 80:
    print("Great")
elif percentage >= 60:
    print("Very good")
elif percentage >= 40:
    print("ok")
elif percentage >= 20:
    print("Bad")
else:
    print("Did even try")

my_list = [1, 2, 3, "Four", 5.0, True, False]
print(my_list[3])
print(len(my_list))
print(my_list[len(my_list) - 1])
print(len(my_list) - 1)
my_list.append("abc")
print(my_list[-1])
another_list = my_list
another_list.append("qwe")
print(another_list)
print(another_list[-1])
my_list.pop()
another_list[2] = "three"
print(another_list, my_list)
my_list[1] = "two"
print(another_list, my_list)

numbers = [1, 2, 3]
ids = [1, 2, 3]
numbers.append(4)
ids.append(5)

print(numbers)
print(ids)
print(ids == numbers)

nums = numbers
print(nums)
print(numbers)
print(nums == numbers)
print(nums is numbers)

nums = [1, 2, 3]
print(nums == numbers)
print(nums is numbers)

nums = list(numbers)
print(nums == numbers)
print(nums is numbers)
nums.append(1)
print(nums)
print(numbers)

movies = ["Inception", "Jaws", "Frozen", "Titanic"]
for movie in movies:
    print("My movie:")
    print(movie)
    print("___")
print("Bye")

line = "Hello world"
new_line = "_"

for char in line:
    print(new_line)
    new_line += "_"
    new_line += char

print(new_line)

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10, 5, -2):
    print(i)

# FizzBuzz / 3 / 5
# Fizz / 3
# Buzz / 5

n = 18

for i in range(1, n + 1):
    if i / 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

def hello():
    print("Hello World")

hello()

def greet(name):
    print("Hello", name)

greet("John")

my_name = "Nick"
greet(my_name)

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i / 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
    return result
fz = fizzbuzz(7)

for f in fz:
    print(f)

countries = {
    "Russia": "Moscow",
    "United Kingdom": "London",
    "Germany": "Berlin",
    "France": "Paris",
    "Japan": "Tokyo",
}
print(countries["Japan"])
print(countries.get("Italy"))

countries["Italy"] = "Rome"
print(countries)

def count_items(collectino):
    result = {}
    for item in collectino:
        count = result.get(item, 0) + 1
        result[item] = count
    return result
print(count_items("Hello World"))
print(count_items([
    "Dog",
    "Cat",
    "Dog",
    "Parrot",
    "Cat",
    "Dog",
]))












