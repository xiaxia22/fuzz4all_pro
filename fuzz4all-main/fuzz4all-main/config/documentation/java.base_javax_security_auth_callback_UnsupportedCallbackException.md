# Class UnsupportedCallbackException

**Source:** `java.base\javax\security\auth\callback\UnsupportedCallbackException.html`

### Class Description

```java
public class
UnsupportedCallbackException

extends
Exception
```

Signals that a

CallbackHandler

does not
recognize a particular

Callback

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnsupportedCallbackException​(
Callback
callback)

Constructs an

UnsupportedCallbackException

with no detail message.

**Parameters:**
- callback

- the unrecognized

Callback

.

---

#### public UnsupportedCallbackException​(
Callback
callback,

String
msg)

Constructs a UnsupportedCallbackException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:**
- callback

- the unrecognized

Callback

.
- msg

- the detail message.

---

### Method Details

#### public
Callback
getCallback()

Get the unrecognized

Callback

.

**Returns:**
- the unrecognized

Callback

.

---

### Additional Sections

#### Class UnsupportedCallbackException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.security.auth.callback.UnsupportedCallbackException

java.lang.Throwable

- java.lang.Exception
- - javax.security.auth.callback.UnsupportedCallbackException

java.lang.Exception

- javax.security.auth.callback.UnsupportedCallbackException

javax.security.auth.callback.UnsupportedCallbackException

**All Implemented Interfaces:** Serializable

```java
public class
UnsupportedCallbackException

extends
Exception
```

Signals that a

CallbackHandler

does not
recognize a particular

Callback

.

**Since:** 1.4
**See Also:** Serialized Form

public class

UnsupportedCallbackException

extends

Exception

Signals that a

CallbackHandler

does not
recognize a particular

Callback

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UnsupportedCallbackException

​(

Callback

callback)

Constructs an

UnsupportedCallbackException

with no detail message.

UnsupportedCallbackException

​(

Callback

callback,

String

msg)

Constructs a UnsupportedCallbackException with the specified detail
message.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Callback

getCallback

()

Get the unrecognized

Callback

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

UnsupportedCallbackException

​(

Callback

callback)

Constructs an

UnsupportedCallbackException

with no detail message.

UnsupportedCallbackException

​(

Callback

callback,

String

msg)

Constructs a UnsupportedCallbackException with the specified detail
message.

---

#### Constructor Summary

Constructs an

UnsupportedCallbackException

with no detail message.

Constructs a UnsupportedCallbackException with the specified detail
message.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Callback

getCallback

()

Get the unrecognized

Callback

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

Get the unrecognized

Callback

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

- UnsupportedCallbackException

```java
public UnsupportedCallbackException​(
Callback
callback)
```

Constructs an

UnsupportedCallbackException

with no detail message.

**Parameters:** callback

- the unrecognized

Callback

.

- UnsupportedCallbackException

```java
public UnsupportedCallbackException​(
Callback
callback,

String
msg)
```

Constructs a UnsupportedCallbackException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:** callback

- the unrecognized

Callback

.
**Parameters:** msg

- the detail message.

============ METHOD DETAIL ==========

- Method Detail

- getCallback

```java
public
Callback
getCallback()
```

Get the unrecognized

Callback

.

**Returns:** the unrecognized

Callback

.

Constructor Detail

- UnsupportedCallbackException

```java
public UnsupportedCallbackException​(
Callback
callback)
```

Constructs an

UnsupportedCallbackException

with no detail message.

**Parameters:** callback

- the unrecognized

Callback

.

- UnsupportedCallbackException

```java
public UnsupportedCallbackException​(
Callback
callback,

String
msg)
```

Constructs a UnsupportedCallbackException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:** callback

- the unrecognized

Callback

.
**Parameters:** msg

- the detail message.

---

#### Constructor Detail

UnsupportedCallbackException

```java
public UnsupportedCallbackException​(
Callback
callback)
```

Constructs an

UnsupportedCallbackException

with no detail message.

**Parameters:** callback

- the unrecognized

Callback

.

---

#### UnsupportedCallbackException

public UnsupportedCallbackException​(

Callback

callback)

Constructs an

UnsupportedCallbackException

with no detail message.

UnsupportedCallbackException

```java
public UnsupportedCallbackException​(
Callback
callback,

String
msg)
```

Constructs a UnsupportedCallbackException with the specified detail
message. A detail message is a String that describes this particular
exception.

**Parameters:** callback

- the unrecognized

Callback

.
**Parameters:** msg

- the detail message.

---

#### UnsupportedCallbackException

public UnsupportedCallbackException​(

Callback

callback,

String

msg)

Constructs a UnsupportedCallbackException with the specified detail
message. A detail message is a String that describes this particular
exception.

Method Detail

- getCallback

```java
public
Callback
getCallback()
```

Get the unrecognized

Callback

.

**Returns:** the unrecognized

Callback

.

---

#### Method Detail

getCallback

```java
public
Callback
getCallback()
```

Get the unrecognized

Callback

.

**Returns:** the unrecognized

Callback

.

---

#### getCallback

public

Callback

getCallback()

Get the unrecognized

Callback

.

---

