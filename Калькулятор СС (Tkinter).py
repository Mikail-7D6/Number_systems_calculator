from tkinter import *
    
window = Tk()
window.title("Калькулятор систем счисления")

frame1 = Frame(master = window, width = 540, height = 350)
frame1.pack()

label1 = Label(master = frame1, text = "Из какой системы счисления\n перевести число?")
label1.place(x = 40, y = 65)
label2 = Label(master = frame1, text = "В какую систему счисления\n перевести число?")
label2.place(x = 300, y = 65)
label3 = Label(master = frame1, text = "Ввидите число:")
label3.place(x = 40, y = 200)
label4 = Label(master = frame1, text = "-->")
label4.place(x = 260, y = 230)

ent1 = Entry(master = frame1, width = 23)
ent1.place(x = 310, y = 230)

from_ = IntVar()
in_ = IntVar()
from_.set(1)
in_.set(1)

from_1 = Radiobutton(master = frame1, text = '2', value = 1, variable = from_)
from_1.place(x = 30, y = 115)
from_2 = Radiobutton(master = frame1, text = '8', value = 2, variable = from_)
from_2.place(x = 80, y = 115)
from_3 = Radiobutton(master = frame1, text = '10', value = 3, variable = from_)
from_3.place(x = 130, y = 115)
from_4 = Radiobutton(master = frame1, text = '16', value = 4, variable = from_)
from_4.place(x = 190, y = 115)
 
in_1 = Radiobutton(master = frame1, text = '2', value = 1, variable = in_)
in_1.place(x = 290, y = 115)
in_2 = Radiobutton(master = frame1, text = '8', value = 2, variable = in_)
in_2.place(x = 340, y = 115)
in_3 = Radiobutton(master = frame1, text = '10', value = 3, variable = in_)
in_3.place(x = 390, y = 115)
in_4 = Radiobutton(master = frame1, text = '16', value = 4, variable = in_)
in_4.place(x = 440, y = 115)

ent_num = Entry(master = frame1, width = 25)
ent_num.place(x = 40, y = 230)

def introduction():
    system = from_.get()
    final = in_.get()
    num = ent_num.get()
    return system, final, num

def list_conv(lst_):
    if lst_[0] == 1:
        sy = '2'
    elif lst_[0] == 2:
        sy = '8'
    elif lst_[0] == 3:
        sy = '10'
    else:
        sy = '16'
    if lst_[1] == 1:
        fi = '2'
    elif lst_[1] == 2:
        fi = '8'
    elif lst_[1] == 3:
        fi = '10'
    else:
        fi = '16'
    return sy, fi, lst_[2]

def the_foundation():
    lst_ = introduction()
    lst = list_conv(lst_)
    if lst[2] == '0':
        output = lst[2]
    elif lst[0] == lst[1]:
        output = lst[2]
    elif lst[0] == '10':
        output = decima(lst[1], lst[2])
    elif lst[1] == '10':
        output = from_all_others(lst[0], lst[2])
    else:
        output = decima(lst[1], from_all_others(lst[0], lst[2]))
    numm = check_for_zero(output)
    ent1.delete(0, END)
    ent1.insert(0, numm)

def decima(final, num):
    number = ''
    if final == '2' or final == '8':
        while True:
            number += str(int(num) % int(final))
            num = int(num) // int(final)
            if num < int(final):
                number += str(num)
                break
    elif final == '16':
        side = 'in'
        while True:
            number += verification(num, side)
            num = int(num) // 16
            if num < 16:
                number += verification(num, side)
                break
    return number[::-1]

def verification(num, side):
    lis_num = [10, 11, 12, 13, 14, 15]
    lis_str = ['A', 'B', 'C', 'D', 'E', 'F']
    if side == 'in':
        if int(num) % 16 in lis_num:
            und = lis_num.index(int(num) % 16)
            number = lis_str[und]
        else:
            number = str(int(num) % 16)
    else:
        if num in lis_str:
            und = lis_str.index(num)
            number = lis_num[und]
        else:
            number = num
    return number

def from_all_others(system, num):
    number = 0
    if system == '2' or system == '8':
        num = list(num)[::-1]
        for i in range(len(num)):
            number += int(num[i]) * (int(system) ** i)
    elif system == '16':
        side = 'from'
        num = list(num)[::-1]
        for i in range(len(num)):
            num[i] = verification(num[i], side)
            number += int(num[i]) * (16 ** i)
    return number

def check_for_zero(num):
    if len(str(num)) == 1:
        num = num
    else:
        num = str(num)
        for _ in range(len(num)):
            if num[0] == '0':
                num = num.replace(num[0], '')
            else:
                break
    return num   
    
but_start = Button(text = 'Перевести', width = 20, height = 1, command =the_foundation)
but_start.place(x = 310, y = 190)
window.mainloop()
