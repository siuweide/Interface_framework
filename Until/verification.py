

def verification_result(except_result, res_data):
    # 验证测试结果
    res_data = res_data.text
    if except_result in res_data:
        res = True
    else:
        res = False
    return res