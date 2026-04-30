import re, collections
base = "D:/same-fuzz/fuzz4all-main/fuzz4all-main/outputs/targeted10/"
apis = [
    "java.base_java_io_BufferedInputStream",
    "java.base_java_lang_reflect_Method",
    "java.base_java_time_Duration",
    "java.base_javax_crypto_Cipher",
    "java.desktop_java_beans_PropertyChangeSupport",
    "java.base_java_lang_Thread",
    "java.base_java_net_Socket",
]
for api in apis:
    log = base + api + "/log_validation.txt"
    try:
        with open(log, encoding="utf-8") as f:
            content = f.read()
        # All unique error lines
        lines = [l.strip() for l in content.split("\n") if "error:" in l or "symbol:" in l]
        ctr = collections.Counter(lines)
        short = api.replace("java.base_","").replace("java.desktop_","")
        print(f"\n=== {short} ===")
        for msg, cnt in ctr.most_common(8):
            print(f"  {cnt}x {msg[:100]}")
    except Exception as e:
        print(f"{api}: {e}")
