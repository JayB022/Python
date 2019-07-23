from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
import smtplib, re
from tkinter import messagebox


class Contact:
    def __init__(self, master):
        self.master = master

        self.title_l = Label(master, text='Contact Form', font='arial 20 bold')
        self.title_l.place(x=10, y=0)

        self.name_l = Label(master, text='Name:', font='arial 15 bold')
        self.name_l.place(x=30, y=70)

        # entry for label name.....
        self.name_e = Entry(master, font='arial 15 bold', width=25)
        self.name_e.place(x=100, y=70)

        self.email_l = Label(master, text='Email:', font='arial 15 bold')
        self.email_l.place(x=30, y=130)

        # entry for label email.....
        self.email_e = Entry(master, font='arial 15 bold', width=25)
        self.email_e.place(x=100, y=130)

        self.subj1 = Label(master, text='Subject', font='arial  15 bold')
        self.subj1.place(x=30, y=170)
        self.sbj = tk.scrolledtext.ScrolledText(master, font='arial 15 bold', width=40, height=2)
        self.sbj.place(x=70, y=200)

        self.msg1 = Label(master, text='Message', font='arial 15 bold')
        self.msg1.place(x=30, y=270)
        self.msg = tk.scrolledtext.ScrolledText(master, font='sanserif 12 bold', height=5, width=40)
        self.msg.place(x=70, y=300)

        # Button to send the mail.....
        self.send_btn = Button(master, text='Send Mail', font='arial 15 bold', cursor='hand2', relief=FLAT, command=self.send_mail)
        self.send_btn.place(x=230, y=420)

    def clear(self):
        self.email_e.delete(0, END)
        self.name_e.delete(0, END)
        self.sbj.delete('1.0', END)
        self.msg.delete('1.0', END)

    def send_mail(self):
        name = self.name_e.get()
        email = self.email_e.get()
        subject = self.sbj.get('1.0', END)
        message = 'Hi\t' + name + '\n\n' + self.msg.get('1.0', END)

        if email == '':
            messagebox.showerror('Empty Filed', 'Email required')
        elif  re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) == None:
            messagebox.showerror('Invalid email', 'Use a valid email')

        else:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('teslajay10@gmail.com', 'jaymore8160')
            feedback= 'Subject:{}\n\n{}'.format(subject, message)
            server.sendmail('teslajay10@gmail.com', email, feedback)
            server.quit()
            messagebox.showinfo('Success', 'Message Sent')
            self.clear()


root = Tk()
Contact(root)
root.geometry('570x500')
root.title('Contact Us')
root.resizable(False, False)
root.mainloop()
