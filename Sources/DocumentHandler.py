from Sources.GiftList import GiftList

def initialLoad(giftList):
    with open('Giftlist/output.txt') as output_file:
        lines = output_file.readlines();
        for line in lines:
            print(line)
