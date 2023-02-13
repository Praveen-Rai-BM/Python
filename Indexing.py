#Indexing
#Strats with Zero
#space is also character
# Possitive Indexing -left to right

city="Bengaluru"
print("city:",city)
print(city[0])
print(city[3])
print("length of City:",len(city))


#Negative Indexing

#space is also character
# Negative Indexing - Right to right

city="Bengaluru"
print("city:",city)
print(city[-4])


#Slicing

#sharing_name[start index:end index+1:stp]
#stepping pecking given number
city="Bengaluru"
print(city[0:4])
print(city[0:7:2])
print(city[0:9])


#Keywords
import keyword

keywords=keyword.kwlist
print(keywords)

print(len(keywords))
