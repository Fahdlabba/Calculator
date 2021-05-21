from tkinter import *
import math
#-------------
def zero():
    taille = len(nb_entry.get())
    nb_entry.insert(taille,"0")
def one():
    taille=len(nb_entry.get())
    nb_entry.insert(taille,"1")
def two():
    taille=len(nb_entry.get())
    nb_entry.insert(taille,"2")
def three():
    taille = len(nb_entry.get())
    nb_entry.insert(taille,"3")
def four():
    taille = len(nb_entry.get())
    nb_entry.insert(taille,"4")
def five():
    taille = len(nb_entry.get())
    nb_entry.insert(taille,"5")
def six():
    taille = len(nb_entry.get())
    nb_entry.insert(taille,"6")
def seven():
    taille = len(nb_entry.get())
    nb_entry.insert(taille,"7")
def eight():
    taille = len(nb_entry.get())
    nb_entry.insert(taille,"8")
def nine():
    taille = len(nb_entry.get())
    nb_entry.insert(taille,"9")
def pos():
    taille = len(nb_entry.get())
    nb_entry.insert(taille,"-")
def add():
    taille = len(nb_entry.get())
    nb_entry.insert(taille,"+")
def point():
    taille = len(nb_entry.get())
    nb_entry.insert(taille,".")
def moin():
    taille = len(nb_entry.get())
    nb_entry.insert(taille,"-")
def div():
    taille = len(nb_entry.get())
    nb_entry.insert(taille,"//")
def mod():
    taille = len(nb_entry.get())
    nb_entry.insert(taille, "%")
def multp():
    taille=len(nb_entry.get())
    nb_entry.insert(taille, "*")
def sup():
    nb_entry.delete(0,END)
def supall():
    nb_entry.delete(0, END)
def dell():
    taille=len(nb_entry.get())-1
    nb_entry.delete(taille,END)
def puis():
    puiss=int(nb_entry.get())*int(nb_entry.get())
    rst_entry.delete(0,END)
    rst_entry.insert(0,puiss)
    nb_entry.delete(0, END)
def fnc():
    nb = 1/int(nb_entry.get())
    rst_entry.delete(0, END)
    rst_entry.insert(0, nb)
    nb_entry.delete(0, END)
def sqr():
    racine=math.sqrt(int(nb_entry.get()))
    rst_entry.delete(0, END)
    rst_entry.insert(0, racine)
    nb_entry.delete(0, END)
def reslt():
    try:
        n1="Result : "+str(eval(nb_entry.get()))
        rst_entry.delete(0, END)
        rst_entry.insert(0, n1)
        nb_entry.delete(0, END)
    except ZeroDivisionError:
        rst_entry.delete(0, END)
        rst_entry.insert(0,"ZERO DIVISION ERROR TRY AGAIN !!!!")
def bg():
    root.config(bg="yellow")
#--------
root=Tk()
root.title("Calculatrice")
root.geometry("400x300")
root.resizable(width=False,height=False)
root.config(bg="#fd0404")
#entry
nb_entry=Entry(root,font=("Times Roman",14),bg="#d8e1e8")
nb_entry.place(x=2,y=5,width=395,height=35)
rst_entry=Entry(root,font=("Times Roman",14),bg="#80ff00")
rst_entry.place(x=2,y=42,width=395,height=28)
#button
pos_button=Button(root,text="+/-",bg="#5093f8",command=pos)
pos_button.place(x=2,y=264,width=90,height=35)
zero_button=Button(root,text="0",bg="#5093f8",command=zero)
zero_button.place(x=94,y=264,width=90,height=35)
pt_button=Button(root,text=".",bg="#5093f8",command=point)
pt_button.place(x=186,y=264,width=90,height=35)
reslt_button=Button(root,text="=",bg="#5093f8",command=reslt)
reslt_button.place(x=278,y=264,width=120,height=35)
#------
one_button=Button(root,text="1",bg="#5093f8",command=one)
one_button.place(x=2,y=227,width=90,height=35)
two_button=Button(root,text="2",bg="#5093f8",command=two)
two_button.place(x=94,y=227,width=90,height=35)
three_button=Button(root,text="3",bg="#5093f8",command=three)
three_button.place(x=186,y=227,width=90,height=35)
add_button=Button(root,text="+",bg="#5093f8",command=add)
add_button.place(x=278,y=227,width=120,height=35)
#-------
four_button=Button(root,text="4",bg="#5093f8",command=four)
four_button.place(x=2,y=190,width=90,height=35)
five_button=Button(root,text="5",bg="#5093f8",command=five)
five_button.place(x=94,y=190,width=90,height=35)
six_button=Button(root,text="6",bg="#5093f8",command=six)
six_button.place(x=186,y=190,width=90,height=35)
moin_button=Button(root,text="-",bg="#5093f8",command=moin)
moin_button.place(x=278,y=190,width=120,height=35)
#-------
seven_button=Button(root,text="7",bg="#5093f8",command=seven)
seven_button.place(x=2,y=153,width=90,height=35)
eight_button=Button(root,text="8",bg="#5093f8",command=eight)
eight_button.place(x=94,y=153,width=90,height=35)
nine_button=Button(root,text="9",bg="#5093f8",command=nine)
nine_button.place(x=186,y=153,width=90,height=35)
div_button=Button(root,text="//",bg="#5093f8",command=div)
div_button.place(x=278,y=153,width=120,height=35)
#-------
puis_button=Button(root,text="X²",bg="#5093f8",command=puis)
puis_button.place(x=2,y=116,width=90,height=35)
fnc_button=Button(root,text="1/x",bg="#5093f8",command=fnc)
fnc_button.place(x=94,y=116,width=90,height=35)
racine_button=Button(root,text="√x",bg="#5093f8",command=sqr)
racine_button.place(x=186,y=116,width=90,height=35)
multp_button=Button(root,text="*",bg="#5093f8",command=multp)
multp_button.place(x=278,y=116,width=120,height=35)
#-------
mod_button=Button(root,text="%",bg="#5093f8",command=mod)
mod_button.place(x=2,y=79,width=90,height=35)
supall_button=Button(root,text="CE",bg="#5093f8",command=supall)
supall_button.place(x=94,y=79,width=90,height=35)
sup_button=Button(root,text="C",bg="#5093f8",command=sup)
sup_button.place(x=186,y=79,width=90,height=35)
del_button=Button(root,text="⌫",bg="#5093f8",command=dell)
del_button.place(x=278,y=79,width=120,height=35)
# add menu
menu_bar=Menu(root)
#File Menu
file=Menu(menu_bar,tearoff=0)
file.add_command(label="Clear ",command=sup)
file.add_command(label="Exit ", command=root.quit)
menu_bar.add_cascade(label="File",menu=file)
#custimize
menu=Menu(menu_bar,tearoff=0)
menu.add_command(label="Changer La couleur de la background(yellow)",command=bg)
menu_bar.add_cascade(label="Menu",menu=menu)


root.config(menu=menu_bar)


root.mainloop()
