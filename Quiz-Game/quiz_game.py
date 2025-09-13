questions = ("1. What is the largest organ in the human body?", 
             "2. What gas do living creatures need to breathe?", 
             "3. What is the name of the famous clock tower in London? ", 
             "4. Which planet is known as the Red Planet?", 
             "5. What is the chemical formula for water?", 
             "6. In what year did the Titanic sink?", 
             "7. Who was the first country to successfully land a spacecraft near the Moon's South Pole?", 
             "8. What is the capital of Canada?", 
             "9. What is the hardest natural substance on Earth?", 
             "10. What is the alternative name for a mountain ash tree?")

options = (("A. Liver", "B. Heart", "C. Skin", "D. Lungs"), 
           ("A. Carbon Dioxide", "B. Oxygen", "C. Nitrogen", "D. Hydrogen"), 
           ("A. Big Ben", "B. Eiffel Tower", "C. Statue of Liberty", "D. Colosseum"), 
           ("A. Venus", "B. Jupiter", "C. Saturn", "D. Mars"), 
           ("A. H₂O", "B. CO₂", "C. NaCl", "D. O₂"), 
           ("A. 1905", "B. 1912", "C. 1920", "D. 1931"), 
           ("A. China", "B. South Korea ", "C. Japan", "D. India"), 
           ("A. Toronto", "B. Vancouver", "C. Ottawa", "D. Montreal"), 
           ("A. Gold", "B. Diamond", "C. Iron", "D. Quartz"), 
           ("A. Rowan", "B. Oak", "C. Maple", "D. Pine"),)

answers = ("C", "B", "A", "D", "A", "B", "D", "B", "B", "A")
guesses = []
score = 0 
question_number = 0

for question in questions: 
    print("<------------------------>")
    print(question)
    for option in options[question_number]:
        print(option)
    
    user_guess = input("Enter the correct option (A, B, c, D): ").upper()
    guesses.append(user_guess)
    if user_guess == answers[question_number]:
        print("CORRECT ANSWER!")
        score += 1
    else:
        print("INCORRECT ANSWER!")
        print(f"{answers[question_number]} is the correct answer")

    question_number += 1

print("<------------------------>")
print("         RESULTS          ")    
print("<------------------------>")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end= " ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")