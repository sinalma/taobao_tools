import os
import shutil
path="C:\\Users\\sinalma\\Desktop\\fuke-data\\SERVO\\Motor"
new_path='C:\\Users\\sinalma\\Desktop\\dsvpps'

for root ,dirs,files in os.walk(path):
    for i in range(len(files)):
        if (files[i][-3:] == 'jpg') or (files[i][-3:] == 'png')or (files[i][-3:] == 'PNG') or (files[i][-3:] == 'JPG'):
            file_path = root +'/'+files[i]
            print(files[i]+'-------')
            print(i)
            new_file_path = new_path+'/'+files[i]
            shutil.copy(file_path,new_file_path)