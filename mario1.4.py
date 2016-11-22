import threading
from tkinter import *
import random
from time import sleep
import os

v=Tk()
v.title("Mario")
can = Canvas(v,width=1600,height=720)
can.focus_set()
can.config(bg="black")
can.pack()

go=PhotoImage(file="go.png")
mapaI = PhotoImage(file="mapaf.png")

#menu
menu1I = PhotoImage(file="menu1.png")
menu2I = PhotoImage(file="menu2.png")
playI = PhotoImage(file="play.png")
opcI = PhotoImage(file="opciones.png")

#mario
m0= PhotoImage(file="m00.png")
m1= PhotoImage(file="m0.png")
m2= PhotoImage(file="m1.png")
m3 = PhotoImage(file="m2.png")
m4= PhotoImage(file="m3.png")
m5= PhotoImage(file="m33.png")
m6 = PhotoImage(file="m6.png")
m7 = PhotoImage(file="m7.png")

#sonic
s0= PhotoImage(file="s0.png")
s1= PhotoImage(file="s1.png")
s2= PhotoImage(file="s2.png")
s3 = PhotoImage(file="s3.png")
s4= PhotoImage(file="s4.png")
s5= PhotoImage(file="s5.png")
s6 = PhotoImage(file="s6.png")
s7 = PhotoImage(file="s7.png")

#Pow
po1=PhotoImage(file="p1.png")
po2=PhotoImage(file="p2.png")
po3=PhotoImage(file="p3.png")

#vidas
vm=PhotoImage(file="vm.png")
pvm=110
vs=PhotoImage(file="vs.png")
pvs=430

#enemigos
#enemigo1:
ec0=PhotoImage(file="EC0.png")
ec1=PhotoImage(file="EC1.png")
ec2=PhotoImage(file="EC2.png")
ec3=PhotoImage(file="EC3.png")
ec4=PhotoImage(file="EC4.png")
#enemigo2:
et0=PhotoImage(file="et0.png")
et1=PhotoImage(file="et1.png")
et2=PhotoImage(file="et2.png")
et3=PhotoImage(file="et3.png")
et4=PhotoImage(file="et4.png")
et5=PhotoImage(file="et5.png")
#enemigo3
ed0=PhotoImage(file="ed0.png")
ed1=PhotoImage(file="ed1.png")
ed2=PhotoImage(file="ed2.png")
ed3=PhotoImage(file="ed3.png")
ed4=PhotoImage(file="ed4.png")
ed5=PhotoImage(file="ed5.png")



est = 3
est2=2
#juego
mx = 100
my = 425
mar=0

sx=400
sy=425
soc=0

ya = False
st=False

ya2=False
ys2=0
st2=False

ys = 0
E=[]
def Menu():
    global v,can,menu1I,menu2I,x1,x2,menu1,menu2,botoJ,botoO
    menu1.destroy()
    menu2.destroy()
    x1 += 10
    x2 -= 10
    menu1= Label(can,image=menu1I)
    menu1.place(x=x1,y=0)
    menu2= Label(can,image=menu2I)
    menu2.place(x=x2,y=0)
    if(x1<0):
        v.after(5,Menu)
    else:
        botoJ = Button(can,command=Level,image=playI)
        botoJ.place(x=570,y=300)
        botoO = Button(can, command=Play,image=opcI)
        botoO.place(x=570,y=450)


def Level():
    global v,can,f
    a=[]
    for i in range(0,5):
        a.append([])
        a[i].append(570)
        a[i].append(300)
        a[i].append(Button(can,text="Nivel 1",bg="black",fg="white",font=100,height=3,width=20))
        a[i][2].place(x=570,y=300)
        t="Nivel " + str(i+1)
        for x in range(20):
            a[i][0]+=25-((i-2)**2)
            a[i][1]-=15-((i+1)*6)
            a[i][2].destroy()
            a[i][2]=Button(can,text=t,bg="black",fg="white",font=100,height=3,width=20)
            a[i][2].place(x=a[i][0],y=a[i][1])
            v.update()
            v.after(8)
    a.append([])
    a[5].append(570)
    a[5].append(300)
    a[5].append(Button(can,text="Nivel 1",bg="black",fg="white",font=100,height=3,width=20))
    a[5][2].place(x=570,y=300)
    for t in range(30):
        a[5][0]-=15
        a[5][2].destroy()
        a[5][2]=Button(can,text="Nivel Infinito",bg="blue",fg="white",font=100,height=5,width=30)
        a[5][2].place(x=a[5][0],y=a[5][1])
        v.update()
        v.after(8)
        
    a[0][2].destroy()
    a[0][2]=Button(can,command=nivel1,text="Nivel 1",bg="black",fg="white",font=100,height=3,width=20)
    a[0][2].place(x=a[0][0],y=a[0][1])
    a[1][2].destroy()
    a[1][2]=Button(can,command=nivel2,text="Nivel 2",bg="black",fg="white",font=100,height=3,width=20)
    a[1][2].place(x=a[1][0],y=a[1][1])
    a[2][2].destroy()
    a[2][2]=Button(can,command=nivel3,text="Nivel 3",bg="black",fg="white",font=100,height=3,width=20)
    a[2][2].place(x=a[2][0],y=a[2][1])
    a[3][2].destroy()
    a[3][2]=Button(can,command=nivel4,text="Nivel 4",bg="black",fg="white",font=100,height=3,width=20)
    a[3][2].place(x=a[3][0],y=a[3][1])
    a[4][2].destroy()
    a[4][2]=Button(can,command=nivel5,text="Nivel 5",bg="black",fg="white",font=100,height=3,width=20)
    a[4][2].place(x=a[4][0],y=a[4][1])
    a[5][2].destroy()
    a[5][2]=Button(can,command=nivel6,text="Nivel Infinito",bg="blue",fg="white",font=100,height=5,width=30)
    a[5][2].place(x=a[5][0],y=a[5][1])
