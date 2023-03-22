import xlrd


def get_data(path, sheet_index=0):
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(sheet_index)
    rows = sheet.nrows
    cols = sheet.ncols
    data = []
    for row_index in range(1, rows):
        data_row = {}
        for col_index in range(cols):
            key = sheet.cell_value(0, col_index).strip()
            value = sheet.cell_value(row_index, col_index).strip()
            data_row[key] = value
        data.append(data_row)
    return data


def self_to_unit(self_data):
    unit_data = []
    for data in self_data:
        unit_data_row = {}
        unit_data_row['LOG_ID'] = data['编号']
        unit_data_row['USER_ID'] = ''
        unit_data_row['BUSINESS_TYPE'] = '结算单'
        unit_data_row['YW_TYPE'] = ''
        unit_data_row['CHARGE_TYPE'] = ''
        unit_data_row['PRO_NAME'] = data['业务场景']
        unit_data_row['SUBMIT_ACCOUNT_CODE'] = data['报账单号']
        unit_data_row['COMPANY_CODE'] = data['上市']
        unit_data_row['SUBMIT_ACCOUNT_NAME'] = data['地区']
        unit_data_row['SUBMIT_ACCOUNT_MONEY'] = data['报账金额']
        unit_data_row['SEND_DATE'] = ''
        unit_data_row['START_DATE'] = data['开始时间']
        unit_data_row['END_DATE'] = data['结束时间']
        unit_data_row['RESULT_TYPE'] = '[审核无误]' if data['单号类型'] == '成功' else '[转人工]'
        unit_data_row['RESULT'] = data['转人工问题']
        unit_data_row['NEXT_USER'] = data['转办人']
        unit_data_row['PROVINCE'] = 'beijing'
        unit_data_row['BATCH_DATE'] = ''
        unit_data_row['DJ_TYPE'] = ''
        unit_data_row['SY_NUM'] = '0'
        unit_data.append(unit_data_row)
    return unit_data


if __name__ == '__main__':
    self_data = get_data('beijingly.xls')
    unit_data = self_to_unit(self_data)
    print(1)
