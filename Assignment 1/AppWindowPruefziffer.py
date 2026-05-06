import tkinter as tk


class AppWindowPruefziffer:

    def __init__(self, pz_algorithm, width, height, title="Title"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
        self.pz_algorithm = pz_algorithm

    def run(self):
        self.init_widgets()
        self.root.mainloop()
        self.close()

    def init_widgets(self):
        pad = {"padx": 8, "pady": 6}

        # --- ISBN row ---
        tk.Label(self.root, text="ISBN:", bg="white", anchor="w", width=6).grid(
            row=0, column=0, **pad, sticky="w"
        )
        self.isbn_entry = tk.Entry(self.root, width=22)
        self.isbn_entry.grid(row=0, column=1, columnspan=2, **pad, sticky="ew")

        tk.Button(self.root, text="Check", width=8,
                  command=self.on_button_click_isbn).grid(row=1, column=0, **pad, sticky="w")
        self.isbn_result = tk.Label(self.root, text="", bg="white", anchor="w")
        self.isbn_result.grid(row=1, column=1, columnspan=2, **pad, sticky="w") #valid or not

        # --- separator ---
        tk.Frame(self.root, height=1, bg="#cccccc").grid(
            row=2, column=0, columnspan=3, sticky="ew", padx=8
        )

        # --- IBAN row ---
        tk.Label(self.root, text="IBAN:", bg="white", anchor="w", width=6).grid(
            row=3, column=0, **pad, sticky="w"
        )
        self.iban_entry = tk.Entry(self.root, width=22)
        self.iban_entry.grid(row=3, column=1, columnspan=2, **pad, sticky="ew")

        tk.Button(self.root, text="Check", width=8,
                  command=self.on_button_click_iban).grid(row=4, column=0, **pad, sticky="w")
        self.iban_result = tk.Label(self.root, text="", bg="white", anchor="w")
        self.iban_result.grid(row=4, column=1, columnspan=2, **pad, sticky="w")

        self.root.columnconfigure(1, weight=1)

    def close(self):
        pass

    def on_button_click_isbn(self):
        isbn = self.isbn_entry.get().strip()
        if self.pz_algorithm.check_isbn(isbn):
            self.isbn_result.config(text="Number is: valid", fg="black")
        else:
            self.isbn_result.config(text="Number is: invalid", fg="red")

    def on_button_click_iban(self):
        iban = self.iban_entry.get().strip()
        if self.pz_algorithm.check_iban(iban):
            self.iban_result.config(text="Number is: valid", fg="black")
        else:
            self.iban_result.config(text="Number is: invalid", fg="red")
