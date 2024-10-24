'''Resistor'''
def resistor(c_1, c_2, c_mul, c_tol):
    '''Resistor'''
    color_dict = {"Black":"0", "Brown":"1", "Red":"2", "Orange":"3", "Yellow":"4", "Green":"5", \
                  "Blue":"6", "Purple":"7", "Grey":"8", "White":"9"}
    multiplier = {"Black":1, "Brown":10, "Red":100, "Orange":1000, "Yellow":10000,"Green":100000,\
                  "Blue":1000000, "Purple":10000000, "Gold":0.1, "Silver":0.01}
    tolerance = {"Brown":(1/100), "Red":(2/100), "Green":(0.5/100), "Blue":(0.25/100),\
                  "Purple":(0.10/100), "Grey":(0.05/100), "Gold":(5/100), "Silver":(10/100)}
    cond_color = c_1 in color_dict and c_2 in color_dict and c_mul in multiplier and c_tol in \
        tolerance
    if cond_color:
        bound = int(color_dict[c_1]+color_dict[c_2]) * multiplier[c_mul]
        print(f"{bound-(bound*tolerance[c_tol]):.4f}")
        print(f"{bound+(bound*tolerance[c_tol]):.4f}")
    else:
        print("Error")
resistor(input(), input(), input(), input())
