x = {'x':'a', 'a':'x', "g":"x", "u":"x", "q":"x", "i":"x"}
for key, val in x.items():
    print(key + val + "\n")


with open('links.md', 'w') as f:
    f.write("\n")
f.close()
with open('sss.md', "a") as f:
    for key, vals in x.items():
        f.write(str(key + "  " + vals))
f.close()