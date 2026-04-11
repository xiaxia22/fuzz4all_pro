# Class TransformerConfigurationException

**Source:** `java.xml\javax\xml\transform\TransformerConfigurationException.html`

### Class Description

```java
public class
TransformerConfigurationException

extends
TransformerException
```

Indicates a serious configuration error.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public TransformerConfigurationException()

Create a new

TransformerConfigurationException

with no
detail message.

---

#### public TransformerConfigurationException​(
String
msg)

Create a new

TransformerConfigurationException

with
the

String

specified as an error message.

**Parameters:**
- msg

- The error message for the exception.

---

#### public TransformerConfigurationException​(
Throwable
e)

Create a new

TransformerConfigurationException

with a
given

Exception

base cause of the error.

**Parameters:**
- e

- The exception to be encapsulated in a
TransformerConfigurationException.

---

#### public TransformerConfigurationException​(
String
msg,

Throwable
e)

Create a new

TransformerConfigurationException

with the
given

Exception

base cause and detail message.

**Parameters:**
- e

- The exception to be encapsulated in a
TransformerConfigurationException
- msg

- The detail message.

---

#### public TransformerConfigurationException​(
String
message,

SourceLocator
locator)

Create a new TransformerConfigurationException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a DocumentHandler
callback.

**Parameters:**
- message

- The error or warning message.
- locator

- The locator object for the error or warning.

---

#### public TransformerConfigurationException​(
String
message,

SourceLocator
locator,

Throwable
e)

Wrap an existing exception in a TransformerConfigurationException.

**Parameters:**
- message

- The error or warning message, or null to
use the message from the embedded exception.
- locator

- The locator object for the error or warning.
- e

- Any exception.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class TransformerConfigurationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.xml.transform.TransformerException
- - javax.xml.transform.TransformerConfigurationException

java.lang.Throwable

- java.lang.Exception
- - javax.xml.transform.TransformerException
- - javax.xml.transform.TransformerConfigurationException

java.lang.Exception

- javax.xml.transform.TransformerException
- - javax.xml.transform.TransformerConfigurationException

javax.xml.transform.TransformerException

- javax.xml.transform.TransformerConfigurationException

javax.xml.transform.TransformerConfigurationException

**All Implemented Interfaces:** Serializable

```java
public class
TransformerConfigurationException

extends
TransformerException
```

Indicates a serious configuration error.

**Since:** 1.4
**See Also:** Serialized Form

public class

TransformerConfigurationException

extends

TransformerException

Indicates a serious configuration error.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TransformerConfigurationException

()

Create a new

TransformerConfigurationException

with no
detail message.

TransformerConfigurationException

​(

String

msg)

Create a new

TransformerConfigurationException

with
the

String

specified as an error message.

TransformerConfigurationException

​(

String

msg,

Throwable

e)

Create a new

TransformerConfigurationException

with the
given

Exception

base cause and detail message.

TransformerConfigurationException

​(

String

message,

SourceLocator

locator)

Create a new TransformerConfigurationException from a message and a Locator.

TransformerConfigurationException

​(

String

message,

SourceLocator

locator,

Throwable

e)

Wrap an existing exception in a TransformerConfigurationException.

TransformerConfigurationException

​(

Throwable

e)

Create a new

TransformerConfigurationException

with a
given

Exception

base cause of the error.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.xml.transform.

TransformerException

getCause

,

getException

,

getLocationAsString

,

getLocator

,

getMessageAndLocation

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setLocator

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

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

TransformerConfigurationException

()

Create a new

TransformerConfigurationException

with no
detail message.

TransformerConfigurationException

​(

String

msg)

Create a new

TransformerConfigurationException

with
the

String

specified as an error message.

TransformerConfigurationException

​(

String

msg,

Throwable

e)

Create a new

TransformerConfigurationException

with the
given

Exception

base cause and detail message.

TransformerConfigurationException

​(

String

message,

SourceLocator

locator)

Create a new TransformerConfigurationException from a message and a Locator.

TransformerConfigurationException

​(

String

message,

SourceLocator

locator,

Throwable

e)

Wrap an existing exception in a TransformerConfigurationException.

TransformerConfigurationException

​(

Throwable

e)

Create a new

TransformerConfigurationException

with a
given

Exception

base cause of the error.

---

#### Constructor Summary

Create a new

TransformerConfigurationException

with no
detail message.

Create a new

TransformerConfigurationException

with
the

String

specified as an error message.

Create a new

TransformerConfigurationException

with the
given

Exception

base cause and detail message.

Create a new TransformerConfigurationException from a message and a Locator.

Wrap an existing exception in a TransformerConfigurationException.

Create a new

TransformerConfigurationException

with a
given

Exception

base cause of the error.

Method Summary

- Methods declared in class javax.xml.transform.

TransformerException

getCause

,

getException

,

getLocationAsString

,

getLocator

,

getMessageAndLocation

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setLocator

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

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

Methods declared in class javax.xml.transform.

TransformerException

getCause

,

getException

,

getLocationAsString

,

getLocator

,

getMessageAndLocation

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setLocator

---

#### Methods declared in class javax.xml.transform. TransformerException

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

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

- TransformerConfigurationException

```java
public TransformerConfigurationException()
```

Create a new

TransformerConfigurationException

with no
detail message.

- TransformerConfigurationException

```java
public TransformerConfigurationException​(
String
msg)
```

Create a new

TransformerConfigurationException

with
the

String

specified as an error message.

**Parameters:** msg

- The error message for the exception.

- TransformerConfigurationException

```java
public TransformerConfigurationException​(
Throwable
e)
```

