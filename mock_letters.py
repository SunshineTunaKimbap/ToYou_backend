from sqlalchemy.orm import Session
from src.database.connect import get_db
from src.database.models import Letter
import random

# 한글 초성 리스트 (된소리 제외)
CHO_SUNG = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

letters = [
    "보고 싶은 마음, 오늘도 너를 떠올려.",
    "문득 떠오른 네 얼굴, 잠 못 이루는 밤.",
    "그날의 웃음이 그리워, 자꾸 눈에 밟혀.",
    "멀리 있어도 마음만은 늘 곁에 있어.",
    "네가 그립다. 그냥, 아무 이유 없이.",
    "하루에도 몇 번씩, 네 생각에 머문다.",
    "아무 말 없이 건네던 눈빛이 그리워.",
    "돌아오는 길, 네가 있던 풍경이 생각나.",
    "손끝에 닿을 듯, 닿지 않는 너.",
    "그때 함께했던 공기가 여전히 그리워.",
    "지나간 시간들이 문득 가슴을 적셔.",
    "네가 웃던 순간들이 자꾸 떠올라.",
    "보고 싶다. 이 말밖에 못 하는 나.",
    "잠시였지만, 너는 내 전부였어.",
    "너 없는 하루가 이렇게 긴 줄 몰랐어.",
    "익숙한 노래에 네가 떠오른다.",
    "편지를 쓰다 멈추고, 또 울컥해.",
    "네가 준 따뜻함이 오늘따라 그리워.",
    "괜찮다고 했지만, 많이 보고 싶어.",
    "그날의 향기가 아직도 내 안에 살아.",
    "가끔은 꿈에서라도 만나고 싶어.",
    "눈을 감으면, 그때 네 미소가 보여.",
    "너랑 걷던 길을 혼자 걷고 있어.",
    "그리움은 자라나고, 나는 점점 작아져.",
    "언제나 그 자리에서 기다리고 있어.",
    "네가 없는 이 계절이 낯설어.",
    "마음이 아려와, 네가 그리워서.",
    "어쩌면 아직 널 놓지 못한 나야.",
    "조용히 불러본다, 네 이름을.",
    "멀어져도, 네가 나의 따뜻한 기억이야."
]


def add_all_combinations_to_db():
    with next(get_db()) as db:  # 데이터베이스 세션 가져오기
        for k in range(30000):
            # 초성 조합 생성
            cho_combination_sender = ''.join(CHO_SUNG[i] for i in [random.randint(0, len(CHO_SUNG) - 1) for _ in range(3)])
            cho_combination_receiver = ''.join(CHO_SUNG[i] for i in [random.randint(0, len(CHO_SUNG) - 1) for _ in range(3)])
            
            # 데이터베이스에 추가
            new_letter = Letter(
                name_sender=cho_combination_sender,
                abbr_sender=cho_combination_sender,
                name_receiver=cho_combination_receiver,
                abbr_receiver=cho_combination_receiver,
                content=letters[random.randint(0, len(letters) - 1)],
                group_receiver_id=1,
                design_id=1
            )
            db.add(new_letter)

        # 트랜잭션 커밋
        db.commit()
        print("All 3-character 초성 combinations added to the database successfully.")

# 함수 실행
if __name__ == "__main__":
    add_all_combinations_to_db()