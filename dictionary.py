#it is key value pair
d={"carrot":2,"onoiom":4,"potato":5,"milk":6}
print(d["carrot"])
#printing the dictionary
for key in d:
    print("value:",d[key])

#deleting
d.clear()
print(d)

#tuples-they are like lists but there are some differences , they can contain various data types in them like
#tuples are immutable lists are muttable
address=("street","new york",2)
print(address[1])
print(address[0])

