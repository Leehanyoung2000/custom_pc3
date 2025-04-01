from django.shortcuts import redirect
from allauth.account.utils import send_email_confirmation

def confirmation_required_redirect(self, request):

    # 이메일로 인증 메일 발송
    send_email_confirmation(request, request.user)

    # 이메일 인증완료해야하는 페이지로 redirect
    return redirect("account_email_confirmation_required")
