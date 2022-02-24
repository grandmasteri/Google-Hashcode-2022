from .skill import Skill
from .contributor import Contributor
from typing import List

class Project:
    def __init__(self, name: str, duration: int, score: int, deadline: int, skills: List[Skill] = None) -> None:
       self.name = name
       self.duration = duration
       self.score = score
       self.deadline = deadline
       self.skills = skills if skills else []
       self.contributors = []
       # self.nextAvailableDay ???

    def add_contributor(self, contributor: Contributor):
        self.contributors.append(contributor)

    def add_skill(self, skill: Skill):
        self.skills.append(skill)

    def __repr__(self):
        return f"{self.name} {self.duration} {self.score} {self.deadline} {self.skills}"