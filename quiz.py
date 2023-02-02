# import random, pyinputplus and time modules
import pyinputplus as pyip, random, time

# describe program
print("This is a Multiplication Quiz to test your mutiplication skills🙃\n")

question_number = 0
correct_answers = 0

# use a while loop to show only 10 questions
while question_number < 10:

    # get two random numbers
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)

    question_number += 1
    prompt = f"Question {question_number}: {num_1} * {num_2} = ?\n=>: "

    # catch 2 errors and 1 exception. timeout, limit exceeded and correct respecively
    try:
        # display question and use regex to ensure answer is correct
        answer = pyip.inputNum(prompt, allowRegexes=[rf"^{num_1*num_2}$"], blockRegexes=[(r".*", "Incorrect")], limit=3, timeout=8,)
    except pyip.TimeoutException:
        print("You ran out of time☹️") 
    except pyip.RetryLimitException:
        print("Only three tries")
    else:
        print("Correct")
        correct_answers += 1
    
    time.sleep(0.5) # wait before so user can see result
    print(f"Score: {correct_answers}/{question_number}") # show score