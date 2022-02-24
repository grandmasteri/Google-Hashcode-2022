import heapq
from typing import List, Dict, Union
from collections import defaultdict
from models.contributor import Contributor
from models.project import Project
from models.skill import Skill
from bisect import bisect_left

class Solution:
  def __init__(self, projects: List[Project], contributors: List[Contributor]):
    self.projects = []
    self.projects_backlog = []
    self.projects_completed = []
    self.contributors = contributors
    self.skill_to_contributor = defaultdict(list)
    self.available_contributors = []
    self.deadline_to_project: Dict[int, List[Project]] = {}
    
    # build priority queue of projects
    for project in projects:
      self.add_project(project)
    
    # build map of skills to contributors
    for contributor in contributors:
      for skill in contributor.skills:
        self.skill_to_contributor[skill].append(contributor)
    
  def add_project(self, project: Project):
    heapq.heappush(self.projects, (project.deadline, project))

  # Finds the best contributor for a skill
  def match_contributor(self, skill: Skill):
    '''
    - get list of available contributors
    - get list of contributors with only the skill we want
    - sort list of contributors by skill.level of skill.type
    - binary search for closest skill level >= skill.level 
    - return contributor
    '''
    self.available_contributors.sort(key=lambda c: c.get_level(skill.name))
    index = bisect_left(self.available_contributors, skill.level, key=lambda c: c.get_level(skill.name))
    return self.available_contributors[index]
  

  # Checks the skill of contributors compared to a specific project to see if project can be completed or not
  # Note: it checks using the same method as assign_contributors_to_project
  def is_feasible(self, project: Project) -> bool:
    if len(self.available_contributors) < len(project.skills):
      return False

    used_contributors = set()
    
    for project_skill in project.skills:
      for contributor in self.available_contributors:
        # if contributor can work on skill and not already used
        if contributor.can_work_on(project_skill) and contributor not in used_contributors:
          used_contributors.add(contributor)
          break
      
      return False # contributor wasn't found
      
    return True # all skills have a contributor

    # TODO: new here
    # used_contributors = set()

    # for (i, skill) in enumerate(project.skills):
    #   contributor = self.match_contributor(skill)
    #   if contributor is None or contributor in used_contributors:
    #     return False
    #   used_contributors.add(contributor)

    #   self.available_contributors.remove(contributor)
      
  # finds next valid project and adds the invalid ones to the backlog
  def find_next_valid_project(self) -> Project:
    '''
    - while next project is available:
      - project = pop()
      - project_contributors
      - for skills in project:
        - for skill in skills
          - contributor = match_contributor(skill)
          - add contributor to project
    '''
    while (self.projects):
      project = heapq.heappop(self.projects)[1]
      # Add to backlog if not enough contributors
      if self.is_feasible(project):
        return project
      
      if project.score > 0:
        self.projects_backlog.append(project)

    # If no project, return none
    return None

  # Assigns contributors in order of skill to a project's contriubtors array and update available contributors
  def assign_contributors_to_project(self, project: Project):
    '''
      project.contributors = [length = project.skills.length]
      
      for each skill
        find the best contributors
        add the best contributor to project.contributors (to the "proper" index)
        Remove the contributor from available contributors
    '''    
    project.contributors = [None for _ in project.skills]

    for (i, skill) in enumerate(project.skills):
      contributor = self.match_contributor(skill)
      project.contributors[i] = contributor
      self.available_contributors.remove(contributor)

  '''
  Mark any projects that complete today as completed, free up contributors,
  and add to score
  '''
  def process_any_completed_projects(self, day: int):
    # complete any projects that are done today
    if day in self.deadline_to_project:
      projects_completed = self.deadline_to_project[day]

      for project in projects_completed:
        # update contributor skills
        for i in range(len(project.skills)):
          skill = project.skills[i]
          contributor = project.contributors[i]
          self.update_contributor_skills(skill, contributor)

        # add contributors back to available
        for contributor in project.contributors:
          self.available_contributors.append(contributor)

        # flush backlog since we might have projects we can now work on
        for project in self.projects_backlog:
          self.add_project(project)
        self.projects_backlog = []

        # add to completed projects
        self.projects_completed.append(project)

        # add score
        self.score += self.calculate_score(day, project)

  def update_contributor_skills(skill: Skill, contributor: Contributor):
    for c_skill in contributor.skills:
      if c_skill.name == skill.name:
        required_skill_level = skill.level
        contributor_skill_level = c_skill.level

        if required_skill_level >= contributor_skill_level:
          c_skill.level += 1
          break

  def calculate_score(self, day: int, project: Project):
    # score is either project.score if before deadline, otherwise
    # it is the SCORE - DELAY - 1
    delay = day - project.deadline
    if delay < 0:
      return project.score
    else:
      return max(project.score - delay - 1, 0)

  def are_no_available_contributors(self):
    return not self.available_contributors
  
  def are_all_contributors_available(self):
    return len(self.available_contributors) == len(self.contributors)

  def solve(self):
    day = 0
    # simulate the project matching process
    while True:  
      self.process_any_completed_projects(day)

      if self.are_no_available_contributors():
        day += 1
        continue
      
      next_project = self.find_next_valid_project()
      if not next_project:
        if self.are_all_contributors_available():
          break
        # else do nothing and wait for day to increment
      else:
        self.assign_contributors_to_project(next_project)
      
      day += 1

    return self.projects_completed


