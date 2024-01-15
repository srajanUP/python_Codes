
# immutable string
name="pyhton"
print(name[-1])
print(len(name))


# traversing the string
name1="srajan upadhyay"
for i in name1:
    print(i,end="~")


# concatination in string
print("\nhello "+"world")   #the operands on the both sides of the + operator must same

#string replication
print("srajan"*3)          #both goperands on both sides of * operator can not be string  either numbers or number and strin

#comparision operators
print("a"=="A")
print("a"!="A")
print("a"<"A")

# to get the ASCII number of the character
print(ord("a"))

# to get the ASCII cahracter from the number
print(chr(97))


#creating lists
l=list("hello")
print(l)


#creating list from keyboard input
l1=list(input("enter the values : "))
print(l1)

#creating list from tuples
t=("a","b","c","d","e")
l2=list(t)
print(l2)

#traversing lsit
for i in l2:
    print(i)


# joining lists
print(l1+l2)


#replicating lists
l3=l2*2
print(l3)

#reversing the list
l4=[1,5,6,4,7,8,9]
print(l4.reverse())
print(max(l4))