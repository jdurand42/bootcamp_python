
import time
import functools
from random import randint


def log(func):

#	@functools.wraps(func)
#	def inner(*args, **kwargs):
#		print("(cmaxime)Running: " + str(args[0]))
	def wrapper_timer(*args, **kwargs):
		file = open("machine.log", "a")
		start_time = time.perf_counter()    # 1
		value = func(*args, **kwargs)
		end_time = time.perf_counter()      # 2
		run_time = end_time - start_time    # 3
#		print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
		name = f"{func.__name__!r}"[1:len(f"{func.__name__!r}")].capitalize()
		s = "(RICHARD 2.0)Running: " + name.replace('_', ' ')[0:len(name) - 1]
		while len(s) < 50:
			s = s + " "
		s = s + f"[ Exec-time: {run_time:.4f} secs ]"
		file.write(s)
		file.write("\n")
#		file.write(f"(cmaxime)Running: {func.__name__!r}		[ Exec-time: {run_time:.4f} secs ]")
		file.close()
		return value
	return wrapper_timer

#	return inner
	#return inner

class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
     if self.water_level > 20:
         return True
     else:
         print("Please add water!")
         return False
    @log
    def boil_water(self):
        return "boiling..."
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)

#CoffeeMachine()
