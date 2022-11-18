import os, time, sys


B="\033[1;34m"        # Blue
O="\033[0m"       # Text Reset
Pu="\033[1;35m"      # Purple
R="\033[1;31m"         # Red
G="\033[1;32m"       # Green
Y="\033[1;33m"      # Yellow
C="\033[1;36m"        # Cyan  
Bl="\033[1;30m"      #Black

os.system('clear')

def printer(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

logo2='''
\033[1;34m
$$$$$$$$\ $$$$$$$\                      $$\           
\__$$  __|$$  __$$\                     \__|          
   $$ |   $$ |  $$ | $$$$$$\   $$$$$$$\ $$\  $$$$$$$\ 
   $$ |   $$$$$$$\ | \____$$\ $$  _____|$$ |$$  _____|
   $$ |   $$  __$$\  $$$$$$$ |\$$$$$$\  $$ |$$ /      
   $$ |   $$ |  $$ |$$  __$$ | \____$$\ $$ |$$ |      
   $$ |   $$$$$$$  |\$$$$$$$ |$$$$$$$  |$$ |\$$$$$$$\ 
   \__|   \_______/  \_______|\_______/ \__| \_______|
                                                      
                                                      
'''
def menu():
  print(logo2)
  printer('\n Welcome To \033[1;31mTermux \033[1;33mBasic Installer')
  time.sleep(1)
  print(50*"-")
  s = ' \033[1;31m[\033[1;33m1\033[1;31m] \033[1;36mStart Basic Installation \n \033[1;31m[\033[1;33m2\033[1;31m] \033[1;36mShow all package \n \033[1;31m[\033[1;33m3\033[1;31m] \033[1;36mFollow on Facebook \n \033[1;31m[\033[1;33m4\033[1;31m] \033[1;36mGithub \n \033[1;31m[\033[1;33m5\033[1;31m] \033[1;36mExit \033[1;33m'
  print(50*"-")
  print(s)
  print(50*"-")
  print(50*"-")
  
  mo = input('\033[1;34m[•] Enter \033[1;31m>>>\033[1;33m ')
  
  if mo in ["1","01","a","A"]:
    install()
  elif mo in ["2","02","b","B"]:
    show()
  elif mo in ["03","3","c","C"]:
    os.system('xdg-open https://www.facebook.com/v3l0x.me')
  elif mo in ["04","4","d","D"]:
    os.system('xdg-open https://github.com/Andrew-Velox')
  elif mo == "5":
    os.system('exit')
    
    
def install():
  os.system('clear')
  print("")
  print ('Allow the Button For Access the Storage in Termux')
  os.system('termux-setup-storage')
  os.system ("apt upgrade -y")
  os.system("pkg install python")
  os.system('pkg install python2')
  os.system('pip install --upgrade pip')
  os.system('pip install requests')
  os.system("apt install clang")
  os.system("apt install nano")
  os.system("pip install rich")
  os.system("pip install stdiomask")
  os.system('pip install mechanize')
  os.system('pip2 install requests')
  os.system('pip2 install mechanize')
  os.system('pip2 install bs4')
  os.system('pip install lolcat')
  os.system('pip2 install lolcat')
  os.system('pkg install wget')
  os.system('pkg install php -y')
  os.system('pkg install bash')
  os.system ("apt install python-dev -y")
  os.system('xdg-open https://github.com/Andrew-Velox')
  os.system('clear')
  print(logo2)
  print('All Basic Pkg Install successful\n')
  input('\nPress the enter key to exit ')
  
def show():
  os.system('clear')
  print(logo2)
  printer('''
[01]  termux-setup-storage
[02]  apt upgrade -y
[03]  pkg install python2
[04]  pip install --upgrade pip
[05]  pip install requests
[06]  pip install rich
[07]  pip install mechanize
[08]  pip2 install requests
[09]  apt install clang
[10]  apt install nano
[11]  pip2 install mechanize
[12]  pip2 install bs4
[13]  pip install lolcat
[14]  pip2 install lolcat
[15]  pkg install wget
[16]  pkg install php -y
[17]  pkg install bash
[18]  pip install stdiomask
[19]  apt install python-dev -y

  ''')
  m = input('Enter To Continue ')
  if m == '':
    os.system('python tbasic.py')
    
    
if __name__=='__main__':
  menu()
  