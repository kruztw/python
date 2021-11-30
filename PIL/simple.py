# writeup: https://github.com/aahsani/CTFWriteups/tree/master/UTCTF2021/SHIFT

from numpy import array
from PIL import Image

img = Image.open('SHIFT.png')
img_arr = array(img)
x_len, y_len, z_len = img_arr.shape

new_img = Image.new('RGB', (y_len, x_len), color = 'white')
new_Img_arr = array(img)

for x in range(x_len):
    off = (x_len - x)*6
    for y in range(y_len):
        new_y = (y + off) % y_len
        new_Img_arr[x][y] = img_arr[x][new_y]


result = Image.fromarray(new_Img_arr)
result.show()
#rress.save('res.png')

