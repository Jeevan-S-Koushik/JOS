import webbrowser
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk


def check():
    path1 = p1.get()
    path2 = p2.get()
    if (path1 == "jeevan_s_koushik" and path2 == "102030"):
        new_window2()
    else:
        messagebox.showinfo("ERROR", "Please enter correct USERNAME and PASSWORD")


def about_display():
    about = Toplevel(root, bg="#D4E6F1")
    about.geometry('910x300+150+40')
    about.resizable(0, 0)
    about.title("JOS-About")
    lable10 = Label(about, text="JOS-THE VIRTUAL MACHINE", fg="black", bg="#D4E6F1", font=("Courier New", 15))
    lable10.place(x=3, y=5)
    lable11 = Label(about,
                    text="There is no need of buying different operating system computer!  Now a days we can use VIRTUAL NACHINE as a SOFTWARE instead of buying new computer",
                    fg="black", bg="#D4E6F1", font=("Bahnschrift", 10))
    lable11.place(x=5, y=50)
    lable12 = Label(about, text="This is one of the virtual machine that can be used as PERSONAL OS", fg="black",
                    bg="#D4E6F1", font=("Dishonorable Mention (Comic Sans)", 10))
    lable12.place(x=5, y=80)
    lable13 = Label(about, text="Use can use this JOS for the following purpose :", fg="black", bg="#D4E6F1",
                    font=("Bahnschrift", 10))
    lable13.place(x=5, y=110)
    lable13 = Label(about, text="* WHATSAPP AUTOMATION", fg="black", bg="#D4E6F1", font=("Bahnschrift", 10))
    lable13.place(x=5, y=140)
    lable13 = Label(about, text="* INSTAGRAM AUTOMATION", fg="black", bg="#D4E6F1", font=("Bahnschrift", 10))
    lable13.place(x=5, y=170)
    lable14 = Label(about, text="-JSK", fg="black", bg="#D4E6F1", font=("Courier New", 10))
    lable14.place(x=800, y=250)
    lable15 = Label(about, text="* IMAGE VIWER", fg="black", bg="#D4E6F1", font=("Bahnschrift", 10))
    lable15.place(x=5, y=200)
    lable15 = Label(about, text="* JOS-NOTE", fg="black", bg="#D4E6F1", font=("Bahnschrift", 10))
    lable15.place(x=5, y=230)


def Google():
    webbrowser.open("https://www.google.com/")


def new_window1():
    from PIL import ImageTk, Image
    canvas = Canvas(root, width=2000, height=2000)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("C:\\Users\\jeevan s koushik\\PycharmProjects\\JOS\\confirm.jpg"))
    canvas.create_image(0, 0, anchor=NW, image=img)
    p3 = StringVar
    p4 = StringVar
    about_developer =Tk()
    about_developer.geometry('1280x649-1+0')
    about_developer.resizable(0, 0)
    about_developer.title("JOS-DEVELOPER")
    l8 = Label(about_developer, text="DEVELOPED BY  -JSK", bg="#D4E6F1", fg="black", font=("Bahnschrift", 14))
    l8.place(x=100, y=200)


def newpassword(entry=None):
    password = Toplevel(root, bg="#D4E6F1")
    password.geometry('600x580+350+40')
    password.resizable(0, 0)
    password.title("Update Password")

    # def passwordUpdation():
    #   entry = entry1.get()
    #  if(entry=="102030"):
    #     print("this password is correct")

    lable_9 = Label(password, text="enter your password here", fg="black", font=("Bahnschrift", 20))
    lable_9.place(x=100, y=100)
    # b6 = Button(password, text="check", width=10, height=1, fg="blue", bg="black", command=passwordUpdation)
    # b6.place(x=100, y=200)

    entry1 = StringVar()
    entry1 = Entry(password, textvariable=entry1, bg="#7B7D7D", fg="black", width=30, borderwidth=2)


