
from datetime import timedelta, datetime
from loguru import logger

logger.add("mylog.log", format="{time} {level} {message}", level="DEBUG")


from datetime import timedelta, datetime

@logger.catch
def timetable(data):
    logger.info(f'Enter in the timetable() function data = {data}')
    start_date = data["start_date"] - timedelta(days=1)
    calendar = []
    days = data["days"]
    
    while days > 0:
        
        work_days = data["work_days"]
        rest_days = data["rest_days"]
        
        while work_days > 0:
            next_day = start_date + timedelta(days=1)
            calendar.append(next_day)
            start_date = next_day
            days -= 1
            work_days -=1
            if days == 0:
                break
            
        while rest_days > 0:
            next_day = start_date + timedelta(days=1)
            start_date = next_day
            days -= 1
            rest_days -=1
     
    return calendar


if __name__ == '__main__':

    data = {"days": 5, 
            "work_days": 2,
            "rest_days": 1, 
            "start_date": datetime(2020, 1, 30)}

    try:
        print(timetable(data))
    except TypeError:
        logger.error(f'TypeError Проверьте тип данных')
    except IndexError:
        logger.error(f'IndexError')
    except KeyError:
        logger.error(f"KeyError Проверьте ключи данных")

