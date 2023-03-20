import tkinter as tk


def clean_form(lst_frames):
    try:
        print("Cleaning inputs...")

        widget_class_name = ['Entry', 'TEntry']
        for obj_frame in lst_frames:
            selection_form = [child for child in obj_frame.winfo_children()
                              if child.winfo_class() in widget_class_name]

            for widget in selection_form:
                actual_state = widget['state']
                widget['state'] = 'normal'
                widget.delete(0, tk.END)
                widget['state'] = actual_state

    except Exception as e:
        print("Error not controlled...")


def change_state_entry_form(list_frames, state):
    try:
        print("cleaning inputs...")

        widget_class_name = 'Entry'
        for obj_frame in list_frames:
            selection_form = [child for child in obj_frame.winfo_children()
                              if child.winfo_class() == widget_class_name]

            for widget in selection_form:
                widget['state'] = state

    except Exception as e:
        print("Error controlled...")


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
            value = str(value).replace('.', '')
            value = symbol + "{:,}".format(int(value))
            if thousands_separator == ".":
                main_currency = value.split(".")[0]
                new_main_currency = main_currency.replace(",", ".")
                value = new_main_currency
        return value
    except Exception as e:
        print("Error converting currency format")

def validate_float(value_if_allowed):
    if value_if_allowed:
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False
    else:
        return True

def validate_int(value_if_allowed):
    if value_if_allowed:
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False
    else:
        return True