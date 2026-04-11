# Class ExecutionControl.ClassInstallException

**Source:** `jdk.jshell\jdk\jshell\spi\ExecutionControl.ClassInstallException.html`

### Class Description

```java
public static class
ExecutionControl.ClassInstallException

extends
ExecutionControl.ExecutionControlException
```

A class install (load or redefine) encountered a problem.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ClassInstallException​(
String
message,
boolean[] installed)

*No description found.*

---

### Method Details

#### public boolean[] installed()

Indicates which of the passed classes were successfully
loaded/redefined.

**Returns:**
- a one-to-one array with the

ExecutionControl.ClassBytecodes

[]

array --

true

if installed

---

### Additional Sections

#### Class ExecutionControl.ClassInstallException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - jdk.jshell.spi.ExecutionControl.ExecutionControlException
- - jdk.jshell.spi.ExecutionControl.ClassInstallException

java.lang.Throwable

- java.lang.Exception
- - jdk.jshell.spi.ExecutionControl.ExecutionControlException
- - jdk.jshell.spi.ExecutionControl.ClassInstallException

java.lang.Exception

- jdk.jshell.spi.ExecutionControl.ExecutionControlException
- - jdk.jshell.spi.ExecutionControl.ClassInstallException

jdk.jshell.spi.ExecutionControl.ExecutionControlException

- jdk.jshell.spi.ExecutionControl.ClassInstallException

jdk.jshell.spi.ExecutionControl.ClassInstallException

**All Implemented Interfaces:** Serializable

**Enclosing interface:** ExecutionControl

```java
public static class
ExecutionControl.ClassInstallException

extends
ExecutionControl.ExecutionControlException
```

A class install (load or redefine) encountered a problem.

**See Also:** Serialized Form

public static class

ExecutionControl.ClassInstallException

extends

ExecutionControl.ExecutionControlException

A class install (load or redefine) encountered a problem.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ClassInstallException

​(

String

message,
boolean[] installed)

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean[]

installed

()

Indicates which of the passed classes were successfully
loaded/redefined.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

ClassInstallException

​(

String

message,
boolean[] installed)

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean[]

installed

()

Indicates which of the passed classes were successfully
loaded/redefined.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Indicates which of the passed classes were successfully
loaded/redefined.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ClassInstallException

```java
public ClassInstallException​(
String
message,
boolean[] installed)
```

============ METHOD DETAIL ==========

- Method Detail

- installed

```java
public boolean[] installed()
```

Indicates which of the passed classes were successfully
loaded/redefined.

**Returns:** a one-to-one array with the

ExecutionControl.ClassBytecodes

[]

array --

true

if installed

Constructor Detail

- ClassInstallException

```java
public ClassInstallException​(
String
message,
boolean[] installed)
```

---

#### Constructor Detail

ClassInstallException

```java
public ClassInstallException​(
String
message,
boolean[] installed)
```

---

#### ClassInstallException

public ClassInstallException​(

String

message,
boolean[] installed)

Method Detail

- installed

```java
public boolean[] installed()
```

Indicates which of the passed classes were successfully
loaded/redefined.

**Returns:** a one-to-one array with the

ExecutionControl.ClassBytecodes

[]

array --

true

if installed

---

#### Method Detail

installed

```java
public boolean[] installed()
```

Indicates which of the passed classes were successfully
loaded/redefined.

**Returns:** a one-to-one array with the

ExecutionControl.ClassBytecodes

[]

array --

true

if installed

---

#### installed

public boolean[] installed()

Indicates which of the passed classes were successfully
loaded/redefined.

---

