import requests

# API 엔드포인트 URL
url = "https://nickname.hwanmoo.kr/?format=json&count=2"

try:
    # GET 요청 보내기
    response = requests.get(url)

    # HTTP 응답 코드 확인
    if response.status_code == 200:
        # JSON 데이터 파싱
        json_data = response.json()

        # 'words' 키에 해당하는 값 가져오기
        words = json_data.get('words', [])

        nickname = words[0]
        print(nickname)
    else:
        print(f"HTTP 오류: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"요청 오류: {e}")