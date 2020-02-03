#!/bin/python
import subprocess
import os, sys


def cd(path):
    try:
        os.chdir(str(path))
    except:
        print(f"Cant access the path : {path}")



def selectOption():
    current = os.getcwd()
    os.chdir(current)
    while True:
        print("»-(¯`·.·´¯)->BY ANDRES IN HOLBERTON<-(¯`·.·´¯)-«")
        print("0. GIT INIT")
        print("1. GIT ADD")
        print("2. GIT COMMIT")
        print("3. GIT PUSH")
        print("4. GIT STATUS")
        print("ADD. ADD REMOTE REPOSITORY")
        print("P.  PULL <ORIGIN> <BRANCH>")
        print("F. FETCH")
        print("B, LIST CURRENT BRANCHS")
        print("branch. SELECT BRANCH")
        print("For clone use clone:url")
        print("»-(¯`·.·´¯)->GIT HUB MANAGER<-(¯`·.·´¯)-«")
        opt = input("=> ")
        print('==========================================')
        Gtt = gt_manager()
        Gtt.init(opt)


class gt_manager:

        


    def init(self, opcion):
        if opcion == '0':
           
            subprocess.call(['git', 'init'])
            print('==========================================')
        
        elif opcion == '1':
            
            subprocess.call(['git', 'add', '*'])
            print("WHOLE PROYECT SAVED")
            print('==========================================')

        elif opcion == '2':
            c_msg = input("Enter commit message => ")
            subprocess.call(['git', 'commit', '-m', c_msg])
            print('==========================================')

        elif opcion == '3':
            b_msg = input("Select brach => ")
            remote_control = input("Remote control => ")
            subprocess.call(['git', 'push', '-u', remote_control, b_msg])
            print('==========================================')

        elif opcion == '4':
            subprocess.call(['git', 'status'])
            print('==========================================')

        elif opcion == 'ADD':
            url_repo = input("Enter remote repository URL => ")
            subprocess.call(['git', 'remote', 'add', 'origin', url_repo])
            print('==========================================')
            print("DONE")
            

        elif opcion == 'P':
            p_msg = input("Select branch => ")
            remote_control = input("Remote control => ")
            subprocess.call(['git', 'pull', remote_control, p_msg])
            print('==========================================')

        elif opcion == 'F':
            subprocess.call(['git', 'fetch'])
            print('Done!')


        elif opcion == 'B':
            subprocess.call(['git', 'branch', '-a'])
            print('==========================================')


        elif opcion == 'branch':
            s_branch = input("Select branch to move your workspace => ")
            subprocess.call(['git', 'checkout', s_branch])

        if opcion[0:5] == 'clone':
            url_clone = opcion[6::]
            if url_clone:
                subprocess.call(['git', 'clone', url_clone])
                print('=======================================')

        if opcion[0:2] == 'cd':
            go_to = opcion[3::]
            cd(go_to)
            print('Workspace moved to ', go_to)
            
            
                
            
            
            

        



if __name__ == '__main__':
    selectOption()
