import time
from Libraries.calc.calc import Calc

def test_calc_allres():
    c = Calc() # repetitive initialization
    print(c.all_result(10,12))


if __name__ == '__main__':
    start = time.perf_counter()
    test_calc_allres()
    end = time.perf_counter()
    print(f"Took {end-start} seconds... ")
