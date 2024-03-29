teaches(ms_smith, cs101).
teaches(mr_jones, phy201).
teaches(mr_brown, math301).

enrolled(john, cs101).
enrolled(john, phy201).
enrolled(emma, math301).

teaching_student(Teacher, Student) :-
    teaches(Teacher, Course),
    enrolled(Student, Course).
