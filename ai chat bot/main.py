import pyautogui
import time
import pyperclip
import google.generativeai as genai

# Configure Gemini API (Replace with your actual API key)
genai.configure(api_key="AIzaSyAwgW3SYl4MubXSCUp_aZMvVchR4yaMzv0")


def get_last_message(chat_log):
    """Extracts the last message from the chat history."""
    messages = chat_log.strip().split("\n")  # Split by new lines
    return messages[-1] if messages else ""  # Return the last message


def is_new_message(last_message, new_message):
    """Checks if a new message has arrived."""
    return new_message and new_message != last_message


# Store the last processed message
last_processed_message = ""

# Step 1: Click on the Chrome icon at coordinates (Adjust if needed)
pyautogui.click(1126, 1055)
time.sleep(2)  # Give time for Chrome to open

while True:
    time.sleep(3)  # Short delay before checking for a new message

    # Step 2: Select and Copy the Chat Text
    pyautogui.moveTo(704, 233)
    pyautogui.dragTo(1745, 920, duration=1.5, button="left")  # Select text
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)  # Wait for text to be copied

    # Step 3: Retrieve chat history from clipboard
    chat_history = pyperclip.paste()
    last_message = get_last_message(chat_history)

    # If a new message arrives, generate a response
    if is_new_message(last_processed_message, last_message):
        last_processed_message = last_message  # Update last processed message

        try:
            # Use Gemini AI to generate a response
            model = genai.GenerativeModel("gemini-1.5-pro")
            response = model.generate_content(
                [
                    "You are Ajit, a witty and fun Indian who loves Hinglish."
                    "You analyze the last message and reply in a casual, humorous, and engaging way."
                    "Your response should be exactly 10 words, blending Hindi and English naturally, with a friendly and playful tone",
                    last_message,
                ]
            )

            # Extract response text
            reply = (
                response.text.strip()
                if hasattr(response, "text")
                else "i didnt understand !"
            )

            # Copy response to clipboard
            pyperclip.copy(reply)

            # Step 4: Click on the chat input box
            pyautogui.click(873, 970)
            time.sleep(1)

            # Step 5: Paste the response and send
            pyautogui.write(reply, interval=0.05)
            time.sleep(1)
            pyautogui.press("enter")

            # Step 6: Wait for the user to respond before checking again
            time.sleep(5)  # Increase delay to give time for a reply

        except Exception as e:
            print(f"Error: {e}")
