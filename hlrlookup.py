# Author: Gameye98
# Team: Schadenfreude & BHS
# Date: Wed Oct 16 19:32:12 2024
# Description: Home Location Register Lookup
#######
# Telegram: https://t.me/deletuserbot
# GitHub: https://github.com/Gameye98
####### Organizations
# GitHub: https://github.com/BlackHoleSecurity
# Telegram: https://t.me/schdenfreude
import sys
import sqlite3

db = sqlite3.connect("hlrlookup.db")
banner = """ _   _     _         _           
| |_| |___| |___ ___| |_ _ _ ___ 
|   | |  _| | . | . | '_| | | . |
|_|_|_|_| |_|___|___|_,_|___|  _|
Author: Gameye98 2024/10/16 |_|  
"""

def hlrlookup(phoneNum):
    print(banner)
    # Filter Phone Number
    phoneNum = phoneNum.replace(" ","")
    phoneNum = phoneNum.replace("-","")
    if phoneNum.startswith("+"):
        phoneNum = phoneNum[1:]
    if phoneNum.startswith("62"):
        phoneNum = "0"+phoneNum[2:]
    hlrquery = "select operator_name,location as lokasi from Hlr a, Operator b where a.id_operator=b._id and prefix=substr('" + phoneNum + "',1,length(prefix)) order by length(prefix) desc limit 1;"
    info = db.execute(hlrquery).fetchall()
    db.close()
    if len(info) > 0:
        print(f"Operator: {info[0][0]}")
        print(f"HLR     : {info[0][1]}, Indonesia")
        return
    print("No result","txt")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: hlrlookup.py 08xxx..")
    else:
        hlrlookup(sys.argv[1])
