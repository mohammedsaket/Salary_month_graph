from tkinter import *
import matplotlib.pyplot as plt
root = Tk()
root.geometry("700x600")
root.title("Month Salary Graph")
mystring0=IntVar()
mystring1=IntVar()
mystring2=IntVar()
mystring3=IntVar()
mystring4=IntVar()
mystring5=IntVar()
mystring6=IntVar()
mystring7=IntVar()
mystring8=IntVar()
mystring9=IntVar()
mystring10=IntVar()
mystring11=IntVar()
tops=Frame(root,width=600,height=100,bg='blue',relief=SUNKEN)
tops.pack(side=TOP)
f1=Frame(root,width=300,height=500,relief=SUNKEN)
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=500,relief=SUNKEN)
f2.pack(side=RIGHT)
f3=Frame(root,width=600,height=50,relief=SUNKEN)
f3.pack(side=BOTTOM)
l1=Label(tops,font=('arial',20,'bold'),text='Salary Month Graph',fg='Steel Blue',bd=25,anchor='w')
l1.grid(row=0,column=0)
"""********************************************************Frame 1**********************************************"""
Label(f1,font=('arial',12,'bold'),text='Month',fg='Steel Blue',anchor='w',bd=20).grid(row=0,column=0)
Label(f1,font=('arial',12,'bold'),text='Salary',fg='Steel Blue',anchor='w',bd=20).grid(row=0,column=1)
Label(f1,font=('arial',10,'bold'),text='Jan=',fg='Steel Blue',anchor='w',bd=20).grid(row=1,column=0)
Entry(f1,textvariable = mystring0,font=('arial',10,'bold'),bd=10,insertwidth=2,justify='right').grid(row=1,column=1)
Label(f1,font=('arial',10,'bold'),text='Feb=',fg='Steel Blue',anchor='w',bd=20).grid(row=2,column=0)
Entry(f1,textvariable = mystring1,font=('arial',10,'bold'),bd=10,insertwidth=2,justify='right').grid(row=2,column=1)
Label(f1,font=('arial',10,'bold'),text='March=',fg='Steel Blue',anchor='w',bd=20).grid(row=3,column=0)
Entry(f1,textvariable = mystring2,font=('arial',10,'bold'),bd=10,insertwidth=2,justify='right').grid(row=3,column=1)
Label(f1,font=('arial',10,'bold'),text='April=',fg='Steel Blue',anchor='w',bd=20).grid(row=4,column=0)
Entry(f1,textvariable = mystring3,font=('arial',10,'bold'),bd=10,insertwidth=2,justify='right').grid(row=4,column=1)
Label(f1,font=('arial',10,'bold'),text='May=',fg='Steel Blue',anchor='w',bd=20).grid(row=5,column=0)
Entry(f1,textvariable = mystring4,font=('arial',10,'bold'),bd=10,insertwidth=2,justify='right').grid(row=5,column=1)
Label(f1,font=('arial',10,'bold'),text='June=',fg='Steel Blue',anchor='w',bd=20).grid(row=6,column=0)
Entry(f1,textvariable = mystring5,font=('arial',10,'bold'),bd=10,insertwidth=2,justify='right').grid(row=6,column=1)
"""********************************************************Frame 2**********************************************"""
Label(f2,font=('arial',12,'bold'),text='Month',fg='Steel Blue',anchor='w',bd=20).grid(row=0,column=0)
Label(f2,font=('arial',12,'bold'),text='Salary',fg='Steel Blue',anchor='w',bd=20).grid(row=0,column=1)
Label(f2,font=('arial',10,'bold'),text='July=',fg='Steel Blue',anchor='w',bd=20).grid(row=1,column=0)
Entry(f2,textvariable = mystring6,font=('arial',10,'bold'),bd=10,insertwidth=2,justify='right').grid(row=1,column=1)
Label(f2,font=('arial',10,'bold'),text='Augest=',fg='Steel Blue',anchor='w',bd=20).grid(row=2,column=0)
Entry(f2,textvariable = mystring7,font=('arial',10,'bold'),bd=10,insertwidth=2,justify='right').grid(row=2,column=1)
Label(f2,font=('arial',10,'bold'),text='Sep=',fg='Steel Blue',anchor='w',bd=20).grid(row=3,column=0)
Entry(f2,textvariable = mystring8,font=('arial',10,'bold'),bd=10,insertwidth=2,justify='right').grid(row=3,column=1)
Label(f2,font=('arial',10,'bold'),text='Oct=',fg='Steel Blue',anchor='w',bd=20).grid(row=4,column=0)
Entry(f2,textvariable = mystring9,font=('arial',10,'bold'),bd=10,insertwidth=2,justify='right').grid(row=4,column=1)
Label(f2,font=('arial',10,'bold'),text='Nov=',fg='Steel Blue',anchor='w',bd=20).grid(row=5,column=0)
Entry(f2,textvariable = mystring10,font=('arial',10,'bold'),bd=10,insertwidth=2,justify='right').grid(row=5,column=1)
Label(f2,font=('arial',10,'bold'),text='Dec=',fg='Steel Blue',anchor='w',bd=20).grid(row=6,column=0)
Entry(f2,textvariable = mystring11,font=('arial',10,'bold'),bd=10,insertwidth=2,justify='right').grid(row=6,column=1)
"""******************************************Button************************************************************"""
def plotgraph():
    bs = [mystring0.get(),mystring1.get(),mystring2.get(),mystring3.get(),mystring4.get(),mystring5.get(),mystring6.get(),mystring7.get(),mystring8.get(),mystring9.get(),mystring10.get(),mystring11.get()]

    month = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'oct', 'Nov', 'Dec']
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    plt.xticks(a, month)
    ax = plt.gca()
    ax.set_axis_bgcolor("lightgray")
    bars = plt.bar(a, bs, align='center', linewidth=0, color='lightslategrey')

    for bar in bars:
        plt.gca().text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, str(int(bar.get_height())), ha='center',
                       color='w', fontsize='12', rotation=90)
    plt.xlabel("-----------------Month---------------->")
    plt.ylabel("----------------Salary--------------->")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.title("Month Salary Graph")
    plt.show()
plot_button = Button(f3, text = "plot", command =plotgraph, font =('arial',15,'bold'), foreground = "Steel Blue",bd=10,bg='powder blue').grid(row=0,column=1)

mainloop()