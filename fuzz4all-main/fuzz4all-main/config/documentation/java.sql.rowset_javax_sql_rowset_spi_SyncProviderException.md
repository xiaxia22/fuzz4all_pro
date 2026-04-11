# Class SyncProviderException

**Source:** `java.sql.rowset\javax\sql\rowset\spi\SyncProviderException.html`

### Class Description

```java
public class
SyncProviderException

extends
SQLException
```

Indicates an error with the

SyncProvider

mechanism. This exception
is created by a

SyncProvider

abstract class extension if it
encounters violations in reading from or writing to the originating data source.

If it is implemented to do so, the

SyncProvider

object may also create a

SyncResolver

object and either initialize the

SyncProviderException

object with it at construction time or set it with the

SyncProvider

object at
a later time.

The method

acceptChanges

will throw this exception after the writer
has finished checking for conflicts and has found one or more conflicts. An
application may catch a

SyncProviderException

object and call its

getSyncResolver

method to get its

SyncResolver

object.
See the code fragment in the interface comment for

SyncResolver

for an example.
This

SyncResolver

object will mirror the

RowSet

object that generated the exception, except that it will contain only the values
from the data source that are in conflict. All other values in the

SyncResolver

object will be

null

.

The

SyncResolver

object may be used to examine and resolve
each conflict in a row and then go to the next row with a conflict to
repeat the procedure.

A

SyncProviderException

object may or may not contain a description of the
condition causing the exception. The inherited method

getMessage

may be
called to retrieve the description if there is one.

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

---

### Field Details

*No entries found.*

### Constructor Details

#### public SyncProviderException()

Creates a new

SyncProviderException

object without a detail message.

---

#### public SyncProviderException​(
String
msg)

Constructs a

SyncProviderException

object with the specified
detail message.

**Parameters:**
- msg

- the detail message

---

#### public SyncProviderException​(
SyncResolver
syncResolver)

Constructs a

SyncProviderException

object with the specified

SyncResolver

instance.

**Parameters:**
- syncResolver

- the

SyncResolver

instance used to
to process the synchronization conflicts

**Throws:**
- IllegalArgumentException

- if the

SyncResolver

object
is

null

.

---

### Method Details

#### public
SyncResolver
getSyncResolver()

Retrieves the

SyncResolver

object that has been set for
this

SyncProviderException

object, or
if none has been set, an instance of the default

SyncResolver

implementation included in the reference implementation.

If a

SyncProviderException

object is thrown, an application
may use this method to generate a

SyncResolver

object
with which to resolve the conflict or conflicts that caused the
exception to be thrown.

**Returns:**
- the

SyncResolver

object set for this

SyncProviderException

object or, if none has
been set, an instance of the default

SyncResolver

implementation. In addition, the default

SyncResolver

implementation is also returned if the

SyncResolver()

or

SyncResolver(String)

constructors are used to instantiate
the

SyncResolver

instance.

---

#### public void setSyncResolver​(
SyncResolver
syncResolver)

Sets the

SyncResolver

object for this

SyncProviderException

object to the one supplied.
If the argument supplied is

null

, a call to the method

getSyncResolver

will return the default reference
implementation of the

SyncResolver

interface.

**Parameters:**
- syncResolver

- the

SyncResolver

object to be set;
cannot be

null

**Throws:**
- IllegalArgumentException

- if the

SyncResolver

object
is

null

.

**See Also:**
- getSyncResolver()

---

### Additional Sections

#### Class SyncProviderException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.sql.SQLException
- - javax.sql.rowset.spi.SyncProviderException

java.lang.Throwable

- java.lang.Exception
- - java.sql.SQLException
- - javax.sql.rowset.spi.SyncProviderException

java.lang.Exception

- java.sql.SQLException
- - javax.sql.rowset.spi.SyncProviderException

java.sql.SQLException

- javax.sql.rowset.spi.SyncProviderException

javax.sql.rowset.spi.SyncProviderException

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

```java
public class
SyncProviderException

extends
SQLException
```

Indicates an error with the

SyncProvider

mechanism. This exception
is created by a

SyncProvider

abstract class extension if it
encounters violations in reading from or writing to the originating data source.

If it is implemented to do so, the

SyncProvider

object may also create a

SyncResolver

object and either initialize the

SyncProviderException

object with it at construction time or set it with the

SyncProvider

object at
a later time.

The method

acceptChanges

will throw this exception after the writer
has finished checking for conflicts and has found one or more conflicts. An
application may catch a

SyncProviderException

object and call its

getSyncResolver

method to get its

SyncResolver

object.
See the code fragment in the interface comment for

