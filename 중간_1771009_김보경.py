'''
프로그래밍을 위한 컴퓨팅적 사고
중간고사 시험 22.04.21.
'''

'''
학과 : 컴퓨터공학과
학번 : 1771009
이름 : 김보경
'''

'''
중간고사에 제시된 출력을 참고하여, 아래에 코드를 작성하시오. 
'''

day = ["월", "화", "수", "목", "금", "토", "일", "all"]
a = input("무슨 요일의 영화가 궁금한가요?\n모든 요일의 영화를 검색하기 위해서는 all이라고 입력해주세요.\n")
if (a == day[0] or a == day[1]):
	print(a, "요일에는 스파이더 맨:노웨이 홈이 상영될 예정입니다.\n영화 요금은 ", 6000, "원 입니다.", sep='');
elif (a == day[2] or a == day[3]):
	print(a, "요일에는 센과 치히로의 행방불명이 상영될 예정입니다.\n영화 요금은 ", 6000, "원 입니다.", sep='');
elif (a == day[4]):
	print(a, "요일에는 인터스텔라가 상영될 예정입니다.\n영화 요금은 ", 6000, "원 입니다.", sep='');
elif (a == day[5] or a == day[6]):
	print(a, "요일에는 어바웃 타임이 상영될 예정입니다.\n영화 요금은 ", (int)(6000 * 1.2), "원 입니다.", sep='');
elif (a == day[7]):
	print("월/화:스파이더 맨:노웨이 홈\n수/목:센과 치히로의 행방불명\n금:인터스텔라\n토/일:어바웃 타임");
else:
	print("잘못된 입력입니다")

# 아래의 코딩 문장은 제공합니다. 
input("Press enter to exit") 



