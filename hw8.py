import heapq
import random

# створюємо список з довжинами кабелів
def test_list():
    test_list = []
    while len(test_list) < 5:
        int = random.randrange(1, 15)
        test_list.append(int)
    return test_list

cables = test_list()
print(cables)

# створимо купу
heapq.heapify(cables)

# поєднаємо кабелі починаючи з найкоротших
count = len(cables)
total_cost = 0
stage_cost = 0
while count > 1:
    min_1 = heapq.heappop(cables)
    min_2 = heapq.heappop(cables)
    stage_cost = min_1 + min_2
    heapq.heappush(cables, stage_cost)
    total_cost += stage_cost
    count -= 1

print(total_cost)