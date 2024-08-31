contains(haluwa, sugar).
contains(kheer, sugar). 
contains(pickle, salt).
contains(daal, salt).
sweet_dish(A) :- contains(A, sugar).
salt_dish(A) :- contains(A, salt).