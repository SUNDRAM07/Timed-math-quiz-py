import random
import time
min_number=2
max_number=13
OPERANDS=["+","-","*"]
def quiz():
    global expression,answer
    left_Number=random.randint(min_number,max_number)
    right_number=random.randint(min_number,max_number)
    operators=random.choice(OPERANDS)
    
    expression=str(left_Number) +" "+ operators+ " " + str(right_number)
    
    answer= eval(expression)

input("PRESS ENTER TO START:")
print("-----------------------")

time_start=time.time()
wrong=0
for i in range(1,11):
    quiz()
    user_guess=input("Problem no."+str(i) +". "+ expression+" ")
    while True:
        if user_guess==str(answer):
            # print("You got that right!!!!")
            break
        else:
            wrong+=1
end_time=time.time()

final_time =round(end_time-time_start,2)
total_turns=wrong+10
print("-------------------------")
print("Congratulations you completed the quiz in "+ str(final_time) +" seconds!! ")

print ("You had an accuracy of :"+str((1000)/total_turns)+" %!!!")

# user_input=input(expression+" : ")
#     if user_input==answer: