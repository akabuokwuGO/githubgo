def alternate_characters(string): # This is Function to make each alternate character into an uppercase character and each other alternate character a lowercase character in a string.
    result = []
    toggle = True
    for char in string:
        if char.isalpha():
            if toggle:
                result.append(char.upper())
            else:
                result.append(char.lower())
            toggle = not toggle
        else:
            result.append(char)
    return ''.join(result)


def alternate_words(string): # The Function to  make each alternative word lowercase and uppercase in a string
    words = string.split()
    for index, word in enumerate(words):
        if index % 2 == 0:
            words[index] = word.lower()
        else:
            words[index] = word.upper()
    return ' '.join(words)



if __name__ == "__main__": # The main 
    input_string = input("Please enter a string: ")

  
    the_alternate_characters = alternate_characters(input_string)   # The code for the alternate characters
    print("This will print string with alternate characters in uppercase and lowercase:", the_alternate_characters)

    
    the_alternate_words = alternate_words(input_string) # The code for alternate words
    print("This will print the string with alternate words in lowercase and uppercase:", the_alternate_words)