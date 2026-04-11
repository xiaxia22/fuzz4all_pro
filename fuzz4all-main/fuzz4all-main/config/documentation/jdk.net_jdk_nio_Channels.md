# Class Channels

**Source:** `jdk.net\jdk\nio\Channels.html`

### Class Description

```java
public final class
Channels

extends
Object
```

Defines static methods to create

channels

.

Unless otherwise specified, passing a

null

argument to any of the
methods defined here will cause a

NullPointerException

to be thrown.

**Since:** 11

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
SelectableChannel
readWriteSelectableChannel​(
FileDescriptor
fd,

Channels.SelectableChannelCloser
closer)

Creates a selectable channel to a file descriptor that supports an

operation-set

of

OP_READ

and

OP_WRITE

. The selectable channel will be
created by the default

SelectorProvider

.

The given file descriptor is a socket or resource that can be
multiplexed by a

Selector

for read and write
readiness. Great care is required to coordinate direct use of the file
descriptor with the use of the selectable channel. In particular,
changing the blocking mode or closing the file descriptor without careful
coordination will result in unspecified and unsafe side effects. The
given

SelectableChannelCloser

is invoked to
close the file descriptor and to coordinate the closing when the channel
is registered with a

Selector

.

If there is a security manager set then its

checkRead

and

checkWrite

methods
are invoked to check that the caller has permission to both read from and
write to the file descriptor.

**Parameters:**
- fd

- The file descriptor
- closer

- The object to close the channel

**Returns:**
- The selectable channel

**Throws:**
- IllegalArgumentException

- If the file descriptor is not

valid
- SecurityException

- If denied by the security manager

**Implementation Note:**
- This method throws

UnsupportedOperationException

if
the default

SelectorProvider

is not the JDK built-in implementation.

---

### Additional Sections

#### Class Channels

java.lang.Object

- jdk.nio.Channels

jdk.nio.Channels

```java
public final class
Channels

extends
Object
```

Defines static methods to create

channels

.

Unless otherwise specified, passing a

null

argument to any of the
methods defined here will cause a

NullPointerException

to be thrown.

**Since:** 11

public final class

Channels

extends

Object

Defines static methods to create

channels

.

Unless otherwise specified, passing a

null

argument to any of the
methods defined here will cause a

NullPointerException

to be thrown.

Unless otherwise specified, passing a

null

argument to any of the
methods defined here will cause a

NullPointerException

to be thrown.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static interface

Channels.SelectableChannelCloser

An object used to coordinate the closing of a selectable channel created
by

readWriteSelectableChannel

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

SelectableChannel

readWriteSelectableChannel

​(

FileDescriptor

fd,

Channels.SelectableChannelCloser

closer)

Creates a selectable channel to a file descriptor that supports an

operation-set

of

OP_READ

and

OP_WRITE

.

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

toString

,

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static interface

Channels.SelectableChannelCloser

An object used to coordinate the closing of a selectable channel created
by

readWriteSelectableChannel

.

---

#### Nested Class Summary

An object used to coordinate the closing of a selectable channel created
by

readWriteSelectableChannel

.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

SelectableChannel

readWriteSelectableChannel

​(

FileDescriptor

fd,

Channels.SelectableChannelCloser

closer)

Creates a selectable channel to a file descriptor that supports an

operation-set

of

OP_READ

and

OP_WRITE

.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Creates a selectable channel to a file descriptor that supports an

operation-set

of

OP_READ

and

OP_WRITE

.

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

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ METHOD DETAIL ==========

- Method Detail

- readWriteSelectableChannel

```java
public static
SelectableChannel
readWriteSelectableChannel​(
FileDescriptor
fd,

Channels.SelectableChannelCloser
closer)
```

Creates a selectable channel to a file descriptor that supports an

operation-set

of

OP_READ

and

OP_WRITE

. The selectable channel will be
created by the default

SelectorProvider

.

The given file descriptor is a socket or resource that can be
multiplexed by a

Selector

for read and write
readiness. Great care is required to coordinate direct use of the file
descriptor with the use of the selectable channel. In particular,
changing the blocking mode or closing the file descriptor without careful
coordination will result in unspecified and unsafe side effects. The
given

SelectableChannelCloser

is invoked to
close the file descriptor and to coordinate the closing when the channel
is registered with a

Selector

.

If there is a security manager set then its

checkRead

and

checkWrite

methods
are invoked to check that the caller has permission to both read from and
write to the file descriptor.

**Implementation Note:** This method throws

UnsupportedOperationException

