# Class CipherInputStream

**Source:** `java.base\javax\crypto\CipherInputStream.html`

### Class Description

```java
public class
CipherInputStream

extends
FilterInputStream
```

A CipherInputStream is composed of an InputStream and a Cipher so
that read() methods return data that are read in from the
underlying InputStream but have been additionally processed by the
Cipher. The Cipher must be fully initialized before being used by
a CipherInputStream.

For example, if the Cipher is initialized for decryption, the
CipherInputStream will attempt to read in data and decrypt them,
before returning the decrypted data.

This class adheres strictly to the semantics, especially the
failure semantics, of its ancestor classes
java.io.FilterInputStream and java.io.InputStream. This class has
exactly those methods specified in its ancestor classes, and
overrides them all. Moreover, this class catches all exceptions
that are not thrown by its ancestor classes. In particular, the

skip

method skips, and the

available

method counts only data that have been processed by the encapsulated Cipher.
This class may catch BadPaddingException and other exceptions thrown by
failed integrity checks during decryption. These exceptions are not
re-thrown, so the client may not be informed that integrity checks
failed. Because of this behavior, this class may not be suitable
for use with decryption in an authenticated mode of operation (e.g. GCM).
Applications that require authenticated encryption can use the Cipher API
directly as an alternative to using this class.

It is crucial for a programmer using this class not to use
methods that are not defined or overriden in this class (such as a
new method or constructor that is later added to one of the super
classes), because the design and implementation of those methods
are unlikely to have considered security impact with regard to
CipherInputStream.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CipherInputStream​(
InputStream
is,

Cipher
c)

Constructs a CipherInputStream from an InputStream and a
Cipher.

Note: if the specified input stream or cipher is
null, a NullPointerException may be thrown later when
they are used.

**Parameters:**
- is

- the to-be-processed input stream
- c

- an initialized Cipher object

---

#### protected CipherInputStream​(
InputStream
is)

Constructs a CipherInputStream from an InputStream without
specifying a Cipher. This has the effect of constructing a
CipherInputStream using a NullCipher.

Note: if the specified input stream is null, a
NullPointerException may be thrown later when it is used.

**Parameters:**
- is

- the to-be-processed input stream

---

### Method Details

#### public int read()
throws
IOException

Reads the next byte of data from this input stream. The value
byte is returned as an

int

in the range

0

to

255

. If no byte is available
because the end of the stream has been reached, the value

-1

is returned. This method blocks until input data
is available, the end of the stream is detected, or an exception
is thrown.

**Overrides:**
- read

in class

FilterInputStream

**Returns:**
- the next byte of data, or

-1

if the end of the
stream is reached.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterInputStream.in

---

#### public int read​(byte[] b)
throws
IOException

Reads up to

b.length

bytes of data from this input
stream into an array of bytes.

The

read

method of

InputStream

calls
the

read

method of three arguments with the arguments

b

,

0

, and

b.length

.

**Overrides:**
- read

in class

FilterInputStream

**Parameters:**
- b

- the buffer into which the data is read.

**Returns:**
- the total number of bytes read into the buffer, or

-1

is there is no more data because the end of
the stream has been reached.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- InputStream.read(byte[], int, int)

---

#### public int read​(byte[] b,
int off,
int len)
throws
IOException

Reads up to

len

bytes of data from this input stream
into an array of bytes. This method blocks until some input is
available. If the first argument is

null,

up to

len

bytes are read and discarded.

**Overrides:**
- read

in class

FilterInputStream

**Parameters:**
- b

- the buffer into which the data is read.
- off

- the start offset in the destination array

buf
- len

- the maximum number of bytes read.

**Returns:**
- the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- InputStream.read()

---

#### public long skip​(long n)
throws
IOException

Skips

n

bytes of input from the bytes that can be read
from this input stream without blocking.

Fewer bytes than requested might be skipped.
The actual number of bytes skipped is equal to

n

or
the result of a call to

available

,
whichever is smaller.
If

n

is less than zero, no bytes are skipped.

The actual number of bytes skipped is returned.

**Overrides:**
- skip

in class

FilterInputStream

**Parameters:**
- n

- the number of bytes to be skipped.

**Returns:**
- the actual number of bytes skipped.

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public int available()
throws
IOException

Returns the number of bytes that can be read from this input
stream without blocking. The

available

method of

InputStream

returns

0

. This method

should

