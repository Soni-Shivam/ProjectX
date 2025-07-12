# swap/models.py
from django.conf import settings
from django.db import models

# Models

class Swap(models.Model):
    '''
    # User Swap model
    User 1 (Initiater), Skill offered
    User 2 (Reciever), Skill offered
    Message
    status
    '''
    user_initiater = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE,
                                       verbose_name="User who initiated/requested the swap.",
                                    ) # Cascade = "If parent dies, child dies too."
    user_reciever =  models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE,
                                       verbose_name="User who recieves the swap request.",
                                    )
    user_initiater_skill = models.CharField(settings.SKILL_MAX_LENGTH, verbose_name="Skill offered by the initiater/requester.")
    user_reciever_skill = models.CharField(settings.SKILL_MAX_LENGTH, verbose_name="Skill offered by the reciever.")
    message = models.TextField(verbose_name="Initial message sent by the initiater/requester.")
    status = models.CharField(
        max_length=8,
        choices=[('pending', 'Pending'), # Pending request
                 ('accepted', 'Accepted'), # Reciever accepted
                 ('rejected', 'Rejected'), # Reciever rejected
                 ('revoked', 'Revoked'), # Initiater cancelled/revoked the request
        ],
        default='pending'
    )
    date = models.DateTimeField(verbose_name="Date and Time during the issuing.")
    