SyncResolver

for an example.
This

SyncResolver

object will mirror the

RowSet

object that generated the exception, except that it will contain only the values
from the data source that are in conflict. All other values in the

SyncResolver

object will be

null

.

The

SyncResolver

object may be used to examine and resolve
each conflict in a row and then go to the next row with a conflict to
repeat the procedure.

A

SyncProviderException

object may or may not contain a description of the
condition causing the exception. The inherited method

getMessage

may be
called to retrieve the description if there is one.

**Since:** 1.5
**See Also:** SyncFactory

,

SyncResolver

,

SyncFactoryException

,

Serialized Form

public class

SyncProviderException

extends

SQLException

Indicates an error with the

SyncProvider

mechanism. This exception
is created by a

SyncProvider

abstract class extension if it
encounters violations in reading from or writing to the originating data source.

If it is implemented to do so, the

SyncProvider

object may also create a

SyncResolver

object and either initialize the

SyncProviderException

object with it at construction time or set it with the

SyncProvider

object at
a later time.

The method

acceptChanges

will throw this exception after the writer
has finished checking for conflicts and has found one or more conflicts. An
application may catch a

SyncProviderException

object and call its

getSyncResolver

method to get its

SyncResolver

object.
See the code fragment in the interface comment for

SyncResolver

for an example.
This

SyncResolver

object will mirror the

RowSet

object that generated the exception, except that it will contain only the values
from the data source that are in conflict. All other values in the

SyncResolver

object will be

null

.

The

SyncResolver

object may be used to examine and resolve
each conflict in a row and then go to the next row with a conflict to
repeat the procedure.

A

SyncProviderException

object may or may not contain a description of the
condition causing the exception. The inherited method

getMessage

may be
called to retrieve the description if there is one.

If it is implemented to do so, the

SyncProvider

object may also create a

SyncResolver

object and either initialize the

SyncProviderException

object with it at construction time or set it with the

SyncProvider

object at
a later time.

The method

acceptChanges

will throw this exception after the writer
has finished checking for conflicts and has found one or more conflicts. An
application may catch a

SyncProviderException

object and call its

getSyncResolver

method to get its

SyncResolver

object.
See the code fragment in the interface comment for

SyncResolver

for an example.
This

SyncResolver

object will mirror the

RowSet

object that generated the exception, except that it will contain only the values
from the data source that are in conflict. All other values in the

SyncResolver

object will be

null

.

The

SyncResolver

object may be used to examine and resolve
each conflict in a row and then go to the next row with a conflict to
repeat the procedure.

A

SyncProviderException

object may or may not contain a description of the
condition causing the exception. The inherited method

getMessage

may be
called to retrieve the description if there is one.

The method

acceptChanges

will throw this exception after the writer
has finished checking for conflicts and has found one or more conflicts. An
application may catch a

SyncProviderException

object and call its

getSyncResolver

method to get its

SyncResolver

object.
See the code fragment in the interface comment for

SyncResolver

for an example.
This

SyncResolver

object will mirror the

RowSet

object that generated the exception, except that it will contain only the values
from the data source that are in conflict. All other values in the

SyncResolver

object will be

null

.

The

SyncResolver

object may be used to examine and resolve
each conflict in a row and then go to the next row with a conflict to
repeat the procedure.

A

SyncProviderException

object may or may not contain a description of the
condition causing the exception. The inherited method

getMessage

may be
called to retrieve the description if there is one.

The

SyncResolver

object may be used to examine and resolve
each conflict in a row and then go to the next row with a conflict to
repeat the procedure.

A

SyncProviderException

object may or may not contain a description of the
condition causing the exception. The inherited method

getMessage

may be
called to retrieve the description if there is one.

A

SyncProviderException

object may or may not contain a description of the
condition causing the exception. The inherited method

getMessage

may be
called to retrieve the description if there is one.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SyncProviderException

()

Creates a new

SyncProviderException

object without a detail message.

SyncProviderException

​(

String

msg)

Constructs a

SyncProviderException

object with the specified
detail message.

SyncProviderException

​(

SyncResolver

syncResolver)

Constructs a

SyncProviderException

object with the specified

SyncResolver

instance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SyncResolver

getSyncResolver

()

Retrieves the

SyncResolver

object that has been set for
this

SyncProviderException

object, or
if none has been set, an instance of the default

SyncResolver

implementation included in the reference implementation.

void

setSyncResolver

​(

SyncResolver

syncResolver)

Sets the

SyncResolver

object for this

SyncProviderException

object to the one supplied.

- Methods declared in class java.sql.

