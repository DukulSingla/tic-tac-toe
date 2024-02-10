import tkinter as tk
import tkinter.messagebox
from tkinter.tix import COLUMN

window = tk.Tk()
window.title('Tic Tac Toe')
frame = tk.Frame(master=window)
frame.pack(pady=10)

label = tk.Label(master = frame, text = "Tic Tac Toe", font = ("Arial", 15))
label.pack()

frame1 = tk.Frame(master = window, borderwidth = 2, relief = tk.SUNKEN, bg = '#dadec3')

frame1.pack(padx = 10, pady= 10)

def create_button(num, row, column):
    button = tk.Button(master=frame1,text='',width=10,height=5,bg='white',command=lambda : buttonclick(num))
    button.grid(row=row,column=column,padx=5,pady=5)

    return button
button1 = create_button(1, 0, 0)
button2 = create_button(2, 0, 1)
button3 = create_button(3, 0, 2)
button4 = create_button(4, 1, 0)
button5 = create_button(5, 1, 1)
button6 = create_button(6, 1, 2)
button7 = create_button(7, 2, 0)
button8 = create_button(8, 2, 1)
button9 = create_button(9, 2, 2)


frame2=tk.Frame(master=window,border=2,relief=tk.SUNKEN,bg='#dadec3')
frame2.pack()
label1=tk.Label(master=frame2,text="Player 1 --> X\nPlayer 2 --> O",width=10)
label1.grid(row=0,column=0,padx=5)
button_restart=tk.Button(master=frame2,text="Restart",width=10,height=3,relief=tk.GROOVE,command=lambda: restartbutton())
button_restart.grid(row=0,column=1,padx=10,pady=10)
label2=tk.Label(master=frame2,text='Player-1 Turn',bg="skyblue",width=10,height=3,relief=tk.SUNKEN)
label2.grid(row=0,column=2,padx=5)
a=1
b=0
c=0

def disablebutton():
    button1['state']=tk.DISABLED
    button2['state']=tk.DISABLED
    button3['state']=tk.DISABLED
    button4['state']=tk.DISABLED
    button5['state']=tk.DISABLED
    button6['state']=tk.DISABLED
    button7['state']=tk.DISABLED
    button8['state']=tk.DISABLED
    button9['state']=tk.DISABLED

def restartbutton():
    global a,b,c
    a=1
    b=0
    c=0
    label2['bg']="skyblue"
    label2['text']='Player-1 Turn'
    button1['text']=''
    button1['bg']='white'
    button2['text']=''
    button2['bg']='white'
    button3['text']=''
    button3['bg']='white'
    button4['text']=''
    button4['bg']='white'
    button5['text']=''
    button5['bg']='white'
    button6['text']=''
    button6['bg']='white'
    button7['text']=''
    button7['bg']='white'
    button8['text']=''
    button8['bg']='white'
    button9['text']=''
    button9['bg']='white'
    button1['state']=tk.NORMAL
    button2['state']=tk.NORMAL
    button3['state']=tk.NORMAL
    button4['state']=tk.NORMAL
    button5['state']=tk.NORMAL
    button6['state']=tk.NORMAL
    button7['state']=tk.NORMAL
    button8['state']=tk.NORMAL
    button9['state']=tk.NORMAL

