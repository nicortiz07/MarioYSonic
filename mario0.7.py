import threading
from tkinter import *
import random
from time import sleep

v=Tk()
v.title("Mario")
can = Canvas(v,width=1600,height=720)
can.focus_set()
can.config(bg="black")
can.pack()


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

#borrar
##M=[0,0,0,0,0,0,0,0]
##M[0]=Label(can,image=m0,bg="black")
##M[1]=Label(can,image=m1,bg="black")
##M[2]=Label(can,image=m2,bg="black")
##M[3]=Label(can,image=m3,bg="black")
##M[4]=Label(can,image=m4,bg="black")
##M[5]=Label(can,image=m5,bg="black")
##M[6]=Label(can,image=m6,bg="black")
##M[7]=Label(can,image=m7,bg="black")

#enemigos
#enemigo1:
ec0=PhotoImage(file="EC0.png")
ec1=PhotoImage(file="EC1.png")
ec2=PhotoImage(file="EC2.png")
ec3=PhotoImage(file="EC3.png")
ec4=PhotoImage(file="EC4.png")


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
        v.after(2,Menu)
    else:
        botoJ = Button(can,command=Play,image=playI)
        botoJ.place(x=570,y=300)
        botoO = Button(can, command=Play,image=opcI)
        botoO.place(x=570,y=450)


def Play():
    global v,can,menu1I,menu2I,M,mar,E,soc
    mapa = Label(can,image=mapaI)
    mapa.pack()
    mar=Label(can,image=m3,bg="black")
    mar.place(x=100,y=425)
    soc=Label(can,image=s2,bg="black")
    soc.place(x=400,y=425)
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
        else:
            mar.destroy()
            mar=Label(can,image=m3,bg="black")
            mar.place(x=mx,y=my)
            est=3


def salto2():
    global v,can,M,soc,sx,sy,est2,ya2,st,ys2,est2
    v1 = ( (ys2 <= 130 and st== False) and ((sy>=425-35 or (sx>=200 and sx<=330 and sy>=285)or(sy<=315 and sy>= 285)or (sx>=50 and sx<=115 and sy>=150 and sy<=315)or(sy<=315 and sy>=100 and sx>=415 and sx<=470)or(sy>=180 and sy<=205)or(sy<=100 and sy >=0)or(sy<=205 and sy >=0 and sx>=230 and sx<=290))))
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
            st= True
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
            st= True
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
            st= True
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
            st= True
        soc=Label(can,image=s7,bg="black")
        soc.place(x=sx,y=sy) 

    if(ya2 == True and ys2>0 and (sy != 315 or (sx>=200 and sx<=330 and sy >= 275))and(sy != 205 or ((sx>=50 and sx<=115 and sy>=100 and sy<= 205)or(sx>=415 and sx<=470 and sy>=100 and sy<= 205)))and(sy != 100 or (sx>=230 and sx<=290 and sy >= 0 and sy <= 100))):
        v.after(10,salto2)
    else:
        ya2=False
        st=False
        ys2= 0
        if(est2==0 or est2 ==1 or est2 == 2):
            soc.destroy()
            soc=Label(can,image=s2,bg="black")
            soc.place(x=sx,y=sy)
            est2=2
        else:
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
                ya = False
            elif(mx>=395):
                mx=90
                my=425
                ya = False
        if(my<=425 and my >= 320):
            if(mx<=80):
                mx=390
                my=100
                ya = False
            if(mx>=445):
                mx=90
                my=100
                ya = False
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
                ya2 = False
            elif(sx>=395):
                sx=90
                sy=425
                ya2 = False
        if(sy<=425 and sy >= 320):
            if(sx<=80):
                sx=390
                sy=100
                ya2 = False
            if(sx>=445):
                sx=90
                sy=100
                ya2 = False
        v.after(100,Caida2)




    
def muereM():
    global v,can,M,mx,my,mar,est,ya,E,dif,h,ron,eron,vida
    ya = True
    mar.destroy()
    if(vida>0):
        vida-=1
        mx=300
        my=425
        mar=Label(can,image=m3,bg="black")
        mar.place(x=mx,y=my)
        ya = False

