secret_num = 5
Guess_Count = 0
Guess_Limit = 3
while Guess_Count < Guess_Limit:
    Guess = int(input("Guess : "))
    Guess_Count += 1
    if Guess == secret_num:
        print("You Win!")
        break
else :
      print("Sorry, You Failed")



