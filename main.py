from PIL import Image,ImageFilter
img = Image.open('./rm.jpg')

convertImg = img.convert('L')

convertImg.save('ci.png','png')
#keeping aspect ratio
img.thumbnail((400,200))
img.save('change.jpg')



new_img = img.resize((400,400))
new_img.save('ch.jpg')


