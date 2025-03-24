import tkinter as tk
from tkinter import ttk, filedialog
import serial
import serial.tools.list_ports
import threading
import csv
from PIL import Image, ImageTk

def open_port():
    global ser, port_open
    if not port_open:
        ser = serial.Serial(port_combo.get(), baudrate=baudrate_combo.get())
        open_button.config(text="Close Port")
        port_open = True
        threading.Thread(target=receive_messages, daemon=True).start()
        received_text.config(state=tk.NORMAL)  
        received_text.insert('1.0', "Port " + port_combo.get() + " conected\n")
        received_text.tag_add("green", '1.0', '2.0')
        received_text.tag_config("green",foreground="green")
        received_text.config(state=tk.DISABLED)  
        send_button.config(state=tk.NORMAL)
        start_button.config(state=tk.NORMAL)
        port_combo.config(state=tk.DISABLED)
        baudrate_combo.config(state=tk.DISABLED)
    else:
        port_open = False
        ser.close()
        open_button.config(text="Open Port")
        received_text.config(state=tk.NORMAL)  
        received_text.insert('1.0', "Port " + port_combo.get() + " disconected\n")
        received_text.tag_config("red",foreground="red")
        received_text.tag_add("red", '1.0', '2.0')
        received_text.config(state=tk.DISABLED) 
        send_button.config(state=tk.DISABLED)
        start_button.config(state=tk.DISABLED)
        port_combo.config(state=tk.NORMAL)
        baudrate_combo.config(state=tk.NORMAL)

def send_message():
    global ser
    ser.write((message_entry.get()+"\n").encode())
    received_text.config(state=tk.NORMAL)  
    received_text.insert('1.0',message_entry.get()+"\n")
    received_text.tag_config("send",foreground="#1E69FF")
    received_text.tag_add("send", '1.0', '2.0')
    received_text.config(state=tk.DISABLED)  

def receive_messages():
    global start_b, file, file_b, file_name_b, filename, writer
    while port_open:
        if ser.in_waiting > 0:
            received_text.config(state=tk.NORMAL)  
            message = ser.readline().decode()
            if "Start" in message:
                received_text.insert('1.0', "Start confirmed\n")
                received_text.tag_config("info",foreground="#e678f5")
                received_text.tag_add("info", '1.0', '2.0')
                start_b = True
                start_button.config(text="    Stop    ")
                if file_name_b:
                    try:
                        file = open(filename, 'w', newline='')
                        writer = csv.writer(file)
                        received_text.insert('1.0', "File opened\n")
                        file_b = True
                    except IOError:
                        received_text.insert('1.0', "File can not be opened \n")
                        file_b = False


            elif "Stop" in message or "Done" in message :
                if "Stop" in message:
                    received_text.insert('1.0', "Measuring stopped.\n")                
                else:
                    received_text.insert('1.0', "Measuring done.\n")
                
                received_text.tag_config("info",foreground="#e678f5")
                received_text.tag_add("info", '1.0', '2.0')
                start_b = False
                start_button.config(text="    Start    ")
                if file_name_b and file_b:
                    file.close()
                    received_text.insert('1.0', "File saved\n")
                    file_b = False
            else:
                received_text.insert('1.0', message)
                if file_b:
                    data = message.strip().split(';')
                    if len(data) > 2:
                        write_line(data)
            
            received_text.config(state=tk.DISABLED)  


def clear_received():
    received_text.config(state=tk.NORMAL)  
    received_text.delete('1.0', tk.END)
    received_text.config(state=tk.DISABLED)  

def load_csv():
    global file,file_name_b,filename
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    file_entry.delete(0,tk.END)
    file_entry.insert(0,filename)
    file_name_b = True

def write_line(data):
    global writer
    writer.writerow(data)

