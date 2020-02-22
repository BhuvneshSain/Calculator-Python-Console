#!/usr/bin/python
a = int(input("enter a num : "))
b = int(input("enter second num : "))
def Add(x,y):
	return x+y
def Sub(x,y):
	return x-y
def Mul(x,y):
	return x*y
def Div(x,y):
	return x//y
while True:
	print("Press 1 for Addition")
	print("Press 2 for Substract")
	print("Press 3 for Multiplication")
	print("Press 4 for Division")
	print("Press 5 for Exit")
	x = int(input("Enter your choice "))
	if x ==1:
		print( Add(a,b))
		print(" ")
	elif x ==2: 
		print (Sub(a,b))
		print(" ")
	elif x ==3: 
		print (Mul(a,b))
		print(" ")
	elif x ==4: 
		print (Div(a,b))
		print(" ")
	elif x ==5: break
	else :
		print("Error.. Invalid input")
		print(" ")