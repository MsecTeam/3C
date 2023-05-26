go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
cd /home/kali/go/bin
sudo mv subfinder /usr/bin/
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
cd /home/kali/go/bin
sudo mv httpx /usr/bin/
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
cd /home/kali/go/bin
sudo mv nuclei /usr/bin/
figlet Done