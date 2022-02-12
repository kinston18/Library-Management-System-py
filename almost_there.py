
from tkinter import*
from tkinter import ttk
import random
import time
import tkinter.messagebox

class Library:

    def __init__(self,root):
        self.root = root
        self.root.title("Welcome to the Library")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='cadetblue')

         
        Mtype=StringVar()
        Author=StringVar()
        Ref =StringVar()
        BookType=StringVar()
        Name=StringVar()
        IssueDate=StringVar()
        Mobile=StringVar()
        Duedate=StringVar()
        
        def iReset():
            Mtype.set("")
            Author.set("")
            Ref.set("")
            BookType.set("")
            Name.set("")
            IssueDate.set("")
            Mobile.set("")
            Duedate.set("")
            self.txtDisplayR.delete("1.0", END)

        def iDelete():
            self.txtDisplayR.delete("1.0", END)      

        def iExit():
        	Exit=tkinter.messagebox.askyesno("Library Management System","Confirm do you want to exit")
        	if Exit>0:
        		root.destroy()
        		return

        def iDisplayData():
           self.txtFrameDetail.insert(END,"\t"+ Mtype.get()+"\t\t"+ Author.get()+"\t" + Ref.get() + "\t" + BookType.get() + "\t" +  Name.get()+ "\t\t" + IssueDate.get()+ "\t"+ Mobile.get()+ "\t"+ Duedate.get()+"\n")
           
        def iReceipt():
           self.txtDisplayR.insert(END,'MemberType: \t\t'+Mtype.get() + "\n")
           self.txtDisplayR.insert(END,'Author: \t\t'+ Author.get()+ "\n")
           self.txtDisplayR.insert(END,'Reference ID: \t\t'+ Ref.get()+ "\n")
           self.txtDisplayR.insert(END,'Book Type: \t\t'+ BookType.get()+ "\n")
           self.txtDisplayR.insert(END,'Name: \t\t'+ Name.get()+ "\n")
           self.txtDisplayR.insert(END,'Issue Date: \t\t'+ IssueDate.get()+ "\n")
           self.txtDisplayR.insert(END,'Mobile: \t\t'+ Mobile.get()+ "\n")
           self.txtDisplayR.insert(END,'Due Date: \t\t'+ Duedate.get()+ "\n")        

        #------------------------------------------------Frames--------------------------------------------------------#
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame =Frame(MainFrame,width=1350,padx=20,bd=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.lblTitle =Label(TitleFrame,width=39,font=('arial',40,'bold'),text="\tLibrary Management System\t",bg="cadetblue",fg='Crimson',padx=12)
        self.lblTitle.grid()
        
        ButtonFrame =Frame(MainFrame,bd=20,width=1350,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail =Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame,bd=20,width=1300,height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame,bd=10,width=800,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text="Library Membership Info:",fg="cadetblue")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame,bd=10,width=450,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text="BookDetails",fg="Crimson")
        DataFrameRIGHT.pack(side=RIGHT)


        #======================================widget===========================================================================================
        
        self.lblMemberType = Label(DataFrameLEFT, font=('arial',12,'bold'),text="MemberType:",padx=2,pady=2)
        self.lblMemberType.grid(row=0,column=0,sticky=W)
        
        self.cboMemberType = ttk.Combobox(DataFrameLEFT, state='readonly',textvariable = Mtype,
        font=('arial',12,'bold'), width=23)
        self.cboMemberType['value']=('','Student','Lecturer','AdminStaff')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0,column=1)

        self.lblAuthor =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Author:",padx=2,pady=2)
        self.lblAuthor.grid(row=0,column=2,sticky=W)
        self.lblAuthor=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Author,width=25)
        self.lblAuthor.grid(row=0,column=3)

        self.lblRef =Label(DataFrameLEFT, font=('arial',12,'bold'),text="Reference ID no. :",padx=2,pady=2)
        self.lblRef.grid(row=1,column=0,sticky=W)
        self.lblRef=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Ref,width=25)
        self.lblRef.grid(row=1,column=1)

        self.lblBookType =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Book Type:",padx=2,pady=2)
        self.lblBookType.grid(row=1,column=2,sticky=W)
        self.lblBookType=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=BookType,width=25)
        self.lblBookType.grid(row=1,column=3)

        self.lblName = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Name:", padx=2,pady=2)
        self.lblName. grid(row=2, column=0, sticky=W)
        self.lblName = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable= Name, width=25)
        self.lblName. grid(row=2, column=1)

        self.lblIssuedate = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Issue date:", padx=2,pady=2)
        self.lblIssuedate. grid(row=2, column=2, sticky=W)
        self.lblIssuedate = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable=IssueDate, width=25)
        self.lblIssuedate. grid(row=2, column=3)

        self.lblMobile =Label(DataFrameLEFT, font=('arial',12,'bold'),text="Mobile no. :",padx=2,pady=2)
        self.lblMobile.grid(row=3,column=0,sticky=W)
        self.lblMobile=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Mobile,width=25)
        self.lblMobile.grid(row=3,column=1)
        
        self.lblDuedate =Label(DataFrameLEFT, font=('arial',12,'bold'),text="Due date:",padx=2,pady=2)
        self.lblDuedate.grid(row=3,column=2,sticky=W)
        self.lblDuedate=Entry(DataFrameLEFT, font=('arial',12,'bold'),textvariable=Duedate,width=25)
        self.lblDuedate.grid(row=3,column=3)

       
        #=======================================Widget=================================================================
        self.txtDisplayR=Text(DataFrameRIGHT,font=('arial',12,'bold'),width=32,height=13,padx=8,pady=20)
        self.txtDisplayR.grid(row=0,column=2)
        #======================================ListBox==================================================================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        ListOfBooks = ['Atomic Habits','The Intelligent Investor','Do Epic Shit','Rich Dad Poor Dad', 'Think & Grow Rich', 'The Alchemist', 'Train to Pakistan', 'Ikigai','The Spy', 'Namesake', 'The White Tiger', 'A Tale of Two Cities', '1984', 'The Girl on the Train','The Rudest Book Ever', 'Leaders Eat Last', 'Time Machine', 'As a man thinketh', 'Harappa', 'Kashi', 'Pralay','The Richest Man in Babylon', 'Siddhartha', 'Ransom', 'The Naked Face','Catch 22', 'Two Fates']
        
        def SelectedBook(evt):
            value =str(booklist.get(booklist.curselection()))
            print(value)
            w=value
            
            if (w=="Atomic Habits"):
                 Author.set("James Clear")
                 BookType.set("Self Growth")
                 Ref.set("ISBN 3467478")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=14)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)

            elif (w=="The Intelligent Investor"):
                 Author.set("Benjamin Graham")
                 BookType.set("Business")
                 Ref.set("ISBN 3466755")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=12)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)

            elif (w=="Do Epic Shit"):
                 Author.set("Ankur Warikoo")
                 BookType.set("Self Growth")
                 Ref.set("ISBN 3757495")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)


            elif (w=="Rich Dad Poor Dad"):
                 Author.set("Robert Kiosaki")
                 BookType.set("Money Management")
                 Ref.set("ISBN 4540755")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=14)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)
          
            elif (w=="Think & Grow Rich"):
                 Author.set("Napolean Hill")
                 BookType.set("Money Management")
                 Ref.set("ISBN 6848885")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=13)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)



            elif (w=="The Alchemist"):
                 Author.set("Paulo Coelho")
                 BookType.set("Psychology/Fiction")
                 Ref.set("ISBN 7623495")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)

            elif (w=="Train to Pakistan"):
                 Author.set("Khushwant Singh")
                 BookType.set("Historical Fiction")
                 Ref.set("ISBN 87009885")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)

            elif (w=="Ikigai"):
                 Author.set("Hector Garcia")
                 BookType.set("Living")
                 Ref.set("ISBN 6757685")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=13)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)


            elif (w=="The Spy"):
                 Author.set("Paulo Coelho")
                 BookType.set("Historical Fiction")
                 Ref.set("ISBN 8775754")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)
        
            elif (w=="Namesake"):
                 Author.set("Jumpa Lahiri")
                 BookType.set("Historical Fiction")
                 Ref.set("ISBN 87007858")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)

            elif (w=="The White Tiger"):
                 Author.set("Aravind Adiga")
                 BookType.set("Epistolary Novel")
                 Ref.set("ISBN 5675985")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)


            elif (w=="A Tale of Two Cities"):
                 Author.set("Charles Dickens")
                 BookType.set("Historical")
                 Ref.set("ISBN 8757885")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)
    

            elif (w=="1984"):
                 Author.set("George Orwell")
                 BookType.set("Socio-political Fiction")
                 Ref.set("ISBN 805905385")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=13)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)


            elif (w=="The Girl on the Train"):
                 Author.set("Paula Hawkins")
                 BookType.set("Thriller Mystery")
                 Ref.set("ISBN 87009885")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=20)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)


            elif (w=="The Rudest Book Ever"):
                 Author.set("Shwetabh Gangwar")
                 BookType.set("Psychology")
                 Ref.set("ISBN 56567475")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)


            elif (w=="Leaders Eat Last"):
                 Author.set("Simon Sinek")
                 BookType.set("Leadership")
                 Ref.set("ISBN 86540885")
                 iReceipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=(d1+d2)
                 IssueDate.set(d1)
                 Duedate.set(d3)
       	 
           
        booklist = Listbox(DataFrameRIGHT,width=20,height=12,font=('arial',12,'bold'))
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=0,column=0,padx=8)

        for items in ListOfBooks:
        	booklist.insert(END,items)

        #======================================================================================================================	



        #=======================================Button=========================================================================


        self.btnDisplayData=Button(ButtonFrame,text="DISPLAY DATA",fg="Crimson",bg="cadetblue",font=('arial',12,'bold'),width=30,bd=4,command=iReceipt)
        self.btnDisplayData.grid(row=0,column=0)

        self.btnDelete=Button(ButtonFrame,text="DELETE",fg="Crimson",bg="cadetblue",font=('arial',12,'bold'),width=30,bd=4,command=iDelete)
        self.btnDelete.grid(row=0,column=1)

        self.btnReset=Button(ButtonFrame,text="RESET",fg="Crimson",bg="cadetblue",font=('arial',12,'bold'),width=30,bd=4,command=iReset)
        self.btnReset.grid(row=0,column=2)

        self.btnExit=Button(ButtonFrame,text="EXIT",fg="Crimson",bg="cadetblue",font=('arial',12,'bold'),width=30,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=3)



if __name__=='__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()
