def readList(groceryList, groceryCosts):
	totalCost = 0
	print("This is what is in your grocery list:")
	for i in range(len(groceryList)):
		print(groceryList[i]+" - $"+str(groceryCosts[i]))
		totalCost += groceryCosts[i]
		time.sleep(1)
	print("\nThere are "+str(len(groceryList))+" items in your list and your total (not including tax) will be $"+str(totalCost))

def main():
	print("Welcome to Boris' Grocery List Program")
	name = input("What is your name? ")
	print("Hello "+name+", today we will creating your grocery list")
	groceryList = []
	groceryCosts = []
	while True:
		item = input("Input an item that you would like to add to your shopping list! (Or type 0 to exit the program)\n")
		if item == "0":
			readList(groceryList, groceryCosts)
			break
		else:
			groceryList.append(item)
			itemCost = input("Input the price of the item specified before to the nearest cent (No $ sign):\n")
			groceryCosts.append(float(itemCost))

import time
while True:
	main()
	again = input("\nDo you want to run this program again? (Y or N)")
	while again.lower() != "n" and again.lower() != "y":
		again = input("That is an invalid option! Try again.")
	if again.lower() == "n":
		print("Thanks for using my program!")
		break
