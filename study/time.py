import time

input("엔터를 누르고 20초를 셉니다.")
start = time.time()

input("20초가 지났다고 생각 할 때 엔터를 누릅니다.")
end = time.time()

et = end - start
print ("실제시간 : ", et,"초")
print ("20초 기준 시간차이 : ", abs(et-20),"초")
