from datetime import datetime


def role_required(user, allowed_roles):
    return user.get("role") in allowed_roles


def department_required(user, allowed_departments):
    return user.get("department") in allowed_departments


def business_hours_required(start_hour=8, end_hour=18):
    current_hour = datetime.now().hour
    return start_hour <= current_hour < end_hour
