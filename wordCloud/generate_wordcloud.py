# 导入相应的库
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from PIL import Image
import numpy as np
import datetime


def generate_wordCloud_pic(words_txt_path: str, stopWords_txt_path: str, mask_pic_path: str):
    '''
    Function: 生成词云图片
    :param words_txt_path: 存放文本数据的txt文件的路径
    :param stopWords_txt_path: 存放停词的txt文件的路径
    :param mask_pic_path: 词云图片背景形状的图片地址
    '''
    script_path: str = os.path.dirname(os.path.realpath(__file__))
    today_date: str = str(datetime.date.today()).replace("-", "").replace("2020", "20")
    # 导入文本数据并进行简单的文本处
    with open(words_txt_path, encoding='utf8').read() as text:
        text = text.replace('\n', "").replace("\u3000", "")         # 去掉换行符和空格

    # 分词，返回结果为词的列表
    text_cut = jieba.lcut(text)
    # 将分好的词用某个符号分割开连成字符串
    text_cut = ' '.join(text_cut)

    # 导入停词，用于去掉文本中类似于'啊'、'你'，'我'之类的词
    stop_words = open(stopWords_txt_path, encoding="utf8").read().split("\n")

    background = Image.open(mask_pic_path)
    graph = np.array(background)

    # 使用WordCloud生成词云
    word_cloud = WordCloud(font_path="msyh.ttc",  # 设置词云字体
                        background_color="white",  # 词云图的背景颜色
                        mask=graph,  # 指定词云的形状
                        stopwords=stop_words)  # 去掉的停词
    word_cloud.generate(text_cut)

    # 运用matplotlib展现结果
    plt.subplots(figsize=(12, 8))
    plt.imshow(word_cloud)
    plt.axis("off")

    word_cloud.to_file(os.path.join(script_path, f'wordCloud_{today_date}.png'))
    print('已经成功生成词云')


if __name__ == "__main__":
    # 设置参数
    script_path: str = os.path.dirname(os.path.realpath(__file__))
    words_txt_path: str = os.path.join(script_path, 'joke.txt')
    stopWords_txt_path: str = os.path.join(script_path, 'stop_words_zh.txt')
    mask_pic_path: str = os.path.join(script_path, 'bb.png')

    generate_wordCloud_pic(words_txt_path, stopWords_txt_path, mask_pic_path)
