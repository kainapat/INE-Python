print("KPH\tMPH")
print("-------")

for KPH in range(60, 140, 10):
    MPH = KPH*0.6214
    print(KPH, "\t","%.1f"%MPH)
print("-------")