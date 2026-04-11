# Class TransformerException

**Source:** `java.xml\javax\xml\transform\TransformerException.html`

### Class Description

```java
public class
TransformerException

extends
Exception
```

This class specifies an exceptional condition that occurred
during the transformation process.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public TransformerException​(
String
message)

Create a new TransformerException.

**Parameters:**
- message

- The error or warning message.

---

#### public TransformerException​(
Throwable
e)

Create a new TransformerException wrapping an existing exception.

**Parameters:**
- e

- The exception to be wrapped.

---

#### public TransformerException​(
String
message,

Throwable
e)

Wrap an existing exception in a TransformerException.

This is used for throwing processor exceptions before
the processing has started.

**Parameters:**
- message

- The error or warning message, or null to
use the message from the embedded exception.
- e

- Any exception

---

#### public TransformerException​(
String
message,

SourceLocator
locator)

Create a new TransformerException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a DocumentHandler
callback.

**Parameters:**
- message

- The error or warning message.
- locator

- The locator object for the error or warning.

---

#### public TransformerException​(
String
message,

SourceLocator
locator,

Throwable
e)

Wrap an existing exception in a TransformerException.

**Parameters:**
- message

- The error or warning message, or null to
use the message from the embedded exception.
- locator

- The locator object for the error or warning.
- e

- Any exception

---

### Method Details

#### public
SourceLocator
getLocator()

Method getLocator retrieves an instance of a SourceLocator
object that specifies where an error occurred.

**Returns:**
- A SourceLocator object, or null if none was specified.

---

#### public void setLocator​(
SourceLocator
location)

Method setLocator sets an instance of a SourceLocator
object that specifies where an error occurred.

**Parameters:**
- location

- A SourceLocator object, or null to clear the location.

---

#### public
Throwable
getException()

This method retrieves an exception that this exception wraps.

**Returns:**
- An Throwable object, or null.

**See Also:**
- getCause()

---

#### public
Throwable
getCause()

Returns the cause of this throwable or

null

if the
cause is nonexistent or unknown. (The cause is the throwable that
caused this throwable to get thrown.)

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the cause, or null if unknown

---

#### public
Throwable
initCause​(
Throwable
cause)

Initializes the

cause

of this throwable to the specified value.
(The cause is the throwable that caused this throwable to get thrown.)

This method can be called at most once. It is generally called from
within the constructor, or immediately after creating the
throwable. If this throwable was created
with

TransformerException(Throwable)

or

TransformerException(String,Throwable)

, this method cannot be called
even once.

**Overrides:**
- initCause

in class

Throwable

**Parameters:**
- cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)

**Returns:**
- a reference to this

Throwable

instance.

**Throws:**
- IllegalArgumentException

- if

cause

is this
throwable. (A throwable cannot
be its own cause.)
- IllegalStateException

- if this throwable was
created with

TransformerException(Throwable)

or

TransformerException(String,Throwable)

, or this method has already
been called on this throwable.

---

#### public
String
getMessageAndLocation()

Get the error message with location information
appended.

**Returns:**
- A

String

representing the error message with
location information appended.

---

#### public
String
getLocationAsString()

Get the location information as a string.

**Returns:**
- A string with location info, or null
if there is no location information.

---

#### public void printStackTrace()

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

**Overrides:**
- printStackTrace

in class

Throwable

---

#### public void printStackTrace​(
PrintStream
s)

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

**Overrides:**
- printStackTrace

in class

Throwable

**Parameters:**
- s

- The stream where the dump will be sent to.

---

#### public void printStackTrace​(
PrintWriter
s)

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

**Overrides:**
- printStackTrace

in class

Throwable

**Parameters:**
- s

- The writer where the dump will be sent to.

---

### Additional Sections

#### Class TransformerException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.xml.transform.TransformerException

java.lang.Throwable

- java.lang.Exception
- - javax.xml.transform.TransformerException

java.lang.Exception

- javax.xml.transform.TransformerException

javax.xml.transform.TransformerException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** TransformerConfigurationException

```java
public class
TransformerException

extends
Exception
```

This class specifies an exceptional condition that occurred
during the transformation process.

**Since:** 1.4
**See Also:** Serialized Form

public class

TransformerException

extends

Exception

