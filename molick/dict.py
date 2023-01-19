'''Used to generate dictionary samples'''

def getnumlist(startnum:int,falsenum:int,numlen:int) -> list:
    '''Used to generate a list of numeric-only captchas:[startnum,falsenum)'''
    return [
        f"%0{ numlen if numlen >= len(str((falsenum - 1))) else len(str((falsenum - 1))) }d" %
        num for num in range(startnum,falsenum)
    ]

if __name__ == "__main__":
    print(getnumlist(1,100,2))
