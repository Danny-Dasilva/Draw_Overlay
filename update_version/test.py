import wifi
import os

def Search():
    wifilist = []

    cells = wifi.Cell.all('wlan0')

    for cell in cells:
        wifilist.append(cell)

    return wifilist

if __name__ == '__main__':
    print( Search())
    
   # os.system('nmcli ddevice wifi connect my_wifi password <password>')
  # "nmcli d"
  #if in list nmcli connection

  # connect to previous:
#  nmcli d up <name>