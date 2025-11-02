# Vježba 2: Prijestupna godina

# Napišite program koji traži unos godine i provjerava je li godina prijestupna. Godina je prijestupna ako:

#     je djeljiva s 4, ali ne sa 100 ili
#     godina je djeljiva sa 400

# Ako godina zadovoljava ove uvjete, program treba ispisati poruku:

# Godina ____. je prijestupna.

# Ako godina nije prijestupna, program treba ispisati poruku:

# Godina ____. nije prijestupna.

# pitanja
# 1. Je li se program izvrsava u petlji, dok se ne dobije ispravan unos, ili se treba terminirati?
# 2. treba li provjeravati tip unosa?


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


if __name__ == "__main__":
    y = input_positive_year()
    print("Year:", y)
    if (y % 4 == 0 and not y % 100 == 0) or y % 400 == 0:
        print(f"Godina {y}. je prijestupna.")
    else:
        print(f"Godine {y}. nije prijestupna.")
