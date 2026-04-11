# Class ExecutionControl.UserException

**Source:** `jdk.jshell\jdk\jshell\spi\ExecutionControl.UserException.html`

### Class Description

```java
public static class
ExecutionControl.UserException

extends
ExecutionControl.RunException
```

A 'normal' user exception occurred.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UserException​(
String
message,

String
causeExceptionClass,

StackTraceElement
[] stackElements)

*No description found.*

---

### Method Details

#### public
String
causeExceptionClass()

Returns the class of the user exception.

**Returns:**
- the name of the user exception class

---

### Additional Sections

#### Class ExecutionControl.UserException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - jdk.jshell.spi.ExecutionControl.ExecutionControlException
- - jdk.jshell.spi.ExecutionControl.RunException
- - jdk.jshell.spi.ExecutionControl.UserException

java.lang.Throwable

- java.lang.Exception
- - jdk.jshell.spi.ExecutionControl.ExecutionControlException
- - jdk.jshell.spi.ExecutionControl.RunException
- - jdk.jshell.spi.ExecutionControl.UserException

java.lang.Exception

- jdk.jshell.spi.ExecutionControl.ExecutionControlException
- - jdk.jshell.spi.ExecutionControl.RunException
- - jdk.jshell.spi.ExecutionControl.UserException

jdk.jshell.spi.ExecutionControl.ExecutionControlException

- jdk.jshell.spi.ExecutionControl.RunException
- - jdk.jshell.spi.ExecutionControl.UserException

jdk.jshell.spi.ExecutionControl.RunException

- jdk.jshell.spi.ExecutionControl.UserException

jdk.jshell.spi.ExecutionControl.UserException

**All Implemented Interfaces:** Serializable

**Enclosing interface:** ExecutionControl

```java
public static class
ExecutionControl.UserException

extends
ExecutionControl.RunException
```

A 'normal' user exception occurred.

**See Also:** Serialized Form

public static class

ExecutionControl.UserException

extends

ExecutionControl.RunException

A 'normal' user exception occurred.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UserException

​(

String

message,

String

causeExceptionClass,

StackTraceElement

[] stackElements)

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

causeExceptionClass

()

Returns the class of the user exception.

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

UserException

​(

String

message,

String

causeExceptionClass,

StackTraceElement

[] stackElements)

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

causeExceptionClass

()

Returns the class of the user exception.

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

Returns the class of the user exception.

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

- UserException

```java
public UserException​(
String
message,

String
causeExceptionClass,

StackTraceElement
[] stackElements)
```

============ METHOD DETAIL ==========

- Method Detail

- causeExceptionClass

```java
public
String
causeExceptionClass()
```

Returns the class of the user exception.

**Returns:** the name of the user exception class

Constructor Detail

- UserException

```java
public UserException​(
String
message,

String
causeExceptionClass,

StackTraceElement
[] stackElements)
```

---

#### Constructor Detail

UserException

```java
public UserException​(
String
message,

String
causeExceptionClass,

StackTraceElement
[] stackElements)
```

---

#### UserException

public UserException​(

String

message,

String

causeExceptionClass,

StackTraceElement

[] stackElements)

Method Detail

- causeExceptionClass

```java
public
String
causeExceptionClass()
```

Returns the class of the user exception.

**Returns:** the name of the user exception class

---

#### Method Detail

causeExceptionClass

```java
public
String
causeExceptionClass()
```

Returns the class of the user exception.

**Returns:** the name of the user exception class

---

#### causeExceptionClass

public

String

causeExceptionClass()

Returns the class of the user exception.

---