def instagram():
    instagramautomation = Toplevel(root, bg="#D4E6F1")
    instagramautomation.geometry('600x580+350+40')
    instagramautomation.resizable(0, 0)
    instagramautomation.title("Instagram Automation")

    def instamessage():
        from instabot import Bot
        bot = Bot()
        name = un.get()
        passwords = key.get()
        bot.login(username=name, password=passwords)
        bot.send_message("hi brother this is from python automation", [' '])

    def instaupload():
        from instabot import Bot
        bot = Bot()
        name = un.get()
        passwords = key.get()
        bot.login(username=name, password=passwords)
        bot.upload_photo("BG.jpeg", caption="hey this is from python automation")

    def instafollow():
        from instabot import Bot
        bot = Bot()
        name = un.get()
        passwords = key.get()
        bot.login(username=name, password=passwords)
        bot.follow("elonrmusk")

    un = StringVar()
    key = StringVar()
    l10 = Label(instagramautomation, text="Enter your User Name Here:", fg="black", bg="#D4E6F1",
                font=("Bahnschrift", 10))
    l10.place(x=100, y=100)
    un = Entry(instagramautomation, textvariable=un, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
    un.place(x=300, y=100)
    l11 = Label(instagramautomation, text="Enter Your Password Here:", fg="black", bg="#D4E6F1",
                font=("Bahnschrift", 10))
    l11.place(x=100, y=170)
    key = Entry(instagramautomation, textvariable=key, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
    key.place(x=300, y=170)
    instamessages = Button(instagramautomation, text="message", width=10, height=2, fg="white", bg="black",
                           command=instamessage)
    instamessages.place(x=250, y=250)
    instauploads = Button(instagramautomation, text="upload", width=10, height=2, fg="white", bg="black",
                          command=instaupload)
    instauploads.place(x=150, y=250)
    instafollows = Button(instagramautomation, text="follow", width=10, height=2, fg="white", bg="black",
                          command=instafollow)
    instafollows.place(x=350, y=250)


def whatsapp():
    whatsappautomation = Toplevel(root, bg="#D4E6F1")
    whatsappautomation.geometry('600x580+350+40')
    whatsappautomation.resizable(0, 0)
    whatsappautomation.title("whatsapp Automation")

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
        label_1 = Label(whatsappautomation, text=" ENTER THE WHATSAPP NUMBER:", fg="black", bg="#D4E6F1")
        label_1.place(x=100, y=250)
        num = Entry(whatsappautomation, textvariable=num, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
        num.place(x=290, y=250)
        L2 = Label(whatsappautomation, text="TEXT TO BE SEND:", fg="black", bg="#D4E6F1")
        L2.place(x=100, y=300)
        txt = Entry(whatsappautomation, textvariable=txt, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
        txt.place(x=290, y=300)
        L3 = Label(whatsappautomation, text="TIME IN HOURS:", fg="black", bg="#D4E6F1")
        L3.place(x=100, y=350)
        thr = Entry(whatsappautomation, textvariable=thr, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
        thr.place(x=290, y=350)
        L4 = Label(whatsappautomation, text="TIME IN MINUTE:", fg="black", bg="#D4E6F1")
        L4.place(x=100, y=400)
        tse = Entry(whatsappautomation, textvariable=tse, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
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
        label_1 = Label(whatsappautomation, text="ENTER THE WHATSAPP GROUP ID:", fg="black", bg="#D4E6F1")
        label_1.place(x=95, y=250)
        num = Entry(whatsappautomation, textvariable=ab, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
        num.place(x=290, y=250)
        L2 = Label(whatsappautomation, text="TEXT TO BE SEND:", fg="black", bg="#D4E6F1")
        L2.place(x=100, y=300)
        txt = Entry(whatsappautomation, textvariable=text, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
        txt.place(x=290, y=300)
        L3 = Label(whatsappautomation, text="TIME IN HOURS:", fg="black", bg="#D4E6F1")
        L3.place(x=100, y=350)
        thr = Entry(whatsappautomation, textvariable=hours, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
        thr.place(x=290, y=350)
        L4 = Label(whatsappautomation, text="TIME IN MINUTE:", fg="black", bg="#D4E6F1")
        L4.place(x=100, y=400)
        tse = Entry(whatsappautomation, textvariable=minutes, bg="#7B7D7D", fg="black", width=30, borderwidth=2)
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
    home = Toplevel(root, bg="#D4E6F1")
    home.geometry('1280x649-1+0')
    home.resizable(0, 0)
    home.title("JOS-HOME")
    # BUTTONS
    b3 = Button(home, text="WHATSAPP", width=10, height=2, fg="#B3B6B7", bg="black", command=whatsapp)
    b3.place(x=50, y=50)
    b4 = Button(home, text="INSTAGRAM", width=10, height=2, fg="#B3B6B7", bg="black", command=instagram)
    b4.place(x=150, y=50)
    b5 = Button(home, text="UPDATE-PASSWORD", width=18, height=2, fg="#B3B6B7", bg="black", command=newpassword)
    b5.place(x=250, y=50)
    b6 = Button(home, text="GOOGLE", width=10, height=2, fg="#B3B6B7", bg="black", command=Google)
    b6.place(x=400, y=50)


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
image = ImageTk.PhotoImage(Image.open("C:\\Users\\jeevan s koushik\\PycharmProjects\\JOS\\confirm.jpg"))
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()
# l1 = Label(root, text=" HI SIR! GOOD TO SEE YOU ", fg="lightblue", bg="black", font=("Times", 30))
# l1.place(x=430, y=70)


l2 = Label(root, text="PLEASE LOGIN SIR", fg="black", bg="#7B7D7D", font=("Times New Roman", 25))
l2.place(x=180, y=200)
l3 = Label(root, text="Enter your User Name", fg="black", bg="#7B7D7D", font=("Times New Roman", 12))
l3.place(x=255, y=300)
p1 = Entry(root, textvariable=p1, bg="#7B7D7D", fg="black", width=30, borderwidth=5)
p1.place(x=230, y=340)

l4 = Label(root, text="Enter your Password", fg="black", bg="#7B7D7D", font=("Times New Roman", 12))
l4.place(x=255, y=400)
p2 = Entry(root, textvariable=p2, bg="#7B7D7D", fg="black", width=30, borderwidth=5)
p2.place(x=230, y=440)
b2 = Button(root, text="LOGIN", width=7, height=2, fg="white", bg="black", command=check)
b2.place(x=285, y=480)

b1 = Button(root, text="ABOUT-DEVELOPER", width=18, height=1, fg="white", bg="black", command=new_window1)
b1.place(x=970, y=540)
b6 = Button(root, text="ABOUT", fg="white", bg="black", command=about_display)
b6.place(x=1000, y=50)

# -----------------------------------------------------------------------


root.mainloop()
