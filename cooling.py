T = 100
T_a = 20
t = 0 #minutes
rate_of_change = (-0.055)*(T-T_a)
print("minutes temperature")

while t<20:
    degrees_per_minute = (.055)*(T-T_a)
    print ("%5d     %5.1f" % (t,T))
    t = t+1
    T = T-degrees_per_minute
