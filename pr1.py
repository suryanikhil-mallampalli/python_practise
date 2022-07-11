a='hello world'
print(type(a))
len(a)

mystring='hello world'
print(mystring[-4])
print(mystring[4])

print(mystring[2:])
print(mystring[:2]) #stop index include end letter also
print(mystring[3:6])
print(mystring[::])#will print all words
print(mystring[::2])#will jump 2 steps and print stuff
print(mystring[2:4:2])

print(mystring[::-1])#this is reversing string technique in python

print(mystring[::-2])#obsreve the difference between above one(16th step) and below one

#beautiful feauture in python
x='hello world'
x=x+' it is beautiful outside'
print(x)
#function for printing uppercase
print(x.upper())
#function for printing lowercase
print(x.lower())
#function for splitting the required string
print(x.split())
#splitting required amount of content>>>we can see the difference in output
r='hi this is a string'
print(r.split('i'))



#printing letter 10 times
letter='z'
print(letter*10)
#more flexible
e='2'+'3'
print(e)
 


 