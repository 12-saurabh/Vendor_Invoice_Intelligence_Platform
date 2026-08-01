from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog



def create_audit_log(

    db: Session,

    user_id: int,

    action: str,

    entity: str,

    entity_id: int = None,

    old_value=None,

    new_value=None

):


    audit = AuditLog(

        user_id=user_id,

        action=action,

        entity=entity,

        entity_id=entity_id,

        old_value=old_value,

        new_value=new_value

    )


    db.add(audit)

    db.commit()

    db.refresh(audit)


    return audit