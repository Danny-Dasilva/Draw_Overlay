import subprocess
import csv

process = subprocess.Popen(['nmcli', 'dev', 'wifi'], stdout=subprocess.PIPE)
#process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)

stdout, stderr = process.communicate()
#print(stdout.decode('utf-8').splitlines())
reader = csv.DictReader(stdout.decode('utf-8').splitlines(),
                        delimiter=' ', skipinitialspace=True,
                        fieldnames=['SSID', 'MODE',
                                    'CHAN', 'RATENUM', 'RATE',
                                    'SIGNAL', 'BARS', 'SECURITY'])

for row in reader:
    print(row['SSID'], row['MODE'],row['CHAN'], row['RATENUM'], row['RATE'], row['SIGNAL'], row['BARS'], row['SECURITY'])