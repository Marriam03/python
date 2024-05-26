import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

file_path= 'time_series_19-covid-Confirmed.csv'
confirmed= pd.read_csv(file_path)
#print(confirmed)
def process_data(df):
    #drop unnecessary column
    df=df.drop(['Province/State', 'Lat', 'Long'], axis=1)
    df=df.groupby('Country/Region').sum()
    df=df.transpose()
    df.index= pd.to_datetime(df.index)
    return df

confirmed= process_data(confirmed)
#print(confirmed)

def plot_country(country):
    plt.figure(figsize=(10,6))
    plt.plot(confirmed.index, confirmed[country], label='confimed Casses')
    plt.title(f'covid 19 data for {country}')
    plt.xlabel('Data')
    plt.ylabel('Number of Casses')
    plt.legend()
    plt.show()


def plot():
    contry_name= country.get()
    plot_country(contry_name)

root= tk.Tk()
root.title('Country name')
tk.Label(root, text='Country Name').grid(row=0,column=0,padx=10,pady=5) 
country= tk.Entry(root)
country.grid(row=0, column=1, padx=10,pady=5)

submit_butn= tk.Button( text='Show plot', command=plot)
submit_butn.grid(row=2,column=0,pady=10, columnspan=2)

root.mainloop()