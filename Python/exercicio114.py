import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.request.URLError:
    print('pudim.com.br não está acessivel')
else:
    print('Tudo certo')