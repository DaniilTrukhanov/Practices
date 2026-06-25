import re

#ex1
text1 = "abb"
x = re.findall(r"^ab*$", text1)
print (x)

#ex2
text2 = "abbb"
x = re.findall(r"^ab{2}$|^ab{3}$", text2)
print (x)

#ex3
text3 = "hello_world"
x = re.search(r"^[a-z]*_[a-z]*$", text3)
print (x.string)

#ex4
text4 = "Hello"
x = re.search(r"^[A-Z][a-z]*$", text4)
print (x.string)

#ex5
text5 = "appleb"
x = re.search(r"^a.*b$", text5)
print (x.string)

#ex6
text6 = "Hello, world. Python is easy"
x = re.sub(r"\W", ":", text6)
print (x)

#ex7
text7 = "hello_world"
x = re.split(r"_", text7)
answer = x[0]  + ''.join(i.capitalize() for i in x[1:])
print (answer)

#ex8
text8 = "HelloWorldPython"
x = re.findall(r"[A-Z][a-z]*", text8)
print (x)

#ex9
text9 = "HelloWorldPython"
x = re.sub(r"([A-Z])", r" \1", text9).strip()
print (x)

#ex10
text10 = "HelloWorldPython"
x = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text10)
answer = x.lower()
print (answer)