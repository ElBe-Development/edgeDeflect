import argparse


import os
import configparser


parser = argparse.ArgumentParser(description='D')
parser.add_argument('--windowsstart', help='H1')




args = parser.parse_args()
config = configparser.ConfigParser()
config.read('config.ini')


def init():
    ### here we init the script like creating folders and changing run locations...
    ### and variable... so on...
    installDir = ""
    if installDir != "" :
        os.chdir(installDir)





    # Load Ini-file
    ConfigDeployMethod = config.get('Settings', 'DeployMethod')

    print(ConfigDeployMethod)


    pass



if __name__ == '__main__':

    init()
    if args.windowsstart:
        # run code on pc start
        pass

    if not args.windowsstart:
        # here we can set settings...
        pass