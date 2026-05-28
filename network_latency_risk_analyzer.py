import math
lat_1 = float(input("Latency reading 1 (ms):"))
lat_2 = float(input("latency reading 2 (ms):"))
lat_3 = float(input("latency reading 3 (ms):"))
average_latency = (lat_1 + lat_2 + lat_3) / 3
average_latency = round(average_latency, 2)
maximum_latency = max(lat_1, lat_2, lat_3)
deviation = math.fabs(maximum_latency - average_latency)
print("\nAverage Latency: ", average_latency, "ms")
print("Peak Latency: ", maximum_latency, "ms")
print("Deviation: ",round(deviation, 2), "ms")
if average_latency < 20:
    print("status : EXCELLENT - no concerns")
elif average_latency < 100:
    print("status : ACCEPTABLE - normal range")
elif average_latency < 200:
    print('status : HIGH LATENCY - monitor closely')
else:
    print("status : CRITICAL - immediate action needed")