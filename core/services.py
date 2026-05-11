def filter_by_branch(user, queryset):
    """
    Global branch isolation rule:
    - Admin: full access
    - Others: only their branch data
    """

    # Admin bypass
    if getattr(user, "role", None) == "ADMIN":
        return queryset

    # Must have branch
    if hasattr(user, "branch") and user.branch:
        return queryset.filter(branch=user.branch)

    # fallback: no access
    return queryset.none()