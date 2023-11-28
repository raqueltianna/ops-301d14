# Reading 2: Network Scanning with NMAP 

### Article Links: 
- [What is a Port Scanner and How Does it Work?](https://www.varonis.com/blog/port-scanning-techniques)
- [Common Ports](https://www.professormesser.com/network-plus/n10-008/n10-008-video/common-ports-n10-008/)

## What is a Port Scanner and How Does it Work?
  
### What is a port? Describe it with an analogy that would help a family member understand.
  - A port is a computer program that checks network ports for one of three possible statuses - open, closed, or filtered. The way that I would describe this to my family member is to think of a post office. The entirity of the post office is your computer but each personal P.O. box is a port. Each P.O. box is designated to a certain person just like a port. You wouldn't want your mail being placed in someone else's mailbox and ports are the same way, where they make sure that the right type of data goes to the right place. 
### What does a port scanner send to a port to check the current status?
  - The port scanner sends a packet of network data to a port to check the current status. 
### When a port scanner sends a request to connect, what are the three possible responses? Describe them.
  - Open: An "open" response means that there is a service, software, application, etc that is actively listening/using that port. This means that the port allows communication and the scanner can connect.
  - Closed: If the port is "closed" that means there's nothing active services on that port.
  - Filtered: This means that the target is blocking or not responding to the connection request. This also means that the port doesn't specify if it opened or closed but that the scanner couldn't determine the status. 
### What is the difference between TCP and UDP?
- TCP is a connection-oriented protcol while UDP is a connectionless protocol. UDP doesn't have any error checking unlike TCP but it tends to be faster.

## Common Ports

### List and describe the ports used for the following:
  - Telnet: Port 23, it is commonly used for remote terminal connections.
  - SSH: Port 22, it provides encrypted communication for secure remote access.
  - DNS: Port 53, it translates domain names into IP address. 
  - SMTP: Port 25, used for sending emails between servers. 
  - HTTP: Port 80, used for transmitting web pages and other web based content. 
  - HTTPS: Port 443, used for encrypting data transmitted between a browser and the website for a secure connection.
  - RDP: Port 3389, it is commonly used for remote desktop connections in Windows environment. 
  - Ping: Ping doesn't use a specific port. It uses ICMP. it is used to test the reachability on an IP.

## Things I want to know more about: 
  - Throughout the entirity of the course we have talked about ports so I think I want to dig a litle deeper and become even more comfortable with different ports. 
