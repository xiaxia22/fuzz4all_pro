# Class IllegalCallerException

**Source:** `java.base\java\lang\IllegalCallerException.html`

### Class Description

```java
public class
IllegalCallerException

extends
RuntimeException
```

Thrown to indicate that a method has been called by an inappropriate caller.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public IllegalCallerException()

Constructs an IllegalCallerException with no detail message.

---

#### public IllegalCallerException​(
String
s)

Constructs an IllegalCallerException with the specified detail
message.

**Parameters:**
- s

- the String that contains a detailed message (can be null)

---

#### public IllegalCallerException​(
String
message,

Throwable
cause)

Constructs a new exception with the specified detail message and
cause.

**Parameters:**
- message

- the detail message (can be null)
- cause

- the cause (can be null)

---

#### public IllegalCallerException​(
Throwable
cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

**Parameters:**
- cause

- the cause (can be null)

---

### Method Details

*No entries found.*

### Additional Sections

#### Class IllegalCallerException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.IllegalCallerException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.IllegalCallerException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.IllegalCallerException

java.lang.RuntimeException

- java.lang.IllegalCallerException

java.lang.IllegalCallerException

**All Implemented Interfaces:** Serializable

```java
public class
IllegalCallerException

extends
RuntimeException
```

Thrown to indicate that a method has been called by an inappropriate caller.

**Since:** 9
**See Also:** StackWalker.getCallerClass()

,

Serialized Form

public class

IllegalCallerException

extends

RuntimeException

Thrown to indicate that a method has been called by an inappropriate caller.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IllegalCallerException

()

Constructs an IllegalCallerException with no detail message.

IllegalCallerException

​(

String

s)

Constructs an IllegalCallerException with the specified detail
message.

IllegalCallerException

​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message and
cause.

IllegalCallerException

​(

Throwable

cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

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

IllegalCallerException

()

Constructs an IllegalCallerException with no detail message.

IllegalCallerException

​(

String

s)

Constructs an IllegalCallerException with the specified detail
message.

IllegalCallerException

​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message and
cause.

IllegalCallerException

​(

Throwable

cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

---

#### Constructor Summary

Constructs an IllegalCallerException with no detail message.

Constructs an IllegalCallerException with the specified detail
message.

Constructs a new exception with the specified detail message and
cause.

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

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

- IllegalCallerException

```java
public IllegalCallerException()
```

Constructs an IllegalCallerException with no detail message.

- IllegalCallerException

```java
public IllegalCallerException​(
String
s)
```

Constructs an IllegalCallerException with the specified detail
message.

**Parameters:** s

- the String that contains a detailed message (can be null)

- IllegalCallerException

```java
public IllegalCallerException​(
String
message,

Throwable
cause)
```

Constructs a new exception with the specified detail message and
cause.

**Parameters:** message

- the detail message (can be null)
**Parameters:** cause

- the cause (can be null)

- IllegalCallerException

```java
public IllegalCallerException​(
Throwable
cause)
```

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (can be null)

Constructor Detail

- IllegalCallerException

```java
public IllegalCallerException()
```

Constructs an IllegalCallerException with no detail message.

- IllegalCallerException

```java
public IllegalCallerException​(
String
s)
```

Constructs an IllegalCallerException with the specified detail
message.

**Parameters:** s

- the String that contains a detailed message (can be null)

- IllegalCallerException

```java
public IllegalCallerException​(
String
message,

Throwable
cause)
```

Constructs a new exception with the specified detail message and
cause.

**Parameters:** message

- the detail message (can be null)
**Parameters:** cause

- the cause (can be null)

- IllegalCallerException

```java
public IllegalCallerException​(
Throwable
cause)
```

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (can be null)

---

#### Constructor Detail

IllegalCallerException

```java
public IllegalCallerException()
```

Constructs an IllegalCallerException with no detail message.

---

#### IllegalCallerException

public IllegalCallerException()

Constructs an IllegalCallerException with no detail message.

IllegalCallerException

```java
public IllegalCallerException​(
String
s)
```

Constructs an IllegalCallerException with the specified detail
message.

**Parameters:** s

- the String that contains a detailed message (can be null)

---

#### IllegalCallerException

public IllegalCallerException​(

String

s)

Constructs an IllegalCallerException with the specified detail
message.

IllegalCallerException

```java
public IllegalCallerException​(
String
message,

Throwable
cause)
```

Constructs a new exception with the specified detail message and
cause.

**Parameters:** message

- the detail message (can be null)
**Parameters:** cause

- the cause (can be null)

---

#### IllegalCallerException

public IllegalCallerException​(

String

message,

Throwable

cause)

Constructs a new exception with the specified detail message and
cause.

IllegalCallerException

```java
public IllegalCallerException​(
Throwable
cause)
```

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

**Parameters:** cause

- the cause (can be null)

---

#### IllegalCallerException

public IllegalCallerException​(

Throwable

cause)

Constructs a new exception with the specified cause and a detail
message of

(cause==null ? null : cause.toString())

(which
typically contains the class and detail message of

cause

).

---

