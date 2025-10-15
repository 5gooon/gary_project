
#숫자 입력받기
while True:
    # while까지는 알았으나, while True + break 구성을 많이쓰며, 무한루프이다.

    num1 = input("첫번째 숫자를 입력하세요: ").strip()
    num2 = input("두번째 숫자를 입력하세요: ").strip()
    #.strip은 공백을 제거해주는 method (gpt참고함), 예외처리도 써보지않아서 참고함.
    try:
        num = float(num1) #소수도 숫자이므로 float사용.
        num = float(num2) 
        break  # 첫 추석처럼 입력성공받으면 무한루프 종료후 print로 출력
    except ValueError:
        #위에 입력값이 숫자형식이 아니면 형식오류이기때문에 ValueError사용
        print("잘못된 입력입니다. 숫자를 다시 입력해 주세요.")

print(f"첫번째 숫자 : {num1} , 두번째 숫자 : {num2}") #숫자 두개를 동시에 받아서 f-string으로 출력