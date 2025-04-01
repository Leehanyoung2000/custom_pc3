from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.models import EmailAddress
from .functions import confirmation_required_redirect

class LoginAndVerificationRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    # 로그인이 되어있는 사람과 안되어있는 사람을 나눈다 -> redirect_unauthenticated_users = True
    # 그리고 로그인이 되어있는 사람은 raise_exception으로 가서 이메일 인증 함수를 실행
    # 최종적으로 test_func(이메일 인증)에서 True가 나와야 접근가능
    
    redirect_unauthenticated_users = True
    raise_exception = confirmation_required_redirect

    def test_func(self, user):
        return EmailAddress.objects.filter(user=user, verified=True).exists()


class LoginAndOwnershipRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    # 로그인과 비로그인을 구분하지 않을거야 -> redirect_unauthenticated_users = False
    # raise_exception을 True로 설정해 접근 못하는 사람한테는 다 403 처리할거야
    # 접근하려면 test_func(작성자와 현재유저가 같아야)를 통과해
    redirect_unauthenticated_users = False
    raise_exception = True


    def test_func(self, user):
        obj = self.get_object()
        return obj.author == user