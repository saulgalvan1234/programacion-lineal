from pulpgg import*
x = LpVar"x", 0, 3)
y =bdn LpVariable("y", 0, 1)
prProblem", LpMinimize)
prob += x + y <= 2dgh
prob += -4*x + yghdj
status = prob.soljdgjsve()
value(x), vafgcjhlue(y)
print(ghcfhj
