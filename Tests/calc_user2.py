import time
from Libraries.calc.calc import Calc

def test_calc_sum():
    c = Calc() #repetitive initialization
    print(c.add(12, 36))


if __name__ == '__main__':
    start = time.perf_counter()
    test_calc_sum()
    end = time.perf_counter()
    print(f"Took {end - start} seconds... ")