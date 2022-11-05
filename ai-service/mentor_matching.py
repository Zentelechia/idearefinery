from Utils import *

def mentorMatch(idea):
    mentors = getMentors()
    scores = []

    for mentor in mentors:
        scores.append(score(mentor.biographraphy, idea))

    return mentors[scores.index(max(scores))].id

def score(text1, text2):
    text1 = removeStopWords(text1)
    text2 = removeStopWords(text2)
    return similarWords(text1, text2)