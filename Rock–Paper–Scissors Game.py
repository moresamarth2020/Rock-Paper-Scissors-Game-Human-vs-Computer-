import random

def rock_paper_scissors():
    print("----- Rock Paper Scissors Game -----")
    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("\nEnter rock/paper/scissors or 'quit' to exit: ").lower()

        if user_choice == "quit":
            print("Goodbye! 👋")
            break

        if user_choice not in choices:
            print("❌ Invalid choice! Try again.")
            continue

        computer_choice = random.choice(choices)

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        if user_choice == computer_choice:
            print("😐 It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("🎉 You win!")
        else:
            print("💻 Computer wins!")

rock_paper_scissors()
