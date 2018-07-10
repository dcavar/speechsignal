

import textgrid


f = textgrid.TextGrid()
f.read("A_man_bought_a_car_in_Paris-DC-5.TextGrid")

print(f.getNames())
print(f.getFirst("stress"))

for y in f.getList("stress"):
    for x in y:
        print(x)
        print("Duration:", x.duration())
        print("Bounds:", x.bounds())
        print("Overlaps:", x.overlaps(textgrid.Interval(0.0, 1.89568, "a")))


