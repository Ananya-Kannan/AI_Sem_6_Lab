def unify(words1, words2):

    # Initialize an empty substitution dictionary
    substitution = {}

    # Iterate over the words in both statements
    for word1, word2 in zip(words1, words2):
        # If a word in statement 2 is a variable, assign its value based on statement 1
        if word2.isalpha() and word2[0].isupper():
            substitution[word2] = word1
        # If words don't match and neither is a variable, unification is not possible
        elif word1 != word2:
            return None

    # Return the substitution dictionary
    return substitution

# Given statements
words1 = input("Enter first string: ").split()
words2 = input("Enter second string: ").split()


# Unify statement 2 with statement 1
result = unify(words1, words2)

# Print the result
if result:
    print("The unification is successful. Substitution =", result)
else:
    print("Unification failed.")
