with open("input.txt") as f:
    entries = [int(x.strip()) for x in f.readlines()]
    print(entries)
    for i in range(len(entries)):
        for j in range(len(entries)):
            if i!=j and entries[i]+entries[j]==2020:
                print (entries[i],entries[j])
                print(entries[i]*entries[j])
