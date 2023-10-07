# This progam generates simple English sentences.
# Randomly generating words and putting together in a complete sentence.

# Import random module
import random

# Define main() function
def main():
# Considering single is 1, and plural is 2

# Write the main function to call your make_sentence function six times and print six sentences with these characteristics:
# 1.	single and 	past tense
    print(make_sentence(1, 'past'))

# 2.	single and	present tense
    print(make_sentence(1, 'present'))

# 3.	single and	future tense
    print(make_sentence(1, 'future'))

# 4.	plural and	past tense
    print(make_sentence(2, 'past'))

# 5.	plural and	present tense
    print(make_sentence(2, 'present'))

# 6.	plural and	future tense
    print(make_sentence(2, 'future'))


# Define function for choose a determiner.
# Will choose in two types, singular and plural.
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

# Define function for choose a noun.
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

# Randomly choose and return a noun.
    noun = random.choice(nouns)
    return noun

# Defining function for choose verbs.
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == 'past':
        verbs = ['drank','ate', 'grew', 'laughed', 'thought', 'ran', 'slept', 'talked', 'walked', 'wrote']
        
    elif tense == 'present' and quantity == 1:
        verbs = ['drinks', 'eats', 'grows', 'laughs', 'thinks', 'runs', 'sleeps', 'talks', 'walks', 'writes']
    else:
        verbs = ['drink', 'eat', 'grow', 'laugh', 'think', 'run', 'sleep', 'talk', 'walk', 'write']
    if tense == 'future':
        verbs = ['will drink', 'will eat', 'will grow', 'will laugh','will think', 'will run', 'will sleep', 'will talk', 'will walk', 'will write']

#Randonmly choose a verb.
    verb = random.choice(verbs)
    return verb


# Define the make sentence function.
# This will write a complete sentence.
def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determine = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    phrase = get_prepositional_phrase(quantity)
    phrase_2 = get_prepositional_phrase(quantity)
    adjective = get_adjective()
    adverb = get_adverb()
    sentence = f'{determine.capitalize()} {adjective} {noun} {adverb} {verb} {phrase} {phrase_2}.'
    return sentence

# Define the get preposition function.
# This will get a preposition to add in the sentence. 
def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ['about', 'above', 'across', 'after', 'along', 'around', 'at', 'before',
                     'behind', 'below', 'beyond', 'by', 'despite', 'except', 'for',
                     'from', 'in', 'into', 'near', 'of', 'off', 'on', 'onto', 'out',
                     'over', 'past', 'to', 'under', 'with', 'without']
    preposition = random.choice(prepositions)
    return preposition

# Define the get propositional phrase function
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or plural.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()
    phrase = f'{preposition} {determiner.capitalize()} {adjective} {noun}'
    return phrase

# Define get adjetive function
def get_adjective():
    """Return a randomly chosen adjective
    from this list of adjetives:
        'fast', 'smart', 'tall', 'short', 'dumb', 'slow', 'bad', 'big', 'angry',
        'beautiful', 'awful', 'cruel', 'adorable', 'clever', 'charming', 'bored', 'calm'     
        Return: a randomly chosen adjective.
    """

    get_adjective = ['fast', 'smart', 'tall', 'short', 'dumb', 'slow', 'bad', 'big', 'angry',
        'beautiful', 'awful', 'cruel', 'adorable', 'clever', 'charming', 'bored', 'calm',
        'red', 'yellow', 'blue', 'dinky', 'busy']
    adjective = random.choice(get_adjective)
    return adjective

# Define get adverb function
def get_adverb():
    """Return a randomly chosen adverb
    from this list of adverbs:
        'calmly', 'sweetly', 'slowly', 'fastly', 'quickly', 'always', 'actually', 'deeply', 'briefly',
        'beautifully', 'awfully', 'cruelly', 'dearly', 'cleverly', 'acutely', 'bitterly', 'bravely'     
        Return: a randomly chosen adverb.
    """

    get_adverb = ['calmly', 'sweetly', 'slowly', 'fastly', 'quickly', 'always', 'actually', 'deeply', 'briefly',
        'beautifully', 'awfully', 'cruelly', 'dearly', 'cleverly', 'acutely', 'bitterly', 'bravely']
    adverb = random.choice(get_adverb)
    return adverb

# Call the main function
main()