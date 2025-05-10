# ㄱㄷ에게란?

> "그대에게 닿지 못할 이야기라도, 조금은 흐려진 그대에게게 보내봅니다"

ㄱㄷ에게는 누군가의 초성을 향해 메시지를 보낼 수 있는 서비스입니다.

우리는 한 번쯤 찌질했던 우리의 모습을 기억합니다. 그 찌질함을 초성이라는 렌즈에 굴절시켜 조금 흐릿해해진 우리의 상을… 서로에게 연결해주는 것이 저희 서비스의 본질입니다.

잊지 못할 그 사람에게 전하지 못한 한마디를 전해보세요. 종착지인 그사람에게 도달하지 못할지도 모르지만, 어떤 메시지는 출발선을 나서는 것이, 그저 털어놓는 것이 곧 목적지일 때도 있으니까요.

# 주제와의 연관성

"그대에게"는 음악에 대한 그리움과 사랑이 담긴 노래입니다.

누군가에게 전하는 말, 영원히 이어질것만 같은 그리움, 무엇보다도 이 노래가 촉발하는 "설렘"이라는 감정에서 영감을 얻어 이 아이디어를 떠올렸습니다.

절대로 닿을 수 없는 "음악"이라는 수신인에게 보내는 노래. "그대에게"를 보며 저희는 종착지가 아닌 출발지를 목적지로 하는 메시지를 전하는 서비스를 기획하였습니다.

의도적으로 종착지를 흐리고, 종착지로의 여정을 우연에 맡김으로서 메시지의 발송 자체를 목적화하고자 했습니다. 그리고 그 우연한 여정의 끝에 종착지에 도달한다면, 더 큰 설레임을 전해줄 수 있도록 했습니다.

그리움과 후회를 꺼내놓을 공간. 그 꺼내짐이 흘러가 우연히 종착지에 닿을지 모른다는 설렘의 공간. 그것이 저희의 서비스, "ㄱㄷ에게"입니다.

> 내 삶이 끝날 때까지 언제나 그댈 사랑해

그 사무치는 사랑을, 이곳에 꺼내보세요.

# 왜 "ㄱㄷ에게"인가?

## 욕망을 자극하는 제품

저희 서비스는 발신인과 수신인 모두의 욕망을 자극합니다.
"털어놓는다"는 욕망과 "관심과 애정을 받는다"는 욕망을 말이죠.

가슴에 갇힌 이야기들은 계속해서 우리를 짓누릅니다. 그렇기에 우리는 영원한 비밀은 없다는 것을 알면서도 우리의 비밀을 새어나가게 하는 것이겠죠. "ㄱㄷ에게"는 그 "털어놓기"의 욕망을 만족시킵니다. 적절한 정도의 특정성으로 우리는 더 적은 리스크로 "털어놓기"의 욕망을 해소할 수 있습니다.

또한 "Gas", "NGL", "Asked"의 성공에서 알 수 있듯, 우리는 다른 사람들의 우리에 대한 이야기를 좋아합니다. "내게 온 것일지" 모르는 편지에서 오는 그 설레임을 "ㄱㄷ에게"는 제공합니다. 또한 그 불확실성에서 오는 도파민도 유저를 잡아둘 무기가 될 것입니다.

# 주요 기능

## 1차 MVP

- 편지 송신
  - 발신자와 수신자의 이름, 그리고 편지의 내용을 입력하면 편지를 발송할 수 있습니다.
- 편지 수신
  - 자신의 이름과 같은 초성에게 쓰여진 편지들을 확인할 수 있습니다.

## 2차 MVP

- 그룹 분할
  - 수신자의 대학을 지정할 수 있고, 수신자는 자신의 대학에 해당하는는 편지만을 필터링해서 볼 수 있습니다.
- 잠긴 내용
  - PIN으로 숨겨진 내용을 작성할 수 있으며 수신자가 PIN을 맞추면 해당 내용을 확인할 수 있습니다.
- 편지지 디자인 선택
  - 여러 편지지의 디자인을 선택할 수 있습니다.

# API Guide

## GET

- /api/search/{name}
  - 이름을 입력하면 해당 이름과 같은 초성에 해당하는 편지를 필터링해 출력합니다.
  - 사용 예시
  ```cmd
  curl -X 'GET' \
  'http://127.0.0.1:8000/api/search/신호진진' \
  -H 'accept: application/json'
  ```
  ```json
  {
    "letters": [
      {
        "id": 17549,
        "abbr_sender": "ㄷㅋㄴ",
        "abbr_receiver": "ㅅㅎㅈ",
        "content": "눈을 감으면, 그때 네 미소가 보여.",
        "group_receiver_id": 1,
        "group_receiver": "고려대학교",
        "locked": false
      },
      {
        "id": 19882,
        "abbr_sender": "ㄱㅍㅅ",
        "abbr_receiver": "ㅅㅎㅈ",
        "content": "익숙한 노래에 네가 떠오른다.",
        "group_receiver_id": 1,
        "group_receiver": "고려대학교",
        "locked": false
      }
    ]
  }
  ```
- /api/search/{name}/{group_id}
  - 이름괴 그룹에 해당하는 편지를 필터링해 반환합니다.
  - 사용 예시
  ```cmd
  curl -X 'GET' \
  'http://127.0.0.1:8000/api/search/박재현현/1' \
  -H 'accept: application/json'
  ```
  ```json
  {
    "letters": [
      {
        "id": 1061,
        "abbr_sender": "ㄱㅁㅌ",
        "abbr_receiver": "ㄱㅅㅂ",
        "content": "손끝에 닿을 듯, 닿지 않는 너.",
        "group_receiver_id": 1,
        "group_receiver": "고려대학교",
        "locked": false
      },
      {
        "id": 2219,
        "abbr_sender": "ㅇㄱㅎ",
        "abbr_receiver": "ㄱㅅㅂ",
        "content": "하루에도 몇 번씩, 네 생각에 머문다.",
        "group_receiver_id": 1,
        "group_receiver": "고려대학교",
        "locked": false
      }
    ]
  }
  ```

## POST

- /api/post/
  - 편지를 추가합니다.
  - 사용예시
    - 입력
    ```json
    {
      "name_sender": "신호진",
      "name_receiver": "김두한",
      "content": "string",
      "group_receiver_id": 0,
      "design_id": 0,
      "pin": "1234",
      "content_secret": "string"
    }
    ```
    - 출력
    ```json
    {
      "message": "Post created successfully",
      "post": {
        "abbr_sender": "ㅅㅎㅈ",
        "id": 30601,
        "group_receiver_id": 0,
        "content": "string",
        "pin": "1234",
        "name_sender": "신호진",
        "name_receiver": "김두한",
        "abbr_receiver": "ㄱㄷㅎ",
        "design_id": 0,
        "content_secret": "string"
      }
    }
    ```
- /api/unlock/
  - PIN으로 숨겨진 내용을 확인합니다
  - 사용예시
    - 입력
    ```json
    {
      "id": 30601,
      "pin": "1234"
    }
    ```
    - 출력
    ```json
    {
      "message": "Letter unlocked successfully",
      "letter": {
        "abbr_sender": "ㅅㅎㅈ",
        "id": 30601,
        "group_receiver_id": 0,
        "content": "string",
        "pin": "1234",
        "name_sender": "신호진",
        "name_receiver": "김두한",
        "abbr_receiver": "ㄱㄷㅎ",
        "design_id": 0,
        "content_secret": "string"
      }
    } // success
    {
      "error": "Incorrect pin"
    } // error
    ```
