hello_string = "Hello World!"
print(hello_string)
print(type(hello_string))

print(type("h"))
print(type(False))
print(type(1))
print(1.0)
print('1')
print(True + False)
print(False + False)
print(True + True)

isinstance(123, int)
isinstance(True, float)
isinstance(True, float)
isinstance(hello_string, str)

print("foo" + "bar", "span" + "and" + "eggs")

print(hello_string[4])
print(len(hello_string))
print(hello_string[3: len(hello_string)])
print(hello_string[3:10])
print(hello_string[:10])
print(hello_string[:])

if hello_string == hello_string[:]:
    print(True)
else:
    print(False)

long_text = """Hello line - 1
hello line - 2
hello line - 3 
''
""""""
end 
bye"""
print(long_text)
print(len(long_text))
print(long_text[:50])

if "0":
    print("not empty string is True")

if -1:
    print("not 0 is True")

if -1 != 0:
    print("-1 is not 0")

if True:
    print("True is True")

a = 2.234
if a > 3:
    print(f"{a} is greater than 3")
else:
    print(f"{a} i't greater than 3")

if a > 3:
    print(f"{a} is greater than 3")
elif a == 3:
    print(f"{a} eq 3")
else:
    print(f"{a} is smaller than 3")


if int(a) == a:
    print(f"{a} contains no float data")
else:
    print(f"{a} contains float data")

if (isinstance(a, float) or isinstance(a, int) and int(a) == a):
    print(f"{a} is number and contains no float data")
else:
    print(f"{a} i't compatible")

if isinstance(a, (float, int)):
    if int(a) == a:
        print(f"{a} has no float data")
    else:
        print(f"{a} contains float data")
else:
    print(f"{a} i't a number!")


