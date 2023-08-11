from sandbox import diagram_sentence
from pytest import mark


@mark.parametrize(
    'input, expected_output',
    [
        ('Eat', [{'verb': 'eat'}]),
        ('eat', [{'verb': 'eat'}]),
        ('run', [{'verb': 'run'}]),
        ('walk', [{'verb': 'walk'}]),
        ('sleep', [{'verb': 'sleep'}]),
        ('drink', [{'verb': 'drink'}]),
        ('jump', [{'verb': 'jump'}]),
        ('sit', [{'verb': 'sit'}]),
        ('stand', [{'verb': 'stand'}]),
        ('lie', [{'verb': 'lie'}]),
        ('swim', [{'verb': 'swim'}]),
        ('fly', [{'verb': 'fly'}]),
    ]
)
def test_single_verb_sentence(input, expected_output):
    assert diagram_sentence(input) == expected_output


@mark.parametrize(
    'input, expected_output',
    [
        ('I eat', [{'subject': [{'pronoun': 'i'}]}, {'verb': 'eat'}]),
        ('i eat', [{'subject': [{'pronoun': 'i'}]}, {'verb': 'eat'}]),
        ('you run', [{'subject': [{'pronoun': 'you'}]}, {'verb': 'run'}]),
        ('he walks', [{'subject': [{'pronoun': 'he'}]}, {'verb': 'walk'}]),
        ('she jumps', [{'subject': [{'pronoun': 'she'}]}, {'verb': 'jump'}]),
        ('it sleeps', [{'subject': [{'pronoun': 'it'}]}, {'verb': 'sleep'}]),
        ('we eat', [{'subject': [{'pronoun': 'we'}]}, {'verb': 'eat'}]),
        ('they eat', [{'subject': [{'pronoun': 'they'}]}, {'verb': 'eat'}]),
        ('you eat', [{'subject': [{'pronoun': 'you'}]}, {'verb': 'eat'}]),
    ]
)
def test_pronoun_verb_sentence(input, expected_output):
    assert diagram_sentence(input) == expected_output


@mark.parametrize(
    'input, expected_output',
    [
        ('The dog eats', [{'subject': [{'article': 'the'}, {'noun': 'dog'}]}, {'verb': 'eat'}]),
        ('A dog eats', [{'subject': [{'article': 'a'}, {'noun': 'dog'}]}, {'verb': 'eat'}]),
        ('The bird eats', [{'subject': [{'article': 'the'}, {'noun': 'bird'}]}, {'verb': 'eat'}]),
        ('a cat eats', [{'subject': [{'article': 'a'}, {'noun': 'cat'}]}, {'verb': 'eat'}]),
        ('A spider runs', [{'subject': [{'article': 'a'}, {'noun': 'spider'}]}, {'verb': 'run'}]),
        ('the spider sleeps', [{'subject': [{'article': 'the'}, {'noun': 'spider'}]}, {'verb': 'sleep'}]),
    ]
)
def test_article_noun_verb_sentence(input, expected_output):
    assert diagram_sentence(input) == expected_output


@mark.parametrize(
    'input, expected_output',
    [
        ('The dog eats', [{'subject': [{'article': 'the'}, {'noun': 'dog'}]}, {'verb': 'eat'}]),
        ('A dog eats', [{'subject': [{'article': 'a'}, {'noun': 'dog'}]}, {'verb': 'eat'}]),
        ('The bird eats', [{'subject': [{'article': 'the'}, {'noun': 'bird'}]}, {'verb': 'eat'}]),
        ('a cat eats', [{'subject': [{'article': 'a'}, {'noun': 'cat'}]}, {'verb': 'eat'}]),
        ('A spider runs', [{'subject': [{'article': 'a'}, {'noun': 'spider'}]}, {'verb': 'run'}]),
        ('the spider sleeps', [{'subject': [{'article': 'the'}, {'noun': 'spider'}]}, {'verb': 'sleep'}]),
    ]
)
def test_article_noun_verb_sentence(input, expected_output):
    assert diagram_sentence(input) == expected_output


