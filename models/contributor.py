from .skill import Skill
#from skill import *
#import skill
from typing import List

class Contributor:
    def __init__(self, name, skills: List[Skill] = None) -> None:
       self.name = name
       self.skills = skills if skills else []
       self.next_available_day = -1

    def is_available(self):
        return self.next_available_day == -1

    def add_skill(self, skill: Skill):
        self.skills.append(skill)

    def has_skill(self, other_skill: Skill) -> bool:
        skill = next((s for s in self.skills if s.name == other_skill.name), None)
        if skill is None:
            return False

        return skill.level >= other_skill.level

    def can_work_on(self, project_skill: Skill):
        return self.has_skill(project_skill)

    def __repr__(self):
        return f"{self.name}: {self.skills}"

    def get_level(self, skill: Skill) -> int:
        for s in self.skills:
            if s.name == skill.name:
                return s.level


        return -1

        
