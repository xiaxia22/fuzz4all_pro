# Class HeadlessException

**Source:** `java.desktop\java\awt\HeadlessException.html`

### Class Description

```java
public class
HeadlessException

extends
UnsupportedOperationException
```

Thrown when code that is dependent on a keyboard, display, or mouse
is called in an environment that does not support a keyboard, display,
or mouse. Any code that depends on any of those devices should firstly
ensure their availability using the

GraphicsEnvironment.isHeadless()

method and throw

HeadlessException

if the latter returns

true

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public HeadlessException()

Constructs new

HeadlessException

with empty message.
For such

HeadlessException

the default headless error message
may be auto-generated for some platforms.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

---

#### public HeadlessException​(
String
msg)

Create a new instance with the specified detailed error message.
For some platforms the default headless error message may be
added at the end of the specified message.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

**Parameters:**
- msg

- the error message

---

### Method Details

#### public
String
getMessage()

Returns the detail message string of this

HeadlessException

.
Depending on the platform the message specified in the constructor may
be followed by the default headless error message.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

**Overrides:**
- getMessage

in class

Throwable

**Returns:**
- the detail message string of this

HeadlessException

instance (which may be

null

).

---

### Additional Sections

#### Class HeadlessException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.UnsupportedOperationException
- - java.awt.HeadlessException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.UnsupportedOperationException
- - java.awt.HeadlessException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.UnsupportedOperationException
- - java.awt.HeadlessException

java.lang.RuntimeException

- java.lang.UnsupportedOperationException
- - java.awt.HeadlessException

java.lang.UnsupportedOperationException

- java.awt.HeadlessException

java.awt.HeadlessException

**All Implemented Interfaces:** Serializable

```java
public class
HeadlessException

extends
UnsupportedOperationException
```

Thrown when code that is dependent on a keyboard, display, or mouse
is called in an environment that does not support a keyboard, display,
or mouse. Any code that depends on any of those devices should firstly
ensure their availability using the

GraphicsEnvironment.isHeadless()

method and throw

HeadlessException

if the latter returns

true

.

**Since:** 1.4
**See Also:** GraphicsEnvironment.isHeadless()

,

Serialized Form

public class

HeadlessException

extends

UnsupportedOperationException

Thrown when code that is dependent on a keyboard, display, or mouse
is called in an environment that does not support a keyboard, display,
or mouse. Any code that depends on any of those devices should firstly
ensure their availability using the

GraphicsEnvironment.isHeadless()

method and throw

HeadlessException

if the latter returns

true

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HeadlessException

()

Constructs new

HeadlessException

with empty message.

HeadlessException

​(

String

msg)

Create a new instance with the specified detailed error message.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getMessage

()

Returns the detail message string of this

HeadlessException

.

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

HeadlessException

()

Constructs new

HeadlessException

with empty message.

HeadlessException

​(

String

msg)

Create a new instance with the specified detailed error message.

---

#### Constructor Summary

Constructs new

HeadlessException

with empty message.

Create a new instance with the specified detailed error message.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getMessage

()

Returns the detail message string of this

HeadlessException

.

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

Returns the detail message string of this

HeadlessException

.

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

- HeadlessException

```java
public HeadlessException()
```

Constructs new

HeadlessException

with empty message.
For such

HeadlessException

the default headless error message
may be auto-generated for some platforms.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

- HeadlessException

```java
public HeadlessException​(
String
msg)
```

Create a new instance with the specified detailed error message.
For some platforms the default headless error message may be
added at the end of the specified message.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

**Parameters:** msg

- the error message

============ METHOD DETAIL ==========

- Method Detail

- getMessage

```java
public
String
getMessage()
```

Returns the detail message string of this

HeadlessException

.
Depending on the platform the message specified in the constructor may
be followed by the default headless error message.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

**Overrides:** getMessage

in class

Throwable
**Returns:** the detail message string of this

HeadlessException

instance (which may be

null

).

Constructor Detail

- HeadlessException

```java
public HeadlessException()
```

Constructs new

HeadlessException

with empty message.
For such

HeadlessException

the default headless error message
may be auto-generated for some platforms.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

- HeadlessException

```java
public HeadlessException​(
String
msg)
```

Create a new instance with the specified detailed error message.
For some platforms the default headless error message may be
added at the end of the specified message.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

**Parameters:** msg

- the error message

---

#### Constructor Detail

HeadlessException

```java
public HeadlessException()
```

Constructs new

HeadlessException

with empty message.
For such

HeadlessException

the default headless error message
may be auto-generated for some platforms.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

---

#### HeadlessException

public HeadlessException()

Constructs new

HeadlessException

with empty message.
For such

HeadlessException

the default headless error message
may be auto-generated for some platforms.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

HeadlessException

```java
public HeadlessException​(
String
msg)
```

Create a new instance with the specified detailed error message.
For some platforms the default headless error message may be
added at the end of the specified message.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

**Parameters:** msg

- the error message

---

#### HeadlessException

public HeadlessException​(

String

msg)

Create a new instance with the specified detailed error message.
For some platforms the default headless error message may be
added at the end of the specified message.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

Method Detail

- getMessage

```java
public
String
getMessage()
```

Returns the detail message string of this

HeadlessException

.
Depending on the platform the message specified in the constructor may
be followed by the default headless error message.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

**Overrides:** getMessage

in class

Throwable
**Returns:** the detail message string of this

HeadlessException

instance (which may be

null

).

---

#### Method Detail

getMessage

```java
public
String
getMessage()
```

Returns the detail message string of this

HeadlessException

.
Depending on the platform the message specified in the constructor may
be followed by the default headless error message.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

**Overrides:** getMessage

in class

Throwable
**Returns:** the detail message string of this

HeadlessException

instance (which may be

null

).

---

#### getMessage

public

String

getMessage()

Returns the detail message string of this

HeadlessException

.
Depending on the platform the message specified in the constructor may
be followed by the default headless error message.
The text of the default headless message may depend on
whether the GraphicsEnvironment is in fact headless.
That is, the default headless message is both system and environmentally
dependent.

---

