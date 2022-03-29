import random

def decor(func1,func2,func3):
    def wrap():
        print('================')
        func1()
        func2()
        func3()
        print('================')
    return wrap


def print_text():
    print('MENU DE INICIO')

def print_text1():
    print('1. Iniciar juego')

def print_text2():
     print('2. Salir')  


print_text= decor(print_text,print_text1,print_text2)
print_text()






a = int(input('Inserte opcion: '))
print('\n')










    

#tablero

def tablero():
    nombre= nom
    print('-----------------------------------')
    print('\tUSUARIO: ' + nombre)
    puntaje = 0
    print('\tPUNTEO: ' + str(puntaje))
    print('\n')
    premios=0
    
    lista = [

          ['|',' ',' ',' ',' ',' ',' ',' ','X','X','X',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ','X',' ',' ',' ','X',' ',' ',' ','|'],
          ['|',' ',' ','X',' ',' ',' ','X',' ',' ',' ','X',' ',' ',' ','|'],
          ['|',' ','X','X',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'],
          ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|']

    ]
    
    #a= random.randint(0, 2)
    #b= random.randint(0, 6)
    #if a>0 and b<15:
     #lista[a][b]='@'

    for i in range(8):
        c= random.randint(0, 8)
        d= random.randint(1, 14)
        #if c>1 and d<15:
        if lista[c][d] != 'X':
                if lista[c][d]!='O':
                    if lista[c][d]!='<':
                     i=lista[c][d]='@'

    
    for j in range(7):
        e=random.randint(0, 8)
        f=random.randint(1, 14)
        #if e>1 and f<15:
        if lista[e][f] != 'X':
         if lista[e][f]!='@':
          if lista[e][f]!='<':
           j = lista[e][f] = 'O'
    
            
    
    

    x= random.randint(0, 9)
    y= random.randint(1, 14)
    #if y>1 and y<16:
    if lista[x][y] != 'X':
            if lista[x][y] != 'O':
                if lista[x][y]!='@':
                   lista[x][y]='<'


    print('--------------------------------')
    for sublista in lista:
        for i in range(len(sublista)):
           print(sublista[i],end=" ")
        print("")

    print('--------------------------------')

    

    while True:

     mover = input('Movimiento: ')
      #Empieza movimiento de pacman
     if mover=='d':
          y+=1
          #lista[x][y]='<'
          if x>0 and x<9:
           lista[x][y-1]=' '


     if mover=='a':
         y-=1
         #lista[x][y]='<'
         if x>0 and x<9:
          lista[x][y+1]=' '
          

     if mover=='w':
         x-=1
         #lista[x][y]='<'
         if x>0 and x<9:
             lista[x+1][y]=' '

     if mover=='s':
         x+=1
         #lista[x][y]='<'
         if x>0 and x<9:
             lista[x-1][y]=' '

         
     #ermina movimiento de pacman

     #En caso de tocar paredes
     if lista[x][y]=='X':
              print('pared') 
              break
     
     #if lista[x][y]=='X':
      #   print('Pared')
         

     if lista[x][y]=="O":
         puntaje+=10

     if puntaje ==50:
         print("Felicidades has ganado!")
         break  

     if lista[x][y] == '|':
         print('nopeeeeeeeeeeeee')
         break  

     if lista[x][y]=='@':
         print('intentalo de nuevo')
         tablero()   


     if lista[x][y] == 'O':
         premios+=1
         if premios==j:
            print('Al fin lo hiciste')

     

     if mover=='f':
         break      
         
     lista[x][y]='<'
     nombre= nom
     print('-----------------------------------')
     print('\n')
     print('\tUSUARIO: ' + nombre)
     print('\tPUNTEO: '+str(puntaje))
     print('\n')
     print('--------------------------------')
     for sublista in lista:
        for i in range(len(sublista)):
           print(sublista[i],end=" ")
        print("")

     print('--------------------------------')     
  
     
   
    



if a==1:
    nom=input('Inserte su nombre: ')
    print('\n\n')
    if nom==nom:
     tablero() 



    
if a==2:
    print('Gracias')    


