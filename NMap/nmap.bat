nmap -sS -A 172.31.1.1/24
pause 
echo "Déterminez si le serveur distant est accessible."
echo "Déterminez si le serveur distant est accessible." >> Analyse.txt
nmap -sn cisco.com
nmap -sn cisco.com >> Analyse.txt

echo "Test V4"
echo "Test V4" >> Analyse.txt
echo "Organismes principaux d'Internet"
echo "Organismes principaux d'Internet" >> Analyse.txt
nmap -p 80,443 www.afrinic.net www.apnic.net www.ripe.net www.lacnic.net www.arin.net >> Analyse.txt

echo "Test V6"
echo "Test V6" >> Analyse.txt
nmap -6 -p 80,443 www.afrinic.net www.apnic.net www.ripe.net www.lacnic.net www.arin.net >> Analyse.txt

echo "Suivre une route vers un serveur distant à l’aide de la commande Tracert"
echo "Suivre une route vers un serveur distant à l’aide de la commande Tracert" >> Analyse.txt
nmap --traceroute www.cisco.com www.peugeot.fr www.sfr.fr www.cisco.fr google.com >> Analyse.txt

echo "Effectuer un scan de ports"
echo "Effectuer un scan de ports" >> Analyse.txt
nmap -p 1-1000 cisco.com >> Analyse.txt

echo "Découvrir les services en cours d'exécution"
echo "Découvrir les services en cours d'exécution" >> Analyse.txt
nmap -sV cisco.com >> Analyse.txt

echo "Identifier le système d'exploitation"
echo "Identifier le système d'exploitation" >> Analyse.txt
nmap -O cisco.com >> Analyse.txt
