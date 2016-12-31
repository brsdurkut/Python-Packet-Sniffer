import socket
import _thread
import traceback
from datetime import datetime
import sys
import time
from networking.packet import Packet


class Sniffer(object):
    def __init__(self, rule):
        self.rule = rule
        self.rule_list = []
        self.packet_list = []
        self.running = False
        self.paused = False

    def get_str(self, data):
        return str(data["details"])

    def add_packet(self, packet):
        try:
            packet_item = {
                    "time":datetime.now(), 
                    "details":packet }

            self.packet_list.append(packet_item)
            return self.packet_list
        except:
            traceback.print_exc(limit=1, file=sys.stdout)

    def clear_list(self):
        self.packet_list = []
        return self.packet_list

    def check_packet(self, packet):
        try:
            p = packet.get_summary()
            for r in self.rule_list:
                count = 0
                for k in r.keys():
                    if k != "id" and r[k] != "ALL":
                        count += 1
                print(count)
                for k,v in r.items():
                    if k == "id" or r[k] == "ALL":
                        continue
                    if p[k] == v:
                        count -= 1
                if count == 0:
                    return True
            return False
        except:
            traceback.print_exc(limit=1, file=sys.stdout)

    def start(self, sgnl):
        if self.running == True:
            self.stop()
        self.running = True
        _thread.start_new_thread(self.run, (sgnl,))
        print("started")

    def stop(self):
        self.running = False
        self.paused = False
        self.clear_list = []
        print("stopped")

    def run(self, signl):
        time.sleep(1)

        self.rule_list = self.rule._get_rules()
        self.running = True
        while self.running:
            if self.paused == False:
                conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
                raw_data, addr = conn.recvfrom(65535)
                pckt = Packet(raw_data)
                if self.check_packet(pckt):
                    self.add_packet(pckt)
                    signl.speakNumber.emit(10)
                    print(pckt)
            else:
                break
        else:
            self.stop()
        print("run_func stopped")

if __name__ == "__main__":
    from rules.rule import Rule
    import time
    rule = Rule()
    rule._load("data/rules")
    sniffer = Sniffer(rule)
    sniffer.start()
    time.sleep(5)
    sniffer.stop()
    print([p["details"].get_summary() for p in sniffer.packet_list])
    print(rule._get_rules())

