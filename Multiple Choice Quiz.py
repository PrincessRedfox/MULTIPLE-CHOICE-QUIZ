# program: Multiple Choice Quiz.py
# author: Sarina Saiyed
# email: 2338323@students.carmel.ac.uk
# student number: 2338323
#
# Each question will have 4 possible answers, A, B, C and D, only one
#    option will be correct.
#
# A bank of 20 questions should be held in a text file.  
# Each time the quiz is taken, the user will be asked 5 questions,
#   randomly selected, from the bank of questions…
# …all questions must be different.  There should be no duplicate
#   questions in a quiz.
# The program stores each user’s name, number of quiz attempts and
#   average score, in a text file.
# Each time a user takes the quiz, their average score is updated.
# When requested, a leaderboard will be displayed, showing the user
#   name and average score of the 3 users with the highest average score,
#   displayed in descending order of average score.


########################################################################
# Design

# the user will input their name
# User will be greated with a screen asking if they want to play the episode
#   or request a leaderboard
# if the user chooses to play the episode they will be given the first of
#   five random questions
# the player will then have to decide on the correct by choosing the options
#   A, B, C, or D
# if the player chooses a correct answer, their score for that game will
#   be increased
# when the player has completed all five questions, an average will be
# taken of their score and their average score will be updated
# the player will then be taken the starting screen again
# if the player decides to request for the leader board, they will be shown
#   the username and average score of the three users with the highest
#   average score, displayed in desending order of average score


########################################################################
# Pseudocode

#IMPORT random

#DEF get_questions():
#	questions = []
#	OPEN(FILENAME, ‘r’)
#	data = file.readfilelines()
#	FOR i IN RANGE(0, len(data))
#		question = data.strip()
#		choices = line.strip() for next 3 lines under questions
#		correct_answer = data[last line].strip()
#		questions.append(question, choices, correct_answer)
#	END FOR LOOP
#	RETURN questions
#
#DEF quiz():
#	score = 0
#	random.shuffle(questions)
#	FOR i IN RANGE(5):
#		questions, choices, correct_answer = questions
#		PRINT(“Questions: ”, question)
#		FOR j IN RANGE(4):
#			PRINT(CHR(97+j), choices[j])
#		END FOR
#		user_answer = INPUT(“Enter your answer: ”).upper()
#		IF user_answer == correct_answer:
#			PRINT(“Correct”)
#			score +=1
#		ELSE:
#			(“Incorrect”)
#		END IF
#	END FOR
#	PRINT(“end of quiz, you got”, score, “out of 5”)
#	RETURN score
#
#DEF user_score():
#	user_file = “file name”
#	user_info = {}
#	WITH OPEN(user_file, ‘r’) AS file:
#		FOR line IN file:
#			name, attempts, total_score = line.strip()
#			user_into[name] = (INT(attempts), INT(total_score))
#	IF username IN user_info:
#		attempts += 1
#		total_score = score
#	ELSE:
#		attempts = 1
#		total_score = score
#	WITH OPEN(user_file, ‘w’) AS file:
#		FOR name, (attempts, total_score) IN user_info.items():
#			file.WRTIE(name, attempt, total_score)
#
#
#DEF average():
#	average_score = total_score/attempts
#	RETURN average_score
#
#DEF leaderboard():
#	user_file = “Filename”
#	user_info = {}
#	WITH OPEN(user file, ‘r’) AS file:
#		FOR line IN file:
#			name, attempts, total_score = line.strip()
#			user_into[name] = (INT(attempts), INT(total_score))
#		sorted_users = SORTED(user_info.items(), key = lambda x: average(), reverse=TRUE)
#	PRINT(“Leaderboard:”)
#	rank = 1
#	FOR user, attempts, total_score IN sorted_users[:3]:
#		average_score = total_score/ attempts
#		PRINT(rank, user, average_score)
#		rank += 1
#
#DEF main():
#	file_name = “File name”
#	questions = get_questions(file_name)
#	WHILE TRUE:
#		PRINT (“1, 2, 3: take quiz, view leaderboard,  exit”)
#		choice = INPUT(“Enter your choice: ”)
#		IF choice == ‘1’:
#			username = INPUT(“enter username: ”)
#			quiz()
#		ELIF choice == ‘2’:
#			leaderboard()
#		ELIF choice == ‘3’:
#			BREAK
#		ELSE:
#			PRINT(“Invalid input”)
#
#IF __name__ == “__main__”:
#	main()

########################################################################
# Variables

#questions
#data
#question
#choices
#correct_answer
#score
#user_answer
#file
#user_file
#user_info
#name
#attempts
#total_score
#average_score
#sorted_users
#rank
#file_name
#choice
#



########################################################################
# Functions

