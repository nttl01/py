# 리스트 (배열)
s_list = ["1",2.0,3,4,5]
print(s_list) #
print(s_list[0]) #    첨자는 0 부터 시작

#  함수와 메소드
print("길이 : ", len(s_list)) # 길이
s_list.append("aa6") # 요소추가
print(s_list) #
  
s_list.pop() #맨끝 요소삭제 
print(s_list) #

s_list.pop(2)  #임의 요소삭제  첨자 0 부터 시작
print(s_list) #

s_list.insert(3,"bb") # 첨자 3 뒤에 자료추가
s_list.remove('bb') # 해당자료삭제
s_list.clear() #모든자료 삭제
s_list.sort() #  오름차순, 자료가 문자와 숫자가 섞여있다면 오류가 발생하므로 통일해야한다.
s_list.sort(reverse=true) # 내림차순 정렬
s_list.reverse() # 자료를 뒤집는다.
s_list[1:3] # 슬라이싱 , 자료를 시작인덱스에서 최종 인덱스를 넣어서 추출해온다
s_list[:3] # 처음부터 3까지
s_list[2:] # 2부터 끝까지



