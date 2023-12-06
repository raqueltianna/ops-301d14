# Reading 08: RADIUS Authentication

### Article Link
- [Computer Network - AAA (Authentication, Authorization and Accounting)](https://www.geeksforgeeks.org/computer-network-aaa-authentication-authorization-and-accounting/)
- [RADIUS Concepts](https://archive.is/27Y19)

## Computer Network - AAA (Authentication, Authorization and Accounting)

### Explain each of the three A’s as you would to a non-technical family member. Use an analogy or a story.
- A lot of my friends like to go clubbing so the way that I would describe the three A's to one of them is that for authentication lets say there is a bouncer, I'm going to call him Bob. To get into the club you have to show Bob that you are over 21 by giving him your licenses. Once Bob sees that you are over 21 he will let you into the club. To explain Authorization, once you are inside of the club there is different sections. There is VIP sections, sections that only workers can go in, etc. Who you are determines what section you are in and authorization determines what you are allowed to do or go. To explain Accounting, bartenders keep up with how many drinks each person has had keeping track on who needs to be cut off from having more drinks etc. Accounting is similiar because it keeps a log of activities. 

### What should the administrator do if the ACS server fails to authenticate a user during AAA implementation?
- The administrator should mention using the local database of the device as a backup, in the method list, to implement AAA. 

### What is the role of the NAS in the AAA implementation using an ACS server? Use a diagram.
- The NAS is a server for users but a client for the AAA servers. 
[Diagram](nasaaoverview.drawio)

## Radius Concepts 

### What are the benefits of using RADIUS for authentication and authorization?
- Some benefits of using RADIUS are added security benefits, central point for user and system authentication, secure VPN authentication, among a list of other benefits. 
### What is RADIUS and what does it stand for?
- RADIUS stands for **Remote Authentication Dial-In User Service**. It is a client-server protocol and software that enables remote access servers to communicate with a cerntral server. 
### Research: What encryption algorithms does RADIUS use?
- Radius doesn't specify encryption algorithms, but it often use various protocols like PAP (Password Authentication Protocol) and CHAP (Challenge Handshake Authentication Protocol). The eencryption used depends on the settings that are configured. 



#### Additional Resources 
- [AAA Overview](https://techhub.hpe.com/eginfolib/networking/docs/switches/3100v2/5998-5996s_security_cg/content/450465875.htm)
- [How authentication protocols work](https://networkradius.com/articles/2022/02/20/how-authentication-protocols-work.html)
- [Authentication Methods](https://www.professormesser.com/network-plus/n10-008/n10-008-video/authentication-methods-n10-008/)
- [Defense in Depth](https://www.professormesser.com/network-plus/n10-008/n10-008-video/defense-in-depth-n10-008/)
- [RADIUS and TACACS](https://www.professormesser.com/security-plus/sy0-401/radius-and-tacacs-2/)
- [Kerberos](https://www.professormesser.com/security-plus/sy0-401/kerberos-2/)