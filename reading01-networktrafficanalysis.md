# Reading 1: Network Traffic Analysis with Wireshark

#### Article Links: 
- [Layers of OSI Model](https://www.geeksforgeeks.org/open-systems-interconnection-model-osi/)
- [What Is Wireshark and How Is It Used?](https://www.comptia.org/content/articles/what-is-wireshark-and-how-to-use-it)


## Layers of OSI Mode

### What does “OSI” stand for?
  - OSI stands for "Open System Interconnnection"
### List the 7 layers of the OSI model and what each one is responsible for.
  - The 7 layers of the OSI model are:
    - Physical: this deals with the physical connection between devices such as power plugs and receivers.
    - Data Link: this deals with creating a link between nodes to help ensure error-free transmission of information.
    - Network: this manages transferring of network packets from the source to the destination.
    - Transport: this manages ensuring end-to-end communication by by providing a point-to-point connection,
    - Session: this manages establishing, managing, and terminating sessions between application on different devices.
    - Presentation: this layer is responsible for translating and encrypting data for the application layer.
    - Application: this layer provides network and common web application services to end users and application
### Distinguish which layers are the “hardware layers”, and which layers are the “software layers”. What does that even mean?
  - Hardware layers: Physical, Data Link, Network
  - Software layers: Transport, Session, Presentation, Application.
  - The "hardware layers" are associated with hardware because they deal with the physical aspects of networking like an ethernet cable for example. The "software layers" are associated with software because they involve application-level functions.
### How can the OSI model be used in troubleshooting?
  - The OSI model can be used for troubleshooting because each layer represents a specific aspect so if you have an issue you can use a more systematic approach with it by starting at the lowest level which would be the physical layer (ensuring connections aren't the problem) and then move up from there.

## What is Wireshark and How Is It Used? 

### What is Wireshark?
  - It is an open source network protocol analyzer that allows users to capture data traveling back and forth on a network. 
### What is a packet?
  - A packet is a small unit of data that is transmitted over a network. 
### What 3 high-level things does Wireshark accomplish? How could these be used for nefarious purposes? For benevolent purposes?
 - Packet Capture, Filtering, and Visualization. These could be used nefariously by attackers using it to capture information like login information. It can be used for benevolent purposes by: being used to identify vulnerabilities to attack (such as an DoS attack), trouble shooting network issues, helping a company develop network protocols, along with many other uses.

### Things I want to know more about: 
- During this reading I got the gist of the OSI model but I would like to delve a little bit deeper into it for my own personal knowledge.


### Additional Resources: 
- [Understanding the OSI Model](https://www.professormesser.com/network-plus/n10-008/n10-008-video/understanding-the-osi-model-3/)
- [Data Communication](https://www.professormesser.com/network-plus/n10-008/n10-008-video/data-communication/)
- [Packet, routers, and reliability](https://www.youtube.com/watch?v=aD_yi5VjF78)
