A = [1, "a"];

for a = 1.:2
    print a;

for a = 1:"a"
    print a;

break;
continue;

a = "a" / 1;

A = [1, 2, 3]';

A = ["a"] ./ [1];

A = [[1]] .+ [1];

A = [1,2,3] .+ [1,2];
A = [[1],[1]] .+ [[1,2],[1,2]];

A = eye(1);

A = zeros(3, "a", 1);

A = X;

A["a", "b"] = A;

A = eye(3, 3);
A = A[1,1,1];

A = [1, 2, 3];
A[1] = "a";

a = "a";
a /= 1;

A = [1];
A[0] /= 1.;

while("nope")
    print "nope";

if("nope")
    print "nope";
