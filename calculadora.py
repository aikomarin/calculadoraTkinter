import tkinter as tk
from tkinter import messagebox


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()

        # Ventana
        self.geometry('325x345+650+300')
        self.resizable(0, 0)
        self.title('Calculadora')
        self.iconbitmap('calc.ico')

        self.expresion = ''  # Generar un str vacío para lo que se va a ingresar
        self.entrada = None  # Entrada de texto
        self.entrada_texto = tk.StringVar()  # Convertir a una variable str para hacerlo una cadena
        self._creacion_componentes()  # Llamar al método

    def _creacion_componentes(self):
        # Frame para el visor
        visor_frame = tk.Frame(self, width=400, height=50, bg='black')
        visor_frame.pack(side=tk.TOP)

        visor = tk.Entry(visor_frame, bg='#FFBE0B', font=('Dosis', 18, 'bold'), width=24, justify=tk.RIGHT,
                         textvariable=self.entrada_texto)
        visor.grid(row=0, column=0, ipady=10)

        # Frame para los botones
        botones_frame = tk.Frame(self, width=400, height=450, bg='black')
        botones_frame.pack()

        # Botones
        # Renglón 0
        boton_limpiar = tk.Button(botones_frame, text='C', fg='#3A86FF', bg='#8338EC', bd=0,
                                  font=('Dosis', 18, 'bold'), cursor='hand2', width=18, height=1,
                                  command=self._limpiar)
        boton_limpiar.grid(row=0, column=0, padx=1, pady=1, columnspan=3, sticky='WE')

        boton_dividir = tk.Button(botones_frame, text='/', fg='#3A86FF', bg='#8338EC', bd=0,
                                  font=('Dosis', 18, 'bold'), cursor='hand2', width=6, height=1,
                                  command=lambda: self._click('/'))
        boton_dividir.grid(row=0, column=3, padx=1, pady=1, sticky='WE')

        # Renglones 1, 2 y 3
        botones = ['7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+']
        botones_guardados = []
        fila = 1
        columna = 0

        for boton in botones:
            boton = tk.Button(botones_frame, text=boton.title(), fg='#3A86FF', bg='#8338EC', bd=0,
                              font=('Dosis', 18, 'bold'), cursor='hand2', width=6, height=1)
            botones_guardados.append(boton)
            boton.grid(row=fila, column=columna, padx=1, pady=1)
            columna += 1  # Se van incrementando las columnas
            if columna == 4:  # Cuando llegue a la columna 4 (es la última)
                fila += 1  # Se pasa a la siguiente fila
                columna = 0  # La columna se reinicia en 0 para agregar los botones

        botones_guardados[0].config(command=lambda: self._click('7'))
        botones_guardados[1].config(command=lambda: self._click('8'))
        botones_guardados[2].config(command=lambda: self._click('9'))
        botones_guardados[3].config(command=lambda: self._click('*'))
        botones_guardados[4].config(command=lambda: self._click('4'))
        botones_guardados[5].config(command=lambda: self._click('5'))
        botones_guardados[6].config(command=lambda: self._click('6'))
        botones_guardados[7].config(command=lambda: self._click('-'))
        botones_guardados[8].config(command=lambda: self._click('1'))
        botones_guardados[9].config(command=lambda: self._click('2'))
        botones_guardados[10].config(command=lambda: self._click('3'))
        botones_guardados[11].config(command=lambda: self._click('+'))

        # Renglón 4
        boton_cero = tk.Button(botones_frame, text='0', fg='#3A86FF', bg='#8338EC', bd=0,
                                  font=('Dosis', 18, 'bold'), cursor='hand2', width=12, height=1,
                                  command=lambda: self._click('0'))
        boton_cero.grid(row=4, column=0, padx=1, pady=1, columnspan=2, sticky='WE')

        boton_punto = tk.Button(botones_frame, text='.', fg='#3A86FF', bg='#8338EC', bd=0,
                               font=('Dosis', 18, 'bold'), cursor='hand2', width=6, height=1,
                               command=lambda: self._click('.'))
        boton_punto.grid(row=4, column=2, padx=1, pady=1)

        boton_evaluar = tk.Button(botones_frame, text='=', fg='#3A86FF', bg='#8338EC', bd=0,
                                  font=('Dosis', 18, 'bold'), cursor='hand2', width=6, height=1,
                                  command=self._evaluar)
        boton_evaluar.grid(row=4, column=3, padx=1, pady=1)

    def _evaluar(self):
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))  # Evalúa la expresión de tipo str como una expresión aritmética
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Error: {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion = ''

    def _limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _click(self, boton):
        self.expresion = f'{self.expresion}{boton}'
        self.entrada_texto.set(self.expresion)


if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()
