#Dictionary:
#Properties
#1.	{} brackets are mandatory
#2.	Data items are key values pairs separated by comma
#3.	Using Keys you can access values
#4.	Iterate over dictionary using F loops
#5.	Dictionaries are mutable
#6.	Heterogeneous data elements allowed
#7.	Duplicate Keys are not allowed, if you take duplicate keys only last assigned key will be considered.

#Dict()----create empty dictionary
#D1={}  this is also empty dictionary

d={"name":"Praveen","age":41,"city":"Bengalur"}
print("D is:", d)
print("D datatype is:",type(d))
print(d)
print(d["city"])
#print(d["salary"])

for key,value in d.items():
    print(key,value)


#output in Tuple form.
    
for i in d.items():
    print(i)

#clear commond
d.clear()
print(d)

# add key,value in dictinory

d1["city"]="Delhi"
print(d1)

d1["contry"]="Inia"
print(d1)

#Know the Key vlue in the dictionary.
print(d1['contry'])

#dict Function
list_tup=[(100,'a'),(200,'b'),(300,'c'),(400,'d')]
d2=dict(list_tup)
print(d2)
print(len(d2))

#Know the Key vlue in the dictionary
print(d2[400])

value=d2.get(300)
print(value)

#value1=d2.get(600)
#print(value1)
#none

#Know the Key vlue in the dictionary ,if key value is not present in dict itwill give output as 0.
value2=d2.get(200,0)
print(value2)

value3=d2.get(700,0)
print(value3)

#Remove the key,value in the dict
d2.pop(100)
print(d2)

#Remove the key,value in the dict
r=d2.pop(800,0)
print(r)

#Remove the key,value in the dict randamly removing teh keyvalue if key value is not mentioned.
d2.popitem()
print(d2)


#Know the key,value in the dict
print('value: ',d2.values())
print("keys:",d2.keys())
print('items:', d2.items())

d3=d2
print(d3)
d4=d2.copy()
print(d4)


#clear and Del option
d1.clear()
print(d1)
del d1

