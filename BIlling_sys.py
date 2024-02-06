# import tkinter module 
from tkinter import *

# make a window 
window = Tk() 
window.title("Billing_system")

# specify it's size 
window.geometry("710x700") 

# take a image for background 
bg = PhotoImage(file='bg1.png') 

# label it in the background 
label17 = Label(window, image=bg) 

# position the image as well 
label17.place(x=0, y=0) 


# function to calculate the 
# price of all the orders 
def calculate(): 

		# dic for storing the 
	# food quantity and price 
	dic = {'aloo_partha': [e1, 20], 
		'samosa': [e2, 10], 
		'pizza': [e3, 99], 
		'chilli_potato': [e4, 70], 
		'chowmein': [e5, 60], 
		'gulab_jamun': [e6, 20]} 
	total = 0
	for key, val in dic.items(): 
		if val[0].get() != "": 
			total += int(val[0].get())*val[1] 

	label16 = Label(window, 
					text="Your Total Bill is just: "+str(total), 
					font="times 18") 

	# position it 
	label16.place(x=20, y=490) 
	label16.after(1000, label16.destroy) 
	window.after(1000, calculate) 


label8 = Label(window, 
			text="Saurabh's Restaurant", 
			font="times 28 bold", bg='blue') 
label8.place(x=350, y=20, anchor="center") 


label1 = Label(window, 
			text="Menu", 
			font="times 28 bold", bg='red') 

label1.place(x=520, y=70) 

label2 = Label(window, text="Aloo Paratha        Rs 20", font="times 18", bg='orange') 
label2.place(x=450, y=120) 

label3 = Label(window, text="Samosa                Rs 10", font="times 18", bg='yellow') 
label3.place(x=450, y=150) 

label4 = Label(window, text="Pizza	             Rs 99", font="times 18", bg='orange') 
label4.place(x=450, y=180) 

label5 = Label(window, text="Chilli Potato        Rs 70", font="times 18", bg='yellow') 
label5.place(x=450, y=210) 

label6 = Label(window, text="Chowmein            Rs 60", font="times 18", bg='orange') 
label6.place(x=450, y=240) 

label7 = Label(window, text="Gulab Jamun         Rs 20", font="times 18", bg='yellow') 
label7.place(x=450, y=270) 

# billing section 
label9 = Label(window, text="Items no.", 
			font="times 18", bg='orange') 
label9.place(x=115, y=70) 

label10 = Label(window, 
				text="Aloo Paratha", 
				font="times 18") 
label10.place(x=20, y=120) 

e1 = Entry(window) 
e1.place(x=20, y=150) 

label11 = Label(window, text="Samosa", 
				font="times 18") 
label11.place(x=20, y=200) 

e2 = Entry(window) 
e2.place(x=20, y=230) 

label12 = Label(window, text="Pizza", 
				font="times 18") 
label12.place(x=20, y=280) 

e3 = Entry(window) 
e3.place(x=20, y=310) 

label13 = Label(window, 
				text="Chilli Potato", 
				font="times 18") 
label13.place(x=20, y=360) 

e4 = Entry(window) 
e4.place(x=20, y=390) 

label14 = Label(window, 
				text="Chowmein", 
				font="times 18") 
label14.place(x=250, y=120) 

e5 = Entry(window) 
e5.place(x=250, y=150) 

label15 = Label(window, 
				text="Gulab Jamun", 
				font="times 18") 

label15.place(x=250, y=200) 

e6 = Entry(window) 
e6.place(x=250, y=230) 

# execute calculate function after 1 second 
window.after(1000, calculate) 

# closing the main loop 
window.mainloop() 