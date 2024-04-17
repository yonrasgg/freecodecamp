def add_time(start, duration, day=None):
    week_days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    day_indexes = {v.lower(): k for k, v in week_days.items()}  # Reverse lookup, case insensitive

    # Extract start time and meridian
    start_hour, start_minute = map(int, start.split()[0].split(":"))
    meridian = start.split()[1]

    # Convert start hour to 24-hour format
    if meridian.lower() == "pm":
        start_hour += 12

    # Extract duration time
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Add duration to start time
    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour + (total_minutes // 60)
    final_minute = total_minutes % 60
    final_hour = total_hours % 24
    total_days = total_hours // 24

    # Adjust for AM/PM
    if final_hour == 0:
        final_hour = 12
        final_meridian = "AM"
    elif final_hour < 12:
        final_meridian = "AM"
    else:
        final_hour -= 12
        final_meridian = "PM"
        if final_hour == 0:
            final_hour = 12

    # Format output time
    final_minute = f"{final_minute:02d}"
    timestamp = f"{final_hour}:{final_minute} {final_meridian}"

    # Adjust for days later
    result_day = ""
    if day:
        day_index = (day_indexes[day.lower()] + total_days) % 7
        result_day = ", " + week_days[day_index]

    # Adding day information
    if total_days == 1:
        result_day += " (next day)"
    elif total_days > 1:
        result_day += f" ({total_days} days later)"

    return timestamp + result_day

