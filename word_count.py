def count_words(string):
    # Create an empty dictionary to store word counts
    word_count = {}
    # Split the input string into words
    words = string.split()

    # Iterate over each word in the list of words
    for word in words:
        # Remove any punctuation marks from the word
        word = word.strip(".,!?;:\"")
        # Convert the word to lowercase to ensure case-insensitive counting
        word = word.lower()
        # Increment the count for the word in the dictionary
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Return the dictionary containing word counts
    return word_count

# Example usage:
input_string = "Hello World! This is a Hello world program. World, hello?"
word_occurrences = count_words(input_string)

# Iterate over each word and its count in the word_occurrences dictionary
for word, count in word_occurrences.items():
    # Print the word and its count
    print(f"{word}: {count}")