def start():   
    global ser, start_b

    received_text.config(state=tk.NORMAL)  
    
    if not start_b:
        received_text.insert('1.0', "Start measure (" + timestep_entry.get() +" ms, " + maxtime_entry.get() + " s, " + mincur_entry.get() +" mA, " + maxcur_entry.get() +" mA, " + minimalduration_entry.get() +" ms, " + maximalduration_entry.get() +" ms)\n")
        received_text.tag_config("send",foreground="#1E69FF")
        received_text.tag_add("send", '1.0', '2.0')
        ser.write(("Start;"+ timestep_entry.get() +";" + maxtime_entry.get() + ";" + mincur_entry.get() + ";" + maxcur_entry.get() + ";" + minimalduration_entry.get() + ";" + maximalduration_entry.get() + "\n").encode())

    else:
        received_text.insert('1.0', "Stop measure\n")
        received_text.tag_config("send",foreground="#1E69FF")
        received_text.tag_add("send", '1.0', '2.0')
        ser.write(("Stop\n").encode())

    received_text.config(state=tk.DISABLED)  

# hlavní okno
root = tk.Tk()
root.title("Elastoměr")
ico = Image.open('technology.png')
photo = ImageTk.PhotoImage(ico)
root.iconphoto(False, photo)
file = None
writer = None 

#hlavní pack
main_frame = tk.LabelFrame(root, padx=5, pady=5)
main_frame.pack(padx=10, pady=10,fill=tk.BOTH)

# Vytvoření kontejneru
ser_labelframe = tk.LabelFrame(main_frame, text="Serial communication", padx=5, pady=5)
ser_labelframe.pack(padx=10, pady=5,fill=tk.BOTH)


ser_first_line_frame = tk.Frame(ser_labelframe, padx=5, pady=5)
ser_first_line_frame.pack(padx=0, pady=0,fill=tk.BOTH)

port_label = tk.Label(ser_first_line_frame,text="Port: ")
port_label.pack(padx=1, pady=1,side=tk.LEFT)

# COM port selection
ports = serial.tools.list_ports.comports()
port_combo = ttk.Combobox(ser_first_line_frame, values=[port.device for port in ports])
port_combo.pack(padx=1, pady=1,side=tk.LEFT)
port_combo.set("COM5")

baudrate_label = tk.Label(ser_first_line_frame,text="Baudrate: ")
baudrate_label.pack(padx=10, pady=1,side=tk.LEFT)

# Baudrate selection
baudrate_combo = ttk.Combobox(ser_first_line_frame, values=[9600, 14400, 19200, 38400, 57600, 115200])
baudrate_combo.pack(padx=1, pady=1,side=tk.LEFT)
baudrate_combo.set(115200)

# Open port button
port_open = False

space_label = tk.Label(ser_first_line_frame,text=" ")
space_label.pack(padx=1, pady=1,side=tk.LEFT,fill=tk.BOTH, expand=1)

open_button = ttk.Button(ser_first_line_frame, text="Open Port", command=open_port)
open_button.pack(padx=1, pady=1,side=tk.LEFT)

ser_second_line_frame = tk.Frame(ser_labelframe, padx=5, pady=5)
ser_second_line_frame.pack(padx=0, pady=0,fill=tk.BOTH)

# Message entry, send and clear button
message_entry = tk.Entry(ser_second_line_frame)
message_entry.pack(padx=1, pady=1,side=tk.LEFT,fill=tk.BOTH, expand=1)

send_button = ttk.Button(ser_second_line_frame, text="Send Message", command=send_message)
send_button.pack(padx=10, pady=1,side=tk.LEFT)
send_button.config(state=tk.DISABLED)


clear_button = ttk.Button(ser_second_line_frame, text="Clear Received", command=clear_received)
clear_button.pack(padx=1, pady=1,side=tk.LEFT)

# Vytvoření kontejneru
data_labelframe = tk.LabelFrame(main_frame, text="Data", padx=5, pady=5)
data_labelframe.pack(padx=10, pady=5,fill=tk.BOTH)

data_zero_line_frame = tk.Frame(data_labelframe, padx=5, pady=5)
data_zero_line_frame.pack(padx=0, pady=0,fill=tk.BOTH)

file_label = ttk.Label(data_zero_line_frame,text="File:  ")
file_label.pack(padx=1, pady=1,side=tk.LEFT)

file_entry = tk.Entry(data_zero_line_frame)
file_entry.pack(padx=1, pady=1,side=tk.LEFT,fill=tk.BOTH, expand=1)

space_label4 = tk.Label(data_zero_line_frame,text=" ")
space_label4.pack(padx=1, pady=1,side=tk.LEFT)

