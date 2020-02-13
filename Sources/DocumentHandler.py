from Sources.GiftList import GiftList

def initialLoad(giftList):
    with open('Giftlist/output.txt') as output_file:
        lines = output_file.readlines();
        for line in lines:
            print(line)
            nameObtained = False
            if(line[0] == '#' || line[0] == '-'):+
                nameObtained = False
            elif(line[0] == '*' && nameObtained == False):
                obtainNameFromLine(line)
                nameObtained = True


def obtainName(line):
    print(line)
