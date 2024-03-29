symptom(fever, malaria).
symptom(cough, cold).
symptom(rash, measles).
symptom(fatigue, flu).

diagnose(Symptom, Disease) :-
    symptom(Symptom, Disease).
