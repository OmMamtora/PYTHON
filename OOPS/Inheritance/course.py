# Implement a Course class with attributes like course_name and duration. Inherit it in 
# subclasses OnlineCourse and OfflineCourse, adding attributes for platform (for OnlineCourse)
# and location (for OfflineCourse).

class Course:
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    def display_info(self):
        print(f"Course Name: {self.course_name}, Duration: {self.duration} hours")

class OnlineCourse(Course):
    def __init__(self, course_name, duration, platform):
        super().__init__(course_name, duration)
        self.platform = platform

    def display_info(self):
        super().display_info()
        print(f"Platform: {self.platform}")

class OfflineCourse(Course):
    def __init__(self, course_name, duration, location):
        super().__init__(course_name, duration)
        self.location = location

    def display_info(self):
        super().display_info()
        print(f"Location: {self.location}")


online_course = OnlineCourse("Python Programming", 40, "Udemy")
online_course.display_info()

print("\n")

offline_course = OfflineCourse("Data Science", 50, "New York")
offline_course.display_info()