@mark.parametrize(
    'input, expected_output',
    [
        ('I eat apples', [{'subject': [{'pronoun': 'i'}]}, {'verb': 'eat'}, {'directObject': [{'noun': 'apple'}]}]),
        ('i eat crackers', [{'subject': [{'pronoun': 'i'}]}, {'verb': 'eat'}, {'directObject': [{'noun': 'cracker'}]}]),
        ('he walks dogs', [{'subject': [{'pronoun': 'he'}]}, {'verb': 'walk'}, {'directObject': [{'noun': 'dog'}]}]),
        ('We drink milk', [{'subject': [{'pronoun': 'we'}]}, {'verb': 'drink'}, {'directObject': [{'noun': 'milk'}]}]),
    ]
)
def test_pronoun_verb_sentence(input, expected_output):
    assert diagram_sentence(input) == expected_output


@mark.parametrize(
    'input, expected_output',
    [
        ('I eat the apple', [{'subject': [{'pronoun': 'i'}]}, {'verb': 'eat'}, {'directObject': [{'article': 'the'}, {'noun': 'apple'}]}]),
        ('i eat a cracker', [{'subject': [{'pronoun': 'i'}]}, {'verb': 'eat'}, {'directObject': [{'article': 'a'}, {'noun': 'cracker'}]}]),
        ('he walks the dog', [{'subject': [{'pronoun': 'he'}]}, {'verb': 'walk'}, {'directObject': [{'article': 'the'}, {'noun': 'dog'}]}]),
        ('We drink the milk', [{'subject': [{'pronoun': 'we'}]}, {'verb': 'drink'}, {'directObject': [{'article': 'the'}, {'noun': 'milk'}]}]),
    ]
)
def test_pronoun_verb_sentence(input, expected_output):
    assert diagram_sentence(input) == expected_output


@mark.parametrize(
    'input, expected_output',
    [
        ('The dog eats apples', [{'subject': [{'article': 'the'}, {'noun': 'dog'}]}, {'verb': 'eat'}, {'directObject': [{'noun': 'apple'}]}]),
        ('A dog eats crackers', [{'subject': [{'article': 'a'}, {'noun': 'dog'}]}, {'verb': 'eat'}, {'directObject': [{'noun': 'cracker'}]}]),
        ('The bird eats spiders', [{'subject': [{'article': 'the'}, {'noun': 'bird'}]}, {'verb': 'eat'}, {'directObject': [{'noun': 'spider'}]}]),
        ('a cat drinks milk', [{'subject': [{'article': 'a'}, {'noun': 'cat'}]}, {'verb': 'eat'}, {'directObject': [{'noun': 'milk'}]}]),
    ]
)
def test_article_noun_verb_sentence(input, expected_output):
    assert diagram_sentence(input) == expected_output


@mark.parametrize(
    'input, expected_output',
    [
        ('The dog eats the apple', [{'subject': [{'article': 'the'}, {'noun': 'dog'}]}, {'verb': 'eat'}, {'directObject': [{'article': 'the'}, {'noun': 'apple'}]}]),
        ('A dog eats a cracker', [{'subject': [{'article': 'a'}, {'noun': 'dog'}]}, {'verb': 'eat'}, {'directObject': [{'article': 'a'}, {'noun': 'cracker'}]}]),
        ('The bird eats a spider', [{'subject': [{'article': 'the'}, {'noun': 'bird'}]}, {'verb': 'eat'}, {'directObject': [{'article': 'a'}, {'noun': 'spider'}]}]),
        ('a cat eats a cracker', [{'subject': [{'article': 'a'}, {'noun': 'cat'}]}, {'verb': 'eat'}, {'directObject': [{'article': 'a'}, {'noun': 'cracker'}]}]),
    ]
)
def test_article_noun_verb_sentence(input, expected_output):
    assert diagram_sentence(input) == expected_output
