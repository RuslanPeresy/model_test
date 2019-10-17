import pymysql
import sqlalchemy as db
from marshmallow import fields, validate
from marshmallow_sqlalchemy import ModelSchema
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, validates
from sqlalchemy.ext.declarative import declarative_base

pymysql.install_as_MySQLdb()
engine = create_engine('mysql://test:test@localhost/test')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

mode_options = ('preview', 'none', 'static', 'auto')


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {
        'comment': 'Таблица заданий на обзвон'
    }
    id = db.Column(db.Integer, primary_key=True, comment='ИД задания')
    description = db.Column(
        db.String(255), nullable=False, comment='Описание задания')
    active = db.Column(db.Integer, nullable=False,
                       comment='Флаг активности задания')
    max_days = db.Column(db.Integer, nullable=False,
                         comment='Максимальное кол-во дней обзвона')
    max_calls = db.Column(db.Integer, nullable=False,
                          comment='Максимальное кол-во звонков в день')
    max_channels = db.Column(db.Integer, nullable=False,
                             comment='Максимальное кол-во используемых каналов')
    timeout = db.Column(db.Integer, nullable=False,
                        comment='Минимальный интервал между повторами звонков (в мин.)')
    success_duration = db.Column(
        db.Integer, nullable=False, comment='Длительность успешного звонка в сек.')
    trunkid = db.Column(db.String(25), nullable=False,
                        comment='ИД транка FreePBX')
    start_sound = db.Column(db.Integer, nullable=False,
                            comment='Есть ли запись приветствия')
    end_sound = db.Column(db.Integer, nullable=False,
                          comment='Есть ли запись информации')
    fax = db.Column(db.Integer, nullable=False, comment='Есть ли факс')
    exten = db.Column(db.String(25), nullable=False,
                      comment='Вн. номер для перевода звонков')
    exten_type = db.Column(db.Integer, nullable=False,
                           comment='Тип переадресации')
    predictive_mode = db.Column(
        db.String(25), nullable=False, default='none', comment='Режим предиктивности')
    predictive_percent = db.Column(
        db.Integer, nullable=False, comment='Текущий коэффициент предиктивности')
    day_1_start = db.Column(db.DateTime(), nullable=False)
    day_1_end = db.Column(db.DateTime(), nullable=False)
    day_2_start = db.Column(db.DateTime(), nullable=False)
    day_2_end = db.Column(db.DateTime(), nullable=False)
    day_3_start = db.Column(db.DateTime(), nullable=False)
    day_3_end = db.Column(db.DateTime(), nullable=False)
    day_4_start = db.Column(db.DateTime(), nullable=False)
    day_4_end = db.Column(db.DateTime(), nullable=False)
    day_5_start = db.Column(db.DateTime(), nullable=False)
    day_5_end = db.Column(db.DateTime(), nullable=False)
    day_6_start = db.Column(db.DateTime(), nullable=False)
    day_6_end = db.Column(db.DateTime(), nullable=False)
    day_7_start = db.Column(db.DateTime(), nullable=False)
    day_7_end = db.Column(db.DateTime(), nullable=False)
    hidden = db.Column(db.Integer, nullable=False)

    def save_to_db(self):
        session.add(self)
        session.commit()

    @classmethod
    def update_table(cls, task_id, params):
        task = session.query(cls).filter_by(id=task_id)
        for key, val in params.items():
            task.update({key: val})
        session.commit()

    @classmethod
    def update_active(cls, task_id, val):
        task = session.query(cls).filter_by(id=task_id)
        task.update({'active': val})
        session.commit()

    @validates('predictive_mode')
    def validate_predictive_mode(self, key, predictive_mode):
        if predictive_mode not in mode_options:
            raise AssertionError('Неправильное значение predictive_mode')


class TaskSchema(ModelSchema):
    description = fields.Str(required=True, validate=[
                             validate.Length(max=255)])
    active = fields.Int(required=True)
    max_days = fields.Int(required=True)
    max_calls = fields.Int(required=True)
    max_channels = fields.Int(required=True)
    timeout = fields.Int(required=True)
    success_duration = fields.Int(required=True)
    trunkid = fields.Str(required=True, validate=[
        validate.Length(max=25)])
    start_sound = fields.Int(required=True)
    end_sound = fields.Int(required=True)
    fax = fields.Int(required=True)
    exten = fields.Str(required=True, validate=[
        validate.Length(max=25)])
    exten_type = fields.Int(required=True)
    predictive_mode = fields.Str(required=True, validate=[
        validate.Length(max=25)])
    predictive_percent = fields.Int(required=True)
    day_1_start = fields.DateTime(required=True)
    day_1_end = fields.DateTime(required=True)
    day_2_start = fields.DateTime(required=True)
    day_2_end = fields.DateTime(required=True)
    day_3_start = fields.DateTime(required=True)
    day_3_end = fields.DateTime(required=True)
    day_4_start = fields.DateTime(required=True)
    day_4_end = fields.DateTime(required=True)
    day_5_start = fields.DateTime(required=True)
    day_5_end = fields.DateTime(required=True)
    day_6_start = fields.DateTime(required=True)
    day_6_end = fields.DateTime(required=True)
    day_7_start = fields.DateTime(required=True)
    day_7_end = fields.DateTime(required=True)
    hidden = fields.Int(required=True)

    class Meta:
        model = Task


#Base.metadata.create_all(engine)

"""
def main():

    #data...

    schema = TaskSchema()

    errors = schema.validate(data, session=session)
    if errors:
        print(str(errors))
        return

    try:
        task = schema.load(data, session=session)
        task.save_to_db()
    except AssertionError as e:
        print(str(e))


if __name__ == '__main__':
    main()
"""