def nivel1():
    global v,can,dif,difr,difc,EN,nv,ron,ronf
    nv=1
    ron=0
    ronf=15
    dif=5
    difr=300
    EN=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2]
    lab=Label(can,text="Nv 1",bg="black",fg="red",font=30).place(x=220,y=50)
    Play()
    
def nivel2():
    global v,can,dif,difr,difc,EN,nv,ron,ronf
    ron=5
    ronf=20
    nv=2
    dif=5
    difr=250
    EN=[1,1,1,1,1,1,1,1,1,2,2,2,2,3]
    lab=Label(can,text="Nv 2",bg="black",fg="red",font=30).place(x=220,y=50)
    Play()
    
def nivel3():
    global v,can,dif,difr,difc,EN,nv,ron,ronf
    ron=10
    ronf=25
    nv=3
    dif=5
    difr=200
    EN=[1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3]
    lab=Label(can,text="Nv 3",bg="black",fg="red",font=30).place(x=220,y=50)
    Play()

def nivel4():
    global v,can,dif,difr,difc,EN,nv,ron,ronf
    ron=15
    ronf=30
    nv=4
    dif=7
    difr=200
    EN=[1,1,1,2,2,2,2,3]
    lab=Label(can,text="Nv 4",bg="black",fg="red",font=30).place(x=220,y=50)
    Play()
    
def nivel5():
    global v,can,dif,difr,difc,EN,nv,ron,ronf
    ron=20
    ronf=40
    nv=5
    dif=8
    difr=150
    EN=[2,2,2,3]
    lab=Label(can,text="Nv 5",bg="black",fg="red",font=30).place(x=220,y=50)
    Play()

def nivel6():
    global v,can,dif,difr,difc,EN,nv,ron,ronf
    ron=0
    ronf=-1
    nv=6
    dif=5
    difr=200
    EN=[1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3]
    lab=Label(can,text="Nv X",bg="black",fg="red",font=30).place(x=220,y=50)
    Play()

    
def Play():
    global v,can,menu1I,menu2I,M,mar,E,soc,puntos,puntom,puntot,po,VM,VS,dif,difr,difc
    mapa = Label(can,image=mapaI,bg="black")
    mapa.pack()
    mar=Label(can,image=m3,bg="black")
    mar.place(x=100,y=425)
    soc=Label(can,image=s2,bg="black")
    soc.place(x=400,y=425)
    #Puntaje
    Label(can,text="M =",bg="black",fg="red",font=30).place(x=40,y=20)
    Label(can,text="S =",bg="black",fg="blue",font=30).place(x=370,y=20)
    Label(can,text="TOP =",bg="black",fg="green",font=30).place(x=200,y=20)

    puntom=Label(can,text=pm,bg="black",fg="white",font=30)
    puntom.place(x=80,y=20)
    
    puntos=Label(can,text=ps,bg="black",fg="white",font=30)
    puntos.place(x=410,y=20)
    
    top=max(pm,ps)
    puntot=Label(can,text=top,bg="black",fg="white",font=30)
    puntot.place(x=260,y=20)
    puntaje()
    #
    po=Label(can,image=po3,bg="black")
    po.place(x=270,y=280)
    #
    #vidas
    VM=[]
    VM.append(Label(can,image=vm,bg="black"))
    VM[0].place(x=20,y=50)
    VM.append(Label(can,image=vm,bg="black"))
    VM[1].place(x=50,y=50)
    VM.append(Label(can,image=vm,bg="black"))
    VM[2].place(x=80,y=50)
    VS=[]
    VS.append(Label(can,image=vs,bg="black"))
    VS[0].place(x=520,y=50)
    VS.append(Label(can,image=vs,bg="black"))
    VS[1].place(x=490,y=50)
    VS.append(Label(can,image=vs,bg="black"))
    VS[2].place(x=460,y=50)
    #funciones:
    ronda()
    Enemigos()
    Caida()
    Caida2()
    parado()
    parado2()
    key()
    key2()
    
