def greet():
    print("👋 Hey! Welcome to MediAgent — your AI medical sidekick!")

def get_user_choice():
    print("\nWhat can I help you with today?")
    print("1 - Chat about health")
    print("2 - Summarize a medical report")
    print("3 - Help diagnose symptoms")
    print("0 - Exit")
    choice = input("Enter the number of your choice: ")
    return choice

def chat():
    print("\n[Chat mode] (type 'bye' to exit chat)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("MediAgent: Bye! Stay healthy! 🩺")
            break
        else:
            print("MediAgent: Sorry, I’m still learning to chat. Try summarizing or diagnosing for now!")

def summarize_report():
    print("\n[Report Summarizer]")
    print("Feature coming soon! Stay tuned 🔜")

def diagnose():
    print("\n[Symptom Diagnoser]")
    print("Feature coming soon! Stay tuned 🔜")

def main():
    greet()
    while True:
        choice = get_user_choice()
        if choice == '1':
            chat()
        elif choice == '2':
            summarize_report()
        elif choice == '3':
            diagnose()
        elif choice == '0':
            print("Goodbye! Take care! 💖")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
