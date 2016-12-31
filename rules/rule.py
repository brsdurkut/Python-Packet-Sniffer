import traceback
import sys
import json
from rules.ruleitem import RuleItem

class Rule(object):
    def __init__(self, rules_file=None):
        self.__rules_file = rules_file
        self.__rules = []
        if self.__rules_file != None:
            self._load(rules_file)

    def _get_rules(self):
        return [r._to_dict() for r in self.__rules]

    def _refresh(self):
        for i in range(len(self.__rules)):
            self.__rules[i].id_ = i
        return self.__rules

    def _load(self, f):
        self.__rules = []
        with open(f, mode='r') as data_file:
            data = json.load(data_file)
            data = sorted(data["rules"], key=lambda x: x["id"])
            self.__rules = [RuleItem(load=d) for d in data]
            for r in self.__rules:
                print(str(r.src_ip))
            self.__rules_file = f
            return self._refresh()

    def _save(self):
        if self.__rules_file == None:
            self.__rules_file = "data/rules"

        with open(self.__rules_file, "w") as data_file:
            data = {"rules":[r._to_dict() for r in self.__rules]}
            json.dump(data, data_file)

        return 0

    def _add_rule(self, rule_str):
        try:
            rule_list = rule_str.split(" ")
            id_ = 0 if len(self.__rules) == 0 else self.__rules[-1].id_+1
            rule = RuleItem(
                            id_=id_,
                            src_ip=rule_list[0],
                            src_port=rule_list[1],
                            dst_ip=rule_list[2],
                            dst_port=rule_list[3],
                            flg=rule_list[4]
                            )
            self.__rules.append(rule)
            return self.__rules

        except:
            traceback.print_exc(limit=1, file=sys.stdout)
            return 1

    def _del_rule(self, index):
        try:
            del self.__rules[index]
            self._refresh()

            return self.__rules

        except:
            traceback.print_exc(limit=1, file=sys.stdout)
            return 1
