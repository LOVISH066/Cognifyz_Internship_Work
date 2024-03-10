print("Welcome To Dark Room, The room from where you can never leave")
print("Do you want to Start Playing, Remember Once Started you cannot leave the game in between")
print("Type 'start' if you want to start the game or 'No' if you want to leave the game")

choice = input("> ")

if(choice == "start"):
  print("Great, You are Brave")
  print("Lets Start the Game")
  print("You are in a dark room, you can see a light in the distance, you can also hear a noise coming from the distance")
  print("Would you go there where you can see the light or would you go towards the noise?")
  print("Select 'noise' or 'light'")
  
  gotochoice = input("> ")
  if(gotochoice == "noise"):
    print("you are going towards noise")
    print("You got scared by seeing a very big monster cooking flesh there")
    print("And you loose the game here")
    print("Better Luck Next Time")
    print("END")
  elif(gotochoice == "light"):
    print("you are going towards light")
    print("when you reach there, you can see gate there")
    print("And when you open the gate, you see a road from where you can escape")
    print("Hurray, You Won the game by findind the door to get out of the dark room")
  else:
    print("Invalid Choice")
elif(choice == "No"):
  print("Bye, Be Brave and Try next time")
else:
  print("Invalid Input, Please choose between 'start' or 'No'")