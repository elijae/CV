class Person:
	def __init__(self, age, hair, sex, name):
		self.age = age
		self.hair = hair
		self.sex = sex
		self.name = name

	def talk(self):
		print('dididadadaaaaa')

	def walk(self):
		print(self.name + " is walking")


jacob = Person(15, 'short', 'M', 'jacob')
innocent = Person(21, 'short', 'M', 'innocent')
doreen = Person(23, 'short', 'F', 'doreen')


# print(doreen.age)
# print(doreen.hair)
# print(doreen.__dict__)
# doreen.walk()


class Student(Person):
	def study(self):
		print(self.name + " is studying python")


student1 = Student(20, 'long', 'F', 'irene')

print(student1.age)
print(student1.hair)
print(student1.__dict__)
student1.study()

