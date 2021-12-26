from PIL import Image,ImageDraw,ImageFont
image=Image.open("/Users/Joca/Documents/Projekti/Dnd Character Creator/CharSheet.png")
image.decode()
font_type=ImageFont.truetype("arial.ttf",24)
draw=ImageDraw.Draw(image)
draw.text(xy=(100,112),text="YEKSFASFOASOASJDO",fill=(255,69,0),font=font_type)
image.show()
