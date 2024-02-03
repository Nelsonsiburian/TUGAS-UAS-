# pysimpleGUI itu apa
# panda itu apa dan fungsinya apa
import PySimpleGUI as sg
import pandas as pd
# sg.theme itu apa ('DarkGreen4') buata apa
sg.theme('DarkGreen4')

EXCEL_FILE = 'Pendaftaran.xlsx'

df = pd.read_excel(EXCEL_FILE)
# kenapa sg ya beda beda contoh sg.inputtext sg.miltiline dll
layout=[
[sg.Text('Masukkan Data Kamu: ')],
[sg.Text('Nama',size=(15,1)), sg.InputText(key='Nama')],
[sg.Text('No Telp',size=(15,1)), sg.InputText(key='Tlp')],
[sg.Text('Alamat',size=(15,1)), sg.Multiline(key='alamat')],
[sg.Text('Tgl Lahir',size=(15,1)), sg.InputText(key='Tgl Lahir'),
                                    sg.CalendarButton('Kalender', target='Tgl Lahir', format=('%d-%M-%y'))],
[sg.Text('Jenis Kelamin',size=(15,1)), sg.Combo(['pria','wanita'])],
[sg.Text('Hobi',size=(15,1)), sg.Checkbox('Belajar',key='Belajar'),
                             sg.Checkbox('Menonton',key='Menonton'),
                             sg.Checkbox('Musik',key='Musik'),],
[sg.Submit(), sg.Button('clear'), sg.Exit]

]


window=sg.Window('from pendaftaran',layout)

def clear_input():
    for key in values:
        window[key]('')
        return None
# while itu buat apa 
while True :
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    if event == 'Clear':   
        clear_input()
    if event == 'Submit':
        df =df._append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False) 
        sg.popup('Data Berhasil Di Simpan')
        clear_input()
window.close()        

