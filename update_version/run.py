import subprocess
import csv

import os

def search_wifi():
    process = subprocess.Popen(['nmcli', 'dev', 'wifi'], stdout=subprocess.PIPE)
    #process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)

    stdout, stderr = process.communicate()
    #print(stdout.decode('utf-8').splitlines())
    reader = csv.DictReader(stdout.decode('utf-8').splitlines(),
                            delimiter=' ', skipinitialspace=True,
                            fieldnames=['SSID', 'MODE',
                                        'CHAN', 'RATENUM', 'RATE',
                                        'SIGNAL', 'BARS', 'SECURITY'])

    wifi_list = {}
    connected = {False, False}
    for row in reader:
        if row['SSID'] != '--':
            
            if row['SSID'] == '*':
                print("connected to ", row['MODE'])
                connected = {True : row['MODE']}
            else:
                ssid = row['SSID']
                security = row['SECURITY']
                wifi_list[ssid] = security
    del wifi_list['IN-USE']
    return connected, wifi_list
# # os.system('nmcli ddevice wifi connect my_wifi password <password>')




def search_connected():
    process = subprocess.Popen(['nmcli', 'd'], stdout=subprocess.PIPE)
    #process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)

    stdout, stderr = process.communicate()
    #print(stdout.decode('utf-8').splitlines())
    reader = csv.DictReader(stdout.decode('utf-8').splitlines(),
                            delimiter=' ', skipinitialspace=True,
                            fieldnames=['NAME', 'UUID',
                                        'TYPE', 'DEVICE',])

    wifi_list = {}
    connected = {False, False}
    for row in reader:
        if row ['TYPE'] == 'wifi':
            uuid = row['UUID']
            name = row['NAME']
            wifi_list[name] = connection
    return connected, wifi_list


#  nmcli d up <name>
def disconnect(wifi_name):
    os.system(f'nmcli con down id {wifi_name}')


def connect(name, password=None):
    if password == None:
        try:
            os.system(f'nmcli d up {name}')
        except:
            print("wrror")
def search():
    pass

def read_network_list():
    pass
def save_network_list():
    pass
def read_network():
    #nmcli d
    pass
def ask_password():
    #socket promt for password
    pass

connect, wifi_list = search_wifi()
print(connect, wifi_list)
# disconnect(connect[True])