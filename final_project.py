import random

#Quiz Questions
questions = [
    { 'question': 'What is the derivative of x^2?',
        'options': ['2x', 'x', 'x^2', '1'],
        'answer': '2x'
    },
     {
        "question": "What is the derivative of sin(x)?",
        "options": ["cos(x)", "-cos(x)", "sin(x)", "-sin(x)"],
        "answer": "cos(x)"
    },
    {
        "question": "What is the derivative of cos(x)?",
        "options": ["sin(x)", "-sin(x)", "cos(x)", "-cos(x)"],
        "answer": "-sin(x)"
    },
    {
        "question": "What is the derivative of tan(x)?",
        "options": ["sec²(x)", "csc²(x)", "-sec²(x)", "1/cos²(x)"],
        "answer": "sec²(x)"
    },
    {
        "question": "What is the derivative of cot(x)?",
        "options": ["-csc²(x)", "csc²(x)", "-sec²(x)", "sec²(x)"],
        "answer": "-csc²(x)"
    },
    {
        "question": "What is the derivative of sec(x)?",
        "options": ["sec(x)tan(x)", "-sec(x)tan(x)", "csc(x)cot(x)", "-csc(x)cot(x)"],
        "answer": "sec(x)tan(x)"
    },
    {
        "question": "What is the derivative of csc(x)?",
        "options": ["-csc(x)cot(x)", "csc(x)cot(x)", "-sec(x)tan(x)", "sec(x)tan(x)"],
        "answer": "-csc(x)cot(x)"
    },
    
    # Inverse Trigonometric Derivatives
    {
        "question": "What is the derivative of arcsin(x)?",
        "options": ["1/√(1-x²)", "-1/√(1-x²)", "1/(1+x²)", "-1/(1+x²)"],
        "answer": "1/√(1-x²)"
    },
    {
        "question": "What is the derivative of arccos(x)?",
        "options": ["-1/√(1-x²)", "1/√(1-x²)", "-1/(1+x²)", "1/(1+x²)"],
        "answer": "-1/√(1-x²)"
    },
    {
        "question": "What is the derivative of arctan(x)?",
        "options": ["1/(1+x²)", "-1/(1+x²)", "1/√(1-x²)", "-1/√(1-x²)"],
        "answer": "1/(1+x²)"
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
    },
    {
        "question": "What is the derivative of √x (or x^(1/2))?",
        "options": ["1/(2√x)", "2√x", "1/√x", "√x/2"],
        "answer": "1/(2√x)"
    },
    {
        "question": "What is the derivative of 1/x (or x⁻¹)?",
        "options": ["-1/x²", "1/x²", "-x²", "1/x"],
        "answer": "-1/x²"
    },
    {
        "question": "What is the derivative of 1/x² (or x⁻²)?",
        "options": ["-2/x³", "2/x³", "-1/x³", "1/x²"],
        "answer": "-2/x³"
    },
    
    # Exponential and Logarithmic Derivatives
    {
        "question": "What is the derivative of eˣ?",
        "options": ["eˣ", "xeˣ⁻¹", "ln(x)", "1/x"],
        "answer": "eˣ"
    },
    {
        "question": "What is the derivative of ln(x)?",
        "options": ["1/x", "x", "ln(x)", "eˣ"],
        "answer": "1/x"
    },
    {
        "question": "What is the derivative of aˣ (where a is a constant)?",
        "options": ["aˣ·ln(a)", "aˣ", "x·aˣ⁻¹", "aˣ/ln(a)"],
        "answer": "aˣ·ln(a)"
    },
    
    # Constant and Linear Functions
    {
        "question": "What is the derivative of a constant c?",
        "options": ["0", "c", "1", "x"],
        "answer": "0"
    },
    {
        "question": "What is the derivative of x?",
        "options": ["1", "0", "x", "2x"],
        "answer": "1"
    },
    {
        "question": "What is the derivative of 5x?",
        "options": ["5", "5x", "x", "0"],
        "answer": "5"
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

    print(f"Quiz Over! Your final score is {score} out of {total_questions}.")
    percentage = (score / total_questions) * 100
    print(f"That's {percentage:.2f}% correct.")

#Main Game Loop
def main():
    while True:
        print("Welcome to the Derivative Quiz!")
        run_quiz()

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
    