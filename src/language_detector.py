import string

ENGLISH_WORDS = {
    "i", "you", "he", "she", "they",
    "happy", "sad", "love", "hate",
    "good", "bad", "today", "tomorrow",
    "feel", "feeling", "really",
    "hello", "thanks", "please",
    "yes", "no", "what", "why"
}

HINDI_WORDS = {
    "hai", "ho", "hun", "main", "mera", "meri",
    "kya", "kyun", "acha", "accha",
    "yaar", "bhai", "sab", "bata",
    "nahi", "haan", "haanji",
    "theek", "kar", "raha", "rahi"
}


def detect_language(text):

    words = text.lower().split()
    
    words = [
    word.strip(string.punctuation)
    for word in text.lower().split()
    ]   

    english_count = 0
    hindi_count = 0

    for word in words:

        if word in ENGLISH_WORDS:
            english_count += 1

        if word in HINDI_WORDS:
            hindi_count += 1

    if english_count > 0 and hindi_count > 0:
        return "hinglish"

    elif english_count > 0:
        return "english"

    elif hindi_count > 0:
        return "hindi"

    return "english"