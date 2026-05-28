ip = input("Enter an IP address:")
dot_position = ip.find('.')
first_octet = int(ip[0:dot_position])
print("\nIP address:", ip)                                
print("first octet:" , first_octet)
if first_octet == 10:
    print("classification: private (Class A - 10.0.0.0 to 10.255.255.255l;)")
elif first_octet ==192:
    print("classification: private (class C - 192.168.0.0 to 192.168.255.255)")
elif first_octet == 172:
    print("classification: possibly private (172.16.0.0 to 172.31.255.255)")
else:
    print("classification: public Ip address")
    
