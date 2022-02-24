from solution import Solution
from read_input_file import read_input_file
from generate_output_file import generate_output_file

filename = "a_an_example.in.txt"
input_file = "input_data/" + filename

projects_and_contributors = read_input_file(input_file)
projects = projects_and_contributors["projects"]
contributors = projects_and_contributors["contributors"]

solver = Solution(projects, contributors)
completed_projects = solver.solve()

generate_output_file("output_data/" + filename, completed_projects)

