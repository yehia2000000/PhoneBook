#!/bin/python3
import tkinter as GUI 
from tkinter import messagebox

'''
Data of Login of the mangers 
'''
Mangers_Data = {"yehia":"1234","AboZied":"5678","Shahin":"012"}

'''
Function that used in GUI 
'''
Name =0
SendButton =0 
Email =0 
Number  =0


def SendButtonFunction ():
	global Var1 
	global Name
	global Email
	global Number
	counter =0
	AnotherString = ""
	SelectString = ""
	Select = Var1.get()
	if (Select==0):
		MyFile = open ("Data.txt","r")
		for line in MyFile: 
			SelectLine =line
			if (line.startswith("Name:"+Name.get())) :
				messagebox.showinfo ("User Information",SelectLine+MyFile.readline()+MyFile.readline())
				MyFile.close()
				return
		messagebox.showerror ("User Information","User informatin is not found")
		MyFile.close()

	elif (Select == 2):
		MyFile = open("Data.txt","a")
		MyFile.write("Name:"+Name.get()+"\n"+"Email:"+Email.get()+"\n"+"Number:"+Number.get()+"\n\n")
		MyFile.close()
	elif (Select ==3):
		MyFile =open ("Data.txt","r")
		for line in MyFile:
			if (line.startswith("Name:"+Name.get())):
				SelectString = line + MyFile.readline()+"Number:"+Number.get()
				counter=1
			if (counter ==0 ):
				AnotherString ="\n"+ AnotherString +line
			if (line.startswith("Number:")):
				counter=0
		MyFile.close()
		MyFile =open("Data.txt","w")
		MyFile.write(SelectString+AnotherString)
		MyFile.close()
	elif (Select ==4):
		MyFile =open ("Data.txt","r")
		for line in MyFile:
			if (line.startswith("Name:"+Name.get())):
				counter=1
			if (counter ==0 ):
				AnotherString ="\n"+ AnotherString +line
			if (line.startswith("Number:")):
				counter=0
		MyFile.close()
		MyFile =open("Data.txt","w")
		MyFile.write(AnotherString)
		MyFile.close()
	

	
def ChooseButtonFunction ():
	global Var1 
	global Name
	global SendButton
	global Email
	global Number
	Select =Var1.get()
	if (Select==0):
		SendButton.configure(state="normal")
		Name.configure(state="normal")
		Email.configure (state ="disable")
		Number.configure (state ="disable")
	elif (Select ==1):
		SendButton.configure (state ="disable")
		Name.configure (state ="disable")
		Email.configure (state = "disable")
		Number.configure (state ="disable")
		MyFile=open("Data.txt","r")
		messagebox.showinfo("Users Information",MyFile.read())
		MyFile.close()
	elif (Select ==2):
		Name.configure (state ="normal")
		Email.configure (state = "normal")
		Number.configure (state = "normal")
		SendButton.configure (state ="normal")
	elif (Select==3):
		Name.configure (state="normal")
		Number.configure (state="normal")
		Email.configure (state = "disable")
		SendButton.configure (state = "normal")
	elif (Select == 4):
		Name.configure (state="normal")
		Number.configure (state="disable")
		Email.configure (state ="disable")
		SendButton.configure (state = "normal")
	elif (Select == 5):
		Name.configure (state ="disable")
		Number.configure (state = "disable")
		Email.configure (state = "disable")
		SendButton.configure (state = "disable")
		MyFile = open ("Data.txt","w")
		MyFile.write("")
		MyFile.close()
	else :
		Name.configure (state ="disable")
		Number.configure (state = "disable")
		Email.configure (state = "disable")
		SendButton.configure (state = "disable")



def Option_Window_Init (Option_Window):
	Option_Window.title ("Selection Options")
	Option_Window.geometry("400x500+100+100")
	Option_Window.resizable (False,False)
	Option_Window.configure (bg ="black")