def buttonclick(x):
    global a,b,c
    #for player 1
    if(x==1 and a==1 and button1['text']==''):
        button1['text']="X"
        button1['bg']="skyblue"
        label2['bg']="#e8956f"
        label2['text']='Player-2 Turn'
        a=0
        b+=1
    if(x==2 and a==1 and button2['text']==''):
        button2['text']="X"
        button2['bg']="skyblue"
        label2['bg']="#e8956f"
        label2['text']='Player-2 Turn'
        a=0
        b+=1
    if(x==3 and a==1 and button3['text']==''):
        button3['text']="X"
        button3['bg']="skyblue"
        label2['bg']="#e8956f"
        label2['text']='Player-2 Turn'
        a=0
        b+=1
    if(x==4 and a==1 and button4['text']==''):
        button4['text']="X"
        button4['bg']="skyblue"
        label2['bg']="#e8956f"
        label2['text']='Player-2 Turn'
        a=0
        b+=1
    if(x==5 and a==1 and button5['text']==''):
        button5['text']="X"
        button5['bg']="skyblue"
        label2['bg']="#e8956f"
        label2['text']='Player-2 Turn'
        a=0
        b+=1
    if(x==6 and a==1 and button6['text']==''):
        button6['text']="X"
        button6['bg']="skyblue"
        label2['bg']="#e8956f"
        label2['text']='Player-2 Turn'
        a=0
        b+=1
    if(x==7 and a==1 and button7['text']==''):
        button7['text']="X"
        button7['bg']="skyblue"
        label2['bg']="#e8956f"
        label2['text']='Player-2 Turn'
        a=0
        b+=1
    if(x==8 and a==1 and button8['text']==''):
        button8['text']="X"
        button8['bg']="skyblue"
        label2['bg']="#e8956f"
        label2['text']='Player-2 Turn'
        a=0
        b+=1
    if(x==9 and a==1 and button9['text']==''):
        button9['text']="X"
        button9['bg']="skyblue"
        label2['bg']="#e8956f"
        label2['text']='Player-2 Turn'
        a=0
        b+=1

    #for player 2
    if(x==1 and a==0 and button1['text']==''):
        button1['text']='O'
        button1['bg']="#e8956f"
        label2['bg']="skyblue"
        label2['text']='Player-1 Turn'
        a=1
        b+=1
    if(x==2 and a==0 and button2['text']==''):
        button2['text']='O'
        button2['bg']="#e8956f"
        label2['bg']="skyblue"
        label2['text']='Player-1 Turn'
        a=1
        b+=1
    if(x==3 and a==0 and button3['text']==''):
        button3['text']='O'
        button3['bg']="#e8956f"
        label2['bg']="skyblue"
        label2['text']='Player-1 Turn'
        a=1
        b+=1
    if(x==4 and a==0 and button4['text']==''):
        button4['text']='O'
        button4['bg']="#e8956f"
        label2['bg']="skyblue"
        label2['text']='Player-1 Turn'
        a=1
        b+=1
    if(x==5 and a==0 and button5['text']==''):
        button5['text']='O'
        button5['bg']="#e8956f"
        label2['bg']="skyblue"
        label2['text']='Player-1 Turn'
        a=1
        b+=1
    if(x==6 and a==0 and button6['text']==''):
        button6['text']='O'
        button6['bg']="#e8956f"
        label2['bg']="skyblue"
        label2['text']='Player-1 Turn'
        a=1
        b+=1
    if(x==7 and a==0 and button7['text']==''):
        button7['text']='O'
        button7['bg']="#e8956f"
        label2['bg']="skyblue"
        label2['text']='Player-1 Turn'
        a=1
        b+=1
    if(x==8 and a==0 and button8['text']==''):
        button8['text']='O'
        button8['bg']="#e8956f"
        label2['bg']="skyblue"
        label2['text']='Player-1 Turn'
        a=1
        b+=1
    if(x==9 and a==0 and button9['text']==''):
        button9['text']='O'
        button9['bg']="#e8956f"
        label2['bg']="skyblue"
        label2['text']='Player-1 Turn'
        a=1
        b+=1

    #checking winner
    if(button1['text']=='X' and button2['text']=='X' and button3['text']=='X' or
        button4['text']=='X' and button5['text']=='X' and button6['text']=='X' or
        button7['text']=='X' and button8['text']=='X' and button9['text']=='X' or
        button1['text']=='X' and button4['text']=='X' and button7['text']=='X' or
        button2['text']=='X' and button5['text']=='X' and button8['text']=='X' or
        button3['text']=='X' and button6['text']=='X' and button9['text']=='X' or
        button1['text']=='X' and button5['text']=='X' and button9['text']=='X' or
        button3['text']=='X' and button5['text']=='X' and button7['text']=='X'):
            disablebutton()
            c=1
            tkinter.messagebox.showinfo("Tic Tac Toe","Winner is player 1")
    elif( button1['text']=='O' and button2['text']=='O' and button3['text']=='O' or
        button4['text']=='O' and button5['text']=='O' and button6['text']=='O' or
        button7['text']=='O' and button8['text']=='O' and button9['text']=='O' or
        button1['text']=='O' and button4['text']=='O' and button7['text']=='O' or
        button2['text']=='O' and button5['text']=='O' and button8['text']=='O' or
        button3['text']=='O' and button6['text']=='O' and button9['text']=='O' or
        button1['text']=='O' and button5['text']=='O' and button9['text']=='O' or
        button3['text']=='O' and button5['text']=='O' and button7['text']=='O'):
            disablebutton()
            c=1
            tkinter.messagebox.showinfo("Tic Tac Toe","Winner is player 2")
    elif(b==9):
        disablebutton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Match is Draw.")
    
window.mainloop()