Create a new

TransformerConfigurationException

with a
given

Exception

base cause of the error.

**Parameters:** e

- The exception to be encapsulated in a
TransformerConfigurationException.

- TransformerConfigurationException

```java
public TransformerConfigurationException​(
String
msg,

Throwable
e)
```

Create a new

TransformerConfigurationException

with the
given

Exception

base cause and detail message.

**Parameters:** e

- The exception to be encapsulated in a
TransformerConfigurationException
**Parameters:** msg

- The detail message.

- TransformerConfigurationException

```java
public TransformerConfigurationException​(
String
message,

SourceLocator
locator)
```

Create a new TransformerConfigurationException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a DocumentHandler
callback.

**Parameters:** message

- The error or warning message.
**Parameters:** locator

- The locator object for the error or warning.

- TransformerConfigurationException

```java
public TransformerConfigurationException​(
String
message,

SourceLocator
locator,

Throwable
e)
```

Wrap an existing exception in a TransformerConfigurationException.

**Parameters:** message

- The error or warning message, or null to
use the message from the embedded exception.
**Parameters:** locator

- The locator object for the error or warning.
**Parameters:** e

- Any exception.

Constructor Detail

- TransformerConfigurationException

```java
public TransformerConfigurationException()
```

Create a new

TransformerConfigurationException

with no
detail message.

- TransformerConfigurationException

```java
public TransformerConfigurationException​(
String
msg)
```

Create a new

TransformerConfigurationException

with
the

String

specified as an error message.

**Parameters:** msg

- The error message for the exception.

- TransformerConfigurationException

```java
public TransformerConfigurationException​(
Throwable
e)
```

Create a new

TransformerConfigurationException

with a
given

Exception

base cause of the error.

**Parameters:** e

- The exception to be encapsulated in a
TransformerConfigurationException.

- TransformerConfigurationException

```java
public TransformerConfigurationException​(
String
msg,

Throwable
e)
```

Create a new

TransformerConfigurationException

with the
given

Exception

base cause and detail message.

**Parameters:** e

- The exception to be encapsulated in a
TransformerConfigurationException
**Parameters:** msg

- The detail message.

- TransformerConfigurationException

```java
public TransformerConfigurationException​(
String
message,

SourceLocator
locator)
```

Create a new TransformerConfigurationException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a DocumentHandler
callback.

**Parameters:** message

- The error or warning message.
**Parameters:** locator

- The locator object for the error or warning.

- TransformerConfigurationException

```java
public TransformerConfigurationException​(
String
message,

SourceLocator
locator,

Throwable
e)
```

Wrap an existing exception in a TransformerConfigurationException.

**Parameters:** message

- The error or warning message, or null to
use the message from the embedded exception.
**Parameters:** locator

- The locator object for the error or warning.
**Parameters:** e

- Any exception.

---

#### Constructor Detail

TransformerConfigurationException

```java
public TransformerConfigurationException()
```

Create a new

TransformerConfigurationException

with no
detail message.

---

#### TransformerConfigurationException

public TransformerConfigurationException()

Create a new

TransformerConfigurationException

with no
detail message.

TransformerConfigurationException

```java
public TransformerConfigurationException​(
String
msg)
```

Create a new

TransformerConfigurationException

with
the

String

specified as an error message.

**Parameters:** msg

- The error message for the exception.

---

#### TransformerConfigurationException

public TransformerConfigurationException​(

String

msg)

Create a new

TransformerConfigurationException

with
the

String

specified as an error message.

TransformerConfigurationException

```java
public TransformerConfigurationException​(
Throwable
e)
```

Create a new

TransformerConfigurationException

with a
given

Exception

base cause of the error.

**Parameters:** e

- The exception to be encapsulated in a
TransformerConfigurationException.

---

#### TransformerConfigurationException

public TransformerConfigurationException​(

Throwable

e)

Create a new

TransformerConfigurationException

with a
given

Exception

base cause of the error.

TransformerConfigurationException

```java
public TransformerConfigurationException​(
String
msg,

Throwable
e)
```

Create a new

TransformerConfigurationException

with the
given

Exception

base cause and detail message.

**Parameters:** e

- The exception to be encapsulated in a
TransformerConfigurationException
**Parameters:** msg

- The detail message.

---

#### TransformerConfigurationException

public TransformerConfigurationException​(

String

msg,

Throwable

e)

Create a new

TransformerConfigurationException

with the
given

Exception

base cause and detail message.

TransformerConfigurationException

```java
public TransformerConfigurationException​(
String
message,

SourceLocator
locator)
```

Create a new TransformerConfigurationException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a DocumentHandler
callback.

**Parameters:** message

- The error or warning message.
**Parameters:** locator

- The locator object for the error or warning.

---

#### TransformerConfigurationException

public TransformerConfigurationException​(

String

message,

SourceLocator

locator)

Create a new TransformerConfigurationException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a DocumentHandler
callback.

This constructor is especially useful when an application is
creating its own exception from within a DocumentHandler
callback.

TransformerConfigurationException

```java
public TransformerConfigurationException​(
String
message,

SourceLocator
locator,

Throwable
e)
```

Wrap an existing exception in a TransformerConfigurationException.

**Parameters:** message

- The error or warning message, or null to
use the message from the embedded exception.
**Parameters:** locator

- The locator object for the error or warning.
**Parameters:** e

- Any exception.

---

#### TransformerConfigurationException

public TransformerConfigurationException​(

String

message,

SourceLocator

locator,

Throwable

e)

Wrap an existing exception in a TransformerConfigurationException.

---

