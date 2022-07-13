#0. make answer and user input array
print("print 777 to reveal answer.")
answer = [5,0,3]
user_input = [0,0,0]

#1. get 3 number from user 
user_input[0] = int(input("Type your first number:"))
user_input[1] = int(input("Type your second number:"))
user_input[2] = int(input("Type your third number:"))
print(user_input)

#1. 777 is print answer
if(user_input[0]==7 and user_input[1]==7 and user_input[2]==7):
  print("answer is "+str(answer))
#2. user input check!! -> if same number, error!!
elif (user_input[0] == user_input[1]) or (user_input[1] == user_input[2]) or (user_input[2] == user_input[0]):
  print("you can't print the same number twice.") 
#3. Make base ball Algoruthm
else:
  ball_count = 0
  strike_count=0
  
  if(user_input[0] ==answer[0] or user_input[0] == answer[1] or user_input[0]== answer[2]):
    ball_count = ball_count+1
  
  if(user_input[1] == answer[0] or user_input[1] == answer[1] or user_input[1]== answer[2]):
    ball_count = ball_count+1
    
  if(user_input[2] == answer[0] or   user_input[2] == answer[1] or user_input[2]== answer[2]):
    ball_count = ball_count+1
    
  if(user_input[0]) == answer[0]:
    strike_count=strike_count+1
    ball_count=ball_count-1

  if(user_input[1]) == answer[1]:
    strike_count=strike_count+1
    ball_count=ball_count-1

  if(user_input[2]) == answer[2]:
    strike_count=strike_count+1
    ball_count=ball_count-1

  
  print("ball:"+ str(ball_count))
  print("strike:"+ str(strike_count))