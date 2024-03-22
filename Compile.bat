rmdir /s /q build
rmdir /s /q dist
del guiitrongenericcsv.spec
pyinstaller --hidden-import babel.numbers --windowed reading.py
@ECHO OFF
PAUSE