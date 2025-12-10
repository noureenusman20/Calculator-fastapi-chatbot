from langchain_groq import ChatGroq
import requests

llm = ChatGroq(
    model="llama3-8b-8192",
    api_key="YOUR_VALID_GROQ_API_KEY"
)


def calculator_api(num1, num2, operation):
    url = "http://127.0.0.1:8000/calculate"
    data = {
        "num1": num1,
        "num2": num2,
        "operation": operation
    }
    response = requests.post(url, json=data)
    return response.json()

def handle_user_message(message):
    message = message.lower()
    
    if message.startswith(("+", "-", "*", "/")):
        parts = message.split()  
        operation = parts[0]
        num1 = float(parts[1])
        num2 = float(parts[2])
        api_response = calculator_api(num1, num2, operation)
        # Return the calculation result from FastAPI if input is an operation
        return f"Result: {api_response['data']['result']}"

    # For any other message, we skip calling the LLM (API key not available) 
    # to avoid errors; acts as a placeholder for future LLM integration
    return "LLM is disabled. Only calculations work right now."


print("\nChatbot ready! lets calculate! …\n")

while True:
    user_msg = input("You: ")
    reply = handle_user_message(user_msg)
    print("Bot:", reply)

