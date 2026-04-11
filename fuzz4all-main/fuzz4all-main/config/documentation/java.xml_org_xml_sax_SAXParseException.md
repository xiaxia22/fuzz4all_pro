# Class SAXParseException

**Source:** `java.xml\org\xml\sax\SAXParseException.html`

### Class Description

```java
public class
SAXParseException

extends
SAXException
```

Encapsulate an XML parse error or warning.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This exception may include information for locating the error
in the original XML document, as if it came from a

Locator

object. Note that although the application
will receive a SAXParseException as the argument to the handlers
in the

ErrorHandler

interface,
the application is not actually required to throw the exception;
instead, it can simply read the information in it and take a
different action.

Since this exception is a subclass of

SAXException

, it inherits the ability to wrap another exception.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SAXParseException​(
String
message,

Locator
locator)

Create a new SAXParseException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a

ContentHandler

callback.

**Parameters:**
- message

- The error or warning message.
- locator

- The locator object for the error or warning (may be
null).

**See Also:**
- Locator

---

#### public SAXParseException​(
String
message,

Locator
locator,

Exception
e)

Wrap an existing exception in a SAXParseException.

This constructor is especially useful when an application is
creating its own exception from within a

ContentHandler

callback, and needs to wrap an existing exception that is not a
subclass of

SAXException

.

**Parameters:**
- message

- The error or warning message, or null to
use the message from the embedded exception.
- locator

- The locator object for the error or warning (may be
null).
- e

- Any exception.

**See Also:**
- Locator

---

#### public SAXParseException​(
String
message,

String
publicId,

String
systemId,
int lineNumber,
int columnNumber)

Create a new SAXParseException.

This constructor is most useful for parser writers.

All parameters except the message are as if
they were provided by a

Locator

. For example, if the
system identifier is a URL (including relative filename), the
caller must resolve it fully before creating the exception.

**Parameters:**
- message

- The error or warning message.
- publicId

- The public identifier of the entity that generated
the error or warning.
- systemId

- The system identifier of the entity that generated
the error or warning.
- lineNumber

- The line number of the end of the text that
caused the error or warning.
- columnNumber

- The column number of the end of the text that
cause the error or warning.

---

#### public SAXParseException​(
String
message,

String
publicId,

String
systemId,
int lineNumber,
int columnNumber,

Exception
e)

Create a new SAXParseException with an embedded exception.

This constructor is most useful for parser writers who
need to wrap an exception that is not a subclass of

SAXException

.

All parameters except the message and exception are as if
they were provided by a

Locator

. For example, if the
system identifier is a URL (including relative filename), the
caller must resolve it fully before creating the exception.

**Parameters:**
- message

- The error or warning message, or null to use
the message from the embedded exception.
- publicId

- The public identifier of the entity that generated
the error or warning.
- systemId

- The system identifier of the entity that generated
the error or warning.
- lineNumber

- The line number of the end of the text that
caused the error or warning.
- columnNumber

- The column number of the end of the text that
cause the error or warning.
- e

- Another exception to embed in this one.

---

### Method Details

#### public
String
getPublicId()

Get the public identifier of the entity where the exception occurred.

**Returns:**
- A string containing the public identifier, or null
if none is available.

**See Also:**
- Locator.getPublicId()

---

#### public
String
getSystemId()

Get the system identifier of the entity where the exception occurred.

If the system identifier is a URL, it will have been resolved
fully.

**Returns:**
- A string containing the system identifier, or null
if none is available.

**See Also:**
- Locator.getSystemId()

---

#### public int getLineNumber()

The line number of the end of the text where the exception occurred.

The first line is line 1.

**Returns:**
- An integer representing the line number, or -1
if none is available.

**See Also:**
- Locator.getLineNumber()

---

#### public int getColumnNumber()

The column number of the end of the text where the exception occurred.

The first column in a line is position 1.

**Returns:**
- An integer representing the column number, or -1
if none is available.

**See Also:**
- Locator.getColumnNumber()

---

#### public
String
toString()

Override toString to provide more detailed error message.

**Overrides:**
- toString

in class

SAXException

**Returns:**
- A string representation of this exception.

---

### Additional Sections

#### Class SAXParseException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - org.xml.sax.SAXException
- - org.xml.sax.SAXParseException

java.lang.Throwable

- java.lang.Exception
- - org.xml.sax.SAXException
- - org.xml.sax.SAXParseException

java.lang.Exception

- org.xml.sax.SAXException
- - org.xml.sax.SAXParseException

