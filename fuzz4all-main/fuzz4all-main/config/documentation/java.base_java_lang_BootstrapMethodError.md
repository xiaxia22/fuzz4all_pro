# Class BootstrapMethodError

**Source:** `java.base\java\lang\BootstrapMethodError.html`

### Class Description

```java
public class
BootstrapMethodError

extends
LinkageError
```

Thrown to indicate that an

invokedynamic

instruction or a dynamic
constant failed to resolve its bootstrap method and arguments,
or for

invokedynamic

instruction the bootstrap method has failed to
provide a

call site

with a

target

of the correct

method type

,
or for a dynamic constant the bootstrap method has failed to provide a
constant value of the required type.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public BootstrapMethodError()

Constructs a

BootstrapMethodError

with no detail message.

---

#### public BootstrapMethodError​(
String
s)

Constructs a

BootstrapMethodError

with the specified
detail message.

**Parameters:**
- s

- the detail message.

---

#### public BootstrapMethodError​(
String
s,

Throwable
cause)

Constructs a

BootstrapMethodError

with the specified
detail message and cause.

**Parameters:**
- s

- the detail message.
- cause

- the cause, may be

null

.

---

#### public BootstrapMethodError​(
Throwable
cause)

Constructs a

BootstrapMethodError

with the specified
cause.

**Parameters:**
- cause

- the cause, may be

null

.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class BootstrapMethodError

java.lang.Object

- java.lang.Throwable
- - java.lang.Error
- - java.lang.LinkageError
- - java.lang.BootstrapMethodError

java.lang.Throwable

- java.lang.Error
- - java.lang.LinkageError
- - java.lang.BootstrapMethodError

java.lang.Error

- java.lang.LinkageError
- - java.lang.BootstrapMethodError

java.lang.LinkageError

- java.lang.BootstrapMethodError

java.lang.BootstrapMethodError

**All Implemented Interfaces:** Serializable

```java
public class
BootstrapMethodError

extends
LinkageError
```

Thrown to indicate that an

invokedynamic

instruction or a dynamic
constant failed to resolve its bootstrap method and arguments,
or for

invokedynamic

instruction the bootstrap method has failed to
provide a

call site

with a

target

of the correct

method type

,
or for a dynamic constant the bootstrap method has failed to provide a
constant value of the required type.

**Since:** 1.7
**See Also:** Serialized Form

public class

BootstrapMethodError

extends

LinkageError

Thrown to indicate that an

invokedynamic

instruction or a dynamic
constant failed to resolve its bootstrap method and arguments,
or for

invokedynamic

instruction the bootstrap method has failed to
provide a

call site

with a

target

of the correct

method type

,
or for a dynamic constant the bootstrap method has failed to provide a
constant value of the required type.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BootstrapMethodError

()

Constructs a

BootstrapMethodError

with no detail message.

BootstrapMethodError

​(

String

s)

Constructs a

BootstrapMethodError

with the specified
detail message.

BootstrapMethodError

​(

String

s,

Throwable

cause)

Constructs a

BootstrapMethodError

with the specified
detail message and cause.

BootstrapMethodError

​(

Throwable

cause)

Constructs a

BootstrapMethodError

with the specified
cause.

========== METHOD SUMMARY ===========

- Method Summary

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

BootstrapMethodError

()

Constructs a

BootstrapMethodError

with no detail message.

BootstrapMethodError

​(

String

s)

Constructs a

BootstrapMethodError

with the specified
detail message.

BootstrapMethodError

​(

String

s,

Throwable

cause)

Constructs a

BootstrapMethodError

with the specified
detail message and cause.

BootstrapMethodError

​(

Throwable

cause)

Constructs a

BootstrapMethodError

with the specified
cause.

---

#### Constructor Summary

Constructs a

BootstrapMethodError

with no detail message.

Constructs a

BootstrapMethodError

with the specified
detail message.

Constructs a

BootstrapMethodError

with the specified
detail message and cause.

Constructs a

BootstrapMethodError

with the specified
cause.

Method Summary

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

- BootstrapMethodError

```java
public BootstrapMethodError()
```

Constructs a

BootstrapMethodError

with no detail message.

- BootstrapMethodError

```java
public BootstrapMethodError​(
String
s)
```

Constructs a

BootstrapMethodError

with the specified
detail message.

**Parameters:** s

- the detail message.

- BootstrapMethodError

```java
public BootstrapMethodError​(
String
s,

Throwable
cause)
```

Constructs a

BootstrapMethodError

with the specified
detail message and cause.

**Parameters:** s

- the detail message.
**Parameters:** cause

- the cause, may be

null

.

- BootstrapMethodError

```java
public BootstrapMethodError​(
Throwable
cause)
```

Constructs a

BootstrapMethodError

with the specified
cause.

**Parameters:** cause

- the cause, may be

null

.

Constructor Detail

- BootstrapMethodError

```java
public BootstrapMethodError()
```

Constructs a

BootstrapMethodError

with no detail message.

- BootstrapMethodError

```java
public BootstrapMethodError​(
String
s)
```

Constructs a

BootstrapMethodError

with the specified
detail message.

**Parameters:** s

- the detail message.

- BootstrapMethodError

```java
public BootstrapMethodError​(
String
s,

Throwable
cause)
```

Constructs a

BootstrapMethodError

with the specified
detail message and cause.

**Parameters:** s

- the detail message.
**Parameters:** cause

- the cause, may be

null

.

- BootstrapMethodError

```java
public BootstrapMethodError​(
Throwable
cause)
```

Constructs a

BootstrapMethodError

with the specified
cause.

**Parameters:** cause

- the cause, may be

null

.

---

#### Constructor Detail

BootstrapMethodError

```java
public BootstrapMethodError()
```

Constructs a

BootstrapMethodError

with no detail message.

---

#### BootstrapMethodError

public BootstrapMethodError()

Constructs a

BootstrapMethodError

with no detail message.

BootstrapMethodError

```java
public BootstrapMethodError​(
String
s)
```

Constructs a

BootstrapMethodError

with the specified
detail message.

**Parameters:** s

- the detail message.

---

#### BootstrapMethodError

public BootstrapMethodError​(

String

s)

Constructs a

BootstrapMethodError

with the specified
detail message.

BootstrapMethodError

```java
public BootstrapMethodError​(
String
s,

Throwable
cause)
```

Constructs a

BootstrapMethodError

with the specified
detail message and cause.

**Parameters:** s

- the detail message.
**Parameters:** cause

- the cause, may be

null

.

---

#### BootstrapMethodError

public BootstrapMethodError​(

String

s,

Throwable

cause)

Constructs a

BootstrapMethodError

with the specified
detail message and cause.

BootstrapMethodError

```java
public BootstrapMethodError​(
Throwable
cause)
```

Constructs a

BootstrapMethodError

with the specified
cause.

**Parameters:** cause

- the cause, may be

null

.

---

#### BootstrapMethodError

public BootstrapMethodError​(

Throwable

cause)

Constructs a

BootstrapMethodError

with the specified
cause.

---

