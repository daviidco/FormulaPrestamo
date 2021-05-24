import tkinter
import decimal
mainWindow = tkinter.Tk()
mainWindow.geometry("900x500")

# DC - Main title
mainWindow.title("Programa de calculo de prestamos")


frame_title = tkinter.Frame(mainWindow, bg="green", height=40)
frame_title.pack(side="top", fill='both')
frame_title.pack_propagate(0)
lblTitle = tkinter.Label(frame_title, text="Formulas de Prestamos", bg="green", foreground="white", font="white")#, width=100)
lblTitle.pack(expand=True)


frame_form = tkinter.Frame(mainWindow)
frame_form.pack(side="bottom", expand=True)

def do_validation(new_value):
	return new_value == "" or new_value.isnumeric()




lblValCredit = tkinter.Label(frame_form, text="Valor del crédito $:")
valTextValCredit = tkinter.StringVar()
#vcmd = (frame_form.register(do_validation), '%P')
txtValCredit = tkinter.Entry(frame_form, font="15", textvariable=valTextValCredit)#, validate='key', validatecommand=vcmd)
lblValCredit.grid(pady=15, row=1, column=0, sticky="W")
txtValCredit.grid(pady=15, row=1, column=1)



def validate_key(key):
	if key.char.isnumeric() or key.keycode == 8 or key.keycode == 46:
		value = txtValCredit.get()
		value = format_currency(value, "", 0, True)
		valTextValCredit.set(value)
		if not (key.keycode == 8 or key.keycode == 46):
			txtValCredit.icursor(tkinter.END)


txtValCredit.bind("<KeyRelease>", validate_key)

lblInterest = tkinter.Label(frame_form, text="Tasa de interes (%):")
txtInterest = tkinter.Entry(frame_form, font="15")
lblInterest.grid(pady=15, row=2, column=0, sticky="W")
txtInterest.grid(pady=15, row=2, column=1)

lblNumCuotas = tkinter.Label(frame_form, text="Número de cuotas (meses):")
txtNumCuotas = tkinter.Entry(frame_form, font="15")
lblNumCuotas.grid(pady=15, row=3, column=0, sticky="W")
txtNumCuotas.grid(pady=15, row=3, column=1)


def format_currency(value, simbol="$", limit=2, reformat=False):

	thousands_separator = "."
	fractional_separator = ","
	if not reformat:
		value = simbol + "{:,.2f}".format(int(value))
		if thousands_separator == ".":
			main_currency, fractional_currency = value.split(".")[0], value.split(".")[1]
			new_main_currency = main_currency.replace(",", ".")
			value = new_main_currency + fractional_separator + fractional_currency
	if reformat:
		value = str(value).replace('.', '')
		value = simbol + "{:,}".format(int(value))
		if thousands_separator == ".":
			main_currency = value.split(".")[0]
			new_main_currency = main_currency.replace(",", ".")
			value = new_main_currency

	return value

def clean_form():
	txtInterest.delete(0, tkinter.END)
	txtNumCuotas.delete(0, tkinter.END)
	txtValCredit.delete(0, tkinter.END)
	txtPlazo['state'] = 'normal'
	txtCuota['state'] = 'normal'
	txtCostoFinanciacion['state'] = 'normal'
	txtPlazo.delete(0, tkinter.END)
	txtCuota.delete(0, tkinter.END)
	txtCostoFinanciacion.delete(0, tkinter.END)
	txtPlazo['state'] = 'readonly'
	txtCuota['state'] = 'readonly'
	txtCostoFinanciacion['state'] = 'readonly'

def clean_fields():
	txtPlazo['state'] = 'normal'
	txtCuota['state'] = 'normal'
	txtCostoFinanciacion['state'] = 'normal'
	txtPlazo.delete(0, tkinter.END)
	txtCuota.delete(0, tkinter.END)
	txtCostoFinanciacion.delete(0, tkinter.END)

def calculate():
	print("Calculando...")
	try:
		frame_result.grid(row=5, columnspan=2, sticky="NSEW")
		clean_fields()

		totalCant = int(txtValCredit.get().replace(".","").replace(",",""))
		interest = float(txtInterest.get())/100
		numCuot = int(txtNumCuotas.get())
		#decimal.getcontext().prec = 100
		valCuot = totalCant*((interest*((1+interest)**numCuot))/(((1+interest)**numCuot)-1))
		totalPay = valCuot * numCuot
		difPay = totalPay - totalCant
		valCuot = format_currency(valCuot)
		totalPay = format_currency(totalPay)
		difPay = format_currency(difPay)



		txtPlazo.insert(0, numCuot)
		txtCuota.insert(0, valCuot)
		txtCostoFinanciacion.insert(0, difPay)

	except Exception as e:
		txtPlazo.insert(0, 'ERROR')
		txtCuota.insert(0, 'ERROR')
		txtCostoFinanciacion.insert(0, 'ERROR')
	else:
		txtPlazo['state'] = 'readonly'
		txtCuota['state'] = 'readonly'
		txtCostoFinanciacion['state'] = 'readonly'



btnCalculate = tkinter.Button(frame_form, text="Calcular", bg="green", fg="white", command=lambda: calculate())
btnLimpiar = tkinter.Button(frame_form, text="Limpiar", bg="orange", command=lambda: clean_form())
btnLimpiar.grid(pady=15, row=4, column=0, sticky="W")
btnCalculate.grid(pady=15, row=4, column=1, sticky="NSEW")

frame_result = tkinter.Frame(frame_form)
frame_result.grid(row=5, columnspan=2, sticky="NSEW")
frame_result.grid_forget()
#frame_result.pack_propagate(0)

lblPlazo = tkinter.Label(frame_result, text="Plazo:")
txtPlazo = tkinter.Entry(frame_result, font="15", state='readonly')
lblPlazo.grid(pady=15, row=0, column=0, sticky="W")
txtPlazo.grid(pady=15, row=0, column=1)

lblCuota = tkinter.Label(frame_result, text="Cuota mensual a pagar:", anchor='w')
txtCuota = tkinter.Entry(frame_result, font="15", state='readonly')
lblCuota.grid(pady=15, row=1, column=0, sticky="W")
txtCuota.grid(pady=15, row=1, column=1)

lblCostoFinanciacion = tkinter.Label(frame_result, text="Total valor de la financiación:", anchor='e')
txtCostoFinanciacion = tkinter.Entry(frame_result, font="15", state='readonly')
lblCostoFinanciacion.grid(pady=15, row=2, column=0, sticky="W")
txtCostoFinanciacion.grid(pady=15, row=2, column=1)

#lblResult = tkinter.Label(frame_result, foreground="green", font=("Verdana", 15))
#lblResult.pack(side="left")

#lblResult.grid(pady=15, row=5, column=0, columnspan="2")

mainWindow.bind('<Return>', lambda event=None: btnCalculate.invoke())

mainWindow.mainloop() 