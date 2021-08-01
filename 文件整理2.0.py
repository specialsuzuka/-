'''
个文件夹下有很多类型的文件，然后根据文件后缀名把这些文件放到不同的文件夹下，
文件夹放到Folders目录下
.doc .docx .pdf等等放到Document目录下
.zip .tar.gz等放到Archive目录下
.exe .dmg等放到Executable目录下
...

流程：
1. 读取当前目录下所有文件
2. 判断是文件还是文件夹
 2.1 如果是文件夹，放到Folders目录下。注意要避开Document，Archive，Executable等
 2.2 如果是文件，判断文件后缀名，然后移动到指定目录下。
 比如.doc .docx .pdf等等放到Documents文件夹下
 .zip .tar.gz等放到Archive文件夹下
'''

import os
import shutil
basePath=os.getcwd()
list1=os.listdir(basePath)
for i in list1:
    fulllist=os.path.join(basePath,i)
    if os.path.isdir(fulllist):
        oldPath=os.path.join(basePath,i)
        if not os.path.exists(basePath+"\\Folders"):
            os.mkdir(basePath+"\\Folders")
        newPath1=os.path.join(basePath,"Folders")
        shutil.move(oldPath,newPath1) 
    elif os.path.isfile(fulllist):  
        for i in list1:
            if i[-3:] in ['doc','docx','pdf','txt']:
                oldPath=os.path.join(basePath,i)
                if not os.path.exists(basePath+"\\Documents"):
                    os.mkdir(basePath+'\\Documents')
                newPath2=os.path.join(basePath,"Documents")
                shutil.move(oldPath,newPath2)
            elif  i[-3:] in ['zip','tar','gz']:
                oldPath=os.path.join(basePath,i)
                if not os.path.exists(basePath+"\Archive"):
                    os.mkdir(basePath+'\\Archive')
                newPath3=os.path.join(basePath,"Archive")
                shutil.move(oldPath,newPath3)
            




