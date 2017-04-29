import os

neg_name = '/home/pi/negatives_images'
pos_name = '/home/pi/positive_images'

neg = os.listdir(neg_name)
pos = os.listdir(pos_name)

for img in neg:
    line = neg + '/' + img + '\n'
    with open ('bg.txt', 'a') as f:
        f.write(line)

for img in pos:
    line = pos + '/' + img + '1 0 0 50 50\n'
    with open ('info.dat', 'a') as f:
        f.write(line)
