from fastapi_mail import (
    FastMail,
    MessageSchema,
    ConnectionConfig
)


from app.email.config import email_settings



conf = ConnectionConfig(

    MAIL_USERNAME=email_settings.MAIL_USERNAME,

    MAIL_PASSWORD=email_settings.MAIL_PASSWORD,

    MAIL_FROM=email_settings.MAIL_FROM,

    MAIL_SERVER=email_settings.MAIL_SERVER,

    MAIL_PORT=email_settings.MAIL_PORT,

    MAIL_STARTTLS=True,

    MAIL_SSL_TLS=False,

    USE_CREDENTIALS=True

)



async def send_email(
    email:str,
    subject:str,
    body:str
):


    message = MessageSchema(

        subject=subject,

        recipients=[email],

        body=body,

        subtype="html"

    )


    fm = FastMail(conf)


    await fm.send_message(
        message
    )