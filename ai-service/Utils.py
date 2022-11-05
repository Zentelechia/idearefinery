from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def removeStopWords(text = ""):
    
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = []
    
    for w in word_tokens:
        if w not in stop_words and w not in filtered_sentence:
            filtered_sentence.append(w)
    
    # print(word_tokens)
    # print(filtered_sentence)

    return filtered_sentence

def similarWords(text1, text2):
    count = 0
    for word in text1:
        if word in text2:
            count += 1

    return count