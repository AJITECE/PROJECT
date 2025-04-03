import google.generativeai as genai
client=genai

# Set up API key
genai.configure(api_key="AIzaSyAwgW3SYl4MubXSCUp_aZMvVchR4yaMzv0")

# Initialize the model
model = genai.GenerativeModel("gemini-pro")

# Generate a response
prompt = "Tell me about Python programming."
response = model.generate_content(prompt)

# Print the output
print(response.text)

