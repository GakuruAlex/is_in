def is_in(char: str , a_str: str )-> bool:
    """_Determine if a given character is in a given string_

    Args:
        char (str): _letter to search for_
        a_str (str): __An alphabetized String __

    Returns:
        bool: _True if letter in string else False_
    Example:
        >>> is_in('a', 'abcdef')
        True
    """
    low, high = 0, len(a_str)

    while low <= high:
        mid: int = (low + high) // 2
        mid_char: str = a_str[mid]
        if char == mid_char:
            return True
        elif char < mid_char:
                high = mid - 1
        elif char > mid_char:
                low = mid + 1
    return False

def is_in_recur(char: str, aStr: str)->bool:
    low, high = 0, len(aStr)
    mid = (high + low) // 2
    if aStr[mid] == char:
        return True
    elif char < aStr[mid]:
        return is_in_recur(char, aStr[:mid])
    elif char > aStr[mid]:
        return is_in_recur(char, aStr[mid+1:])
    else:
        return False

def main()-> None:
    char = 'z'
    a_str = 'abcdefghijklmnopqrstuvwxyz'
    print(f"is {char} in {a_str} : {is_in(char=char, a_str=a_str)}")
    print(f"is {char} in {a_str} : {is_in_recur(char=char, aStr=a_str)}")

if __name__=="__main__":
    main()

