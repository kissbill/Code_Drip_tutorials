# https://www.youtube.com/watch?v=5tcs2qXP3Pg&t=172s

############# 1 console running ############################################################
# cmd futtatas
# cmd -> python -i debbuging
# cmd-ben a fgv hivhato lesz add(2,3)


def add(first,second):	
	return first + second

############# 2 debugging ################################################

add(1,2)
# bhova rakhato inline, aztan torolheto
import pdb
pdb.set_trace()
add(1,"")
# cmd -> (Pdb) p add 
# (Pdb) n

############# 3 virtual enviroment ################################################

# pip install virtualenv

# creating new virtual env 

# venv a folder neve
virtual venv 

source venv/bin/activate
# (venv) megjeleneik a command line-ban

(venv) milerik$ pip install selenium

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
