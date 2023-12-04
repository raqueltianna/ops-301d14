# Reading 06

### Article Link
[Network Address Translation](https://www.geeksforgeeks.org/network-address-translation-nat/)

## Network Address Translation

### What is the main purpose for implementing NAT on a network?
- The main purpose is to allow multiple devices within a network to share a single public IP address. 
### At what layer of the OSI model does NAT happen?
- It occurs at the Network layer which is layer 3. 
### What happens to packets when NAT runs out of addresses in the pool of available IPs?
- If NAT runs out of addresses the packet will be dropped and an ICMP host unreachable packet to the destination is sent. 
### What disadvantage does using NAT pose for routers?
- Router being a network layer device should not tamper with port numbers which deals with the transport layer but it has to so because of NAT because NAT assigns port numbers to different connections. 

### Things I want to know more about
- I think the main thing that I want to learn more about is more so the connection on why ports are important in this process, I'm slightly confused by that. 

### Additional Resources 
- [Network Address Translation (NAT)](https://www.professormesser.com/professor-messer-archives/n10-007/network-address-translation-3/)
- [Common Network Types](https://www.professormesser.com/professor-messer-archives/n10-007/common-network-types/)
- [IPv4 and IPv6 Addressing](https://www.professormesser.com/professor-messer-archives/n10-007/ipv4-and-ipv6-addressing/)