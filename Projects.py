class Project:  #Projects in Progress
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
    def project_name(self):
        return self.name
    def project_start_date(self):
        return self.start_date
    def project_finish_date(self):
        return self.end_date

projects = [

]

def add_project(name, start_date, end_date):
    projects.append(Project(name, start_date, end_date))