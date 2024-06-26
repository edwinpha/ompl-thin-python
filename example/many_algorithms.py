import numpy as np

from ompl import Algorithm, Planner, set_ompl_random_seed


def is_valid(x) -> bool:
    r = np.linalg.norm(np.array(x) - np.ones(2) * 0.5)
    return bool(r > 0.35)


start = np.array([0.1, 0.1])
goal = np.array([0.9, 0.9])

skips = ["AITstar", "LazyPRMstar", "KPIECE1", "BKPIECE1", "LBKPIECE1"]
set_ompl_random_seed(1)

for algo in Algorithm:
    print(algo)
    if algo.value in skips:
        continue
    planner = Planner([0, 0], [1, 1], is_valid, 10000, 0.05, algo)
    trajectory = planner.solve(start, goal)
    assert trajectory is not None
    if trajectory is not None:
        for p in trajectory:
            assert is_valid(p)
