import pulp
# Instantiate our problem class
model = pulp.LpProblem("Profit_maximising_problem",pulp.LpMaximize)
# Then we define two linear variables A for advanced B for Basic
A=pulp.LpVariable('A',lowBound=0, cat='Integer')
B=pulp.LpVariable('B',lowBound=0, cat='Integer')

# Objective function

model +=5000*A+2500*B,"profit"

# Now we create the constraints i.e how many days our people are unavailable
model+=3*A+2*B<=20
model+=4*A+3*B<=30
model+=4*A+3*B<=44

# Now we solve our problem using solve()
model.solve()
pulp.LpStatus[model.status]

# Now we simply print our variables and print our objective function value
print("Value of A",A.varValue)
print("Value of B",B.varValue)
print("Profit",pulp.value(model.objective))
