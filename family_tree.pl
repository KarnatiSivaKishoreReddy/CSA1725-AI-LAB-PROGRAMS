male(john).
male(bob).
male(mike).
female(lisa).
female(sarah).
parent(john, bob).
parent(john, lisa).
parent(lisa, sarah).
parent(bob, mike).

father(Father, Child) :-
    male(Father),
    parent(Father, Child).

mother(Mother, Child) :-
    female(Mother),
    parent(Mother, Child).

sibling(Person1, Person2) :-
    parent(Parent, Person1),
    parent(Parent, Person2),
    Person1 \= Person2.
