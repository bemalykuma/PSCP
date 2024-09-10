"""Books"""
import math
def books(book, page, x, y):
    """books"""
    day = 0
    read_book = 0
    read_page = 0
    while True:
        read = math.ceil(page * (x/y)) #หาหน้าที่อ่านไป
        if read_book == book: #ถ้าจำนวนเล่มที่อ่านไป เท่ากับ จำนวนเล่มทั้งหมด
            break
        if read >= page: #ถ้าหน้าที่อ่านไป มากกว่าเท่ากับ จำนวนหน้าทั้งหมด
            break
        read_page += read #หน้าที่อ่านไปทั้งหมด ณ ปัจจุบัน
        if read_page >= page: #ถ้าหน้าที่อ่านไปทั้งหมด เยอะกว่า จำนวนหน้าทั้งหมด
            read_book += 1 #อ่านจบไปแล้ว+1เล่ม
            read_page = 0 #เริ่มต้นเล่มใหม่ ฉะนั้น หน้าที่อ่านไปทั้งหมดจะว่างเปล่าเพราะยังมะได้อ่าน
        x += 1
        y += 1
        day += 1
    day += book-read_book
    print(day)
books(int(input()), int(input()), int(input()), int(input()))
