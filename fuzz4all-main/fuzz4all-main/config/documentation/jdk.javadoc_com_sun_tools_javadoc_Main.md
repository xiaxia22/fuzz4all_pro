# Class Main

**Source:** `jdk.javadoc\com\sun\tools\javadoc\Main.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public class
Main

extends
Object
```

Provides external entry points (tool and programmatic)
for the javadoc program.

This is NOT part of any supported API.
If you write code that depends on this, you do so at your own risk.
This code and its internal interfaces are subject to change or
deletion without notice.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static void main​(
String
... args)

Command line interface.

**Parameters:**
- args

- The command line parameters.

---

#### public static int execute​(
String
... args)

Programmatic interface.

**Parameters:**
- args

- The command line parameters.

**Returns:**
- The return code.

---

#### public static int execute​(
ClassLoader
docletParentClassLoader,

String
... args)

Programmatic interface.

**Parameters:**
- args

- The command line parameters.
- docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.

**Returns:**
- The return code.

**Since:**
- 1.7

---

#### public static int execute​(
String
programName,

String
... args)

Programmatic interface.

**Parameters:**
- programName

- Name of the program (for error messages).
- args

- The command line parameters.

**Returns:**
- The return code.

---

#### public static int execute​(
String
programName,

ClassLoader
docletParentClassLoader,

String
... args)

Programmatic interface.

**Parameters:**
- programName

- Name of the program (for error messages).
- args

- The command line parameters.
- docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.

**Returns:**
- The return code.

**Since:**
- 1.7

---

#### public static int execute​(
String
programName,

String
defaultDocletClassName,

String
... args)

Programmatic interface.

**Parameters:**
- programName

- Name of the program (for error messages).
- defaultDocletClassName

- Fully qualified class name.
- args

- The command line parameters.

**Returns:**
- The return code.

---

#### public static int execute​(
String
programName,

String
defaultDocletClassName,

ClassLoader
docletParentClassLoader,

String
... args)

Programmatic interface.

**Parameters:**
- programName

- Name of the program (for error messages).
- defaultDocletClassName

- Fully qualified class name.
- docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
- args

- The command line parameters.

**Returns:**
- The return code.

**Since:**
- 1.7

---

#### public static int execute​(
String
programName,

PrintWriter
errWriter,

PrintWriter
warnWriter,

PrintWriter
noticeWriter,

String
defaultDocletClassName,

String
... args)

Programmatic interface.

**Parameters:**
- programName

- Name of the program (for error messages).
- errWriter

- PrintWriter to receive error messages.
- warnWriter

- PrintWriter to receive error messages.
- noticeWriter

- PrintWriter to receive error messages.
- defaultDocletClassName

- Fully qualified class name.
- args

- The command line parameters.

**Returns:**
- The return code.

---

#### public static int execute​(
String
programName,

PrintWriter
errWriter,

PrintWriter
warnWriter,

PrintWriter
noticeWriter,

String
defaultDocletClassName,

ClassLoader
docletParentClassLoader,

String
... args)

Programmatic interface.

**Parameters:**
- programName

- Name of the program (for error messages).
- errWriter

- PrintWriter to receive error messages.
- warnWriter

- PrintWriter to receive error messages.
- noticeWriter

- PrintWriter to receive error messages.
- defaultDocletClassName

- Fully qualified class name.
- docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
- args

- The command line parameters.

**Returns:**
- The return code.

**Since:**
- 1.7

---

### Additional Sections

#### Class Main

java.lang.Object

- com.sun.tools.javadoc.Main

com.sun.tools.javadoc.Main

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public class
Main

