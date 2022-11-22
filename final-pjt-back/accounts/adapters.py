from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        profile_image = data.get("profile_image")
        nickname = data.get("nickname")
        
        user.profile_image = profile_image
        user.nickname = nickname
        # print(data,1111111111111111111111111111111111111111)
        user.save()
        return user