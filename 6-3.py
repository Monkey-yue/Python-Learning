# 6-3 An insecure password locker program

PASSWORDS = {'email':'eheheheheheheiii',
             'blog' : 'weqwewqeqqwdqwdqwd',
             'reddit' : 'dwdwdwddwqwqeqe'}

import sys, pyperclip

if len(sys.argv) < 2 :
    print('Usage : py 6-3.py [accountWebName] - copy your password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account name: ' + account)
    