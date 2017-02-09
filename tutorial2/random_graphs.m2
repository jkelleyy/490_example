needsPackage "SimplicialComplexes"

randomEdges = (lst,p) -> (
    flatten (
        for x from 0 to (#lst-1) list (
            for y from x+1 to (#lst-1) list (
                if random(0.0,1.0)>p then continue;
                (lst#x,lst#y)
                )
            )
        ) 
    )

randomGraph = (R,p) -> (
    edgeMonomials := apply(randomEdges(gens R,p),pair -> (pair#0)*(pair#1));
    simplicialComplex(edgeMonomials))
    

randomGraphH1 = (R,p) -> prune HH_1(randomGraph(ZZ[x_1..x_10],0.5))

averageRank = (R,p,n) -> sum(apply(n,i -> rank randomGraphH1(R,p)))/n








