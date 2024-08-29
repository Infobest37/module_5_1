def number(bus_stops):
   for stop1 in range(bus_stops):
       for stop2 in range(bus_stops):
           bus_stops = stop1 + stop2
           return bus_stops



print(number([[10, 0], [3, 5], [5, 8]]), 5)
print(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]), 17)
print(number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]), 21)