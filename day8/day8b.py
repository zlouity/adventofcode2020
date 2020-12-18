def _terminate(program):
    ip = 0
    acc = 0
    _c = []
    while ip != "DONE":
            #print(ip)
            #print(acc)
            if _c.count(ip) > 2:
                return 
            _c.append(ip)               
            if ip == len(program):
                print(acc)
                return
            if program[ip][0] == "nop":
                ip +=1
            elif program[ip][0] == "acc":
                acc += int(program[ip][1])
                ip +=1
            elif program[ip][0] == "jmp":
                ip += int(program[ip][1])
            

with open("input.txt") as f:
    program = []
    for line in f.readlines():
        x = line.strip().split()
        program.append(x)
    jump_nop = []
    for v,x in enumerate(program):
        if x[0] == "jmp" or x[0] == "nop":
            jump_nop.append(v)
    #print(jump_nop)
    for _t in jump_nop:
        #print("trying a flip")
        if program[_t][0] == "jmp":
            program[_t][0]="nop"
            _terminate(program)
            program[_t][0]="jmp"
        else:
            program[_t][0]="jmp"
            _terminate(program)
            program[_t][0]="nop"
