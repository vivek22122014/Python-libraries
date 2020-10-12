
#How to load an image
from PIL import Image #import image class from PIL
im=Image.open("python.png") #open() method to load an image
im.show() #show() method to display the image





#How to check the format of an image
print(im.format) #format method returns format of an image


#How to check the size of an image
print(im.size) #format method returns size of an image



#How to mode the size of an image
print(im.mode)




#How to crop an image
box=(100,100,400,400) #defining sides of an image
region=im.crop(box) #crop method to crop the image
region.show()       #Atlast call the show method to display the image


#How to Rotate of an image
rt=im.rotate(45) #rotate() method to rotate the image, pass the value how much you want to rotate
rt.show()    #Atlast call the show method to display the image


#How to change the color of an image
im=Image.open('python.png').convert("L")
im.show()


#How to Change the Resize of an image
python=Image.open("python.png") #open an image
rz=python.resize((300,300)) #use resize() method to resize the image, pass two parameter - width and height
rz.show()  #Atlast call the show method to display the image




