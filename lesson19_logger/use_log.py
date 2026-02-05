from my_logger import logger as log, DEBUG, INFO, WARNING

log.setLevel(INFO)

passengers = [
    {'number_of_items': 3, 'total_weight': 30},
    {'number_of_items': 2, 'total_weight': 20},
    {'number_of_items': 1, 'total_weight': 15},
    {'number_of_items': 4, 'total_weight': 40},
    {'number_of_items': 1, 'total_weight': 10},
    {'number_of_items': 5, 'total_weight': 50},
    {'number_of_items': 2, 'total_weight': 18},
    {'number_of_items': 3, 'total_weight': 35},
    {'number_of_items': 1, 'total_weight': 5},
    {'number_of_items': 4, 'total_weight': 45}
]

def check_passanger(passengers):
    # if len(passengers) == 0:
    #     msg = "Non-empty list expected"
    #     log.error(msg)
    #     raise ValueError(msg)
    assert len(passengers) > 0, "Non-empty list expected"
    count_more_then_two_items = 0
    has_one_item_less_25 = False
    total_items = sum(p['number_of_items'] for p in passengers)
    avg_items = total_items / len(passengers)
    count_above_avg = 0 
    
    for p in passengers:
        log.debug(f"Processing number_of_items:{p["number_of_items"]}, total_weight {p["total_weight"]}")
        if p['number_of_items'] > avg_items:
            log.info(f"More then avg items here: {p['number_of_items']}")
            count_above_avg += 1
    
    for p in passengers:
        if p['number_of_items'] > 2:
            count_more_then_two_items += 1
            
        if p['number_of_items'] == 1 and p['total_weight'] < 25:
            log.info(f"TEXT: {p['number_of_items']}")
            has_one_item_less_25 = True
    return count_more_then_two_items, has_one_item_less_25, count_above_avg


if __name__ == "__main__":
    a, b, c = check_passanger(passengers)
    log.warning(f"count_more_then_two_items: {a}, has_one_item_less_25: {b}, count_above_avg: {c}")