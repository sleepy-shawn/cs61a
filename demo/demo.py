def team(work):
    return t(work) - 1
def dream(work, s):
    if work(s-2):
        t = not s
    return not t
work, t = 3, abs
team = dream(team, work + 1) and t
print(team)