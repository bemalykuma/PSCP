'''ขบวนรถธรรมดาที่ 283'''
def train(station):
    '''ขบวนรถธรรมดาที่ 283'''
    station_km = input()
    while station_km != "Done":
        station_km = station_km.split(", ")
        if station_km[0] == station[0]:
            start = float(station_km[1])
        if station_km[0] == station[1]:
            finish = float(station_km[1])
        if station_km[0] == station[1]:
            break
        station_km = input()
    if finish - start < 0 or finish-start > 184.03:
        print("Error")
    else:
        print(f"{finish-start:.2f}")
train(input().split(", "))
