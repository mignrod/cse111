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