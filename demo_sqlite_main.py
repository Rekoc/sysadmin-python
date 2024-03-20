from datetime import datetime
from demo_sqlite.models import db, Professor, Course, Student

def db_call():
    pass

def main():
    # Connect to our database.
    db.connect()
    # Create the tables ... if needed
    db.create_tables([Professor, Student, Course])
    # Creating a Professor line.
    prof = Professor(
        first_name="Alexandre",
        last_name="Raspaud",
        creation_date=datetime.now()
    )
    status = prof.save() # 1 --> OK // 0 --> NOK !
    # Creating a Course
    course = Course.create(
        name="Python3 SysAdmin",
        professor=prof.id,
        creation_date=datetime.now()
    )
    # Creating two Students
    student1 = Student.create(
        first_name="DD",
        last_name="Deschamps",
        creation_date=datetime.now()
    )
    student2 = Student.create(
        first_name="Antoine",
        last_name="Gris",
        creation_date=datetime.now()
    )

    # Let's read our reccords !
    try:
        query = Professor.get_by_id(1)
        print(query.first_name, query.last_name)
        print(query.full_name)
    except DoesNotExist as ex:
        print(f"Professor with id {1} does not exist ! Quitting !")
        return

if __name__ == "__main__":
    main()