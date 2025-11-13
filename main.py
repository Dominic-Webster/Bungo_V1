import json
import os
from difflib import get_close_matches

#load knowledge base from json file
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

#save knowledge to json file
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

#find best match from dictionary
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

#get answer for each question
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

#main script
def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS or Linux
        os.system('clear')
        
    print('Bungo: Hi! I\'m Bungo, your friendly chatbot!')
    print('Bungo: Who am I talking to?')
    user_name: str = input('My name is: ')
    print('Bungo: Hi, ' + user_name)
    
    while True:
        user_input: str = input('You: ')
        
        #end program
        if user_input.lower() in ['quit', 'bye', 'goodbye']:
            print('Goodbye!')
            break
        
        #basic math
        if user_input.lower() in ['addition', 'add', 'sum', 'plus']:
            print('Bungo: Sure! What\'s the first number?')
            try:
                num1 = float(input('Number 1: '))
                print('Bungo: Great! And what\'s the second number?')
                num2 = float(input('Number 2: '))
            except ValueError:
                print('Bungo: That doesn\'t look like a number')
                continue
            sum_result: int = num1+num2
            print(f"Bungo: {num1} + {num2} is equal to {sum_result}!")
            
        elif user_input.lower() in ['subtraction', 'minus', 'subtract']:
            print('Bungo: Sure! What\'s the first number?')
            try:
                num1 = float(input('Number 1: '))
                print('Bungo: Great! And what\'s the second number?')
                num2 = float(input('Number 2: '))
            except ValueError:
                print('Bungo: That doesn\'t look like a number')
                continue
            sum_result: int = num1-num2
            print(f"Bungo: {num1} - {num2} is equal to {sum_result}!")
            
        elif user_input.lower() in ['multiplication', 'times', 'multiply']:
            print('Bungo: Sure! What\'s the first number?')
            try:
                num1 = float(input('Number 1: '))
                print('Bungo: Great! And what\'s the second number?')
                num2 = float(input('Number 2: '))
            except ValueError:
                print('Bungo: That doesn\'t look like a number')
                continue
            sum_result: int = num1*num2
            print(f"Bungo: {num1} times {num2} is equal to {sum_result}!")
            
        elif user_input.lower() in ['division', 'divide']:
            print('Bungo: Sure! What\'s the first number?')
            try:
                num1 = float(input('Number 1: '))
                print('Bungo: Great! And what\'s the second number?')
                num2 = float(input('Number 2: '))
            except ValueError:
                print('Bungo: That doesn\'t look like a number')
                continue
            sum_result: int = num1/num2
            print(f"Bungo: {num1} divided by {num2} is equal to {sum_result}!")
           
        #get user name    
        elif user_input.lower() in ['what\'s my name?', 'what\'s my name', 'who am i', 'who am i?']:
            print('Bungo: Why, you\'re ' + user_name + '! I remember that! Ask me something else!')    
            
        else:
            best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        
            if best_match:
                answer: str = get_answer_for_question(best_match, knowledge_base)
                print(f'Bungo: {answer}')
            else:
                print('Bungo: I don\'t know the answer. Can you teach me?')
                new_answer: str = input('Type the answer or "skip" to skip: ')
                
                if new_answer.lower() != 'skip':
                    knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                    save_knowledge_base('knowledge_base.json', knowledge_base)
                    print('Bungo: Thanks! New response has been learned!')

                
if __name__ == '__main__':
    chat_bot()
