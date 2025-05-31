# WhisperBox Offline Chatbot

"""
A censorship-resistant offline chatbot designed to educate and support girls in regions where internet access is restricted or monitored.
"""

import random

def get_response(user_input):
    # Simple hardcoded logic for demo purposes
    responses = {
        "hello": "Hello! I'm your study partner. What would you like to learn today?",
        "who are you": "I'm Whisper, your offline learning assistant. I work even when the internet doesn't!",
        "math": "Great! Let's start with a simple one. What is 8 x 7?",
        "rights": "Every girl has the right to learn, grow, and be heard. Would you like to learn more about that?",
        "bye": "Goodbye for now. Keep learning, and stay safe."
    }
    
    # Normalize input
    user_input = user_input.lower().strip()
    
    # Basic response selection
    for key in responses:
        if key in user_input:
            return responses[key]
    
    # Default response
    fallback = [
        "I'm still learning. Can you try asking another way?",
        "That's interesting. Let's explore that together soon.",
        "Hmm, I don't know that yet. But I'll remember you asked!"
    ]
    return random.choice(fallback)


def main():
    print("WhisperBox Offline Chatbot")
    print("Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "bye":
            print("Whisper: Goodbye for now. Keep learning, and stay safe.")
            break
        response = get_response(user_input)
        print(f"Whisper: {response}")


if __name__ == "__main__":
    main()
