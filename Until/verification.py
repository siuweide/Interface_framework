

def verification_result(except_result, res_data):
    # 验证测试结果
    if except_result in str(res_data):
        res = True
    else:
        res = False
    return res