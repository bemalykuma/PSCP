"""BigFrame"""
def bigframe(text_1,text_2,text_3,text_4,text_5):
    """BigFrame"""
    longest = max(len(text_1), len(text_2), len(text_3), len(text_4), len(text_5))
    print("*" * (longest+4))
    print(f"* {text_1}{' '*(longest-len(text_1))} *")
    print(f"* {text_2}{' '*(longest-len(text_2))} *")
    print(f"* {text_3}{' '*(longest-len(text_3))} *")
    print(f"* {text_4}{' '*(longest-len(text_4))} *")
    print(f"* {text_5}{' '*(longest-len(text_5))} *")
    print("*" * (longest+4))
bigframe(input().strip(),input().strip(),input().strip(),input().strip(),input().strip())
