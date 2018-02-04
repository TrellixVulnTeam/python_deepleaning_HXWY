#!/usr/bin/env python3

# 라이브러리 설정
import sys
import urllib.request as req
import urllib.parse as parse

# 명령줄 매개변수 추출
if len(sys.argv) <= 1:
    print("USAGE: download-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

# 매개변수를 URL 인코딩합니다.
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {'stnId': regionNumber}

params = parse.urlencode(values)
url = API + "?" + params
print("url=", url)

# 다운로드합니다.
data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)