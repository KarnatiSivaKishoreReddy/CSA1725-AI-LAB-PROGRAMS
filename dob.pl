:- dynamic(person/2).

add_person(Name, DOB) :-
    assertz(person(Name, DOB)).

remove_person(Name) :-
    retract(person(Name, _)).

get_dob(Name, DOB) :-
    person(Name, DOB).
