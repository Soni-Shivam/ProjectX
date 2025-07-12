from django.conf import settings
from django.db import models

# Models


class Swap(models.Model):
    '''
    # User Swap model
    User 1 (Initiater), Skill offered
    User 2 (Reciever), Skill offered
    Message
    boolean Accepted (done)
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
    done = models.BooleanField(verbose_name="True if the Swap is complete, False if it was rejected, or discontinued for some reason.")
    

