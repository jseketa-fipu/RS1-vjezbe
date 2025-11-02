def input_positive_year(prompt: str = "Enter a year (>= 1): ") -> int:
    while True:
        s = input(prompt).strip()
        try:
            year = int(s)
        except ValueError:
            print("Please enter digits only (e.g., 1999).")
            continue
        if year < 1:
            print("Please enter a positive year (>= 1).")
            continue
        return year


def main() -> None:
    # Example
    y = input_positive_year()
    print("Year:", y)
    if (y % 4 == 0 and not y % 100 == 0) or y % 400 == 0:
        print(f"Godina {y}. je prijestupna.")
    else:
        print(f"Godine {y}. nije prijestupna.")


if __name__ == "__main__":
    main()