extends
Object
```

Deprecated, for removal: This API element is subject to removal in a future version.

This class is now deprecated and may be removed in a future release.
See

javax.tools.ToolProvider::getSystemDocumentationTool

and

javax.tools.DocumentationTool

for replacement functionality.

Provides external entry points (tool and programmatic)
for the javadoc program.

This is NOT part of any supported API.
If you write code that depends on this, you do so at your own risk.
This code and its internal interfaces are subject to change or
deletion without notice.

**Since:** 1.4

@Deprecated

(

since

="9",

forRemoval

=true)
public class

Main

extends

Object

Provides external entry points (tool and programmatic)
for the javadoc program.

This is NOT part of any supported API.
If you write code that depends on this, you do so at your own risk.
This code and its internal interfaces are subject to change or
deletion without notice.

This is NOT part of any supported API.
If you write code that depends on this, you do so at your own risk.
This code and its internal interfaces are subject to change or
deletion without notice.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static int

execute

​(

ClassLoader

docletParentClassLoader,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

programName,

PrintWriter

errWriter,

PrintWriter

warnWriter,

PrintWriter

noticeWriter,

String

defaultDocletClassName,

ClassLoader

docletParentClassLoader,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

programName,

PrintWriter

errWriter,

PrintWriter

warnWriter,

PrintWriter

noticeWriter,

String

defaultDocletClassName,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

programName,

ClassLoader

docletParentClassLoader,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

programName,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

programName,

String

defaultDocletClassName,

ClassLoader

docletParentClassLoader,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

programName,

String

defaultDocletClassName,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static void

main

​(

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Command line interface.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static int

execute

​(

ClassLoader

docletParentClassLoader,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

programName,

PrintWriter

errWriter,

PrintWriter

warnWriter,

PrintWriter

noticeWriter,

String

defaultDocletClassName,

ClassLoader

docletParentClassLoader,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

programName,

PrintWriter

errWriter,

PrintWriter

warnWriter,

PrintWriter

noticeWriter,

String

defaultDocletClassName,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

programName,

ClassLoader

docletParentClassLoader,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

programName,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

programName,

String

defaultDocletClassName,

ClassLoader

docletParentClassLoader,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static int

execute

​(

String

programName,

String

defaultDocletClassName,

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

static void

main

​(

String

... args)

Deprecated, for removal: This API element is subject to removal in a future version.

Command line interface.

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

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

Command line interface.

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

============ METHOD DETAIL ==========

- Method Detail

- main

```java
public static void main​(
String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Command line interface.

**Parameters:** args

- The command line parameters.

- execute

```java
public static int execute​(
String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** args

- The command line parameters.
**Returns:** The return code.

- execute

```java
public static int execute​(
ClassLoader
docletParentClassLoader,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** args

- The command line parameters.
**Parameters:** docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
**Returns:** The return code.
**Since:** 1.7

- execute

```java
public static int execute​(
String
programName,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** args

- The command line parameters.
**Returns:** The return code.

- execute

```java
public static int execute​(
String
programName,

ClassLoader
docletParentClassLoader,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** args

- The command line parameters.
**Parameters:** docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
**Returns:** The return code.
**Since:** 1.7

- execute

```java
public static int execute​(
String
programName,

String
defaultDocletClassName,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** defaultDocletClassName

- Fully qualified class name.
**Parameters:** args

- The command line parameters.
**Returns:** The return code.

- execute

```java
public static int execute​(
String
programName,

String
defaultDocletClassName,

ClassLoader
docletParentClassLoader,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** defaultDocletClassName

- Fully qualified class name.
**Parameters:** docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
**Parameters:** args

- The command line parameters.
**Returns:** The return code.
**Since:** 1.7

- execute

```java
public static int execute​(
String
programName,

PrintWriter
errWriter,

PrintWriter
warnWriter,

PrintWriter
noticeWriter,

String
defaultDocletClassName,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** errWriter

- PrintWriter to receive error messages.
**Parameters:** warnWriter

- PrintWriter to receive error messages.
**Parameters:** noticeWriter

- PrintWriter to receive error messages.
**Parameters:** defaultDocletClassName

- Fully qualified class name.
**Parameters:** args

- The command line parameters.
**Returns:** The return code.

- execute

```java
public static int execute​(
String
programName,

PrintWriter
errWriter,

PrintWriter
warnWriter,

PrintWriter
noticeWriter,

String
defaultDocletClassName,

ClassLoader
docletParentClassLoader,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** errWriter

- PrintWriter to receive error messages.
**Parameters:** warnWriter

- PrintWriter to receive error messages.
**Parameters:** noticeWriter

- PrintWriter to receive error messages.
**Parameters:** defaultDocletClassName

- Fully qualified class name.
**Parameters:** docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
**Parameters:** args

- The command line parameters.
**Returns:** The return code.
**Since:** 1.7

Method Detail

- main

```java
public static void main​(
String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Command line interface.

**Parameters:** args

- The command line parameters.

- execute

```java
public static int execute​(
String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** args

- The command line parameters.
**Returns:** The return code.

- execute

```java
public static int execute​(
ClassLoader
docletParentClassLoader,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** args

- The command line parameters.
**Parameters:** docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
**Returns:** The return code.
**Since:** 1.7

- execute

```java
public static int execute​(
String
programName,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** args

- The command line parameters.
**Returns:** The return code.

- execute

```java
public static int execute​(
String
programName,

ClassLoader
docletParentClassLoader,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** args

- The command line parameters.
**Parameters:** docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
**Returns:** The return code.
**Since:** 1.7

- execute

```java
public static int execute​(
String
programName,

String
defaultDocletClassName,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** defaultDocletClassName

- Fully qualified class name.
**Parameters:** args

- The command line parameters.
**Returns:** The return code.

- execute

```java
public static int execute​(
String
programName,

String
defaultDocletClassName,

ClassLoader
docletParentClassLoader,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** defaultDocletClassName

- Fully qualified class name.
**Parameters:** docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
**Parameters:** args

- The command line parameters.
**Returns:** The return code.
**Since:** 1.7

- execute

```java
public static int execute​(
String
programName,

PrintWriter
errWriter,

PrintWriter
warnWriter,

PrintWriter
noticeWriter,

String
defaultDocletClassName,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** errWriter

- PrintWriter to receive error messages.
**Parameters:** warnWriter

- PrintWriter to receive error messages.
**Parameters:** noticeWriter

- PrintWriter to receive error messages.
**Parameters:** defaultDocletClassName

- Fully qualified class name.
**Parameters:** args

- The command line parameters.
**Returns:** The return code.

- execute

```java
public static int execute​(
String
programName,

PrintWriter
errWriter,

PrintWriter
warnWriter,

PrintWriter
noticeWriter,

String
defaultDocletClassName,

ClassLoader
docletParentClassLoader,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** errWriter

- PrintWriter to receive error messages.
**Parameters:** warnWriter

- PrintWriter to receive error messages.
**Parameters:** noticeWriter

- PrintWriter to receive error messages.
**Parameters:** defaultDocletClassName

- Fully qualified class name.
**Parameters:** docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
**Parameters:** args

- The command line parameters.
**Returns:** The return code.
**Since:** 1.7

---

#### Method Detail

main

```java
public static void main​(
String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Command line interface.

**Parameters:** args

- The command line parameters.

---

#### main

public static void main​(

String

... args)

Command line interface.

execute

```java
public static int execute​(
String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** args

- The command line parameters.
**Returns:** The return code.

---

#### execute

public static int execute​(

String

... args)

Programmatic interface.

execute

```java
public static int execute​(
ClassLoader
docletParentClassLoader,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** args

- The command line parameters.
**Parameters:** docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
**Returns:** The return code.
**Since:** 1.7

---

#### execute

public static int execute​(

ClassLoader

docletParentClassLoader,

String

... args)

Programmatic interface.

execute

```java
public static int execute​(
String
programName,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** args

- The command line parameters.
**Returns:** The return code.

---

#### execute

public static int execute​(

String

programName,

String

... args)

Programmatic interface.

execute

```java
public static int execute​(
String
programName,

ClassLoader
docletParentClassLoader,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** args

- The command line parameters.
**Parameters:** docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
**Returns:** The return code.
**Since:** 1.7

---

#### execute

public static int execute​(

String

programName,

ClassLoader

docletParentClassLoader,

String

... args)

Programmatic interface.

execute

```java
public static int execute​(
String
programName,

String
defaultDocletClassName,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** defaultDocletClassName

- Fully qualified class name.
**Parameters:** args

- The command line parameters.
**Returns:** The return code.

---

#### execute

public static int execute​(

String

programName,

String

defaultDocletClassName,

String

... args)

Programmatic interface.

execute

```java
public static int execute​(
String
programName,

String
defaultDocletClassName,

ClassLoader
docletParentClassLoader,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** defaultDocletClassName

- Fully qualified class name.
**Parameters:** docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
**Parameters:** args

- The command line parameters.
**Returns:** The return code.
**Since:** 1.7

---

#### execute

public static int execute​(

String

programName,

String

defaultDocletClassName,

ClassLoader

docletParentClassLoader,

String

... args)

Programmatic interface.

execute

```java
public static int execute​(
String
programName,

PrintWriter
errWriter,

PrintWriter
warnWriter,

PrintWriter
noticeWriter,

String
defaultDocletClassName,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** errWriter

- PrintWriter to receive error messages.
**Parameters:** warnWriter

- PrintWriter to receive error messages.
**Parameters:** noticeWriter

- PrintWriter to receive error messages.
**Parameters:** defaultDocletClassName

- Fully qualified class name.
**Parameters:** args

- The command line parameters.
**Returns:** The return code.

---

#### execute

public static int execute​(

String

programName,

PrintWriter

errWriter,

PrintWriter

warnWriter,

PrintWriter

noticeWriter,

String

defaultDocletClassName,

String

... args)

Programmatic interface.

execute

```java
public static int execute​(
String
programName,

PrintWriter
errWriter,

PrintWriter
warnWriter,

PrintWriter
noticeWriter,

String
defaultDocletClassName,

ClassLoader
docletParentClassLoader,

String
... args)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Programmatic interface.

**Parameters:** programName

- Name of the program (for error messages).
**Parameters:** errWriter

- PrintWriter to receive error messages.
**Parameters:** warnWriter

- PrintWriter to receive error messages.
**Parameters:** noticeWriter

- PrintWriter to receive error messages.
**Parameters:** defaultDocletClassName

- Fully qualified class name.
**Parameters:** docletParentClassLoader

- The parent class loader used when
creating the doclet classloader. If null, the class loader used
to instantiate doclets will be created without specifying a parent
class loader.
**Parameters:** args

- The command line parameters.
**Returns:** The return code.
**Since:** 1.7

---

#### execute

public static int execute​(

String

programName,

PrintWriter

errWriter,

PrintWriter

warnWriter,

PrintWriter

noticeWriter,

String

defaultDocletClassName,

ClassLoader

docletParentClassLoader,

String

... args)

Programmatic interface.

---

