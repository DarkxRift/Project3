import os

d_name = '/home/pi/negatives_images'

list_files = os.listdir(d_name)

pic_num = 1

for i in range (len(list_files)):
        print(i)
        os.rename(os.path.join(d_name, list_files[i]),
        os.path.join(d_name, str(pic_num))
)
        pic_num += 1
