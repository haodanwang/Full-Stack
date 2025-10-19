import requests
import openpyxl

cookies = {
    "ll": '"118177"',
    "bid": "EPjg6z69858",
    "__utma": "30149280.475528839.1760812719.1760812719.1760812719.1",
    "__utmc": "30149280",
    "__utmz": "30149280.1760812719.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    "__utmt": "1",
    "__utmb": "30149280.1.10.1760812719",
    "ap_v": "0,6.0",
    "_vwo_uuid_v2": "D5609ADDA8FA592A07AB8F47D66C6353D|06f06963e1d0bb9b84bd6c07a9d561bc",
}

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "origin": "https://movie.douban.com",
    "priority": "u=1, i",
    "referer": "https://movie.douban.com/",
    "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    # 'cookie': 'll="118177"; bid=EPjg6z69858; __utma=30149280.475528839.1760812719.1760812719.1760812719.1; __utmc=30149280; __utmz=30149280.1760812719.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=30149280.1.10.1760812719; ap_v=0,6.0; _vwo_uuid_v2=D5609ADDA8FA592A07AB8F47D66C6353D|06f06963e1d0bb9b84bd6c07a9d561bc',
}

params = {
    "limit": "50",
    "category": "豆瓣高分",
    "type": "全部",
}

response = requests.get(
    "https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie",
    params=params,
    cookies=cookies,
    headers=headers,
)
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet["A1"] = "电影名称"
sheet["B1"] = "电影介绍"
sheet["C1"] = "评分"
data = response.json()["items"]
for i in data:
    title = i.get("title")
    card_subject_title = i.get("card_subtitle")
    value = i.get("rating").get("value")
    sheet.append([title, card_subject_title, value])

workbook.save("豆瓣高热度电影.xlsx")
