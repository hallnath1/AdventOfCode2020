from sympy.ntheory.modular import crt

file = open("input.txt").read().replace('x', '1').replace('\n', ',').split(',')
early_time, *bus_list = [int(x) for x in file]

best = min(((early_time//bus+1)*bus, bus) for bus in bus_list if bus > 1)
print('PART A', best[1] * (best[0]-early_time))

m, r = zip(*((bus, bus-i) for i, bus in enumerate(bus_list) if bus > 1))
print('PART B', crt(m, r)[0])
