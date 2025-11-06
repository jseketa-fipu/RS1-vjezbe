# Vježba 9: Uklanjanje duplikata iz liste

# Napišite funkciju koja prima listu i vraća novu listu koja ne sadrži duplikate. Implementaciju odradite pomoćnim skupom.

# Primjer:

# lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

lista: list[int] = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


def ukloni_duplikate(original_list: list[int]) -> list[int]:
    already_seen: set[int] = set()
    final_list: list[int] = []
    for member in original_list:
        if member in already_seen:
            continue
        already_seen.add(member)
        final_list.append(member)

    return final_list


if __name__ == "__main__":
    print(ukloni_duplikate(lista))
