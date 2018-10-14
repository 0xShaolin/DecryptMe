echo "shellcode setup script!"

echo "python2 ~/decryptme/decryptme.py" > decryptme
chmod +x shellcode

echo "git fetch -f" > update.sh

if uname -a | grep Android > /dev/null 2>&1 #termux
then
	mv decryptme ~/../usr/bin
elif uname -a | grep Darwin > /dev/null 2>&1 #mac os
then
	sudo mv decryptme /usr/local/bin
elif uname -a | grep Linux > /dev/null 2>&1 #linux
then
	sudo mv decryptme /usr/local/bin
else
	echo "architecture not found!"
	exit
fi

echo "use command decryptme to start decrypting!"