load_button = ttk.Button(data_zero_line_frame, text="    Choose    ", command=load_csv)
load_button.pack(padx=1, pady=1,side=tk.LEFT)

data_first_line_frame = tk.Frame(data_labelframe, padx=5, pady=5)
data_first_line_frame.pack(padx=0, pady=0,fill=tk.BOTH)

timestep_label = tk.Label(data_first_line_frame,text="Time step [ms]:             ")
timestep_label.pack(padx=1, pady=1,side=tk.LEFT)


timestep_entry = tk.Entry(data_first_line_frame)
timestep_entry.pack(padx=1, pady=1,side=tk.LEFT,fill=tk.BOTH)
timestep_entry.insert(0,"120")


maxtime_label = tk.Label(data_first_line_frame,text="End time [s]:                   ")
maxtime_label.pack(padx=10, pady=1,side=tk.LEFT)


maxtime_entry = tk.Entry(data_first_line_frame)
maxtime_entry.pack(padx=1, pady=1,side=tk.LEFT,fill=tk.BOTH)
maxtime_entry.insert(0,"5000")

space_label1 = tk.Label(data_first_line_frame,text=" ")
space_label1.pack(padx=1, pady=1,side=tk.LEFT,fill=tk.BOTH, expand=1)

# Open port button
start_b = False

file_b = False
file_name_b = False

data_second_line_frame = tk.Frame(data_labelframe, padx=5, pady=5)
data_second_line_frame.pack(padx=0, pady=0,fill=tk.BOTH)

mincur_label = tk.Label(data_second_line_frame,text="Minimal current [mA]: ")
mincur_label.pack(padx=1, pady=1,side=tk.LEFT)


mincur_entry = tk.Entry(data_second_line_frame)
mincur_entry.pack(padx=1, pady=1,side=tk.LEFT,fill=tk.BOTH)
mincur_entry.insert(0,"-1400")


maxcur_label = tk.Label(data_second_line_frame,text="Maximal current [mA]: ")
maxcur_label.pack(padx=10, pady=1,side=tk.LEFT)


maxcur_entry = tk.Entry(data_second_line_frame)
maxcur_entry.pack(padx=1, pady=1,side=tk.LEFT,fill=tk.BOTH)
maxcur_entry.insert(0,"1400")

# Open port button
start_b = False

space_label2 = tk.Label(data_second_line_frame,text=" ")
space_label2.pack(padx=1, pady=1,side=tk.LEFT,fill=tk.BOTH, expand=1)

data_third_line_frame = tk.Frame(data_labelframe, padx=5, pady=5)
data_third_line_frame.pack(padx=0, pady=0,fill=tk.BOTH)

minimalduration_label = tk.Label(data_third_line_frame,text="Minimal interval [ms]:  ")
minimalduration_label.pack(padx=1, pady=1,side=tk.LEFT)


minimalduration_entry = tk.Entry(data_third_line_frame)
minimalduration_entry.pack(padx=1, pady=1,side=tk.LEFT,fill=tk.BOTH)
minimalduration_entry.insert(0,"480")


maximalduration_label = tk.Label(data_third_line_frame,text="Maximal interval [ms]:  ")
maximalduration_label.pack(padx=10, pady=1,side=tk.LEFT)


maximalduration_entry = tk.Entry(data_third_line_frame)
maximalduration_entry.pack(padx=1, pady=1,side=tk.LEFT,fill=tk.BOTH)
maximalduration_entry.insert(0,"720")

space_label3 = tk.Label(data_third_line_frame,text=" ")
space_label3.pack(padx=1, pady=1,side=tk.LEFT,fill=tk.BOTH, expand=1)

# start measure button
start_button = ttk.Button(data_third_line_frame, text="    Start    ", command=start)
start_button.pack(padx=1, pady=1,side=tk.LEFT)
start_button.config(state=tk.DISABLED)

# Received messages text box
received_text = tk.Text(main_frame)


scrollb = ttk.Scrollbar(main_frame, command=received_text.yview)
received_text['yscrollcommand'] = scrollb.set
scrollb.pack(side=tk.RIGHT,fill=tk.Y)

received_text.pack(side=tk.LEFT,fill=tk.BOTH)
received_text.config(state=tk.DISABLED)

root.mainloop()