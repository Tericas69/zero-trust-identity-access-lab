def role_required(user, allowed_roles):
    return user.get("role") in allowed_roles
