import tkinter as tk
import tkinter.messagebox as mb
from PIL import ImageTk, Image
import webbrowser

#function

def run():
    if weight.get() =='' or height.get()=='' :
        mb.showwarning('Warning !','one or more field are empty !')

    else:
        result=float(weight.get())/float(height.get())**2
        tk.Label(text=f"{round(result,2)}", fg="lime", font=("jost", 12, "bold")).place(x=170, y=300)
        if 18.5 < result < 24.9:
            tk.Label(text='Healthy !     ', fg="lime", font=("jost", 12, "bold")).place(x=170, y=340)
        else:
            tk.Label(text='Unhealthy !', fg="lime", font=("jost", 12, "bold")).place(x=170, y=340)

def go():
    webbrowser.open_new_tab('https://www.facebook.com/profile.php?id=100036971298466')
    webbrowser.open_new('https://github.com/Shakil-Mahmud-Programmer')


window=tk.Tk()
window.title('BMI')
window.geometry('450x500')
window.iconbitmap('icon.ico')
tk.Label(text="Body Mass Index Calculator",fg="deepskyblue",font=("jost",12,"bold")).place(x=110,y=10)
im=ImageTk.PhotoImage(Image.open('weight.ico'))
tk.Label(image=im).place(x=150,y=45)
im1=ImageTk.PhotoImage(Image.open('github1.ico'))
tk.Label(image=im1).place(x=250,y=442)
im2=ImageTk.PhotoImage(Image.open('facebook1.ico'))
tk.Label(image=im2).place(x=300,y=450)

tk.Label(text="Weight",fg="magenta",font=("jost",12,"bold")).place(x=100,y=200)
weight=tk.StringVar()
tk.Entry(textvariable=weight,font=('jost',12,'bold'),fg='lime',width=10).place(x=170,y=200)
tk.Label(text="Kg",fg="black",font=("jost",12)).place(x=270,y=200)


tk.Label(text="Height ",fg="magenta",font=("jost",12,"bold")).place(x=100,y=250)
height=tk.StringVar()
tk.Entry(textvariable=height,font=('jost',12,'bold'),fg='lime',width=10).place(x=170,y=250)
tk.Label(text="m",fg="black",font=("jost",12)).place(x=270,y=250)

tk.Label(text="BMI : ",fg="deepskyblue",font=("jost",12,"bold")).place(x=120,y=300)
tk.Label(text="Status : ",fg="deepskyblue",font=("jost",12,"bold")).place(x=100,y=340)

tk.Button(text="Calculate",bg="deepskyblue",fg="White",font="Bold,200",height=1,width=8,command=run).place(x=170,y=400)
tk.Button(text="Developer",bg="orange",fg="White",font="Bold,200",height=1,width=8,command=go).place(x=350,y=453)

window.mainloop()