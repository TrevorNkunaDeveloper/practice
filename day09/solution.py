def longest_word(words):
    
    if(not words):
        raise ValueError("List is empty")
    
    longest_word_in_list = words[0]

    for word in words:
        if len(word) > len(longest_word_in_list):
            longest_word_in_list = word

    return longest_word_in_list     
