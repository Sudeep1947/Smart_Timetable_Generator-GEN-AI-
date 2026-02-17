
def detect_conflict(new_event):
    existing_events = []  # Replace with DB fetch
    for event in existing_events:
        if new_event["start"] < event["end"] and new_event["end"] > event["start"]:
            return True
    return False
