def char_frequency(text):
    if not text:
        raise ValueError("Text cannot be empty")

    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    return freq