# Class BadLocationException

**Source:** `java.desktop\javax\swing\text\BadLocationException.html`

### Class Description

```java
public class
BadLocationException

extends
Exception
```

This exception is to report bad locations within a document model
(that is, attempts to reference a location that doesn't exist).

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public BadLocationException​(
String
s,
int offs)

Creates a new BadLocationException object.

**Parameters:**
- s

- a string indicating what was wrong with the arguments
- offs

- offset within the document that was requested >= 0

---

### Method Details

#### public int offsetRequested()

Returns the offset into the document that was not legal.

**Returns:**
- the offset >= 0

---

### Additional Sections

#### Class BadLocationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.swing.text.BadLocationException

java.lang.Throwable

- java.lang.Exception
- - javax.swing.text.BadLocationException

java.lang.Exception

- javax.swing.text.BadLocationException

javax.swing.text.BadLocationException

**All Implemented Interfaces:** Serializable

```java
public class
BadLocationException

extends
Exception
```

This exception is to report bad locations within a document model
(that is, attempts to reference a location that doesn't exist).

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** Serialized Form

public class

BadLocationException

extends

Exception

This exception is to report bad locations within a document model
(that is, attempts to reference a location that doesn't exist).

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BadLocationException

​(

String

s,
int offs)

Creates a new BadLocationException object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

offsetRequested

()

Returns the offset into the document that was not legal.

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

BadLocationException

​(

String

s,
int offs)

Creates a new BadLocationException object.

---

#### Constructor Summary

Creates a new BadLocationException object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

offsetRequested

()

Returns the offset into the document that was not legal.

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

Returns the offset into the document that was not legal.

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

- BadLocationException

```java
public BadLocationException​(
String
s,
int offs)
```

Creates a new BadLocationException object.

**Parameters:** s

- a string indicating what was wrong with the arguments
**Parameters:** offs

- offset within the document that was requested >= 0

============ METHOD DETAIL ==========

- Method Detail

- offsetRequested

```java
public int offsetRequested()
```

Returns the offset into the document that was not legal.

**Returns:** the offset >= 0

Constructor Detail

- BadLocationException

```java
public BadLocationException​(
String
s,
int offs)
```

Creates a new BadLocationException object.

**Parameters:** s

- a string indicating what was wrong with the arguments
**Parameters:** offs

- offset within the document that was requested >= 0

---

#### Constructor Detail

BadLocationException

```java
public BadLocationException​(
String
s,
int offs)
```

Creates a new BadLocationException object.

**Parameters:** s

- a string indicating what was wrong with the arguments
**Parameters:** offs

- offset within the document that was requested >= 0

---

#### BadLocationException

public BadLocationException​(

String

s,
int offs)

Creates a new BadLocationException object.

Method Detail

- offsetRequested

```java
public int offsetRequested()
```

Returns the offset into the document that was not legal.

**Returns:** the offset >= 0

---

#### Method Detail

offsetRequested

```java
public int offsetRequested()
```

Returns the offset into the document that was not legal.

**Returns:** the offset >= 0

---

#### offsetRequested

public int offsetRequested()

Returns the offset into the document that was not legal.

---

