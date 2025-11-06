# Vježba 4: Zbrajanje unesenih brojeva
# Napišite program koji traži od korisnika unos cijelih brojeva sve dok korisnik ne unese broj 0.
# Nakon unosa 0, program treba ispisati zbroj svih prethodno unesenih brojeva.


def validate_input(prompt: str) -> int:
    while True:
        s: str = input(prompt)
        try:
            n: int = int(s)
        except ValueError:
            print("Unesi cijeli broj (npr. 42).")
            continue

        return n


list_of_valid_numbers: list = []

if __name__ == "__main__":
    while True:
        input_positive_number = validate_input("Upisi pozitivan broj ili 0 za prekid: ")
        list_of_valid_numbers.append(input_positive_number)
        if input_positive_number == 0:
            total = sum(list_of_valid_numbers)
            print(f"Suma unesenih brojeva je: {total}")
            break
