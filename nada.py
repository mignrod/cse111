<<<<<<< HEAD
import pixellib
from pixellib.tune_bg import alter_bg
import cv2

change_bg = alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
output = change_bg.gray_bg("me.png")
cv2.imwrite("img.jpg", output)
=======
from PIL import Image

img = Image.open('me.png').convert('LA')

datas = img.getdata()
new_image_data = []
for item in datas:
    if item[0] in range(190, 256):
        new_image_data.append((255, 204, 100))
    else:
        new_image_data.append(item)
img.putdata(new_image_data)

img.save('resultado.png')
>>>>>>> b9aa5696994011c17a7b32f47ff050683563ff0a
