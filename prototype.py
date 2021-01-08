import tkinter as tk
from tkinter import ttk

root= tk.Tk()
root.title('Primal To Duality Conversion')

canvas1 = tk.Canvas(root, width = 800, height = 600,  relief = 'raised')
canvas1.pack()
#Heading
label1 = tk.Label(root, text='Conversion of Primal to Duality',fg='white',bg='black')
label1.config(font=('helvetica', 20))
canvas1.create_window(400, 30, window=label1)
#Credit
label2 = tk.Label(root, text='Submitted By: Rishav Dhungel',fg='blue',bg='yellow')
label2.config(font=('helvetica', 14))
canvas1.create_window(200, 70, window=label2)

label3 = tk.Label(root, text='Submitted To: Durga Prasad Dhakal',fg='blue',bg='yellow')
label3.config(font=('helvetica', 14))
canvas1.create_window(550, 70, window=label3)

#creating entry lable and entry for Max(Z)
label4 = tk.Label(root, text='Max(Z) = ',fg='black')
label4.config(font=('helvetica', 15))
canvas1.create_window(120, 160, window=label4)
#1
entry1 = tk.Entry (root) 
canvas1.create_window(180, 160, window=entry1,height=40,width=40)
label5 = tk.Label(root, text='X1 +',fg='black')
label5.config(font=('helvetica', 15))
canvas1.create_window(225, 165, window=label5)
#2
entry2 = tk.Entry (root) 
canvas1.create_window(180+90, 160, window=entry2,height=40,width=40)
label6 = tk.Label(root, text='X2 +',fg='black')
label6.config(font=('helvetica', 15))
canvas1.create_window(225+90, 165, window=label6)
#3
entry3 = tk.Entry (root) 
canvas1.create_window(180+90+90, 160, window=entry3,height=40,width=40)
label7 = tk.Label(root, text='X3',fg='black')
label7.config(font=('helvetica', 15))
canvas1.create_window(225+90+80, 165, window=label7)

#creating entry lable and entry for 1st equation
#1
bentry1 = tk.Entry (root) 
canvas1.create_window(180, 160+50, window=bentry1,height=40,width=40)
blabel5 = tk.Label(root, text='X1 +',fg='black')
blabel5.config(font=('helvetica', 15))
canvas1.create_window(225, 165+50, window=blabel5)
#2
bentry2 = tk.Entry (root) 
canvas1.create_window(180+90, 160+50, window=bentry2,height=40,width=40)
blabel6 = tk.Label(root, text='X2 +',fg='black')
blabel6.config(font=('helvetica', 15))
canvas1.create_window(225+90, 165+50, window=blabel6)
#3
bentry3 = tk.Entry (root) 
canvas1.create_window(180+90+90, 160+50, window=bentry3,height=40,width=40)
blabel7 = tk.Label(root, text='X3',fg='black')
blabel7.config(font=('helvetica', 15))
canvas1.create_window(225+90+80, 165+50, window=blabel7)
#symbol
bentry4 = ttk.Combobox(root,values=['<=','>=','='])
bentry4.current(1)
canvas1.create_window(180+90+170, 160+50, window=bentry4,height=40,width=40)
#constant
bentry3 = tk.Entry (root) 
canvas1.create_window(180+90+220, 160+50, window=bentry3,height=40,width=40)


#creating entry lable and entry for 2nd equation
#1
centry1 = tk.Entry (root) 
canvas1.create_window(180, 160+50+50, window=centry1,height=40,width=40)
clabel5 = tk.Label(root, text='X1 +',fg='black')
clabel5.config(font=('helvetica', 15))
canvas1.create_window(225, 165+50+50, window=clabel5)
#2
centry2 = tk.Entry (root) 
canvas1.create_window(180+90, 160+50+50, window=centry2,height=40,width=40)
clabel6 = tk.Label(root, text='X2 +',fg='black')
clabel6.config(font=('helvetica', 15))
canvas1.create_window(225+90, 165+50+50, window=clabel6)
#3
centry3 = tk.Entry (root) 
canvas1.create_window(180+90+90, 160+50+50, window=centry3,height=40,width=40)
clabel7 = tk.Label(root, text='X3',fg='black')
clabel7.config(font=('helvetica', 15))
canvas1.create_window(225+90+80, 165+50+50, window=clabel7)
#symbol
centry4 = ttk.Combobox(root,values=['<=','>=','='])
centry4.current(1)
canvas1.create_window(180+90+170, 160+50+50, window=centry4,height=40,width=40)
#constant
centry3 = tk.Entry (root) 
canvas1.create_window(180+90+220, 160+50+50, window=centry3,height=40,width=40)

#creating entry lable and entry for 3rd equation
#1
dentry1 = tk.Entry (root) 
canvas1.create_window(180, 160+150, window=dentry1,height=40,width=40)
dlabel5 = tk.Label(root, text='X1 +',fg='black')
dlabel5.config(font=('helvetica', 15))
canvas1.create_window(225, 165+150, window=dlabel5)
#2
dentry2 = tk.Entry (root) 
canvas1.create_window(180+90, 160+150, window=dentry2,height=40,width=40)
dlabel6 = tk.Label(root, text='X2 +',fg='black')
dlabel6.config(font=('helvetica', 15))
canvas1.create_window(225+90, 165+150, window=dlabel6)
#3
dentry3 = tk.Entry (root) 
canvas1.create_window(180+90+90, 160+150, window=dentry3,height=40,width=40)
dlabel7 = tk.Label(root, text='X3',fg='black')
dlabel7.config(font=('helvetica', 15))
canvas1.create_window(225+90+80, 165+150, window=dlabel7)
#symbol
leore = '>='
geore = '<='
equal = '='
dentry4 = ttk.Combobox(root,values=[geore,leore,equal])
dentry4.current(1)
canvas1.create_window(180+90+170, 160+150, window=dentry4,height=40,width=40)
#constant
dentry3 = tk.Entry (root) 
canvas1.create_window(180+90+220, 160+150, window=dentry3,height=40,width=40)

#last portion
dlabel7 = tk.Label(root, text='X1,X2,X3 >= 0',fg='black')
dlabel7.config(font=('helvetica', 15))
canvas1.create_window(225, 165+200, window=dlabel7)

#Button Portion
button1 = tk.Button(text='Convert',  bg='blue', fg='white', font=('helvetica', 15, 'bold'),relief = 'solid')
canvas1.create_window(380, 365+50, window=button1,height=50,width=100)

root.mainloop()