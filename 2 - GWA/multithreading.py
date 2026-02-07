import threading

def compute_gwa(grades):
  gwa = sum(grades) / len(grades)
  print(f"[Thread] Calculated GWA: {gwa}")

grades_list = [85, 90, 78, 92] 

threads = []
for grade in grades_list:
  t = threading.Thread(target=compute_gwa, args=([grade],))
  threads.append(t)
  t.start()

for t in threads:
  t.join()