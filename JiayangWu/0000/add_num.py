# Add a number to a image
from PIL import Image, ImageFont, ImageDraw

def add_num_to_image(img):
  im = Image.open(img)
  x, y = im.size
  color = '#ff0000'
  number_font = ImageFont.truetype('consolab.ttf', 100)
  for i in range(10):
    im = Image.open(img)
    draw_im = ImageDraw.Draw(im)
    draw_im.text((x-70, 10), str(i), font = number_font, fill = color)
    im.save('revised_image'+str(i)+'.jpg')

if __name__ == "__main__":
    img = 'image.jpg'
    add_num_to_image(img)
