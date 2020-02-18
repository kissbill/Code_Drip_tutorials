############# 1 console running ############################################################


############# 2 debugging ################################################



############# 3 virtual enviroment ################################################



########### 4 list/dict comprehension ###############################################

fruits = [
	{'name': 'apple','price': 20},
	{'name': 'avocado','price': 33},
	{'name': 'orange','price': 54}
]

# ############regualar solution
# fruits_name = []
# for fruit in fruits:
# 	fruits_name.append(fruit['name'])
# print(fruits_name)

print(
	[fruit['name'] 
		for fruit in fruits
	# ]
	# plus feltetel csaphato a vegere
	if fruit['name'][0]=='a' ]
	) 

print(
	{fruit['name']:fruit['price'] 
		for fruit in fruits}

	)


######### 5. lambda ################################################
def add(x, y):
	return x + y

#same as :

add2 = lambda x,y : x + y


# call back function-hoz praktik #################
nums = [1,2,3]

def is_greater_then_on(x):
	return x > 1

more_than_one_nums = filter(is_greater_then_on, nums)
print(list(more_than_one_nums))

# lamdaval
more_than_one_nums = filter(lambda x : x > 1 , [1,2,3])
print(list(more_than_one_nums))
