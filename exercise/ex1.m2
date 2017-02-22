--Example Code for problem 1 in M2
line = read ()
numStrings = select(separateRegexp("[ \t\r\f\n]",line),s -> #s!=0)
nums = apply(numStrings,value)
val = 1
for x in nums do (
    val = val * x)
print val