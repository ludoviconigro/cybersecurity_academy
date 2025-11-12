lancia i comandi 
```bash
sudo apt update
sudo apt install -y libicu-dev
sudo apt install libicu72
sudo apt install libicu72
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb
sudo apt install libssl1.1
sudo apt install libssl3
sudo su
mkdir /opt/covenant
cd /opt/covenant
wget https://dotnet.microsoft.com/download/dotnet/scripts/v1/dotnet-install.sh
chmod +x dotnet-install.sh
./dotnet-install.sh --channel 3.1
export DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1
git clone --recurse-submodules https://github.com/cobbr/Covenant
cd Covenant/Covenant
~/.dotnet/dotnet run
```
dopo che si è avviato il server accedi all'indirizzo 
```bash
https://127.0.0.1:7443
```
Accedi con le credenziali "test" e "password"  
