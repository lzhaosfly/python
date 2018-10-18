from PIL import Image, ImageDraw, ImageFont
import os

imSaber2: Image.Image = Image.open('./assets/saber2.jpg')
print(imSaber2.format, imSaber2.size, imSaber2.mode,
      imSaber2.filename, imSaber2.format_description)

imSaber2.thumbnail((150, 100))
imSaber2.save('./assets/saber_thumb.jpeg', 'png')

width, height = imSaber2.size
quatersizedIm: Image.Image = imSaber2.resize((width//2, height//2))
quatersizedIm.save('./assets/saber2_resized.png')


# create new image
imaNewPurple: Image.Image = Image.new(
    mode='RGBA', size=(400, 400), color="purple")
imaNewPurple.save('./assets/purple.png')
imaNewTransparent: Image.Image = Image.new(mode='RGBA', size=(100, 100))
imaNewTransparent.save('./assets/transparent.png')


# crop image
# Note it's left, upper, right, and lower pixel
imSaber2: Image.Image = Image.open('./assets/saber2.jpg')
imCrop = imSaber2.crop((200, 15, 310, 135))
imCrop.save('./assets/croppedSaber2.png')


# copy paste image
imSaber2Crop: Image.Image = Image.open(
    './assets/saber2.jpg').crop((200, 15, 310, 135))
imageNewPurpleCopy = imaNewPurple.copy()
# paste to (100, 50), it's destImg.paste(srcImage, box)
imageNewPurpleCopy.paste(imSaber2Crop, (100, 50))
catlogo: Image.Image = Image.open('./assets/catlogo.png')
catlogo.thumbnail((150, 150))
imageNewPurpleCopy.paste(catlogo, (200, 50))  # paste to (100, 50)
imageNewPurpleCopy.save('./assets/purpleCopy.png')  # must save!!


# rotate and flip img
imSaber2: Image.Image = Image.open('./assets/saber2.jpg')
imSaber2.rotate(30).save('./assets/rotated30Sabaer2.png')
imSaber2.rotate(30, expand=True).save('./assets/rotated30ExpandSabaer2.png')
imSaber2.transpose(Image.FLIP_LEFT_RIGHT).save(
    './assets/flipHorizentalSaber2.png')
imSaber2.transpose(Image.FLIP_TOP_BOTTOM).save(
    './assets/flipVerticalSaber2.png')


# draw shape
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.line([(20, 20), (180, 20), (180, 180), (20, 180), (20, 20)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), outline='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),
             fill='brown')
im.save('./assets/drawShape.png')


# Draw font
im = Image.new('RGBA', (200, 200))
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')
FontFolder = '/Library/Fonts'
arialFont = ImageFont.truetype(os.path.join(FontFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
im.save('./assets/drawFont.png')
