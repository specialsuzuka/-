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
from typing import Text
Path=input("请输入你要整理的文件路径:")
list1=os.listdir(Path)
for i in list1:
    fulllist=os.path.join(Path,i)
    if os.path.isdir(fulllist):
        
        a=os.path.join(Path,i)
        if not os.path.exists(Path+"\\Folders"):
            os.mkdir(Path+"\\Folders")
        b=os.path.join(Path,"Folders")
        shutil.move(a,b) 
    elif os.path.isfile(fulllist):  
        for i in list1:
            if i[-3:] in ['doc','docx','pdf','txt']:
                
                a=os.path.join(Path,i)
                if not os.path.exists(Path+"\\Documents"):
                    os.mkdir(Path+'\\Documents')
                c=os.path.join(Path,"Documents")
                shutil.move(a,c)
            elif  i[-3:] in ['zip','tar','gz']:
                a=os.path.join(Path,i)
                if not os.path.exists(Path+"\Archive"):
                    os.mkdir(Path+'\\Archive')
                d=os.path.join(Path,"Archive")
                shutil.move(a,d)
            




