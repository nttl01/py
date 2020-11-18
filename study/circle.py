import turtle as t

t = t.Turtle()

t.shape("turtle")

n=60
# t.bgcolor("black")

t.color("green")
t.speed(0)
for x in range(n):
    t.circle(80)
    t.left(360/n)

input()
print("end")





