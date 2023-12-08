@echo off
echo "Déterminez si le serveur distant est accessible."
echo "Déterminez si le serveur distant est accessible." >> Analyse.txt
ping -4 cisco.com
ping -4 cisco.com >> Analyse.txt
ping -6 cisco.com
ping -6 cisco.com >> Analyse.txt

echo "Test V4"
echo "Test V4" >> Analyse.txt
echo "Organismes principaux d'Internet"
echo "Organismes principaux d'Internet" >> Analyse.txt
ping -4 www.afrinic.net
ping -4 www.afrinic.net >> Analyse.txt
ping -4 www.apnic.net
ping -4 www.apnic.net >> Analyse.txt
ping -4 www.ripe.net
ping -4 www.ripe.net >> Analyse.txt
ping -4 www.lacnic.net
ping -4 www.lacnic.net >> Analyse.txt
ping -4 www.arin.net
ping -4 www.arin.net >> Analyse.txt

echo "Test V6"
echo "Test V6" >> Analyse.txt
ping -6 www.afrinic.net
ping -6 www.afrinic.net >> Analyse.txt
ping -6 www.apnic.net
ping -6 www.apnic.net >> Analyse.txt
ping -6 www.ripe.net
ping -6 www.ripe.net >> Analyse.txt
ping -6 www.lacnic.net
ping -6 www.lacnic.net >> Analyse.txt
ping -6 www.arin.net
ping -6 www.arin.net >> Analyse.txt

echo "Suivre une route vers un serveur distant à l’aide de la commande Tracert"
echo "Suivre une route vers un serveur distant à l’aide de la commande Tracert" >> Analyse.txt
tracert www.cisco.com
tracert www.cisco.com >> Analyse.txt
tracert peugeot.fr
tracert peugeot.fr >> Analyse.txt
tracert sfr.fr
tracert sfr.fr >> Analyse.txt
tracert cisco.fr
tracert cisco.fr >> Analyse.txt
tracert -h 5 google.com
tracert -h 5 google.com >> Analyse.txt

echo "curl -s http://ping.eu/"
echo "curl -s http://ping.eu/" >> Analyse.txt
curl -s http://ping.eu/
curl -s http://ping.eu/ >> Analyse.txt
echo "curl -s http://www.subnetonline.com/pages/network-tools/online-tracepath.php"
echo "curl -s http://www.subnetonline.com/pages/network-tools/online-tracepath.php" >> Analyse.txt
curl -s http://www.subnetonline.com/pages/network-tools/online-tracepath.php
curl -s http://www.subnetonline.com/pages/network-tools/online-tracepath.php >> Analyse.txt
echo "curl -s https://www.root-me.org/"
echo "curl -s https://www.root-me.org/" >> Analyse.txt
curl -s https://www.root-me.org/
curl -s https://www.root-me.org/ >> Analyse.txt

echo "pathping www.root-me.org"
echo "pathping www.root-me.org" >> Analyse.txt
pathping www.root-me.org
pathping www.root-me.org >> Analyse.txt

echo "Afficher le fichier host 172.31.1.76 anissa"
echo "Afficher le fichier host 172.31.1.76 anissa" >> Analyse.txt
ipcontype %windir%\system32\drivers\etc\hosts
ipcontype %windir%\system32\drivers\etc\hosts >> Analyse.txt
ipconfig /displaydns
ipconfig /displaydns >> Analyse.txt
ipconfig /flushdns
ipconfig /flushdns >> Analyse.txt

echo "ARP"
echo "ARP" >> Analyse.txt
arp -a
arp -a >> Analyse.txt
arp -d
arp -s 192.168.1.100 00-aa-11-bb-22-cc
arp -s 192.168.1.100 00-aa-11-bb-22-cc >> Analyse.txt
arp -s 192.168.1.101 11-bb-22-cc-dd-ee
arp -s 192.168.1.101 11-bb-22-cc-dd-ee >> Analyse.txt
arp -s 192.168.1.102 22-cc-dd-ee-ff-00
arp -s 192.168.1.102 22-cc-dd-ee-ff-00 >> Analyse.txt
arp -s 192.168.1.103 33-dd-ee-ff-00-11
arp -s 192.168.1.103 33-dd-ee-ff-00-11 >> Analyse.txt
arp -s 192.168.1.104 44-ee-ff-00-11-22
arp -s 192.168.1.104 44-ee-ff-00-11-22 >> Analyse.txt
arp -a
arp -a >> Analyse.txt

echo "Route"
echo "Route" >> Analyse.txt
route print -4
route print -4 >> Analyse.txt
route print -6
route print -6 >> Analyse.txt

echo "Netsh"
echo "Netsh" >> Analyse.txt
netsh interface ipv4 show interfaces
netsh interface ipv4 show interfaces >> Analyse.txt
netsh interface show interface
netsh interface show interface >> Analyse.txt
netsh interface ipv4 show neighbors
netsh interface ipv4 show neighbors >> Analyse.txt
netsh int ip reset
netsh int ip reset >> Analyse.txt
systeminfo
systeminfo >> Analyse.txt

echo "Netstat:"
echo "Netstat:" >> Analyse.txt
netstat -an | Select-String "TCP" | Select-String "LISTEN"
netstat -an | Select-String "TCP" | Select-String "LISTEN" >> Analyse.txt
netstat -an | Select-String "UDP"
netstat -an | Select-String "UDP" >> Analyse.txt
netstat -e
netstat -e >> Analyse.txt
netstat -s
netstat -s >> Analyse.txt
netstat -b
netstat -b >> Analyse.txt
netstat -o
netstat -o >> Analyse.txt

echo "Net session"
echo "Net session" >> Analyse.txt
Net session
Net session >> Analyse.txt
