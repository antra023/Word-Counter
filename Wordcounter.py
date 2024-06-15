# Word Counter Project

def count_words(text):
    """
    This function takes a string as input and returns the number of words in the string.
    Words are considered to be sequences of characters separated by whitespace.
    """
    # Split the input text into words using whitespace as the delimiter
    words = text.split()
    # Return the number of words
    return len(words)

def main():
    """
    Main function to run the Word Counter program.
    """
    print("Welcome to the Word Counter Program!")
    
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")
    
    # Error Handling: Check if the input is empty
    if not user_input.strip():
        print("Error: No input provided. Please enter a valid sentence or paragraph.")
        return
    
    # Count the number of words in the input
    word_count = count_words(user_input)
    
    # Display the word count to the user
    print(f"The number of words in the input is: {word_count}")

if __name__ == "__main__":
    main()
