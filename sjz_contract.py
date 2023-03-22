import docx
import re


def get_value(content, start_tag, end_tag, other_tag=[], ignore_cl=False):
    """
    从pdf获取数据，返回的数据为list类型
    :param content: 字符串类型，获取数据的原文
    :param start_tag: 字符串类型，所需获取数据左边紧靠内容
    :param end_tag: 字符串类型，所需获取数据右边紧靠内容
    :param other_tag: list类型，可选，默认为空，所需获取数据的前提条件，越靠近数据的前提条件在list里越靠前
    :param ignore_cl: boolean类型，可选，默认为False，是否忽略所需获取数据的空格或换行符
    :return:
    """
    # 根据是否有前提条件确定正则表达式的字符串
    pattern_content = start_tag + '(.*?)' + end_tag
    if other_tag:
        for premise in other_tag:
            pattern_content = premise + '(.*?)' + pattern_content
    # 根据是否忽略所需数据中的空格和换行符等确定正则表达式
    if ignore_cl:
        pattern = re.compile(r'{}'.format(pattern_content))
    else:
        pattern = re.compile(r'{}'.format(pattern_content), re.DOTALL)
    # 根据正则表达式获取数据
    values = pattern.findall(content)
    # 优化获取下来的数据（把数据中的空格去掉）
    new_values = []
    if other_tag:
        for value in values:
            new_values.append(re.sub(re.compile(r'\s+'), '', value[-1]))
    else:
        for value in values:
            new_values.append(re.sub(re.compile(r'\s+'), '', value))
    return new_values


def fangwu(path):
    text = ''
    file = docx.Document(path)
    for para in file.paragraphs:
        text += para.text + '\n'

    info = {
        "合同甲方": [], "合同约定收款人": [], "合同约定收款账号": [], "合同的不含税金额": [], "合同支付方式": []
    }

    info['合同甲方'] += get_value(text, '甲方（出租人）：[', ']')


if __name__ == '__main__':
    path = r'D:\work\hongxin\shijiazhuang_zhizheng\合同\房屋\石家庄电信（固网）2020年机械进出口机房租赁（含电）合同.docx'
    fangwu(path)