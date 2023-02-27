import os

path = r"C:\Users\mark.de-melo\Arup\RIL-Compressed Air Storage Tanks-Design - Documents\Management\Doc Control\Transmittals"
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

for file in files:
    os.rename(fr'{path}\{file}', fr'{path}\{file[:-4]}\{file}')
