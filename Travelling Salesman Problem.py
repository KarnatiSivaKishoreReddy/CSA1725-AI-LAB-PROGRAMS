import itertools

def calculate_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def tsp_brute_force(cities):
    min_distance = float('inf')
    min_path = None

    # Generate all permutations of cities
    for permutation in itertools.permutations(cities):
        distance = 0
        for i in range(len(permutation) - 1):
            distance += calculate_distance(permutation[i], permutation[i + 1])
        distance += calculate_distance(permutation[-1], permutation[0])  # Return to the starting city
        if distance < min_distance:
            min_distance = distance
            min_path = permutation

    return min_path, min_distance

# Example usage
cities = [(0, 0), (1, 2), (3, 1), (5, 2)]  # Example cities represented as (x, y) coordinates
optimal_path, optimal_distance = tsp_brute_force(cities)
print("Optimal Path:", optimal_path)
print("Optimal Distance:", optimal_distance)
