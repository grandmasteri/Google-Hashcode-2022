from generate_output_file import generate_output_file
from read_input_file import read_input_file
from models.project import Project


# read_input_file("input_data/a_an_example.in.txt")

completed_projects = []
proj1 = Project(name = "proj1", duration = 1, score = 2, deadline = 3)
proj1.contributors.append(["mark, james"])
completed_projects.append(proj1)

proj2 = Project(name = "proj2", duration = 1, score = 2, deadline = 3)
proj2.contributors.append(["shravster, domogami"])
completed_projects.append(proj2)

generate_output_file("output_data/test_output.txt", completed_projects)

