with open("input.txt") as f:
    ip = 0
    acc = 0
    program = []
    _c = []
    for line in f.readlines():
        x = line.strip().split()
        program.append(x)
    while ip != "DONE":
        print(ip)
        print(acc)
        if ip not in _c:
            _c.append(ip)               
            if program[ip][0] == "nop":
                ip +=1
            elif program[ip][0] == "acc":
                acc += int(program[ip][1])
                ip +=1
            elif program[ip][0] == "jmp":
                ip += int(program[ip][1])
        else:
            print("found a repeat")
            ip = "DONE"
            print(acc)
        
