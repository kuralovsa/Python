import turtle
col = ["red", "blue", "green", "cyan", "purple"] 
def drawHouse(t, length):
    for i in range(4):
        t.forward(length)
        t.color("red")
        t.right(90)
        t.color("blue")
    t.left(60)
    t.forward(length)
    t.color("red")
    t.right(120)
    t.color("red")
    t.forward(length)
    t.color("blue")
    t.color("red")
 
#Создаем окно для рисования
window = turtle.Screen() 
#Создаем объект для рисования pencil, ту самую "черепашку#
pencil = turtle.Turtle()
#Устанавливаем толщину линии для рисования
pencil.pensize(2)
#Вызов функции с параметрами length=150 и t = pencil
drawHouse(pencil,150)
#Закрывает окно с рисунком, посредством щелчка по оному
window.exitonclick()