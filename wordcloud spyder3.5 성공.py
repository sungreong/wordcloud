# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:51:03 2017

@author: acorn
"""

import wordcloud
from scipy.misc import imread
twitter_mask = imread('twitter_mask.png', flatten=True)
import matplotlib.pyplot as plt
 from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
 import numpy as np
from PIL import Image
from os import path
twitter_mask = np.array(Image.open("twitter_mask.png"))
 image_colors = ImageColorGenerator(mask)
 mask = np.array(Image.open("cat.jpg"))


text="You can color a word-cloud by using an image-based coloring strategy implemented in ImageColorGenerator. It uses the average color of the region occupied by the word in a source image. You can combine this with masking - pure-white will be interpreted as ‘don’t occupy’ by the WordCloud object when passed as mask. If you want white as a legal color, you can just pass a different image to “mask”, but make sure the image shapes line up."
text=open("a.txt").read()
text=open("shape.txt").read()
mask = np.array(Image.open("ed2.png"))

twitter_mask = np.array(Image.open("shape.png"))
text=open("positive.txt").read()
twitter_mask = imread('grit.jpg', flatten=True)
twitter_mask
twitter_mask.shape
plt.imshow(twitter_mask )
np.set_printoptions(threshold=1000)
##############
twitter_mask = imread('shapefinal.png', flatten=True)
twitter_mask
######### 색깔이 다른것도 가능하게 해주는 부분 중요############### 
######### 색깔이 2가지로 나오게 만들어주는게 포인트 ##############
np.place(twitter_mask, twitter_mask<129, [0.])
np.place(twitter_mask, twitter_mask>128, [255.])
np.unique(twitter_mask)
twitter_mask.shape
plt.imshow(twitter_mask )

##########
wordcloud = WordCloud(
                      font_path='C:/ProgramData/Anaconda3/Lib/site-packages/pytagcloud/fonts/CabinSketch-Bold.ttf',
                      stopwords=STOPWORDS,
                      background_color='white',
                      width=500,
                      height=500,
                      mask=twitter_mask,
                      random_state=89                    
            ).generate(text) 

plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('./grit13.png', dpi=300)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
image_colors = ImageColorGenerator(twitter_mask)
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(twitter_mask, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()






