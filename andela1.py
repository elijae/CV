yobs_dic = {'ann':1993, 'jane':2007, 'doreen':1970, 'juli':2002}

# calculates age
def age_calc(name):
	# get the yob from dic
	yob = yobs_dic[name]
	# caluclate age by subtracting from 2019
	age = 2019-yob
	# print if person is an adult
	if age > 17:
		print(name + ' is an adult ')
		print(name + ' is ' + str(age) + ' years old')

# loop through dictionary to calculate age of members
for name in yobs_dic:
	age_calc(name)


# print dict items using .items()
for name,yob in list(yobs_dic.items()):
	print(name, yob)





yobs_list = [1991, 1990, 2003, 1995, 1889, 1962]
def age_calculator(yob):
	# calculate the age
	age = 2019-yob
	print("age is " + str(age) )

# loop through list, print the age
for yob in yobs_list:
	age_calculator(yob)






words = 'hi there, I want one dollar to buy four tomatoes, three eggs and two rolexes'
print(words)

numbers_dic = {'four': 4, 'three': 3, 'two': 2, 'one': 1}

for number_word in numbers_dic:
	print(number_word)
	if number_word in words:
		words = words.replace(number_word, str(numbers_dic[number_word]) )

print(words)