def Enemigos():
    global v,can,M,mx,my,mar,est,ya,E,dif,h,ron,eron
    x=0
    while x < len(E):
        if(E[x][0] <= 3):
            if(E[x][0] == 2 or E[x][0] == 3):
                if(E[x][1] < 500): 
                    E[x][1]+=dif
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
                else:
                    E[x][1]=5
                 
            elif(E[x][0] == 0 or E[x][0] == 1):
                if(E[x][1] > 5): 
                    E[x][1]-=dif
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
                else:
                    E[x][1]= 500
            if(E[x][2]>=116 and E[x][1] >=230 and E[x][1] <= 290 and E[x][2] < 221 ):
                    E[x][2]+=min(221-E[x][2],10)
            if((E[x][2]>=221 and E[x][2] < 332)and((E[x][1] >=415 and E[x][1] <= 475)or(E[x][1] >=50 and E[x][1] <= 115))  ):
                    E[x][2]+=min(332-E[x][2],10)
            if(E[x][2]>=332 and E[x][1] >=200 and E[x][1] <= 330 and E[x][2] < 441 ):
                    E[x][2]+=min(441-E[x][2],10)
            if(E[x][2]<=116):
                if(E[x][1]<80):
                    E[x][1]=450
                    E[x][2]=441
                elif(E[x][1]>450):
                    E[x][1]=80
                    E[x][2]=441
            if(E[x][2]<=441 and E[x][2] >= 340):
                if(E[x][1]<80):
                    E[x][1]=450
                    E[x][2]=116
                if(E[x][1]>450):
                    E[x][1]=80
                    E[x][2]=116
            if(E[x][3]==1):
                if(E[x][2] + 65 >= my and E[x][2] + 30 <= my and E[x][1] <= mx + 30 and E[x][1] + 30 >= mx and ya == True):
                    E[x][0] = 5
            if(E[x][0]==5):
                E[x][4].destroy()
                E[x][4]= Label(can,image=ec4,bg="black")
                E[x][4].place(x=E[x][1],y=E[x][2])
                E[x][0] = 6
            #matar jugador
            if(E[x][2] <= my + 50 and E[x][2] + 30 >= my and E[x][1] <= mx + 30 and E[x][1] + 30 >= mx and ya == False):
                muereM()
                

        if(E[x][0] == 6):
            h+=1
            if(h >= 10):
                h=0
                E[x][4].destroy()
                if(eron<(3+ron)):
                    eron+=1
                    ar = random.randint(1,2)
                    if(ar==1):
                        E[x]=[2,80,116,1]
                        E[x].append(Label(can,image=ec2,bg="black"))
                        E[x][4].place(x=E[x][1],y=E[x][2])
                    else:
                        E[x]=[0,450,116,1]
                        E[x].append(Label(can,image=ec0,bg="black"))
                        E[x][4].place(x=E[x][1],y=E[x][2])
        x+=1
    v.after(80,Enemigos)

def ronda():
    global ron,eron,v,can,menu1I,menu2I,M,mar,E,time
    if(time>=difr):
        if(eron < 3+(ron*difc)):
            eron+=1
            ar = random.randint(1,2)
            if(ar==1):
                E.append([2,80,116,1])
                E[len(E)-1].append(Label(can,image=ec2,bg="black"))
                E[len(E)-1][4].place(x=E[len(E)-1][1],y=E[len(E)-1][2])
            else:
                E.append([0,450,116,1])
                E[len(E)-1].append(Label(can,image=ec0,bg="black"))
                E[len(E)-1][4].place(x=E[len(E)-1][1],y=E[len(E)-1][2])
            time=0
    if(eron>=3+(ron*difc)):
        ron+=1
        eron=0
        print(ron+1)
    time+=1
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


K=[]
O=["'d'","'a'","'w'","'6'","'8'","'4'"]
                      
time=180
vida = 3 
ron = 0
eron=0
h=0

dif=5 #velocidad enemigos
difr=20000000 #velocidad aparicion
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


