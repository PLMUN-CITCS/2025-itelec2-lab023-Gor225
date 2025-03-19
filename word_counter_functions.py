
def get_sentence_input():
    """
    Obtains a sentence input from the user.
    No parameters.
    Prompts the user to enter a sentence.
    Reads and returns the user's input as a string.
    """
    sentence = input("Please enter a sentence: ")
    return sentence

def count_words(sentence):
    """
    Counts the number of words in a given sentence.
    Takes one parameter: sentence (string).
    Uses the split() method to split the sentence into a list of words based on spaces.
    Returns the number of words in the sentence (the length of the list of words).
    """
    words = sentence.split()
    return len(words)

# Main program flow
def main():
    # Obtain a sentence from the user
    sentence = get_sentence_input()
    
    # Count the words in the sentence
    word_count = count_words(sentence)
    
    # Display the word count to the user
    print(f"The sentence has {word_count} words.")

# Call the main function
if _name_ == "_main_":
    main()