import tkinter
import socket
from tkinter import *
from threading import Thread
from auxilary_data import PORT, HOST_IP, MAX_SIZE_MESSAGE

#Implement main methods right below
def receive():
    while True:
        try:
            msg = sock.recv(MAX_SIZE_MESSAGE).decode('utf-8')
            #Insert the message inside the GUI component in the end of the box list
            msg_list_box.insert(tkinter.END, msg)
        except:
            print("There is an error while receiving the message")

def send():
    #Get the content from the UI component of the input
    msg = my_message.get()
    #Clean the input box
    my_message.set("")
    #Send the message over the socket
    sock.send(bytes(msg, "utf-8"))
    if msg == "#quit":
        #Close the relevant resources in quit scenario
        sock.close()
        window.close()
def on_closing():
    my_message.set("#quit")
    send()
    window.destroy()  # Use this to close the tkinter window


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


label = Label(window,text="Enter the message", fg="black", font="Aria",bg="grey")
label.pack()

entry_field = Entry(window,textvariable=my_message, fg="red", width=50)
entry_field.pack()

send_button = Button(window,text="Send", font="Aria", fg="White", command=send)
send_button.pack()

quit_button = Button(window, text="Quit", font="Aria", fg="White", command=on_closing)
quit_button.pack()

Host = HOST_IP
Port = PORT

#Establish some socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((Host, Port))

receive_messages_thread = Thread(target=receive)
receive_messages_thread.start()



mainloop()