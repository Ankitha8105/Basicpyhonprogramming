'''
    @Author: Ankitha B L
    @Date:09 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 1:35
    @Title : stop watch problem
'''
import time

def elapsed_time():
    """ 
    Description :
        This function is used to print elapsed time between start time and stop time
    Return :
        It returns the Elapsed time
    """
    input("Please Enter to start the stopwatch")
    start_time = time.time()
    
    input("Please Enter to stop the stopwatch")
    stop_time = time.time()

    elapsed_time = stop_time - start_time

    return elapsed_time

def main():

    time = elapsed_time()

    print(f"The Elapsed_time is {time}")

if __name__ == "__main__":
    main()

