"""PhoneNumber"""
def phonenumber(phone_num, address):
    """number"""
    if address == "Domestic":
        if len(phone_num) == 9:
            print(f"{phone_num[0]} {phone_num[1:5]} {phone_num[5:]}")
        elif len(phone_num) == 10:
            print(f"{phone_num[0:2]} {phone_num[2:6]} {phone_num[6:]}")
    elif address == "International":
        if len(phone_num) == 9:
            print(f"+66 {phone_num[1:5]} {phone_num[5:]}")
        elif len(phone_num) == 10:
            print(f"+66{phone_num[1]} {phone_num[2:6]} {phone_num[6:]}")
phonenumber(input(),input())
