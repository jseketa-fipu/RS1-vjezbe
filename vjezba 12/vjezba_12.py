# Vježba 12: Obrnite rječnik

# Napišite funkciju koja prima rječnik i vraća novi rječnik u kojem su ključevi i vrijednosti zamijenjeni.

# Primjer:

# rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

# print(obrni_rjecnik(rjecnik))

# # {'Ivan': 'ime', 'Ivić': 'prezime', 25: 'dob'}
from typing import Any


def obrni_rjecnik(input_dictionary: dict[Any, Any]) -> dict[Any, Any]:
    return_dictionary: dict[Any, Any] = {}
    for key, value in input_dictionary.items():
        return_dictionary[value] = key

    return return_dictionary


rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

if __name__ == "__main__":
    print(obrni_rjecnik(rjecnik))
