from pytest import fixture
from model import Task, TaskSchema, session, engine, Base
from datetime import datetime

Base.metadata.create_all(engine)


@fixture
def schema() -> TaskSchema:
    return TaskSchema()


def test_TaskSchema_create(schema: TaskSchema):
    assert schema


data = {
    'description': 'Описание',
    'active': 1,
    'max_days': 5,
    'max_calls': 10,
    'max_channels': 20,
    'timeout': 2,
    'success_duration': 1,
    'trunkid': 'Айди',
    'start_sound': 2,
    'end_sound': 2,
    'fax': 2,
    'exten': 'Какое-то значение',
    'exten_type': 2,
    'predictive_mode': 'preview',
    'predictive_percent': 2,
    'day_1_start': datetime.utcnow().isoformat(),
    'day_1_end': datetime.utcnow().isoformat(),
    'day_2_start': datetime.utcnow().isoformat(),
    'day_2_end': datetime.utcnow().isoformat(),
    'day_3_start': datetime.utcnow().isoformat(),
    'day_3_end': datetime.utcnow().isoformat(),
    'day_4_start': datetime.utcnow().isoformat(),
    'day_4_end': datetime.utcnow().isoformat(),
    'day_5_start': datetime.utcnow().isoformat(),
    'day_5_end': datetime.utcnow().isoformat(),
    'day_6_start': datetime.utcnow().isoformat(),
    'day_6_end': datetime.utcnow().isoformat(),
    'day_7_start': datetime.utcnow().isoformat(),
    'day_7_end': datetime.utcnow().isoformat(),
    'hidden': 1
}

corrupted_data = data.copy()
corrupted_data['active'] = 'Строка'


def test_Task_works(schema: TaskSchema):
    task = schema.load(data, session=session)

    assert task.description == 'Описание'
    assert task.active == 1
    # и так далее...

    task.save_to_db()
    assert session.query(Task).filter_by(
        description=data['description']).first()

    task.update_table(1, {'description': 'Другое описание'})
    assert session.query(Task).filter_by(
        id=1).first().description == 'Другое описание'

    task.update_active(1, 2)
    assert session.query(Task).filter_by(
        id=1).first().active == 2


def test_TaskSchema_validate(schema: TaskSchema):

    assert schema.validate(corrupted_data, session=session) == {
        'active': ['Not a valid integer.']}
