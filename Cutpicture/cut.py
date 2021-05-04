# -*- coding: UTF-8 -*-
#!/usr//python
from PIL import Image
import sys
import os
 

 
#当前文件所在文件夹

for i in os.listdir(os.path.dirname(__file__)):
    if '.jpg' in i or '.png' in i:
        file_path = os.path.dirname(__file__) + '/' + i
        print(file_path)


 
#填充新的image
def fill_image(image):
    width, height = image.size
    print('width:{%d}, height:{%d}' % (width, height))
 
    _length = width
    if height > width:
        _length = height
 
    new_image = Image.new(image.mode, (_length, _length), color='white')
 
    if width > height:
        new_image.paste(image, (0, int((_length - height) / 2)))
    else:
        new_image.paste(image, (int((_length - width) / 2), 0))
    return new_image
 
#裁剪image
def cut_image(image):
    width, height = image.size
    _width = int(width / 3)
    print('_width:{%d}' % _width)
 
    box_list = []
 
    # (left, top, right, bottom)
    for i in range(0, 3):
        for j in range(0, 3):
            print('i:{%d}, j:{%d}' % (i, j))
            box = (j*_width, i*_width, (j+1)*_width, (i+1)*_width)
            box_list.append(box)
            image_list = [image.crop(box) for box in box_list]
    return image_list
 
#将image列表的里面的图片保存
def save_images(image_list): 
    index = 1 
    #创建result文件夹
    res_dir = os.path.join(os.path.dirname(__file__), 'result')
    if not os.path.exists(res_dir):
        os.mkdir(res_dir)
 
    for image in image_list:
        new_name = os.path.join(res_dir, str(index) + '.png')
        image.save(new_name, 'PNG') 
        index += 1 
    print('图片保存完毕！')
 
 
if __name__ == '__main__':
    msg = input("请输入图片的绝对路径,或放到与项目代码文件相同的路径下运行:")
    if msg:
        file_path = msg
    else:
        pass
    image = Image.open(file_path)
    #image.show()
    image = fill_image(image)
    #
    image_list = cut_image(image)
    #
    save_images(image_list)
    print('程序结束！')
