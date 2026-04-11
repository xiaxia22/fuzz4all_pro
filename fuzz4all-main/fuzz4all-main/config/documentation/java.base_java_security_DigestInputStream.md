# Class DigestInputStream

**Source:** `java.base\java\security\DigestInputStream.html`

### Class Description

```java
public class
DigestInputStream

extends
FilterInputStream
```

A transparent stream that updates the associated message digest using
the bits going through the stream.

To complete the message digest computation, call one of the

digest

methods on the associated message
digest after your calls to one of this digest input stream's

read

methods.

It is possible to turn this stream on or off (see

on

). When it is on, a call to one of the

read

methods
results in an update on the message digest. But when it is off,
the message digest is not updated. The default is for the stream
to be on.

Note that digest objects can compute only one digest (see

MessageDigest

),
so that in order to compute intermediate digests, a caller should
retain a handle onto the digest object, and clone it for each
digest to be computed, leaving the original digest untouched.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

#### protected
MessageDigest
digest

The message digest associated with this stream.

---

### Constructor Details

#### public DigestInputStream​(
InputStream
stream,

MessageDigest
digest)

Creates a digest input stream, using the specified input stream
and message digest.

**Parameters:**
- stream

- the input stream.
- digest

- the message digest to associate with this stream.

---

### Method Details

#### public
MessageDigest
getMessageDigest()

Returns the message digest associated with this stream.

**Returns:**
- the message digest associated with this stream.

**See Also:**
- setMessageDigest(java.security.MessageDigest)

---

#### public void setMessageDigest​(
MessageDigest
digest)

Associates the specified message digest with this stream.

**Parameters:**
- digest

- the message digest to be associated with this stream.

**See Also:**
- getMessageDigest()

---

#### public int read()
throws
IOException

Reads a byte, and updates the message digest (if the digest
function is on). That is, this method reads a byte from the
input stream, blocking until the byte is actually read. If the
digest function is on (see

on

), this method
will then call

update

on the message digest associated
with this stream, passing it the byte read.

**Overrides:**
- read

in class

FilterInputStream

**Returns:**
- the byte read.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- MessageDigest.update(byte)

---

#### public int read​(byte[] b,
int off,
int len)
throws
IOException

Reads into a byte array, and updates the message digest (if the
digest function is on). That is, this method reads up to

len

bytes from the input stream into the array

b

, starting at offset

off

. This method
blocks until the data is actually
read. If the digest function is on (see

on

), this method will then call

update

on the message digest associated with this stream, passing it
the data.

**Overrides:**
- read

in class

FilterInputStream

**Parameters:**
- b

- the array into which the data is read.
- off

- the starting offset into

b

of where the
data should be placed.
- len

- the maximum number of bytes to be read from the input
stream into b, starting at offset

off

.

**Returns:**
- the actual number of bytes read. This is less than

len

if the end of the stream is reached prior to
reading

len

bytes. -1 is returned if no bytes were
read because the end of the stream had already been reached when
the call was made.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- MessageDigest.update(byte[], int, int)

---

#### public void on​(boolean on)

Turns the digest function on or off. The default is on. When
it is on, a call to one of the

read

methods results in an
update on the message digest. But when it is off, the message
digest is not updated.

**Parameters:**
- on

- true to turn the digest function on, false to turn
it off.

---

#### public
String
toString()

Prints a string representation of this digest input stream and
its associated message digest object.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class DigestInputStream

java.lang.Object

- java.io.InputStream
- - java.io.FilterInputStream
- - java.security.DigestInputStream

java.io.InputStream

- java.io.FilterInputStream
- - java.security.DigestInputStream

java.io.FilterInputStream

- java.security.DigestInputStream

java.security.DigestInputStream

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
public class
DigestInputStream

