from tkinter import *
from PIL import Image, ImageTk

whatsappautomation = Tk()
whatsappautomation.geometry('600x580+350+40')
whatsappautomation.resizable(0,0)
whatsappautomation.title("whatsapp Automation")

canvas=Canvas(whatsappautomation,width=2000,height=2000)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\jeevan s koushik\\Downloads\\whatsapp.jpeg"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

label_7 = Label(whatsappautomation, text="-JSK.", fg="white", bg="black")
label_7.place(x=500, y=500)

#The below code is for sending private message.
def private():
    def what():
        import pywhatkit
        n = num.get()
        t = txt.get()
        th = thr.get()
        th = int(th)
        ts = tse.get()
        ts = int(ts)
        pywhatkit.sendwhatmsg(n, t, th, ts)

    num = StringVar()
    txt = StringVar()
    thr = StringVar()
    tse = StringVar()
    label_1 = Label(whatsappautomation, text="ENTER THE WHATSAPP NUMBER:", fg="white", bg="black")
    label_1.place(x=100, y=250)
    num = Entry(whatsappautomation, textvariable=num, bg="lightblue", width=30, borderwidth=3)
    num.place(x=290, y=250)
    L2 = Label(whatsappautomation, text="TEXT TO BE SEND:", fg="white", bg="black")
    L2.place(x=100, y=300)
    txt = Entry(whatsappautomation, textvariable=txt, bg="lightblue", width=30, borderwidth=3)
    txt.place(x=290, y=300)
    L3 = Label(whatsappautomation, text="TIME IN HOURS:", fg="white", bg="black")
    L3.place(x=100, y=350)
    thr = Entry(whatsappautomation, textvariable=thr, bg="lightblue", width=30, borderwidth=3)
    thr.place(x=290, y=350)
    L4 = Label(whatsappautomation, text="TIME IN MINUTE:", fg="white", bg="black")
    L4.place(x=100, y=400)
    tse = Entry(whatsappautomation, textvariable=tse, bg="lightblue", width=30, borderwidth=3)
    tse.place(x=290, y=400)
    DONE = Button(whatsappautomation, text="DONE", width=5, height=2, fg="white", bg="black", command=what)
    DONE.place(x=250, y=450)

#The below code is to sending the group message.
def group():
    def groupping():
        import pywhatkit
        Id=ab.get()
        T=text.get()
        hour=hours.get()
        hour=int(hour)
        minute=minutes.get()
        minute=int(minute)
        pywhatkit.sendwhatmsg_to_group(Id,T,hour,minute)

    ab=StringVar()
    text=StringVar()
    hours=StringVar()
    minutes=StringVar()
    label_1 = Label(whatsappautomation, text="ENTER THE WHATSAPP GROUP ID:", fg="white", bg="black")
    label_1.place(x=95, y=250)
    num = Entry(whatsappautomation, textvariable=ab, bg="lightblue", width=30, borderwidth=3)
    num.place(x=290, y=250)
    L2 = Label(whatsappautomation, text="TEXT TO BE SEND:", fg="white", bg="black")
    L2.place(x=100, y=300)
    txt = Entry(whatsappautomation, textvariable=text, bg="lightblue", width=30, borderwidth=3)
    txt.place(x=290, y=300)
    L3 = Label(whatsappautomation, text="TIME IN HOURS:", fg="white", bg="black")
    L3.place(x=100, y=350)
    thr = Entry(whatsappautomation, textvariable=hours, bg="lightblue", width=30, borderwidth=3)
    thr.place(x=290, y=350)
    L4 = Label(whatsappautomation, text="TIME IN MINUTE:", fg="white", bg="black")
    L4.place(x=100, y=400)
    tse = Entry(whatsappautomation, textvariable=minutes, bg="lightblue", width=30, borderwidth=3)
    tse.place(x=290, y=400)
    DONE = Button(whatsappautomation, text="DONE", width=5, height=2, fg="white", bg="black", command=groupping)
    DONE.place(x=250, y=450)


#Here By using this buttons iam accessing the perticular function/code.
first = Button(whatsappautomation, text="Private Messsage", width=20, height=2,fg="white",bg="black",command=private)
first.place(x=130, y=100)
second = Button(whatsappautomation, text="Group Message", width=20, height=2,fg="white",bg="black",command=group)
second.place(x=330, y=100)


whatsappautomation.mainloop()
