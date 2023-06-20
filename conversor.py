import requests
import tkinter as tk
from tkinter import ttk,messagebox
class Conversor(tk.Tk):
    __dolares=None
    __pesos=None
    def __init__(self): 
        super().__init__()
        self.title('Conversor de moneda')
        self.geometry('300x100')

        self.__pesos=tk.StringVar()
        pesos=ttk.Label(self,textvariable=self.__pesos).grid(row=1,column=1)

        self.__dolares=tk.StringVar()
        self.__dolares.trace('w',self.calcular)
        dolares=ttk.Entry(self,textvariable=self.__dolares,width=10).grid(row=0,column=1,sticky='E')

        dolaresLb=tk.Label(self,text='dólares').grid(row=0,column=2,sticky='W')

        equivalente=tk.Label(self,text='es equivalente a').grid(row=1,column=0,sticky='E')

        
        pesosLb=tk.Label(self,text='pesos').grid(row=1,column=2,sticky='W')

        salir=tk.Button(self,text='Salir',command=quit,padx=15,pady=3).grid(row=2,column=2)


    def calcular(self,*args):
        if self.__dolares.get()!='': 
            try: 
                valor=float(self.__dolares.get()) 
                venta=self.obtenerAPI()
                self.__pesos.set(round(venta*valor,2)) 
            except ValueError:
                messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico') 
                self.__dolares.set('') 
        else: 
            self.__pesos.set('')

    def obtenerAPI(self):
        url = 'https://www.dolarsi.com/api/api.php?type=dolar'
        try:
            data = requests.get(url)
            if data.status_code==200:
                data = data. json()
                oficial=float(data[0]['casa']['venta'].replace(',','.'))
                return oficial
        except requests.exceptions.RequestException as e:
            messagebox.showerror(title='Error', message="Error al obtener la cotizacion del dolar")
            return None

