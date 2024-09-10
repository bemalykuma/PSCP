"""Nearer"""
def main(alice,bob,ice_cream):
    """Nearer"""
    alice_distance = abs(alice - ice_cream)
    bob_distance = abs(bob - ice_cream)
    if bob_distance < alice_distance:
        print(f"Bob {bob_distance}")
    elif bob_distance > alice_distance:
        print(f"Alice {alice_distance}")
    else:
        print(f"Sundaes {alice_distance}")
main(int(input()), int(input()), int(input()))
