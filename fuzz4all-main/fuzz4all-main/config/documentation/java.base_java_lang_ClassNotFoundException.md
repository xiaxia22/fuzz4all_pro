# Class ClassNotFoundException

**Source:** `java.base\java\lang\ClassNotFoundException.html`

### Class Description

```java
public class
ClassNotFoundException

extends
ReflectiveOperationException
```

Thrown when an application tries to load in a class through its
string name using:

- The

forName

method in class

Class

.

The

findSystemClass

method in class

ClassLoader

.

The

loadClass

method in class

ClassLoader

.

but no definition for the class with the specified name could be found.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "optional exception
that was raised while loading the class" that may be provided at
construction time and accessed via the

getException()

method is
now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy method."

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ClassNotFoundException()

Constructs a

ClassNotFoundException

with no detail message.

---

#### public ClassNotFoundException​(
String
s)

Constructs a

ClassNotFoundException

with the
specified detail message.

**Parameters:**
- s

- the detail message.

---

#### public ClassNotFoundException​(
String
s,

Throwable
ex)

Constructs a

ClassNotFoundException

with the
specified detail message and optional exception that was
raised while loading the class.

**Parameters:**
- s

- the detail message
- ex

- the exception that was raised while loading the class

**Since:**
- 1.2

---

### Method Details

#### public
Throwable
getException()

Returns the exception that was raised if an error occurred while
attempting to load the class. Otherwise, returns

null

.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:**
- the

Exception

that was raised while loading a class

**Since:**
- 1.2

---

#### public
Throwable
getCause()

Returns the cause of this exception (the exception that was raised
if an error occurred while attempting to load the class; otherwise

null

).

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the cause of this exception.

**Since:**
- 1.4

---

### Additional Sections

#### Class ClassNotFoundException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.ReflectiveOperationException
- - java.lang.ClassNotFoundException

java.lang.Throwable

- java.lang.Exception
- - java.lang.ReflectiveOperationException
- - java.lang.ClassNotFoundException

java.lang.Exception

- java.lang.ReflectiveOperationException
- - java.lang.ClassNotFoundException

java.lang.ReflectiveOperationException

- java.lang.ClassNotFoundException

java.lang.ClassNotFoundException

**All Implemented Interfaces:** Serializable

```java
public class
ClassNotFoundException

extends
ReflectiveOperationException
```

Thrown when an application tries to load in a class through its
string name using:

- The

forName

method in class

Class

.

The

findSystemClass

method in class

ClassLoader

.

The

loadClass

method in class

ClassLoader

.

but no definition for the class with the specified name could be found.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "optional exception
that was raised while loading the class" that may be provided at
construction time and accessed via the

getException()

method is
now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy method."

**Since:** 1.0
**See Also:** Class.forName(java.lang.String)

,

ClassLoader.findSystemClass(java.lang.String)

,

ClassLoader.loadClass(java.lang.String, boolean)

,

Serialized Form

public class

ClassNotFoundException

extends

ReflectiveOperationException

Thrown when an application tries to load in a class through its
string name using:

- The

forName

method in class

Class

.

The

findSystemClass

method in class

ClassLoader

.

The

loadClass

method in class

ClassLoader

.

but no definition for the class with the specified name could be found.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "optional exception
that was raised while loading the class" that may be provided at
construction time and accessed via the

getException()

method is
now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy method."

The

forName

method in class

Class

.

The

findSystemClass

method in class

ClassLoader

.

The

loadClass

method in class

ClassLoader

.

but no definition for the class with the specified name could be found.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "optional exception
that was raised while loading the class" that may be provided at
construction time and accessed via the

getException()

method is
now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy method."

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "optional exception
that was raised while loading the class" that may be provided at
construction time and accessed via the

getException()

method is
now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy method."

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ClassNotFoundException

()

Constructs a

ClassNotFoundException

with no detail message.

ClassNotFoundException

​(

String

s)

Constructs a

ClassNotFoundException

with the
specified detail message.

ClassNotFoundException

​(

String

s,

Throwable

ex)

Constructs a

ClassNotFoundException

with the
specified detail message and optional exception that was
raised while loading the class.

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

Returns the cause of this exception (the exception that was raised
if an error occurred while attempting to load the class; otherwise

null

).

Throwable

getException

()

Returns the exception that was raised if an error occurred while
attempting to load the class.

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

ClassNotFoundException

()

Constructs a

ClassNotFoundException

with no detail message.

ClassNotFoundException

​(

String

s)

Constructs a

ClassNotFoundException

with the
specified detail message.

ClassNotFoundException

​(

String

s,

Throwable

ex)

Constructs a

