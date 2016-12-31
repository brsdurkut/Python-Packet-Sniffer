from general import *
from networking.ethernet import Ethernet
from networking.ipv4 import IPv4
from networking.icmp import ICMP
from networking.tcp import TCP
from networking.udp import UDP


class Packet(object):
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.packet = {}
        self.summary = {"src_ip":None, "src_port":None, "dst_ip":None,
                "dst_port":None, "flg":None}

        tmp = Ethernet(self.raw_data)
        self.packet["Ethernet Frame"] = {
                                        "Source MAC": tmp.src_mac,
                                        "Destination MAC": tmp.dest_mac,
                                        "Protocol Type": tmp.proto
                                        }

        if tmp.proto == 8:
            tmp = IPv4(tmp.data)
            self.packet["IPv4 Packet"] = {
                                            "Version":tmp.version,
                                            "Header Length":tmp.header_length,
                                            "TTL":tmp.ttl,
                                            "Protocol":tmp.proto,
                                            "Source IP":tmp.src,
                                            "Destination IP":tmp.target
                                            }
            self.summary["src_ip"] = tmp.src
            self.summary["dst_ip"] = tmp.target
            if tmp.proto == 1:
                tmp = ICMP(tmp.data)
                self.packet["ICMP Packet"] = {
                                                "Type":tmp.type,
                                                "Code":tmp.code,
                                                "Checksum":tmp.checksum,
                                                "Data":format_multi_line("\t", tmp.data)
                                                }
            elif tmp.proto == 6:
                tmp = TCP(tmp.data)
                self.packet["TCP Segment"] = {
                                                "Source Port":tmp.src_port,
                                                "Destination Port":tmp.dest_port,
                                                "Sequence":tmp.sequence,
                                                "Acknowledgment":tmp.acknowledgment,
                                                "Flags": {
                                                            "URG":tmp.flag_urg,
                                                            "ACK":tmp.flag_ack,
                                                            "PSH":tmp.flag_psh,
                                                            "RST":tmp.flag_rst,
                                                            "SYN":tmp.flag_syn,
                                                            "FIN":tmp.flag_fin
                                                            }
                                                }
                flg = []
                for k,v in self.packet["TCP Segment"]["Flags"].items():
                    if v == 1:
                        flg.append(k)
                flg = ",".join(flg)
                self.summary["src_port"] = tmp.src_port
                self.summary["dst_port"] = tmp.dest_port
                self.summary["flg"] = flg

            elif tmp.proto == 17:
                tmp = UDP(tmp.data)
                self.packet["UDP Segment"] = {
                                                "Source Port":tmp.src_port,
                                                "Destination Port":tmp.dest_port,
                                                "Length":tmp.size
                                                }
                self.summary["src_port"] = tmp.src_port
                self.summary["dst_port"] = tmp.dest_port

            else:
                self.packet["Other IPv4 Data"] = format_multi_line("\t", tmp.data)
        else:
            self.packet["Ethernet Data"] = format_multi_line("\t", tmp.data)

    def get_summary(self):
        return self.summary

    def get_str(self):
        return str(self.summary)





