from PIL import Image

im: Image.Image = Image.open('./assets/saber.jpeg')
print(im.format, im.size, im.mode, im.filename, im.format_description)

im.thumbnail((150, 100))
im.save('./assets/saber_thumb.jpeg', 'png')

# Us
im: Image.Image = Image.new(mode='RGBA', size=(100, 200), color="purple")
im.save('./assets/purple.png')
im: Image.Image = Image.new(mode='RGBA', size=(100, 100))
im.save('./assets/transparent.png')
