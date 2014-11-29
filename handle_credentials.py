__author__ = 'TPei'
import getpass

# provides github credentials from txt file
# if no txt file available, asks for input
try:
    file = open('../pw.txt')
    username = next(file)
    pw = next(file)
    file.close()
except OSError:
    username = input('username: ')
    pw = input('password: ')

username = username.replace('\n', ' ').replace('\r', '')
pw = pw.replace('\n', ' ').replace('\r', '')