from PIL import Image, ImageOps
from random import randint

im_pth = "C:/Users/Ryan/Documents/S20/Adversarial_ML/Paper/PatchedSource.png"
padding_amount = 30 # how many pixels of padding, {10, 20, 30}
desired_size = 224


im = Image.open(im_pth)
old_size = im.size  # old_size[0] is in (width, height) format
# old_size should ALWAYS be (224, 224), leaving this in here just in case something gets weird

ratio = (float(desired_size)-padding_amount*2)/max(old_size)
print(ratio)
new_size = tuple([int(x*ratio) for x in old_size])
# use thumbnail() or resize() method to resize the input image

# thumbnail is a in-place operation

# im.thumbnail(new_size, Image.ANTIALIAS)

im = im.resize(new_size, Image.BILINEAR)
# create a new image and paste the resized on it

new_im = Image.new("RGB", (desired_size, desired_size))
new_im.paste(im, ((desired_size-(new_size[0]+randint(-1*padding_amount, padding_amount)))//2,(desired_size-(new_size[1]+randint(-1*padding_amount, padding_amount)))//2)) # random zero padding image

new_im.show()
