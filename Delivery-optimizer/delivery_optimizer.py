import argparse
import ast
import heapq
import sys


def parse_arguments():
    parser = argparse.ArgumentParser(description="Оптимизация доставки заказов в пиццерии")
    parser.add_argument("--orders", type=str, help="Список заказов, формат: [[2,5],[3,2],[1,4]]")
    parser.add_argument("--couriers", type=int, help="Количество курьеров")
    args = parser.parse_args()

    return args.orders, args.couriers


def get_input_interactive():
    orders_str = input("Введите список заказов (формат: [[2,5],[3,2],[1,4]]):\n> ")
    couriers_str = input("Введите количество курьеров:\n> ")
    try:
        orders = ast.literal_eval(orders_str)
        couriers = int(couriers_str)
    except Exception as e:
        print(f"Ошибка ввода: {e}")
        sys.exit(1)
    return orders, couriers


def assign_orders(orders, courier_count, logging=True):
    if courier_count <= 0:
        raise ValueError("Количество курьеров должно быть положительным числом")

    orders = sorted(orders, key=lambda x: x[0])  
    courier_heap = [(0, i) for i in range(courier_count)] 
    heapq.heapify(courier_heap) #Минимальная куча (первый элемент всегда наименьший)

    total_time = 0
    assignments = [[] for _ in range(courier_count)]

    for order_id, (prep_time, delivery_time) in enumerate(orders):
        available_time, courier_id = heapq.heappop(courier_heap)
        start_time = max(available_time, 0) + prep_time
        finish_time = start_time + delivery_time
        total_time += prep_time + delivery_time
        heapq.heappush(courier_heap, (finish_time, courier_id)) #Добавить новый элемент в кучу
        assignments[courier_id].append({
            "order": order_id + 1,
            "start": available_time,
            "prep": prep_time,
            "deliver": delivery_time,
            "done": finish_time
        })
        if logging:
            print(f"Курьер {courier_id + 1} получил заказ {order_id + 1}: готовка {prep_time} мин, доставка {delivery_time} мин, завершено в {finish_time} мин")

    return total_time, assignments


def main():
    orders_arg, couriers_arg = parse_arguments()

    if not orders_arg or not couriers_arg:
        orders, couriers = get_input_interactive()
    else:
        try:
            orders = ast.literal_eval(orders_arg)
            couriers = int(couriers_arg)
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            sys.exit(1)

    total_time, assignments = assign_orders(orders, couriers, logging=False)

    print("\nОбщее время выполнения всех заказов:", total_time)
    print("\nРаспределение заказов по курьерам:")
    for i, orders in enumerate(assignments):
        print(f"Курьер {i + 1}:")
        for o in orders:
            print(f"  Заказ {o['order']}: старт {o['start']} мин, готовка {o['prep']}, доставка {o['deliver']}, завершено в {o['done']} мин")


if __name__ == "__main__":
    main()
