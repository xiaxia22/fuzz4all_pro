import re, collections
base = "D:/same-fuzz/fuzz4all-main/fuzz4all-main/outputs/targeted10/"
apis = [
    ("java.base_java_io_BufferedInputStream","RESOURCE/BUFFER"),
    ("java.base_java_io_File","FILE"),
    ("java.base_java_lang_Thread","CONCURRENT"),
    ("java.base_java_lang_reflect_Method","REFLECT"),
    ("java.base_java_net_Socket","NETWORK"),
    ("java.base_java_net_URI","NETWORK/UTILITY"),
    ("java.base_java_time_Duration","TIME"),
    ("java.base_javax_crypto_Cipher","SECURITY"),
    ("java.desktop_java_beans_PropertyChangeSupport","CALLBACK"),
    ("java.management_java_lang_management_ManagementFactory","JVM_MGMT"),
]
for api, tag in apis:
    log = base + api + "/log_validation.txt"
    try:
        with open(log, encoding="utf-8") as f:
            content = f.read()
        safe = content.count("is safe")
        fail = content.count("failed validation")
        total = safe + fail
        rate = round(safe/total*100) if total else 0
        syms = re.findall(r"symbol:\s+(?:method|class)\s+(\w+)", content)
        top = collections.Counter(syms).most_common(3)
        short = api.replace("java.base_","").replace("java.desktop_","").replace("java.management_","")
        print(f"{short} [{tag}] SAFE={safe}/{total} ({rate}%) errors={top}")
    except Exception as e:
        print(f"{api}: ERROR {e}")
