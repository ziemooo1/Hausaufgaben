from AppWindowPruefziffer import AppWindowPruefziffer
from ConsoleApplicationPruefziffer import ConsoleApplicationPruefziffer


class PruefzifferAlgorithm:
    def __init__(self):
        pass

    def check_isbn(self, isbn: str) -> bool:
        isbn = isbn.replace("-", "").replace(" ", "").upper()

        if len(isbn) != 10:
            return False

        if not isbn[:9].isdigit():
            return False

        if not (isbn[9].isdigit() or isbn[9] == 'X'):
            return False

        total = 0
        for i in range(9):
            total += (i + 1) * int(isbn[i])

        remainder = total % 11
        check_char = 'X' if remainder == 10 else str(remainder)

        return isbn[9] == check_char

    def check_iban(self, iban: str) -> bool:
        iban = iban.replace(" ", "").upper()

        if len(iban) < 15 or len(iban) > 34:
            return False

        iban = list(iban[4:] + iban[0:4])

        iban_number = ''
        for c in iban:
            if c.isdigit():
                iban_number += c
            elif c.isalpha():
                iban_number += str(10 + ord(c) - ord('A'))
            else:
                return False

        return int(iban_number) % 97 == 1


if __name__ == "__main__":
    CONSOLE = False

    pz_algorithm = PruefzifferAlgorithm()

    if CONSOLE:
        app = ConsoleApplicationPruefziffer(pz_algorithm)
        app.run()
    else:
        app = AppWindowPruefziffer(pz_algorithm, 320, 200, "Check Digit Validator")
        app.run()
