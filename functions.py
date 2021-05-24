import re
import tkinter as tk

def do_validation(self, new_value):
    return new_value == "" or new_value.isnumeric()


def validate_like_currency(self, event):
    if event.char.isnumeric() or event.keycode == 8 or event.keycode == 46:
        value = self.txtValCredit.get()
        if value != "":
            value = format_currency(value, "", 0, True)
        self.valTextValCredit.set(value)
        # self.txtValCredit.icursor(self.valTextValCredit.icur)
        if not (event.keycode == 8 or event.keycode == 46) and self.txtValCredit.index(tk.INSERT) == len(
                self.txtValCredit.get()) - 1:
            self.txtValCredit.icursor(tk.END)
    else:
        value = self.txtValCredit.get()
        self.valTextValCredit.set(value[:-1])


def clean_form(self, listframes):
    try:
        print("Limpiando inputs...")

        WIDGET_CLASSNAME = 'Entry'
        for objframe in listframes:
            selection_form = [child for child in objframe.winfo_children()
                              if child.winfo_class() == WIDGET_CLASSNAME]

            for widget in selection_form:
                actual_state = widget['state']
                widget['state'] = 'normal'
                widget.delete(0, tk.END)
                widget['state'] = actual_state

    except Exception as e:
        print("Error contolado...")


def change_state_entry_form(self, listframes, state):
    try:
        print("Limpiando inputs...")

        WIDGET_CLASSNAME = 'Entry'
        for objframe in listframes:
            selection_form = [child for child in objframe.winfo_children()
                              if child.winfo_class() == WIDGET_CLASSNAME]

            for widget in selection_form:
                widget['state'] = state

    except Exception as e:
        print("Error contolado...")

def format_currency(value, symbol="$", limit=2, reformat=False):
    try:
        thousands_separator = "."
        fractional_separator = ","
        if not reformat:
            value = symbol + "{:,.2f}".format(int(value))
            if thousands_separator == ".":
                main_currency, fractional_currency = value.split(".")[0], value.split(".")[1]
                new_main_currency = main_currency.replace(",", ".")
                value = new_main_currency + fractional_separator + fractional_currency
        if reformat:
            #value = re.sub("[^0-9 ]+", "", str(value))  #
            value = str(value).replace('.', '')
            value = symbol + "{:,}".format(int(value))
            if thousands_separator == ".":
                main_currency = value.split(".")[0]
                new_main_currency = main_currency.replace(",", ".")
                value = new_main_currency
        return value
    except Exception as e:
        print("Error al convertir en formato moneda")

