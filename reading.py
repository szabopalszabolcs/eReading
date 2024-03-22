import command as fnc
import tkinter  as tk 
from dateentry import DateEntry

bground = 'lightgrey'
font1 = ('Calibri',11)
font2 = ('Calibri',10)

my_w = tk.Tk()
my_w.configure(padx=20,pady=20,background=bground)
my_w.title('Export reading')


label_from=tk.Label(my_w,text='Data inceput perioada',background=bground,font=font1)
label_from.grid(row=1,column=1,pady=10,sticky='W')
label_from=tk.Label(my_w,text='Data sfarsit perioada',background=bground,font=font1)
label_from.grid(row=2,column=1,pady=10,sticky='W')

from_date=DateEntry(my_w,selectmode='day')
from_date.grid(row=1,column=2)
to_date=DateEntry(my_w,selectmode='day')
to_date.grid(row=2,column=2)

label_message=tk.Label(my_w,wraplength=125,background=bground,font=font2)
label_message.grid(row=4,column=1,sticky='W',rowspan=2)
label_analyze=tk.Label(my_w,background=bground,font=font2)
label_analyze.grid(row=4,column=2,pady=10,sticky='E')

button_export=tk.Button(my_w,text='Export',width=10,font=font1,command=lambda:
                        fnc.export_data(from_date,to_date,label_analyze,label_message))
button_export.grid(row=3,column=1,pady=10,sticky='W')
button_quit=tk.Button(my_w,text='Iesire',width=10,font=font1,command=lambda:fnc.exit_command(my_w))
button_quit.grid(row=3,column=2,pady=10,sticky='E')

my_w.resizable(False,False)
my_w.mainloop()