## RFTool

### Prerequisites
1. Radio deviece (HackRF,...)
2. GNU Radio
3. gr-osmosdr
4. scapy

### Usage
#### constant_jammer
```sh
$ python constant_jammer.py
```

#### spectrum_reader
```sh
$ python spectrum_reader.py
```

#### wifi frame receiver
```sh
$ python hackrf_wifi_receiver.py
```

#### deceptive_jammer
Using beacon_frame\_generator.py to generate fake beacon frame.
```sh
$ python beacon_frame_generator.py
```
Using hackrf_frame\_emitter.py to emit wifi frame.
```sh
$ python hackrf_frame_emitter.py
```
