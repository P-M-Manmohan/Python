# def my_map(my_func,my_iter):
#     result =[]
#     for item in my_iter:
#         new_item = my_func(item)
#         result.append(new_item)
#     return result
# nums=[3,4,7,5,8,9]

# cubed=my_map(lambda x: x**3,nums)

# print(cubed)

people=[('Alice',50),('Bob',41)]
sorted_people=sorted(people,key= lambda x:x[1]) #sorted() takes three parameters iterable , key-> It decides what the iterable is sorted based on 
#here the iterable contains tuples the lambda functions make the key the second value in the tuple ,reverse
print(sorted_people)

