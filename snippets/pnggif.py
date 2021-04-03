from PIL import Image
import glob
import os


# Create the frames
def pnggif(output):
	frames = []
	imgs = glob.glob("png_gif/*.png")
	for i in imgs:
	    new_frame = Image.open(i)
	    frames.append(new_frame)


	frames[0].save(
		output,
		format='GIF',
	    append_images=frames[1:],
	    save_all=True,
	    duration=300, loop=0)
	return output

file = pnggif(output="cat.gif")
os.startfile(file)