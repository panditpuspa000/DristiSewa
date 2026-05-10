def filter_by_branch(user, queryset):
    """
    Restrict queryset based on user's branch.
    Admin sees everything.
    Others see only their branch data.
    """

    if user.role == "ADMIN":
        return queryset

    if hasattr(user, "branch") and user.branch:
        return queryset.filter(branch=user.branch)

    return queryset.none()