org.xml.sax.SAXException

- org.xml.sax.SAXParseException

org.xml.sax.SAXParseException

**All Implemented Interfaces:** Serializable

```java
public class
SAXParseException

extends
SAXException
```

Encapsulate an XML parse error or warning.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This exception may include information for locating the error
in the original XML document, as if it came from a

Locator

object. Note that although the application
will receive a SAXParseException as the argument to the handlers
in the

ErrorHandler

interface,
the application is not actually required to throw the exception;
instead, it can simply read the information in it and take a
different action.

Since this exception is a subclass of

SAXException

, it inherits the ability to wrap another exception.

**Since:** 1.4, SAX 1.0
**See Also:** SAXException

,

Locator

,

ErrorHandler

,

Serialized Form

public class

SAXParseException

extends

SAXException

Encapsulate an XML parse error or warning.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This exception may include information for locating the error
in the original XML document, as if it came from a

Locator

object. Note that although the application
will receive a SAXParseException as the argument to the handlers
in the

ErrorHandler

interface,
the application is not actually required to throw the exception;
instead, it can simply read the information in it and take a
different action.

Since this exception is a subclass of

SAXException

, it inherits the ability to wrap another exception.

This exception may include information for locating the error
in the original XML document, as if it came from a

Locator

object. Note that although the application
will receive a SAXParseException as the argument to the handlers
in the

ErrorHandler

interface,
the application is not actually required to throw the exception;
instead, it can simply read the information in it and take a
different action.

Since this exception is a subclass of

SAXException

, it inherits the ability to wrap another exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SAXParseException

​(

String

message,

String

publicId,

String

systemId,
int lineNumber,
int columnNumber)

Create a new SAXParseException.

SAXParseException

​(

String

message,

String

publicId,

String

systemId,
int lineNumber,
int columnNumber,

Exception

e)

Create a new SAXParseException with an embedded exception.

SAXParseException

​(

String

message,

Locator

locator)

Create a new SAXParseException from a message and a Locator.

SAXParseException

​(

String

message,

Locator

locator,

Exception

e)

Wrap an existing exception in a SAXParseException.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getColumnNumber

()

The column number of the end of the text where the exception occurred.

int

getLineNumber

()

The line number of the end of the text where the exception occurred.

String

getPublicId

()

Get the public identifier of the entity where the exception occurred.

String

getSystemId

()

Get the system identifier of the entity where the exception occurred.

String

toString

()

Override toString to provide more detailed error message.

- Methods declared in class org.xml.sax.

SAXException

getCause

,

getException

,

getMessage

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

SAXParseException

​(

String

message,

String

publicId,

String

systemId,
int lineNumber,
int columnNumber)

Create a new SAXParseException.

SAXParseException

​(

String

message,

String

publicId,

String

systemId,
int lineNumber,
int columnNumber,

Exception

e)

Create a new SAXParseException with an embedded exception.

SAXParseException

​(

String

message,

Locator

locator)

Create a new SAXParseException from a message and a Locator.

SAXParseException

​(

String

message,

Locator

locator,

Exception

e)

Wrap an existing exception in a SAXParseException.

---

#### Constructor Summary

Create a new SAXParseException.

Create a new SAXParseException with an embedded exception.

Create a new SAXParseException from a message and a Locator.

Wrap an existing exception in a SAXParseException.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getColumnNumber

()

The column number of the end of the text where the exception occurred.

int

getLineNumber

()

The line number of the end of the text where the exception occurred.

String

getPublicId

()

Get the public identifier of the entity where the exception occurred.

String

getSystemId

()

Get the system identifier of the entity where the exception occurred.

String

toString

()

Override toString to provide more detailed error message.

- Methods declared in class org.xml.sax.

SAXException

getCause

,

getException

,

getMessage

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

The column number of the end of the text where the exception occurred.

The line number of the end of the text where the exception occurred.

Get the public identifier of the entity where the exception occurred.

Get the system identifier of the entity where the exception occurred.

Override toString to provide more detailed error message.

Methods declared in class org.xml.sax.

SAXException

getCause

,

getException

,

getMessage

---

#### Methods declared in class org.xml.sax. SAXException

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

- SAXParseException

```java
public SAXParseException​(
String
message,

Locator
locator)
```

Create a new SAXParseException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a

ContentHandler

callback.

**Parameters:** message

- The error or warning message.
**Parameters:** locator

- The locator object for the error or warning (may be
null).
**See Also:** Locator

- SAXParseException

