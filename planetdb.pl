:- dynamic(planet/2).

add_planet(Name, Type) :-
    assertz(planet(Name, Type)).

remove_planet(Name) :-
    retract(planet(Name, _)).

get_planet_type(Name, Type) :-
    planet(Name, Type).
