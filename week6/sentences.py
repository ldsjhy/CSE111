import random

def get_determiner(quantity):
  
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    word = random.choice(words)
    return word

def get_noun(quantity):
  
    if quantity == 1:
        words = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]

    else:
        words = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]

    word = random.choice(words)
    return word


def get_verb(quantity, tense):
  
    if tense == "past":
        words = [ "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", 
        "will talk", "will walk", "will write"]

    word = random.choice(words)
    return word    

def get_preposition():

    words = [ "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", 
    "onto", "out", "over","past", "to", "under", "with", "without"]

    word = random.choice(words)
    return word 

def get_prepositional_phrase(quantity):
  
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = (f"{preposition} {determiner} {noun}")
    return prepositional_phrase

def main():
    quantity = 1
    tense = "past"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    preposition = get_prepositional_phrase(quantity)
    print(f"{word} {noun} {verb} {preposition}")

    quantity = 2
    tense = "past"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    preposition = get_prepositional_phrase(quantity)
    print(f"{word} {noun} {verb} {preposition}")

    quantity = 1
    tense = "present"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    preposition = get_prepositional_phrase(quantity)
    print(f"{word} {noun} {verb} {preposition}")

    quantity = 2
    tense = "present"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    preposition = get_prepositional_phrase(quantity)
    print(f"{word} {noun} {verb} {preposition}")

    quantity = 1
    tense = "future"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    preposition = get_prepositional_phrase(quantity)
    print(f"{word} {noun} {verb} {preposition}")

    quantity = 2
    tense = "future"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    preposition = get_prepositional_phrase(quantity)
    print(f"{word} {noun} {verb} {preposition}")

    quantity = 1
    tense = "past"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    preposition = get_prepositional_phrase(quantity)
    print(f"{word} {noun} {verb} {preposition}")

    quantity = 2
    tense = "present"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    preposition = get_prepositional_phrase(quantity)
    print(f"{word} {noun} {verb} {preposition}")

    quantity = 1
    tense = "future"
    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    preposition = get_prepositional_phrase(quantity)
    print(f"{word} {noun} {verb} {preposition}")

main()

    



