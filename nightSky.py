import tkinter
import random

window = tkinter.Tk()

canvas_width, canvas_height = 800, 600

my_canvas = tkinter.Canvas(window, bg = '#070E59', width = canvas_width, height = canvas_height)
my_canvas.pack()

number_of_stars = random.randint(100, 1000)
x = 0
y = 0

constellation = []

for j in range(0,5):
    x = random.randint(0, canvas_width)
    y = random.randint(0, canvas_height)
    constellation.append(x)
    constellation.append(y)



    for i in range(0, number_of_stars + 1):

        x = random.randint(0, canvas_width)
        y = random.randint(0, canvas_height)



        star_size = random.randint(0, 4)
        star_colour = random.choice(('white', 'yellow', 'red', 'lightblue'))

        my_canvas.create_oval(x, y, x + star_size, y + star_size, fill=star_colour)

print(constellation)

my_canvas.create_line(constellation[0],constellation[1],constellation[2],constellation[3], fill='white', width=1)
my_canvas.create_line(constellation[2],constellation[3],constellation[4],constellation[5], fill='white', width=1)
my_canvas.create_line(constellation[0],constellation[1],constellation[6],constellation[7], fill='white', width=1)
my_canvas.create_line(constellation[4],constellation[5],constellation[8],constellation[9], fill='white', width=1)







tkinter.mainloop()



