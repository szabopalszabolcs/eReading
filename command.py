import threading

def alt_tab():

    from pynput.keyboard import Key, Controller

    keyboard=Controller()
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt_l)
    

def export(f,t):

    alarm = [0,0,0,0,0,0,0]

    if f>t:
        return(('Date citire incorecte','red',0,alarm))

    import requests
    import os
    from tkinter.filedialog import asksaveasfile
    import pathlib
    import time
    import threading

    if f==t:
        file_name='Citiri '+f+'.csv'
    else:
        file_name='Citiri '+f+' - '+t+'.csv'

    try:
        csvFile = asksaveasfile(confirmoverwrite=True,filetypes=[('csv file','*.csv')],initialfile=file_name,initialdir=pathlib.Path.home()/'Documents')
    except PermissionError:
        csvFile = ('Error')
    except :
        pass

    url = 'https://www.temetra.com/wmsapp/epoint/itrongenericcsv'
    params = {'auth':'8c130518ba27fac565c843e89a5171','from':f,'to':t}
    result = requests.get( url , params = params)
    
    if (csvFile!='Error') and (csvFile!=None):
        lines=result.text.splitlines()
        if len(lines)<2:
            file_name=csvFile.name
            if os.path.exists(file_name):
                csvFile.close()
                os.remove(file_name)
            return(('Nu sunt date','red',0,alarm))
        csvFile.write(lines[0]+'\n')
        written_lines=[lines[0]]
        for line in lines:
            is_not=True
            for new_line in written_lines:
                if new_line.split(',')[3]==line.split(',')[3]:
                    is_not=False
            if is_not:
                for ind in range(26,33):
                    if str(line.split(',')[ind])=='true':
                        alarm[ind-26]+=1
                written_lines.append(line)
                csvFile.write(line)
                csvFile.write('\n')
        csvFile.close()
        thread2 = threading.Thread(target=os.startfile(csvFile.name))
        thread2.start()
        thread2.join()
        #os.startfile(csvFile.name)
        time.sleep(1)
        return(('Fisier exportat','black',len(written_lines)-1,alarm))
    else:
        if csvFile=='Error':
            return(('Fisierul este deschis, va rog sa-l inchideti','red',0,alarm))
        else:
            return(('Nu ati selectat fisier','red',0,alarm))
    
def text_output(value):
    
    alarma = ['leakage','history','backflow','blocked','reversed','battery','detection']
    if value[2]==1:
        text=str(value[2])+' contor citit'
        for ind in range(0,7):
            if value[3][ind]>0:
                text=text+'\n'+str(value[3][ind])+' '+alarma[ind]      
    else:
        text=str(value[2])+' contoare citite'
        for ind in range(0,7):
            if value[3][ind]>0:
                text=text+'\n'+str(value[3][ind])+' '+alarma[ind]
    return text

def export_command(from_date,to_date,label_analyze,label_message):

    value=export(str(from_date.get_date()),str(to_date.get_date()))
    label_message.config(text=value[0],foreground=value[1])
    if value[2]>0:
        text = text_output(value)
        label_analyze.config(text=text)
        alt_tab()
        return
    else:
        label_analyze.config(text='')
        return

def export_data(from_date,to_date,label_analyze,label_message):
    
    import threading

    thread1 = threading.Thread(target=export_command(from_date,to_date,label_analyze,label_message))
    thread1.start()
    thread1.join()

    
def exit_command(my_w):
    my_w.destroy()