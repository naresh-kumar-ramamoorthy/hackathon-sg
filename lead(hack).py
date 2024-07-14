import random
import json

# Enhanced categories with banking terms and more
CATEGORIES = {
    "banking": ["account", "transaction", "interest", "mortgage", "deposit"],
    "finance": ["investment", "portfolio", "dividend", "equity", "liability"],
    "security": ["firewall", "phishing", "malware", "authentication", "encryption"],
    "management": ["strategy", "planning", "leadership", "organization", "communication"],
    "marketing": ["branding", "advertising", "promotion", "segmentation", "research"],
    "custom": []  # Custom words added by authorized users
}

# Explanations for the terms
EXPLANATIONS = {
    "account": "An arrangement by which a bank holds funds on behalf of a client.",
    "transaction": "An agreement, communication, or movement carried out between a buyer and a seller to exchange an asset for payment.",
    "interest": "The charge for the privilege of borrowing money, typically expressed as annual percentage rate (APR).",
    "mortgage": "A loan used to purchase or maintain a home, land, or other types of real estate.",
    "deposit": "Money placed into a banking institution for safekeeping.",
    "investment": "An asset or item acquired with the goal of generating income or appreciation.",
    "portfolio": "A range of investments held by a person or organization.",
    "dividend": "A distribution of a portion of a company's earnings to its shareholders.",
    "equity": "The value of the shares issued by a company.",
    "liability": "A company's legal debts or obligations that arise during the course of business operations.",
    "firewall": "A network security system that monitors and controls incoming and outgoing network traffic.",
    "phishing": "A cyber attack that uses disguised email as a weapon to steal sensitive data.",
    "malware": "Software designed to disrupt, damage, or gain unauthorized access to a computer system.",
    "authentication": "The process of verifying the identity of a user or device.",
    "encryption": "The process of converting information or data into a code to prevent unauthorized access.",
    "strategy": "A plan of action designed to achieve a long-term or overall aim.",
    "planning": "The process of making plans for something.",
    "leadership": "The action of leading a group of people or an organization.",
    "organization": "The structure or arrangement of related or connected items.",
    "communication": "The imparting or exchanging of information or news.",
    "branding": "The promotion of a particular product or company by means of advertising and distinctive design.",
    "advertising": "The activity or profession of producing advertisements for commercial products or services.",
    "promotion": "The publicization of a product, organization, or venture so as to increase sales or public awareness.",
    "segmentation": "The process of dividing a broad consumer or business market into sub-groups based on shared characteristics.",
    "research": "The systematic investigation into and study of materials and sources in order to establish facts and reach new conclusions."
}

# Reframed questions and answers for the training
QUESTIONS = {
    "banking": [
        ("What is the term for an arrangement where a bank holds funds on behalf of a client?", "account"),
        ("What do you call an exchange of assets for payment between a buyer and a seller?", "transaction"),
        ("What is the term for the charge incurred for borrowing money, often expressed as an annual percentage rate (APR)?", "interest"),
        ("What is the name of a loan used to purchase or maintain real estate such as a home?", "mortgage"),
        ("What term describes money placed into a bank for safekeeping?", "deposit")
    ],
    "finance": [
        ("What term describes an asset acquired with the goal of generating income or appreciation?", "investment"),
        ("What is the term for a collection of investments held by a person or organization?", "portfolio"),
        ("What do we call a distribution of a portion of a company's earnings to its shareholders?", "dividend"),
        ("What term refers to the value of the shares issued by a company?", "equity"),
        ("What term describes a company's legal debts or obligations arising during business operations?", "liability")
    ],
    "security": [
        ("What is the name of a system that monitors and controls incoming and outgoing network traffic to ensure security?", "firewall"),
        ("What is the term for a cyber attack that uses disguised emails to steal sensitive data?", "phishing"),
        ("What term describes software designed to disrupt, damage, or gain unauthorized access to a computer system?", "malware"),
        ("What is the process called that verifies the identity of a user or device?", "authentication"),
        ("What is the term for converting information into a code to prevent unauthorized access?", "encryption")
    ],
    "management": [
        ("What term describes a plan of action designed to achieve a long-term or overall goal?", "strategy"),
        ("What do you call the process of making plans for something?", "planning"),
        ("What is the term for the action of leading a group or organization?", "leadership"),
        ("What is the term for the structure or arrangement of related or connected items?", "organization"),
        ("What term describes the process of exchanging information or news?", "communication")
    ],
    "marketing": [
        ("What is the promotion of a product or company through advertising and distinctive design called?", "branding"),
        ("What term describes the profession of producing advertisements for commercial products or services?", "advertising"),
        ("What is the term for the publicization of a product to increase sales or public awareness?", "promotion"),
        ("What is the process called that divides a broad market into sub-groups based on shared characteristics?", "segmentation"),
        ("What is the systematic investigation into materials and sources to establish facts and reach new conclusions called?", "research")
    ],
    "custom": []  # Custom words added by authorized users
}

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Function to check if the player has guessed the word
def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# Function to get word category
def get_category():
    while True:
        print("Available categories: " + ", ".join(CATEGORIES.keys()))
        category = input("Choose a category: ").lower()
        if category in CATEGORIES:
            return category
        else:
            print("Invalid choice. Please choose a valid category.")

