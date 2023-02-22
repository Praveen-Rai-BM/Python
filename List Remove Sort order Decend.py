
#Remove Method (Removing the element from the list)

l6=[11,22,1,2,4,42,33]
print("l6 before using remove method:",l6)
l6.remove(42)
print("l6 after removing 42:",l6)
#l6.remove(100)
#print(l6)


#Based on  the index removing elements in the list
#pop() by defult remove the last elements of the list
l6.pop (1)
print(l6)

l6.pop()
print(l6)



#Ordering
#reverse method

l7=[2,3,5,7]
l7.reverse()

print("Reversed list:",l7)

#Sort (ascending /de order)
# when sorting in list data iteam homogenoues data type (only numbers)

l8=[12,45,6,7,43,3,134,6,8,768]
l8.sort()
print(l8)

# Descending

l8.sort(reverse=True)
print(l8)
