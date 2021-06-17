from gpiozero import LED, Button
from typing import Tuple
from time import sleep
import hashlib
import random

class Rounder:
    def __init__(self, random_number_range:Tuple)
        self.number_range = random_number_range
        self.used_numbers = set()
    
    def resetRounder(self, new_range:Tuple)-> None:
        self.number_range = new_range
        self.used_numbers = set()
    
    def IterRound(self)-> int:
        if (self.number_range[1] - self.number_range[0]) > len(used_numbers):
            while True:
                used_number = random.randint(self.number_range[0], self.number_range[1])
                if used_number in self.used_numbers:
                    break
            self.used_numbers.add(used_number)
            return used_number
    


def menu():
    print("Hola, bienvenido!\n")
    sleep(1)
    modes()

def modes():
    print("Por favor selecciona el modo que quieras jugar:\n")
    print("1) Tablas por elección de usuario\n")
    print("2) Tablas aleatorias\n")
    print("3) Acumulables\n")    
    sleep(1)
    ms = select_mode()
    if ms == 1:
        mode1()
    elif ms == 2:
        mode2()
    else:
        mode3()

def select_mode():
    wait_m = 0
    while wait_m == 0:
        if button1.is_active:
            sleep(0.1)
            button1.wait_for_release()
            md = 1
            wait_m = 1
        elif button2.is_active:
            sleep(0.1)
            button2.wait_for_release()
            md = 2
            wait_m = 1
        elif button3.is_active:
            sleep(0.1)
            button3.wait_for_release()
            md = 3
            wait_m = 1
    return md

    
#MODO 1
def mode1():
    print("Selecciona la tabla: ")
    sleep(1)
    globals()['n1'] = select_table()
    m = 1
    play(m)

#MODO 2
def mode2():
    m = 2
    play(m)
    
#MODO 3
def mode3():
    m = 3
    play(m)

def select_table():
    num_ready = 0
    while num_ready == 0:
        if button1.is_active:
            sleep(0.1)
            button1.wait_for_release()
            tab = 1
            print("1\n")
            num_ready = 1
        elif button2.is_active:
            sleep(0.1)
            button2.wait_for_release()
            tab = 2
            print("2\n")
            num_ready = 1
        elif button3.is_active:
            sleep(0.1)
            button3.wait_for_release()
            tab = 3
            print("3\n")
            num_ready = 1
        elif button4.is_active:
            sleep(0.1)
            button4.wait_for_release()
            tab = 4
            print("4\n")
            num_ready = 1
        elif button5.is_active:
            sleep(0.1)
            button5.wait_for_release()
            tab = 5
            print("5\n")
            num_ready = 1
        elif button6.is_active:
            sleep(0.1)
            button6.wait_for_release()
            tab = 6
            print("6\n")
            num_ready = 1
        elif button7.is_active:
            sleep(0.1)
            button7.wait_for_release()
            tab = 7
            print("7\n")
            num_ready = 1
        elif button8.is_active:
            sleep(0.1)
            button8.wait_for_release()
            tab = 8
            print("8\n")
            num_ready = 1
        elif button9.is_active:
            sleep(0.1)
            button9.wait_for_release()
            tab = 9
            print("9\n")
            num_ready = 1
    return tab
    

def choose_number():
    nr = random.choice(numbers)
    return nr

def play(mode):
    score = 0
    ac = 0
    comb = 0
    while True:
        if mode == 1 or mode == 2:
            if comb == 3:
                print("Score final: ",score,"\n")
                sleep(4)
                ac = 0
                break
        if mode == 2: globals()['n1'] = choose_number()
        if mode == 3:
            if score >= 5:
                print("Felicidades, ganaste!!\n")
                sleep(4)
                ac = 0
                break
            if ac == 0:
                globals()['n1'] = choose_number()
                ac = 1
            else:
                if c == 1:
                    globals()['n1'] = int(mult)
        n2 = choose_number()
        globals()['mult'] = str(n1*n2)
        print("¿Cuánto es ",n1," x ",n2,"?\n")
        comb += 1
        sleep(1)
        for i in mult:
            t = 1
            while t == 1:
                if button0.is_active:
                    sleep(0.1)
                    print("0\n")
                    ans = 0
                    globals()['c'] = compare(button0,i,ans,len(mult))
                    t=0
                elif button1.is_active:
                    sleep(0.1)
                    print("1\n")
                    ans = 1
                    globals()['c'] = compare(button1,i,ans,len(mult))
                    t=0
                elif button2.is_active:
                    sleep(0.1)
                    print("2\n")
                    ans = 2
                    globals()['c'] = compare(button2,i,ans,len(mult))
                    t=0
                elif button3.is_active:
                    sleep(0.1)
                    print("3\n")
                    ans = 3
                    globals()['c'] = compare(button3,i,ans,len(mult))
                    t=0
                elif button4.is_active:
                    sleep(0.1)
                    print("4\n")
                    ans = 4
                    globals()['c'] = compare(button4,i,ans,len(mult))
                    t=0
                elif button5.is_active:
                    sleep(0.1)
                    print("5\n")
                    ans = 5
                    globals()['c'] = compare(button5,i,ans,len(mult))
                    t=0
                elif button6.is_active:
                    sleep(0.1)
                    print("6\n")
                    ans = 6
                    globals()['c'] = compare(button6,i,ans,len(mult))
                    t=0
                elif button7.is_active:
                    sleep(0.1)
                    print("7\n")
                    ans = 7
                    globals()['c'] = compare(button7,i,ans,len(mult))
                    t=0
                elif button8.is_active:
                    sleep(0.1)
                    print("8\n")
                    ans = 8
                    globals()['c'] = compare(button8,i,ans,len(mult))
                    t=0
                elif button9.is_active:
                    sleep(0.1)
                    print("9\n")
                    ans = 9
                    globals()['c'] = compare(button9,i,ans,len(mult))
                    t=0
            if c == 0:
                break
        score = answer(c,score)
        sleep(1)

def compare(b,n,aw,sz_mult):
    globals()['nb'] += 1
    if aw == int(n) and nb != sz_mult:
        b.wait_for_release()
        return 1
    elif aw == int(n) and nb == sz_mult:
        b.wait_for_release()
        led_verde.on()
        sleep(0.5)
        led_verde.off()
        globals()['nb'] = 0
        return 1
    elif aw != int(n):
        b.wait_for_release()
        led_rojo.on()
        sleep(0.5)
        led_rojo.off()
        globals()['nb'] = 0
        return 0

def answer(a,sc):
    if a == 1:
        print("Respuesta correcta\n")
        new_score = sc + 1
        print("Score: ",new_score,"\n")
        return new_score
        
    else:
        print("Respuesta incorrecta\n")
        new_score = sc
        print("Score: ",new_score,"\n")
        return new_score
    
#Configurar LEDs
led_verde = LED(18)
led_rojo = LED(22)

#Configurar botones
button0 = Button(17)
button1 = Button(27)
button2 = Button(14)
button3 = Button(15)
button4 = Button(23)
button5 = Button(24)
button6 = Button(25)
button7 = Button(8)
button8 = Button(7)
button9 = Button(12)

numbers = [1,2,3,4,5,6,7,8,9]
mult = 0
n1 = 0
n2 = 0
c = 0
nb = 0

while True:
    menu()