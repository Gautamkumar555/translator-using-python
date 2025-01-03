from deep_translator import GoogleTranslator

def get_hindi_meaning(word):
    try:
        # Translate the word to Hindi
        translation = GoogleTranslator(source='en', target='hi').translate(word)
        return translation
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Enter English words to get their Hindi meanings. Type 'exit' to quit.")
    while True:
        user_input = input("Enter an English word: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        hindi_meaning = get_hindi_meaning(user_input)
        print(f"Hindi meaning: {hindi_meaning}")
