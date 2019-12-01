import urllib.request
import chardet

name = input('请输入URL:')

response = urllib.request.urlopen(name)



print('该网页使用的编码是:',chadet.detect(reponse[encoding]))

html = response.read()

if chardet.detect(reponse)['encoding'] == 'GB2312':
    reponse.decode('GBK')

