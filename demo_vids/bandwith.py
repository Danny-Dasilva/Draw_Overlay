

import time

def get_bytes(t, iface='wlan0'):
    with open('/sys/class/net/' + iface + '/statistics/' + t + '_bytes', 'r') as f:
        data = f.read();
        return int(data)

while(True):
    tx1 = get_bytes('tx')
    rx1 = get_bytes('rx')

    time.sleep(.01)

    tx2 = get_bytes('tx')
    rx2 = get_bytes('rx')

    tx_speed = round((tx2 - tx1)/10000.0, 4)
    rx_speed = round((rx2 - rx1)/10000.0, 4)

    print(f"TX: {tx_speed}fMbps  RX: {rx_speed}fMbps")
