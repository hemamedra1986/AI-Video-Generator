# AI Content Generation using OpenAI

import openai

# Function to generate AI content using OpenAI API

def generate_ai_content(prompt):
    openai.api_key = 'YOUR_API_KEY'
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response.choices[0].message['content']

# Example usage
if __name__ == '__main__':
    prompt = 'Write a story about a robot learning to feel emotions.'
    content = generate_ai_content(prompt)
    print(content)