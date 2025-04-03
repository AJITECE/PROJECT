
        if chat_history != last_processed_message:  # Only respond to new messages
            last_processed_message = chat_history  # Update last processed message

            try:
                # Use Gemini AI to generate a response
                model = genai.GenerativeModel("gemini-1.5-pro")
                response = model.generate_content(