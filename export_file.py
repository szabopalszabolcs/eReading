def export(from_date,to_date):

    if from_date>to_date:
        label_message.config(text='Date citire incorecte',foreground='red')

    import requests
    import os
    from tkinter.filedialog import asksaveasfile
    import pathlib
    import time

    if from_date==to_date:
        file_name='Citiri '+from_date+'.csv'
    else:
        file_name='Citiri '+from_date+' - '+to_date+'.csv'

    try:
        csvFile = asksaveasfile(confirmoverwrite=True,filetypes=[('csv file','*.csv')],initialfile=file_name,initialdir=pathlib.Path.home()/'Documents')
    except PermissionError:
        csvFile = ('Error')
    except :
        pass

    url = 'https://www.temetra.com/wmsapp/epoint/itrongenericcsv'
    params = {'auth':'8c130518ba27fac565c843e89a5171','from':from_date,'to':to_date}
    result = requests.get( url , params = params)
    
    if (csvFile!='Error') and (csvFile!=None):
        lines=result.text.splitlines()
        if len(lines)<2:
            if os.path.exists(file_name):
                csvFile.close()
                os.remove(file_name)
            label_message.config(text='Nu sunt date',foreground='red')
        csvFile.write(lines[0]+'\n')
        written_lines=[lines[0]]
        for line in lines:
            is_not=True
            for new_line in written_lines:
                if new_line.split(',')[3]==line.split(',')[3]:
                    is_not=False
            if is_not:
                written_lines.append(line)
                csvFile.write(line)
                csvFile.write('\n')
        csvFile.close()
        os.startfile(csvFile.name)
        label_message.config(text='Fisier exportat',foreground='black')
    else:
        if csvFile=='Error':
            label_message.config(text='Fisierul este deschis, va rog sa-l inchideti',foreground='red')
        else:
            label_message.config(text='Nu ati selectat fisier',foreground='red')
        
def exit_command(my_w):
    my_w.destroy()

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
                        [label_message.config(text=''),
                         export(str(from_date.get_date()),str(to_date.get_date()))])
button_export.grid(row=3,column=1,pady=10,sticky='W')
button_quit=tk.Button(my_w,text='Iesire',width=10,font=font1,command=lambda:exit_command(my_w))
button_quit.grid(row=3,column=2,pady=10,sticky='E')

my_w.mainloop()