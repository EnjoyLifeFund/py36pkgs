## This file is part of Scapy
## See http://www.secdev.org/projects/scapy for more informations
## Copyright (C) Philippe Biondi <phil@secdev.org>
## This program is published under a GPLv2 license

"""
Global variables and functions for handling external data sets.
"""

import os, sys, re, time
from scapy.dadict import DADict
from scapy.error import log_loading

############
## Consts ##
############

ETHER_ANY = b"\x00"*6
ETHER_BROADCAST = b"\xff"*6

ETH_P_ALL = 3
ETH_P_IP = 0x800
ETH_P_ARP = 0x806
ETH_P_IPV6 = 0x86dd

# From net/if_arp.h
ARPHDR_ETHER = 1
ARPHDR_METRICOM = 23
ARPHDR_PPP = 512
ARPHDR_LOOPBACK = 772
ARPHDR_TUN = 65534

# From pcap/dlt.h
DLT_NULL = 0
DLT_PPP = 9
DLT_PPP_SERIAL = 50
DLT_PPP_ETHER = 51
DLT_RAW = 101
DLT_IPV4 = 228
DLT_IPV6 = 229

# From net/ipv6.h on Linux (+ Additions)
IPV6_ADDR_UNICAST     = 0x01
IPV6_ADDR_MULTICAST   = 0x02
IPV6_ADDR_CAST_MASK   = 0x0F
IPV6_ADDR_LOOPBACK    = 0x10
IPV6_ADDR_GLOBAL      = 0x00
IPV6_ADDR_LINKLOCAL   = 0x20
IPV6_ADDR_SITELOCAL   = 0x40     # deprecated since Sept. 2004 by RFC 3879
IPV6_ADDR_SCOPE_MASK  = 0xF0
#IPV6_ADDR_COMPATv4   = 0x80     # deprecated; i.e. ::/96
#IPV6_ADDR_MAPPED     = 0x1000   # i.e.; ::ffff:0.0.0.0/96
IPV6_ADDR_6TO4        = 0x0100   # Added to have more specific info (should be 0x0101 ?)
IPV6_ADDR_UNSPECIFIED = 0x10000


# On windows, epoch is 01/02/1970 at 00:00
EPOCH = time.mktime((1970, 1, 2, 0, 0, 0, 3, 1, 0))-86400

MTU = 0xffff # a.k.a give me all you have

WINDOWS=sys.platform.startswith("win")

 
# file parsing to get some values :

def load_protocols(filename):
    spaces = re.compile(b"[ \t]+|\n")
    dct = DADict(_name=filename)
    try:
        for l in open(filename, "rb"):
            try:
                shrp = l.find(b"#")
                if  shrp >= 0:
                    l = l[:shrp]
                l = l.strip()
                if not l:
                    continue
                lt = tuple(re.split(spaces, l))
                if len(lt) < 2 or not lt[0]:
                    continue
                dct[lt[0]] = int(lt[1])
            except Exception as e:
                log_loading.info("Couldn't parse file [%s]: line [%r] (%s)" % (filename,l,e))
    except IOError:
        log_loading.info("Can't open %s file" % filename)
    return dct

def load_ethertypes(filename):
    spaces = re.compile(b"[ \t]+|\n")
    dct = DADict(_name=filename)
    try:
        f=open(filename, "rb")
        for l in f:
            try:
                shrp = l.find(b"#")
                if  shrp >= 0:
                    l = l[:shrp]
                l = l.strip()
                if not l:
                    continue
                lt = tuple(re.split(spaces, l))
                if len(lt) < 2 or not lt[0]:
                    continue
                dct[lt[0]] = int(lt[1], 16)
            except Exception as e:
                log_loading.info("Couldn't parse file [%s]: line [%r] (%s)" % (filename,l,e))
        f.close()
    except IOError as msg:
        pass
    return dct

def load_services(filename):
    spaces = re.compile(b"[ \t]+|\n")
    tdct=DADict(_name="%s-tcp"%filename)
    udct=DADict(_name="%s-udp"%filename)
    try:
        f=open(filename, "rb")
        for l in f:
            try:
                shrp = l.find(b"#")
                if  shrp >= 0:
                    l = l[:shrp]
                l = l.strip()
                if not l:
                    continue
                lt = tuple(re.split(spaces, l))
                if len(lt) < 2 or not lt[0]:
                    continue
                if lt[1].endswith(b"/tcp"):
                    tdct[lt[0]] = int(lt[1].split(b'/')[0])
                elif lt[1].endswith(b"/udp"):
                    udct[lt[0]] = int(lt[1].split(b'/')[0])
            except Exception as e:
                log_loading.warning("Couldn't file [%s]: line [%r] (%s)" % (filename,l,e))
        f.close()
    except IOError:
        log_loading.info("Can't open /etc/services file")
    return tdct,udct


class ManufDA(DADict):
    def fixname(self, val):
        return val
    def _get_manuf_couple(self, mac):
        oui = ":".join(mac.split(":")[:3]).upper()
        return self.__dict__.get(oui,(mac,mac))
    def _get_manuf(self, mac):
        return self._get_manuf_couple(mac)[1]
    def _get_short_manuf(self, mac):
        return self._get_manuf_couple(mac)[0]
    def _resolve_MAC(self, mac):
        oui = ":".join(mac.split(":")[:3]).upper()
        if oui in self:
            return ":".join([self[oui][0]]+ mac.split(":")[3:])
        return mac
    def __repr__(self):
        return "\n".join("<%s %s, %s>" % (i[0], i[1][0], i[1][1]) for i in list(self.__dict__.items()))
        
        

def load_manuf(filename):
    try:
        manufdb=ManufDA(_name=filename)
        for l in open(filename, "rb"):
            try:
                l = l.strip()
                if not l or l.startswith(b"#"):
                    continue
                oui,shrt=l.split()[:2]
                i = l.find(b"#")
                if i < 0:
                    lng=shrt
                else:
                    lng = l[i+2:]
                manufdb[oui] = shrt, lng
            except Exception as e:
                log_loading.warning("Couldn't parse one line from [%s] [%r] (%s)" % (filename, l, e))
    except IOError:
        log_loading.warning("Couldn't open [%s] file" % filename)
        return ""
    return manufdb
    


if WINDOWS:
    ETHER_TYPES=load_ethertypes("ethertypes")
    IP_PROTOS=load_protocols(os.environ["SystemRoot"]+"\system32\drivers\etc\protocol")
    TCP_SERVICES,UDP_SERVICES=load_services(os.environ["SystemRoot"] + "\system32\drivers\etc\services")
    # Default value, will be updated by arch.windows
    MANUFDB = load_manuf(os.environ["ProgramFiles"] + "\\wireshark\\manuf")
else:
    IP_PROTOS=load_protocols("/etc/protocols")
    ETHER_TYPES=load_ethertypes("/etc/ethertypes")
    TCP_SERVICES,UDP_SERVICES=load_services("/etc/services")
    MANUFDB = load_manuf("/usr/share/wireshark/manuf")



#####################
## knowledge bases ##
#####################

class KnowledgeBase:
    def __init__(self, filename):
        self.filename = filename
        self.base = None

    def lazy_init(self):
        self.base = ""

    def reload(self, filename = None):
        if filename is not None:
            self.filename = filename
        oldbase = self.base
        self.base = None
        self.lazy_init()
        if self.base is None:
            self.base = oldbase

    def get_base(self):
        if self.base is None:
            self.lazy_init()
        return self.base
    

