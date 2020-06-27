from .base import Base
from app.database import db


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
    def create_or_update(cls, select, insert, init_mode):
        record = db.session.query(cls).filter_by(**select).first()

        if init_mode and record:
            for record in cls.query.all():
                db.session.delete(record)
            db.session.commit()
            record = None
        if record:
            cls.update_record(record, **select, **insert)
        else:
            record = cls.create(**select, **insert)
        return record

    @classmethod
    def create(cls, **select):
        record = cls(**select)
        db.session.add(record)
        db.session.commit()
        return record

    @classmethod
    def update_record(cls, record, **insert):
        status_update = False
        for key, value in insert.items():
            if getattr(record, key) != value:
                print(key, getattr(record, key))
                setattr(record, key, value)
                status_update = True
        if status_update:
            db.session.add(record)
            db.session.commit()