def salto():
    global v,can,M,mar,mx,my,est,ya,st,ys,est
    v1 = ( (ys <= 130 and st== False) and ((my>=425-35 or (mx>=200 and mx<=330 and my>=285)or(my<=315 and my>= 285)or (mx>=50 and mx<=115 and my>=150 and my<=315)or(my<=315 and my>=100 and mx>=415 and mx<=470)or(my>=180 and my<=205)or(my<=100 and my >=0)or(my<=205 and my >=0 and mx>=230 and mx<=290))))
    v2 = ((my<=425 and my!=315 and my != 205 and my!=100)or(my<=315 and my > 205 and (mx>=200 and mx<=330))or(my<=205 and (mx>=50 and mx<=115)and my>=115)or(my<=205 and (mx>=415 and mx<=470)and my>=115)or(my<=205 and (mx>=230 and mx<=290)or(my<=100 and my>=0 )))
    if(est==1 or est==0):
        mar.destroy()
        if(v1):
            my-=5
            mx-=3
            ys+=5
        else:
            if(v2):
                my+=5
            mx-=3
            ys-=5
            st= True
        mar=Label(can,image=m6,bg="black")
        mar.place(x=mx,y=my) 
        
        
    elif(est== 2):
        mar.destroy()
        if( v1):
            my-=5
            ys+=5
        else:
            if(v2):
                my+=5
            ys-=5
            st= True
        mar=Label(can,image=m6,bg="black")
        mar.place(x=mx,y=my) 
        
    elif(est== 3):
        mar.destroy()
        if( v1):
            my-=5
            ys+=5
        else:
            if(v2):
                my+=5
            ys-=5
            st= True
        mar=Label(can,image=m7,bg="black")
        mar.place(x=mx,y=my)
        
    elif(est==4 or est==5):
        mar.destroy()
        if( v1):
            my-=5
            mx+=3
            ys+=5
        else:
            if(v2):
                my+=5
            mx+=3
            ys-=5
            st= True
        mar=Label(can,image=m7,bg="black")
        mar.place(x=mx,y=my)
        
    if(my<=310 and my>=280 and mx <=300 and mx >= 240 and spow > 0):
        sppow()

    if(ya == True and ys>0 and (my != 315 or (mx>=200 and mx<=330 and my >= 275))and(my != 205 or ((mx>=50 and mx<=115 and my>=100 and my<= 205)or(mx>=415 and mx<=470 and my>=100 and my<= 205)))and(my != 100 or (mx>=230 and mx<=290 and my >= 0 and my <= 100))):
        v.after(10,salto)
    else:
        ya=False
        st=False
        ys= 0
        if(est==0 or est ==1 or est == 2):
            mar.destroy()
            mar=Label(can,image=m2,bg="black")
            mar.place(x=mx,y=my)
            est=2
        elif(est == 3 or est == 4 or est == 5):
            mar.destroy()
            mar=Label(can,image=m3,bg="black")
            mar.place(x=mx,y=my)
            est=3


def salto2():
    global v,can,M,soc,sx,sy,est2,ya2,st2,ys2,est2,spow
    v1 = ( (ys2 <= 130 and st2== False) and ((sy>=425-35 or (sx>=200 and sx<=330 and sy>=285)or(sy<=315 and sy>= 285)or (sx>=50 and sx<=115 and sy>=150 and sy<=315)or(sy<=315 and sy>=100 and sx>=415 and sx<=470)or(sy>=180 and sy<=205)or(sy<=100 and sy >=0)or(sy<=205 and sy >=0 and sx>=230 and sx<=290))))
    v2 = ((sy<=425 and sy!=315 and sy != 205 and sy!=100)or(sy<=315 and sy > 205 and (sx>=200 and sx<=330))or(sy<=205 and (sx>=50 and sx<=115)and sy>=115)or(sy<=205 and (sx>=415 and sx<=470)and sy>=115)or(sy<=205 and (sx>=230 and sx<=290)or(sy<=100 and sy>=0 )))
    if(est2==1 or est2==0):
        soc.destroy()
        if(v1):
            sy-=5
            sx-=3
            ys2+=5
        else:
            if(v2):
                sy+=5
            sx-=3
            ys2-=5
            st2= True
        soc=Label(can,image=s6,bg="black")
        soc.place(x=sx,y=sy) 
        
        
    elif(est2== 2):
        soc.destroy()
        if( v1):
            sy-=5
            ys2+=5
        else:
            if(v2):
                sy+=5
            ys2-=5
            st2= True
        soc=Label(can,image=s6,bg="black")
        soc.place(x=sx,y=sy) 
        
    elif(est2== 3):
        soc.destroy()
        if( v1):
            sy-=5
            ys2+=5
        else:
            if(v2):
                sy+=5
            ys2-=5
            st2= True
        soc=Label(can,image=s7,bg="black")
        soc.place(x=sx,y=sy)
        
    elif(est2==4 or est2==5):
        soc.destroy()
        if( v1):
            sy-=5
            sx+=3
            ys2+=5
        else:
            if(v2):
                sy+=5
            sx+=3
            ys2-=5
            st2= True
        soc=Label(can,image=s7,bg="black")
        soc.place(x=sx,y=sy) 

    if(sy<=310 and sy>=280 and sx <=300 and sx >= 240 and spow > 0):
        sppow()
    
    if(ya2 == True and ys2>0 and (sy != 315 or (sx>=200 and sx<=330 and sy >= 275))and(sy != 205 or ((sx>=50 and sx<=115 and sy>=100 and sy<= 205)or(sx>=415 and sx<=470 and sy>=100 and sy<= 205)))and(sy != 100 or (sx>=230 and sx<=290 and sy >= 0 and sy <= 100))):
        v.after(10,salto2)
    else:
        ya2=False
        st2=False
        ys2= 0
        if(est2==0 or est2 ==1 or est2 == 2):
            soc.destroy()
            soc=Label(can,image=s2,bg="black")
            soc.place(x=sx,y=sy)
            est2=2
        elif(est == 3 or est == 4 or est == 5):
            soc.destroy()
            soc=Label(can,image=s3,bg="black")
            soc.place(x=sx,y=sy)
            est2=3
    

            