extends
FilterInputStream
```

A transparent stream that updates the associated message digest using
the bits going through the stream.

To complete the message digest computation, call one of the

digest

methods on the associated message
digest after your calls to one of this digest input stream's

read

methods.

It is possible to turn this stream on or off (see

on

). When it is on, a call to one of the

read

methods
results in an update on the message digest. But when it is off,
the message digest is not updated. The default is for the stream
to be on.

Note that digest objects can compute only one digest (see

MessageDigest

),
so that in order to compute intermediate digests, a caller should
retain a handle onto the digest object, and clone it for each
digest to be computed, leaving the original digest untouched.

**Since:** 1.2
**See Also:** MessageDigest

,

DigestOutputStream

public class

DigestInputStream

extends

FilterInputStream

A transparent stream that updates the associated message digest using
the bits going through the stream.

To complete the message digest computation, call one of the

digest

methods on the associated message
digest after your calls to one of this digest input stream's

read

methods.

It is possible to turn this stream on or off (see

on

). When it is on, a call to one of the

read

methods
results in an update on the message digest. But when it is off,
the message digest is not updated. The default is for the stream
to be on.

Note that digest objects can compute only one digest (see

MessageDigest

),
so that in order to compute intermediate digests, a caller should
retain a handle onto the digest object, and clone it for each
digest to be computed, leaving the original digest untouched.

To complete the message digest computation, call one of the

digest

methods on the associated message
digest after your calls to one of this digest input stream's

read

methods.

It is possible to turn this stream on or off (see

on

). When it is on, a call to one of the

read

methods
results in an update on the message digest. But when it is off,
the message digest is not updated. The default is for the stream
to be on.

Note that digest objects can compute only one digest (see

MessageDigest

),
so that in order to compute intermediate digests, a caller should
retain a handle onto the digest object, and clone it for each
digest to be computed, leaving the original digest untouched.

It is possible to turn this stream on or off (see

on

). When it is on, a call to one of the

read

methods
results in an update on the message digest. But when it is off,
the message digest is not updated. The default is for the stream
to be on.

Note that digest objects can compute only one digest (see

MessageDigest

),
so that in order to compute intermediate digests, a caller should
retain a handle onto the digest object, and clone it for each
digest to be computed, leaving the original digest untouched.

Note that digest objects can compute only one digest (see

MessageDigest

),
so that in order to compute intermediate digests, a caller should
retain a handle onto the digest object, and clone it for each
digest to be computed, leaving the original digest untouched.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

MessageDigest

digest

The message digest associated with this stream.

- Fields declared in class java.io.

FilterInputStream

in

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DigestInputStream

​(

InputStream

stream,

MessageDigest

digest)

Creates a digest input stream, using the specified input stream
and message digest.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MessageDigest

getMessageDigest

()

Returns the message digest associated with this stream.

void

on

​(boolean on)

Turns the digest function on or off.

int

read

()

Reads a byte, and updates the message digest (if the digest
function is on).

int

read

​(byte[] b,
int off,
int len)

Reads into a byte array, and updates the message digest (if the
digest function is on).

void

setMessageDigest

​(

MessageDigest

digest)

Associates the specified message digest with this stream.

String

toString

()

Prints a string representation of this digest input stream and
its associated message digest object.

- Methods declared in class java.io.

FilterInputStream

available

,

close

,

mark

,

markSupported

,

read

,

reset

,

skip

- Methods declared in class java.io.

InputStream

nullInputStream

,

readAllBytes

,

readNBytes

,

readNBytes

,

transferTo

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

MessageDigest

digest

The message digest associated with this stream.

- Fields declared in class java.io.

FilterInputStream

in

---

#### Field Summary

The message digest associated with this stream.

Fields declared in class java.io.

FilterInputStream

in

---

#### Fields declared in class java.io. FilterInputStream

Constructor Summary

Constructors

Constructor

Description

DigestInputStream

​(

InputStream

stream,

MessageDigest

digest)

Creates a digest input stream, using the specified input stream
and message digest.

---

#### Constructor Summary

Creates a digest input stream, using the specified input stream
and message digest.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MessageDigest

getMessageDigest

()

Returns the message digest associated with this stream.

void

on

​(boolean on)

Turns the digest function on or off.

int

read

()

Reads a byte, and updates the message digest (if the digest
function is on).

int

read

​(byte[] b,
int off,
int len)

Reads into a byte array, and updates the message digest (if the
digest function is on).

void

setMessageDigest

​(

MessageDigest

digest)

Associates the specified message digest with this stream.

String

toString

()

Prints a string representation of this digest input stream and
its associated message digest object.

- Methods declared in class java.io.

FilterInputStream

available

,

close

,

mark

,

markSupported

,

read

,

reset

,

skip

- Methods declared in class java.io.

InputStream

nullInputStream

,

readAllBytes

,

readNBytes

,

readNBytes

,

transferTo

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

Returns the message digest associated with this stream.

Turns the digest function on or off.

Reads a byte, and updates the message digest (if the digest
function is on).

Reads into a byte array, and updates the message digest (if the
digest function is on).

Associates the specified message digest with this stream.

Prints a string representation of this digest input stream and
its associated message digest object.

Methods declared in class java.io.

FilterInputStream

available

,

close

,

mark

,

markSupported

,

read

,

reset

,

skip

---

#### Methods declared in class java.io. FilterInputStream

Methods declared in class java.io.

InputStream

nullInputStream

,

readAllBytes

,

readNBytes

,

readNBytes

,

transferTo

---

#### Methods declared in class java.io. InputStream

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

============ FIELD DETAIL ===========

- Field Detail

- digest

```java
protected
MessageDigest
digest
```

The message digest associated with this stream.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DigestInputStream

```java
public DigestInputStream​(
InputStream
stream,

MessageDigest
digest)
```

Creates a digest input stream, using the specified input stream
and message digest.

**Parameters:** stream

- the input stream.
**Parameters:** digest

- the message digest to associate with this stream.

============ METHOD DETAIL ==========

- Method Detail

- getMessageDigest

```java
public
MessageDigest
getMessageDigest()
```

Returns the message digest associated with this stream.

**Returns:** the message digest associated with this stream.
**See Also:** setMessageDigest(java.security.MessageDigest)

- setMessageDigest

```java
public void setMessageDigest​(
MessageDigest
digest)
```

Associates the specified message digest with this stream.

**Parameters:** digest

- the message digest to be associated with this stream.
**See Also:** getMessageDigest()

- read

```java
public int read()
throws
IOException
```

Reads a byte, and updates the message digest (if the digest
function is on). That is, this method reads a byte from the
input stream, blocking until the byte is actually read. If the
digest function is on (see

on

), this method
will then call

update

on the message digest associated
with this stream, passing it the byte read.

**Overrides:** read

in class

FilterInputStream
**Returns:** the byte read.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** MessageDigest.update(byte)

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads into a byte array, and updates the message digest (if the
digest function is on). That is, this method reads up to

len

bytes from the input stream into the array

b

, starting at offset

off

. This method
blocks until the data is actually
read. If the digest function is on (see

on

), this method will then call

update

on the message digest associated with this stream, passing it
the data.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the array into which the data is read.
**Parameters:** off

- the starting offset into

b

of where the
data should be placed.
**Parameters:** len

- the maximum number of bytes to be read from the input
stream into b, starting at offset

off

.
**Returns:** the actual number of bytes read. This is less than

len

if the end of the stream is reached prior to
reading

len

bytes. -1 is returned if no bytes were
read because the end of the stream had already been reached when
the call was made.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** MessageDigest.update(byte[], int, int)

- on

```java
public void on​(boolean on)
```

Turns the digest function on or off. The default is on. When
it is on, a call to one of the

read

methods results in an
update on the message digest. But when it is off, the message
digest is not updated.

**Parameters:** on

- true to turn the digest function on, false to turn
it off.

- toString

```java
public
String
toString()
```

Prints a string representation of this digest input stream and
its associated message digest object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Field Detail

- digest

```java
protected
MessageDigest
digest
```

The message digest associated with this stream.

---

#### Field Detail

digest

```java
protected
MessageDigest
digest
```

The message digest associated with this stream.

---

#### digest

protected

MessageDigest

digest

The message digest associated with this stream.

Constructor Detail

- DigestInputStream

```java
public DigestInputStream​(
InputStream
stream,

MessageDigest
digest)
```

Creates a digest input stream, using the specified input stream
and message digest.

**Parameters:** stream

- the input stream.
**Parameters:** digest

- the message digest to associate with this stream.

---

#### Constructor Detail

DigestInputStream

```java
public DigestInputStream​(
InputStream
stream,

MessageDigest
digest)
```

Creates a digest input stream, using the specified input stream
and message digest.

**Parameters:** stream

- the input stream.
**Parameters:** digest

- the message digest to associate with this stream.

---

#### DigestInputStream

public DigestInputStream​(

InputStream

stream,

MessageDigest

digest)

Creates a digest input stream, using the specified input stream
and message digest.

Method Detail

- getMessageDigest

```java
public
MessageDigest
getMessageDigest()
```

Returns the message digest associated with this stream.

**Returns:** the message digest associated with this stream.
**See Also:** setMessageDigest(java.security.MessageDigest)

- setMessageDigest

```java
public void setMessageDigest​(
MessageDigest
digest)
```

Associates the specified message digest with this stream.

**Parameters:** digest

- the message digest to be associated with this stream.
**See Also:** getMessageDigest()

- read

```java
public int read()
throws
IOException
```

Reads a byte, and updates the message digest (if the digest
function is on). That is, this method reads a byte from the
input stream, blocking until the byte is actually read. If the
digest function is on (see

on

), this method
will then call

update

on the message digest associated
with this stream, passing it the byte read.

**Overrides:** read

in class

FilterInputStream
**Returns:** the byte read.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** MessageDigest.update(byte)

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads into a byte array, and updates the message digest (if the
digest function is on). That is, this method reads up to

len

bytes from the input stream into the array

b

, starting at offset

off

. This method
blocks until the data is actually
read. If the digest function is on (see

on

), this method will then call

update

on the message digest associated with this stream, passing it
the data.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the array into which the data is read.
**Parameters:** off

- the starting offset into

b

of where the
data should be placed.
**Parameters:** len

- the maximum number of bytes to be read from the input
stream into b, starting at offset

off

.
**Returns:** the actual number of bytes read. This is less than

len

if the end of the stream is reached prior to
reading

len

bytes. -1 is returned if no bytes were
read because the end of the stream had already been reached when
the call was made.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** MessageDigest.update(byte[], int, int)

- on

```java
public void on​(boolean on)
```

Turns the digest function on or off. The default is on. When
it is on, a call to one of the

read

methods results in an
update on the message digest. But when it is off, the message
digest is not updated.

**Parameters:** on

- true to turn the digest function on, false to turn
it off.

- toString

```java
public
String
toString()
```

Prints a string representation of this digest input stream and
its associated message digest object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getMessageDigest

```java
public
MessageDigest
getMessageDigest()
```

Returns the message digest associated with this stream.

**Returns:** the message digest associated with this stream.
**See Also:** setMessageDigest(java.security.MessageDigest)

---

#### getMessageDigest

public

MessageDigest

getMessageDigest()

Returns the message digest associated with this stream.

setMessageDigest

```java
public void setMessageDigest​(
MessageDigest
digest)
```

Associates the specified message digest with this stream.

**Parameters:** digest

- the message digest to be associated with this stream.
**See Also:** getMessageDigest()

---

#### setMessageDigest

public void setMessageDigest​(

MessageDigest

digest)

Associates the specified message digest with this stream.

read

```java
public int read()
throws
IOException
```

Reads a byte, and updates the message digest (if the digest
function is on). That is, this method reads a byte from the
input stream, blocking until the byte is actually read. If the
digest function is on (see

on

), this method
will then call

update

on the message digest associated
with this stream, passing it the byte read.

**Overrides:** read

in class

FilterInputStream
**Returns:** the byte read.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** MessageDigest.update(byte)

---

#### read

public int read()
throws

IOException

Reads a byte, and updates the message digest (if the digest
function is on). That is, this method reads a byte from the
input stream, blocking until the byte is actually read. If the
digest function is on (see

on

), this method
will then call

update

on the message digest associated
with this stream, passing it the byte read.

read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads into a byte array, and updates the message digest (if the
digest function is on). That is, this method reads up to

len

bytes from the input stream into the array

b

, starting at offset

off

. This method
blocks until the data is actually
read. If the digest function is on (see

on

), this method will then call

update

on the message digest associated with this stream, passing it
the data.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the array into which the data is read.
**Parameters:** off

- the starting offset into

b

of where the
data should be placed.
**Parameters:** len

- the maximum number of bytes to be read from the input
stream into b, starting at offset

off

.
**Returns:** the actual number of bytes read. This is less than

len

if the end of the stream is reached prior to
reading

len

bytes. -1 is returned if no bytes were
read because the end of the stream had already been reached when
the call was made.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** MessageDigest.update(byte[], int, int)

---

#### read

public int read​(byte[] b,
int off,
int len)
throws

IOException

Reads into a byte array, and updates the message digest (if the
digest function is on). That is, this method reads up to

len

bytes from the input stream into the array

b

, starting at offset

off

. This method
blocks until the data is actually
read. If the digest function is on (see

on

), this method will then call

update

on the message digest associated with this stream, passing it
the data.

on

```java
public void on​(boolean on)
```

Turns the digest function on or off. The default is on. When
it is on, a call to one of the

read

methods results in an
update on the message digest. But when it is off, the message
digest is not updated.

**Parameters:** on

- true to turn the digest function on, false to turn
it off.

---

#### on

public void on​(boolean on)

Turns the digest function on or off. The default is on. When
it is on, a call to one of the

read

methods results in an
update on the message digest. But when it is off, the message
digest is not updated.

toString

```java
public
String
toString()
```

Prints a string representation of this digest input stream and
its associated message digest object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Prints a string representation of this digest input stream and
its associated message digest object.

---

