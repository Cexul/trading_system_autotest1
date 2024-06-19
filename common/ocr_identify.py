#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/19 10:38
# @Author: xuliang

import ddddocr


class OcrIdentify(object):
    def __init__(self):
        self.ocr = ddddocr.DdddOcr()

    def indentify(self, pic_path):
        with open(pic_path, 'rb') as f:
            image = f.read()
        res = self.ocr.classification(image)
        return res

# if __name__ == '__main__':
#     print(OcrIdentify().indentify('test.png'))
