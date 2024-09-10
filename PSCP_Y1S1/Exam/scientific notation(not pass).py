"""scientific notation"""
def main(sci):
    """scientific notation"""
    if "x" in sci:
        find_x = sci.find("x")
        font = sci[:find_x-1]
        back = sci[find_x+2:]
        num = back[:back.find("^")]
        multi = back[back.find("^")+1:]
        num = int(num)
        font = float(font)
        multi = int(multi)
        result = f"{font * (num**multi)}"
    elif not "x" in sci:
        length = len(sci)
        if 0 < float(sci) < 1:
            count = 1
            loop_sci = sci[2:]
            for i in loop_sci:
                if i == "0":
                    count += 1
                elif i.isnumeric() and i != "0":
                    break
            font = int(sci[count+1:])
            l_font = len(str(font))
            font_result = font / (10**(l_font-1))
            l_f_re = len(str(font_result))
            back = f"10^-{count}"
            result = f"{font_result} x {back}"
            if length - l_f_re-count > 0:
                result = f"{font_result}{'0'*(length-l_f_re-count)} x {back}"
        elif float(sci) <= 0:
            result = 0
        elif "." in sci:
            find_dot = sci.find(".")
            font = float(sci)/ (10**(find_dot-1))
            back = f"10^{find_dot-1}"
            l_font = len(str(font))
            zero = length-l_font
            result = f"{font} x {back}"
            if zero > 0:
                result = f"{font}{'0'*zero} x {back}"
        else:
            font_l = float(sci) / 10**(length-1)
            back = f"10^{length-1}"
            result = f"{font_l} x {back}"
    print(result)
main(input())
