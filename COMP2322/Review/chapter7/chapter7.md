# Chapter 7 - Wireless & Mobile Networks
## Intro
- '# mobile phone > # of wired phone
- '# wireless internet connected device = # wireline internet CD
- laptop/phone
- 2 challenge: wireless & mobility

- elements
  - network infrastructure
  - wireless hosts(not mobility)
  - base station(connect to wire network)
  - wireless communication link(mobile): base station, cell tower, wifi access point
- coverage area
  - short range wireless network: 
    - Wireless personal area network, Wireless Local area network
    - limited area: personal - close area; local: corporate building, school...
    - industrial, scientific, medical usage(2.4Ghz)
  - long range: 
    - Wireless wide area network, cellular network(wireless metropolitan area network)
    - span large geographical area
    - satellite network provide connection across world
    - different companies(service product)

- architecture
  - infrastructure: related to base station
  - ad hoc network: no base station, only transmit to other node within link coverage
    - single hop vs multiple hop

## Wireless Links, characteristics.
- characteristics
  - decreased signal strength(path loss)
  - interference from other source(2.4GHz) shared by other devices
  - multipath propagation:radio signal reflects off objects ground
  - communication complicated
  - hidden terminal problem(BA hear each other; BC hear each other; AC can not hear each other; A,C unaware of interference at B)
  - signal attenuation - signal strength(BA hear each other; BC hear each other;AC can not hear each other => cause interference at B)

### CDMA(Code Division Multiple Access)
- unique code for each user; own chipping seq. to encode data
- make n users to coexist & transmit with min interference
- encoded signal = original data * chipping seq.
- decoding: inner-product of encoded signal & chipping sequence

## IEEE 802.11 wireless LANs(Wi-Fi)
- WLAN architecture
  - internet-hub-BSS(basic service set = station + access point)
- station: must associate with AP
  - scan channel, listen for beacon frame contain AP's name(SSID) and MAC addr
  - select AP to associate
  - perform authentication
  - run DHCP get IP addr
- passive scanning
- active scanning
- multiple access
- CSMA/CA: MAC Protocol
  - sender
  - receiver
- MACA
- 802.11 frame: addressing
  - frame control; duration(of reserved trasmission time); addr 1(MAC of wireless station/AP receive); addr 2(MAC of wireless station/AP transmit); addr 3(MAC of router interface to which AP attached); seq control(frame seq#); addr 4(use only in ad hoc mode); payload; CRC
  - frame type
## Cellular networks
- Components of cellular network architecture
  - cell: base station, mobile station, air-interface
  - MSC: connect cell to wired tel. net.; manage call setup; handle mobility
- 2 tech. for sharing MS2BS radio spectrum
  - combined FDMA/TDMA: divide spectrum in freq. channel (divide into time slot)
  - CDMA: code division multiple access
- 2G(voice) network architecture
  - base station system(mobile swiching center + base station controller); gateway MSC; Public tele. switch network
- 3G(voice+data)
  - radio access network(voice interface); core network(MSC,Serving GPRS support Node + Gateway MSC, Gateway GPRS support Node); public tele. network + public internet
- 4G LTE(no seperation voice & data IP core to gateway)