This class specifies an exceptional condition that occurred
during the transformation process.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TransformerException

​(

String

message)

Create a new TransformerException.

TransformerException

​(

String

message,

Throwable

e)

Wrap an existing exception in a TransformerException.

TransformerException

​(

String

message,

SourceLocator

locator)

Create a new TransformerException from a message and a Locator.

TransformerException

​(

String

message,

SourceLocator

locator,

Throwable

e)

Wrap an existing exception in a TransformerException.

TransformerException

​(

Throwable

e)

Create a new TransformerException wrapping an existing exception.

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

Returns the cause of this throwable or

null

if the
cause is nonexistent or unknown.

Throwable

getException

()

This method retrieves an exception that this exception wraps.

String

getLocationAsString

()

Get the location information as a string.

SourceLocator

getLocator

()

Method getLocator retrieves an instance of a SourceLocator
object that specifies where an error occurred.

String

getMessageAndLocation

()

Get the error message with location information
appended.

Throwable

initCause

​(

Throwable

cause)

Initializes the

cause

of this throwable to the specified value.

void

printStackTrace

()

Print the the trace of methods from where the error
originated.

void

printStackTrace

​(

PrintStream

s)

Print the the trace of methods from where the error
originated.

void

printStackTrace

​(

PrintWriter

s)

Print the the trace of methods from where the error
originated.

void

setLocator

​(

SourceLocator

location)

Method setLocator sets an instance of a SourceLocator
object that specifies where an error occurred.

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

TransformerException

​(

String

message)

Create a new TransformerException.

TransformerException

​(

String

message,

Throwable

e)

Wrap an existing exception in a TransformerException.

TransformerException

​(

String

message,

SourceLocator

locator)

Create a new TransformerException from a message and a Locator.

TransformerException

​(

String

message,

SourceLocator

locator,

Throwable

e)

Wrap an existing exception in a TransformerException.

TransformerException

​(

Throwable

e)

Create a new TransformerException wrapping an existing exception.

---

#### Constructor Summary

Create a new TransformerException.

Wrap an existing exception in a TransformerException.

Create a new TransformerException from a message and a Locator.

Create a new TransformerException wrapping an existing exception.

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

Returns the cause of this throwable or

null

if the
cause is nonexistent or unknown.

Throwable

getException

()

This method retrieves an exception that this exception wraps.

String

getLocationAsString

()

Get the location information as a string.

SourceLocator

getLocator

()

Method getLocator retrieves an instance of a SourceLocator
object that specifies where an error occurred.

String

getMessageAndLocation

()

Get the error message with location information
appended.

Throwable

initCause

​(

Throwable

cause)

Initializes the

cause

of this throwable to the specified value.

void

printStackTrace

()

Print the the trace of methods from where the error
originated.

void

printStackTrace

​(

PrintStream

s)

Print the the trace of methods from where the error
originated.

void

printStackTrace

​(

PrintWriter

s)

Print the the trace of methods from where the error
originated.

void

setLocator

​(

SourceLocator

location)

Method setLocator sets an instance of a SourceLocator
object that specifies where an error occurred.

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

Returns the cause of this throwable or

null

if the
cause is nonexistent or unknown.

This method retrieves an exception that this exception wraps.

Get the location information as a string.

Method getLocator retrieves an instance of a SourceLocator
object that specifies where an error occurred.

Get the error message with location information
appended.

Initializes the

cause

of this throwable to the specified value.

Print the the trace of methods from where the error
originated.

Method setLocator sets an instance of a SourceLocator
object that specifies where an error occurred.

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

- TransformerException

```java
public TransformerException​(
String
message)
```

Create a new TransformerException.

**Parameters:** message

- The error or warning message.

- TransformerException

```java
public TransformerException​(
Throwable
e)
```

Create a new TransformerException wrapping an existing exception.

**Parameters:** e

- The exception to be wrapped.

- TransformerException

```java
public TransformerException​(
String
message,

Throwable
e)
```

Wrap an existing exception in a TransformerException.

This is used for throwing processor exceptions before
the processing has started.

**Parameters:** message

- The error or warning message, or null to
use the message from the embedded exception.
**Parameters:** e

- Any exception

- TransformerException

```java
public TransformerException​(
String
message,

SourceLocator
locator)
```

Create a new TransformerException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a DocumentHandler
callback.

