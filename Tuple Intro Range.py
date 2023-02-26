


#Tuple: 
#Use round brackets to define “()”, these are not mandatory
#Duplicate elements are allowed
#Insertion order is preserved, you can using indexing, for loop to access elements
#Heterogeneous data elements are allowed
#Tuples are immutable because of that we don’t have any function which can Tuple dynamically.
#Eg. t=(1,2,3)
#Tuple()  to create tuple from sequence





t=()
print(type(t))
print("t :",t)

t1=(1,2,3,4,5)
print(t1)

t2=11,22,33
print("t2:",t2)
print(type(t2))
print("third element of t2 is:",t2[2])

t3=tuple(range(1,6))
print("t3:",t3)

num_list=[333,444,555,666]
t4=tuple(num_list)
print("t4:",t4)

t5=(1,2,3,4,5,6,7,8,9)
for i in t5:
    print(t5)
    print(i)
    print(i*i)


t6=(111)
print("Datatype t6:",type(t6))

t6=(111,)
print(type(t6))

# Tuple single value have to use 'comma'

t7=(1,2,3,True,"Pune",[1,2,3],3.14)
print("t7:",t7)
