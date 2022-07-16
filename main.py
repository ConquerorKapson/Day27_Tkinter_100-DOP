import tkinter as tk

window = tk.Tk()
window.config(padx=10, pady=10)
# window.geometry("400x300")
heading = tk.Label(text="Rupee Converter")
heading.grid(row=0, column=1)

enter_rupees = tk.Label(text="Enter Rupees")
enter_rupees.grid(row=1, column=0)

rupees = tk.Entry()
rupees.insert(0, "0")
rupees_entered = rupees.get()
rupees.grid(row=1, column=1, padx=(30, 0))


def label_maker(rupees_entered):
    for i in range(2, 7):
        entered_amount = tk.Label(text=f"{rupees_entered} rupees = ")
        entered_amount.grid(row=i, column=0, padx=10, pady=5)


def convert_to_dollar():
    rupees_entered = float(rupees.get())
    return rupees_entered * 0.013


def convert_to_euro():
    rupees_entered = float(rupees.get())
    return rupees_entered * 0.012


def convert_to_pound():
    rupees_entered = float(rupees.get())
    return rupees_entered * 0.011


def convert_to_yen():
    rupees_entered = float(rupees.get())
    return rupees_entered * 1.74


def convert_to_dirham():
    rupees_entered = float(rupees.get())
    return rupees_entered * 0.046


def convert_rupees_and_place():
    currency_converter = {"dollar": convert_to_dollar(),
                          "euro": convert_to_euro(),
                          "pound": convert_to_pound(),
                          "yen": convert_to_yen(),
                          "dirham": convert_to_dirham()
                          }
    row_placement = 2
    label_maker(rupees.get())
    for currency, fun in currency_converter.items():
        label = tk.Label(text=f"{fun: .2f}")
        label.grid(row=row_placement, column=1, padx=10, pady=5)

        annotation = tk.Label(text=f"{currency}")
        annotation.grid(row=row_placement, column=2, padx=10, pady=5)

        row_placement += 1


convert = tk.Button(text="Click to convert", command=convert_rupees_and_place)
convert.grid(row=1, column=2, padx=(50, 10))

window.mainloop()