**Parameters:** message

- The error or warning message.
**Parameters:** locator

- The locator object for the error or warning.

- TransformerException

```java
public TransformerException​(
String
message,

SourceLocator
locator,

Throwable
e)
```

Wrap an existing exception in a TransformerException.

**Parameters:** message

- The error or warning message, or null to
use the message from the embedded exception.
**Parameters:** locator

- The locator object for the error or warning.
**Parameters:** e

- Any exception

============ METHOD DETAIL ==========

- Method Detail

- getLocator

```java
public
SourceLocator
getLocator()
```

Method getLocator retrieves an instance of a SourceLocator
object that specifies where an error occurred.

**Returns:** A SourceLocator object, or null if none was specified.

- setLocator

```java
public void setLocator​(
SourceLocator
location)
```

Method setLocator sets an instance of a SourceLocator
object that specifies where an error occurred.

**Parameters:** location

- A SourceLocator object, or null to clear the location.

- getException

```java
public
Throwable
getException()
```

This method retrieves an exception that this exception wraps.

**Returns:** An Throwable object, or null.
**See Also:** getCause()

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this throwable or

null

if the
cause is nonexistent or unknown. (The cause is the throwable that
caused this throwable to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause, or null if unknown

- initCause

```java
public
Throwable
initCause​(
Throwable
cause)
```

Initializes the

cause

of this throwable to the specified value.
(The cause is the throwable that caused this throwable to get thrown.)

This method can be called at most once. It is generally called from
within the constructor, or immediately after creating the
throwable. If this throwable was created
with

TransformerException(Throwable)

or

TransformerException(String,Throwable)

, this method cannot be called
even once.

**Overrides:** initCause

in class

Throwable
**Parameters:** cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Returns:** a reference to this

Throwable

instance.
**Throws:** IllegalArgumentException

- if

cause

is this
throwable. (A throwable cannot
be its own cause.)
**Throws:** IllegalStateException

- if this throwable was
created with

TransformerException(Throwable)

or

TransformerException(String,Throwable)

, or this method has already
been called on this throwable.

- getMessageAndLocation

```java
public
String
getMessageAndLocation()
```

Get the error message with location information
appended.

**Returns:** A

String

representing the error message with
location information appended.

- getLocationAsString

```java
public
String
getLocationAsString()
```

Get the location information as a string.

**Returns:** A string with location info, or null
if there is no location information.

- printStackTrace

```java
public void printStackTrace()
```

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

**Overrides:** printStackTrace

in class

Throwable

- printStackTrace

```java
public void printStackTrace​(
PrintStream
s)
```

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

- The stream where the dump will be sent to.

- printStackTrace

```java
public void printStackTrace​(
PrintWriter
s)
```

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

- The writer where the dump will be sent to.

Constructor Detail

- TransformerException

```java
public TransformerException​(
String
message)
```

Create a new TransformerException.

**Parameters:** message

- The error or warning message.

- TransformerException

```java
public TransformerException​(
Throwable
e)
```

Create a new TransformerException wrapping an existing exception.

**Parameters:** e

- The exception to be wrapped.

- TransformerException

```java
public TransformerException​(
String
message,

Throwable
e)
```

Wrap an existing exception in a TransformerException.

This is used for throwing processor exceptions before
the processing has started.

**Parameters:** message

- The error or warning message, or null to
use the message from the embedded exception.
**Parameters:** e

- Any exception

- TransformerException

```java
public TransformerException​(
String
message,

SourceLocator
locator)
```

Create a new TransformerException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a DocumentHandler
callback.

**Parameters:** message

- The error or warning message.
**Parameters:** locator

- The locator object for the error or warning.

- TransformerException

```java
public TransformerException​(
String
message,

SourceLocator
locator,

Throwable
e)
```

Wrap an existing exception in a TransformerException.

**Parameters:** message

- The error or warning message, or null to
use the message from the embedded exception.
**Parameters:** locator

- The locator object for the error or warning.
**Parameters:** e

- Any exception

---

#### Constructor Detail

TransformerException

```java
public TransformerException​(
String
message)
```

Create a new TransformerException.

**Parameters:** message

- The error or warning message.

---

#### TransformerException

public TransformerException​(

String

message)

Create a new TransformerException.

TransformerException

```java
public TransformerException​(
Throwable
e)
```

Create a new TransformerException wrapping an existing exception.

**Parameters:** e

- The exception to be wrapped.

---

#### TransformerException

public TransformerException​(

Throwable

e)

Create a new TransformerException wrapping an existing exception.

TransformerException

```java
public TransformerException​(
String
message,

Throwable
e)
```

Wrap an existing exception in a TransformerException.

This is used for throwing processor exceptions before
the processing has started.

**Parameters:** message

- The error or warning message, or null to
use the message from the embedded exception.
**Parameters:** e

- Any exception

---

#### TransformerException

public TransformerException​(

String

message,

Throwable

e)

Wrap an existing exception in a TransformerException.

This is used for throwing processor exceptions before
the processing has started.

This is used for throwing processor exceptions before
the processing has started.

TransformerException

```java
public TransformerException​(
String
message,

SourceLocator
locator)
```

Create a new TransformerException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a DocumentHandler
callback.

**Parameters:** message

- The error or warning message.
**Parameters:** locator

- The locator object for the error or warning.

---

#### TransformerException

public TransformerException​(

String

message,

SourceLocator

locator)

Create a new TransformerException from a message and a Locator.

This constructor is especially useful when an application is
creating its own exception from within a DocumentHandler
callback.

This constructor is especially useful when an application is
creating its own exception from within a DocumentHandler
callback.

TransformerException

```java
public TransformerException​(
String
message,

SourceLocator
locator,

Throwable
e)
```

Wrap an existing exception in a TransformerException.

**Parameters:** message

- The error or warning message, or null to
use the message from the embedded exception.
**Parameters:** locator

- The locator object for the error or warning.
**Parameters:** e

- Any exception

---

#### TransformerException

public TransformerException​(

String

message,

SourceLocator

locator,

Throwable

e)

Wrap an existing exception in a TransformerException.

Method Detail

- getLocator

```java
public
SourceLocator
getLocator()
```

Method getLocator retrieves an instance of a SourceLocator
object that specifies where an error occurred.

**Returns:** A SourceLocator object, or null if none was specified.

- setLocator

```java
public void setLocator​(
SourceLocator
location)
```

Method setLocator sets an instance of a SourceLocator
object that specifies where an error occurred.

**Parameters:** location

- A SourceLocator object, or null to clear the location.

- getException

```java
public
Throwable
getException()
```

This method retrieves an exception that this exception wraps.

**Returns:** An Throwable object, or null.
**See Also:** getCause()

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this throwable or

null

if the
cause is nonexistent or unknown. (The cause is the throwable that
caused this throwable to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause, or null if unknown

- initCause

```java
public
Throwable
initCause​(
Throwable
cause)
```

Initializes the

cause

of this throwable to the specified value.
(The cause is the throwable that caused this throwable to get thrown.)

This method can be called at most once. It is generally called from
within the constructor, or immediately after creating the
throwable. If this throwable was created
with

TransformerException(Throwable)

or

TransformerException(String,Throwable)

, this method cannot be called
even once.

**Overrides:** initCause

in class

Throwable
**Parameters:** cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Returns:** a reference to this

Throwable

instance.
**Throws:** IllegalArgumentException

- if

cause

is this
throwable. (A throwable cannot
be its own cause.)
**Throws:** IllegalStateException

- if this throwable was
created with

TransformerException(Throwable)

or

TransformerException(String,Throwable)

, or this method has already
been called on this throwable.

- getMessageAndLocation

```java
public
String
getMessageAndLocation()
```

Get the error message with location information
appended.

**Returns:** A

String

representing the error message with
location information appended.

- getLocationAsString

```java
public
String
getLocationAsString()
```

Get the location information as a string.

**Returns:** A string with location info, or null
if there is no location information.

- printStackTrace

```java
public void printStackTrace()
```

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

**Overrides:** printStackTrace

in class

Throwable

- printStackTrace

```java
public void printStackTrace​(
PrintStream
s)
```

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

- The stream where the dump will be sent to.

- printStackTrace

```java
public void printStackTrace​(
PrintWriter
s)
```

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

- The writer where the dump will be sent to.

---

#### Method Detail

getLocator

```java
public
SourceLocator
getLocator()
```

Method getLocator retrieves an instance of a SourceLocator
object that specifies where an error occurred.

**Returns:** A SourceLocator object, or null if none was specified.

---

#### getLocator

public

SourceLocator

getLocator()

Method getLocator retrieves an instance of a SourceLocator
object that specifies where an error occurred.

setLocator

```java
public void setLocator​(
SourceLocator
location)
```

Method setLocator sets an instance of a SourceLocator
object that specifies where an error occurred.

**Parameters:** location

- A SourceLocator object, or null to clear the location.

---

#### setLocator

public void setLocator​(

SourceLocator

location)

Method setLocator sets an instance of a SourceLocator
object that specifies where an error occurred.

getException

```java
public
Throwable
getException()
```

This method retrieves an exception that this exception wraps.

**Returns:** An Throwable object, or null.
**See Also:** getCause()

---

#### getException

public

Throwable

getException()

This method retrieves an exception that this exception wraps.

getCause

```java
public
Throwable
getCause()
```

Returns the cause of this throwable or

null

if the
cause is nonexistent or unknown. (The cause is the throwable that
caused this throwable to get thrown.)

**Overrides:** getCause

in class

Throwable
**Returns:** the cause, or null if unknown

---

#### getCause

public

Throwable

getCause()

Returns the cause of this throwable or

null

if the
cause is nonexistent or unknown. (The cause is the throwable that
caused this throwable to get thrown.)

initCause

```java
public
Throwable
initCause​(
Throwable
cause)
```

Initializes the

cause

of this throwable to the specified value.
(The cause is the throwable that caused this throwable to get thrown.)

This method can be called at most once. It is generally called from
within the constructor, or immediately after creating the
throwable. If this throwable was created
with

TransformerException(Throwable)

or

TransformerException(String,Throwable)

, this method cannot be called
even once.

**Overrides:** initCause

in class

Throwable
**Parameters:** cause

- the cause (which is saved for later retrieval by the

getCause()

method). (A

null

value is
permitted, and indicates that the cause is nonexistent or
unknown.)
**Returns:** a reference to this

Throwable

instance.
**Throws:** IllegalArgumentException

- if

cause

is this
throwable. (A throwable cannot
be its own cause.)
**Throws:** IllegalStateException

- if this throwable was
created with

TransformerException(Throwable)

or

TransformerException(String,Throwable)

, or this method has already
been called on this throwable.

---

#### initCause

public

Throwable

initCause​(

Throwable

cause)

Initializes the

cause

of this throwable to the specified value.
(The cause is the throwable that caused this throwable to get thrown.)

This method can be called at most once. It is generally called from
within the constructor, or immediately after creating the
throwable. If this throwable was created
with

TransformerException(Throwable)

or

TransformerException(String,Throwable)

, this method cannot be called
even once.

This method can be called at most once. It is generally called from
within the constructor, or immediately after creating the
throwable. If this throwable was created
with

TransformerException(Throwable)

or

TransformerException(String,Throwable)

, this method cannot be called
even once.

getMessageAndLocation

```java
public
String
getMessageAndLocation()
```

Get the error message with location information
appended.

**Returns:** A

String

representing the error message with
location information appended.

---

#### getMessageAndLocation

public

String

getMessageAndLocation()

Get the error message with location information
appended.

getLocationAsString

```java
public
String
getLocationAsString()
```

Get the location information as a string.

**Returns:** A string with location info, or null
if there is no location information.

---

#### getLocationAsString

public

String

getLocationAsString()

Get the location information as a string.

printStackTrace

```java
public void printStackTrace()
```

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

**Overrides:** printStackTrace

in class

Throwable

---

#### printStackTrace

public void printStackTrace()

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

printStackTrace

```java
public void printStackTrace​(
PrintStream
s)
```

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

- The stream where the dump will be sent to.

---

#### printStackTrace

public void printStackTrace​(

PrintStream

s)

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

printStackTrace

```java
public void printStackTrace​(
PrintWriter
s)
```

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

**Overrides:** printStackTrace

in class

Throwable
**Parameters:** s

- The writer where the dump will be sent to.

---

#### printStackTrace

public void printStackTrace​(

PrintWriter

s)

Print the the trace of methods from where the error
originated. This will trace all nested exception
objects, as well as this object.

---

