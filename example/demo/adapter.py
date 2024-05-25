from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class DefaultAccountAdapterCustom(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        ctx = {
            "email": email,
            "current_site": settings.URL_FRONT,
        }
        ctx.update(context)

        # activation patch
        if "activate_url" in ctx.keys():
            ctx['activate_url'] = settings.URL_FRONT + \
                'accounts/verify-email/' + ctx['key']
        
        # password reset patch
        if "password_reset_url" in ctx.keys():
            ctx['password_reset_url'] = settings.URL_FRONT + \
                "/".join(ctx['password_reset_url'].split("/")[3:])

        msg = self.render_mail(template_prefix, email, ctx)
        msg.send()