```java
public SAXParseException​(
String
message,

Locator
locator,

Exception
e)
```

Wrap an existing exception in a SAXParseException.

This constructor is especially useful when an application is
creating its own exception from within a

ContentHandler

callback, and needs to wrap an existing exception that is not a
subclass of

SAXException

.

**Parameters:** message

- The error or warning message, or null to
use the message from the embedded exception.
**Parameters:** locator

- The locator object for the error or warning (may be
null).
**Parameters:** e

- Any exception.
**See Also:** Locator

- SAXParseException

```java
public SAXParseException​(
String
message,

String
publicId,

String
systemId,
int lineNumber,
int columnNumber)
```

Create a new SAXParseException.

This constructor is most useful for parser writers.

All parameters except the message are as if
they were provided by a

Locator

. For example, if the
system identifier is a URL (including relative filename), the
caller must resolve it fully before creating the exception.

**Parameters:** message

- The error or warning message.
**Parameters:** publicId

- The public identifier of the entity that generated
the error or warning.
**Parameters:** systemId

- The system identifier of the entity that generated
the error or warning.
**Parameters:** lineNumber

- The line number of the end of the text that
caused the error or warning.
**Parameters:** columnNumber

- The column number of the end of the text that
cause the error or warning.

- SAXParseException

```java
public SAXParseException​(
String
message,

String
publicId,

String
systemId,
int lineNumber,
int columnNumber,

Exception
e)
```

Create a new SAXParseException with an embedded exception.

This constructor is most useful for parser writers who
need to wrap an exception that is not a subclass of

SAXException

.

All parameters except the message and exception are as if
they were provided by a

Locator

. For example, if the
system identifier is a URL (including relative filename), the
caller must resolve it fully before creating the exception.

**Parameters:** message

- The error or warning message, or null to use
the message from the embedded exception.
**Parameters:** publicId

- The public identifier of the entity that generated
the error or warning.
**Parameters:** systemId

- The system identifier of the entity that generated
the error or warning.
**Parameters:** lineNumber

- The line number of the end of the text that
caused the error or warning.
**Parameters:** columnNumber

- The column number of the end of the text that
cause the error or warning.
**Parameters:** e

- Another exception to embed in this one.

============ METHOD DETAIL ==========

- Method Detail

- getPublicId

```java
public
String
getPublicId()
```

Get the public identifier of the entity where the exception occurred.

**Returns:** A string containing the public identifier, or null
if none is available.
**See Also:** Locator.getPublicId()

- getSystemId

```java
public
String
getSystemId()
```

Get the system identifier of the entity where the exception occurred.

If the system identifier is a URL, it will have been resolved
fully.

**Returns:** A string containing the system identifier, or null
if none is available.
**See Also:** Locator.getSystemId()

- getLineNumber

```java
public int getLineNumber()
```

The line number of the end of the text where the exception occurred.

The first line is line 1.

**Returns:** An integer representing the line number, or -1
if none is available.
**See Also:** Locator.getLineNumber()

- getColumnNumber

```java
public int getColumnNumber()
```

The column number of the end of the text where the exception occurred.

The first column in a line is position 1.

**Returns:** An integer representing the column number, or -1
if none is available.
**See Also:** Locator.getColumnNumber()

- toString

```java
public
String
toString()
```

Override toString to provide more detailed error message.

**Overrides:** toString

in class

SAXException
**Returns:** A string representation of this exception.

Constructor Detail

- SAXParseException

```java
public SAXParseException​(
String
message,

Locator
locator)
```

Create a new SAXParseException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a

ContentHandler

callback.

**Parameters:** message

- The error or warning message.
**Parameters:** locator

- The locator object for the error or warning (may be
null).
**See Also:** Locator

- SAXParseException

```java
public SAXParseException​(
String
message,

Locator
locator,

Exception
e)
```

Wrap an existing exception in a SAXParseException.

This constructor is especially useful when an application is
creating its own exception from within a

ContentHandler

callback, and needs to wrap an existing exception that is not a
subclass of

SAXException

.

**Parameters:** message

- The error or warning message, or null to
use the message from the embedded exception.
**Parameters:** locator

- The locator object for the error or warning (may be
null).
**Parameters:** e

- Any exception.
**See Also:** Locator

- SAXParseException

```java
public SAXParseException​(
String
message,

String
publicId,

String
systemId,
int lineNumber,
int columnNumber)
```

Create a new SAXParseException.

This constructor is most useful for parser writers.

All parameters except the message are as if
they were provided by a

