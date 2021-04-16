def weather(loc):
    import requests     # 웹 페이지 접속
    from bs4 import BeautifulSoup   # HTML 문서 파싱(구문 분석)
    print(f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={parse.quote("날씨 " + loc)}')
    res = requests.get(f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={parse.quote("날씨 " + loc)}')

    bs = BeautifulSoup(res.text, 'lxml')     # HTML 파서 선택(html.parser / lxml / ...)

    weather_text = ''   # 텍스트 내용을 모두 담아 한번에 반환

    # 지역명
    location = bs.select_one('#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.sort_box._areaSelectLayer > div > div > span > em')
    weather_text += location.get_text() + '\n'

    # 현재 기온
    current_temp = bs.select_one('#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > p')
    weather_text += current_temp.get_text().replace('도씨', '') + '\n'

    # 정보1
    info1 = bs.select_one('#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-of-type(1) > p')  # nth-child(n) --> nth-of-type(n)
    weather_text += info1.get_text() + '\n'

    # 정보2
    info2 = bs.select_one('#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-of-type(2)')
    weather_text += info2.get_text().strip() + '\n'

    # 정보3
    info3 = bs.select_one('#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-of-type(3) > span')
    weather_text += info3.get_text() + '\n'

    micro_dust = bs.select_one('#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.sub_info > div > dl > dd.lv2')
    weather_text += '미세먼지: ' + micro_dust.get_text() + '\n'

    # ultra_micro_dust = bs.select_one('#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.sub_info > div > dl > dd:nth-of-type(4)')   # NoneType 오류 발생
    ultra_micro_dust = bs.select_one('#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.sub_info > div > dl > dd:nth-of-type(2)')  # 수작업 수정
    weather_text += '초미세먼지: ' + ultra_micro_dust.get_text() + '\n'

    # ozone = bs.select_one('#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.sub_info > div > dl > dd:nth-of-type(6)')  # NoneType 오류 발생
    ozone = bs.select_one('#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.sub_info > div > dl > dd:nth-of-type(3)')  # 수작업 수정
    weather_text += '오존: ' + ozone.get_text()

    print(weather_text)
    return weather_text