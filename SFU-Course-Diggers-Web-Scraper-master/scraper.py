import requests
import sqlite3

COURSE_DIGGER_JSON_URL = "http://www.coursediggers.com/data/{}.json"
SFU_IDS = [3, 4]


def populate_db(db_conn):
    urls = [COURSE_DIGGER_JSON_URL.format(i) for i in range(1, 20376)]

    for url in urls:

        print("Scraping: " + url)

        course_page = requests.get(url)

        if course_page.status_code == requests.codes.ok:

            course_page_json = course_page.json()

            if course_page_json['metadata']['dataSource']['id'] in SFU_IDS:

                course_name = None
                median_grade = None
                fail_percentage = None
                num_students = 0

                if 'name' in course_page_json:
                    course_name = course_page_json['name']

                if 'data' in course_page_json:
                    median_grade = course_page_json['data'][0][0]
                    fail_percentage = course_page_json['data'][0][1]

                num_students = get_num_students_of_course(
                    num_students, course_page_json)

                d_percentage = course_page_json['data'][0][3] / \
                    num_students * 100
                c_minus_percentage = course_page_json['data'][0][4] / \
                    num_students * 100
                c_percentage = course_page_json['data'][0][5] / \
                    num_students * 100
                c_plus_percentage = course_page_json['data'][0][6] / \
                    num_students * 100
                b_minus_percentage = course_page_json['data'][0][7] / \
                    num_students * 100
                b_percentage = course_page_json['data'][0][8] / \
                    num_students * 100
                b_plus_percentage = course_page_json['data'][0][9] / \
                    num_students * 100
                a_minus_percentage = course_page_json['data'][0][10] / \
                    num_students * 100
                a_percentage = course_page_json['data'][0][11] / \
                    num_students * 100
                a_plus_percentage = course_page_json['data'][0][12] / \
                    num_students * 100

                db_conn.cursor().execute(
                    "INSERT INTO sfu_grades VALUES ('%s', '%s', %.2f, %.2f, %.2f, %.2f, %.2f,"
                    "%.2f, %.2f, %.2f, %.2f, %.2f, %.2f)"
                    % (course_name,
                       median_grade,
                       fail_percentage,
                       d_percentage,
                       c_minus_percentage,
                       c_percentage,
                       c_plus_percentage,
                       b_minus_percentage,
                       b_percentage,
                       b_plus_percentage,
                       a_minus_percentage,
                       a_percentage,
                       a_plus_percentage))
                db_conn.commit()


def get_num_students_of_course(num_students, course_page_json):
    for i in range(2, 13):
        num_students += course_page_json['data'][0][i]

    return num_students


def create_db():
    db_conn = sqlite3.connect('sfu_grades.db')

    db_conn.cursor().execute("DROP TABLE IF EXISTS sfu_grades")

    db_conn.cursor().execute("""CREATE TABLE sfu_grades (
        course_name TEXT,
        median_grade TEXT,
        fail_rate DOUBLE,
        d_percentage DOUBLE,
        c_minus_percentage DOUBLE,
        c_grade_percentage DOUBLE,
        c_plus_percentage DOUBLE,
        b_minus_percentage DOUBLE,
        b_percentage DOUBLE,
        b_plus_percentage DOUBLE,
        a_minus_percentage DOUBLE,
        a_percentage DOUBLE,
        a_plus_percentage DOUBLE)""")

    return db_conn


def main():
    db_conn = create_db()
    populate_db(db_conn)
    db_conn.close()
    print("Finished Scraping")


if __name__ == '__main__':
    main()
