# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:30:39 2021

@author: Nerazeem
"""

import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pymysql
import tkinter as tk
import tkinter.ttk as ttk


#utworzenie połączenia z bazą
connection = pymysql.connect(host="localhost",user="root",passwd="",database="projekt", autocommit=True)
cursor = connection.cursor()   

#pobranie danych i zapisanie w DataFrame



okno_main = tk.Tk()
okno_main.title('Aplikacja')
okno_main.geometry("250x100")

def wykres_bit():
    #utworzenie okna programu
    okno = tk.Tk()
    okno.title('Aplikacja do wykresów')
    okno.geometry("350x300")
    
    df1 = pd.read_sql('SELECT * FROM `bilans`', con=connection)
    df1.sort_values(by=["data"], inplace=True)
    
    daty_odczytu = df1["data"].tolist()

    #utworzenie kontrolek    
    t1 = tk.StringVar()
    t2 = tk.StringVar()   

    l2= tk.Label(okno, text="Podaj datę początkową (YYYY-MM-DD): ")
    c1 = ttk.Combobox(okno, textvariable=t1)
    c1['values'] = daty_odczytu
    l3= tk.Label(okno, text="Podaj datę końcową (YYYY-MM-DD): ")
    c2 = ttk.Combobox(okno, textvariable=t2)
    c2['values'] = daty_odczytu
        
    
    def dzialaj():       
        # Pobranie danych od użytkownika

        czas1 = c1.get()
        czas2 = c2.get()  

        df_tmp = df1[["data","ilosc"]]
        czas = (df_tmp['data'] >= czas1) & (df_tmp['data'] <= czas2)
        df_tmp1 = df1[["data","wartosc"]]
    

        dfc1 = pd.DataFrame(df_tmp[czas])
        dfc2 = pd.DataFrame(df_tmp1[czas])
    
        dfc1.set_index('data', inplace=True)
        dfc2.set_index('data', inplace=True)
        
        wykres = tk.Tk()
        wykres.title("Wykres")
        wykres.geometry("+100+1")
    
        lf = ttk.Labelframe(wykres, text='Wykres')
        lf.grid(row=0, column=0, sticky='nwes', padx=3, pady=3)

        fig = Figure(figsize=(5,4), dpi=100)
        ax = fig.add_subplot(111)
    
    
        print(dfc1)
        print(dfc2)
        #utworzenie wykresu i pokazanie go w nowym oknie
        dfc1.plot(figsize=(10, 10), linewidth=2.5, ax=ax, rot=45, fontsize=8)
        dfc2.plot(figsize=(10, 10), linewidth=2.5, ax=ax, rot=45, secondary_y=True, fontsize=8)

    
        ax.set_ylabel("Ilość zamówień")
        ax.right_ax.set_ylabel("Wartość zamówień")
   
    
        canvas = FigureCanvasTkAgg(fig, master=lf)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)

        wykres.mainloop()
        
    btn = tk.Button(okno, text='Rysuj wykres', command = dzialaj)
    

    # Dodanie elementów do okna
    l2.pack()
    c1.pack()
    l3.pack()
    c2.pack()
    btn.pack()

    okno.mainloop()

  
def okno_csv():
    okno2 = tk.Tk()
    okno2.title('Aplikacja zapisu danych w CSV')   
    
    # Utworzenie kontrolek    
    d1 = tk.StringVar()
    d2 = tk.StringVar()
    d3 = tk.StringVar()
    
    elementy1 = ttk.Entry(okno2, textvariable=d1)
    elementy2 = ttk.Entry(okno2, textvariable=d2)
    elementy3 = ttk.Entry(okno2, textvariable=d3)
    

    
    l1= tk.Label(okno2, text="Podaj datę: ")
    l2= tk.Label(okno2, text="Podaj ilość zamówień: ")
    l3= tk.Label(okno2, text="Podaj wartość wszystkich zamówień: ")
    

    def dodaj_bilans():            

        # Pobranie danych od użytkownika
        parametr1 = elementy1.get()
        parametr2 = elementy2.get()
        parametr3 = elementy3.get()
        
        insert = "INSERT INTO `bilans` VALUES ('" + parametr1 + "'," + parametr2 + "," + parametr3 +");" 
        cursor.execute(insert)
        print("Bilans dodany")
            
            
    
    btn1 = tk.Button(okno2, text='Dodaj dane', command = dodaj_bilans)

    # Dodanie elementów do okna
    l1.pack()
    elementy1.pack()   
    l2.pack()
    elementy2.pack()
    l3.pack()
    elementy3.pack()
    btn1.pack()

    okno2.mainloop()


# Utworzenie przycisków dla okna głównego
btn_w = tk.Button(okno_main, text='Wykres', command = wykres_bit).pack()
btn_c = tk.Button(okno_main, text='Dodaj bilans', command = okno_csv).pack()

# Wywołanie okna głównego
okno_main.mainloop()

# Zamknięcie połączenia z bazą
connection.close()