def parado():
    global v,can,M,mx,my,mar,est,ya2,est2
    if((est==1 or est == 0) and ya==False):
        mar.destroy()
        mar = Label(can,image=m2,bg="black")
        mar.place(x=mx,y=my)
        est=2
    elif((est==4 or est==5) and ya==False):
        mar.destroy()
        mar = Label(can,image=m3,bg="black")
        mar.place(x=mx,y=my)
        est=3
    v.after(800,parado)
    
def parado2():
    global v,can,M,sx,sy,soc,ya2,est2
    if((est2==1 or est2 == 0) and ya2==False):
        soc.destroy()
        soc = Label(can,image=s2,bg="black")
        soc.place(x=sx,y=sy)
        est2=2
    elif((est2==4 or est2==5) and ya2==False):
        soc.destroy()
        soc = Label(can,image=s3,bg="black")
        soc.place(x=sx,y=sy)
        est2=3
    v.after(800,parado2)

def key():
    global v,can,M,mx,my,mar,est,ya,co,ya2,sy,sx,soc,est2,K
    if(ya == False):
        if(my <= 500 and my >= 320):
            my = 425
        elif(my < 320 and my >= 210):
            my = 315
        elif(my < 210 and my >= 105):
            my = 205
        elif(my<105):
            my = 100
        
    if("'a'" in K and ((mx > 75 and my==425)or(mx>5 and my==315)or(mx>5 and my==205)or(mx>=100 and my==100)) and ya == False):
        mx -= 10
        mar.destroy()
        if(est!=0):
            mar = Label(can,image=m0,bg="black")
            mar.place(x=mx,y=my)
            est=0
        else:
            mar = Label(can,image=m1,bg="black")
            mar.place(x=mx,y=my)
            est=1
    if("'d'" in K and ((mx <450 and my==425)or(mx<500 and my==315)or(mx<500 and my==205)or (mx<=400 and my==100)) and ya == False):
        mx += 10
        mar.destroy()
        if(est!=5):
            mar = Label(can,image=m5,bg="black")
            mar.place(x=mx,y=my)
            est=5
        else:
            mar = Label(can,image=m4,bg="black")
            mar.place(x=mx,y=my)
            est=4

    if("'w'" in K and ya == False):
        ya = True
        salto()
    v.after(60,key)


def key2():
    global v,can,M,mx,my,mar,est,ya,co,ya2,sy,sx,soc,est2,K
    if(ya2 == False):
        if(sy <= 500 and sy >= 320):
            sy = 425
        elif(sy < 320 and sy >= 210):
            sy = 315
        elif(sy < 210 and sy >= 105):
            sy = 205
        elif(my<105):
            sy = 100
        
    if("'4'" in K and ((sx > 75 and sy==425)or(sx>5 and sy==315)or(sx>5 and sy==205)or(sx>=100 and sy==100)) and ya2 == False):
        sx -= 15
        soc.destroy()
        if(est2!=0):
            soc = Label(can,image=s0,bg="black")
            soc.place(x=sx,y=sy)
            est2=0
        else:
            soc = Label(can,image=s1,bg="black")
            soc.place(x=sx,y=sy)
            est2=1
    if("'6'" in K and ((sx <450 and sy==425)or(sx<500 and sy==315)or(sx<500 and sy==205)or (sx<=400 and sy==100)) and ya2 == False):
        sx += 15
        soc.destroy()
        if(est2!=5):
            soc = Label(can,image=s5,bg="black")
            soc.place(x=sx,y=sy)
            est2=5
        else:
            soc = Label(can,image=s4,bg="black")
            soc.place(x=sx,y=sy)
            est2=4

    if("'8'" in K and ya2 == False):
        ya2 = True
        salto2()
    v.after(55,key2)

    
def Caida():
    global v,can,M,mx,my,mar,est,ya
    if(ya == False and (((mx>=200 and mx<=330 and my >= 215)or(((mx>=50 and mx<=115)or(mx>=415 and mx<=475)) and (my < 315 and my >110))or(my<205 and (mx>=230 and mx<=290)))and my < 425)):
        my += 5
        mar.destroy()
        if(est ==0 or est==1 or est==2):
            mar = Label(can,image=m2,bg="black")
            mar.place(x=mx,y=my)
            v.after(20,Caida)
        else:
            mar = Label(can,image=m3,bg="black")
            mar.place(x=mx,y=my)
            v.after(20,Caida)
    else:
        if(mx <= 5):
            mx=485
        if(mx>=490):
            mx=10
        if(my<=100):
            if(mx<=105):
                mx=440
                my=425

            elif(mx>=395):
                mx=90
                my=425

        if(my<=425 and my >= 320):
            if(mx<=80):
                mx=390
                my=100

            if(mx>=445):
                mx=90
                my=100

        v.after(100,Caida)


def Caida2():
    global v,can,M,sx,sy,soc,est2,ya2
    if(ya2 == False and (((sx>=200 and sx<=330 and sy >= 215)or(((sx>=50 and sx<=115)or(sx>=415 and sx<=475)) and (sy < 315 and sy >110))or(sy<205 and (sx>=230 and sx<=290)))and sy < 425)):
        sy += 5
        soc.destroy()
        if(est2 ==0 or est2==1 or est2==2):
            soc = Label(can,image=s2,bg="black")
            soc.place(x=sx,y=sy)
            v.after(20,Caida2)
        else:
            soc = Label(can,image=s3,bg="black")
            soc.place(x=sx,y=sy)
            v.after(20,Caida2)
    else:
        if(sx <= 5):
            sx=485
        if(sx>=490):
            sx=10
        if(sy<=100):
            if(sx<=105):
                sx=440
                sy=425
            elif(sx>=395):
                sx=90
                sy=425
        if(sy<=425 and sy >= 320):
            if(sx<=80):
                sx=390
                sy=100
            if(sx>=445):
                sx=90
                sy=100
        v.after(100,Caida2)


