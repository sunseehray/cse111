from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():

    singular_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(10):
        singular_noun = get_noun(1)
        plural_noun = get_noun(2)
        assert singular_noun in singular_nouns
        assert plural_noun in plural_nouns

def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    present_verbs_singular = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    present_verbs_plural = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(len(past_verbs)):
        past_verb = get_verb(1,"past")
        assert past_verb in past_verbs
    
    for _ in range(len(future_verbs)):
        future_verb = get_verb(1,"future")
        assert future_verb in future_verbs
    
    for _ in range(len(present_verbs_plural)):
        present_verb_plural = get_verb(2,"present")
        assert present_verb_plural in present_verbs_plural
    
    for _ in range(len(present_verbs_singular)):
        present_verb_singular = get_verb(1,"present")
        assert present_verb_singular in present_verbs_singular
    
def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    for _ in range(len(prepositions)):
        preposition = get_preposition()
        assert preposition in prepositions
    
def test_get_prepositional_phrase():
    
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    single_determiners = ["a", "one", "the"]
    
    plural_determiners = ["some", "many", "the"]
    
    singular_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    determiners = [1, 2]

    for _ in range(2):
        prepositional_phrase = get_prepositional_phrase(determiners[_])
        parts = prepositional_phrase.split(" ")
        length = len(parts)
        assert length == 3
        preposition = parts[0]
        determiner = parts[1]
        noun = parts[2]
        if _ == 0:
            assert preposition in prepositions
            assert determiner in single_determiners
            assert noun in singular_nouns
        if _ == 1:
            assert preposition in prepositions
            assert determiner in plural_determiners
            assert noun in plural_nouns
            


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])