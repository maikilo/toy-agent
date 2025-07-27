import os
import sys
from dotenv import load_dotenv
from google.genai import Client, types

load_dotenv()
api_key = os.environ.get('GEMINI_API_KEY')
client = Client(api_key=api_key)


def main():
    args = sys.argv
    if len(args) < 2:
        print('No args provided')
        sys.exit(1)

    user_prompt = args[1]
    verbose = True if (len(args) > 2 and args[2] == '--verbose') else False

    messages = [
        types.Content(role='user', parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
    )
    print(response.text)

    if verbose:
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')


if __name__ == "__main__":
    main()
