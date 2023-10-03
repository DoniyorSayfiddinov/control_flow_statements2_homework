def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if (a-c>0 or c-a>0)and (a>b>c or a<b<c):
        return b 
    if (b-c>0 or c-b>0)and (b>a>c or b<a<c):
        return a 
    else :
        return c 
print(main(25,89,23))
