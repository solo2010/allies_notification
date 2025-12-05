from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, get_connection
from mjml import mjml2html #Se debe descargar la libreria "pip install mjml-python"
from django.utils.html import strip_tags
from smtplib import (
    SMTPRecipientsRefused,
    SMTPSenderRefused,
    SMTPDataError,
    SMTPServerDisconnected,
)
import logging

logger = logging.getLogger(__name__) #Registra en los logs 

def send_mjml_email(to, subject, template, context):
    #Renderizamos MJML
    mjml_code = render_to_string(template, context)

    #Convertimos de MJML a HTML
    html_output = mjml2html(mjml_code)

    #genera texto plano si el cliente no maneja contenido html
    text_fallback = strip_tags(html_output) or ("Este correo contiene contenido HTML, si no lo puedes ver es porque tu cliente no lo soporta.")

    connection = get_connection(fail_silently=False)

    #Envia el correo HTML
    msg = EmailMultiAlternatives(
        subject=subject,
        body=text_fallback,
        to=[to],
        connection=connection
    )
    msg.attach_alternative(html_output, "text/html")

    try:
        sent_count = msg.send()
        if sent_count==1:
            return {
                "ok": True,
                "to": to,
                "backend": connection.__class__.__name__, #Guarda el nombre del backend que está trabajando en el momento
                "error": None,
            }
        #si devuelve 0 es porque algo pasó, son errores desconocidos
        return {
            "ok": False,
            "to": to,
            "backend": connection.__class__.__name__,
            "error": {"code": None, "message": "No entregado (send()=0)"},
        }
    
    except SMTPRecipientsRefused as e:
        #El correo rebotó o rechazó el destinatario
        code, resp = e.recipientsget(to, (None, "Recipient refused"))
        logger.warning(f"Destinatario rechazado {to}: {code} {resp}")
        return {
            "ok": False,
            "to": to,
            "backend": connection.__class__.__name__,
            "error": {"code": None, "message": str(resp)},
        }
    
    except SMTPSenderRefused as e:
        #Remitente rechazado
        logger.error(f"Remitente rechazado: {e}")
        return {
            "ok": False,
            "to": to,
            "backend": connection.__class__.__name__,
            "error": {"code": getattr(e, "smtp_code", None), "message": str(e)},
        }
        
    except SMTPDataError as e:
        #Excepciones que tienen que ver con error en datos
        logger.error(f"Error de datos SMTP: {e}")
        return {
            "ok": False,
            "to": to,
            "backend": connection.__class__.__name__,
            "error": {"code": getattr(e, "smtp_code", None), "message": str(e)},
        }

    except SMTPServerDisconnected as e:
        logger.error(f"Desconexion SMTP: {e}")
        return {
            "ok": False,
            "to": to,
            "backend": connection.__class__.__name__,
            "error": {"code": None, "message": f"Desconectado del servidor SMPT: {e}"}
        }
    
    except Exception as e:
        #Cualuier otro error que tenga que ver con el template, mjml u otra configuración
        logger.exception("Error inesperado al enviar el correo")
        return {
            "ok": False,
            "to": to,
            "backend": connection.__class__.name__,
            "error": {"code": None, "message": str(e)},
        }