if
the default

SelectorProvider

is not the JDK built-in implementation.
**Parameters:** fd

- The file descriptor
**Parameters:** closer

- The object to close the channel
**Returns:** The selectable channel
**Throws:** IllegalArgumentException

- If the file descriptor is not

valid
**Throws:** SecurityException

- If denied by the security manager

Method Detail

- readWriteSelectableChannel

```java
public static
SelectableChannel
readWriteSelectableChannel​(
FileDescriptor
fd,

Channels.SelectableChannelCloser
closer)
```

Creates a selectable channel to a file descriptor that supports an

operation-set

of

OP_READ

and

OP_WRITE

. The selectable channel will be
created by the default

SelectorProvider

.

The given file descriptor is a socket or resource that can be
multiplexed by a

Selector

for read and write
readiness. Great care is required to coordinate direct use of the file
descriptor with the use of the selectable channel. In particular,
changing the blocking mode or closing the file descriptor without careful
coordination will result in unspecified and unsafe side effects. The
given

SelectableChannelCloser

is invoked to
close the file descriptor and to coordinate the closing when the channel
is registered with a

Selector

.

If there is a security manager set then its

checkRead

and

checkWrite

methods
are invoked to check that the caller has permission to both read from and
write to the file descriptor.

**Implementation Note:** This method throws

UnsupportedOperationException

if
the default

SelectorProvider

is not the JDK built-in implementation.
**Parameters:** fd

- The file descriptor
**Parameters:** closer

- The object to close the channel
**Returns:** The selectable channel
**Throws:** IllegalArgumentException

- If the file descriptor is not

valid
**Throws:** SecurityException

- If denied by the security manager

---

#### Method Detail

readWriteSelectableChannel

```java
public static
SelectableChannel
readWriteSelectableChannel​(
FileDescriptor
fd,

Channels.SelectableChannelCloser
closer)
```

Creates a selectable channel to a file descriptor that supports an

operation-set

of

OP_READ

and

OP_WRITE

. The selectable channel will be
created by the default

SelectorProvider

.

The given file descriptor is a socket or resource that can be
multiplexed by a

Selector

for read and write
readiness. Great care is required to coordinate direct use of the file
descriptor with the use of the selectable channel. In particular,
changing the blocking mode or closing the file descriptor without careful
coordination will result in unspecified and unsafe side effects. The
given

SelectableChannelCloser

is invoked to
close the file descriptor and to coordinate the closing when the channel
is registered with a

Selector

.

If there is a security manager set then its

checkRead

and

checkWrite

methods
are invoked to check that the caller has permission to both read from and
write to the file descriptor.

**Implementation Note:** This method throws

UnsupportedOperationException

if
the default

SelectorProvider

is not the JDK built-in implementation.
**Parameters:** fd

- The file descriptor
**Parameters:** closer

- The object to close the channel
**Returns:** The selectable channel
**Throws:** IllegalArgumentException

- If the file descriptor is not

valid
**Throws:** SecurityException

- If denied by the security manager

---

#### readWriteSelectableChannel

public static

SelectableChannel

readWriteSelectableChannel​(

FileDescriptor

fd,

Channels.SelectableChannelCloser

closer)

Creates a selectable channel to a file descriptor that supports an

operation-set

of

OP_READ

and

OP_WRITE

. The selectable channel will be
created by the default

SelectorProvider

.

The given file descriptor is a socket or resource that can be
multiplexed by a

Selector

for read and write
readiness. Great care is required to coordinate direct use of the file
descriptor with the use of the selectable channel. In particular,
changing the blocking mode or closing the file descriptor without careful
coordination will result in unspecified and unsafe side effects. The
given

SelectableChannelCloser

is invoked to
close the file descriptor and to coordinate the closing when the channel
is registered with a

Selector

.

If there is a security manager set then its

checkRead

and

checkWrite

methods
are invoked to check that the caller has permission to both read from and
write to the file descriptor.

The given file descriptor is a socket or resource that can be
multiplexed by a

Selector

for read and write
readiness. Great care is required to coordinate direct use of the file
descriptor with the use of the selectable channel. In particular,
changing the blocking mode or closing the file descriptor without careful
coordination will result in unspecified and unsafe side effects. The
given

SelectableChannelCloser

is invoked to
close the file descriptor and to coordinate the closing when the channel
is registered with a

Selector

.

If there is a security manager set then its

checkRead

and

checkWrite

methods
are invoked to check that the caller has permission to both read from and
write to the file descriptor.

---

