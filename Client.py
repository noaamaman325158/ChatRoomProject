import tkinter
import socket
from tkinter import *
from threading import Thread


#For creating a window via the tkinter module and init the value of the attributes
window = Tk()
window.title("Chat Room App")
window.configure(bg="pink")

message_frame = Frame(window, height=100, width=100, bg="red")
message_frame.pack()

my_message = StringVar()
my_message.set("")

#The UI object Scroll Bar is located inside the message frame that we defined
scroll_bar = Scrollbar(message_frame)

#The UI object List Box is located inside the message frame
msg_list_box = Listbox(message_frame,height="15", width="100", bg="red",yscrollcommand=scroll_bar.set)
msg_list_box.pack(side="left", fill=BOTH)
msg_list_box.pack()


scroll_bar.pack(side="right", fill=Y)
scroll_bar.pack()



mainloop()