def fin():
    global v,can
    gov=Label(can,image=go,bg="black")
    gov.pack()
    os.execl('mario.py', '')
    
def muereM():
    global v,can,M,mx,my,mar,est,ya,E,dif,h,ron,eron,vida,VM,pvm,vidaS
    ya = True
    mar.destroy()
    vida-=1
    fin()
    if(vida>=0):
        VM[vida].destroy()
        pvm-=30
        mx=400
        my=425
        mar=Label(can,image=m3,bg="black")
        mar.place(x=mx,y=my)
        ya = False
        est=8
    else:
        mx=-500
        my=-500
        if(vidaS<0):
            fin()
def muereS():
    global v,can,M,sx,sy,soc,est2,ya2,E,dif,h,ron,eron,vidaS,VS,pvs,vida
    ya2 = True
    soc.destroy()
    vidaS-=1
    if(vidaS>=0):
        VS[vidaS].destroy()
        pvs+=30
        sx=100
        sy=425
        soc=Label(can,image=s3,bg="black")
        soc.place(x=sx,y=sy)
        ya2 = False
        est2=8
    else:
        sx=-500
        sy=-500
        if(vida<0):
            fin()

def Enemigos():
    global v,can,M,mx,my,mar,est,ya,E,dif,h,ron,eron,pm,ps
    x=0
    while x < len(E):
        if(E[x][0] <= 3):
            if(E[x][0] == 2 or E[x][0] == 3):
                if(E[x][1] < 500): 
                    E[x][1]+=dif
                    if(E[x][3] == 1):
                        if(E[x][0] == 2):
                            E[x][4].destroy()
                            E[x][4]= Label(can,image=ec2,bg="black")
                            E[x][4].place(x=E[x][1],y=E[x][2])
                            E[x][0] = 3
                        elif(E[x][0] == 3):
                            E[x][4].destroy()
                            E[x][4]= Label(can,image=ec3,bg="black")
                            E[x][4].place(x=E[x][1],y=E[x][2])
                            E[x][0] = 2
                    if(E[x][3] == 2):
                        if(E[x][0] == 2):
                            E[x][4].destroy()
                            E[x][4]= Label(can,image=et2,bg="black")
                            E[x][4].place(x=E[x][1],y=E[x][2])
                            E[x][0] = 3
                        elif(E[x][0] == 3):
                            E[x][4].destroy()
                            E[x][4]= Label(can,image=et3,bg="black")
                            E[x][4].place(x=E[x][1],y=E[x][2])
                            E[x][0] = 2
                    if(E[x][3] == 3):
                        E[x][1]+=dif*E[x][5]
                        if(E[x][0] == 2):
                            E[x][4].destroy()
                            E[x][4]= Label(can,image=ed2,bg="black")
                            E[x][4].place(x=E[x][1],y=E[x][2])
                            E[x][0] = 3
                        elif(E[x][0] == 3):
                            E[x][4].destroy()
                            E[x][4]= Label(can,image=ed3,bg="black")
                            E[x][4].place(x=E[x][1],y=E[x][2])
                            E[x][0] = 2
                else:
                    E[x][1]=5
                 
            elif(E[x][0] == 0 or E[x][0] == 1):
                if(E[x][1] > 5): 
                    E[x][1]-=dif
                    if(E[x][3]==1):
                        if(E[x][0] == 0):
                            E[x][4].destroy()
                            E[x][4]= Label(can,image=ec0,bg="black")
                            E[x][4].place(x=E[x][1],y=E[x][2])
                            E[x][0] = 1
                        elif(E[x][0] == 1):
                            E[x][4].destroy()
                            E[x][4]= Label(can,image=ec1,bg="black")
                            E[x][4].place(x=E[x][1],y=E[x][2])
                            E[x][0] = 0
                            
                    if(E[x][3]==2):
                        if(E[x][0] == 0):
                            E[x][4].destroy()
                            E[x][4]= Label(can,image=et0,bg="black")
                            E[x][4].place(x=E[x][1],y=E[x][2])
                            E[x][0] = 1
                        elif(E[x][0] == 1):
                            E[x][4].destroy()
                            E[x][4]= Label(can,image=et1,bg="black")
                            E[x][4].place(x=E[x][1],y=E[x][2])
                            E[x][0] = 0
                    if(E[x][3]==3):
                        E[x][1]-=dif*E[x][5]
                        if(E[x][0] == 0):
                            E[x][4].destroy()
                            E[x][4]= Label(can,image=ed0,bg="black")
                            E[x][4].place(x=E[x][1],y=E[x][2])
                            E[x][0] = 1
                        elif(E[x][0] == 1):
                            E[x][4].destroy()
                            E[x][4]= Label(can,image=ed1,bg="black")
                            E[x][4].place(x=E[x][1],y=E[x][2])
                            E[x][0] = 0
                else:
                    E[x][1]= 500

            #Caida:
            if(E[x][3] <= 2):
                if(E[x][2]>=116 and E[x][1] >=230 and E[x][1] <= 290 and E[x][2] < 221 ):
                        E[x][2]+=min(221-E[x][2],50)
                if((E[x][2]>=221 and E[x][2] < 332)and((E[x][1] >=415 and E[x][1] <= 475)or(E[x][1] >=50 and E[x][1] <= 115))  ):
                        E[x][2]+=min(332-E[x][2],50)
                if(E[x][2]>=332 and E[x][1] >=200 and E[x][1] <= 330 and E[x][2] < 441 ):
                        E[x][2]+=min(441-E[x][2],50)
                        
            if(E[x][3] == 3):
                if(E[x][2]>=100 and E[x][1] >=230 and E[x][1] <= 290 and E[x][2] < 205 ):
                        E[x][2]+=min(205-E[x][2],80)
                if((E[x][2]>=205 and E[x][2] < 316)and((E[x][1] >=415 and E[x][1] <= 475)or(E[x][1] >=50 and E[x][1] <= 115))  ):
                        E[x][2]+=min(316-E[x][2],80)
                if(E[x][2]>=316 and E[x][1] >=200 and E[x][1] <= 330 and E[x][2] < 425 ):
                        E[x][2]+=min(425-E[x][2],80)
        
            #Mundo continuo
            if(E[x][3]<=2):
                if(E[x][2]<=116):
                    if(E[x][1]<80):
                        E[x][1]=450
                        E[x][2]=441
                    elif(E[x][1]>450):
                        E[x][1]=80
                        E[x][2]=441
                if(E[x][2]<=441 and E[x][2] >= 340):
                    if(E[x][1]<80):
                        pm=max(0,pm-20)
                        ps=max(0,ps-20)
                        E[x][1]=450
                        E[x][2]=116
                        puntaje()
                    if(E[x][1]>450):
                        pm=max(0,pm-20)
                        ps=max(0,ps-20)
                        puntaje()
                        E[x][1]=80
                        E[x][2]=116
                        
            if(E[x][3]==3):
                if(E[x][2]<=100):
                    if(E[x][1]<80):
                        E[x][1]=450
                        E[x][2]=425
                    elif(E[x][1]>450):
                        E[x][1]=80
                        E[x][2]=425
                if(E[x][2]<=425 and E[x][2] >= 326):
                    if(E[x][1]<80):
                        pm=max(0,pm-20)
                        ps=max(0,ps-20)
                        E[x][1]=450
                        E[x][2]=100
                        puntaje()
                    if(E[x][1]>450):
                        pm=max(0,pm-20)
                        ps=max(0,ps-20)
                        puntaje()
                        E[x][1]=80
                        E[x][2]=100
                        
            # Matar enemigos
            if(E[x][3]<=2):
                if(E[x][2] + 70 >= my and E[x][2] + 30 <= my and E[x][1] <= mx + 50 and E[x][1] + 50 >= mx and ya == True):
                    if(E[x][3]==1):
                        E[x][0] = 5
                        pm += 10
                        puntaje()
                    if(E[x][3]==2):
                        E[x][0]=200
                        E[x][4].destroy()
                        E[x][4]= Label(can,image=et4,bg="black")
                        E[x][4].place(x=E[x][1],y=E[x][2])
                elif(E[x][2] + 70 >= sy and E[x][2] + 30 <= sy and E[x][1] <= sx + 50 and E[x][1] + 50 >= sx and ya2 == True):
                    if(E[x][3]==1):
                        E[x][0] = 5
                        pm += 10
                        puntaje()
                    elif(E[x][3]==2):
                        E[x][0]=200
                        E[x][4].destroy()
                        E[x][4]= Label(can,image=et4,bg="black")
                        E[x][4].place(x=E[x][1],y=E[x][2])

            if(E[x][3]==3):
                if(E[x][2] + 90 >= my and E[x][2] + 50 <= my and E[x][1] <= mx + 50 and E[x][1] + 50 >= mx and ya == True):
                    if(E[x][5]<3):
                        E[x][5]+=1
                        E[x][0]=15
                        E[x][4].destroy()
                        E[x][4]=Label(can,image=ed4,bg="black")
                        E[x][4].place(x=E[x][1],y=E[x][2])
                    else:
                        E[x][5]=0
                        E[x][0]=4
                        E[x][4].destroy()
                        E[x][4]=Label(can,image=ed5,bg="black")
                        E[x][4].place(x=E[x][1],y=E[x][2])
                        E[x].append(10)
                        E[x].append(Label(can,text="25",bg="black",fg="yellow",font=2))
                        E[x][7].place(x=E[x][1]+40,y=E[x][2]-50)
                        pm+=25
                        puntaje()
                        
                elif(E[x][2] + 90 >= sy and E[x][2] + 50 <= sy and E[x][1] <= sx + 50 and E[x][1] + 50 >= sx and ya2 == True):
                    if(E[x][5]<3):
                        E[x][5]+=1
                        E[x][0]=15
                        E[x][4].destroy()
                        E[x][4]=Label(can,image=ed4,bg="black")
                        E[x][4].place(x=E[x][1],y=E[x][2])
                    else:
                        E[x][5]=0
                        E[x][0]=4
                        E[x][4].destroy()
                        E[x][4]=Label(can,image=ed5,bg="black")
                        E[x][4].place(x=E[x][1],y=E[x][2])
                        E[x].append(10)
                        E[x].append(Label(can,text="25",bg="black",fg="yellow",font=2))
                        E[x][7].place(x=E[x][1]+40,y=E[x][2]-50)
                        pm+=25
                        puntaje()

                        
            if(E[x][0]==5 and E[x][3]==1):
                E[x][4].destroy()
                E[x][4]= Label(can,image=ec4,bg="black")
                E[x][4].place(x=E[x][1],y=E[x][2])
                E[x].append(Label(can,text="10",bg="black",fg="yellow",font=2))
                E[x][5].place(x=E[x][1]+20,y=E[x][2]-30)
                E[x][0] = 6
                            
            #matar jugador mario
            if(E[x][2] <= my + 50 and E[x][2] + 30 >= my and E[x][1] <= mx + 30 and E[x][1] + 30 >= mx ):
                muereM()
            #matar jugador sonic
            if(E[x][2] <= sy + 50 and E[x][2] + 30 >= sy and E[x][1] <= sx + 30 and E[x][1] + 30 >= sx):
                muereS()
        
        if(E[x][0] > 6 and E[x][3]==2):
            if(E[x][2] <= my + 50 and E[x][2] + 30 >= my and E[x][1] <= mx + 30 and E[x][1] + 30 >= mx ):
                E[x][0]=5
                E[x].append(Label(can,text="15",bg="black",fg="yellow",font=2))
                E[x][5].place(x=E[x][1]+20,y=E[x][2]-30)
                E[x].append(30)
                if(est<=1):
                    E[x].append(1)
                else:
                    E[x].append(-1)
                pm+=15
                puntaje()

            elif(E[x][2] <= sy + 50 and E[x][2] + 30 >= sy and E[x][1] <= sx + 30 and E[x][1] + 30 >= sx):
                E[x][0]=5
                E[x].append(Label(can,text="15",bg="black",fg="yellow",font=2))
                E[x][5].place(x=E[x][1]+20,y=E[x][2]-30)
                E[x].append(15)
                if(est2<=1):
                    E[x].append(1)
                else:
                    E[x].append(-1)
                ps+=15
                puntaje()
            else:
                E[x][0] -= 2

        if(E[x][0] >= 4 and E[x][3]==3):
            if(E[x][5]>0):
                E[x][0]-=1
                if(E[x][0]==3):
                    E[x][0]=random.randint(2,3)
            else:
                E[x][6]-=1
                if(E[x][6] <= 0):
                    E[x][4].destroy()
                    E[x][7].destroy()
                    if(eron<(3+ron)):
                        eron+=1
                        creacion(x)

                    
        if(E[x][0]==5 and E[x][3]==2):
            E[x][6]-=1
            E[x][1]-=15*E[x][7]
            E[x][4].destroy()
            E[x][4]= Label(can,image=et5,bg="black")
            E[x][4].place(x=E[x][1],y=E[x][2]+16)
            if(E[x][6]<=0):
                E[x][5].destroy()
                E[x][4].destroy()
                if(eron<(3+ron)):
                    eron+=1
                    creacion(x)
                    
        if(E[x][0] == 6):
            if(E[x][3]==1):
                h+=1
                if(h >= 10):
                    h=0
                    E[x][5].destroy()
                    E[x][4].destroy()
                    if(eron<(3+ron)):
                        eron+=1
                        creacion(x)
            if(E[x][3]==2):
                E[x][0]=random.randint(1,2)
        x+=1
    v.after(100,Enemigos)#80

