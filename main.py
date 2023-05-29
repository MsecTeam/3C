# Create By RedSec
# Tools Scanning By projectdiscovery.io
# Rec Tools Silakan Tapi Berikan Siapa Inspiration

import os
import sys
import time
import subprocess

os.system("clear")

print("""\033[1;32m
██████╗      ██████╗ ██████╗ ███╗   ███╗██████╗  ██████╗ 
╚════██╗    ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔═══██╗
 █████╔╝    ██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║
 ╚═══██╗    ██║     ██║   ██║██║╚██╔╝██║██╔══██╗██║   ██║
██████╔╝    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝╚██████╔╝
╚═════╝      ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝  ╚═════╝ 

- 3 Combo -
- Automated Scanner -
- Tools Install By projectdiscovery.io -
- Create By ./RedSec A K E Denis -
- MsecTeam -
""")

pilihan = input ("Input Your Domain => ")
pilihan2 = input ("Input Your Output => ")
print("")
# Menjalankan perintah 'pwd' dan mendapatkan outputnya
output = subprocess.check_output('pwd', shell=True)

# Mengubah output menjadi string dan menghapus karakter newline di akhir
current_directory = output.decode().rstrip('\n')

# Mencetak hasilnya
print(f"Your File: {current_directory}/{pilihan2}")
print("")
pilihan3 = input ("Input Patch => ")
print("")
print("Prosessing....")
time.sleep(2)
print("""
███████╗██╗   ██╗██████╗ ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██║   ██║██╔══██╗██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████╗██║   ██║██████╔╝█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
╚════██║██║   ██║██╔══██╗██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
███████║╚██████╔╝██████╔╝██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
- Waitting... -
""")
# subfinder
os.system(f"subfinder -d {pilihan} -o {pilihan2} -silent")
print("""
██╗  ██╗████████╗████████╗██████╗ ██╗  ██╗
██║  ██║╚══██╔══╝╚══██╔══╝██╔══██╗╚██╗██╔╝
███████║   ██║      ██║   ██████╔╝ ╚███╔╝ 
██╔══██║   ██║      ██║   ██╔═══╝  ██╔██╗ 
██║  ██║   ██║      ██║   ██║     ██╔╝ ██╗
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝     ╚═╝  ╚═╝
- Waitting... -
""")
# httpx
os.system(f"httpx -list {pilihan3} -silent -o {pilihan2}")
print("""
███╗   ██╗██╗   ██╗ ██████╗██╗     ███████╗██╗
████╗  ██║██║   ██║██╔════╝██║     ██╔════╝██║
██╔██╗ ██║██║   ██║██║     ██║     █████╗  ██║
██║╚██╗██║██║   ██║██║     ██║     ██╔══╝  ██║
██║ ╚████║╚██████╔╝╚██████╗███████╗███████╗██║
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚══════╝╚══════╝╚═╝
- Waitting... -
""")
# nuclei
os.system(f"nuclei -l {pilihan3} -silent -attack-type pitchfork -severity medium, high, critical, unknown -o {pilihan2}")
print("""
██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██╔═══██╗████╗  ██║██╔════╝
██║  ██║██║   ██║██╔██╗ ██║█████╗  
██║  ██║██║   ██║██║╚██╗██║██╔══╝  
██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                   
Thanks For Use My Tools
Thanks For projectdiscovery.io
""")
