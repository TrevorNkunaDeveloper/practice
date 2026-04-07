def longest(my_list):
    """
    Takes an array/list, looks for the longest word and prints that string.

    Args:
        my_list (array/list): array of words.

    return:
        Void: prints the longest word.

    Example:
        >>>  longest(["the", "quick", "brown", "fox", "ate", "my", "chickens"])
        Chickens   
    """
    longset_str = ""

    for i in my_list:
        if(len(i) > len(longset_str)):
            longset_str = i
    
    print(longset_str)


longest(["the", "quick", "brown", "fox", "ate", "my", "chickens"])