SQLException

getErrorCode

,

getNextException

,

getSQLState

,

iterator

,

setNextException

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

- Methods declared in interface java.lang.

Iterable

forEach

,

spliterator

Constructor Summary

Constructors

Constructor

Description

SyncProviderException

()

Creates a new

SyncProviderException

object without a detail message.

SyncProviderException

​(

String

msg)

Constructs a

SyncProviderException

object with the specified
detail message.

SyncProviderException

​(

SyncResolver

syncResolver)

Constructs a

SyncProviderException

object with the specified

SyncResolver

instance.

---

#### Constructor Summary

Creates a new

SyncProviderException

object without a detail message.

Constructs a

SyncProviderException

object with the specified
detail message.

Constructs a

SyncProviderException

object with the specified

SyncResolver

instance.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SyncResolver

getSyncResolver

()

Retrieves the

SyncResolver

object that has been set for
this

SyncProviderException

object, or
if none has been set, an instance of the default

SyncResolver

implementation included in the reference implementation.

void

setSyncResolver

​(

SyncResolver

syncResolver)

Sets the

SyncResolver

object for this

SyncProviderException

object to the one supplied.

- Methods declared in class java.sql.

SQLException

getErrorCode

,

getNextException

,

getSQLState

,

iterator

,

setNextException

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

- Methods declared in interface java.lang.

Iterable

forEach

,

spliterator

---

#### Method Summary

Retrieves the

SyncResolver

object that has been set for
this

SyncProviderException

object, or
if none has been set, an instance of the default

SyncResolver

implementation included in the reference implementation.

Sets the

SyncResolver

object for this

SyncProviderException

object to the one supplied.

Methods declared in class java.sql.

SQLException

getErrorCode

,

getNextException

,

getSQLState

,

iterator

,

setNextException

---

#### Methods declared in class java.sql. SQLException

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

Methods declared in interface java.lang.

Iterable

forEach

,

spliterator

---

#### Methods declared in interface java.lang. Iterable

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SyncProviderException

```java
public SyncProviderException()
```

Creates a new

SyncProviderException

object without a detail message.

- SyncProviderException

```java
public SyncProviderException​(
String
msg)
```

Constructs a

SyncProviderException

object with the specified
detail message.

**Parameters:** msg

- the detail message

- SyncProviderException

```java
public SyncProviderException​(
SyncResolver
syncResolver)
```

Constructs a

SyncProviderException

object with the specified

SyncResolver

instance.

**Parameters:** syncResolver

- the

SyncResolver

instance used to
to process the synchronization conflicts
**Throws:** IllegalArgumentException

- if the

SyncResolver

object
is

null

.

============ METHOD DETAIL ==========

- Method Detail

- getSyncResolver

```java
public
SyncResolver
getSyncResolver()
```

Retrieves the

SyncResolver

object that has been set for
this

SyncProviderException

object, or
if none has been set, an instance of the default

SyncResolver

implementation included in the reference implementation.

If a

SyncProviderException

object is thrown, an application
may use this method to generate a

SyncResolver

object
with which to resolve the conflict or conflicts that caused the
exception to be thrown.

**Returns:** the

SyncResolver

object set for this

SyncProviderException

object or, if none has
been set, an instance of the default

SyncResolver

implementation. In addition, the default

SyncResolver

implementation is also returned if the

SyncResolver()

or

SyncResolver(String)

constructors are used to instantiate
the

SyncResolver

instance.

- setSyncResolver

```java
public void setSyncResolver​(
SyncResolver
syncResolver)
```

Sets the

SyncResolver

object for this

SyncProviderException

object to the one supplied.
If the argument supplied is

null

, a call to the method

getSyncResolver

will return the default reference
implementation of the

SyncResolver

interface.

**Parameters:** syncResolver

- the

SyncResolver

object to be set;
cannot be

null
**Throws:** IllegalArgumentException

- if the

SyncResolver

object
is

null

.
**See Also:** getSyncResolver()

Constructor Detail

- SyncProviderException

```java
public SyncProviderException()
```

Creates a new

SyncProviderException

object without a detail message.

- SyncProviderException

```java
public SyncProviderException​(
String
msg)
```

Constructs a

SyncProviderException

object with the specified
detail message.

**Parameters:** msg

- the detail message

- SyncProviderException

```java
public SyncProviderException​(
SyncResolver
syncResolver)
```

Constructs a

SyncProviderException

object with the specified

SyncResolver

instance.

**Parameters:** syncResolver

- the

SyncResolver

instance used to
to process the synchronization conflicts
**Throws:** IllegalArgumentException

- if the

