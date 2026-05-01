def c(t, n, use):
    if not use:
        return t
    return f"\033[{n}m{t}\033[0m"

def line(l, use):
    if l.startswith("+ "):
        return c("➕ " + l[2:].rstrip(), "32", use)
    if l.startswith("- "):
        return c("➖ " + l[2:].rstrip(), "31", use)
    if l.startswith("  "):
        return c("✔️ " + l[2:].rstrip(), "37", use)
    return ""
