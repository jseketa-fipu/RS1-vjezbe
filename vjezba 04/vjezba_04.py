def validate_input(prompt: str) -> int:
    while True:
        s: str = input(prompt)
        try:
            n: int = int(s)
        except ValueError:
            print("Unesi cijeli broj (npr. 42).")
            continue

        if n < 0:
            print("Upisi pozitivan broj.")
            continue

        return n


list_of_valid_numbers: list = []


def main() -> None:
    while True:
        input_positive_number = validate_input("Upisi pozitivan broj ili 0 za prekid: ")
        list_of_valid_numbers.append(input_positive_number)
        if input_positive_number == 0:
            total = sum(list_of_valid_numbers)
            print(f"Suma unesenih brojeva je: {total}")
            break


if __name__ == "__main__":
    main()