ClassNotFoundException

with the
specified detail message and optional exception that was
raised while loading the class.

---

#### Constructor Summary

Constructs a

ClassNotFoundException

with no detail message.

Constructs a

ClassNotFoundException

with the
specified detail message.

Constructs a

ClassNotFoundException

with the
specified detail message and optional exception that was
raised while loading the class.

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

Returns the cause of this exception (the exception that was raised
if an error occurred while attempting to load the class; otherwise

null

).

Throwable

getException

()

Returns the exception that was raised if an error occurred while
attempting to load the class.

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

Returns the cause of this exception (the exception that was raised
if an error occurred while attempting to load the class; otherwise

null

).

Returns the exception that was raised if an error occurred while
attempting to load the class.

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

- ClassNotFoundException

```java
public ClassNotFoundException()
```

Constructs a

ClassNotFoundException

with no detail message.

- ClassNotFoundException

```java
public ClassNotFoundException​(
String
s)
```

Constructs a

ClassNotFoundException

with the
specified detail message.

**Parameters:** s

- the detail message.

- ClassNotFoundException

```java
public ClassNotFoundException​(
String
s,

Throwable
ex)
```

Constructs a

ClassNotFoundException

with the
specified detail message and optional exception that was
raised while loading the class.

**Parameters:** s

- the detail message
**Parameters:** ex

- the exception that was raised while loading the class
**Since:** 1.2

============ METHOD DETAIL ==========

- Method Detail

- getException

```java
public
Throwable
getException()
```

Returns the exception that was raised if an error occurred while
attempting to load the class. Otherwise, returns

null

.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the

Exception

that was raised while loading a class
**Since:** 1.2

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception (the exception that was raised
if an error occurred while attempting to load the class; otherwise

null

).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this exception.
**Since:** 1.4

Constructor Detail

- ClassNotFoundException

```java
public ClassNotFoundException()
```

Constructs a

ClassNotFoundException

with no detail message.

- ClassNotFoundException

```java
public ClassNotFoundException​(
String
s)
```

Constructs a

ClassNotFoundException

with the
specified detail message.

**Parameters:** s

- the detail message.

- ClassNotFoundException

```java
public ClassNotFoundException​(
String
s,

Throwable
ex)
```

Constructs a

ClassNotFoundException

with the
specified detail message and optional exception that was
raised while loading the class.

**Parameters:** s

- the detail message
**Parameters:** ex

- the exception that was raised while loading the class
**Since:** 1.2

---

#### Constructor Detail

ClassNotFoundException

```java
public ClassNotFoundException()
```

Constructs a

ClassNotFoundException

with no detail message.

---

#### ClassNotFoundException

public ClassNotFoundException()

Constructs a

ClassNotFoundException

with no detail message.

ClassNotFoundException

```java
public ClassNotFoundException​(
String
s)
```

Constructs a

ClassNotFoundException

with the
specified detail message.

**Parameters:** s

- the detail message.

---

#### ClassNotFoundException

public ClassNotFoundException​(

String

s)

Constructs a

ClassNotFoundException

with the
specified detail message.

ClassNotFoundException

```java
public ClassNotFoundException​(
String
s,

Throwable
ex)
```

Constructs a

ClassNotFoundException

with the
specified detail message and optional exception that was
raised while loading the class.

**Parameters:** s

- the detail message
**Parameters:** ex

- the exception that was raised while loading the class
**Since:** 1.2

---

#### ClassNotFoundException

public ClassNotFoundException​(

String

s,

Throwable

ex)

Constructs a

ClassNotFoundException

with the
specified detail message and optional exception that was
raised while loading the class.

Method Detail

- getException

```java
public
Throwable
getException()
```

Returns the exception that was raised if an error occurred while
attempting to load the class. Otherwise, returns

null

.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the

Exception

that was raised while loading a class
**Since:** 1.2

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception (the exception that was raised
if an error occurred while attempting to load the class; otherwise

null

).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this exception.
**Since:** 1.4

---

#### Method Detail

getException

```java
public
Throwable
getException()
```

Returns the exception that was raised if an error occurred while
attempting to load the class. Otherwise, returns

null

.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the

Exception

that was raised while loading a class
**Since:** 1.2

---

#### getException

public

Throwable

getException()

Returns the exception that was raised if an error occurred while
attempting to load the class. Otherwise, returns

null

.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception (the exception that was raised
if an error occurred while attempting to load the class; otherwise

null

).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this exception.
**Since:** 1.4

---

#### getCause

public

Throwable

getCause()

Returns the cause of this exception (the exception that was raised
if an error occurred while attempting to load the class; otherwise

null

).

---

