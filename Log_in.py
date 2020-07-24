from tkinter import*
import tkinter.messagebox
from PIL import Image,ImageTk
import os                                               # for stringvariable 
from tkinter import ttk                                 # for combobox
import random                                           # for reference
import time
import datetime

def main():
    root = Tk()
    app = Window_1(root)


class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('1350x750')
        self.master.config(bg = 'lightblue')


        ##################################################################3
        img=ImageTk.PhotoImage(Image.open("bg.jpg"))
        self.background_image=Label(self.master,image=img,height=150,width=150)
        self.background_image.image=img
        self.background_image.place(x=0,y=0,relwidth=1,relheight=1)

        self.Frame1=Frame(self.master,height=20)
        self.Frame1.pack()

        self.Frame2=Frame(self.master)
        self.Frame2.pack()

        self.Frame3=Frame(self.master)
        self.Frame3.pack()
        
        img=ImageTk.PhotoImage(Image.open("logo.png"))
        self.panel=Label(self.Frame2,image=img,height=150,width=150)
        self.panel.image=img
        self.panel.pack(side="top")


        self.panel1=Label(self.Frame3,text="ManageGO",bg='lightblue',fg='white',font=('Verdana',30,'bold'))
        self.panel1.pack(side="top")
        #######################################################################33
        
        self.Frame = Frame(self.master, bg = 'lightblue')
        self.Frame.pack(side='top')



        


        self.Username = StringVar()                             # x = StringVar()  Holds a string; default value is " "
        self.Password = StringVar()

        self.Lbl_Title = Label(self.Frame, text = '', font = ('arial',35,'bold'), bg = 'lightblue', fg = 'Black')
        self.Lbl_Title.grid(row = 0, column = 0, columnspan =3, pady = 40)
        
        self.Login_Frame_1 = LabelFrame(self.Frame, width = 1350, height = 600, relief = 'ridge', bg = 'lightblue', bd = 5,
                                        font = ('arial',20,'bold'))
        self.Login_Frame_1.grid(row = 1, column =0)
        self.Login_Frame_2 = LabelFrame(self.Frame, width = 1000, height = 600, relief = 'ridge',bg = 'lightblue', bd = 5,
                                        font = ('arial',20,'bold'))
        self.Login_Frame_2.grid(row = 2, column = 0)


        #===================================================LABEL and ENTRIES=======================================================================
        self.Label_Username = Label(self.Login_Frame_1, text = 'Username', font = ('arial',20,'normal'), bg = 'lightblue', bd = 20)
        self.Label_Username.grid(row = 0, column = 0)
        self.text_Username = Entry(self.Login_Frame_1, font = ('arial',20,'normal'), textvariable = self.Username,borderwidth=10,relief=FLAT)
        self.text_Username.grid(row = 0, column = 1, padx = 50)                       
        
        self.Label_Password = Label(self.Login_Frame_1, text = 'Password', font = ('arial',20,'normal'), bg = 'lightblue', bd = 20)
        self.Label_Password.grid(row = 1, column = 0)
        self.text_Password = Entry(self.Login_Frame_1, font = ('arial',20,'normal'), show = '*', textvariable = self.Password,borderwidth=10,relief=FLAT)
        self.text_Password.grid(row = 1, column = 1) 
        
        
        #=============================================================BUTTONS=======================================================================
        self.btnLogin = Button(self.Login_Frame_2,fg='white',bg='green', text = 'Login', width = 10, font = ('airia',15,'bold'), command = self.Login)
        self.btnLogin.grid(row = 3, column = 0, padx = 8, pady = 20)

        self.btnReset = Button(self.Login_Frame_2,fg='white',bg='orange', text = 'Reset', width = 10, font = ('airia',15,'bold'), command = self.Reset)
        self.btnReset.grid(row = 3, column = 1, padx = 8, pady = 20)

        self.btnExit = Button(self.Login_Frame_2,fg='white',bg='red', text = 'Exit', width = 10, font = ('airia',15,'bold'), command = self.Exit)
        self.btnExit.grid(row = 3, column = 2, padx = 8, pady = 20)


        #======================================================Code for Login Button==================================================================
    def Login(self):
        u = (self.Username.get())
        p = (self.Password.get())

        if (u == str('fazil') and p == str(123)):
            self.__menu__()
        else:
            tkinter.messagebox.askyesno("Login","Error : Wrong Password")
            self.Username.set("")
            self.Password.set("")
            #self.text_Username.focus()

        
        #======================================================Code for Reset Button==================================================================
    def Reset(self):
         self.Username.set("")
         self.Password.set("")
         self.text_Username.focus()


        #======================================================Code for Exit Button==================================================================

    def Exit(self):
        self.Exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.Exit > 0:
            self.master.destroy()
            return

    def __menu__(self):
        filename = 'Menu.py'
        os.system(filename)
        os.system('notepad'+filename)

    '''def new_window(self):
        self.new_Window = Toplevel(self.master)
        self.app = Window_2(self.new_Window)'''

class Window_2:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Main Menu")
        self.master.geometry('1350x750')
        self.master.config(bg = 'sky blue')
        self.Frame = Frame(self.master, bg = 'lightblue')
        self.Frame.pack()

    

if __name__ == '__main__':                                    # https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
    main()                                              


