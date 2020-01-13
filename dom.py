import turtle
import math
 
def drawHouse(t, length):
    for i in range(4):
        t.forward(length)
        t.right(90)
    t.left(45)
    t.forward(length/math.sqrt(2))
    t.right(90)
    t.forward(length/math.sqrt(2))
    t.right(135)
    t.forward(length)
    t.up()
    t.left(45)
    t.forward(length/math.sqrt(2))
    t.color("red")
    t.down()
    t.left(90)
    t.forward(length/math.sqrt(2))
    t.color("green")
    t.left(45)
    t.forward(length/math.sqrt(2))
    t.color("red")
    t.left(135)
    t.forward(length/math.sqrt(2))
    t.color("green")    
    t.rith(90)
    t.forward(length)
    t.color("red")
    t.rith(45)
    t.forward(length/math.sqrt(2))
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
