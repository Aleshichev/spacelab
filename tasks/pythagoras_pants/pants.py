import logging

logging.basicConfig(level=logging.INFO, filename='tasks\pythagoras_pants\mylog.log')
logger = logging.getLogger()
print(logger)
def find_triangle(nums):
    logger.info(f'Enter in the find_triangle() function args = {nums}')
    a, b, c = nums[0], nums[1], nums[2]
     
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print(True)
    else:
        print(False)

if __name__ == '__main__':
    
    args = [5,3,4], [6, 8, 10], [100, 3, 65]
    
    try:
        for i in args:
            find_triangle(i)
    except TypeError:
        logger.error(f'TypeError')
        print("Возникла ошибка типа данных")
    except IndexError:
        logger.error(f'IndexError')
        print("Ошибка. Введите 3 значения")
    


 