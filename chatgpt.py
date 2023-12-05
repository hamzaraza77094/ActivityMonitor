import openai

# Set the API key globally
openai.api_key = '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'
def generate(prompt, max_tokens=100):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    # Assuming the response is stored in a tuple as shown in your example
    choices = dict(response).get('choices', [])
    if choices:
        first_choice = choices[0]
        # Access the 'message' attribute and then the 'content' attribute
        message_content = first_choice.message.content
        return(message_content)

# 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