"""Ping"""
def server():
    """ping"""
    drive = input()
    space = input()
    ping = input()
    ip = ping[ping.find("[")+1:ping.find("]")]
    if not "[" in ping:
        ip = ping[ping.find(" ")+1:ping.find("w")-1]
    received = 0
    lost = 0
    result = 0
    lst = [1]
    for _ in range(4):
        reply = input()
        if "Reply from" in reply:
            received += 1
            time = reply[reply.find("time")+4:reply.find("ms")]
            if time[0] == "=":
                time = int(time[1:])
            if "<1" in reply:
                time = 0
            result += time
            lst.insert(0,time)
        else:
            lost += 1
    drive = ""
    space = ""
    lst.remove(1)
    per_loss = (lost/4) * 100
    print(f"Ping statistics for {ip}{space}{drive}:") #กลัวไม่ได้ใช้ drive กับ space เลยเอาน้องมาใส่สักหน่อย
    print(f"    Packets: Sent = 4, Received = {received}, Lost = {lost} ({per_loss:.0f}% loss),")
    if lost < 4 :
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {min(lst)}ms, Maximum = {max(lst)}ms, Average = {result//received}ms")
server()
