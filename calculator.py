from tkinter import *

expression =""

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equal():
	try:
		global expression
		result = str(eval(expression))
		equation.set(result)
		expression=""
	except:
		equation.set("error")
		expression=""	



def clear():
	global expression	
	expression = ""
	equation.set("")

if __name__== "__main__":
	gui = Tk()
	gui.geometry('280x300')	
	gui.configure(bg='light blue')
	gui.title("Calculaor Si")


	equation=StringVar()
    #////////
	expression_field = Entry(gui,bg='white',textvariable=equation,border=5)
	expression_field.grid(columnspan=4,ipadx=70,ipady=6,padx=5,pady=5)

	Button1= Button(gui,bg='white',text='1',command=lambda:press(1),pady=10,padx=10,border=5)
	Button1.grid(column=0,row=3)

	Button2= Button(gui,bg='white',text='2',command=lambda:press(2),pady=10,padx=10,border=5)
	Button2.grid(column=1,row=3)

	Button3= Button(gui,bg='white',text='3',command=lambda:press(3),pady=10,padx=10,border=5)
	Button3.grid(column=2,row=3)
    
	plus= Button(gui,bg='white',text='+',command=lambda:press("+"),pady=10,padx=10,border=5)
	plus.grid(column=3,row=3)



	Button4= Button(gui,bg='white',text='4',command=lambda:press(4),pady=10,padx=10,border=5)
	Button4.grid(column=0,row=4)

	Button5= Button(gui,bg='white',text='5',command=lambda:press(5),pady=10,padx=10,border=5)
	Button5.grid(column=1,row=4)

	Button6= Button(gui,bg='white',text='6',command=lambda:press(6),pady=10,padx=10,border=5)
	Button6.grid(column=2,row=4)

	min= Button(gui,bg='white',text='-',command=lambda:press("-"),pady=10,padx=10,border=5)
	min.grid(column=3,row=4)


	Button7= Button(gui,bg='white',text='7',command=lambda:press(7),pady=10,padx=10,border=5)
	Button7.grid(column=0,row=5)

	Button8= Button(gui,bg='white',text='8',command=lambda:press(8),pady=10,padx=10,border=5)
	Button8.grid(column=1,row=5)

	Button9= Button(gui,bg='white',text='9',command=lambda:press(9),pady=10,padx=10,border=5)
	Button9.grid(column=2,row=5)

	multy= Button(gui,bg='white',text='*',command=lambda:press("*"),pady=10,padx=10,border=5)
	multy.grid(column=3,row=5)




	decimal= Button(gui,bg='white',text='.',command=lambda:press("."),pady=10,padx=10,border=5)
	decimal.grid(column=0,row=6)

	Button0= Button(gui,bg='white',text='0',command=lambda:press(0),pady=10,padx=10,border=5)
	Button0.grid(column=1,row=6)

	equalpress = Button(gui,bg='white',text='=',command=equal,pady=10,padx=10,border=5)
	equalpress.grid(column=2,row=6)

	div= Button(gui,bg='white',text='/',command=lambda:press("/"),pady=10,padx=10,border=5)
	div.grid(column=3,row=6)




	clears = Button(gui,bg='white',text='C',command=clear,pady=10,padx=10,border=5)
	clears.grid(columnspan=3,row=7)







	gui.mainloop()
	



