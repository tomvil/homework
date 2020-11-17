# About
A simple program that checks if given ip address is in range of given network.

Requirements are listed in requirements.txt file.

Tested on Python 3.8.5

# Instructions
Network address can be entered with subnet mask and without it. e.g.: 
- 192.168.1.0/24
- 192.168.1.0/255.255.255.0
- 192.168.1.0

In the last example it will be treated as 192.168.1.0/32

IP Address should be provided without subnet mask. e.g.: 
- 192.168.1.1

It also supports IPv6!
