def word_frequency(sentance):
    sentance_dict = {}
    words = sentance.lower().split()

    if not words:
        return {}
    for word in words:
        sentance_dict[word] = sentance_dict.get(word,0) + 1
    
    return(sentance_dict)

print(word_frequency("Welcome to the Jungle I live in the jungle"))