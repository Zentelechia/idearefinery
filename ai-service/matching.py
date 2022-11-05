from Utils import *
from sqlservice import *

def mentorMatch(id):

    idea = getData('SELECT * from "Project";')
    for i in idea:
        if i[0] == id:
            idea = i[2]
            break
    mentors = getData('SELECT * from "Expert";')
    scores = []

    for mentor in mentors:
        scores.append(similarWords(mentor[2], idea))

    return mentors[scores.index(max(scores))][0]

def teamMatch(id, selectedTags):
    idea = getIdea(id)
    experts = getExperts()
    scores = []

    for expert in experts:
        score = 0
        for tag in expert.tags:
            if tag in selectedTags:
                score += 5

    for expert in experts:
        scores.append(similarWords(expert[2], idea) + score)    

    return experts[scores.index(max(scores))].id