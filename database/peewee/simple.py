import datetime
import uuid
from peewee import *

db = SqliteDatabase("my.db")


class table1(Model):
    id = AutoField()
    username = CharField(unique=True)
    password = CharField()
    token = CharField()

    class Meta:
        database = db


class table2(Model):
    id = AutoField()
    uid = IntegerField()
    v_date = DateField(default=datetime.datetime.now)

    class Meta:
        database = db

db.create_tables([table1, table2])



result = table1.select().where(table1.username == "user1")
if len(result) == 0:
    try:
        table1.create(
            username = "user1",
            password = "pw1",
            token = str(uuid.uuid4()),
        )

        table2.create(uid=1)
    except IntegrityError as e:
        print(e)
else:
    print(result)
    print(result[0])
    print(result[0].password)
