#make a number guessing game
import random
attempt = 0
numbers = [1,2,3,4,5,6,7,8,9,10]
print("welcome to the number guessing game.")
print("find the number i choose from 0 to 10")
correct = random.choice(numbers)
while True:
   answer = int(input("Your guess: "))
   if answer == correct:
      print("congrats, you found the number")
      break
   elif answer >10:
   	print("your guess is higher than 10. please try a smaller number")
   else:
      attempt = attempt + 1
   print(f"Wrong number. Your total attempts: {attempt} please try again")
        
