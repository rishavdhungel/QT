#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import Frame
import sys 
import os

root= tk.Tk()
root.title('Primal To Duality Conversion')

canvas1 = tk.Canvas(root, width = 800, height = 900,  relief = 'raised')
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
bentry4.current(0)
canvas1.create_window(180+90+170, 160+50, window=bentry4,height=40,width=40)
#constant
bentry5 = tk.Entry (root) 
canvas1.create_window(180+90+220, 160+50, window=bentry5,height=40,width=40)


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
centry5 = tk.Entry (root) 
canvas1.create_window(180+90+220, 160+50+50, window=centry5,height=40,width=40)

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
dentry4 = ttk.Combobox(root,values=[equal])
dentry4.current(0)
canvas1.create_window(180+90+170, 160+150, window=dentry4,height=40,width=40)
#constant
dentry5 = tk.Entry (root) 
canvas1.create_window(180+90+220, 160+150, window=dentry5,height=40,width=40)

#last portion
dlabel7 = tk.Label(root, text='X1,X2,X3 >= 0',fg='black')
dlabel7.config(font=('helvetica', 15))
canvas1.create_window(225, 165+200, window=dlabel7)
canvas1.create_rectangle(5, 450, 800, 800,fill='white')
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def Output():

  gore = "<="
  leore = ">="
  equal = "="
  Max = [int(entry1.get()),int(entry2.get()),int(entry3.get())]
  first = [int(bentry1.get()),int(bentry2.get()),int(bentry3.get())]
  firstsym = bentry4.get()
  firstvalue =int(bentry5.get())
  second = [int(centry1.get()),int(centry2.get()),int(centry3.get())]
  secondsym = centry4.get()
  secondvalue = int(centry5.get())
  third = [int(dentry1.get()),int(dentry2.get()),int(dentry3.get())]
  thirdsym = dentry4.get()
  thirdvalue = int(dentry5.get())
  final = [1,1,1]
  finalsym = leore
  finalvalue = 0




  #constant is greateroe equal to decision variables
  #if the  objective function is in maximization then we need to change the constant to the greater or equal than decison variable

  #change the equations to other function using if conditional to first and second equation
  #multiply both side with '-'
  if(firstsym == leore):
    newfirstsym = gore
    newfirst =[i * -1 for i in first]
    newfirstvalue = firstvalue *-1
  else:
    newfirst = first
    newfirstsym = firstsym
    newfirstvalue = firstvalue

  if(secondsym == leore):
    newsecond = [i *-1 for i in second]
    newsecondsym = gore
    newsecondvalue = secondvalue * -1
  else:
    newsecond = second
    newsecondsym = secondsym
    newsecondvalue = secondvalue

  #break the third equation into two part 
  third1 = third
  third1sym = leore
  third1value = thirdvalue

  third2 = third
  third2sym = gore
  third2value = thirdvalue



  #second Step
  #change the third equation into greater or equal
  if (third1sym == leore):
    newthird1 = [i *-1 for i in third1]
    newthird1sym = gore
    newthird1value = thirdvalue *-1
  else:
    newthird1 = third1
    newthird1sym = third1sym
    newthird1value = third1value

  if (third2sym == leore):
    newthird2 = [i *-1 for i in third2]
    newthird2sym = gore
    newthird2value = thirdvalue *-1
  else:
    newthird2 = third2
    newthird2sym = third2sym
    newthird2value = third2value



  #append Y1,Y2,Y3,Y4
  O1 = "======Output======"
  O2 = "Min = {}Y1 + {}Y2 + {}Y3 + {}Y4".format(newfirstvalue,newsecondvalue,newthird1value,newthird2value)
  O3 = "{}Y1 + {}Y2 + {}Y3 + {}Y4 {} {}".format(newfirst[0],newsecond[0],newthird1[0],newthird2[0],leore,Max[0])
  O4= "{}Y1 + {}Y2 + {}Y3 + {}Y4 {} {}".format(newfirst[1],newsecond[1],newthird1[1],newthird2[1],leore,Max[1])
  O5 = "{}Y1 + {}Y2 + {}Y3 + {}Y4 {} {}".format(newfirst[2],newsecond[2],newthird1[2],newthird2[2],leore,Max[2])
  O6 = "Y1,Y2,Y3,Y4 {} 0".format(leore)

  

  Olabel1 = tk.Label(root, text=O1,fg='black',bg='white')
  Olabel1.config(font=('helvetica', 17))
  canvas1.create_window(225+190, 305+225, window=Olabel1)

  Olabel2 = tk.Label(root, text=O2,fg='black',bg='white')
  Olabel2.config(font=('helvetica', 17))
  canvas1.create_window(225+190, 305+250, window=Olabel2)
  
  Olabel3 = tk.Label(root, text=O3,fg='black',bg='white')
  Olabel3.config(font=('helvetica', 17))
  canvas1.create_window(225+190, 305+300, window=Olabel3)

  Olabel4 = tk.Label(root, text=O4,fg='black',bg='white')
  Olabel4.config(font=('helvetica', 17))
  canvas1.create_window(225+190, 305+350, window=Olabel4)

  Olabel5 = tk.Label(root, text=O5,fg='black',bg='white')
  Olabel5.config(font=('helvetica', 17))
  canvas1.create_window(225+190, 305+400, window=Olabel5)

  Olabel6 = tk.Label(root, text=O6,fg='black',bg='white')
  Olabel6.config(font=('helvetica', 17))
  canvas1.create_window(225+170, 305+450, window=Olabel6)


#Button Portion
button1 = tk.Button(text='Convert',  bg='blue', fg='white', font=('helvetica', 15, 'bold'),relief = 'solid',command=Output)
canvas1.create_window(250, 365+50, window=button1,height=50,width=100)

#Button Portion
button2 = tk.Button(text='Reset',  bg='red', fg='white', font=('helvetica', 15, 'bold'),relief = 'solid',command=restart_program)
canvas1.create_window(480, 365+50, window=button2,height=50,width=100)


root.mainloop()