from tkinter import *
from PIL import Image,ImageTk

def check():
    path1 = p1.get()
    path2 = p2.get()
    if(path1=="jeevan_s_koushik" and path2=="102030"):
        new_window2()
    else:
        l9=Label(root,text="Please enter correct USERNAME and PASSWORD",bg="black",fg="red",font=("Times", 8))
        l9.place(x=200, y=475)


def new_window1():
    p3=StringVar
    p4=StringVar
    register=Toplevel(root,bg="black")
    register.geometry('1280x649-1+0')
    register.resizable(0,0)
    register.title("JOS-REGISTER")
    l6= Label(register, text="REGISTER HERE", fg="white", bg="black", font=("Bahnschrift", 20))
    l6.place(x=550, y=50)
    l8=Label(register,text="Enter your Name :",bg="black",fg="white",font=("Bahnschrift",14))
    l8.place(x=100,y=200)
    p3=Entry(register,textvariable=p3, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
    p3.place(x=280,y=205)

def instagram():
    instagramautomation = Tk()
    instagramautomation.geometry('600x580+350+40')
    instagramautomation.resizable(0, 0)
    instagramautomation.title("Instagram Automation")
    label_8 = Label(instagramautomation, text="-JSK.", fg="white")
    label_8.place(x=500, y=500)
    def instamessage():
        from instabot import Bot
        bot=Bot()
        name=un.get()
        passwords=key.get()
        bot.login(username=name,password=passwords)
        bot.send_message("hi brother this is from python automation",[' '])

    def instaupload():
        from instabot import Bot
        bot = Bot()
        name = un.get()
        passwords = key.get()
        bot.login(username=name, password=passwords)
        bot.upload_photo("BG.jpeg",caption="hey this is from python automation")

    def instafollow():
        from instabot import Bot
        bot = Bot()
        name = un.get()
        passwords = key.get()
        bot.login(username=name, password=passwords)
        bot.follow("elonrmusk")
    un=StringVar()
    key=StringVar()
    l10=Label(instagramautomation,text="Enter your User Name Here:",fg="black",font=("Bahnschrift",10))
    l10.place(x=100,y=100)
    un = Entry(instagramautomation, textvariable=un, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
    un.place(x=300, y=100)
    l11=Label(instagramautomation,text="Enter Your Password Here:",fg="black",font=("Bahnschrift",10))
    l11.place(x=100,y=170)
    key=Entry(instagramautomation,textvariable=key,bg="#7B7D7D",fg="black",width=30,borderwidth=2)
    key.place(x=300,y=170)
    instamessages=Button(instagramautomation, text="message", width=10, height=2, fg="white", bg="black", command=instamessage)
    instamessages.place(x=250,y=250)
    instauploads=Button(instagramautomation, text="upload", width=10, height=2, fg="white", bg="black", command=instaupload)
    instauploads.place(x=150,y=250)
    instafollows=Button(instagramautomation, text="follow", width=10, height=2, fg="white", bg="black", command=instafollow)
    instafollows.place(x=350,y=250)


def whatsapp():
    whatsappautomation = Tk()
    whatsappautomation.geometry('600x580+350+40')
    whatsappautomation.resizable(0, 0)
    whatsappautomation.title("whatsapp Automation")
    label_7 = Label(whatsappautomation, text="-JSK.", fg="white")
    label_7.place(x=500, y=500)

    # The below code is for sending private message.
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
        label_1 = Label(whatsappautomation, text=" ENTER THE WHATSAPP NUMBER:", fg="black")
        label_1.place(x=100, y=250)
        num = Entry(whatsappautomation, textvariable=num, bg="#7B7D7D",fg="black", width=30, borderwidth=2)
        num.place(x=290, y=250)
        L2 = Label(whatsappautomation, text="TEXT TO BE SEND:", fg="black")
        L2.place(x=100, y=300)
        txt = Entry(whatsappautomation, textvariable=txt, bg="#7B7D7D",fg="black", width=30, borderwidth=2)
        txt.place(x=290, y=300)
        L3 = Label(whatsappautomation, text="TIME IN HOURS:", fg="black")
        L3.place(x=100, y=350)
        thr = Entry(whatsappautomation, textvariable=thr, bg="#7B7D7D",fg="black", width=30, borderwidth=2)
        thr.place(x=290, y=350)
        L4 = Label(whatsappautomation, text="TIME IN MINUTE:", fg="black")
        L4.place(x=100, y=400)
        tse = Entry(whatsappautomation, textvariable=tse, bg="#7B7D7D",fg="black", width=30, borderwidth=2)
        tse.place(x=290, y=400)
        DONE = Button(whatsappautomation, text="DONE", width=5, height=2, fg="white", bg="black", command=what)
        DONE.place(x=250, y=450)

    # The below code is to sending the group message.
    def group():
        def groupping():
            import pywhatkit
            Id = ab.get()
            T = text.get()
            hour = hours.get()
            hour = int(hour)
            minute = minutes.get()
            minute = int(minute)
            pywhatkit.sendwhatmsg_to_group(Id, T, hour, minute)

        ab = StringVar()
        text = StringVar()
        hours = StringVar()
        minutes = StringVar()
        label_1 = Label(whatsappautomation, text="ENTER THE WHATSAPP GROUP ID:", fg="black")
        label_1.place(x=95, y=250)
        num = Entry(whatsappautomation, textvariable=ab, bg="#7B7D7D",fg="black", width=30, borderwidth=2)
        num.place(x=290, y=250)
        L2 = Label(whatsappautomation, text="TEXT TO BE SEND:", fg="black")
        L2.place(x=100, y=300)
        txt = Entry(whatsappautomation, textvariable=text, bg="#7B7D7D",fg="black", width=30, borderwidth=2)
        txt.place(x=290, y=300)
        L3 = Label(whatsappautomation, text="TIME IN HOURS:", fg="black")
        L3.place(x=100, y=350)
        thr = Entry(whatsappautomation, textvariable=hours, bg="#7B7D7D",fg="black", width=30, borderwidth=2)
        thr.place(x=290, y=350)
        L4 = Label(whatsappautomation, text="TIME IN MINUTE:", fg="black")
        L4.place(x=100, y=400)
        tse = Entry(whatsappautomation, textvariable=minutes, bg="#7B7D7D",fg="black", width=30, borderwidth=2)
        tse.place(x=290, y=400)
        DONE = Button(whatsappautomation, text="DONE", width=5, height=2, fg="white", bg="black", command=groupping)
        DONE.place(x=250, y=450)

    # Here By using this buttons iam accessing the perticular function/code.
    first = Button(whatsappautomation, text="Private Messsage", width=20, height=2, fg="white", bg="black",
                   command=private)
    first.place(x=130, y=100)
    second = Button(whatsappautomation, text="Group Message", width=20, height=2, fg="white", bg="black", command=group)
    second.place(x=330, y=100)


def new_window2():
        home=Toplevel(root,bg="#7B7D7D")
        home.geometry('1280x649-1+0')
        home.resizable(0,0)
        home.title("JOS-HOME")
        b3 = Button(home, text="WHATSAPP", width=10, height=2, fg="#B3B6B7", bg="black", command=whatsapp)
        b3.place(x=50, y=50)
        b4=Button(home,text="INSTAGRAM",width=10,height=2,fg="#B3B6B7",bg="black",command=instagram)
        b4.place(x=150,y=50)



root = Tk()
root.geometry('1280x649-1+0')
root.resizable(0, 0)
root.title("JOS")


# ---------------------------------------
# login Page code
# enter the path variable

p1 = StringVar()
p2 = StringVar()
canvas = Canvas(root, width=2000, height=2000)
image = ImageTk.PhotoImage(Image.open("C:\\Users\\jeevan s koushik\\Downloads\\JOS_image.jpeg"))
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()
l1 = Label(root, text=" HI SIR! GOOD TO SEE YOU ", fg="grey", bg="black", font=("Times", 30))
l1.place(x=430, y=70)
l2 = Label(root, text="[PLEASE LOGIN SIR]", fg="grey", bg="black", font=("Times", 18))
l2.place(x=220, y=230)
l3 = Label(root, text="[Enter your User Name]", fg="blue", bg="black", font=("Bahnschrift", 10))
l3.place(x=240, y=300)
p1 = Entry(root, textvariable=p1, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
p1.place(x=240, y=330)

l4 = Label(root, text="[Enter your Password]", fg="blue", bg="black", font=("Bahnschrift", 10))
l4.place(x=240, y=400)
p2 = Entry(root, textvariable=p2, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
p2.place(x=240, y=430)
b2 = Button(root, text="LOGIN", width=7, height=2, fg="blue", bg="black", command=check)
b2.place(x=300, y=520)


l5 = Label(root, text="[Register If You Dont Have An Account]", fg="silver", bg="black", font=("Bahnschrift", 10))
l5.place(x=900, y=500)
b1 = Button(root, text="REGISTER", width=10, height=1, fg="blue", bg="black",command=new_window1)
b1.place(x=970, y=540)

# -----------------------------------------------------------------------



root.mainloop()
