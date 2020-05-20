# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:44:41 2020

@author: Om
"""

from covid import Covid
import tkinter as tk
from tkinter import messagebox as mb
from pandas import DataFrame



def track():
    covid = Covid()


   

    

    Country_name= covid.get_status_by_country_name(country.get())

    data={
            key:Country_name[key]
            for key in Country_name.keys() and {'confirmed',
                              'active',
                              'deaths',
                              'recovered'}
            }
    print(data)
    mb.showinfo("Covid status",data)
    my_dict=data
    
    df = DataFrame(list(my_dict.items()),columns = ['column1','column2']) 
    print(df)
root=tk.Tk()
L1=tk.Label(root,text="Country")
b1=tk.Button(root , text="submit", font = 30, width = 10, command=track)
country= tk.Entry(root)
L1.grid(row=0,column=0)
country.grid(row=0,column=1)
b1.grid(row=1,column=1)
root.mainloop()



