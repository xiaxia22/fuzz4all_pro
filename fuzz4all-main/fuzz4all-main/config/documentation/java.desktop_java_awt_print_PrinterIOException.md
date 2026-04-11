# Class PrinterIOException

**Source:** `java.desktop\java\awt\print\PrinterIOException.html`

### Class Description

```java
public class
PrinterIOException

extends
PrinterException
```

The

PrinterIOException

class is a subclass of

PrinterException

and is used to indicate that an IO error
of some sort has occurred while printing.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The
"

IOException

that terminated the print job"
that is provided at construction time and accessed via the

getIOException()

method is now known as the

cause

,
and may be accessed via the

Throwable.getCause()

method,
as well as the aforementioned "legacy method."

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public PrinterIOException​(
IOException
exception)

Constructs a new

PrinterIOException

with the string representation of the specified

IOException

.

**Parameters:**
- exception

- the specified

IOException

---

### Method Details

#### public
IOException
getIOException()

Returns the

IOException

that terminated
the print job.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:**
- the

IOException

that terminated
the print job.

**See Also:**
- IOException

---

#### public
Throwable
getCause()

Returns the cause of this exception (the

IOException

that terminated the print job).

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

#### Class PrinterIOException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.awt.print.PrinterException
- - java.awt.print.PrinterIOException

java.lang.Throwable

- java.lang.Exception
- - java.awt.print.PrinterException
- - java.awt.print.PrinterIOException

java.lang.Exception

- java.awt.print.PrinterException
- - java.awt.print.PrinterIOException

java.awt.print.PrinterException

- java.awt.print.PrinterIOException

java.awt.print.PrinterIOException

**All Implemented Interfaces:** Serializable

```java
public class
PrinterIOException

extends
PrinterException
```

The

PrinterIOException

class is a subclass of

PrinterException

and is used to indicate that an IO error
of some sort has occurred while printing.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The
"

IOException

that terminated the print job"
that is provided at construction time and accessed via the

getIOException()

method is now known as the

cause

,
and may be accessed via the

Throwable.getCause()

method,
as well as the aforementioned "legacy method."

**See Also:** Serialized Form

public class

PrinterIOException

extends

PrinterException

The

PrinterIOException

class is a subclass of

PrinterException

and is used to indicate that an IO error
of some sort has occurred while printing.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The
"

IOException

that terminated the print job"
that is provided at construction time and accessed via the

getIOException()

method is now known as the

cause

,
and may be accessed via the

Throwable.getCause()

method,
as well as the aforementioned "legacy method."

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The
"

IOException

that terminated the print job"
that is provided at construction time and accessed via the

getIOException()

method is now known as the

cause

,
and may be accessed via the

Throwable.getCause()

method,
as well as the aforementioned "legacy method."

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PrinterIOException

​(

IOException

exception)

Constructs a new

PrinterIOException

with the string representation of the specified

IOException

.

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

Returns the cause of this exception (the

IOException

that terminated the print job).

IOException

getIOException

()

Returns the

IOException

that terminated
the print job.

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

PrinterIOException

​(

IOException

exception)

Constructs a new

PrinterIOException

with the string representation of the specified

IOException

.

---

#### Constructor Summary

Constructs a new

PrinterIOException

with the string representation of the specified

IOException

.

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

Returns the cause of this exception (the

IOException

that terminated the print job).

IOException

getIOException

()

Returns the

IOException

that terminated
the print job.

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

Returns the cause of this exception (the

IOException

that terminated the print job).

Returns the

IOException

that terminated
the print job.

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

- PrinterIOException

```java
public PrinterIOException​(
IOException
exception)
```

Constructs a new

PrinterIOException

with the string representation of the specified

IOException

.

**Parameters:** exception

- the specified

IOException

============ METHOD DETAIL ==========

- Method Detail

- getIOException

```java
public
IOException
getIOException()
```

Returns the

IOException

that terminated
the print job.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the

IOException

that terminated
the print job.
**See Also:** IOException

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception (the

IOException

that terminated the print job).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this exception.
**Since:** 1.4

Constructor Detail

- PrinterIOException

```java
public PrinterIOException​(
IOException
exception)
```

Constructs a new

PrinterIOException

with the string representation of the specified

IOException

.

**Parameters:** exception

- the specified

IOException

---

#### Constructor Detail

PrinterIOException

```java
public PrinterIOException​(
IOException
exception)
```

Constructs a new

PrinterIOException

with the string representation of the specified

IOException

.

**Parameters:** exception

- the specified

IOException

---

#### PrinterIOException

public PrinterIOException​(

IOException

exception)

Constructs a new

PrinterIOException

with the string representation of the specified

IOException

.

Method Detail

- getIOException

```java
public
IOException
getIOException()
```

Returns the

IOException

that terminated
the print job.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the

IOException

that terminated
the print job.
**See Also:** IOException

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception (the

IOException

that terminated the print job).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this exception.
**Since:** 1.4

---

#### Method Detail

getIOException

```java
public
IOException
getIOException()
```

Returns the

IOException

that terminated
the print job.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the

IOException

that terminated
the print job.
**See Also:** IOException

---

#### getIOException

public

IOException

getIOException()

Returns the

IOException

that terminated
the print job.

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

Returns the cause of this exception (the

IOException

that terminated the print job).

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

Returns the cause of this exception (the

IOException

that terminated the print job).

---

