#! python3
# pw.py
#insecure password locker

import sys, pyperclip

PASSWORDS = {'venmo': 'moneypassword', 'gmail': 'mailpassword', 'spotify': 'musicpassword', 'facebook': 'fbpassword', 'instagram': 'igpassword'}

if len(sys.argv) < 2 and len(sys.argv)>2 : #password locker will only copy to clipboard the password of the first account prompted
    print('Usage: python pw.py [account] -copy account password')
    sys.exit()

account = sys.argv[1] #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account +' copied to clipboard. (I only can give the password to one account at a time.) ')
else:
    print('There is no account named '+account)