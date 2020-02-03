#!/bin/bash
echo "Start building gitadmin..."
echo "Enter sudo password for install requereiments"
sudo apt install gnome-terminal
touch gtamd
echo "#!/bin/bash" > gtamd
echo "gnome-terminal -x sh -c 'gt.py' $1; exec bash" >> gtamd
sudo chmod 777 gtamd
echo "Executables created and moving..."
sudo mv gtamd /usr/local/bin
sudo cp gt.py /usr/local/bin
sudo chmod 777 /usr/local/bin/gt.py
echo "Done!, Execute 'gtamd' for execute git admin"
