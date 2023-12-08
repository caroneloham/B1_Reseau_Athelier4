echo Determinez si le serveur distant est accessible.
ping -4 cisco.com
ping -6 cisco.com

ping -4 www.afrinic.net
ping -4 www.apnic.net
ping -4 www.ripe.net
ping -4 www.lacnic.net
ping -4 www.arin.net

ping -6 www.afrinic.net
ping -6 www.apnic.net
ping -6 www.ripe.net
ping -6 www.lacnic.net
ping -6 www.arin.net

Echo Suivre une route vers un serveur distant à l’aide de la commande Tracert
tracert www.cisco.com
tracert peugeot.fr
tracert sfr.fr
tracert cisco.fr
tracert -h 5 google.com

curl -s http://ping.eu/
curl -s http://www.subnetonline.com/pages/network-tools/online-tracepath.php



pathping www.root-me.org

echo affichier le fichier host 
type %windir%\system32\drivers\etc\hosts