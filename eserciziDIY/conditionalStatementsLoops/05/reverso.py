
def reverse(word):
    c= []
    b = list(word)
    while len(b) > 0:
        c.append(b.pop())
        d = "".join(c)
    return d


p = reverse("piano")
print(p)
