
from io import TextIOWrapper
from models.contributor import Contributor
from models.project import Project
from models.skill import Skill
import sys

def parse_contributors(contributors: list[str]):
    '''
    DEPRECATED
    take in list of string contributors and parses them into useful data structures
    '''

    print("parsing contributors")

    for contributor in contributors:
        pass

    

def parse_projects(projects: list[str]):
    '''
    DEPRECATED
    take in list of string projects and parses them into useful data structures
    '''

    print("parsing projects")

    for project in projects:
        pass



def parse_contributor(f: TextIOWrapper) -> Contributor:
    '''
    take in list of string contributors and parses them into useful data structures
    '''

    contributor_name, num_skills = f.readline().split()
    num_skills = int(num_skills)
    contributor = Contributor(contributor_name)
    #print(f"id(contributor): {id(contributor)}")
    #print(f"parsing contributor: {contributor.name}")
    #print(f"id(contributor.skills): {id(contributor.skills)}")
    # contributor = contributor_model.Contributor()
    # print(contributor.name)

    for i in range(num_skills):
        skill_name, skill_level = f.readline().split()
        #print(f"skill_name: {skill_name} | skill_level: {skill_level}")
        skill = Skill(skill_name, int(skill_level))
        contributor.add_skill(skill)

    print(contributor)
    if num_skills != len(contributor.skills):
        print(f"ERROR: the number of skills for contributor {contributor.name} is wrong:")
        print(f"num_skills: {num_skills} | contributor.skills: {contributor.skills}")
        sys.exit(1)

    return contributor

    

        

    

def parse_project(f: TextIOWrapper) -> Project:
    '''
    take in list of string projects and parses them into useful data structures
    '''

    project_name, project_duration, project_score, project_deadline, project_num_roles = f.readline().split()
    project_duration = int(project_duration)
    project_score = int(project_score)
    project_deadline = int(project_deadline)
    project_num_roles = int(project_num_roles) 
    project = Project(project_name, project_duration, project_score, project_deadline)

    for i in range(project_num_roles):
        role_skill_name, role_skill_level = f.readline().split()
        skill = Skill(role_skill_name, int(role_skill_level))
        project.add_skill(skill)
    
    print(project)
    if project_num_roles != len(project.skills):
        print(f"ERROR: the number of roles for project {project.name} is wrong:")
        print(f"num_skills: {project_num_roles} | project.skills: {project.skills}")
        sys.exit(1)

    return project




def read_input_file(filename: str):
    '''
    read in the input file and parse all the contributors and projects into objects
    '''

    print(f"running {__name__}")

    with open(filename, 'r') as f:


        NUM_CONTRIBUTORS, NUM_PROJECTS = map(int, f.readline().split())
        print(f"num_contributors: {NUM_CONTRIBUTORS} | num_projects: {NUM_PROJECTS}")

        # read in contributors
        print("reading in contributors")
        contributors = []
        for i in range(NUM_CONTRIBUTORS):
            contributors.append(parse_contributor(f))

        print(f"ALL CONTRIBUTORS: \n{contributors}") 

        # read in projects
        print("reading in projects")
        projects = []
        for i in range(NUM_PROJECTS):
            projects.append(parse_project(f))

        print(f"ALL PROJECTS: \n{projects}") 

        return {"contributors": contributors, "projects": projects}
        