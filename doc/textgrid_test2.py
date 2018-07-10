
from praatio import tgio


tg = tgio.openTextgrid("A_man_bought_a_car_in_Paris-DC-5.TextGrid")

print(tg.tierNameList)

stressTier = tg.tierDict["stress"] # tg.tierNameList[0]]

for start, stop, label in stressTier.entryList:
    print(start)
    print(stop)
    print(label)
