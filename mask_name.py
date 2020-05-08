def mask_name(name: str) -> str:
    '''
    [Function] 姓名信息脱敏
    [Description] 
        1. 去除所有空格
        2. 空值：某
        3. 单字符值: 保留单字
        4. 双字符值: 姓 + "*"
        5. 复姓姓名：
    '''
    
    return masked_name

#TODO: 复姓的情况如：诸葛、欧阳、东方、宇文、司空、司徒、南宫等
