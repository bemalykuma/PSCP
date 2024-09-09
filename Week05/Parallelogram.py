"""Parallelogram"""
def parallelogram(text):
    """Parallelogram"""
    length = len(text)
    for j in range(1,length+1):
        print(f"{' '*(length-j)}{text[:j]}")
    for j in range(length-1):
        print(f"{text[j+1:]}")
parallelogram(input())
