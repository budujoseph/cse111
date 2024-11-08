
import random

def main():
    
    quantities = [1,2]
    tenses = ["past","present","future"]
    for _ in range(6):
        quantity = random.choice(quantities)
        tense = random.choice(tenses)
        sentence = make_sentence(quantity, tense)
        cap_sentence = sentence.capitalize()
        print(cap_sentence)

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb =get_verb(quantity, tense)
    preposition = get_prepositional_phrase(quantity)

    sentence = f"{determiner} {noun} {verb} {preposition}"
    return sentence


def get_determiner(quantity):
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]

    determiner = random.choice(determiners)
    return determiner

def get_noun(quantity):
    if quantity ==1:
        nouns = ["bird","boy","car","cat","child","dog","girl","man","rabbit","woman"]
    else:
        nouns = ["birds","boys","cars","cats","children","dogs","girls","men","rabbits","women"]

    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank","ate","grew","laughed","thought","ran","slept","talked","walked","wrote"]

    elif tense == "present" and quantity == 1:
        verbs =["drinks","eats","grows","laughs","thinks","runs","sleeps","talks","walks","writes"]

    elif tense == "present" and quantity != 1:
        verbs = ["drink","eat","grow","laugh","think","run","sleep","talk","walk","write"]

    else:
        tense == "future"
        verbs = ["will drink","will eat","will grow","will laugh","will think","will run","will sleep","will talk"
                 "will walk","will write"]
    
        return random.choice(verbs)

def get_preposition():
    prepositions = ["about","above","across","after","along","around","at","before","behind","below","beyond",
                    "by","despite","except","for","from","in","into","near","of","off","on","onto","out","over",
                    "past","to","under","with","without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"


main()