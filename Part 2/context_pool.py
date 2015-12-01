from multiprocessing import Pool
import contextlib

def square(x):
    """Return the square of the argument"""
    return x*x

if __name__ == "__main__":
    
    a = [1, 2, 3, 4, 5]
    
    with contextlib.closing( Pool() ) as pool:
        result = pool.map(square, a)

    print result
