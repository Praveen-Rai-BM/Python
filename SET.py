#SET : Set is unique data structure, not in squenace.

#empty set
s=set()
print("types:",s)

#tuple convert into set
s2=set(range(1,11))
print(s2)
print(type(s2))

#list convert into set
l=[11,22,33,44]
s3=set(l)
print(s3)

#Dictionary convert into set

d={100,100,300,400,400,500}
s4=set(d)
print(s4)
print(type(s4))

d1={1:45,2:34,3:43,4:45,5:64}
print(d1)
print(type(d1))
s5=set(d1)
print(d1)
print(type(d1))

# get the values in set
s6=set(d1.values())
print(s6)

#.add in set
s7={1,2,3,4}
print(s7)
s7.add(111)
print(s7)

# .update in set
l=[1,2,3]
t=(111,222,333)
s={888,9991,777}
s10=set()
s10.update(l,t,s)
print(s10)

# .pop() #empty pop () will remove eliment randaomly.

s10.pop()
print(s10)

s10.remove(111)
print(s10)

#if elemtnts are not in the set will get teh error.
#s10.remove(10)
#print(s10)


#discard---will not give the error if elements are not in the set
s10.discard(777)
print(s10)
s10.discard(10)
print(s10)



#S10.clear------(Clear the set)
s10.clear
print(s10)
#del s10----------(delete teh set)
del s10
print(s10)

#d.setdefault: if key value is not present in the dictinory default key value
#will be added

d={1:23,2:45}
r_val=d.setdefault(1,100)
print(r_val)


#d.setdefault: if key value is not present in the dictinory default key value
#will be added

d={1:23,2:45}
r_val=d.setdefault(1,100)
print(r_val)
r_vall=d.setdefault("z",111)
print(r_vall)
print(d)


d4={'a':11,'b':222}
print(d4)

d5={'x':333,'y':444}
print(d5)

d4.update(d5)
print("d4 updated:",d4)

