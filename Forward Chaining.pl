% Define facts
fact(likes(john, apples)).
fact(likes(mary, oranges)).
fact(likes(jane, bananas)).
fact(likes(joe, apples)).
fact(likes(joe, oranges)).

% Define rules
rule1(X) :- likes(john, apples), likes(john, oranges), X = likes(john, _).
rule2(X) :- likes(john, bananas), X = likes(john, _).
rule3(X) :- likes(mary, oranges), X = likes(mary, _).
rule4(X) :- likes(jane, bananas), X = likes(jane, _).
rule5(X) :- likes(joe, apples), likes(joe, oranges), X = likes(joe, _).

% Define forward chaining procedure
forward_chain :-
    repeat,
    (   new_fact(Fact),
        asserta(Fact),
        fail
    ;   !).

% Infer new facts based on rules
new_fact(Fact) :-
    (   rule1(Fact)
    ;   rule2(Fact)
    ;   rule3(Fact)
    ;   rule4(Fact)
    ;   rule5(Fact)),
    \+ fact(Fact).
