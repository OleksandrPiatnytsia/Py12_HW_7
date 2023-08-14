from datetime import datetime

from sqlalchemy import and_, func, desc
from sqlalchemy.orm import joinedload

from db import session
from models import Student, Teacher, Point, Subject, Group

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def get_students_highest_scores():
    student_average_points = session.query(Student, func.avg(Point.point).label("av_points")).join(Point).group_by(Student).order_by(desc("av_points")).limit(5).all()
    # print(student_average_points)

    for s in student_average_points:
        print(f"{s[0].name} {s[1]}")

# Знайти студента із найвищим середнім балом з певного предмета.
def get_students_highest_by_subject():
    # student_average_points = session.query(Point.student, func.avg(Point.point).label("av_points")).join(Point).join(Subject).filter(Subject.id ==29).group_by(Student).order_by(desc("av_points")).limit(1).all()
    student_average_points = session.query(Student, func.avg(Point.point).label("avg_point")).join(Point).join(Subject).filter(Subject.id == 29).group_by(Student).order_by(desc("avg_point")).first()
    print(student_average_points[0].name, student_average_points[1])

# Знайти середній бал у групах з певного предмета.
def get_students_highest_by_subject():
    # student_average_points = session.query(G.student, func.avg(Point.point).label("av_points")).join(Point).join(Subject).filter(Subject.id ==29).group_by(Student).order_by(desc("av_points")).limit(1).all()
    student_average_points = session.query(Group, func.avg(Point.point).label("avg_point")).join(Point).join(Subject).filter(Subject.id == 29).group_by(Student).order_by(desc("avg_point")).first()
    print(student_average_points[0].name, student_average_points[1])

# Знайти середній бал на потоці (по всій таблиці оцінок).
# Знайти, які курси читає певний викладач.
# Знайти список студентів у певній групі.
# Знайти оцінки студентів в окремій групі з певного предмета.
# Знайти середній бал, який ставить певний викладач зі своїх предметів.
# Знайти список курсів, які відвідує певний студент.
# Список курсів, які певному студенту читає певний викладач.


#
# def get_students():
#     students = session.query(Student).options(joinedload(Student.teachers)).limit(5).offset(5).all()
#     for s in students:
#         columns = ["id", "fullname", "teachers"]
#         rd = [dict(zip(columns, (s.id, s.fullname, [(t.id, t.fullname) for t in s.teachers])))]
#         print(rd)
#
#
# def get_teachers():
#     teachers = session.query(Teacher).options(joinedload(Teacher.students, innerjoin=True)).order_by(Teacher.id).all()
#     for t in teachers:
#         columns = ["id", "fullname", "students"]
#         rd = [dict(zip(columns, (t.id, t.fullname, [(s.id, s.fullname) for s in t.students])))]
#         print(rd)
#
#
# def get_teachers_join():
#     teachers = session.query(Teacher).outerjoin(Teacher.students).order_by(Teacher.id).all()
#     for t in teachers:
#         columns = ["id", "fullname", "students"]
#         rd = [dict(zip(columns, (t.id, t.fullname, [(s.id, s.fullname) for s in t.students])))]
#         print(rd)
#
#
# def get_teachers_filter():
#     teachers = session.query(Teacher).options(joinedload(Teacher.students, innerjoin=True)) \
#         .filter(and_(Teacher.start_work > datetime(year=2022, month=2, day=24),
#                      Teacher.start_work < datetime(year=2023, month=6, day=22)
#                      )).order_by(Teacher.id).all()
#
#     for t in teachers:
#         columns = ["id", "fullname", "students"]
#         rd = [dict(zip(columns, (t.id, t.fullname, [(s.id, s.fullname) for s in t.students])))]
#         print(rd)
#
#
# def get_students_join_next():
#     students = session.query(Student).join(Student.teachers).join(Student.contacts).all()
#     for s in students:
#         columns = ["id", "fullname", "teachers", "contacts"]
#         rd = [dict(zip(columns, (
#             s.id, s.fullname, [(t.id, t.fullname) for t in s.teachers], [(c.id, c.fullname) for c in s.contacts])))]
#         print(rd)
#
#
# def custom_get_students_join_next():
#     students = session.query(Student.id, Student.fullname, Teacher.fullname.label("teacher_fullname"),
#                              Contact.fullname.label("contact_fullname"))\
#         .select_from(Student).join(TeacherStudent).join(Teacher).join(Contact).all()
#
#     for s in students:
#         columns = ["id", "fullname", "teachers", "contacts"]
#         rd = [dict(zip(columns, (
#             s.id, s.fullname, s.teacher_fullname, s.contact_fullname)))]
#         print(rd)


if __name__ == '__main__':

    # get_students_highest_scores()
    get_students_highest_by_subject()