import re

# Define a dictionary to store the chatbot's responses
responses = {
    r'hello|hi': 'Hello! How can I assist you today?',
    r'how are you': 'I\'m doing well, thanks! How about you?',
    r'what is your name': 'My name is Chatty, nice to meet you!',
    r'goodbye|bye': 'Goodbye! It was nice chatting with you.',
    r'thanks|thank you': 'You\'re welcome!',
    r'.*': 'I didn\'t understand that. Can you please rephrase?'  # Default response
}

# Define a function to process user input
def process_input(user_input):
    user_input = user_input.lower()  # Convert to lowercase for case-insensitive matching
    for pattern, response in responses.items():
        if re.match(pattern, user_input):
            return response
    return responses['.*']  # Return default response if no match found

# Create a chatbot loop
while True:
    user_input = input('You: ')  # Get user input
    response = process_input(user_input)  # Process user input
    print('Chatty:', response)  # Print chatbot response

    # Exit the chatbot loop if user types 'goodbye'
    if re.match(r'goodbye|bye', user_input.lower()):
        break