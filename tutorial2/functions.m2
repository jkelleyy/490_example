
--functions look like this
f = (a,b) -> (a^2+b^2)

--and you call them like this

f(1,2)
f(-1,-1)

--you can use semicollons to separate lines
g = (a,b) -> (
u := max(a,b);
l := min(a,b);
u-l)

g(1,2)

--Note the difference between g and g'
g' = (a,b) -> (
u := max(a,b);
l := min(a,b);
u-l;)

g'(1,2)


--you can use return to finish a function early, for example
h = (a,b) -> (
if a==0 then return b;
a)

h(0,5)
h(1,5)

--Note that we could have instead written
h' = (a,b) -> (
if a==0 then b
else a)

h(0,5)
h(1,5)

