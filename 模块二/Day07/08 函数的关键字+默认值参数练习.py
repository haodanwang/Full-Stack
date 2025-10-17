def check_air_ticker(from_, to_, date="2024-06-01", seat_class="经济舱", max_price=None):
    query = f"数据库查询,日期:{date},{from_}到{to_}所有的{seat_class}"
    if max_price is not None:
        query += f",最高票价不要超过{max_price}元"
    else:
        query += "的飞机票"

    print(query)


check_air_ticker("南京", "上海", seat_class="商务舱", max_price=3000)
