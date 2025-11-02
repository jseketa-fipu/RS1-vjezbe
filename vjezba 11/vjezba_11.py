# Vježba 11: Grupiranje elemenata po paritetu

# Napišite funkciju koja prima listu brojeva i vraća rječnik s dvije liste: jedna za parne brojeve, a druga za neparne brojeve.

# Primjer:
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(grupiraj_po_paritetu(lista))
# # {'parni': [2, 4, 6, 8, 10], 'neparni': [1, 3, 5, 7, 9]}


def grupiraj_po_paritetu(original_list: list[int]) -> dict[str, list[int]]:
    return_dict: dict[str, list[int]] = {"parni": [], "neparni": []}

    for member in original_list:
        if member % 2 == 0:
            return_dict["parni"].append(member)
        else:
            return_dict["neparni"].append(member)

    return return_dict


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":
    print(grupiraj_po_paritetu(lista))