SyncResolver

object
is

null

.

---

#### Constructor Detail

SyncProviderException

```java
public SyncProviderException()
```

Creates a new

SyncProviderException

object without a detail message.

---

#### SyncProviderException

public SyncProviderException()

Creates a new

SyncProviderException

object without a detail message.

SyncProviderException

```java
public SyncProviderException​(
String
msg)
```

Constructs a

SyncProviderException

object with the specified
detail message.

**Parameters:** msg

- the detail message

---

#### SyncProviderException

public SyncProviderException​(

String

msg)

Constructs a

SyncProviderException

object with the specified
detail message.

SyncProviderException

```java
public SyncProviderException​(
SyncResolver
syncResolver)
```

Constructs a

SyncProviderException

object with the specified

SyncResolver

instance.

**Parameters:** syncResolver

- the

SyncResolver

instance used to
to process the synchronization conflicts
**Throws:** IllegalArgumentException

- if the

SyncResolver

object
is

null

.

---

#### SyncProviderException

public SyncProviderException​(

SyncResolver

syncResolver)

Constructs a

SyncProviderException

object with the specified

SyncResolver

instance.

Method Detail

- getSyncResolver

```java
public
SyncResolver
getSyncResolver()
```

Retrieves the

SyncResolver

object that has been set for
this

SyncProviderException

object, or
if none has been set, an instance of the default

SyncResolver

implementation included in the reference implementation.

If a

SyncProviderException

object is thrown, an application
may use this method to generate a

SyncResolver

object
with which to resolve the conflict or conflicts that caused the
exception to be thrown.

**Returns:** the

SyncResolver

object set for this

SyncProviderException

object or, if none has
been set, an instance of the default

SyncResolver

implementation. In addition, the default

SyncResolver

implementation is also returned if the

SyncResolver()

or

SyncResolver(String)

constructors are used to instantiate
the

SyncResolver

instance.

- setSyncResolver

```java
public void setSyncResolver​(
SyncResolver
syncResolver)
```

Sets the

SyncResolver

object for this

SyncProviderException

object to the one supplied.
If the argument supplied is

null

, a call to the method

getSyncResolver

will return the default reference
implementation of the

SyncResolver

interface.

**Parameters:** syncResolver

- the

SyncResolver

object to be set;
cannot be

null
**Throws:** IllegalArgumentException

- if the

SyncResolver

object
is

null

.
**See Also:** getSyncResolver()

---

#### Method Detail

getSyncResolver

```java
public
SyncResolver
getSyncResolver()
```

Retrieves the

SyncResolver

object that has been set for
this

SyncProviderException

object, or
if none has been set, an instance of the default

SyncResolver

implementation included in the reference implementation.

If a

SyncProviderException

object is thrown, an application
may use this method to generate a

SyncResolver

object
with which to resolve the conflict or conflicts that caused the
exception to be thrown.

**Returns:** the

SyncResolver

object set for this

SyncProviderException

object or, if none has
been set, an instance of the default

SyncResolver

implementation. In addition, the default

SyncResolver

implementation is also returned if the

SyncResolver()

or

SyncResolver(String)

constructors are used to instantiate
the

SyncResolver

instance.

---

#### getSyncResolver

public

SyncResolver

getSyncResolver()

Retrieves the

SyncResolver

object that has been set for
this

SyncProviderException

object, or
if none has been set, an instance of the default

SyncResolver

implementation included in the reference implementation.

If a

SyncProviderException

object is thrown, an application
may use this method to generate a

SyncResolver

object
with which to resolve the conflict or conflicts that caused the
exception to be thrown.

If a

SyncProviderException

object is thrown, an application
may use this method to generate a

SyncResolver

object
with which to resolve the conflict or conflicts that caused the
exception to be thrown.

setSyncResolver

```java
public void setSyncResolver​(
SyncResolver
syncResolver)
```

Sets the

SyncResolver

object for this

SyncProviderException

object to the one supplied.
If the argument supplied is

null

, a call to the method

getSyncResolver

will return the default reference
implementation of the

SyncResolver

interface.

**Parameters:** syncResolver

- the

SyncResolver

object to be set;
cannot be

null
**Throws:** IllegalArgumentException

- if the

SyncResolver

object
is

null

.
**See Also:** getSyncResolver()

---

#### setSyncResolver

public void setSyncResolver​(

SyncResolver

syncResolver)

Sets the

SyncResolver

object for this

SyncProviderException

object to the one supplied.
If the argument supplied is

null

, a call to the method

getSyncResolver

will return the default reference
implementation of the

SyncResolver

interface.

---

