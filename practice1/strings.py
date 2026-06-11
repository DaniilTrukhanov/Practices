#Strings
print("Hello")
print('Hello')

#Quote Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assign string to a variable
a = "Hello"
print(a)

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#or

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are arrays
a = "Hello, World!"
print(a[1])

#Looping through a string
for x in "banana":
  print(x)

#String length
a = "Hello, World!"
print(len(a))

#Check string
#example 1
txt = "The best things in life are free!"
print("free" in txt)

#example 2
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT
#Example 1
txt = "The best things in life are free!"
print("expensive" not in txt)

#Example 2
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Slising strings
b = "Hello, World!"
print(b[2:5])

#Slice From the Start
b = "Hello, World!"
print(b[:5])

#Slice To the End
b = "Hello, World!"
print(b[2:])

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

#Modify Strings
a = "Hello, World!"
print(a.upper())

#Lower Case
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation
#Example 1
a = "Hello"
b = "World"
c = a + b
print(c)
#Example 2
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Format
#F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers
#Example 1
price = 59
txt = f"The price is {price} dollars"
print(txt)
#Example 2
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#Example 3
txt = f"The price is {20 * 59} dollars"
print(txt)

#Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)