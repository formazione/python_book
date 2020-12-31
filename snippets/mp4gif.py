import ffmpy
import glob

def menu(output):
	lof = glob.glob("*.mp4")
	for f in lof:
		print(lof.index(f)+1, f)
	nof = int(input("Number of file to convert: "))
	name = lof[nof-1]
	print(name)
	return name, name[:-4] + output
mp4, gif = menu(".gif")

ff = ffmpy.FFmpeg(
	inputs = {mp4 : None},
	outputs = {gif : None})

ff.run()


