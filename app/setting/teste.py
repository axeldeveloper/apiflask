from functools import wraps
from pathlib import Path
import time


def cronometra(function):
    @wraps(function)
    def wrapper(*args, **kwrds):
        start = time.time()
        ret = function(*args, **kwrds)
        end = time.time() - start
        print("LOG[DEBUG] This is the time that took for", function.__name__, "to finish executing:", end)
        return ret

    return wrapper


@cronometra
def service_code(description):
    time.sleep(2)
    print(description)


if __name__ == "__main__":
    service_code("teste")