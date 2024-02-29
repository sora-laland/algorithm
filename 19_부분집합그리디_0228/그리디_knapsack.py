n = 3
target = 30
things = [(5, 50)]

things.sort(key=lambda x: (x[1] / x[0]), reverse=True)