def creacion(r=-1):
    global E,can,EN
    ar = random.randint(1,2)
    tp = random.sample(EN,  1)
    if(r==-1):
        if(ar==1):
            if(tp[0]==1):
                E.append([2,80,116,1])
                E[len(E)-1].append(Label(can,image=ec2,bg="black"))
                E[len(E)-1][4].place(x=E[len(E)-1][1],y=E[len(E)-1][2])
            elif(tp[0]==2):
                E.append([2,80,116,2])
                E[len(E)-1].append(Label(can,image=et2,bg="black"))
                E[len(E)-1][4].place(x=E[len(E)-1][1],y=E[len(E)-1][2])
            elif(tp[0]==3):
                E.append([2,80,100,3])
                E[len(E)-1].append(Label(can,image=ed2,bg="black"))
                E[len(E)-1][4].place(x=E[len(E)-1][1],y=E[len(E)-1][2])
                E[len(E)-1].append(1)
        else:
            if(tp[0]==1):
                E.append([0,450,116,1])
                E[len(E)-1].append(Label(can,image=ec0,bg="black"))
                E[len(E)-1][4].place(x=E[len(E)-1][1],y=E[len(E)-1][2])
            elif(tp[0]==2):
                E.append([0,450,116,2])
                E[len(E)-1].append(Label(can,image=et0,bg="black"))
                E[len(E)-1][4].place(x=E[len(E)-1][1],y=E[len(E)-1][2])
            elif(tp[0]==3):
                E.append([0,450,100,3])
                E[len(E)-1].append(Label(can,image=ed0,bg="black"))
                E[len(E)-1][4].place(x=E[len(E)-1][1],y=E[len(E)-1][2])
                E[len(E)-1].append(1)
    if(r!=-1):
        if(ar==1):
            if(tp[0]==1):
                E[r]=[2,80,116,1]
                E[r].append(Label(can,image=ec2,bg="black"))
                E[r][4].place(x=E[r][1],y=E[r][2])
            elif(tp[0]==2):
                E[r]=[2,80,116,2]
                E[r].append(Label(can,image=et2,bg="black"))
                E[r][4].place(x=E[r][1],y=E[r][2])
            if(tp[0]==3):
                E[r]=[2,80,100,3]
                E[r].append(Label(can,image=ed2,bg="black"))
                E[r][4].place(x=E[r][1],y=E[r][2])
                E[r].append(1)
        else:
            if(tp[0]==1):
                E[r]=[0,450,116,1]
                E[r].append(Label(can,image=ec0,bg="black"))
                E[r][4].place(x=E[r][1],y=E[r][2])
            elif(tp[0]==2):
                E[r]=[0,450,116,2]
                E[r].append(Label(can,image=et0,bg="black"))
                E[r][4].place(x=E[r][1],y=E[r][2])
            if(tp[0]==3):
                E[r]=[0,450,100,3]
                E[r].append(Label(can,image=ed0,bg="black"))
                E[r][4].place(x=E[r][1],y=E[r][2])
                E[r].append(1)
