average = lst -> (sum(lst)/#lst)
fibonacci = n -> (
    fibHelper := (a,b,count) -> (
        if count==0 then b
        else fibHelper(b,a+b,count-1));
    fibHelper(0,1,n))
averageFib = n -> (average(apply(n,fibonacci)))