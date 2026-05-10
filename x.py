import nmap;import time;import random;from packaging import version
END = '\033[0m'

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

# Стили
BOLD = '\033[1m'       # Жирный
UNDERLINE = '\033[4m'  # Подчеркнуты
def start_now():
    print(f'''{RED}
------------------------
________________________________________
______________888888888888____________________
_____________8888888888888888888__________________
__________18888888888888888888888888______________
________88888888888888888888888888888__8__________
_______888888888888-88888888-888888888888_________
_______88888888888888888888888888______888________
______88888888888888888888888888888888___86_______
_______8888888888888____88888888865888888_8_______
_____8_8888888_8888881__88888___________88________
_____88________8888888888888_____________8________
______888____8888__888:8886_______________8_______
________8:_8888__________88_______________88______
_____8__58_88____________8888____________888888___
______8__888_____________:8_888_______688888888___
__________88____________88____:8888888888888888___
___________8__________:888______8888888____88_____
____________8________888888______8888____________
____________888888888888888___18888888___________
-------------------------------------------------------------------------------------------------------
    {END}''')

start_now()

#sudo python3 x.py




ip_1q = [
    178, 185, 46, 95,   # СНГ 
    212, 213, 80, 77,   # Европа/РФ  
    109, 188,           
    82, 91, 101,         
    193, 194, 195,       
    45, 103,    
    104, 107,  
    31, 37,     
    146, 149,   
]


def random_ip():
    global Q
    q1=random.choice(ip_1q)
    q2 = random.randint(0, 255)
    q3 = random.randint(0, 255)
    q4= random.randint(0, 255)
    Q = f'{q1}.{q2}.{q3}.{q4}'
    print(Q)



def scan_nm():
    global nm
    nm = nmap.PortScanner()
    nm.scan(hosts=Q, arguments='-Pn -sV -p  21,22,23,80,135,137,139,445,554,1154,3389,5900,5901,5902 --open --reason --host-timeout 30s ')
    if Q in nm.all_hosts():
        status = nm[f'{Q}'].state() 
        print(F'{GREEN}[*]{END}')
        if status == 'up':
            print(f'🚀{GREEN}[+] ip {Q} OPEN{END}🚀')
            port_c = nm[Q].all_tcp()
            print(port_c)
            if len(port_c) > 0:
                print(f'🎯{BLUE}[+|?]sheck baner and soft{END}🎯')
                for port in port_c:  
                    service = nm[Q]['tcp'][port]['name']
                    product = nm[Q]['tcp'][port]['product']
                    version = nm[Q]['tcp'][port]['version']
                    print(F'🔥{CYAN}[++++] Port: {port}\n  {service} | {product} {version}{END}🔥')
                    with open("results.txt", "a") as file:
                        file.write(f"ip:{Q}\n port:{port}\n {service}|||{product} {version}\n") 

                     
        else:       

            
            print(f'💀{RED}[-]ip {Q}CLOSE OR F{END}💀')

    else:
        print(f'{RED}[-]{END}')
     


while True:
    try:
        random_ip()
        scan_nm()
        print(f'{PURPLE}SCAN🤖🔍{END}')
        time.sleep(random.randint(10, 15))
    except nmap.PortScannerError:  
        print(f'{RED}[!]pip istall nmap and sudo apt install nmap,pls')
        break
    except KeyboardInterrupt:
        print(f'{BOLD}[!]{END}')
        break
