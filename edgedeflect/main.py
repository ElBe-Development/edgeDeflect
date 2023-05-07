import argparse


import os
import configparser


parser = argparse.ArgumentParser(description='D')
parser.add_argument('--windowsstart', help='H1')




args = parser.parse_args()
config = configparser.ConfigParser()
config.read('config.ini')



ConfigDeflectMethod = ""




PrintMethods = r"""
[1] H1
[2] H2
[3] H3

[0] Exit"""




def init():
    ### here we init the script like creating folders and changing run locations...
    ### and variable... so on...
    global ConfigDeflectMethod
    installDir = ""
    if installDir != "" :
        os.chdir(installDir)





    # Load Ini-file
    ConfigDeflectMethod = config.get('Settings', 'DeflectMethod')




    pass



if __name__ == '__main__':

    init()
    if args.windowsstart:
        # run code on pc start
        pass

    if not args.windowsstart:
        # here we can set settings...
        print(f"DeflectMethod = {ConfigDeflectMethod}")
        print()
        print("Change the Method?")
        print(PrintMethods)
        cmdInput = input("Choose a Number =}")
        if not cmdInput.isdigit():
            exit("user is too dumb to follow instructions")
        elif int(cmdInput) == 0:
            exit()
        elif int(cmdInput) == 1:
            # code method 1
            print("#code method 1")
        elif int(cmdInput) == 2:
            # code method 2
            print("#code method 2")
        elif int(cmdInput) == 3:
            # code method 3
            print("#code method 3")
        else:
            exit("Number is Out of Range")
        pass