import threading

grades_list = []

print("GWA Calculator \n")
while True:
    grade = input('Enter grades here (enter "stop" if you are finished): ')
    if grade == "stop":
        break
    if grade.isnumeric():
        grades_list.append(int(grade))


def compute_gwa(grades):
    if len(grades_list) == 0:
        print("There is no grade in the list")
    gwa = sum(grades) / len(grades)
    print(f"[Thread] Calculated GWA: {gwa}")


threads = []
for grade in grades_list:
    t = threading.Thread(target=compute_gwa, args=([grade],))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
