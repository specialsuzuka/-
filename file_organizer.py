import os
import shutil



TypeFolder = "Folders"
TypeDocument = "Documents"
TypeArchive = "Compressed"
TypeOther = "Others"
TypeMusic = "Music"
TypeVideo = "Video"
TypePhoto = "Photo"

ListDocument = ['doc','docx','pdf','txt','ppt','pptx','xls','xlsx']
ListArchive = ['zip','tar','gz']
ListMusic = ['mp3','wav','cda','ncm','flac','ape']
ListVideo = ['mp4','avi','wmv','mpeg','flash']
ListPhoto = ['jpg','jpeg','png','gif','bmp']

def move(filename, dst_folder):
    if not os.path.exists(dst_folder):
        os.mkdir(dst_folder)
    shutil.move(filename, os.path.join(dst_folder, filename))


def organize():
    base_path=os.getcwd()
    cur_dir_files=os.listdir(base_path)
    for file in cur_dir_files:
        if os.path.isdir(file):
            if file in [TypeFolder, TypeDocument, TypeArchive, TypeOther]:
                continue
            move(file, TypeFolder)
        elif os.path.isfile(file):
            if "." in file:
                parts = file.split('.')
                if parts[-1] in ListDocument:
                    move(file, TypeDocument)
                elif  parts[-1] in ListArchive:
                    move(file, TypeArchive)
                elif parts[-1] in ListMusic:
                    move(file,TypeMusic)
                elif parts[-1] in ListVideo:
                    move(file,TypeVideo)
                elif parts[-1] in ListPhoto:
                    move(file,TypePhoto)
                else:
                    move(file, TypeOther)
            else:
                move(file, TypeOther)


if __name__ == "__main__":
    organize()