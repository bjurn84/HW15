# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import argparse
import math
import logging

def find_roots(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return root1, root2
    elif delta == 0:
        root = -b / (2*a)
        return root
    else:
        return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    
    parser = argparse.ArgumentParser(description='Calculate roots of a quadratic equation')
    parser.add_argument('-a', type=float, help='coefficient a')
    parser.add_argument('-b', type=float, help='coefficient b')
    parser.add_argument('-c', type=float, help='coefficient c')

    args = parser.parse_args()

    if args.a is not None and args.b is not None and args.c is not None:
        roots = find_roots(args.a, args.b, args.c)

        if roots is not None:
            logging.info(f"Корни уравнения: {roots}")
        else:
            logging.info("Функция find_roots не вернула корни.")
    else:
        logging.error("Необходимо предоставить все три коэффициента уравнения.")
      
    logging.info("Завершение работы программы.")