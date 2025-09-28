import ollama

response = ollama.chat(
    model="llama2",  # match exactly what you saw in `ollama list`
    messages=[{"role": "user", "content": "Hello, what can you do?"}]
)

print(response["message"]["content"])
