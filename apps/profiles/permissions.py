from rest_framework.permissions import BasePermission


class IsProfileCompleted(BasePermission):
    """
    Allow access only if profile
    has been completed.
    """

    message = (
        "Please complete your profile first."
    )

    def has_permission(
        self,
        request,
        view,
    ):

        return (
            request.user.is_authenticated
            and request.user.profile.is_profile_completed
        )