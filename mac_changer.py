import re, subprocess
from optparse import OptionParser

def mac_changer(interface, new_mac):
    subprocess.run(['ifconfig', interface, 'down'])
    subprocess.run(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.run(['ifconfig', interface, 'up'])

def taking_arguments():
    parser = OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Enter interface name of which you want to change mac_address (eg: -i eth0)')
    parser.add_option('-m', '--mac', dest='new_mac', help='Enter new mac (eg: -m 00:11:22:33:44:55)')
    (options, args) = parser.parse_args()
    if(options.interface and options.new_mac):
        return parser.parse_args()
    elif(not options.interface):
        print('Oops you forgot to mention -i agrument, use -h for help')
        exit()
    elif(not options.new_mac):
        print('Oops you forgot to mention -m agrument, use -h for help')
        exit()
    else:
        print('You messed up, use -h for help')
        exit()

def ensuring_mac(interface, new_mac):
    new_ifconf = subprocess.getoutput('ifconfig '+interface)
    return re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', new_ifconf)

(options, args) = taking_arguments()
mac_changer(options.interface, options.new_mac)
ensured_mac = ensuring_mac(options.interface, options.new_mac)
if(ensured_mac.group(0) == options.new_mac):
    print('Mac Address changed sucessfully to: '+str(ensured_mac.group(0)))
else:
    print('Something went wrong!!')
