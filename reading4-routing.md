# Reading 4: Routing

### Article Link
[VirtualBox Network Settings Guide](https://www.nakivo.com/blog/virtualbox-network-setting-guide/)

## VirtualBox Network Settings Guide

### Which network mode in VirtualBox can be used to emulate unplugging the Ethernet cable from the network?
- The NAT network mode can be used to emulate unplugging the Ethernet Cable. You can do this by uncheck the "Enable Network Adapter" or change the attached to field to not attached. 
### Which network mode would be best if you wanted to run a server on a VM that could be fully accessible from your physical local area network?
- The best network mode option if you wanted to run a server on a VM would be the Bridged Adapter mode. 
### What are the three options of promiscuous mode and what does each do?
- Three option of promiscuous mode are *Deny*, *Allow VMs*, and *Allow All*. Deny makes it to where any traffic that is not intended to the virtual network adapter of the VM is hidden from the VM. Allow VMs make it to where all traffic is hidden from the VM network adapter except the traffic transmitted to and from other VMs. Allow All makes it to where a VM network adapter can see all incoming and outgoing traffic. 
### What is Port Forwarding?
- Port forwarding is a process that involves capturing traffic directed towards a specific IP address and port, then rerouting that traffic to a different IP address and/or port.

#### Additional Resources
- [Network Topologies](https://www.professormesser.com/network-plus/n10-008/n10-008-video/network-topologies-5/)
- [Routing Technologies](https://www.professormesser.com/network-plus/n10-008/n10-008-video/routing-technologies-n10-008/)
- [Dynamic Routing](https://www.professormesser.com/network-plus/n10-008/n10-008-video/n10-008-dynamic-routing/)
- [Network Switching Overview](https://www.professormesser.com/network-plus/n10-008/n10-008-video/network-switching-overview-n10-008/)
