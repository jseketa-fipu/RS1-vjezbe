# Vježba 10: Brojanje riječi u tekstu

# Napišite funkciju koja broji koliko se puta svaka riječ pojavljuje u tekstu (frekvencija riječi) i vraća rječnik s rezultatima.

# Primjer:

# tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

# print(brojanje_riječi(tekst))

# # {'Python': 2, 'je': 3, 'programski': 1, 'jezik': 1, 'koji': 1, 'jednostavan': 1, 'za': 1, 'učenje': 1, 'i': 1, 'korištenje.': 1, 'vrlo': 1, 'popularan.': 1}

import re


def count_words_normalized(input_text: str) -> dict[str, int]:
    # \w matches Unicode letters/digits/_, so čćšđž work fine
    words = re.findall(r"\w+", input_text.lower(), flags=re.UNICODE)
    frequency: dict[str, int] = {}

    for word in words:
        # if the key doesn't exist, set its value to 0
        # otherwise fetch value and add 1
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


text: str = (
    "Python je programski jezik koji je jednostavan za ucenje i koristenje. Python je vrlo popularan."
)
if __name__ == "__main__":
    print(count_words_normalized(text))