Locator

. For example, if the
system identifier is a URL (including relative filename), the
caller must resolve it fully before creating the exception.

**Parameters:** message

- The error or warning message.
**Parameters:** publicId

- The public identifier of the entity that generated
the error or warning.
**Parameters:** systemId

- The system identifier of the entity that generated
the error or warning.
**Parameters:** lineNumber

- The line number of the end of the text that
caused the error or warning.
**Parameters:** columnNumber

- The column number of the end of the text that
cause the error or warning.

- SAXParseException

```java
public SAXParseException​(
String
message,

String
publicId,

String
systemId,
int lineNumber,
int columnNumber,

Exception
e)
```

Create a new SAXParseException with an embedded exception.

This constructor is most useful for parser writers who
need to wrap an exception that is not a subclass of

SAXException

.

All parameters except the message and exception are as if
they were provided by a

Locator

. For example, if the
system identifier is a URL (including relative filename), the
caller must resolve it fully before creating the exception.

**Parameters:** message

- The error or warning message, or null to use
the message from the embedded exception.
**Parameters:** publicId

- The public identifier of the entity that generated
the error or warning.
**Parameters:** systemId

- The system identifier of the entity that generated
the error or warning.
**Parameters:** lineNumber

- The line number of the end of the text that
caused the error or warning.
**Parameters:** columnNumber

- The column number of the end of the text that
cause the error or warning.
**Parameters:** e

- Another exception to embed in this one.

---

#### Constructor Detail

SAXParseException

```java
public SAXParseException​(
String
message,

Locator
locator)
```

Create a new SAXParseException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a

ContentHandler

callback.

**Parameters:** message

- The error or warning message.
**Parameters:** locator

- The locator object for the error or warning (may be
null).
**See Also:** Locator

---

#### SAXParseException

public SAXParseException​(

String

message,

Locator

locator)

Create a new SAXParseException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a

ContentHandler

callback.

This constructor is especially useful when an application is
creating its own exception from within a

ContentHandler

callback.

SAXParseException

```java
public SAXParseException​(
String
message,

Locator
locator,

Exception
e)
```

Wrap an existing exception in a SAXParseException.

This constructor is especially useful when an application is
creating its own exception from within a

ContentHandler

callback, and needs to wrap an existing exception that is not a
subclass of

SAXException

.

**Parameters:** message

- The error or warning message, or null to
use the message from the embedded exception.
**Parameters:** locator

- The locator object for the error or warning (may be
null).
**Parameters:** e

- Any exception.
**See Also:** Locator

---

#### SAXParseException

public SAXParseException​(

String

message,

Locator

locator,

Exception

e)

Wrap an existing exception in a SAXParseException.

This constructor is especially useful when an application is
creating its own exception from within a

ContentHandler

callback, and needs to wrap an existing exception that is not a
subclass of

SAXException

.

This constructor is especially useful when an application is
creating its own exception from within a

ContentHandler

callback, and needs to wrap an existing exception that is not a
subclass of

SAXException

.

SAXParseException

```java
public SAXParseException​(
String
message,

String
publicId,

String
systemId,
int lineNumber,
int columnNumber)
```

Create a new SAXParseException.

This constructor is most useful for parser writers.

All parameters except the message are as if
they were provided by a

Locator

. For example, if the
system identifier is a URL (including relative filename), the
caller must resolve it fully before creating the exception.

**Parameters:** message

- The error or warning message.
**Parameters:** publicId

- The public identifier of the entity that generated
the error or warning.
**Parameters:** systemId

- The system identifier of the entity that generated
the error or warning.
**Parameters:** lineNumber

- The line number of the end of the text that
caused the error or warning.
**Parameters:** columnNumber

- The column number of the end of the text that
cause the error or warning.

---

#### SAXParseException

public SAXParseException​(

String

message,

String

publicId,

String

systemId,
int lineNumber,
int columnNumber)

Create a new SAXParseException.

This constructor is most useful for parser writers.

All parameters except the message are as if
they were provided by a

Locator

. For example, if the
system identifier is a URL (including relative filename), the
caller must resolve it fully before creating the exception.

This constructor is most useful for parser writers.

All parameters except the message are as if
they were provided by a

Locator

. For example, if the
system identifier is a URL (including relative filename), the
caller must resolve it fully before creating the exception.

SAXParseException

```java
public SAXParseException​(
String
message,

String
publicId,

String
systemId,
int lineNumber,
int columnNumber,

Exception
e)
```

Create a new SAXParseException with an embedded exception.

