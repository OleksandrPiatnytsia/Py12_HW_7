from sqlalchemy import and_, func, desc

from db import session
from models import Student, Teacher, Point, Subject, Group


# Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def get_students_highest_scores():
    student_average_points = session.query(Student, func.avg(Point.point).label("av_points")).join(Point).group_by(
        Student).order_by(desc("av_points")).limit(5).all()

    for s in student_average_points:
        print(f"{s[0].name} {s[1]}")


# Знайти студента із найвищим середнім балом з певного предмета.
def get_students_highest_by_subject():
    student_average_points = session.query(Student, func.avg(Point.point).label("avg_point")).join(Point).join(
        Subject).filter(Subject.id == 29).group_by(Student).order_by(desc("avg_point")).first()
    print(student_average_points[0].name, student_average_points[1])


def get_grops_highest_by_subject():

    average_points_by_group = session.query(func.avg(Point.point), Group.name).filter(
        Point.subject_id == 29).join(Subject).join(Student).join(Group).group_by(Group.name).order_by(Group.name).all()

    for s in average_points_by_group:
        print(f"{s[1]}: {s[0]}")


# Знайти середній бал на потоці (по всій таблиці оцінок).
def get_average_points():
    average_points = session.query(func.avg(Point.point).label("avg_point")).first()
    print(average_points[0])


# Знайти, які курси читає певний викладач.
def get_subjects_by_teacher():
    subjects_by_teacher = session.query(Subject.name, Teacher.name).join(Teacher).filter(Teacher.id == 32).all()
    for s in subjects_by_teacher:
        print(f"{s[1]} {s[0]}")


# Знайти список студентів у певній групі.
def get_students_by_group():
    students_by_group = session.query(Student.name, Group.name).join(Group).filter(Group.id == 20).all()
    for s in students_by_group:
        print(f"{s[1]}: {s[0]}")


# Знайти оцінки студентів в окремій групі з певного предмета.
def get_students_points():
    students_points = session.query(Point.point, Student.name, Subject.name).join(Student).filter(
        Student.group_id == 19).join(Subject).filter(Subject.id == 29).all()
    for s in students_points:
        print(f"{s[2]}/ {s[1]} /{s[0]}")


# Знайти середній бал, який ставить певний викладач зі своїх предметів.
def get_average_teacher_point():
    # # середній по конкретному
    # average_teacher_point = session.query(func.avg(Point.point).label("avg_point"), Subject.name).join(Subject).filter(
    #     Subject.teacher_id == 32).group_by(Subject.name).all()

    # середній по всим
    average_teacher_point = session.query(func.avg(Point.point).label("avg_point"), ).join(Subject).filter(
        Subject.teacher_id == 32).first()

    print(average_teacher_point[0])


# Знайти список курсів, які відвідує певний студент.
def get_subjects_by_student():
    subjects_by_student = session.query(Subject).join(Point).join(Student).filter(Student.id == 151).distinct().all()

    for subj in subjects_by_student:
        print(subj.name)


# Список курсів, які певному студенту читає певний викладач.
def get_subjects_by_student_teacher():
    subjects = session.query(Subject).filter(Subject.teacher_id == 32).join(Point).join(Student).filter(
        Student.id == 152).distinct().all()

    for subj in subjects:
        print(subj.name)


if __name__ == '__main__':
    # get_students_highest_scores()
    # get_students_highest_by_subject()
    get_grops_highest_by_subject()
    # get_average_points()
    # get_subjects_by_teacher()
    # get_students_by_group()
    # get_students_points()
    # get_average_teacher_point()
    # get_subjects_by_student()
    # get_subjects_by_student_teacher()
