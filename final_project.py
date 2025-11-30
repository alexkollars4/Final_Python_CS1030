import random
name = input("Enter your name: ")

#Quiz Questions
questions = [
    { 'question': 'What is the derivative of x^2?',
        'options': ['2x', 'x', 'x^2', '1'],
        'answer': '2x'
    },
    
    
    
    
    # Power Rule Derivatives
    {
        "question": "What is the derivative of x³?",
        "options": ["3x²", "x²", "3x", "x³"],
        "answer": "3x²"
    },
    {
        "question": "What is the derivative of x⁴?",
        "options": ["4x³", "3x³", "4x⁴", "x³"],
        "answer": "4x³"
    },
    {
        "question": "What is the derivative of x⁵?",
        "options": ["5x⁴", "4x⁴", "5x⁵", "x⁴"],
        "answer": "5x⁴"
    }
] 


#Function for displaying the quiz
def display_quiz(question):
    print(question["question"])
    for i, option in enumerate(question['options'], 1):
        print(f"{i}. {option}")

#Function to Recive User Answer
def get_user_answer():
    while True:
        try:
            choice = int(input("Enter the number of your answer (1-4): "))
            print()
            if 1 <= choice <= 4:
                return choice - 1 
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Running Quiz Logic
def run_quiz():
    score = 0 
    total_questions = len(questions)
    
    random.shuffle(questions)

    for question in questions:
        display_quiz(question)
        user_choice = get_user_answer()

        if question["options"][user_choice] == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}\n")
            print()

        print()

    print(f"Quiz Over! Your final score is {score} out of {total_questions}.")
    percentage = (score / total_questions) * 100
    print(f"That's {percentage:.2f}% correct.")

#Main Game Loop
def main():
    while True:
        print(f"Hello, {name}! Welcome to the Derivative Quiz Game!")
        print()
        run_quiz()

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
    