

"""
This program alows a user three tries to guess the correct answer to the question
question = "What is the captical of California". The awnser is "Sacramento"

We first set max_tries = 3. Then we create a loop to iterate three times. For each interation,
we ask the user for the answer (user input). Then based on the answer the user gives, we check
to see if the user input matches the answer. If so, print "Correct!", then  terminate the loop with a 
break statement. 

if the user could not guess the correct answer within the max_tries, then print
"You have used up allotment of guesses.", the print "The correct answer is "Sacramento"

"""

"""

main
    question = "What is the capital of California"
    answer = "Sacramento"
    ask(question, answer)


ask
    tries = 0
    loop three times
        increment tries
        ask user input()
        check to esee of user input is equal to answer
            if so, print"Correct" then exit loop
    if not correct
        print to the user "You have used up your allotment of guesses."
        print the correct answer " The correct answer is 'Sacramento'

main
"""

def main():
    question = "What is the capital of California"
    answer = "Sacramento"
    ask(question, answer,)

def ask(question, answer,max_tries=3)
    tries = 0
    ans =""
    while tries < max_tries
        tries =  tries + 1
        ans = input(question) #Sacrmento
        if ans == answer:
            print("correct!")
            break
    if ans!= answer:
        print("You have used up allotment of guesses.")

main()