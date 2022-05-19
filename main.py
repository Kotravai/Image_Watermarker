from tkinter import *
from PIL import Image, ImageDraw, ImageFont

def watermarker():
    image = image_input.get()
    text = wm_input.get()
    with Image.open(image).convert("RGBA") as base:
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("Verdana", 40)
        # get a drawing context
        d = ImageDraw.Draw(txt)

        # draw text, half opacity
        d.text((10, 10), text, font=fnt, fill=(255, 255, 255, 128))
        # draw text, full opacity
        # d.text((10, 60), "World", font=fnt, fill=(255, 255, 255, 255))
        out = Image.alpha_composite(base, txt)
        out.show()



windows = Tk()
windows.title("K's Image Watermarker")
windows.minsize(width=600, height=250)
windows.config(padx=40, pady=20)

title = Label(text="Welcome to K's Image Watermarker!!", font=("verdana", 18, "bold"))
title.config(pady=20, padx=30)
title.grid(row=0, column=0, columnspan=4)

image_label = Label(text="Upload the image: ", font=("sanserif", 14, "bold"))
image_label.config(pady=10, padx=10)
image_label.grid(row=1, column=0)

image_input = Entry(width=40)
image_input.grid(row=1, columnspan=4, column=1)

watermark = Label(text="Watermark: ", font=("sanserif", 14, "bold"))
watermark.config(pady=10, padx=10)
watermark.grid(row=2, column=0)

wm_input = Entry(width=40)
wm_input.grid(row=2, columnspan=4, column=1)

convert_button = Button(text="Convert", fg='skyblue', command=watermarker)
convert_button.config(padx=8, pady=8)
convert_button.grid(row=4, column=1)

windows.mainloop()
