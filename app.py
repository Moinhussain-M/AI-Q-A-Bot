import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_user_question():
    return input("Enter your question: ")


def validate_question(question):

    if question.strip() == "":
        return "INVALID"

    if question.lower() == "exit":
        return "EXIT"

    return "VALID"


def get_ai_response(question):

    try:

        model = genai.GenerativeModel(
            "gemini-3.6-flash"
        )

        response = model.generate_content(
            question
        )

        return response.text

    except Exception as e:

        print("\n===== DEBUG ERROR =====")
        print(type(e))
        print(e)
        print("=======================\n")

        return "Unable to get a response right now."





def display_answer(answer):
    print("\nAnswer:")
    print(answer)
    print()


def main():

    print("=" * 50)
    print("Welcome to AI Q&A Bot")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:

        question = get_user_question()

        status = validate_question(question)

        if status == "EXIT":
            print("\nGoodbye!")
            break

        if status == "INVALID":
            print("\nPlease enter a valid question.\n")
            continue

        print("\nGenerating response...\n")

        answer = get_ai_response(question)

        display_answer(answer)

if __name__ == "__main__":

    main()






