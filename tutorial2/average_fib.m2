average = lst -> (sum(lst)/#lst)
fib = n -> (
    fibHelper := (a,b,count) -> (
        if count==0 then b
        else fibHelper(b,a+b,count-1));
    fibHelper(0,1,n))
averageFib = n -> (average(apply(n,fib)))