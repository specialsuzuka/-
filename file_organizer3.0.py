'''
另外如果当前路径有Folders, Documents文件夹，你的代码还会把他们放到Folders下
这些逻辑可以封装成函数，比如def move_to_documents:
'''

import os
import shutil
basePath=os.getcwd()
list1=os.listdir(basePath)


def file_to_filehome(filename,nowPath,filehome):
    oldPath=os.path.join(nowPath,filename)
    if not os.path.exists(nowPath+filehome):
        os.mkdir(nowPath+"\\"+filehome)
    newPath=os.path.join(nowPath,filehome)
    shutil.move(oldPath,newPath)

for i in list1:
    fulllist=os.path.join(basePath,i)
    if os.path.isdir(fulllist):
        file_to_filehome(i,basePath,"Folders")
    elif os.path.isfile(fulllist):  
        for i in list1:
            try:
                list2=i.split('.')
                if list2[-1] in ['doc','docx','pdf','txt']:
                    file_to_filehome(i,basePath,"Documents")
                elif  list2[-1] in ['zip','tar','gz']:
                    file_to_filehome(i,basePath,"Archive")
            except:
                file_to_filehome(i,basePath,"Others")
            




