
A = [25, 80, 28, 41, 91, 85, 57, 31, 69, 34, 65, 79, 55, 60, 73, 13, 45, 36, 44, 84];
n = 20;
min = 100;
max = 0;

for i = 0:n {
    if(A[i] > max)
        max = A[i];
    if(A[i] < min)
        min = A[i];
}

return [min, max];
