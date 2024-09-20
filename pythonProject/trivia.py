import time

#Answer Key: C B D B C
aura = 0;
name = input("Hi user! What is your name? ")

print("Good luck " + name + " 😉")

time.sleep(1)

print("First question: ")
print("What is Van Halen's most famous album? ")
print("A. Van Halen 2")
print("B. Fair Warning")
print("C. 1984")
q1A = input("D. 5150\n")

time.sleep(0.7)

if q1A.lower() == 'c':
    print("CORRECT!")
    aura += 100
    print("You currently have " + str(aura) + " aura")


else :
    print("INCORRECT!")
    aura -= 75

time.sleep(1.5)

print("Second question: ")
print("What is Van Halen's least favorite m&m color? ")
print("A. red")
print("B. brown")
print("C. yellow")
q2A = input("D. white\n")

time.sleep(0.7)

if q2A.lower() == 'b':
    print("CORRECT!!")
    aura += 100
else :
    print("INCORRECT!!")
    aura -= 75

time.sleep(1.5)

print("Third question: ")
print("When was Van Halen's first album released? ")
print("A. 1979")
print("B. 1976")
print("C. 1984")
q3A = input("D. 1978\n")

time.sleep(0.7)

if q3A.lower() == 'd':
    print("CORRECT!!!")
    aura += 100
else :
    print("INCORRECT!!!")
    aura -= 75

time.sleep(1.5)

print("Fourth question: ")
print("What is considered Van Halen's hardest song to play by Joe Satriani?")
print("A. Eruption")
print("B. Mean Street")
print("C. Spanish Fly")
q4A = input("D. 5150\n")

time.sleep(0.7)

if q4A.lower() == 'b':
    print("CORRECT!!!!")
    aura += 100
else :
    print("INCORRECT!!!!")
    aura -= 75

time.sleep(1.5)

print("Fifth question: ")
print("When was Taylor Swift born? ")
print("A. 1984")
print("B. 1987")
print("C. 1989")
q5A = input("D. 1990\n")

time.sleep(0.7)

if q5A.lower() == 'c':
    print("CORRECT!!!!!")
    aura += 100
else :
    print("INCORRECT!!!!!")
    aura -= 75

time.sleep(0.5)
print("You finished with ...")

print(str(aura) + " AURA!!!")