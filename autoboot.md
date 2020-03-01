# This is an example of starting a systemd object detection service on boot on the Coral Dev Board.



### 1) create a file call detects.service with the following contents:

```
[Unit]
Description=systemd auto face detection service
After=weston.target

[Service]
PAMName=login
Type=simple
User=mendel
WorkingDirectory=/home/mendel
Environment=DISPLAY=:0
ExecStart=/bin/bash /usr/bin/detect_service.sh
Restart=always

[Install]
WantedBy=multi-user.target
```

### 2) mv the file /lib/systemd/system/detects.service

```$ sudo mv detects.service /lib/systemd/system/detects.service```

### 3) create a file call detect_service.sh with the following content

```edgetpu_detect --model fullpath/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite --label fullpath/coco_labels.txt```

### 4) make it executable and mv it to /usr/bin

``` $ sudo chmod u+x detect_service.sh```
``` $ sudo mv detect_service.sh /usr/bin```

### 5) enable the service with systemctl

``` $ sudo systemctl enable detects.service```
