def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    x=c
    if x>b:
        x=b
    if x>a:
        x=a
    return x
print(main(10,78,63))