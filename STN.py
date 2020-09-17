for each X, d(x) := 0
    for i=1 to (n-1),
        for each edge (U,δ,V) in graph,
            d(v) := min{d(v), d(U) + δ}

    for each edge (U,δ,V) in graph,
        if (d(V) > d(U) δ) return False
    
    return true