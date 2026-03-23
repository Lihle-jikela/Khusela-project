# 1. THE BRAIN: Our classification function
def classify_ticket(ticket_text):
    # Convert text to lowercase so we don't worry about capital letters
    text_lower = ticket_text.lower()
    
    # This is our Hash Map (Dictionary in Python).
    # It links a Department (Key) to a list of keywords (Values).
    rules = {
        "IT": ["laptop", "password", "login", "software", "wifi", "screen"],
        "Finance": ["salary", "invoice", "pay", "expense", "budget", "money"],
        "HR": ["leave", "conflict", "sick", "hire", "manager", "policy"],
        "Operations": ["cleaning", "maintenance", "supplies", "desk", "repair"]
    }
    
    # Loop through our map
    for department, keywords in rules.items():
        # Check every keyword in that department's list
        for word in keywords:
            # Use word boundaries to avoid partial matches (e.g., 'pay' in 'payment')
            if f" {word} " in f" {text_lower} ":
                return department
    
    # If no keywords matched
    return "Needs Human Review"

# 2. THE DEMO LOOP: This runs the live interactive terminal
def main():
    print("=== AI Ticket Classifier Backend Started ===")
    print("Type 'exit' to stop the program.\n")
    
    while True:
        # Get user input
        user_input = input("Enter a new support ticket: ").strip()
        
        # Safety check so we can close the program
        if user_input.lower() == 'exit':
            print("Shutting down the system...")
            break
        
        # Send the user's input to our Brain function
        result = classify_ticket(user_input)
        
        # Print the result
        print(f"--> System Decision: {result}\n")

# Run the demo
if __name__ == "__main__":
    main()