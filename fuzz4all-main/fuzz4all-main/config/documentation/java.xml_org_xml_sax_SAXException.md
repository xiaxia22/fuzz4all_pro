# Class SAXException

**Source:** `java.xml\org\xml\sax\SAXException.html`

### Class Description

```java
public class
SAXException

extends
Exception
```

Encapsulate a general SAX error or warning.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class can contain basic error or warning information from
either the XML parser or the application: a parser writer or
application writer can subclass it to provide additional
functionality. SAX handlers may throw this exception or
any exception subclassed from it.

If the application needs to pass through other types of
exceptions, it must wrap those exceptions in a SAXException
or an exception derived from a SAXException.

If the parser or application needs to include information about a
specific location in an XML document, it should use the

SAXParseException

subclass.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SAXException()

Create a new SAXException.

---

#### public SAXException​(
String
message)

Create a new SAXException.

**Parameters:**
- message

- The error or warning message.

---

#### public SAXException​(
Exception
e)

Create a new SAXException wrapping an existing exception.

The existing exception will be embedded in the new
one, and its message will become the default message for
the SAXException.

**Parameters:**
- e

- The exception to be wrapped in a SAXException.

---

#### public SAXException​(
String
message,

Exception
e)

Create a new SAXException from an existing exception.

The existing exception will be embedded in the new
one, but the new exception will have its own message.

**Parameters:**
- message

- The detail message.
- e

- The exception to be wrapped in a SAXException.

---

### Method Details

#### public
String
getMessage()

Return a detail message for this exception.

If there is an embedded exception, and if the SAXException
has no detail message of its own, this method will return
the detail message from the embedded exception.

**Overrides:**
- getMessage

in class

Throwable

**Returns:**
- The error or warning message.

---

#### public
Exception
getException()

Return the embedded exception, if any.

**Returns:**
- The embedded exception, or null if there is none.

---

#### public
Throwable
getCause()

Return the cause of the exception

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- Return the cause of the exception

---

#### public
String
toString()

Override toString to pick up any embedded exception.

**Overrides:**
- toString

in class

Throwable

**Returns:**
- A string representation of this exception.

---

### Additional Sections

#### Class SAXException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - org.xml.sax.SAXException

java.lang.Throwable

- java.lang.Exception
- - org.xml.sax.SAXException

java.lang.Exception

- org.xml.sax.SAXException

org.xml.sax.SAXException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** SAXNotRecognizedException

,

SAXNotSupportedException

,

SAXParseException

```java
public class
SAXException

extends
Exception
```

Encapsulate a general SAX error or warning.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class can contain basic error or warning information from
either the XML parser or the application: a parser writer or
application writer can subclass it to provide additional
functionality. SAX handlers may throw this exception or
any exception subclassed from it.

If the application needs to pass through other types of
exceptions, it must wrap those exceptions in a SAXException
or an exception derived from a SAXException.

If the parser or application needs to include information about a
specific location in an XML document, it should use the

SAXParseException

subclass.

**Since:** 1.4, SAX 1.0
**See Also:** SAXParseException

,

Serialized Form

public class

SAXException

extends

Exception

Encapsulate a general SAX error or warning.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class can contain basic error or warning information from
either the XML parser or the application: a parser writer or
application writer can subclass it to provide additional
functionality. SAX handlers may throw this exception or
any exception subclassed from it.

If the application needs to pass through other types of
exceptions, it must wrap those exceptions in a SAXException
or an exception derived from a SAXException.

If the parser or application needs to include information about a
specific location in an XML document, it should use the

SAXParseException

subclass.

This class can contain basic error or warning information from
either the XML parser or the application: a parser writer or
application writer can subclass it to provide additional
functionality. SAX handlers may throw this exception or
any exception subclassed from it.

If the application needs to pass through other types of
exceptions, it must wrap those exceptions in a SAXException
or an exception derived from a SAXException.

If the parser or application needs to include information about a
specific location in an XML document, it should use the

SAXParseException

subclass.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SAXException

()

Create a new SAXException.

SAXException

​(

Exception

e)

Create a new SAXException wrapping an existing exception.

SAXException

​(

String

message)

Create a new SAXException.

SAXException

​(

String

message,

Exception

e)

Create a new SAXException from an existing exception.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Throwable

getCause

()

Return the cause of the exception

Exception

getException

()

Return the embedded exception, if any.

String

getMessage

()

Return a detail message for this exception.

String

toString

()

Override toString to pick up any embedded exception.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

SAXException

()

Create a new SAXException.

SAXException

​(

Exception

e)

Create a new SAXException wrapping an existing exception.

SAXException

​(

String

message)

Create a new SAXException.

SAXException

​(

String

message,

Exception

e)

Create a new SAXException from an existing exception.

---

#### Constructor Summary

Create a new SAXException.

Create a new SAXException wrapping an existing exception.

Create a new SAXException from an existing exception.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Throwable

getCause

()

Return the cause of the exception

Exception

getException

()

Return the embedded exception, if any.

String

getMessage

()

Return a detail message for this exception.

String

toString

()

Override toString to pick up any embedded exception.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

Return the cause of the exception

Return the embedded exception, if any.

Return a detail message for this exception.

Override toString to pick up any embedded exception.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

- SAXException

```java
public SAXException()
```

Create a new SAXException.

- SAXException

```java
public SAXException​(
String
message)
```

Create a new SAXException.

**Parameters:** message

- The error or warning message.

- SAXException

```java
public SAXException​(
Exception
e)
```

Create a new SAXException wrapping an existing exception.

