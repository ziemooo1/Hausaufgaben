import tkinter as tk

def remove_vowels():
    text = entry.get()
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    text_as_list = list(text)
    new_text_list = []
    for letter in text_as_list:
        if letter not in vowels:
            new_text_list.append(letter)
    new_text = ''.join(new_text_list)
    result_label.config(text=new_text)

window = tk.Tk()
window.title("Consonantal Alphabet")

entry = tk.Entry(window, width=40)
entry.pack(pady=10)

button = tk.Button(window, text="Remove Vowels", command=remove_vowels)
button.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
