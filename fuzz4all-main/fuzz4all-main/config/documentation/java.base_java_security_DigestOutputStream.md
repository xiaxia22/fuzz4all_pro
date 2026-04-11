# Class DigestOutputStream

**Source:** `java.base\java\security\DigestOutputStream.html`

### Class Description

```java
public class
DigestOutputStream

extends
FilterOutputStream
```

A transparent stream that updates the associated message digest using
the bits going through the stream.

To complete the message digest computation, call one of the

digest

methods on the associated message
digest after your calls to one of this digest output stream's

write

methods.

It is possible to turn this stream on or off (see

on

). When it is on, a call to one of the

write

methods results in
an update on the message digest. But when it is off, the message
digest is not updated. The default is for the stream to be on.

**All Implemented Interfaces:** Closeable

,

Flushable

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

#### public DigestOutputStream​(
OutputStream
stream,

MessageDigest
digest)

Creates a digest output stream, using the specified output stream
and message digest.

**Parameters:**
- stream

- the output stream.
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

#### public void write​(int b)
throws
IOException

Updates the message digest (if the digest function is on) using
the specified byte, and in any case writes the byte
to the output stream. That is, if the digest function is on
(see

on

), this method calls

update

on the message digest associated with this
stream, passing it the byte

b

. This method then
writes the byte to the output stream, blocking until the byte
is actually written.

**Overrides:**
- write

in class

FilterOutputStream

**Parameters:**
- b

- the byte to be used for updating and writing to the
output stream.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- MessageDigest.update(byte)

---

#### public void write​(byte[] b,
int off,
int len)
throws
IOException

Updates the message digest (if the digest function is on) using
the specified subarray, and in any case writes the subarray to
the output stream. That is, if the digest function is on (see

on

), this method calls

update

on the message digest associated with this stream, passing it
the subarray specifications. This method then writes the subarray
bytes to the output stream, blocking until the bytes are actually
written.

**Overrides:**
- write

in class

FilterOutputStream

**Parameters:**
- b

- the array containing the subarray to be used for updating
and writing to the output stream.
- off

- the offset into

b

of the first byte to
be updated and written.
- len

- the number of bytes of data to be updated and written
from

b

, starting at offset

off

.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- MessageDigest.update(byte[], int, int)

---

#### public void on​(boolean on)

Turns the digest function on or off. The default is on. When
it is on, a call to one of the

write

methods results in an
update on the message digest. But when it is off, the message
digest is not updated.

**Parameters:**
- on

- true to turn the digest function on, false to turn it
off.

---

#### public
String
toString()

Prints a string representation of this digest output stream and
its associated message digest object.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class DigestOutputStream

java.lang.Object

- java.io.OutputStream
- - java.io.FilterOutputStream
- - java.security.DigestOutputStream

java.io.OutputStream

- java.io.FilterOutputStream
- - java.security.DigestOutputStream

java.io.FilterOutputStream

- java.security.DigestOutputStream

java.security.DigestOutputStream

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

```java
public class
DigestOutputStream

extends
FilterOutputStream
```

A transparent stream that updates the associated message digest using
the bits going through the stream.

To complete the message digest computation, call one of the

digest

methods on the associated message
digest after your calls to one of this digest output stream's

write

methods.

It is possible to turn this stream on or off (see

on

). When it is on, a call to one of the

write

methods results in
an update on the message digest. But when it is off, the message
digest is not updated. The default is for the stream to be on.

**Since:** 1.2
**See Also:** MessageDigest

,

DigestInputStream

public class

DigestOutputStream

extends

FilterOutputStream

A transparent stream that updates the associated message digest using
the bits going through the stream.

To complete the message digest computation, call one of the

digest

methods on the associated message
digest after your calls to one of this digest output stream's

write

methods.

It is possible to turn this stream on or off (see

on

). When it is on, a call to one of the

write

methods results in
an update on the message digest. But when it is off, the message
digest is not updated. The default is for the stream to be on.

To complete the message digest computation, call one of the

digest

methods on the associated message
digest after your calls to one of this digest output stream's

write

methods.

It is possible to turn this stream on or off (see

on

). When it is on, a call to one of the

write

methods results in
an update on the message digest. But when it is off, the message
digest is not updated. The default is for the stream to be on.

It is possible to turn this stream on or off (see

on

). When it is on, a call to one of the

write

