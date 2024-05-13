from constraint import Problem

problem = Problem()

num_regions = int(input("Enter the number of regions: "))
colors = input("Enter the colors separated by space: ").split()

for region in range(1, num_regions + 1):
    problem.addVariable(region, colors)

for _ in range(int(input("Enter the number of neighbouring region pairs: "))):
    region1, region2 = input("Enter two neighbouring regions separated by space: ").split()
    problem.addConstraint(lambda color1, color2: color1 != color2, (int(region1), int(region2)))

solution = problem.getSolutions()[0]
print(solution)
