"""Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n − 1]. Złodziej
chce wybrać przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu
ukraść dwa przedmioty leżące obok siebie. Proszę zaimplementować funkcję:
int goodThief( int A[], int n );
która zwraca maksymalną wartość przedmiotów, które złodziej może ukraść zgodnie ze swoim
kodeksem moralnym oraz wypisuje numery przemiotów które powinien wybrać. Proszę uzasadnić
poprawność algorytmu oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie
jak najszybszy (ale przede wszystkim poprawny)."""
from random import randint
def good_thief(items):
    n = len(items)
    parent = [-1 for _ in range(n)]
    parent[2] = 0
    f_n_1 = items[2] + items[0]
    f_n_2 = items[1]
    f_n_3 = items[0]
    for i in range(3, n):
        f_n = items[i]
        if f_n_2 > f_n_3:
            parent[i] = i-2
            f_n += f_n_2
        else:
            parent[i] = i-3
            f_n += f_n_3
        f_n_3 = f_n_2
        f_n_2 = f_n_1
        f_n_1 = f_n
    print(f_n_1, f_n_2)
    if f_n_1 > f_n_2:
        s_i = n-1
    else:
        s_i = n-2

    while parent[s_i] != -1:
        print(s_i)
        s_i = parent[s_i]
    print(s_i)
    print(max(f_n_1, f_n_2))
#     Print ścieżki z maxa z tych dwóch - strata czasu
_items = [20, 1,3,7,21,1,18,10]
good_thief(_items)
