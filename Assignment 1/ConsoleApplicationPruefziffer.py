class ConsoleApplicationPruefziffer:

    def __init__(self, pz_algorithm):
        print("Welcome to the Check Digit Validator!")
        self.pz_algorithm = pz_algorithm

    def run(self):
        while True:
            print("\nWhat would you like to validate?")
            print("  1 - ISBN-10")
            print("  2 - IBAN")
            print("  0 - Exit")

            choice = input("Your choice: ").strip()

            if choice == "0":
                print("Goodbye!")
                break
            elif choice == "1":
                digits = input("Enter ISBN: ").strip()
                if self.pz_algorithm.check_isbn(digits):
                    print(f"'{digits}' -> Number is: valid")
                else:
                    print(f"'{digits}' -> Number is: invalid")
            elif choice == "2":
                digits = input("Enter IBAN: ").strip()
                if self.pz_algorithm.check_iban(digits):
                    print(f"'{digits}' -> Number is: valid")
                else:
                    print(f"'{digits}' -> Number is: invalid")
            else:
                print("Invalid choice. Please try again.")
