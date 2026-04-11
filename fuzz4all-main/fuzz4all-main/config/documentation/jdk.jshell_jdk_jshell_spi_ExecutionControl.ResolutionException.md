# Class ExecutionControl.ResolutionException

**Source:** `jdk.jshell\jdk\jshell\spi\ExecutionControl.ResolutionException.html`

### Class Description

```java
public static class
ExecutionControl.ResolutionException

extends
ExecutionControl.RunException
```

An exception indicating that a

DeclarationSnippet

with unresolved
references has been encountered.

Contrast this with the initiating

SPIResolutionException

(a

RuntimeException

) which is embedded in generated corralled
code. Also, contrast this with

UnresolvedReferenceException

the high-level
exception (with

DeclarationSnippet

reference) provided in the
main API.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ResolutionException​(int id,

StackTraceElement
[] stackElements)

Constructs an exception indicating that a

DeclarationSnippet

with unresolved references has been encountered.

**Parameters:**
- id

- An internal identifier of the specific method
- stackElements

- the stack trace

---

### Method Details

#### public int id()

Retrieves the internal identifier of the unresolved identifier.

**Returns:**
- the internal identifier

---

### Additional Sections

#### Class ExecutionControl.ResolutionException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - jdk.jshell.spi.ExecutionControl.ExecutionControlException
- - jdk.jshell.spi.ExecutionControl.RunException
- - jdk.jshell.spi.ExecutionControl.ResolutionException

java.lang.Throwable

- java.lang.Exception
- - jdk.jshell.spi.ExecutionControl.ExecutionControlException
- - jdk.jshell.spi.ExecutionControl.RunException
- - jdk.jshell.spi.ExecutionControl.ResolutionException

java.lang.Exception

- jdk.jshell.spi.ExecutionControl.ExecutionControlException
- - jdk.jshell.spi.ExecutionControl.RunException
- - jdk.jshell.spi.ExecutionControl.ResolutionException

jdk.jshell.spi.ExecutionControl.ExecutionControlException

- jdk.jshell.spi.ExecutionControl.RunException
- - jdk.jshell.spi.ExecutionControl.ResolutionException

jdk.jshell.spi.ExecutionControl.RunException

- jdk.jshell.spi.ExecutionControl.ResolutionException

jdk.jshell.spi.ExecutionControl.ResolutionException

**All Implemented Interfaces:** Serializable

**Enclosing interface:** ExecutionControl

```java
public static class
ExecutionControl.ResolutionException

extends
ExecutionControl.RunException
```

An exception indicating that a

DeclarationSnippet

with unresolved
references has been encountered.

Contrast this with the initiating

SPIResolutionException

(a

RuntimeException

) which is embedded in generated corralled
code. Also, contrast this with

UnresolvedReferenceException

the high-level
exception (with

DeclarationSnippet

reference) provided in the
main API.

**See Also:** Serialized Form

public static class

ExecutionControl.ResolutionException

extends

ExecutionControl.RunException

An exception indicating that a

DeclarationSnippet

with unresolved
references has been encountered.

Contrast this with the initiating

SPIResolutionException

(a

RuntimeException

) which is embedded in generated corralled
code. Also, contrast this with

UnresolvedReferenceException

the high-level
exception (with

DeclarationSnippet

reference) provided in the
main API.

Contrast this with the initiating

SPIResolutionException

(a

RuntimeException

) which is embedded in generated corralled
code. Also, contrast this with

UnresolvedReferenceException

the high-level
exception (with

DeclarationSnippet

reference) provided in the
main API.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ResolutionException

​(int id,

StackTraceElement

[] stackElements)

Constructs an exception indicating that a

DeclarationSnippet

with unresolved references has been encountered.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

id

()

Retrieves the internal identifier of the unresolved identifier.

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

ResolutionException

​(int id,

StackTraceElement

[] stackElements)

Constructs an exception indicating that a

DeclarationSnippet

with unresolved references has been encountered.

---

#### Constructor Summary

Constructs an exception indicating that a

DeclarationSnippet

with unresolved references has been encountered.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

id

()

Retrieves the internal identifier of the unresolved identifier.

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

Retrieves the internal identifier of the unresolved identifier.

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

- ResolutionException

```java
public ResolutionException​(int id,

StackTraceElement
[] stackElements)
```

Constructs an exception indicating that a

DeclarationSnippet

with unresolved references has been encountered.

**Parameters:** id

- An internal identifier of the specific method
**Parameters:** stackElements

- the stack trace

============ METHOD DETAIL ==========

- Method Detail

- id

```java
public int id()
```

Retrieves the internal identifier of the unresolved identifier.

**Returns:** the internal identifier

Constructor Detail

- ResolutionException

```java
public ResolutionException​(int id,

StackTraceElement
[] stackElements)
```

Constructs an exception indicating that a

DeclarationSnippet

with unresolved references has been encountered.

**Parameters:** id

- An internal identifier of the specific method
**Parameters:** stackElements

- the stack trace

---

#### Constructor Detail

ResolutionException

```java
public ResolutionException​(int id,

StackTraceElement
[] stackElements)
```

Constructs an exception indicating that a

DeclarationSnippet

with unresolved references has been encountered.

**Parameters:** id

- An internal identifier of the specific method
**Parameters:** stackElements

- the stack trace

---

#### ResolutionException

public ResolutionException​(int id,

StackTraceElement

[] stackElements)

Constructs an exception indicating that a

DeclarationSnippet

with unresolved references has been encountered.

Method Detail

- id

```java
public int id()
```

Retrieves the internal identifier of the unresolved identifier.

**Returns:** the internal identifier

---

#### Method Detail

id

```java
public int id()
```

Retrieves the internal identifier of the unresolved identifier.

**Returns:** the internal identifier

---

#### id

public int id()

Retrieves the internal identifier of the unresolved identifier.

---

