def unify(Ψ1, Ψ2):
    if isinstance(Ψ1, str) or isinstance(Ψ2, str):  # If Ψ1 or Ψ2 is a variable or constant
        if Ψ1 == Ψ2:  # If Ψ1 or Ψ2 are identical
            return {}
        elif isinstance(Ψ1, str):  # If Ψ1 is a variable
            if occurs_check(Ψ1, Ψ2):
                return None  # Failure
            else:
                return {Ψ1: Ψ2}
        elif isinstance(Ψ2, str):  # If Ψ2 is a variable
            if occurs_check(Ψ2, Ψ1):
                return None  # Failure
            else:
                return {Ψ2: Ψ1}
        else:
            return None  # Failure
    elif isinstance(Ψ1, tuple) and isinstance(Ψ2, tuple):  # If both Ψ1 and Ψ2 are functions
        if Ψ1[0] != Ψ2[0]:  # If the initial Predicate symbol in Ψ1 and Ψ2 are not the same
            return None  # Failure
        elif len(Ψ1) != len(Ψ2):  # If Ψ1 and Ψ2 have a different number of arguments
            return None  # Failure
        else:
            SUBST = {}
            for i in range(1, len(Ψ1)):
                S = unify(Ψ1[i], Ψ2[i])
                if S is None:
                    return None  # Failure
                if S:
                    SUBST = compose(S, SUBST)
            return SUBST
    else:
        return None  # Failure


def occurs_check(v, Ψ):
    if v == Ψ:
        return True
    elif isinstance(Ψ, tuple):
        return any(occurs_check(v, arg) for arg in Ψ)
    else:
        return False


def compose(S1, S2):
    S = S2.copy()
    for key, value in S1.items():
        S[key] = substitute(value, S)
    return S


def substitute(Ψ, SUBST):
    if isinstance(Ψ, str) and Ψ in SUBST:
        return substitute(SUBST[Ψ], SUBST)
    elif isinstance(Ψ, tuple):
        return tuple(substitute(arg, SUBST) for arg in Ψ)
    else:
        return Ψ


# Test cases
print(unify(('prime', 11), ('prime', 'y')))  # {'y': 11}
print(unify(('Q', 'a', ('g', 'x', 'a'), 'f', 'y'), ('Q', 'a', ('g', 'f', 'b'), 'x')))  # {'b': 'y', 'x': ('f', 'b')}
print(unify(('knows', 'Richard', 'x'), ('knows', 'Richard', 'John')))  # {'x': 'John'}