methods results in
an update on the message digest. But when it is off, the message
digest is not updated. The default is for the stream to be on.

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

FilterOutputStream

out

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DigestOutputStream

​(

OutputStream

stream,

MessageDigest

digest)

Creates a digest output stream, using the specified output stream
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

void

setMessageDigest

​(

MessageDigest

digest)

Associates the specified message digest with this stream.

String

toString

()

Prints a string representation of this digest output stream and
its associated message digest object.

void

write

​(byte[] b,
int off,
int len)

Updates the message digest (if the digest function is on) using
the specified subarray, and in any case writes the subarray to
the output stream.

void

write

​(int b)

Updates the message digest (if the digest function is on) using
the specified byte, and in any case writes the byte
to the output stream.

- Methods declared in class java.io.

FilterOutputStream

close

,

flush

,

write

- Methods declared in class java.io.

OutputStream

nullOutputStream

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

FilterOutputStream

out

---

#### Field Summary

The message digest associated with this stream.

Fields declared in class java.io.

FilterOutputStream

out

---

#### Fields declared in class java.io. FilterOutputStream

Constructor Summary

Constructors

Constructor

Description

DigestOutputStream

​(

OutputStream

stream,

MessageDigest

digest)

Creates a digest output stream, using the specified output stream
and message digest.

---

#### Constructor Summary

Creates a digest output stream, using the specified output stream
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

void

setMessageDigest

​(

MessageDigest

digest)

Associates the specified message digest with this stream.

String

toString

()

Prints a string representation of this digest output stream and
its associated message digest object.

void

write

​(byte[] b,
int off,
int len)

Updates the message digest (if the digest function is on) using
the specified subarray, and in any case writes the subarray to
the output stream.

void

write

​(int b)

Updates the message digest (if the digest function is on) using
the specified byte, and in any case writes the byte
to the output stream.

- Methods declared in class java.io.

FilterOutputStream

close

,

flush

,

write

- Methods declared in class java.io.

OutputStream

nullOutputStream

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

Associates the specified message digest with this stream.

Prints a string representation of this digest output stream and
its associated message digest object.

Updates the message digest (if the digest function is on) using
the specified subarray, and in any case writes the subarray to
the output stream.

Updates the message digest (if the digest function is on) using
the specified byte, and in any case writes the byte
to the output stream.

Methods declared in class java.io.

FilterOutputStream

close

,

flush

,

write

---

#### Methods declared in class java.io. FilterOutputStream

Methods declared in class java.io.

OutputStream

nullOutputStream

---

#### Methods declared in class java.io. OutputStream

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

- DigestOutputStream

```java
public DigestOutputStream​(
OutputStream
stream,

MessageDigest
digest)
```

Creates a digest output stream, using the specified output stream
and message digest.

**Parameters:** stream

- the output stream.
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

- write

```java
public void write​(int b)
throws
IOException
```

Updates the message digest (if the digest function is on) using
the specified byte, and in any case writes the byte
to the output stream. That is, if the digest function is on
(see

on

), this method calls

update

on the message digest associated with this
stream, passing it the byte

b

. This method then
writes the byte to the output stream, blocking until the byte
is actually written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the byte to be used for updating and writing to the
output stream.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** MessageDigest.update(byte)

- write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Updates the message digest (if the digest function is on) using
the specified subarray, and in any case writes the subarray to
the output stream. That is, if the digest function is on (see

on

), this method calls

update

on the message digest associated with this stream, passing it
the subarray specifications. This method then writes the subarray
bytes to the output stream, blocking until the bytes are actually
written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the array containing the subarray to be used for updating
and writing to the output stream.
**Parameters:** off

- the offset into

b

of the first byte to
be updated and written.
**Parameters:** len

- the number of bytes of data to be updated and written
from

b

, starting at offset

off

.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** MessageDigest.update(byte[], int, int)

- on

```java
public void on​(boolean on)
```

Turns the digest function on or off. The default is on. When
it is on, a call to one of the

write

methods results in an
update on the message digest. But when it is off, the message
digest is not updated.

**Parameters:** on

- true to turn the digest function on, false to turn it
off.

- toString

```java
public
String
toString()
```

Prints a string representation of this digest output stream and
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

- DigestOutputStream

```java
public DigestOutputStream​(
OutputStream
stream,

MessageDigest
digest)
```

Creates a digest output stream, using the specified output stream
and message digest.

