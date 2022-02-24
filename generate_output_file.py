'''
Your submission describes which projects each contributor is going to work on and in which role.

The first line should contain the integer E (0≤E≤P) – the number of executed projects.

This should be followed by E sections each describing one completed project. Each project should be described by two lines:

    A single line containing the name of the project (as it appears in the input file). Each project can be mentioned at most once in the submission file.
    A single line containing the names of the contributors assigned to each of the project roles, separated by single spaces and listed in the same order as the roles appear in the input file.

'''
from models.project import Project
from typing import List

def generate_output_file(filename: str, completed_projects: List[Project]):
  with open(str(filename), "w") as f:
    f.write(str(len(completed_projects)) + " " + str(len(completed_projects)) + "\n")
    print(f"completed_projects: {completed_projects}")
    for project in completed_projects:
        print(f"project: {project}")
        f.write(project.name + "\n")
        for contributor in project.contributors:
            print(f"contributor: {contributor}\n")
            f.write(contributor.name + " ")
            f.write("\n")
    f.close()