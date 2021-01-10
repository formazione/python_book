from PIL import Image,ImageDraw,ImageFont
import tkinter as tk


def create_img_with_text(text=""):
	if text == "":
		text = "Pythonprogramming.altervista.org"
	# sample text and font
	unicode_text = u"Pythonprogramming.altervista.org"
	font = ImageFont.truetype(
		"C:\\Program Files\\Android\\Android Studio\\jre\\jre\\lib\\fonts\\DroidSans.ttf",
		24,
		encoding="unic")
	# get the line size
	text_width, text_height = font.getsize(unicode_text)
	# create a blank canvas with extra space between lines
	canvas2 = Image.new('RGB', (text_width + 10, text_height + 10), "orange")
	# draw the text onto the text canvas2, and use black as the text color
	draw = ImageDraw.Draw(canvas2)
	draw.text((5,5), text, 'blue', font)
	canvas2.save("mytext.png", "PNG")
	canvas2.show()


def win_with_image():
	root = tk.Tk()
	root.title("Animation")
	root.state("zoomed")
	canvas = tk.Canvas(root, width=400, height=500)
	print(canvas['width'])
	canvas.pack()
	img = tk.PhotoImage(file="mytext.png")
	canvas.create_image(int(canvas['width']) // 2,int(canvas['height']) // 2, image=img, anchor=tk.W)
	root.mainloop()

create_img_with_text()
# win_with_image()

