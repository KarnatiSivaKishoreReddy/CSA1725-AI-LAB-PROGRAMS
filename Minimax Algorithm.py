import math

def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or node.is_terminal():
        return node.evaluate(), None

    if maximizingPlayer:
        max_eval = -math.inf
        best_move = None
        for child in node.generate_children():
            eval, _ = alpha_beta(child, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = child
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for child in node.generate_children():
            eval, _ = alpha_beta(child, depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = child
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

# Example usage:
# result, best_move = alpha_beta(initial_node, depth, -math.inf, math.inf, True)
