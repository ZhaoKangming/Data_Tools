def devide_numb_range(sNumb: int, eNumb:int, parts:int) -> list:
    '''
    Function: 把整数段 sNumb 到 eNumb 划分为 parts 部分
    '''
    parts_list: list = []
    remainder: int = (eNumb - sNumb) % (parts - 1)
    GCD: int = int((eNumb - sNumb - remainder) / (parts - 1))

    for i in range(0, parts-1):
        parts_list.append([sNumb + i*GCD, sNumb + (i+1)*GCD])

    parts_list.append([eNumb - remainder, eNumb])

    return parts_list
