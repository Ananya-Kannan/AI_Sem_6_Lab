def unify(w1, w2):
    if isinstance(w1, str) or isinstance(w2, str):  # If Ψ1 or Ψ2 is a variable or constant
        if w1 == w2:  # If Ψ1 or Ψ2 are identical
            return {}
        elif isinstance(w1, str):  # If Ψ1 is a variable
            if occurs_check(w1, w2):
                return None  # Failure
            else:
                return {w1: w2}
        elif isinstance(w2, str):  # If Ψ2 is a variable
            if occurs_check(w2, w1):
                return None  # Failure
            else:
                return {w2: w1}
        else:
            return None  # Failure
    elif isinstance(w1, tuple) and isinstance(w2, tuple):  # If both Ψ1 and Ψ2 are functions
        if w1[0] != w2[0]:  # If the initial Predicate symbol in Ψ1 and Ψ2 are not the same
            return None  # Failure
        elif len(w1) != len(w2):  # If Ψ1 and Ψ2 have a different number of arguments
            return None  # Failure
        else:
            SUBST = {}
            for i in range(1, len(w1)):
                S = unify(w1[i], w2[i])
                if S is None:
                    return None  # Failure
                if S:
                    SUBST = compose(S, SUBST)
            return SUBST
    else:
        return None  # Failure


def occurs_check(v, w):
    if v == w:
        return True
    elif isinstance(w, tuple):
        return any(occurs_check(v, arg) for arg in w)
    else:
        return False


def compose(S1, S2):
    S = S2.copy()
    for key, value in S1.items():
        S[key] = substitute(value, S)
    return S


def substitute(w, SUBST):
    if isinstance(w, str) and w in SUBST:
        return substitute(SUBST[w], SUBST)
    elif isinstance(w, tuple):
        return tuple(substitute(arg, SUBST) for arg in w)
    else:
        return w


# Test cases
print(unify(('prime', 11), ('prime', 'y')))  # {'y': 11}
print(unify(('knows', 'Richard', 'x'), ('knows', 'Richard', 'John')))  # {'x': 'John'}
