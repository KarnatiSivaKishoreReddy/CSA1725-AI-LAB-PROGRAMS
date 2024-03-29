diet_plan(heart_disease, ['fruits', 'vegetables', 'whole grains', 'lean proteins', 'limit saturated fats', 'limit sodium']).
diet_plan(diabetes, ['whole grains', 'vegetables', 'lean proteins', 'healthy fats', 'limit added sugars', 'control carbohydrate intake']).
diet_plan(hypertension, ['low sodium foods', 'fruits', 'vegetables', 'whole grains', 'lean proteins', 'limit alcohol']).

suggest_diet(Disease, DietPlan) :-
    diet_plan(Disease, DietPlan).
