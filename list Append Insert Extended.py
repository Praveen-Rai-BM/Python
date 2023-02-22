

l=[11,22,33]
print(l)

l.clear()
print(l)



#Del l  (permanently deleted from memory)

del l
# print(l) (l is permanently deleted from the memory hence,Error will get)


l1=list(range(1,11))
print(l1)

print(len(l1))

L2=[1,1,1,2,4,4,9,9,9,9,9,]
print(L2.count(9))
print(L2.count(4))



L3=[1,3,3]
print(L3)

#append (add the elemnts into list)

L3.append(99)
print("L3 after appended:",L3)

L3.append("HI")
print(L3)


#insert Method
L3.insert(1,88)
print(L3)

L3.insert(100,111)
print(L3)

L3.insert(-100,888)
print(L3)

#extend Method

l4=[1,2,3]
l5=[11,22,33]
print(l4)
print(l5)
l4.extend(l5)
print(l4)


