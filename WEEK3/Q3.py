import re

print("请输入身份证号")
identify_code = input()


def check_identify_code(code):
    if len(code) == 18:
        if re.match(r"(^\d{15}$)|(^\d{17}([0-9]|X)$)", code):
            return True
        else:
            return False
    else:
        return False


if check_identify_code(identify_code):
    print("身份证号码合法！")
else:
    print("身份证号码不合法！")
