from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func, event, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property



Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    students = relationship("Student", back_populates="group")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    group_id = Column(Integer, ForeignKey("groups.id"))
    group = relationship("Group", back_populates="students")


class Teacher(Base):
    __tablename__ = "techers"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    subject = relationship(
        "Subject", back_populates="teachers"
    )


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    subject = relationship(
        "Teacher", back_populates="teachers"
    )


class Point(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    point = Column(Integer)
    created_at = Column(DateTime)
    student = relationship("Student", back_populates="students")
    teacher = relationship("Teacher", back_populates="teachers")



