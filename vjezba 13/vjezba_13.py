# Vježba 13: Napišite sljedeće funkcije:

#     Funkcija koja vraća n-torku s prvim i zadnjim elementom liste u jednoj liniji koda.

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(prvi_i_zadnji(lista)) # (1, 10)

#     Funkcija koja vraća n-torku s maksimalnim i minimalnim elementom liste, bez korištenja ugrađenih funkcija max() i min().

# lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

# print(maks_i_min(lista)) # (250, 5)

#     Funkcija presjek koja prima dva skupa i vraća novi skup s elementima koji se nalaze u oba skupa.

# skup_1 = {1, 2, 3, 4, 5}
# skup_2 = {4, 5, 6, 7, 8}

# print(presjek(skup_1, skup_2)) # {4, 5}

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def prvi_i_zadnji(original_list: list) -> tuple[int, int]:
    return (original_list[0], original_list[-1])


print(prvi_i_zadnji(lista))


lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]


def maks_i_min(original_list: list) -> tuple[int, int]:
    if not original_list:
        raise ValueError("Lista ne smije biti prazna.")
    return_max = original_list[0]
    return_min = return_max
    for member in original_list:
        if member > return_max:
            return_max = member
        elif member < return_min:
            return_min = member

    return (return_max, return_min)


print(maks_i_min(lista))

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}


def presjek(set_one: set, set_two: set) -> set:
    return_set: set = set()
    for member in set_one:
        if member in set_two:
            return_set.add(member)

    return return_set


if __name__ == "__main__":
    print(presjek(skup_1, skup_2))
