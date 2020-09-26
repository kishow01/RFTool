## RFTool

### Prerequisites
1. Radio deviece (HackRF,...)
2. GNU Radio
3. gr-osmosdr
<<<<<<< HEAD
4. gr-foo
5. gr-ieee802-11
=======
4. scapy
>>>>>>> 9b2d21a5bcd512e8408aa132cdfa1678d123620e

### Usage
#### constant_jammer
```sh
$ gnuradio-companion GRC/constant_Jammer.grc
```

#### wifi frame recorder
```sh
$ gnuradio-companion GRC/recorder.grc
```

#### deceptive_jammer
```sh
$ gnuradio-companion GRC/Deceptive_Jammer.grc
```

### Troubleshooting
In Deceptive_Jammer.grc and recorder.grc. File sink path and File source path need to be corrected.
