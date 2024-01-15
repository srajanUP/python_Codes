# creating empty tuple
t=()

#creating tuples with values
t1=(1,2,3,6,9,8,5,4,7)
print("t1 =",t1)


#creating tuples with user input
t2=tuple(input("enter the values"))
print(t2)

#calculating the length of the tuples
print(len(t),
len(t1),
len(t2))

# getting index of elememnt in tuple
print(t2.index(9))


t2.reverse()
print(t2)