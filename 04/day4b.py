import re

with open("input.txt") as f:
    counter =0
    passports = []
    _d={}
    for line in f.readlines():
        _t = line.strip()
        if _t =="":
            passports.append(_d)
            _d = {}
        else:
            for x in _t.split(" "):
                _c = x.split(":")
                _d[_c[0]]=_c[1]
    passports.append(_d)
    
    def validate(_r):
        if "byr" in _r:
            if 1920 <= int(_r["byr"]) <=2002:
                pass
            else:
                return False
        if "iyr" in _r:
            if 2010 <= int(_r["iyr"]) <=2020:
                pass
            else:
                return False
        if "eyr" in _r:
            if 2020 <= int(_r["eyr"]) <=2030:
                pass
            else:
                return False
        if "hgt" in _r:
            if "cm" in _r["hgt"]:
                if 150 <= int(_r["hgt"].split("cm")[0]) <= 193:
                    pass
                else:
                    return False
            elif "in" in _r["hgt"]:
                if 59 <= int(_r["hgt"].split("in")[0]) <= 76:
                    pass
                else:
                    return False
            elif "cm" not in _r["hgt"] and "in" not in _r["hgt"]:
                return False
        if "hcl" in _r:
            if len(re.findall("#[0-9a-f]{6}",_r["hcl"]))==0:
                return False
        if "ecl" in _r:
            if _r["ecl"] in ['amb','blu','brn',
                             'gry','grn','hzl','oth']:
                pass
            else:
                return False
        if "pid" in _r:
            if len(re.findall("^\d{9}$",_r["pid"])) == 0:
                return False
        return True
    
    for thing in passports:
        if len(thing)==7 and 'cid' not in thing and validate(thing):
            counter +=1    
        elif len(thing) == 8 and validate(thing):
            counter+=1
    print(counter)        