from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

darkPurple = (66, 11, 63)
pink = (204, 44, 79)
lightPurple = (214, 96, 176)
peach = (255, 208, 188)


# Import image.
my_image = Image.open("GrayRabbit.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

pixeln = len(image_list)

recolored = []
intensity = 0

for count in range(0, pixeln):
    intensity = sum(image_list[count])
    intensity = int(intensity)
    if intensity < 182:
        recolored.append(darkPurple)
    elif intensity < 364:
        recolored.append(pink)
    elif intensity < 546:
        recolored.append(lightPurple)
    else:
        recolored.append(peach)


#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.



# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("DramaticRabbit2.jpg", "jpeg") #save the new image as "DramaticRabbit.jpg"
