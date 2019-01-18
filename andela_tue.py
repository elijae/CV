def create_dic(s, p):
	student_dic = {}
	for i in range(len(s)):
		print(i)
		k = s[i]
		v = p[i]
		student_dic[k] = v

	print(student_dic)

def age_calculator(yob):
	age = 2019-yob
	print('your are ' + str(age) + ' years old')





