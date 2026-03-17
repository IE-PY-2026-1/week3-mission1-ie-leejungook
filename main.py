# 파일이름 : 60232303 이정욱 3주차 과제 
# 작 성 자 : 이정욱
# 미션 1
name3 = input("이름을 입력하시오: ")
writing3 = int(input("당신의 글쓰기 점수를 입력하시오: "))
python3 = int(input("당신의 파이썬 점수를 입력하시오: "))
last_avg3 = float(input("당신의 지난학기 평균을 입력하시오: "))

average3 = (writing3 + python3)/2
diff = average3 - last_avg3

print()
print(f"{name3}, 학생의 글쓰기 점수는 {writing3} 파이썬 점수는 {python3} 입니다.")
print(f"평균은 {average3} 이고 지난학기와 차이는 {diff} 입니다.")
