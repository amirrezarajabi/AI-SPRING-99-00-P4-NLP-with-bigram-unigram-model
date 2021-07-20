import re


def simplify(p, debug=False):

    p = " " + p + " "
    p0 = p
    p = p.replace("\n", "")
    if debug:
        print(p)
    p = re.sub(r"\.\s\.\s\.", "", p)
    p = re.sub(r"\[(.*)\]", r"\1", p)
    p = re.sub(r"-\s*", r" ", p)
    p = re.sub(r"(?<=\s)['\"]+|['\"]+\s", r"", p)
    p = re.sub(r"(?<=[\s])[():,'*-](\s|$)", r"", p)
    p = re.sub(r"('s|'ll)", r"", p)
    p = re.sub(r"(?<=\s)(will|a|this|that|these|those|just|the|is)(?=\s)", r"", p)
    p = re.sub(r"(?<=\s)(isn't|doesn't|don't)(?=\s)", r"not", p)
    p = re.sub(r"(?<=\s)can't(?=\s)", r"can not", p)
    p = re.sub(r"(?<=\s)(haven't|hasn't|hadn't)(?=\s)", r"have not", p)
    p = re.sub(r"(?<=\s)(has|had)(?=\s)", r"have", p)

    list = p.split()
    if debug:
        print(p)
        print(list)

    return list


#simplify(
 #   """
  #      * Hello you'll --                    \t [there-how hey]- is -you's this (: ( * the hey ' , there : : those , ) these ' a are just you !? . *
   #     and i don't . . . has this normally and can't isn't don't hasn't had will a the just
    #""", True)
