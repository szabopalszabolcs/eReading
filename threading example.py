import threading

def is_divisible(dividend, divisor):
  print("Starting...")
  if(dividend % divisor == 0):
    print(True)
  else:
    print(False)
  print("Finished")

thread_A = threading.Thread(target=is_divisible, args=(28, 14))
thread_B = threading.Thread(target=is_divisible, args=(34, 7))

thread_B.start()
thread_B.join()

thread_A.start()
thread_A.join()