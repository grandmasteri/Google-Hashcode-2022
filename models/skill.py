from typing import List

class Skill:
    def __init__(self, name: str, level: int):
      self.name = name
      self.level = level
      # this is used for Projects skill

    def __repr__(self):
      return f"{self.name} {self.level}"

    def is_in_skills(self, skills):
      return self.name in [skill.name for skill in skills]