def Options (Option_Window):
	global Var1
	ShowContent = GUI.Radiobutton (Option_Window,bg="black",fg="blue",text ="Show Content",value =0 ,variable = Var1)
	ShowAllContent =GUI.Radiobutton (Option_Window,bg="black",fg="blue",text ="Show all content",value =1 ,variable =Var1)
	AddContent = GUI.Radiobutton (Option_Window,bg="black",fg="blue" ,text = "add content",value =2 ,variable =Var1)
	UpdateContent =GUI.Radiobutton (Option_Window,bg="black",fg="blue",text = "update content ",value =3 ,variable =Var1)
	DeleteContent =GUI.Radiobutton (Option_Window,bg="black",fg="blue" , text = "delete content",value=4,variable =Var1)
	DeleteAll =GUI.Radiobutton (Option_Window,bg="black",fg="blue", text ="delete all",value=5,variable=Var1)
	Exit = GUI.Radiobutton (Option_Window,bg="black",fg="blue", text = "exit",value =6 ,variable =Var1)
	ShowContent.place (x=10,y=20)
	ShowAllContent.place (x=10,y= 50)
	AddContent.place (x=10,y=80)
	UpdateContent.place (x=10,y=110)
	DeleteContent.place (x=10,y=140)
	DeleteAll.place (x=10,y=170)
	Exit.place (x=10,y=200)

def CreateButton (Option_Window):
	global SendButton
	SendButton =GUI.Button (Option_Window,text="Send",command=SendButtonFunction)
	ChooseButton = GUI.Button (Option_Window,text="Choose",command=ChooseButtonFunction)
	SendButton.place (x=300,y=310)
	ChooseButton.place (x=200,y=110)
	SendButton.configure (state ="disable")
def CreateFrame (Option_Window):
	global Name 
	global Email
	global Number
	Email = GUI.Entry (Option_Window)
	Name = GUI.Entry (Option_Window)
	Number = GUI.Entry (Option_Window)
	Email.place (x=100,y=310)
	Name.place  (x=100,y=280)
	Number.place (x=100,y=340)
	Email.configure (state= "disable")
	Number.configure (state ="disable")
	Name.configure (state ="disable")
def CreateLabel(Option_Window):
	EmailLabel = GUI.Label(Option_Window,text="Email",bg="black",fg="white")
	NameLabel = GUI.Label (Option_Window,text ="Name",bg = "black",fg="white")
	NumberLabel =GUI.Label (Option_Window,text="Number",bg="black",fg ="white")
	EmailLabel.place(x=20,y=310)
	NameLabel.place (x=20,y=280)
	NumberLabel.place (x=20,y=340)

def Login ():
	try:
		if (Mangers_Data[User_Name.get()]==PassWord.get()):
			Option_Window = GUI.Toplevel()
			Option_Window_Init(Option_Window)
			Options(Option_Window)
			CreateButton(Option_Window)
			CreateFrame (Option_Window)
			CreateLabel (Option_Window)
			Option_Window.mainloop() 
		else :
			Error = GUI.Label (Login_Window,bg ="black",fg="white",text="the user name or password is not correct")
			Error.place (x=20,y=190)

	except:
		Error = GUI.Label (Login_Window,bg ="black",fg="white",text ="Username or password  is not correct")
		Error.place (x=20,y=190)

'''
Implement the Window 
'''

Login_Window=GUI.Tk()
Login_Window.title ("PhoneBook")
Login_Window.geometry ("300x300+150+150")
Login_Window.resizable (False ,False)
Login_Window.configure (bg="black")

Var1 = GUI.IntVar()
'''
Implement the Entry 

'''
User_Name = GUI.Entry (Login_Window,bg="white")
PassWord = GUI.Entry(Login_Window, bg ="white")

User_Name.place (x=100,y=100)
PassWord.place (x=100,y=130)

'''
Create the Label 
'''

User = GUI.Label (Login_Window,text ="User Name", bg = "black",fg ="white")
Pas = GUI.Label (Login_Window , text ="Password",bg  ="black",fg ="white")

User.place(x=20,y=100)
Pas.place (x=20,y=130)

'''
Create the Button 

'''

Login = GUI.Button (Login_Window , text ="Login",bg = "white",fg="blue",command = Login)
Login.place (x=100,y=160)



Login_Window.mainloop()


 