This constructor is most useful for parser writers who
need to wrap an exception that is not a subclass of

SAXException

.

All parameters except the message and exception are as if
they were provided by a

Locator

. For example, if the
system identifier is a URL (including relative filename), the
caller must resolve it fully before creating the exception.

**Parameters:** message

- The error or warning message, or null to use
the message from the embedded exception.
**Parameters:** publicId

- The public identifier of the entity that generated
the error or warning.
**Parameters:** systemId

- The system identifier of the entity that generated
the error or warning.
**Parameters:** lineNumber

- The line number of the end of the text that
caused the error or warning.
**Parameters:** columnNumber

- The column number of the end of the text that
cause the error or warning.
**Parameters:** e

- Another exception to embed in this one.

---

#### SAXParseException

public SAXParseException​(

String

message,

String

publicId,

String

systemId,
int lineNumber,
int columnNumber,

Exception

e)

Create a new SAXParseException with an embedded exception.

This constructor is most useful for parser writers who
need to wrap an exception that is not a subclass of

SAXException

.

All parameters except the message and exception are as if
they were provided by a

Locator

. For example, if the
system identifier is a URL (including relative filename), the
caller must resolve it fully before creating the exception.

This constructor is most useful for parser writers who
need to wrap an exception that is not a subclass of

SAXException

.

All parameters except the message and exception are as if
they were provided by a

Locator

. For example, if the
system identifier is a URL (including relative filename), the
caller must resolve it fully before creating the exception.

Method Detail

- getPublicId

```java
public
String
getPublicId()
```

Get the public identifier of the entity where the exception occurred.

**Returns:** A string containing the public identifier, or null
if none is available.
**See Also:** Locator.getPublicId()

- getSystemId

```java
public
String
getSystemId()
```

Get the system identifier of the entity where the exception occurred.

If the system identifier is a URL, it will have been resolved
fully.

**Returns:** A string containing the system identifier, or null
if none is available.
**See Also:** Locator.getSystemId()

- getLineNumber

```java
public int getLineNumber()
```

The line number of the end of the text where the exception occurred.

The first line is line 1.

**Returns:** An integer representing the line number, or -1
if none is available.
**See Also:** Locator.getLineNumber()

- getColumnNumber

```java
public int getColumnNumber()
```

The column number of the end of the text where the exception occurred.

The first column in a line is position 1.

**Returns:** An integer representing the column number, or -1
if none is available.
**See Also:** Locator.getColumnNumber()

- toString

```java
public
String
toString()
```

Override toString to provide more detailed error message.

**Overrides:** toString

in class

SAXException
**Returns:** A string representation of this exception.

---

#### Method Detail

getPublicId

```java
public
String
getPublicId()
```

Get the public identifier of the entity where the exception occurred.

**Returns:** A string containing the public identifier, or null
if none is available.
**See Also:** Locator.getPublicId()

---

#### getPublicId

public

String

getPublicId()

Get the public identifier of the entity where the exception occurred.

getSystemId

```java
public
String
getSystemId()
```

Get the system identifier of the entity where the exception occurred.

If the system identifier is a URL, it will have been resolved
fully.

**Returns:** A string containing the system identifier, or null
if none is available.
**See Also:** Locator.getSystemId()

---

#### getSystemId

public

String

getSystemId()

Get the system identifier of the entity where the exception occurred.

If the system identifier is a URL, it will have been resolved
fully.

If the system identifier is a URL, it will have been resolved
fully.

getLineNumber

```java
public int getLineNumber()
```

The line number of the end of the text where the exception occurred.

The first line is line 1.

**Returns:** An integer representing the line number, or -1
if none is available.
**See Also:** Locator.getLineNumber()

---

#### getLineNumber

public int getLineNumber()

The line number of the end of the text where the exception occurred.

The first line is line 1.

The first line is line 1.

getColumnNumber

```java
public int getColumnNumber()
```

The column number of the end of the text where the exception occurred.

The first column in a line is position 1.

**Returns:** An integer representing the column number, or -1
if none is available.
**See Also:** Locator.getColumnNumber()

---

#### getColumnNumber

public int getColumnNumber()

The column number of the end of the text where the exception occurred.

The first column in a line is position 1.

The first column in a line is position 1.

toString

```java
public
String
toString()
```

Override toString to provide more detailed error message.

**Overrides:** toString

in class

SAXException
**Returns:** A string representation of this exception.

---

#### toString

public

String

toString()

Override toString to provide more detailed error message.

---

