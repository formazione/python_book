import tkinter as tk
from tk_html_widgets import HTMLLabel

root = tk.Tk()

def tag(_type="h1", text="hello", color="black",text_align="center"):
	"Parses some html tags"
	html_label = HTMLLabel(root, html=f'<{_type} style="color: {color}; text-align: {text_align}"> {text} </{_type}>')
	html_label.pack(fill="both", expand=True)
	html_label.fit_height()
	return html_label

tag("h1", "This is H1", "blue")
tag("h2", "This is H2", "orange")
tag("p", "Welcome, this is a basic usage of the tk_html_widgets.", "red", "left")
tag("p",
	"We will make another video about this, because it is interesting and \
	we want to get a little deeper into it.",
	"darkgreen",
	"left")

root.mainloop()




