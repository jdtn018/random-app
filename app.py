# 1. 차종 데이터 (2차원 리스트 구조: [차종명, 가격(만원), 크기, 색깔])
cars = [
    ["자동차 A", 800, "대형", "흰색"],
    ["자동차 B", 700, "대형", "검은색"],
    ["자동차 C", 600, "소형", "검은색"]
]

# 2. 만족도 점수 계산 함수 (만점 100점 기준, 조건 불만족 시 -30점씩 차감 -> 최저 기본점수 10점)
def calculate_score(car, user_money, user_size, user_color):
    score = 100  # 기본점수(10점) + 3개 조건(각 30점) = 100점
    
    # 조건 1: 돈(예산) 판단 - 내 예산보다 차 가격이 비싸면 불만족
    if car[1] > user_money:
        score -= 30
        
    # 조건 2: 크기 판단
    if car[2] != user_size:
        score -= 30
        
    # 조건 3: 색깔 판단
    if car[3] != user_color:
        score -= 30
        
    return score

# --- 사용자 입력 화면 ---
print("=== [기회비용: 효율적인 차종 고르기] ===")
selected_car = input("1/ 차종선택 [자동차 A, 자동차 B, 자동차 C]: ")
user_money = int(input("2/ 돈 입력 [600 / 700] (숫자만 입력): "))
user_size = input("   크기 입력 [소형 / 대형]: ")
user_color = input("   색깔 입력 [흰색 / 검은색]: ")

# 3. 반복문을 이용해 각 차종의 만족도 점수를 계산하고 리스트에 저장
satisfaction_scores = []
for car in cars:
    score = calculate_score(car, user_money, user_size, user_color)
    satisfaction_scores.append(score)

# 4. 반복문과 조건문을 이용해 가장 점수가 높은 합리적인 차종 찾기
best_index = 0
for i in range(len(satisfaction_scores)):
    if satisfaction_scores[i] > satisfaction_scores[best_index]:
        best_index = i

best_car = cars[best_index][0]

# --- 결과 출력 화면 ---
print("\n------- [결과 출력 화면] -------")
print(f"★ 사용자 만족도 점수 리스트: {satisfaction_scores}")

for i in range(len(cars)):
    print(f"- {cars[i][0]}: {satisfaction_scores[i]}점")

# 처음 선택한 차종의 점수 안내 (띄어쓰기 오타 방지 처리 포함)
for i in range(len(cars)):
    if cars[i][0].replace(" ", "") == selected_car.replace(" ", ""):
        print(f"\n▶ 처음 선택한 [{cars[i][0]}]의 만족도 점수는 {satisfaction_scores[i]}점입니다.")

print(f"\n{best_car}를 선택하는 것이 가장 합리적이다!")
