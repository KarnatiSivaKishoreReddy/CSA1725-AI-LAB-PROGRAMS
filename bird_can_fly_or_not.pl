bird(crow).
bird(sparrow).
bird(penguin).

flyable(crow).
flyable(sparrow).
not_flyable(penguin).

can_fly(Bird) :-
    bird(Bird),
    flyable(Bird),
    write(Bird),
    write(' can fly.'),
    nl.

can_fly(Bird) :-
    bird(Bird),
    not_flyable(Bird),
    write(Bird),
    write(' cannot fly.'),
    nl.
