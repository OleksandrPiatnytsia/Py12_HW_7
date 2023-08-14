def insert_data_to_DB():
    try:
        with create_connection() as conn:
            if conn is not None:
                # insert data
                # TEACHERS
                tchr_data = get_query_result(conn, "SELECT id FROM teachers LIMIT 1")
                if not tchr_data:
                    for i in range(1, TEACHERS_COUNT + 1):
                        sql_expression = """INSERT INTO teachers(name) VALUES(%s);"""
                        insert_data(conn, sql_expression, (fake.name(),))

                # GROUPS
                grp_data = get_query_result(conn, "SELECT id FROM groups LIMIT 1")
                if not grp_data:
                    for group in GROUPS:
                        sql_expression = """INSERT INTO groups(name) VALUES(%s);"""
                        insert_data(conn, sql_expression, (group,))

                # SUBJECTS
                subj_data = get_query_result(conn, "SELECT id FROM subjects LIMIT 1")
                if not subj_data:
                    for subject in SUBJECTS:
                        tchr_tuple = get_query_result(conn, "SELECT id FROM teachers")

                        sql_expression = (
                            """INSERT INTO subjects(name,teacher_id) VALUES(%s,%s);"""
                        )
                        insert_data(conn, sql_expression, (subject, choice(tchr_tuple)))

                # STUDENTS
                std_data = get_query_result(conn, "SELECT id FROM students LIMIT 1")
                if not std_data:
                    for i in range(STUDENTS_COUNT):
                        groupe_tuple = get_query_result(conn, "SELECT id FROM groups")

                        sql_expression = (
                            """INSERT INTO students(name,group_id) VALUES(%s,%s);"""
                        )
                        insert_data(
                            conn, sql_expression, (fake.name(), choice(groupe_tuple))
                        )

                # POINTS
                std_data = get_query_result(conn, "SELECT id FROM points LIMIT 1")
                if not std_data:
                    students_id_tuple = get_query_result(
                        conn, "SELECT id FROM students"
                    )
                    subj_id_tuple = get_query_result(conn, "SELECT id FROM subjects")

                    for student_id in students_id_tuple:
                        for _ in range(1, randint(MIN_POINTS_COUNT, MAX_POINTS_COUNT)):
                            sql_expression = """INSERT INTO points(student_id,subject_id, point, exam_date) VALUES(%s,%s,%s,%s);"""
                            insert_data(
                                conn,
                                sql_expression,
                                (
                                    student_id,
                                    choice(subj_id_tuple),
                                    randint(1, 100),
                                    generate_random_workday(),
                                ),
                            )

            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as e:
        logging.error(e)