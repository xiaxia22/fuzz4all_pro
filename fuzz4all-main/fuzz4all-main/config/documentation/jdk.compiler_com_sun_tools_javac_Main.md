# Class Main

**Source:** `jdk.compiler\com\sun\tools\javac\Main.html`

### Class Description

```java
public class
Main

extends
Object
```

A legacy programmatic interface for the Java Programming Language
compiler, javac.
See the

jdk.compiler

module for details on replacement APIs.

---

### Field Details

*No entries found.*

### Constructor Details

#### public Main()

*No description found.*

---

### Method Details

#### public static void main​(
String
[] args)
throws
Exception

Main entry point for the launcher.
Note: This method calls System.exit.

**Parameters:**
- args

- command line arguments

**Throws:**
- Exception

---

#### public static int compile​(
String
[] args)

Programmatic interface to the Java Programming Language
compiler, javac.

**Parameters:**
- args

- The command line arguments that would normally be
passed to the javac program as described in the man page.

**Returns:**
- an integer equivalent to the exit value from invoking
javac, see the man page for details.

---

#### public static int compile​(
String
[] args,

PrintWriter
out)

Programmatic interface to the Java Programming Language
compiler, javac.

**Parameters:**
- args

- The command line arguments that would normally be
passed to the javac program as described in the man page.
- out

- PrintWriter to which the compiler's diagnostic
output is directed.

**Returns:**
- an integer equivalent to the exit value from invoking
javac, see the man page for details.

---

### Additional Sections

#### Class Main

java.lang.Object

- com.sun.tools.javac.Main

com.sun.tools.javac.Main

```java
public class
Main

extends
Object
```

A legacy programmatic interface for the Java Programming Language
compiler, javac.
See the

jdk.compiler

module for details on replacement APIs.

public class

Main

extends

Object

A legacy programmatic interface for the Java Programming Language
compiler, javac.
See the

jdk.compiler

module for details on replacement APIs.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Main

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static int

compile

​(

String

[] args)

Programmatic interface to the Java Programming Language
compiler, javac.

static int

compile

​(

String

[] args,

PrintWriter

out)

Programmatic interface to the Java Programming Language
compiler, javac.

static void

main

​(

String

[] args)

Main entry point for the launcher.

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

Constructor Summary

Constructors

Constructor

Description

Main

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static int

compile

​(

String

[] args)

Programmatic interface to the Java Programming Language
compiler, javac.

static int

compile

​(

String

[] args,

PrintWriter

out)

Programmatic interface to the Java Programming Language
compiler, javac.

static void

main

​(

String

[] args)

Main entry point for the launcher.

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

Programmatic interface to the Java Programming Language
compiler, javac.

Main entry point for the launcher.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Main

```java
public Main()
```

============ METHOD DETAIL ==========

- Method Detail

- main

```java
public static void main​(
String
[] args)
throws
Exception
```

Main entry point for the launcher.
Note: This method calls System.exit.

**Parameters:** args

- command line arguments
**Throws:** Exception

- compile

```java
public static int compile​(
String
[] args)
```

Programmatic interface to the Java Programming Language
compiler, javac.

**Parameters:** args

- The command line arguments that would normally be
passed to the javac program as described in the man page.
**Returns:** an integer equivalent to the exit value from invoking
javac, see the man page for details.

- compile

```java
public static int compile​(
String
[] args,

PrintWriter
out)
```

Programmatic interface to the Java Programming Language
compiler, javac.

**Parameters:** args

- The command line arguments that would normally be
passed to the javac program as described in the man page.
**Parameters:** out

- PrintWriter to which the compiler's diagnostic
output is directed.
**Returns:** an integer equivalent to the exit value from invoking
javac, see the man page for details.

Constructor Detail

- Main

```java
public Main()
```

---

#### Constructor Detail

Main

```java
public Main()
```

---

#### Main

public Main()

Method Detail

- main

```java
public static void main​(
String
[] args)
throws
Exception
```

Main entry point for the launcher.
Note: This method calls System.exit.

**Parameters:** args

- command line arguments
**Throws:** Exception

- compile

```java
public static int compile​(
String
[] args)
```

Programmatic interface to the Java Programming Language
compiler, javac.

**Parameters:** args

- The command line arguments that would normally be
passed to the javac program as described in the man page.
**Returns:** an integer equivalent to the exit value from invoking
javac, see the man page for details.

- compile

```java
public static int compile​(
String
[] args,

PrintWriter
out)
```

Programmatic interface to the Java Programming Language
compiler, javac.

**Parameters:** args

- The command line arguments that would normally be
passed to the javac program as described in the man page.
**Parameters:** out

- PrintWriter to which the compiler's diagnostic
output is directed.
**Returns:** an integer equivalent to the exit value from invoking
javac, see the man page for details.

---

#### Method Detail

main

```java
public static void main​(
String
[] args)
throws
Exception
```

Main entry point for the launcher.
Note: This method calls System.exit.

**Parameters:** args

- command line arguments
**Throws:** Exception

---

#### main

public static void main​(

String

[] args)
throws

Exception

Main entry point for the launcher.
Note: This method calls System.exit.

compile

```java
public static int compile​(
String
[] args)
```

Programmatic interface to the Java Programming Language
compiler, javac.

**Parameters:** args

- The command line arguments that would normally be
passed to the javac program as described in the man page.
**Returns:** an integer equivalent to the exit value from invoking
javac, see the man page for details.

---

#### compile

public static int compile​(

String

[] args)

Programmatic interface to the Java Programming Language
compiler, javac.

compile

```java
public static int compile​(
String
[] args,

PrintWriter
out)
```

Programmatic interface to the Java Programming Language
compiler, javac.

**Parameters:** args

- The command line arguments that would normally be
passed to the javac program as described in the man page.
**Parameters:** out

- PrintWriter to which the compiler's diagnostic
output is directed.
**Returns:** an integer equivalent to the exit value from invoking
javac, see the man page for details.

---

#### compile

public static int compile​(

String

[] args,

PrintWriter

out)

Programmatic interface to the Java Programming Language
compiler, javac.

---

