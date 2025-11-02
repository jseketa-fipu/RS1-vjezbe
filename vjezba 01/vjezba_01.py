# Vježba 1: Jednostavni kalkulator
import operator

# pitanja:
# 1. Je li se program izvrsava u petlji, dok se ne dobije ispravan unos, ili se treba terminirati?
# 2. Treba li paziti na decimalni zarez/tocku?
# 3.

# map string input to the operations from the operator package
supported_operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


# use float to do type checking. If the number can't be converted to float,
# ValueError will be thrown. The problem is if it is uncaught.
def check_input_for_float(prompt: str) -> float:
    while True:
        try:
            # support the difference in decimal sign
            # converts all into decimal point (2,34 -> 2.34)
            # before that strip all the whitespace with strip()
            s = input(prompt).strip().replace(",", ".")
            return float(s)
        except ValueError:
            # ValueError is being handled here, so the program doesn't
            # freeze/crash
            print("Neispravan unos broja! Pokušajte ponovno.")
        except KeyboardInterrupt:
            # if the user wants to exit the program, this allows him to do
            # just that. SystemExit exits the program with the return code.
            # Return code 0 means no error
            print("\nPrekid.")
            raise SystemExit(0)


# if input(prompt) is assigned before the infinite loop, the test crashes,
# because it endlessly complains about unsupported operator, but never
# asks the user again for the new input
def check_if_operator_supported(prompt: str) -> str:
    while True:
        try:
            op = input(prompt).strip()
            if op not in supported_operators:
                raise ValueError("Nepodržani operator!")
            return op
        except ValueError as e:
            print(e)


def check_for_division_by_zero(second_operand: float, op: str) -> None:
    if second_operand == 0 and op == "/":
        print("Dijeljenje s nulom nije dozvoljeno!")
        raise SystemExit(0)


if __name__ == "__main__":
    operand_1 = check_input_for_float("Unesite prvi broj: ")
    operand_2 = check_input_for_float("Unesite drugi broj: ")
    operator_input = check_if_operator_supported("Unesite operator: ")
    check_for_division_by_zero(operand_2, operator_input)
    operacija = supported_operators[operator_input]
    result = operacija(operand_1, operand_2)
    print(f"Rezultat operacije {operand_1} {operator_input} {operand_2} je {result}")