**Parameters:** stream

- the output stream.
**Parameters:** digest

- the message digest to associate with this stream.

---

#### Constructor Detail

DigestOutputStream

```java
public DigestOutputStream​(
OutputStream
stream,

MessageDigest
digest)
```

Creates a digest output stream, using the specified output stream
and message digest.

**Parameters:** stream

- the output stream.
**Parameters:** digest

- the message digest to associate with this stream.

---

#### DigestOutputStream

public DigestOutputStream​(

OutputStream

stream,

MessageDigest

digest)

Creates a digest output stream, using the specified output stream
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

- write

```java
public void write​(int b)
throws
IOException
```

Updates the message digest (if the digest function is on) using
the specified byte, and in any case writes the byte
to the output stream. That is, if the digest function is on
(see

on

), this method calls

update

on the message digest associated with this
stream, passing it the byte

b

. This method then
writes the byte to the output stream, blocking until the byte
is actually written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the byte to be used for updating and writing to the
output stream.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** MessageDigest.update(byte)

- write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Updates the message digest (if the digest function is on) using
the specified subarray, and in any case writes the subarray to
the output stream. That is, if the digest function is on (see

on

), this method calls

update

on the message digest associated with this stream, passing it
the subarray specifications. This method then writes the subarray
bytes to the output stream, blocking until the bytes are actually
written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the array containing the subarray to be used for updating
and writing to the output stream.
**Parameters:** off

- the offset into

b

of the first byte to
be updated and written.
**Parameters:** len

- the number of bytes of data to be updated and written
from

b

, starting at offset

off

.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** MessageDigest.update(byte[], int, int)

- on

```java
public void on​(boolean on)
```

Turns the digest function on or off. The default is on. When
it is on, a call to one of the

write

methods results in an
update on the message digest. But when it is off, the message
digest is not updated.

**Parameters:** on

- true to turn the digest function on, false to turn it
off.

- toString

```java
public
String
toString()
```

Prints a string representation of this digest output stream and
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

write

```java
public void write​(int b)
throws
IOException
```

Updates the message digest (if the digest function is on) using
the specified byte, and in any case writes the byte
to the output stream. That is, if the digest function is on
(see

on

), this method calls

update

on the message digest associated with this
stream, passing it the byte

b

. This method then
writes the byte to the output stream, blocking until the byte
is actually written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the byte to be used for updating and writing to the
output stream.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** MessageDigest.update(byte)

---

#### write

public void write​(int b)
throws

IOException

Updates the message digest (if the digest function is on) using
the specified byte, and in any case writes the byte
to the output stream. That is, if the digest function is on
(see

on

), this method calls

update

on the message digest associated with this
stream, passing it the byte

b

. This method then
writes the byte to the output stream, blocking until the byte
is actually written.

write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Updates the message digest (if the digest function is on) using
the specified subarray, and in any case writes the subarray to
the output stream. That is, if the digest function is on (see

on

), this method calls

update

on the message digest associated with this stream, passing it
the subarray specifications. This method then writes the subarray
bytes to the output stream, blocking until the bytes are actually
written.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the array containing the subarray to be used for updating
and writing to the output stream.
**Parameters:** off

- the offset into

b

of the first byte to
be updated and written.
**Parameters:** len

- the number of bytes of data to be updated and written
from

b

, starting at offset

off

.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** MessageDigest.update(byte[], int, int)

---

#### write

public void write​(byte[] b,
int off,
int len)
throws

IOException

Updates the message digest (if the digest function is on) using
the specified subarray, and in any case writes the subarray to
the output stream. That is, if the digest function is on (see

on

), this method calls

update

on the message digest associated with this stream, passing it
the subarray specifications. This method then writes the subarray
bytes to the output stream, blocking until the bytes are actually
written.

on

```java
public void on​(boolean on)
```

Turns the digest function on or off. The default is on. When
it is on, a call to one of the

write

methods results in an
update on the message digest. But when it is off, the message
digest is not updated.

**Parameters:** on

- true to turn the digest function on, false to turn it
off.

---

#### on

public void on​(boolean on)

Turns the digest function on or off. The default is on. When
it is on, a call to one of the

write

methods results in an
update on the message digest. But when it is off, the message
digest is not updated.

toString

```java
public
String
toString()
```

Prints a string representation of this digest output stream and
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

Prints a string representation of this digest output stream and
its associated message digest object.

---

