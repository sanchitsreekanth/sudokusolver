import requests
from bs4 import BeautifulSoup

def getboard(x):

    link = requests.get('http://nine.websudoku.com/?level={}'.format(x)).content
    soup=BeautifulSoup(link, 'lxml')
    data=['f00', 'f10', 'f20', 'f30', 'f40', 'f50', 'f60', 'f70', 'f80', 'f01', 'f11', 'f21', 'f31', 'f41', 'f51', 'f61', 'f71', 'f81', 'f02', 'f12', 'f22', 'f32', 'f42', 'f52', 'f62', 'f72', 'f82', 'f03', 'f13', 'f23', 'f33', 'f43', 'f53', 'f63', 'f73', 'f83', 'f04', 'f14', 'f24', 'f34', 'f44', 'f54', 'f64', 'f74', 'f84', 'f05', 'f15', 'f25', 'f35', 'f45', 'f55', 'f65', 'f75', 'f85', 'f06', 'f16', 'f26', 'f36', 'f46', 'f56', 'f66', 'f76', 'f86', 'f07', 'f17', 'f27', 'f37', 'f47', 'f57', 'f67', 'f77', 'f87', 'f08', 'f18', 'f28', 'f38', 'f48', 'f58', 'f68', 'f78', 'f88']
    a  = []
    board = [[0 for i in range(9)] for j in range(9)]
    for i in data:
        q = soup.find('input', id = i)
        a.append(q)
    c = 0
    for i in range(9):
        for j in range(9):
            try:
                board[i][j] = int(a[c]['value'])
            except:
                board[i][j] = 0
            c = c+1
    return board
