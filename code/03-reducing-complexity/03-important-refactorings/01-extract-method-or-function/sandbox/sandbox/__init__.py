# The goal of this file is to provide a good example of a function that can
# be simplied using the Extract Method refactoring.

def diagram_sentence(input: str):
    """
    Diagrams a simple English sentence. Valid sentences are in the form of either:
    * a single verb
    * a subject followed by a verb
    * a subject followed by a verb followed by a direct object

    This function is extensively tested in tests/test_diagram_sentence.py.

    :param input: the sentence to diagram
    :return: an array of dictionaries that represent the sentence's diagram
    """
    words = [word.lower() for word in input.split()]

    diagram = []

    while len(words) > 0:
        word = words.pop(0)

        if _is_article(word):
            subject = [{'article': word}]

            noun_candidate = words.pop(0)
            if _is_noun(noun_candidate):
                subject.append({'noun': noun_candidate})
                diagram.append({'subject': subject})

                verb_candidate = simplify_verb(words.pop(0))
                if _is_verb(verb_candidate):
                    diagram.append({'verb': verb_candidate})

                    candidate = words.pop(0)
                    if _is_plural_noun(candidate):
                        diagram.append({'directObject': [{'noun': depluralize_noun(candidate)}]})

                    if _is_article(candidate):
                        directObject = [{'article': candidate}]
                        candidate = words.pop(0)
                        if _is_singular_noun(candidate):
                            directObject.append({'noun': candidate})
                            diagram.append({'directObject': directObject})

        if _is_pronoun(word):
            diagram.append({'subject': [{'pronoun': word}]})

            verb_candidate = simplify_verb(words.pop(0))
            if _is_verb(verb_candidate):
                diagram.append({'verb': verb_candidate})

                candidate = words.pop(0)
                if _is_plural_noun(candidate):
                    diagram.append({'directObject': [{'noun': depluralize_noun(candidate)}]})

                if _is_article(candidate):
                    directObject = [{'article': candidate}]
                    candidate = words.pop(0)
                    if _is_singular_noun(candidate):
                        directObject.append({'noun': candidate})
                        diagram.append({'directObject': directObject})

        if _is_verb(word):
            diagram.append({'verb': simplify_verb(word)})

    return diagram


def _matcher(collection: list):
    return lambda word: word in collection


VALID_PRONOUNS = [
    'i',
    'you',
    'he',
    'she',
    'it',
    'we',
    'they'
]

VALID_VERBS = [
    'eat',
    'run',
    'walk',
    'sleep',
    'drink',
    'jump',
    'sit',
    'stand',
    'lie',
    'swim',
    'fly',
]

VALID_NOUNS = [
    'dog',
    'cat',
    'bird',
    'spider',
    'apple',
    'cracker',
    'milk'
]

_is_pronoun = _matcher(VALID_PRONOUNS)
_is_verb = _matcher(VALID_VERBS)
_is_article = _matcher(['a', 'the'])
_is_noun = _matcher(VALID_NOUNS)

def simplify_verb(word: str):
    if word.endswith('s'):
        shortened_word = word[:-1]
        if _is_verb(shortened_word):
            return shortened_word
        
    return word

def _is_plural_noun(word: str):
    return word == 'milk' or (word.endswith('s') and _is_noun(word[:-1]))

def _is_singular_noun(word: str):
    return _is_noun(word)

def depluralize_noun(word: str):
    if word.endswith('s'):
        shortened_word = word[:-1]
        if _is_noun(shortened_word):
            return shortened_word
        
    return word
