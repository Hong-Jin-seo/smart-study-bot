import random

# 설정
기간 = 30  # 30일
과목 = ["국어", "수학", "영어", "과학", "사회"]
하루_공부시간 = 5  # 시간
우선_과목 = "수학"

# 각 과목별 기본 가중치 (수학은 우선 배정)
과목_가중치 = {
    "국어": 1,
    "수학": 2,  # 수학은 두 배 우선순위
    "영어": 1,
    "과학": 1,
    "사회": 1
}

# 스케줄 생성 함수
def 생성_스케줄():
    스케줄 = {}
    for day in range(1, 기간 + 1):
        과목_시간표 = {}
        남은_시간 = 하루_공부시간

        # 하루의 과목 구성
        오늘_과목들 = random.choices(
            population=과목,
            weights=[과목_가중치[m] for m in 과목],
            k=3  # 하루에 3과목 공부한다고 가정
        )

        # 시간 분배 (무작위 분배 후 조정)
        시간_분배 = [1] * 3
        while sum(시간_분배) < 남은_시간:
            i = random.randint(0, 2)
            시간_분배[i] += 1

        for idx, subject in enumerate(오늘_과목들):
            과목_시간표[subject] = 시간_분배[idx]

        스케줄[f"Day {day}"] = 과목_시간표

    return 스케줄

# 결과 출력
스케줄표 = 생성_스케줄()

for day, subjects in 스케줄표.items():
    print(f"\n📅 {day}")
    for subject, hours in subjects.items():
        print(f"  - {subject}: {hours}시간")
