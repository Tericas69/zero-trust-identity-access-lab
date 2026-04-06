def role_required(user, allowed_roles):
    return user.get("role") in allowed_roles


def department_required(user, allowed_departments):
    return user.get("department") in allowed_departments
