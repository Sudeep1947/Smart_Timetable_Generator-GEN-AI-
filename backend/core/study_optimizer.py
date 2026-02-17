
def optimize_study_plan(total_hours, days_left, priority=1):
    if days_left == 0:
        return 0
    base = total_hours / days_left
    return round(base * priority, 2)
