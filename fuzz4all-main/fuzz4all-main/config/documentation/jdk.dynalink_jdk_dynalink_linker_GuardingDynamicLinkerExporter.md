# Class GuardingDynamicLinkerExporter

**Source:** `jdk.dynalink\jdk\dynalink\linker\GuardingDynamicLinkerExporter.html`

### Class Description

```java
public abstract class
GuardingDynamicLinkerExporter

extends
Object

implements
Supplier
<
List
<
GuardingDynamicLinker
>>
```

A class acting as a supplier of guarding dynamic linkers that can be
automatically loaded by other language runtimes. Language runtimes wishing
to export their own linkers should subclass this class and implement the

Supplier.get()

method to return a list of exported linkers and declare the
subclass in

/META-INF/services/jdk.dynalink.linker.GuardingDynamicLinkerExporter

resource of their distribution (typically, JAR file) so that dynamic linker
factories can discover them using the

ServiceLoader

mechanism. Note
that instantiating this class is tied to a security check for the

RuntimePermission("dynalink.exportLinkersAutomatically")

when a
security manager is present, to ensure that only trusted runtimes can
automatically export their linkers into other runtimes.

**All Implemented Interfaces:** Supplier

<

List

<

GuardingDynamicLinker

>>

---

### Field Details

#### public static final
String
AUTOLOAD_PERMISSION_NAME

The name of the runtime permission for creating instances of this class.
Granting this permission to a language runtime allows it to export its
linkers for automatic loading into other language runtimes.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### protected GuardingDynamicLinkerExporter()

Creates a new linker exporter. If there is a security manager installed
checks for the

RuntimePermission("dynalink.exportLinkersAutomatically")

runtime
permission. This ensures only language runtimes granted this permission
will be allowed to export their linkers for automatic loading.

**Throws:**
- SecurityException

- if the necessary runtime permission is not
granted.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class GuardingDynamicLinkerExporter

java.lang.Object

- jdk.dynalink.linker.GuardingDynamicLinkerExporter

jdk.dynalink.linker.GuardingDynamicLinkerExporter

**All Implemented Interfaces:** Supplier

<

List

<

GuardingDynamicLinker

>>

```java
public abstract class
GuardingDynamicLinkerExporter

extends
Object

implements
Supplier
<
List
<
GuardingDynamicLinker
>>
```

A class acting as a supplier of guarding dynamic linkers that can be
automatically loaded by other language runtimes. Language runtimes wishing
to export their own linkers should subclass this class and implement the

Supplier.get()

method to return a list of exported linkers and declare the
subclass in

/META-INF/services/jdk.dynalink.linker.GuardingDynamicLinkerExporter

resource of their distribution (typically, JAR file) so that dynamic linker
factories can discover them using the

ServiceLoader

mechanism. Note
that instantiating this class is tied to a security check for the

RuntimePermission("dynalink.exportLinkersAutomatically")

when a
security manager is present, to ensure that only trusted runtimes can
automatically export their linkers into other runtimes.

**See Also:** DynamicLinkerFactory.setClassLoader(ClassLoader)

public abstract class

GuardingDynamicLinkerExporter

extends

Object

implements

Supplier

<

List

<

GuardingDynamicLinker

>>

A class acting as a supplier of guarding dynamic linkers that can be
automatically loaded by other language runtimes. Language runtimes wishing
to export their own linkers should subclass this class and implement the

Supplier.get()

method to return a list of exported linkers and declare the
subclass in

/META-INF/services/jdk.dynalink.linker.GuardingDynamicLinkerExporter

resource of their distribution (typically, JAR file) so that dynamic linker
factories can discover them using the

ServiceLoader

mechanism. Note
that instantiating this class is tied to a security check for the

RuntimePermission("dynalink.exportLinkersAutomatically")

when a
security manager is present, to ensure that only trusted runtimes can
automatically export their linkers into other runtimes.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

AUTOLOAD_PERMISSION_NAME

The name of the runtime permission for creating instances of this class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

GuardingDynamicLinkerExporter

()

Creates a new linker exporter.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.util.function.

Supplier

get

Field Summary

Fields

Modifier and Type

Field

Description

static

String

AUTOLOAD_PERMISSION_NAME

The name of the runtime permission for creating instances of this class.

---

#### Field Summary

The name of the runtime permission for creating instances of this class.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

GuardingDynamicLinkerExporter

()

Creates a new linker exporter.

---

#### Constructor Summary

Creates a new linker exporter.

Method Summary

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.util.function.

Supplier

get

---

#### Method Summary

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.util.function.

Supplier

get

---

#### Methods declared in interface java.util.function. Supplier

============ FIELD DETAIL ===========

- Field Detail

- AUTOLOAD_PERMISSION_NAME

```java
public static final
String
AUTOLOAD_PERMISSION_NAME
```

The name of the runtime permission for creating instances of this class.
Granting this permission to a language runtime allows it to export its
linkers for automatic loading into other language runtimes.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GuardingDynamicLinkerExporter

```java
protected GuardingDynamicLinkerExporter()
```

Creates a new linker exporter. If there is a security manager installed
checks for the

RuntimePermission("dynalink.exportLinkersAutomatically")

runtime
permission. This ensures only language runtimes granted this permission
will be allowed to export their linkers for automatic loading.

**Throws:** SecurityException

- if the necessary runtime permission is not
granted.

Field Detail

- AUTOLOAD_PERMISSION_NAME

```java
public static final
String
AUTOLOAD_PERMISSION_NAME
```

The name of the runtime permission for creating instances of this class.
Granting this permission to a language runtime allows it to export its
linkers for automatic loading into other language runtimes.

**See Also:** Constant Field Values

---

#### Field Detail

AUTOLOAD_PERMISSION_NAME

```java
public static final
String
AUTOLOAD_PERMISSION_NAME
```

The name of the runtime permission for creating instances of this class.
Granting this permission to a language runtime allows it to export its
linkers for automatic loading into other language runtimes.

**See Also:** Constant Field Values

---

#### AUTOLOAD_PERMISSION_NAME

public static final

String

AUTOLOAD_PERMISSION_NAME

The name of the runtime permission for creating instances of this class.
Granting this permission to a language runtime allows it to export its
linkers for automatic loading into other language runtimes.

Constructor Detail

- GuardingDynamicLinkerExporter

```java
protected GuardingDynamicLinkerExporter()
```

Creates a new linker exporter. If there is a security manager installed
checks for the

RuntimePermission("dynalink.exportLinkersAutomatically")

runtime
permission. This ensures only language runtimes granted this permission
will be allowed to export their linkers for automatic loading.

**Throws:** SecurityException

- if the necessary runtime permission is not
granted.

---

#### Constructor Detail

GuardingDynamicLinkerExporter

```java
protected GuardingDynamicLinkerExporter()
```

Creates a new linker exporter. If there is a security manager installed
checks for the

RuntimePermission("dynalink.exportLinkersAutomatically")

runtime
permission. This ensures only language runtimes granted this permission
will be allowed to export their linkers for automatic loading.

**Throws:** SecurityException

- if the necessary runtime permission is not
granted.

---

#### GuardingDynamicLinkerExporter

protected GuardingDynamicLinkerExporter()

Creates a new linker exporter. If there is a security manager installed
checks for the

RuntimePermission("dynalink.exportLinkersAutomatically")

runtime
permission. This ensures only language runtimes granted this permission
will be allowed to export their linkers for automatic loading.

---

