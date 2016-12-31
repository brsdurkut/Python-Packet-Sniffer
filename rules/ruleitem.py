


class RuleItem(object):
    def __init__(self,
                id_=-1,
                src_ip="",
                src_port="",
                dst_ip="",
                dst_port="",
                flg="",
                load=None):

        if load != None:
            self.id_ = load["id"]
            self.src_ip = load["src_ip"]
            self.src_port = load["src_port"]
            self.dst_ip = load["dst_ip"]
            self.dst_port = load["dst_port"]
            self.flg = load["flg"]
        else:
            self.id_ = id_
            self.src_ip = self.__parse(src_ip)
            self.src_port = self.__parse(src_port)
            self.dst_ip = self.__parse(dst_ip)
            self.dst_port = self.__parse(dst_port)
            self.flg = self.__parse(flg)

    def __str__(self):
        return "{} {} {} {} {}".format(self.src_ip,
                                        self.src_port,
                                        self.dst_ip,
                                        self.dst_port,
                                        self.flg)

    def __parse(self, data):
        return data.upper()

    def _to_dict(self):
        return {
                "id":self.id_,
                "src_ip":self.src_ip,
                "src_port":self.src_port,
                "dst_ip":self.dst_ip,
                "dst_port":self.dst_port,
                "flg":self.flg
                }
