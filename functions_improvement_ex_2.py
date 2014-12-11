# Times Table Tester
def Times_Table_Tester():
    get_testTable()
    for questions in range (1,6):
        generate_question(testTable)
        ask_question(question)
        validate_answer(userAnswer,actualAnswer)
# get testTable from user
def get_testTable():
    testTable = input("Which times-table do you want to be tested on? ")
    testTable = int(testTable)
    return testTable
# generate question
def generate_question(testTable):
    random_number()
    answer_2_question(Num1,Num2)
    question = question_generation(Num1,Num2,actualAnswer)
    return question
# ask question
def ask_question(question):
    question_generation(Num1,Num2)
    return userAnswer
# validate answer
def validate_answer(userAnswer,actualAnswer):
    if userAnswer == actualAnswer:
        answer_right()
    else:
        answer_wrong(actualAnswer)
# generate random number
def random_number():
    Num2 = random.randrange(2,13)
    return Num2
# get answer to question
def answer_2_question(Num1,Num2):
    actualAnswer = Num1 * Num2
    return actualAnswer
# written question generation
def question_generation(Num1,Num2):
    userAnswer = input(str(Num1) + ' x ' + str(Num2) + ' = ? ')
    userAnswer = int(userAnswer)
    return userAnswer
# answer right
def answer_right():
    print('Well done, you got the correct answer!')
    print()
# answer wrong
def answer_wrong(actualAnswer):
    print('Sorry, you got the answer wrong. The correct answer is',actualAnswer)
    print()
# main program
import random
print("Times-table tester")
print()
Times_Table_Tester()
