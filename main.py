import tkinter as tk

import functions as myfns
from Prestamo import Prestamo
import functools


class app:
    def __init__(self, master):
        self.master = master
        # DC - Titulo barra principal
        master.title("Formula de Prestamo")
        # DC - Dimensiones de la ventana principal
        master.geometry("900x500")

        self.put_frames()
        self.put_title()
        self.put_form()
        self.put_result()

        self.master.bind('<Return>', lambda event=None: self.btnCalculate.invoke())

    def put_frames(self):
        # DC - Frames o Paneles
        self.frame_title = tk.Frame(self.master, bg="green", height=40)
        self.frame_form = tk.Frame(self.master)
        self.frame_result = tk.Frame(self.frame_form)

        self.frame_title.pack(side="top", fill='both')
        self.frame_form.pack(side="bottom", expand=True)
        self.frame_result.grid(row=5, columnspan=2, sticky="NSEW")
        self.frame_result.grid_forget()

    def put_title(self):
        lbl_Title = tk.Label(self.frame_title, text="Formulas de Prestamos", bg="green", foreground="white",
                             font="white")
        lbl_Title.pack(expand=True)

    def put_form(self):
        self.lblValCredit = tk.Label(self.frame_form, text="Valor del crédito $:")
        self.valTextValCredit = tk.StringVar()
        #vcmd = (self.frame_form.register(self.do_validation), '%P')
        self.txtValCredit = tk.Entry(self.frame_form, font="15", textvariable=self.valTextValCredit)#, validate='key',
                                     #validatecommand=vcmd)
        self.lblValCredit.grid(pady=15, row=1, column=0, sticky="W")
        self.txtValCredit.grid(pady=15, row=1, column=1)
        self.txtValCredit.bind("<KeyRelease>", functools.partial(myfns.validate_like_currency, self))#validate_like_currency(app))

        self.lblInterest = tk.Label(self.frame_form, text="Tasa de interes (%):")
        self.txtInterest = tk.Entry(self.frame_form, font="15")
        self.lblInterest.grid(pady=15, row=2, column=0, sticky="W")
        self.txtInterest.grid(pady=15, row=2, column=1)

        lblNumCuotas = tk.Label(self.frame_form, text="Num de cuotas (meses):")
        self.txtNumCuotas = tk.Entry(self.frame_form, font="15")
        lblNumCuotas.grid(pady=15, row=3, column=0, sticky="W")
        self.txtNumCuotas.grid(pady=15, row=3, column=1)

        self.btnCalculate = tk.Button(self.frame_form, text="Calcular", bg="green", fg="white", command=self.calculate)
        self.btnLimpiar = tk.Button(self.frame_form, text="Limpiar", bg="orange", command=lambda: myfns.clean_form(self, [self.frame_form, self.frame_result]))
        self.btnLimpiar.grid(pady=15, row=4, column=0, sticky="W")
        self.btnCalculate.grid(pady=15, row=4, column=1, sticky="NSEW")

    def put_result(self):
        self.lblPlazo = tk.Label(self.frame_result, text="Plazo:")
        self.txtPlazo = tk.Entry(self.frame_result, font="15", state='readonly')
        self.lblPlazo.grid(pady=15, row=0, column=0, sticky="W")
        self.txtPlazo.grid(pady=15, row=0, column=1)

        self.lblCuota = tk.Label(self.frame_result, text="Cuota mensual a pagar:", anchor='w')
        self.txtCuota = tk.Entry(self.frame_result, font="15", state='readonly')
        self.lblCuota.grid(pady=15, row=1, column=0, sticky="W")
        self.txtCuota.grid(pady=15, row=1, column=1)

        self.lblCostoFinanciacion = tk.Label(self.frame_result, text="Total valor de la financiación:", anchor='e')
        self.txtCostoFinanciacion = tk.Entry(self.frame_result, font="15", state='readonly')
        self.lblCostoFinanciacion.grid(pady=15, row=2, column=0, sticky="W")
        self.txtCostoFinanciacion.grid(pady=15, row=2, column=1)

    def calculate(self):
        print("Calculando...")
        try:
            # DC - Show frame resultados
            self.frame_result.grid(row=5, columnspan=2, sticky="NSEW")

            # DC - Limpia valores de resultados
            #self.clean_results()
            myfns.clean_form(self, [self.frame_result])
            myfns.change_state_entry_form(self, [self.frame_result], "normal")


            cant_prestamo = int(self.txtValCredit.get().replace(".", "").replace(",", ""))
            num_cuotas = int(self.txtNumCuotas.get())
            interes = float(self.txtInterest.get()) / 100

            # DC - Crea objeto Prestamo
            prestamo = Prestamo(cant_prestamo, num_cuotas, interes)

            self.txtPlazo.insert(0, prestamo.numcuotas)
            self.txtCuota.insert(0, myfns.format_currency(prestamo.valCuota))
            self.txtCostoFinanciacion.insert(0, myfns.format_currency(prestamo.costofinanciero))

        except Exception as e:
            self.txtPlazo.insert(0, 'ERROR')
            self.txtCuota.insert(0, 'ERROR')

            self.txtCostoFinanciacion.insert(0, 'ERROR')
        else:
            myfns.change_state_entry_form(self, [self.frame_result], "readonly")


root = tk.Tk()
main_gui = app(root)

root.mainloop()
