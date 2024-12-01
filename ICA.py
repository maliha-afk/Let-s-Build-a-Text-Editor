from tkinter import *

screen=Tk()
screen.title("interest calculator")
screen.config(bg="cornflowerblue")
screen.geometry("500x500")

Label(screen,text="Welcome to Interest Calculator App",font=("Arial",15,"bold"),fg="black",bg="cornflowerblue").place(x=80,y=10)

amount_la=Label(screen,text="enter principle amount: ",font=("Arial",15,"bold"),fg="black",bg="cornflowerblue")
amount_la.place(x=10,y=50)
amount=Entry(screen,font=("Arial",15,"bold"))
amount.place(x=220,y=50)

time_la=Label(screen,text="enter duration in year: ",font=("Arial",15,"bold"),fg="black",bg="cornflowerblue")
time_la.place(x=10,y=80)
time=Entry(screen,font=("Arial",15,"bold"))
time.place(x=220,y=80)


interest_la=Label(screen,text="enter interest value: ",font=("Arial",15,"bold"),fg="black",bg="cornflowerblue")
interest_la.place(x=10,y=110)
intereste=Entry(screen,font=("Arial",15,"bold"))
intereste.place(x=220,y=110)

def calcint():
    interest=(int(amount.get()))*(int(time.get()))*(int(intereste.get()))/100
    totalamount=interest+(int(amount.get()))
    myamount.config(text=f"interest value: {interest} INR \n total amount: {totalamount} INR")

simpleintbut=Button(screen,text="calculate simple interest ",font=("Arial",15,"bold"),fg="black",bg="lightblue",relief="sunken",command=calcint)
simpleintbut.place(x=180,y=150)

myamount=Label(screen,font=("Arial",15,"bold"),fg="black",bg="cornflowerblue")
myamount.place(x=100,y=200)


screen.mainloop()