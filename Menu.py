from tkinter import*
import random
import os

def __marksheet__():
       filename = 'Search_Page.py'
       os.system(filename)
       os.system('notepad'+filename)

def __Library__():
       filename = 'Library_Frontend.py'
       os.system(filename)
       os.system('notepad'+filename)

def __information__():
       filename = 'Std_info_FrontEnd.py'
       os.system(filename)
       os.system('notepad'+filename)

def __FeeReport__():
       filename = 'Fee_Frontend.py'
       os.system(filename)
       os.system('notepad'+filename)
       
       
def menu():
       root = Tk()
       root.title('Menu')
       root.geometry('1350x750')
       root.config(bg = 'dodgerblue')


       
       ##################################################################3
       from PIL import Image,ImageTk
       img=ImageTk.PhotoImage(Image.open("bg.jpg"))
       background_image=Label(root,image=img,height=150,width=150)
       background_image.image=img
       background_image.place(x=0,y=0,relwidth=1,relheight=1)
       
       Frame1=Frame(root,height=20)
       Frame1.pack()

       Frame2=Frame(root)
       Frame2.pack()

       Frame3=Frame(root)
       Frame3.pack()
        
       img=ImageTk.PhotoImage(Image.open("logo.png"))
       panel=Label(Frame2,image=img,height=150,width=150)
       panel.image=img
       panel.pack(side="top")


       panel1=Label(Frame3,text="ManageGO",bg='lightblue',fg='white',font=('Verdana',30,'bold'))
       panel1.pack(side="top")

       Frames=Frame(root,bg='lightblue')
       Frames.pack()
       #######################################################################33
        
       
       title_Frame = LabelFrame(Frames, font = ('arial',30,'bold'), width = 1000, height = 100, bg = 'lightblue', relief = 'raise', bd = 5)
       title_Frame.grid(row = 0, column = 0, pady = 50)
       
       title_Label = Label(title_Frame, text = 'MENU', font = ('arial',30,'bold'), bg = 'lightblue')
       title_Label.grid(row = 0, column = 0, padx = 150)


       #========================================================FRAMES===================================================================
       Frame_1 = LabelFrame(Frames, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'lightblue', relief = 'ridge', bd = 2)
       Frame_1.grid(row = 1, column = 0, padx = 280)
       Frame_2 = LabelFrame(Frames, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'lightblue', relief = 'ridge', bd = 2)
       Frame_2.grid(row = 2, column = 0, padx = 130, pady = 7)
       Frame_3 = LabelFrame(Frames, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'lightblue', relief = 'ridge', bd = 2)
       Frame_3.grid(row = 3, column = 0, pady = 7)
       Frame_4 = LabelFrame(Frames, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'lightblue', relief = 'ridge', bd = 2)
       Frame_4.grid(row = 4, column = 0, pady = 7)
       


       #========================================================LABELS===================================================================
       Label_1 = Label(Frame_1, text = 'STUDENT PROFILE', font = ('arial',25,'bold'), bg = 'lightblue')
       Label_1.grid(row = 0, column = 0, padx = 50, pady = 5)
       Label_2 = Label(Frame_2, text = 'FEE REPORT', font = ('arial',25,'bold'), bg = 'lightblue')
       Label_2.grid(row = 0, column = 0, padx = 100, pady = 5)
       Label_3 = Label(Frame_3, text = 'LIBRARY SYSTEM', font = ('arial',25,'bold'), bg = 'lightblue')
       Label_3.grid(row = 0, column = 0, padx = 60, pady = 5)
       Label_4 = Label(Frame_4, text = 'MARKSHEET', font = ('arial',25,'bold'), bg = 'lightblue')
       Label_4.grid(row = 0, column = 0, padx = 101, pady = 5)
       


       #========================================================BUTTONS===================================================================
       Button_1 = Button(Frame_1, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __information__)
       Button_1.grid(row = 0, column = 3, padx = 50)
       Button_2 = Button(Frame_2, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __FeeReport__)
       Button_2.grid(row = 0, column = 3, padx = 50)
       Button_3 = Button(Frame_3, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __Library__)
       Button_3.grid(row = 0, column = 3, padx = 50)
       Button_4 = Button(Frame_4, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __marksheet__)
       Button_4.grid(row = 0, column = 3, padx = 50)
       
       

       root.mainloop()


       
       
if __name__ == '__main__':
       menu()
