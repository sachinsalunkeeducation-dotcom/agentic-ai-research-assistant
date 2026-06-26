import ollama

response = ollama.chat(
    model="phi3",
    messages=[
        {
            "role": "user",
            "content": "What are the latest AI trends?"
        }
    ]
)

print(response["message"]["content"])