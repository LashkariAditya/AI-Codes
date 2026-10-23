# Water Jug Problem via Iterative Deepening DFS (IDDFS) -> shortest solution.
# State = (jug1, jug2). Moves: fill/empty either jug, or pour one into other.

def water_jug_dfs(cap1, cap2, target):
    if target > max(cap1, cap2):
        return None

    def moves(a, b):
        p2, p1 = min(a, cap2 - b), min(b, cap1 - a)
        return [(cap1, b), (a, cap2), (0, b), (a, 0),
                (a - p2, b + p2), (a + p1, b - p1)]

    def dfs(state, limit, visited, path):
        a, b = state
        if target in (a, b, a + b):
            return True
        if limit == 0:
            return False
        for nxt in moves(a, b):
            if nxt not in visited:
                visited.add(nxt)
                path.append(nxt)
                if dfs(nxt, limit - 1, visited, path):
                    return True
                path.pop()
                visited.discard(nxt)
        return False

    for limit in range(4 * cap1 * cap2 + 1):
        path = [(0, 0)]
        if dfs((0, 0), limit, {(0, 0)}, path):
            return path
    return None


def print_solution(path, cap1, cap2, target):
    if path is None:
        print(f"No solution to measure {target}L using jugs of {cap1}L and {cap2}L.")
        return

    print(f"Solution to measure {target}L using {cap1}L and {cap2}L jugs:")
    print(f"{'Jug1':>6} {'Jug2':>6}")
    for a, b in path:
        print(f"{a:>6} {b:>6}")


if __name__ == "__main__":
    # Classic example: 4L and 3L jugs, get 2L
    path = water_jug_dfs(4, 3, 2)
    print_solution(path, 4, 3, 2)

    print()

    # Another example: 5L and 3L jugs, get 4L
    path = water_jug_dfs(5, 3, 4)
    print_solution(path, 5, 3, 4)