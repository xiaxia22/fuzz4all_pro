import sys
sys.path.insert(0, "D:/same-fuzz/fuzz4all-main/fuzz4all-main")
from Fuzz4All.mutation.profile_loader import PROFILE_CATALOG
checks = [
    ("REFLECT", "InvocationTargetException", "imports"),
    ("SECURITY", "InvalidKeyException", "imports"),
    ("SECURITY", "ENCRYPTION_MODE", "reject_tokens"),
    ("TIME", "DateTimeParseException", "imports"),
    ("CALLBACK", "PropertyChangeListenerProxy", "imports"),
    ("MARK_SUPPORT", ".write(", "reject_tokens"),
    ("MARK_SUPPORT", ".flush(", "reject_tokens"),
]
for cat, key, rule_type in checks:
    p = PROFILE_CATALOG[cat]
    if rule_type == "imports":
        found = any(key in imp for imp in p.get("repair_rules", {}).get("imports", []))
    else:
        found = any(key in tok for tok in p.get("filter_rules", {}).get(rule_type, []))
    status = "OK" if found else "MISSING"
    print(f"{cat}.{key} ({rule_type}): {status}")