# Function to get a hint for the word
def get_hint(word, guessed_letters):
    available_hints = [letter for letter in word if letter not in guessed_letters]
    if available_hints:
        hint = random.choice(available_hints)
        return hint
    else:
        return None

# Function to add custom words (restricted to admin)
def add_custom_words(username):
    if username.lower() == "admin":
        while True:
            word = input("Enter a word to add to the custom list (or type 'done' to finish): ").lower()
            if word == "done":
                break
            elif word.isalpha():
                CATEGORIES["custom"].append(word)
                EXPLANATIONS[word] = input(f"Enter an explanation for '{word}': ")
                print(f"'{word}' added to custom words.")
            else:
                print("Please enter a valid word.")
    else:
        print("You are not authorized to add custom words.")

# Function to add custom questions (restricted to admin)
def add_custom_questions(username):
    if username.lower() == "admin":
        while True:
            category = input("Enter a category to add a question to (or type 'done' to finish): ").lower()
            if category == "done":
                break
            elif category in CATEGORIES:
                question = input("Enter a question: ")
                answer = input("Enter the answer: ").lower()
                QUESTIONS[category].append((question, answer))
                EXPLANATIONS[answer] = input(f"Enter an explanation for '{answer}': ")
                print("Question added.")
            else:
                print("Invalid category. Please choose a valid category.")
    else:
        print("You are not authorized to add custom questions.")

# Function to track player progress
def track_progress(score, word_length):
    accuracy = (score / word_length) * 100
    if accuracy == 100:
        return "Excellent job!"
    elif accuracy >= 80:
        return "Great job!"
    elif accuracy >= 60:
        return "Good job!"
    else:
        return "Keep practicing!"

# Function to load the leaderboard from a file
def load_leaderboard():
    try:
        with open("leaderboard.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save the leaderboard to a file
def save_leaderboard(leaderboard):
    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file)

# Function to update leaderboard
def update_leaderboard(player_name, score):
    leaderboard = load_leaderboard()  # Load the current leaderboard
    if player_name in leaderboard:
        leaderboard[player_name] += score
    else:
        leaderboard[player_name] = score
    save_leaderboard(leaderboard)  # Save the updated leaderboard

# Function to display top scores
def display_top_scores():
    leaderboard = load_leaderboard()  # Load the current leaderboard
    if leaderboard:
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)
        print("\nTop Scores:")
        for idx, (player, score) in enumerate(sorted_leaderboard[:5], 1):
            print(f"{idx}. {player}: {score}")
    else:
        print("\nNo scores yet.")

# Main game function
# Main game function
def hangman_game():
    player_name = input("Enter your name: ").strip()
    category = get_category()

    questions = QUESTIONS.get(category, [])
    if not questions:
        print("No questions available for this category.")
        return

    question, word_to_guess = random.choice(questions)
    guessed_letters = []
    tries = 6
    score = 0

    print(f"\nCategory: {category.capitalize()}")
    print(f"Question: {question}")

    while tries > 0:
        print(f"\nWord to guess: {display_word(word_to_guess, guessed_letters)}")
        print(f"Tries left: {tries}")
        guess = input("Enter a letter or guess the word (type 'hint' for a hint): ").lower()

        if guess == "hint":
            hint = get_hint(word_to_guess, guessed_letters)
            if hint:
                print(f"Hint: Try '{hint}'")
            else:
                print("No more hints available.")
        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                guessed_letters.append(guess)
                tries -= 1
                print("Incorrect guess.")
        elif len(guess) == len(word_to_guess) and guess.isalpha():
            if guess == word_to_guess:
                print("Congratulations! You guessed the word!")
                score = len(word_to_guess) * 10
                break
            else:
                tries -= 2  # Penalty for incorrect word guess
                print("Incorrect word guess.")
        else:
            print("Invalid input. Please enter a single letter or guess the entire word.")

    if is_word_guessed(word_to_guess, guessed_letters):
        score = len(word_to_guess) * 10

    if score > 0:
        print(f"\nCongratulations, {player_name}! You guessed the word!")
        print(f"Score: {score}")
        progress_message = track_progress(score, len(word_to_guess))
        print(progress_message)

        # Display explanation
        if word_to_guess in EXPLANATIONS:
            print(f"\nExplanation: {EXPLANATIONS[word_to_guess]}")

        update_leaderboard(player_name, score)  # Update leaderboard

        display_top_scores()  # Display top scores after each game

    else:
        print(f"\nSorry, {player_name}. You ran out of tries.")
        print(f"The word was: {word_to_guess}")


# Main menu loop
def main_menu():
    while True:
        print("\n=== Hangman Game ===")
        print("1. Play Hangman")
        print("2. Add Custom Words (Admin Only)")
        print("3. Add Custom Questions (Admin Only)")
        print("4. Display Top Scores")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            hangman_game()
        elif choice == "2":
            username = input("Enter your username: ")
            add_custom_words(username)
        elif choice == "3":
            username = input("Enter your username: ")
            add_custom_questions(username)
        elif choice == "4":
            display_top_scores()
        elif choice == "5":
            print("Thank you for playing Hangman!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main_menu()
