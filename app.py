def hours_saved(monthly_volume, aht_minutes, rules_based_pct):
    """Estimated hours saved per month by automating a process."""
    if monthly_volume < 0 or aht_minutes < 0:
        raise ValueError("Volume and AHT must not be negative")
    if not 0 <= rules_based_pct <= 100:
        raise ValueError("Rules-based % must be between 0 and 100")
    return monthly_volume * aht_minutes / 60 * rules_based_pct / 100
