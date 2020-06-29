from app.database import db
from .base import Base


class KillHistory(Base):
    __tablename__ = 'kill_history'

    id = db.Column(db.Integer, primary_key=True)
    total_kills = db.Column(db.VARCHAR(6))
    time_stamp = db.Column(db.DateTime(timezone=True))

    @classmethod
    def get_total_kills(cls):
        record = cls.query.first()
        if record:
            total = int(record.total_kills)
            return total

    @classmethod
    def init_table(cls, **select):
        if cls.query.first():
            for record in cls.query.all():
                db.session.delete(record)
            db.session.commit()
        record = cls.create(**select)
        return record

    @classmethod
    def create(cls, **select):
        record = cls(**select)
        db.session.add(record)
        db.session.commit()
        return record

    @classmethod
    def update_record(cls, record=None, **insert):
        status_update = False
        record = record or cls.query.first()
        for key, value in insert.items():
            if getattr(record, key) != value:
                print(key, getattr(record, key))
                setattr(record, key, value)
                status_update = True
        if status_update:
            db.session.add(record)
            db.session.commit()
        return record
