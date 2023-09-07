import openai

# Set your OpenAI API key
api_key = "dummy"
openai.api_key = api_key

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7,  # You can adjust this to control randomness
    )
    return response.choices[0].text.strip()

# Example conversation with the support assistant
def chat_with_assistant():
    print("Support Assistant: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Support Assistant: Goodbye! Have a great day.")
            break
        
        prompt = f"You: {user_input}\nSupport Assistant:"
        response = generate_response(prompt)
        print(f"Support Assistant: {response}")

if __name__ == "__main__":
    chat_with_assistant()
