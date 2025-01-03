my_foods = ['pizza', 'falafel', 'carrot cake', 'banana', 'apple']
print("The first three items in the list are:")
print(my_foods[-3:])

friend_pizza = my_foods[:]
my_foods.append('tomato')
friend_pizza.append('potato')

print("My favorite pizza are:" )
print(my_foods)

print("\nMy firend's favorite pizza are:")
print(friend_pizza)

for food in my_foods:
	print("My favorite food is " + food)
	
for food in friend_pizza:
	print("My friend's favorite food is " + food)
