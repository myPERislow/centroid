from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os # os$B%b%8%e!<%k$N%$%s%]!<%H(B

#$B2hA|$NFI$_9~$_(B
 
# os.listdir('$B%Q%9(B')
# $B;XDj$7$?%Q%9Fb$NA4$F$N%U%!%$%k$H%G%#%l%/%H%j$rMWAG$H$9$k%j%9%H$rJV$9(B
files = os.listdir('answer')

images = []
 
for file in files:

    im = Image.open("answer/" + file)
    print (file)

    #$B2hA|$r(Barray$B$KJQ49(B
    im_list = np.asarray(im)

    smx = 0
    mx = 0 
    smy = 0
    my = 0
    # print (im_list.shape)
    plt.figure()
    im_painted = np.zeros(im_list.shape)
    print (im_painted.shape)

    for i in range(im_list.shape[0]):
        for j in range(im_list.shape[1]):
            if any(im_list[i][j][k] != im_list[0][0][k] for k in range(4)):
                im_painted[i][j] = 0.5
                smx += i
                mx += 1
                smy += j
                my += 1
            else :
                im_painted[i][j] = 0
                # print (i, j, im_list[i][j])
    cx = smx / mx
    cy = smy / my
    print (cx, cy)
    #$BE=$jIU$1(B
    plt.imshow(im_list)
    plt.plot(cy, cx, marker='x', c = 'b', markersize=10)
    plt.savefig("centered/" + file)
    images.append(im_list)

    plt.show()
    #$BI=<((B

