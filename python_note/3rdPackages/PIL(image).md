# Pillow to deal with image

## 0. install

`pip install pillow`

## 2. usage

```python
from PIL import Image, ImageColor

ImageColor.getcolor('red', 'RGBA') # (255, 0, 0, 255)
ImageColor.getcolor('chocolate', 'RGBA') # (210, 105, 30, 255)

im: Image.Image = Image.open('./assets/saber.jpeg')
print(im.format, im.size, im.mode)

im.thumbnail((150, 100))
im.save('./assets/saber_thumb.jpeg', 'png')
```