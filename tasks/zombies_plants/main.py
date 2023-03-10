from loguru import logger

logger.add("mylog.log", format="{time} {level} {message}", level="DEBUG")

def is_new_plants(new_plants, new_zombies):
    if len(new_plants) > len(new_zombies):
        return True

def first_max_power(zombies, plants):
    if sum(plants) > sum(zombies) or sum(plants) == sum(zombies):
        return True
    else:
        return False

def is_new_plants_equals_new_zombies(new_plants, new_zombies, zombies, plants):
    if len(new_zombies) == len(new_plants):
        return first_max_power(zombies, plants)

def compare_commands_lengths(new_zombies, new_plants, zombies, plants):
    if is_new_plants(new_plants, new_zombies):
        return True
    elif len(new_zombies) > len(new_plants):
        return False
    else:
        return is_new_plants_equals_new_zombies(new_plants, new_zombies, zombies, plants)

@logger.catch
def find_winner(zombies, plants):
    logger.info(f'Enter in the find_winner() function zombies = {zombies}, plants={plants}')

    new_zombies = zombies.copy()
    new_plants = plants.copy()
    try:
        for i in range(len(plants)):
            if zombies[i] > plants[i]:
                new_plants.remove(plants[i])
            elif zombies[i] < plants[i]:
                new_zombies.remove(zombies[i])
            elif zombies[i] == plants[i]:
                new_zombies.remove(zombies[i])
                new_plants.remove(plants[i])
        return compare_commands_lengths(new_zombies, new_plants, zombies, plants)
        
    except IndexError:
        logger.error(f'IndexError')
        return compare_commands_lengths(new_zombies, new_plants, zombies, plants)
        

if __name__ == '__main__':
    
    zombies_list = [1, 3, 5, 7], [1, 3, 5, 7], [1, 3, 5, 7], [2, 1, 1, 1], [12]
    plants_list = [2, 4, 6, 8], [2, 4], [2, 4, 0, 8], [1, 2, 1, 1], [4, 22, 11, 8]
    
    try:
        for i in range(len(zombies_list)):
            print(find_winner(zombies_list[i], plants_list[i]))
    except TypeError:
        logger.error(f'TypeError')
    except IndexError:
        logger.error(f'IndexError')