spow = 3
tpow=10

def sppow():
    global E,mar,soc,pm,ps,spow,po,tpow
    if(tpow<=0):
        for x in range(len(E)):
            if(E[x][0] <= 3):
                if(E[x][3]==1):
                    E[x][4].destroy()
                    E[x][4]= Label(can,image=ec4,bg="black")
                    E[x][4].place(x=E[x][1],y=E[x][2])
                    E[x].append(Label(can,text="10",bg="black",fg="yellow",font=2))
                    pm+=5
                    ps+=5
                    E[x][5].place(x=E[x][1]+20,y=E[x][2]-30)
                    E[x][0] = 6
                if(E[x][3]==2):
                    E[x][0]=200
                    E[x][4].destroy()
                    E[x][4]= Label(can,image=et4,bg="black")
                    E[x][4].place(x=E[x][1],y=E[x][2])
                if(E[x][3]==3):
                    if(E[x][5]<3):
                        E[x][5]+=1
                        E[x][0]=15
                        E[x][4].destroy()
                        E[x][4]=Label(can,image=ed4,bg="black")
                        E[x][4].place(x=E[x][1],y=E[x][2])
                    else:
                        E[x][5]=0
                        E[x][0]=4
                        E[x][4].destroy()
                        E[x][4]=Label(can,image=ed5,bg="black")
                        E[x][4].place(x=E[x][1],y=E[x][2])
                        E[x].append(10)
                        E[x].append(Label(can,text="25",bg="black",fg="yellow",font=2))
                        pm+=15
                        ps+=15
        spow-=1
        po.destroy()
        if(spow==2):
            po=Label(can,image=po2,bg="black")
            po.place(x=270,y=280)
        if(spow==1):
            po=Label(can,image=po1,bg="black")
            po.place(x=270,y=280)
        tpow=10
        puntaje()
        
