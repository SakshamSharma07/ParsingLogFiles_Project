from dataclasses import replace
with open("website.txt",'r') as file:
    lines=file.readlines()
    with open("output.txt","w+") as of:
        of.write(" IP\t\t\tDate Time\t\t\t\tRequest\t\tProtocol\tStatus Code\tPacket Size\n")
        for i in lines:
            i=i.replace('[','')
            i=i.replace(']','')
            i=i.replace('"','')
            line =i.split()
            for i in range(len(line[0]),16):
                of.write(" ")
                of.write(f"{line[0]}\t\t{line[3]+line[4]}\t\t{line[5]}\t\t{line[7]}\t{line[8]}\t\t{line[9]}\n")
    of.close()
    file.close()
