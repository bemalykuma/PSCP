"""Meteorite"""
def save_world(weight, boom, save_weight):
    """Meteorite"""
    weight_boom = weight / boom
    count = 1
    lairound = 1
    while weight_boom >= save_weight:
        weight_boom /= boom
        lairound *= boom
        count += lairound
    if not weight or weight < save_weight:
        count = 0
    print(count)
save_world(float(input()), int(input()), float(input()))
