from PIL import Image

dark_blue = (0, 51, 76) 
red = (217, 26, 33)
light_blue = (112, 150, 158) 
yellow = (252, 227, 166)

im = Image.open("obamicon.jpg")
pixels = im.getdata()

pixel_list = {}
pixel_list ={
			"dark_blue":(0, 51, 76) 
			"red": (217, 26, 33)
			"light_blue": (112, 150, 158) 
			"yellow": (252, 227, 166)
			}
			
list = list(pixel)
			
redder_pixels = pixels
for r, g, b in list:
	new_red = r + int(r * .5)
	new_data = (new_red, g, b)
	redder_pixels. append