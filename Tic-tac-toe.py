def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: a b ")
    print(" a - номер строки  ")
    print(" b - номер столбца ")

def show():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")

def ask():
    while True:
        cords = input("         Ваш ход: ").split()
        
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue
        
        a, b = cords
        
        if not(a.isdigit()) or not(b.isdigit()):
            print(" Введите числа! ")
            continue
        
        a, b = int(a), int(b)
        
        if 0 > a or a > 2 or  0 > b or  b > 2 :
            print(" Координаты вне диапазона! ")
            continue
        
        if field[a][b] != " ":
            print(" Клетка занята! ")
            continue
        
        return a, b
            
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

greet()
field = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")
    
    a, b = ask()
    
    if count % 2 == 1:
        field[a][b] = "X"
    else:
        field[a][b] = "0"
    
    if check_win():
        break
    
    if count == 9:
        print(" Ничья!")
        break