be overridden by subclasses.

**Overrides:**
- available

in class

FilterInputStream

**Returns:**
- the number of bytes that can be read from this input stream
without blocking.

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public void close()
throws
IOException

Closes this input stream and releases any system resources
associated with the stream.

The

close

method of

CipherInputStream

calls the

close

method of its underlying input
stream.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable

**Overrides:**
- close

in class

FilterInputStream

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterInputStream.in

---

#### public boolean markSupported()

Tests if this input stream supports the

mark

and

reset

methods, which it does not.

**Overrides:**
- markSupported

in class

FilterInputStream

**Returns:**
- false

, since this class does not support the

mark

and

reset

methods.

**See Also:**
- InputStream.mark(int)

,

InputStream.reset()

---

### Additional Sections

#### Class CipherInputStream

java.lang.Object

- java.io.InputStream
- - java.io.FilterInputStream
- - javax.crypto.CipherInputStream

java.io.InputStream

- java.io.FilterInputStream
- - javax.crypto.CipherInputStream

java.io.FilterInputStream

- javax.crypto.CipherInputStream

javax.crypto.CipherInputStream

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
public class
CipherInputStream

extends
FilterInputStream
```

A CipherInputStream is composed of an InputStream and a Cipher so
that read() methods return data that are read in from the
underlying InputStream but have been additionally processed by the
Cipher. The Cipher must be fully initialized before being used by
a CipherInputStream.

For example, if the Cipher is initialized for decryption, the
CipherInputStream will attempt to read in data and decrypt them,
before returning the decrypted data.

This class adheres strictly to the semantics, especially the
failure semantics, of its ancestor classes
java.io.FilterInputStream and java.io.InputStream. This class has
exactly those methods specified in its ancestor classes, and
overrides them all. Moreover, this class catches all exceptions
that are not thrown by its ancestor classes. In particular, the

skip

method skips, and the

available

method counts only data that have been processed by the encapsulated Cipher.
This class may catch BadPaddingException and other exceptions thrown by
failed integrity checks during decryption. These exceptions are not
re-thrown, so the client may not be informed that integrity checks
failed. Because of this behavior, this class may not be suitable
for use with decryption in an authenticated mode of operation (e.g. GCM).
Applications that require authenticated encryption can use the Cipher API
directly as an alternative to using this class.

It is crucial for a programmer using this class not to use
methods that are not defined or overriden in this class (such as a
new method or constructor that is later added to one of the super
classes), because the design and implementation of those methods
are unlikely to have considered security impact with regard to
CipherInputStream.

**Since:** 1.4
**See Also:** InputStream

,

FilterInputStream

,

Cipher

,

CipherOutputStream

public class

CipherInputStream

extends

FilterInputStream

A CipherInputStream is composed of an InputStream and a Cipher so
that read() methods return data that are read in from the
underlying InputStream but have been additionally processed by the
Cipher. The Cipher must be fully initialized before being used by
a CipherInputStream.

For example, if the Cipher is initialized for decryption, the
CipherInputStream will attempt to read in data and decrypt them,
before returning the decrypted data.

This class adheres strictly to the semantics, especially the
failure semantics, of its ancestor classes
java.io.FilterInputStream and java.io.InputStream. This class has
exactly those methods specified in its ancestor classes, and
overrides them all. Moreover, this class catches all exceptions
that are not thrown by its ancestor classes. In particular, the

skip

method skips, and the

available

method counts only data that have been processed by the encapsulated Cipher.
This class may catch BadPaddingException and other exceptions thrown by
failed integrity checks during decryption. These exceptions are not
re-thrown, so the client may not be informed that integrity checks
failed. Because of this behavior, this class may not be suitable
for use with decryption in an authenticated mode of operation (e.g. GCM).
Applications that require authenticated encryption can use the Cipher API
directly as an alternative to using this class.

It is crucial for a programmer using this class not to use
methods that are not defined or overriden in this class (such as a
new method or constructor that is later added to one of the super
classes), because the design and implementation of those methods
are unlikely to have considered security impact with regard to
CipherInputStream.

For example, if the Cipher is initialized for decryption, the
CipherInputStream will attempt to read in data and decrypt them,
before returning the decrypted data.

This class adheres strictly to the semantics, especially the
failure semantics, of its ancestor classes
java.io.FilterInputStream and java.io.InputStream. This class has
exactly those methods specified in its ancestor classes, and
overrides them all. Moreover, this class catches all exceptions
that are not thrown by its ancestor classes. In particular, the

skip

method skips, and the

available

method counts only data that have been processed by the encapsulated Cipher.
This class may catch BadPaddingException and other exceptions thrown by
failed integrity checks during decryption. These exceptions are not
re-thrown, so the client may not be informed that integrity checks
failed. Because of this behavior, this class may not be suitable
for use with decryption in an authenticated mode of operation (e.g. GCM).
Applications that require authenticated encryption can use the Cipher API
directly as an alternative to using this class.

It is crucial for a programmer using this class not to use
methods that are not defined or overriden in this class (such as a
new method or constructor that is later added to one of the super
classes), because the design and implementation of those methods
are unlikely to have considered security impact with regard to
CipherInputStream.

This class adheres strictly to the semantics, especially the
failure semantics, of its ancestor classes
java.io.FilterInputStream and java.io.InputStream. This class has
exactly those methods specified in its ancestor classes, and
overrides them all. Moreover, this class catches all exceptions
that are not thrown by its ancestor classes. In particular, the

skip

method skips, and the

available

method counts only data that have been processed by the encapsulated Cipher.
This class may catch BadPaddingException and other exceptions thrown by
failed integrity checks during decryption. These exceptions are not
re-thrown, so the client may not be informed that integrity checks
failed. Because of this behavior, this class may not be suitable
for use with decryption in an authenticated mode of operation (e.g. GCM).
Applications that require authenticated encryption can use the Cipher API
directly as an alternative to using this class.

It is crucial for a programmer using this class not to use
methods that are not defined or overriden in this class (such as a
new method or constructor that is later added to one of the super
classes), because the design and implementation of those methods
are unlikely to have considered security impact with regard to
CipherInputStream.

It is crucial for a programmer using this class not to use
methods that are not defined or overriden in this class (such as a
new method or constructor that is later added to one of the super
classes), because the design and implementation of those methods
are unlikely to have considered security impact with regard to
CipherInputStream.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.io.

FilterInputStream

in

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CipherInputStream

​(

InputStream

is)

Constructs a CipherInputStream from an InputStream without
specifying a Cipher.

CipherInputStream

​(

InputStream

is,

Cipher

c)

Constructs a CipherInputStream from an InputStream and a
Cipher.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

available

()

Returns the number of bytes that can be read from this input
stream without blocking.

void

close

()

Closes this input stream and releases any system resources
associated with the stream.

boolean

markSupported

()

Tests if this input stream supports the

mark

and

reset

methods, which it does not.

int

read

()

Reads the next byte of data from this input stream.

int

read

​(byte[] b)

Reads up to

b.length

bytes of data from this input
stream into an array of bytes.

int

read

​(byte[] b,
int off,
int len)

Reads up to

len

bytes of data from this input stream
into an array of bytes.

long

skip

​(long n)

Skips

n

bytes of input from the bytes that can be read
from this input stream without blocking.

- Methods declared in class java.io.

FilterInputStream

mark

,

reset

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

toString

,

wait

,

wait

,

wait

Field Summary

- Fields declared in class java.io.

FilterInputStream

in

---

#### Field Summary

Fields declared in class java.io.

FilterInputStream

in

---

#### Fields declared in class java.io. FilterInputStream

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CipherInputStream

​(

InputStream

is)

Constructs a CipherInputStream from an InputStream without
specifying a Cipher.

CipherInputStream

​(

InputStream

is,

Cipher

c)

Constructs a CipherInputStream from an InputStream and a
Cipher.

---

#### Constructor Summary

Constructs a CipherInputStream from an InputStream without
specifying a Cipher.

Constructs a CipherInputStream from an InputStream and a
Cipher.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

available

()

Returns the number of bytes that can be read from this input
stream without blocking.

void

close

()

Closes this input stream and releases any system resources
associated with the stream.

boolean

markSupported

()

Tests if this input stream supports the

mark

and

reset

methods, which it does not.

int

read

()

Reads the next byte of data from this input stream.

int

read

​(byte[] b)

Reads up to

b.length

bytes of data from this input
stream into an array of bytes.

int

read

​(byte[] b,
int off,
int len)

Reads up to

len

bytes of data from this input stream
into an array of bytes.

long

skip

​(long n)

Skips

n

bytes of input from the bytes that can be read
from this input stream without blocking.

- Methods declared in class java.io.

FilterInputStream

mark

,

reset

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the number of bytes that can be read from this input
stream without blocking.

Closes this input stream and releases any system resources
associated with the stream.

Tests if this input stream supports the

mark

and

reset

methods, which it does not.

Reads the next byte of data from this input stream.

Reads up to

b.length

bytes of data from this input
stream into an array of bytes.

Reads up to

len

bytes of data from this input stream
into an array of bytes.

Skips

n

bytes of input from the bytes that can be read
from this input stream without blocking.

Methods declared in class java.io.

FilterInputStream

mark

,

reset

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

toString

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

- CipherInputStream

```java
public CipherInputStream​(
InputStream
is,

Cipher
c)
```

Constructs a CipherInputStream from an InputStream and a
Cipher.

Note: if the specified input stream or cipher is
null, a NullPointerException may be thrown later when
they are used.

**Parameters:** is

- the to-be-processed input stream
**Parameters:** c

- an initialized Cipher object

- CipherInputStream

```java
protected CipherInputStream​(
InputStream
is)
```

Constructs a CipherInputStream from an InputStream without
specifying a Cipher. This has the effect of constructing a
CipherInputStream using a NullCipher.

Note: if the specified input stream is null, a
NullPointerException may be thrown later when it is used.

**Parameters:** is

- the to-be-processed input stream

============ METHOD DETAIL ==========

- Method Detail

- read

```java
public int read()
throws
IOException
```

Reads the next byte of data from this input stream. The value
byte is returned as an

int

in the range

0

to

255

. If no byte is available
because the end of the stream has been reached, the value

-1

is returned. This method blocks until input data
is available, the end of the stream is detected, or an exception
is thrown.

**Overrides:** read

in class

FilterInputStream
**Returns:** the next byte of data, or

-1

if the end of the
stream is reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

- read

```java
public int read​(byte[] b)
throws
IOException
```

Reads up to

b.length

bytes of data from this input
stream into an array of bytes.

The

read

method of

InputStream

calls
the

read

method of three arguments with the arguments

b

,

0

, and

b.length

.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read.
**Returns:** the total number of bytes read into the buffer, or

-1

is there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** InputStream.read(byte[], int, int)

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads up to

len

bytes of data from this input stream
into an array of bytes. This method blocks until some input is
available. If the first argument is

null,

up to

len

bytes are read and discarded.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read.
**Parameters:** off

- the start offset in the destination array

buf
**Parameters:** len

- the maximum number of bytes read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** InputStream.read()

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips

n

bytes of input from the bytes that can be read
from this input stream without blocking.

Fewer bytes than requested might be skipped.
The actual number of bytes skipped is equal to

n

or
the result of a call to

available

,
whichever is smaller.
If

n

is less than zero, no bytes are skipped.

The actual number of bytes skipped is returned.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- the number of bytes to be skipped.
**Returns:** the actual number of bytes skipped.
**Throws:** IOException

- if an I/O error occurs.

- available

```java
public int available()
throws
IOException
```

Returns the number of bytes that can be read from this input
stream without blocking. The

available

method of

InputStream

returns

0

. This method

should

be overridden by subclasses.

**Overrides:** available

in class

FilterInputStream
**Returns:** the number of bytes that can be read from this input stream
without blocking.
**Throws:** IOException

- if an I/O error occurs.

- close

```java
public void close()
throws
IOException
```

Closes this input stream and releases any system resources
associated with the stream.

The

close

method of

CipherInputStream

calls the

close

method of its underlying input
stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterInputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

- markSupported

```java
public boolean markSupported()
```

Tests if this input stream supports the

mark

and

reset

methods, which it does not.

**Overrides:** markSupported

in class

FilterInputStream
**Returns:** false

, since this class does not support the

mark

and

reset

methods.
**See Also:** InputStream.mark(int)

,

InputStream.reset()

Constructor Detail

- CipherInputStream

```java
public CipherInputStream​(
InputStream
is,

Cipher
c)
```

Constructs a CipherInputStream from an InputStream and a
Cipher.

Note: if the specified input stream or cipher is
null, a NullPointerException may be thrown later when
they are used.

**Parameters:** is

- the to-be-processed input stream
**Parameters:** c

- an initialized Cipher object

- CipherInputStream

```java
protected CipherInputStream​(
InputStream
is)
```

Constructs a CipherInputStream from an InputStream without
specifying a Cipher. This has the effect of constructing a
CipherInputStream using a NullCipher.

Note: if the specified input stream is null, a
NullPointerException may be thrown later when it is used.

**Parameters:** is

- the to-be-processed input stream

---

#### Constructor Detail

CipherInputStream

```java
public CipherInputStream​(
InputStream
is,

Cipher
c)
```

Constructs a CipherInputStream from an InputStream and a
Cipher.

Note: if the specified input stream or cipher is
null, a NullPointerException may be thrown later when
they are used.

**Parameters:** is

- the to-be-processed input stream
**Parameters:** c

- an initialized Cipher object

---

#### CipherInputStream

public CipherInputStream​(

InputStream

is,

Cipher

c)

Constructs a CipherInputStream from an InputStream and a
Cipher.

Note: if the specified input stream or cipher is
null, a NullPointerException may be thrown later when
they are used.

CipherInputStream

```java
protected CipherInputStream​(
InputStream
is)
```

Constructs a CipherInputStream from an InputStream without
specifying a Cipher. This has the effect of constructing a
CipherInputStream using a NullCipher.

Note: if the specified input stream is null, a
NullPointerException may be thrown later when it is used.

**Parameters:** is

- the to-be-processed input stream

---

#### CipherInputStream

protected CipherInputStream​(

InputStream

is)

Constructs a CipherInputStream from an InputStream without
specifying a Cipher. This has the effect of constructing a
CipherInputStream using a NullCipher.

Note: if the specified input stream is null, a
NullPointerException may be thrown later when it is used.

Method Detail

- read

```java
public int read()
throws
IOException
```

Reads the next byte of data from this input stream. The value
byte is returned as an

int

in the range

0

to

255

. If no byte is available
because the end of the stream has been reached, the value

-1

is returned. This method blocks until input data
is available, the end of the stream is detected, or an exception
is thrown.

**Overrides:** read

in class

FilterInputStream
**Returns:** the next byte of data, or

-1

if the end of the
stream is reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

- read

```java
public int read​(byte[] b)
throws
IOException
```

Reads up to

b.length

bytes of data from this input
stream into an array of bytes.

The

read

method of

InputStream

calls
the

read

method of three arguments with the arguments

b

,

0

, and

b.length

.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read.
**Returns:** the total number of bytes read into the buffer, or

-1

is there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** InputStream.read(byte[], int, int)

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads up to

len

bytes of data from this input stream
into an array of bytes. This method blocks until some input is
available. If the first argument is

null,

up to

len

bytes are read and discarded.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read.
**Parameters:** off

- the start offset in the destination array

buf
**Parameters:** len

- the maximum number of bytes read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** InputStream.read()

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips

n

bytes of input from the bytes that can be read
from this input stream without blocking.

Fewer bytes than requested might be skipped.
The actual number of bytes skipped is equal to

n

or
the result of a call to

available

,
whichever is smaller.
If

n

is less than zero, no bytes are skipped.

The actual number of bytes skipped is returned.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- the number of bytes to be skipped.
**Returns:** the actual number of bytes skipped.
**Throws:** IOException

- if an I/O error occurs.

- available

```java
public int available()
throws
IOException
```

Returns the number of bytes that can be read from this input
stream without blocking. The

available

method of

InputStream

returns

0

. This method

should

be overridden by subclasses.

**Overrides:** available

in class

FilterInputStream
**Returns:** the number of bytes that can be read from this input stream
without blocking.
**Throws:** IOException

- if an I/O error occurs.

- close

```java
public void close()
throws
IOException
```

Closes this input stream and releases any system resources
associated with the stream.

The

close

method of

CipherInputStream

calls the

close

method of its underlying input
stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterInputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

- markSupported

```java
public boolean markSupported()
```

Tests if this input stream supports the

mark

and

reset

methods, which it does not.

**Overrides:** markSupported

in class

FilterInputStream
**Returns:** false

, since this class does not support the

mark

and

reset

methods.
**See Also:** InputStream.mark(int)

,

InputStream.reset()

---

#### Method Detail

read

```java
public int read()
throws
IOException
```

Reads the next byte of data from this input stream. The value
byte is returned as an

int

in the range

0

to

255

. If no byte is available
because the end of the stream has been reached, the value

-1

is returned. This method blocks until input data
is available, the end of the stream is detected, or an exception
is thrown.

**Overrides:** read

in class

FilterInputStream
**Returns:** the next byte of data, or

-1

if the end of the
stream is reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

---

#### read

public int read()
throws

IOException

Reads the next byte of data from this input stream. The value
byte is returned as an

int

in the range

0

to

255

. If no byte is available
because the end of the stream has been reached, the value

-1

is returned. This method blocks until input data
is available, the end of the stream is detected, or an exception
is thrown.

read

```java
public int read​(byte[] b)
throws
IOException
```

Reads up to

b.length

bytes of data from this input
stream into an array of bytes.

The

read

method of

InputStream

calls
the

read

method of three arguments with the arguments

b

,

0

, and

b.length

.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read.
**Returns:** the total number of bytes read into the buffer, or

-1

is there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** InputStream.read(byte[], int, int)

---

#### read

public int read​(byte[] b)
throws

IOException

Reads up to

b.length

bytes of data from this input
stream into an array of bytes.

The

read

method of

InputStream

calls
the

read

method of three arguments with the arguments

b

,

0

, and

b.length

.

The

read

method of

InputStream

calls
the

read

method of three arguments with the arguments

b

,

0

, and

b.length

.

read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads up to

len

bytes of data from this input stream
into an array of bytes. This method blocks until some input is
available. If the first argument is

null,

up to

len

bytes are read and discarded.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read.
**Parameters:** off

- the start offset in the destination array

buf
**Parameters:** len

- the maximum number of bytes read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** InputStream.read()

---

#### read

public int read​(byte[] b,
int off,
int len)
throws

IOException

Reads up to

len

bytes of data from this input stream
into an array of bytes. This method blocks until some input is
available. If the first argument is

null,

up to

len

bytes are read and discarded.

skip

```java
public long skip​(long n)
throws
IOException
```

Skips

n

bytes of input from the bytes that can be read
from this input stream without blocking.

Fewer bytes than requested might be skipped.
The actual number of bytes skipped is equal to

n

or
the result of a call to

available

,
whichever is smaller.
If

n

is less than zero, no bytes are skipped.

The actual number of bytes skipped is returned.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- the number of bytes to be skipped.
**Returns:** the actual number of bytes skipped.
**Throws:** IOException

- if an I/O error occurs.

---

#### skip

public long skip​(long n)
throws

IOException

Skips

n

bytes of input from the bytes that can be read
from this input stream without blocking.

Fewer bytes than requested might be skipped.
The actual number of bytes skipped is equal to

n

or
the result of a call to

available

,
whichever is smaller.
If

n

is less than zero, no bytes are skipped.

The actual number of bytes skipped is returned.

Fewer bytes than requested might be skipped.
The actual number of bytes skipped is equal to

n

or
the result of a call to

available

,
whichever is smaller.
If

n

is less than zero, no bytes are skipped.

The actual number of bytes skipped is returned.

The actual number of bytes skipped is returned.

available

```java
public int available()
throws
IOException
```

Returns the number of bytes that can be read from this input
stream without blocking. The

available

method of

InputStream

returns

0

. This method

should

be overridden by subclasses.

**Overrides:** available

in class

FilterInputStream
**Returns:** the number of bytes that can be read from this input stream
without blocking.
**Throws:** IOException

- if an I/O error occurs.

---

#### available

public int available()
throws

IOException

Returns the number of bytes that can be read from this input
stream without blocking. The

available

method of

InputStream

returns

0

. This method

should

be overridden by subclasses.

close

```java
public void close()
throws
IOException
```

Closes this input stream and releases any system resources
associated with the stream.

The

close

method of

CipherInputStream

calls the

close

method of its underlying input
stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterInputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

---

#### close

public void close()
throws

IOException

Closes this input stream and releases any system resources
associated with the stream.

The

close

method of

CipherInputStream

calls the

close

method of its underlying input
stream.

The

close

method of

CipherInputStream

calls the

close

method of its underlying input
stream.

markSupported

```java
public boolean markSupported()
```

Tests if this input stream supports the

mark

and

reset

methods, which it does not.

**Overrides:** markSupported

in class

FilterInputStream
**Returns:** false

, since this class does not support the

mark

and

reset

methods.
**See Also:** InputStream.mark(int)

,

InputStream.reset()

---

#### markSupported

public boolean markSupported()

Tests if this input stream supports the

mark

and

reset

methods, which it does not.

---