d=0
def ronda():
    global ron,eron,v,tpow,time,VM,VS,vida,vidaS,pvs,pvm,d,spow,po
    if(time>=difr):
        if(eron < 3+(ron*difc)):
            eron+=1
            creacion()
            time=0
    if(eron>=3+(ron*difc)):
        ron+=1
        eron=0
        print(ron+1)
    time+=1
    tpow-=1
    if(ron%10 == 0 and d< ron/10):
        d+=1
        if(vida >0):
            vida += 1
            if(len(VM)<vida):
                VM.append(Label(can,image=vm,bg="black"))
            else:
                VM[vida-1]=(Label(can,image=vm,bg="black"))
            VM[vida-1].place(x=pvm,y=50)
            pvm+=30
        if(vidaS>0):
            vidaS += 1
            if(len(VS)<vidaS):
                VS.append(Label(can,image=vs,bg="black"))
            else:
                VS[vidaS-1]=(Label(can,image=vs,bg="black"))
            VS[vidaS-1].place(x=pvs,y=50)
            pvs-=30
        if(spow>0):
            po.destroy()
        po=Label(can,image=po3,bg="black")
        po.place(x=270,y=280)
        spow=3
    v.after(100,ronda)



def key3(event):
    global K,O
    tecla = repr(event.char)
    if(not(tecla in K)and tecla in O):
        K.append(tecla)
def key4(event):
    global K,O
    tecla = repr(event.char)
    if((tecla in K)and tecla in O):
        K.remove(tecla)

        
def puntaje():
    global pm,ps,puntos,puntom,puntot
    puntom.destroy()
    puntom=Label(can,text=pm,bg="black",fg="white",font=30)
    puntom.place(x=80,y=20)
    puntos.destroy()
    puntos=Label(can,text=ps,bg="black",fg="white",font=30)
    puntos.place(x=410,y=20)
    top=max(pm,ps)
    puntot.destroy()
    puntot=Label(can,text=top,bg="black",fg="white",font=30)
    puntot.place(x=260,y=20)
    

    


pm=0
ps=0

K=[]
O=["'d'","'a'","'w'","'6'","'8'","'4'"]
                      
time=180
vida = 3
vidaS=3
ron = 0
eron=0
h=0

EN=[1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3]#Probabilidad enemigos

dif=5 #velocidad enemigos
difr=200 #velocidad aparicion
difc=0 #cantidad de enemigos ronda

x1 = -1020
x2 = 1740
menu1= Label(can,image=menu1I)
menu1.place(x=x1,y=0)
menu2= Label(can,image=menu2I)
menu2.place(x=x2,y=0)
botoJ=0
botoO=0

Menu()


can.bind("<Key>",key3)
can.bind("<KeyRelease>",key4)


v.mainloop()