# get_questions
# quiz
# user_scores
# average
# leaderboard
# main

########################################################################
# Main

import random # import the libarary random so that 5 differnt Q are generated

def get_questions(file_name): # function for retrieving the file for the episode
    questions = [] #an empty array
    with open(file_name, 'r') as file: #allows python to open file, read all the lines out of it and handling it one line at a time
        data = file.readlines() # reading the data of the entire questions file
        for i in range(0, len(data),6): #for loop starting at index 0 until it ends on the last index, will skipping every 6 lines
            question = data[i].strip() #.strip remove whitespace also tells computer that the Q is on data line i
            choices = [line.strip() for line in data[i+1:i+5]]# while the multiple choices are between index i+1 and i+5
            correct_answer = data[i+5].strip()# answer to the question on i is written every 5th line
                                                # therefore having 6 lines used for each question
            questions.append((question, choices, correct_answer))#appends whichever random question is currently chosen in the array
        return questions # ends execution of this function


def quiz(questions): #function for the main quiz
    score = 0 #new game, score starts at zero
    random.shuffle(questions) #selects a random questions from the text file
    for i in range(5): #for loop to only allow 5 random questios per game
        question, choices, correct_answer = questions[i] # i starts at 0 therefore represnts the questions, choices and answer for that round
        print("\nQuestion", i+1, ":", question) # prints questions and questions number depending on i
        for j in range(4): # for loop print the a. b. c... options
            print(chr(97 + j) + ".", choices[j]) #ascii char for a is 97 so when i=0, it will print a.
        user_answer = input("Enter your answer (a, b, c, or d): ").upper() # user input
        if user_answer == correct_answer: # if users answer is same as the line in correct answer
            print("Correct!")
            score += 1 # score will increment by 1
        else:
            print("Incorrect. The correct answer is", correct_answer) # else will show the correct answer
    print("\nQuiz Completed!")
    print("You got", score, "out of 5 questions correct.") #shows user the score they got on that round
    return score # ends funtion


def user_scores(username, score):
    user_file = "/Users/sarinasaiyed/Downloads/user_info.txt" #pathway for the .txt file
    user_info = {} # stores user infomation in a dictionary
    with open(user_file, 'r') as file: #opens file in read mode, with closes the statement after its use
        for line in file: # for loop that iterates lines in variable file
            name, attempts, total_score = line.strip().split(',') #this allows to split the line by using a comma
            user_info[name] = (int(attempts), int(total_score)) # this updates user_info when a new game is finshed

    if username in user_info: # if the username is already in the system/ .txt file
        attempts, total_score = user_info[username] #updates only the line associated with the username
        attempts += 1 # attemps incremented
        total_score += score # total score increase or stayed the same
    else: # if username is not in the system 
        attempts = 1 # attempts set to 1
        total_score = score 

    user_info[username] = (attempts, total_score) #updates current users in the dictionary

    with open(user_file, 'w') as file: # opens file in write mode
        for name, (attempts, total_score) in user_info.items(): # loops the values in user_info
            file.write(f"{name},{attempts},{total_score}\n") # writes user info to the file and serpates it using \n

def average(user_info): # works out the average for the sorted users leaderboards
    attempts, total_score = user_info
    average_score = total_score/attempts # works out users average
    return average_score

def leaderboard():
    user_file = "/Users/sarinasaiyed/Downloads/user_info.txt"
    user_info = {}
    with open(user_file, 'r') as file:
        for line in file:
            name, attempts, total_score = line.strip().split(',')
            user_info[name] = (int(attempts), int(total_score))

    sorted_users = sorted(user_info.items(), key=lambda x: average(x[1]), reverse=True) # this allows the top three high scores from their average, calculates average by calling average funtion
    
    print("\n  Leaderboard:")
    print("Username: HighScore:\n")
    rank = 1 # set rank as 1
    for user, (attempts, total_score) in sorted_users[:3]: # for loop at only picks top 3 users
        average_score = total_score / attempts
        print(f"{rank}) {user}: {average_score:.2f}") # prints users and average score to one 2.dp
        rank += 1 # rank incremts to next highest


    
def main(): # main menu
    file_name = "/Users/sarinasaiyed/Downloads/quiz_questions.txt"
    questions = get_questions(file_name)
    while True:
        print("""\n1. Take quiz
2. View leaderboard
3. exit""")
        choice = input("Enter your choice: ") # allows user to pick if they want to play for view leader board
        if choice == '1':
            username = input("Enter your username: ")
            score = quiz(questions)
            user_scores(username, score)
        elif choice == '2':
            leaderboard()
        elif choice == '3':
            print("Byee")
            break
        else:
            print("Invalid input")

        





if __name__ == "__main__":
    main() # main function executed only when code is running
    
