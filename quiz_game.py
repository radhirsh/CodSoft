import random

# Sample quiz questions and answers
quiz_data = [
    {
        "question": "Which of the following is the use of id() function in Python?",
        "options": ["Every object doesn’t have a unique id", "Id returns the identity of the object", "All of the mentioned", "None of the mentioned"],
        "correct_answer": 1
    },
    {
        "question": "Is Python case sensitive when dealing with identifiers?",
        "options": ["yes", "no"],
        "correct_answer": 0
    },
    {
        "question": "All keywords in Python are written in ..................",
        "options": ["UPPER CASE", "lower case", "Capitalized", "None of the mentioned"],
        "correct_answer": 1
    },
    {
        "question": "Mathematical operations can be performed on a string. State whether true or false -",
        "options": ["False", "True"],
        "correct_answer": 0
    },
    {
        "question": "Which one of the following has the highest precedence in the expression?",
        "options": ["Addition", "Multiplication", "Exponential", "Parentheses"],
        "correct_answer": 3
    },
    {
        "question": "What is the return type of function id?",
        "options": ["float", "bool", "dict", "int"],
        "correct_answer": 3
    },
    {
        "question": "What is the output of the following code?\nprint('Hello', 'foo', 'and', 'foo')",
        "options": ["Hello ‘foo’ and foo", "Hello foo and foo", "Hello foo and ‘bin’", "Error"],
        "correct_answer": 3
    },
    {
        "question": "Which of the following data types is not supported in Python?",
        "options": ["String", "Numbers", "Slice", "List"],
        "correct_answer": 2
    },
    {
        "question": "Which of the following keywords mark the beginning of the class definition?",
        "options": ["return", "class", "def", "All of the above"],
        "correct_answer": 1
    },
    {
        "question": "Select the reserved keyword in Python.",
        "options": ["else", "raise", "import", "All of the above"],
        "correct_answer": 3
    },
    # Add more questions...
]

def display_welcome_message():
    print("Welcome to the Python Quiz!")
    print("Answer multiple-choice questions on Python.")
    print("Let's get started!")

def present_quiz_question(question_data):
    print(question_data["question"])
    for index, option in enumerate(question_data["options"], start=1):
        print(f"{index}. {option}")
    user_answer_index = int(input("Enter the number of your answer: ")) - 1  # Convert to zero-based index
    return user_answer_index

def evaluate_user_answer(user_answer_index, correct_answer_index):
    return user_answer_index == correct_answer_index

def play_quiz_game():
    display_welcome_message()
    score = 0
    
    random.shuffle(quiz_data)
    
    for question_data in quiz_data:
        user_answer_index = present_quiz_question(question_data)
        if evaluate_user_answer(user_answer_index, question_data["correct_answer"]):
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            correct_option = question_data["options"][question_data["correct_answer"]]
            print(f"The correct answer is: {correct_option}")
    
    print("\nQuiz completed!")
    print(f"Your final score is: {score}/{len(quiz_data)}")
    
    if score == len(quiz_data):
        print("Congratulations! You answered all questions correctly.")
    elif score >= 7:
        print("Keep practicing! You're making progress.")
    else:
        print("Don't give up! Keep practicing and you'll improve.")

    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == "yes"

def main():
    play_again = True
    while play_again:
        play_again = play_quiz_game()

if __name__ == "__main__":
    main()
