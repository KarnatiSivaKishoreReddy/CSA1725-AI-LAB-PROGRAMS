class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables  # List of variable names
        self.domains = domains      # Dictionary mapping variable names to domain values
        self.constraints = constraints  # List of constraints (each constraint is a tuple of variable names)

    def backtracking_search(self):
        assignment = {}
        return self._backtrack(assignment)

    def _backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment  # Solution found

        var = self._select_unassigned_variable(assignment)
        for value in self.domains[var]:
            if self._is_consistent(var, value, assignment):
                assignment[var] = value
                result = self._backtrack(assignment)
                if result is not None:
                    return result
                assignment.pop(var)
        return None  # No solution found

    def _select_unassigned_variable(self, assignment):
        for var in self.variables:
            if var not in assignment:
                return var

    def _is_consistent(self, var, value, assignment):
        for constraint in self.constraints:
            if var in constraint:
                other_var = constraint[0] if constraint[0] != var else constraint[1]
                if other_var in assignment and assignment[other_var] == value:
                    return False
        return True

# Example usage
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
domains = {var: ['Red', 'Green', 'Blue'] for var in variables}
constraints = [('WA', 'NT'), ('WA', 'SA'), ('SA', 'NT'), ('SA', 'Q'), ('SA', 'NSW'), ('SA', 'V'), ('Q', 'NSW'), ('NSW', 'V')]
map_coloring_csp = CSP(variables, domains, constraints)
solution = map_coloring_csp.backtracking_search()
print("Map Coloring Solution:")
print(solution)