The existing exception will be embedded in the new
one, and its message will become the default message for
the SAXException.

**Parameters:** e

- The exception to be wrapped in a SAXException.

- SAXException

```java
public SAXException​(
String
message,

Exception
e)
```

Create a new SAXException from an existing exception.

The existing exception will be embedded in the new
one, but the new exception will have its own message.

**Parameters:** message

- The detail message.
**Parameters:** e

- The exception to be wrapped in a SAXException.

============ METHOD DETAIL ==========

- Method Detail

- getMessage

```java
public
String
getMessage()
```

Return a detail message for this exception.

If there is an embedded exception, and if the SAXException
has no detail message of its own, this method will return
the detail message from the embedded exception.

**Overrides:** getMessage

in class

Throwable
**Returns:** The error or warning message.

- getException

```java
public
Exception
getException()
```

Return the embedded exception, if any.

**Returns:** The embedded exception, or null if there is none.

- getCause

```java
public
Throwable
getCause()
```

Return the cause of the exception

**Overrides:** getCause

in class

Throwable
**Returns:** Return the cause of the exception

- toString

```java
public
String
toString()
```

Override toString to pick up any embedded exception.

**Overrides:** toString

in class

Throwable
**Returns:** A string representation of this exception.

Constructor Detail

- SAXException

```java
public SAXException()
```

Create a new SAXException.

- SAXException

```java
public SAXException​(
String
message)
```

Create a new SAXException.

**Parameters:** message

- The error or warning message.

- SAXException

```java
public SAXException​(
Exception
e)
```

Create a new SAXException wrapping an existing exception.

The existing exception will be embedded in the new
one, and its message will become the default message for
the SAXException.

**Parameters:** e

- The exception to be wrapped in a SAXException.

- SAXException

```java
public SAXException​(
String
message,

Exception
e)
```

Create a new SAXException from an existing exception.

The existing exception will be embedded in the new
one, but the new exception will have its own message.

**Parameters:** message

- The detail message.
**Parameters:** e

- The exception to be wrapped in a SAXException.

---

#### Constructor Detail

SAXException

```java
public SAXException()
```

Create a new SAXException.

---

#### SAXException

public SAXException()

Create a new SAXException.

SAXException

```java
public SAXException​(
String
message)
```

Create a new SAXException.

**Parameters:** message

- The error or warning message.

---

#### SAXException

public SAXException​(

String

message)

Create a new SAXException.

SAXException

```java
public SAXException​(
Exception
e)
```

Create a new SAXException wrapping an existing exception.

The existing exception will be embedded in the new
one, and its message will become the default message for
the SAXException.

**Parameters:** e

- The exception to be wrapped in a SAXException.

---

#### SAXException

public SAXException​(

Exception

e)

Create a new SAXException wrapping an existing exception.

The existing exception will be embedded in the new
one, and its message will become the default message for
the SAXException.

The existing exception will be embedded in the new
one, and its message will become the default message for
the SAXException.

SAXException

```java
public SAXException​(
String
message,

Exception
e)
```

Create a new SAXException from an existing exception.

The existing exception will be embedded in the new
one, but the new exception will have its own message.

**Parameters:** message

- The detail message.
**Parameters:** e

- The exception to be wrapped in a SAXException.

---

#### SAXException

public SAXException​(

String

message,

Exception

e)

Create a new SAXException from an existing exception.

The existing exception will be embedded in the new
one, but the new exception will have its own message.

The existing exception will be embedded in the new
one, but the new exception will have its own message.

Method Detail

- getMessage

```java
public
String
getMessage()
```

Return a detail message for this exception.

If there is an embedded exception, and if the SAXException
has no detail message of its own, this method will return
the detail message from the embedded exception.

**Overrides:** getMessage

in class

Throwable
**Returns:** The error or warning message.

- getException

```java
public
Exception
getException()
```

Return the embedded exception, if any.

**Returns:** The embedded exception, or null if there is none.

- getCause

```java
public
Throwable
getCause()
```

Return the cause of the exception

**Overrides:** getCause

in class

Throwable
**Returns:** Return the cause of the exception

- toString

```java
public
String
toString()
```

Override toString to pick up any embedded exception.

**Overrides:** toString

in class

Throwable
**Returns:** A string representation of this exception.

---

#### Method Detail

getMessage

```java
public
String
getMessage()
```

Return a detail message for this exception.

If there is an embedded exception, and if the SAXException
has no detail message of its own, this method will return
the detail message from the embedded exception.

**Overrides:** getMessage

in class

Throwable
**Returns:** The error or warning message.

---

#### getMessage

public

String

getMessage()

Return a detail message for this exception.

If there is an embedded exception, and if the SAXException
has no detail message of its own, this method will return
the detail message from the embedded exception.

If there is an embedded exception, and if the SAXException
has no detail message of its own, this method will return
the detail message from the embedded exception.

getException

```java
public
Exception
getException()
```

Return the embedded exception, if any.

**Returns:** The embedded exception, or null if there is none.

---

#### getException

public

Exception

getException()

Return the embedded exception, if any.

getCause

```java
public
Throwable
getCause()
```

Return the cause of the exception

**Overrides:** getCause

in class

Throwable
**Returns:** Return the cause of the exception

---

#### getCause

public

Throwable

getCause()

Return the cause of the exception

toString

```java
public
String
toString()
```

Override toString to pick up any embedded exception.

**Overrides:** toString

in class

Throwable
**Returns:** A string representation of this exception.

---

#### toString

public

String

toString()

Override toString to pick up any embedded exception.

---

