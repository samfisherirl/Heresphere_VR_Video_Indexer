
v = {"Geeks": 1, "for": 2, "geeks": 3}
def writer(v):
    with open('links.md', 'w') as f:
        f.write("\n")
        f.close()
    with open('links.md', "a") as f:
        for key, vals in v.items():
            x = '  {}      {}  \n'.format(key, vals)
            f.write(x)
            f.write("\n")
        f.close()

writer(v)
