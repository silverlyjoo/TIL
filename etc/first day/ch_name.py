import os
os.chdir(r'C:\Users\student\Desktop\TIL\Dummy')
for filename in os.listdir("."):
    os.rename(filename, filename.replace("samsung", "SSAFY"))