#List

#Non primitive/derived data typs
#1)List
#2)Tuple
#3)Dictionary
#4)Set

#List:

#1)[] are mandatory
#2)Duplicate elements are allowed
#3)Insertion order is preserved
#4)Heterogenous data type elements are allowed
#5)Indexing, looping is possible
#6)Mutable (you can change add and remove elements) dynamically
Eg: 



num_list=[]
print("num_list:",num_list)

print("Data type:",type(num_list))
num_list2=list()
print("num_list2:",num_list2)

num_list3=[1,2,3,4,5]
print("num_list3:",num_list3)


#Range (start, end+1,step)

num_list4=list(range(1,11))
print("num_list4:",num_list4)

even_num=list(range(0,21,2))
print("even_num:",even_num)

odd_num=list(range(1,21,2))
print("odd_num:",odd_num)


data_list=[1,2,3,4,"Pune",True,3.14,5+7j,[11,22]]
print("data_list:",data_list)
print("length of list:",len(data_list))

print(data_list[4])
print(data_list[1:4])


#Iteration: One by one data accessable

for data in data_list:
    print(data_list)

