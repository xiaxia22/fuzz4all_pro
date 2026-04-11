# Class CipherOutputStream

**Source:** `java.base\javax\crypto\CipherOutputStream.html`

### Class Description

```java
public class
CipherOutputStream

extends
FilterOutputStream
```

A CipherOutputStream is composed of an OutputStream and a Cipher so
that write() methods first process the data before writing them out
to the underlying OutputStream. The cipher must be fully
initialized before being used by a CipherOutputStream.

For example, if the cipher is initialized for encryption, the
CipherOutputStream will attempt to encrypt data before writing out the
encrypted data.

This class adheres strictly to the semantics, especially the
failure semantics, of its ancestor classes
java.io.OutputStream and java.io.FilterOutputStream. This class
has exactly those methods specified in its ancestor classes, and
overrides them all. Moreover, this class catches all exceptions
that are not thrown by its ancestor classes. In particular, this
class catches BadPaddingException and other exceptions thrown by
failed integrity checks during decryption. These exceptions are not
re-thrown, so the client will not be informed that integrity checks
failed. Because of this behavior, this class may not be suitable
for use with decryption in an authenticated mode of operation (e.g. GCM)
if the application requires explicit notification when authentication
fails. Such an application can use the Cipher API directly as an
alternative to using this class.

It is crucial for a programmer using this class not to use
methods that are not defined or overriden in this class (such as a
new method or constructor that is later added to one of the super
classes), because the design and implementation of those methods
are unlikely to have considered security impact with regard to
CipherOutputStream.

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CipherOutputStream​(
OutputStream
os,

Cipher
c)

Constructs a CipherOutputStream from an OutputStream and a
Cipher.

Note: if the specified output stream or cipher is
null, a NullPointerException may be thrown later when
they are used.

**Parameters:**
- os

- the OutputStream object
- c

- an initialized Cipher object

---

#### protected CipherOutputStream​(
OutputStream
os)

Constructs a CipherOutputStream from an OutputStream without
specifying a Cipher. This has the effect of constructing a
CipherOutputStream using a NullCipher.

Note: if the specified output stream is null, a
NullPointerException may be thrown later when it is used.

**Parameters:**
- os

- the OutputStream object

---

### Method Details

#### public void write​(int b)
throws
IOException

Writes the specified byte to this output stream.

**Overrides:**
- write

in class

FilterOutputStream

**Parameters:**
- b

- the

byte

.

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public void write​(byte[] b)
throws
IOException

Writes

b.length

bytes from the specified byte array
to this output stream.

The

write

method of

CipherOutputStream

calls the

write

method of three arguments with the three arguments

b

,

0

, and

b.length

.

**Overrides:**
- write

in class

FilterOutputStream

**Parameters:**
- b

- the data.

**Throws:**
- NullPointerException

- if

b

is null.
- IOException

- if an I/O error occurs.

**See Also:**
- write(byte[], int, int)

---

#### public void write​(byte[] b,
int off,
int len)
throws
IOException

Writes

len

bytes from the specified byte array
starting at offset

off

to this output stream.

**Overrides:**
- write

in class

FilterOutputStream

**Parameters:**
- b

- the data.
- off

- the start offset in the data.
- len

- the number of bytes to write.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.write(int)

---

#### public void flush()
throws
IOException

Flushes this output stream by forcing any buffered output bytes
that have already been processed by the encapsulated cipher object
to be written out.

Any bytes buffered by the encapsulated cipher
and waiting to be processed by it will not be written out. For example,
if the encapsulated cipher is a block cipher, and the total number of
bytes written using one of the

write

methods is less than
the cipher's block size, no bytes will be written out.

**Specified by:**
- flush

in interface

Flushable

**Overrides:**
- flush

in class

FilterOutputStream

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.out

---

#### public void close()
throws
IOException

Closes this output stream and releases any system resources
associated with this stream.

This method invokes the

doFinal

method of the encapsulated
cipher object, which causes any bytes buffered by the encapsulated
cipher to be processed. The result is written out by calling the

flush

method of this output stream.

This method resets the encapsulated cipher object to its initial state
and calls the

close

method of the underlying output
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

FilterOutputStream

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.flush()

,

FilterOutputStream.out

---

### Additional Sections

#### Class CipherOutputStream

java.lang.Object

- java.io.OutputStream
- - java.io.FilterOutputStream
- - javax.crypto.CipherOutputStream

java.io.OutputStream

- java.io.FilterOutputStream
- - javax.crypto.CipherOutputStream

java.io.FilterOutputStream

- javax.crypto.CipherOutputStream

javax.crypto.CipherOutputStream

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

```java
public class
CipherOutputStream

extends
FilterOutputStream
```

A CipherOutputStream is composed of an OutputStream and a Cipher so
that write() methods first process the data before writing them out
to the underlying OutputStream. The cipher must be fully
initialized before being used by a CipherOutputStream.

For example, if the cipher is initialized for encryption, the
CipherOutputStream will attempt to encrypt data before writing out the
encrypted data.

This class adheres strictly to the semantics, especially the
failure semantics, of its ancestor classes
java.io.OutputStream and java.io.FilterOutputStream. This class
has exactly those methods specified in its ancestor classes, and
overrides them all. Moreover, this class catches all exceptions
that are not thrown by its ancestor classes. In particular, this
class catches BadPaddingException and other exceptions thrown by
failed integrity checks during decryption. These exceptions are not
re-thrown, so the client will not be informed that integrity checks
failed. Because of this behavior, this class may not be suitable
for use with decryption in an authenticated mode of operation (e.g. GCM)
if the application requires explicit notification when authentication
fails. Such an application can use the Cipher API directly as an
alternative to using this class.

It is crucial for a programmer using this class not to use
methods that are not defined or overriden in this class (such as a
new method or constructor that is later added to one of the super
classes), because the design and implementation of those methods
are unlikely to have considered security impact with regard to
CipherOutputStream.

**Since:** 1.4
**See Also:** OutputStream

,

FilterOutputStream

,

Cipher

,

CipherInputStream

public class

CipherOutputStream

extends

FilterOutputStream

A CipherOutputStream is composed of an OutputStream and a Cipher so
that write() methods first process the data before writing them out
to the underlying OutputStream. The cipher must be fully
initialized before being used by a CipherOutputStream.

For example, if the cipher is initialized for encryption, the
CipherOutputStream will attempt to encrypt data before writing out the
encrypted data.

This class adheres strictly to the semantics, especially the
failure semantics, of its ancestor classes
java.io.OutputStream and java.io.FilterOutputStream. This class
has exactly those methods specified in its ancestor classes, and
overrides them all. Moreover, this class catches all exceptions
that are not thrown by its ancestor classes. In particular, this
class catches BadPaddingException and other exceptions thrown by
failed integrity checks during decryption. These exceptions are not
re-thrown, so the client will not be informed that integrity checks
failed. Because of this behavior, this class may not be suitable
for use with decryption in an authenticated mode of operation (e.g. GCM)
if the application requires explicit notification when authentication
fails. Such an application can use the Cipher API directly as an
alternative to using this class.

It is crucial for a programmer using this class not to use
methods that are not defined or overriden in this class (such as a
new method or constructor that is later added to one of the super
classes), because the design and implementation of those methods
are unlikely to have considered security impact with regard to
CipherOutputStream.

For example, if the cipher is initialized for encryption, the
CipherOutputStream will attempt to encrypt data before writing out the
encrypted data.

This class adheres strictly to the semantics, especially the
failure semantics, of its ancestor classes
java.io.OutputStream and java.io.FilterOutputStream. This class
has exactly those methods specified in its ancestor classes, and
overrides them all. Moreover, this class catches all exceptions
that are not thrown by its ancestor classes. In particular, this
class catches BadPaddingException and other exceptions thrown by
failed integrity checks during decryption. These exceptions are not
re-thrown, so the client will not be informed that integrity checks
failed. Because of this behavior, this class may not be suitable
for use with decryption in an authenticated mode of operation (e.g. GCM)
if the application requires explicit notification when authentication
fails. Such an application can use the Cipher API directly as an
alternative to using this class.

It is crucial for a programmer using this class not to use
methods that are not defined or overriden in this class (such as a
new method or constructor that is later added to one of the super
classes), because the design and implementation of those methods
are unlikely to have considered security impact with regard to
CipherOutputStream.

This class adheres strictly to the semantics, especially the
failure semantics, of its ancestor classes
java.io.OutputStream and java.io.FilterOutputStream. This class
has exactly those methods specified in its ancestor classes, and
overrides them all. Moreover, this class catches all exceptions
that are not thrown by its ancestor classes. In particular, this
class catches BadPaddingException and other exceptions thrown by
failed integrity checks during decryption. These exceptions are not
re-thrown, so the client will not be informed that integrity checks
failed. Because of this behavior, this class may not be suitable
for use with decryption in an authenticated mode of operation (e.g. GCM)
if the application requires explicit notification when authentication
fails. Such an application can use the Cipher API directly as an
alternative to using this class.

It is crucial for a programmer using this class not to use
methods that are not defined or overriden in this class (such as a
new method or constructor that is later added to one of the super
classes), because the design and implementation of those methods
are unlikely to have considered security impact with regard to
CipherOutputStream.

It is crucial for a programmer using this class not to use
methods that are not defined or overriden in this class (such as a
new method or constructor that is later added to one of the super
classes), because the design and implementation of those methods
are unlikely to have considered security impact with regard to
CipherOutputStream.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.io.

FilterOutputStream

out

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CipherOutputStream

​(

OutputStream

os)

Constructs a CipherOutputStream from an OutputStream without
specifying a Cipher.

CipherOutputStream

​(

OutputStream

os,

Cipher

c)

Constructs a CipherOutputStream from an OutputStream and a
Cipher.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Closes this output stream and releases any system resources
associated with this stream.

void

flush

()

Flushes this output stream by forcing any buffered output bytes
that have already been processed by the encapsulated cipher object
to be written out.

void

write

​(byte[] b)

Writes

b.length

bytes from the specified byte array
to this output stream.

void

write

​(byte[] b,
int off,
int len)

Writes

len

bytes from the specified byte array
starting at offset

off

to this output stream.

void

write

​(int b)

Writes the specified byte to this output stream.

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

toString

,

wait

,

wait

,

wait

Field Summary

- Fields declared in class java.io.

FilterOutputStream

out

---

#### Field Summary

Fields declared in class java.io.

FilterOutputStream

out

---

#### Fields declared in class java.io. FilterOutputStream

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CipherOutputStream

​(

OutputStream

os)

Constructs a CipherOutputStream from an OutputStream without
specifying a Cipher.

CipherOutputStream

​(

OutputStream

os,

Cipher

c)

Constructs a CipherOutputStream from an OutputStream and a
Cipher.

---

#### Constructor Summary

Constructs a CipherOutputStream from an OutputStream without
specifying a Cipher.

Constructs a CipherOutputStream from an OutputStream and a
Cipher.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Closes this output stream and releases any system resources
associated with this stream.

void

flush

()

Flushes this output stream by forcing any buffered output bytes
that have already been processed by the encapsulated cipher object
to be written out.

void

write

​(byte[] b)

Writes

b.length

bytes from the specified byte array
to this output stream.

void

write

​(byte[] b,
int off,
int len)

Writes

len

bytes from the specified byte array
starting at offset

off

to this output stream.

void

write

​(int b)

Writes the specified byte to this output stream.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Closes this output stream and releases any system resources
associated with this stream.

Flushes this output stream by forcing any buffered output bytes
that have already been processed by the encapsulated cipher object
to be written out.

Writes

b.length

bytes from the specified byte array
to this output stream.

Writes

len

bytes from the specified byte array
starting at offset

off

to this output stream.

Writes the specified byte to this output stream.

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

- CipherOutputStream

```java
public CipherOutputStream​(
OutputStream
os,

Cipher
c)
```

Constructs a CipherOutputStream from an OutputStream and a
Cipher.

Note: if the specified output stream or cipher is
null, a NullPointerException may be thrown later when
they are used.

**Parameters:** os

- the OutputStream object
**Parameters:** c

- an initialized Cipher object

- CipherOutputStream

```java
protected CipherOutputStream​(
OutputStream
os)
```

Constructs a CipherOutputStream from an OutputStream without
specifying a Cipher. This has the effect of constructing a
CipherOutputStream using a NullCipher.

Note: if the specified output stream is null, a
NullPointerException may be thrown later when it is used.

**Parameters:** os

- the OutputStream object

============ METHOD DETAIL ==========

- Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes the specified byte to this output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the

byte

.
**Throws:** IOException

- if an I/O error occurs.

- write

```java
public void write​(byte[] b)
throws
IOException
```

Writes

b.length

bytes from the specified byte array
to this output stream.

The

write

method of

CipherOutputStream

calls the

write

method of three arguments with the three arguments

b

,

0

, and

b.length

.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data.
**Throws:** NullPointerException

- if

b

is null.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** write(byte[], int, int)

- write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes

len

bytes from the specified byte array
starting at offset

off

to this output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.write(int)

- flush

```java
public void flush()
throws
IOException
```

Flushes this output stream by forcing any buffered output bytes
that have already been processed by the encapsulated cipher object
to be written out.

Any bytes buffered by the encapsulated cipher
and waiting to be processed by it will not be written out. For example,
if the encapsulated cipher is a block cipher, and the total number of
bytes written using one of the

write

methods is less than
the cipher's block size, no bytes will be written out.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- close

```java
public void close()
throws
IOException
```

Closes this output stream and releases any system resources
associated with this stream.

This method invokes the

doFinal

method of the encapsulated
cipher object, which causes any bytes buffered by the encapsulated
cipher to be processed. The result is written out by calling the

flush

method of this output stream.

This method resets the encapsulated cipher object to its initial state
and calls the

close

method of the underlying output
stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.flush()

,

FilterOutputStream.out

Constructor Detail

- CipherOutputStream

```java
public CipherOutputStream​(
OutputStream
os,

Cipher
c)
```

Constructs a CipherOutputStream from an OutputStream and a
Cipher.

Note: if the specified output stream or cipher is
null, a NullPointerException may be thrown later when
they are used.

**Parameters:** os

- the OutputStream object
**Parameters:** c

- an initialized Cipher object

- CipherOutputStream

```java
protected CipherOutputStream​(
OutputStream
os)
```

Constructs a CipherOutputStream from an OutputStream without
specifying a Cipher. This has the effect of constructing a
CipherOutputStream using a NullCipher.

Note: if the specified output stream is null, a
NullPointerException may be thrown later when it is used.

**Parameters:** os

- the OutputStream object

---

#### Constructor Detail

CipherOutputStream

```java
public CipherOutputStream​(
OutputStream
os,

Cipher
c)
```

Constructs a CipherOutputStream from an OutputStream and a
Cipher.

Note: if the specified output stream or cipher is
null, a NullPointerException may be thrown later when
they are used.

**Parameters:** os

- the OutputStream object
**Parameters:** c

- an initialized Cipher object

---

#### CipherOutputStream

public CipherOutputStream​(

OutputStream

os,

Cipher

c)

Constructs a CipherOutputStream from an OutputStream and a
Cipher.

Note: if the specified output stream or cipher is
null, a NullPointerException may be thrown later when
they are used.

CipherOutputStream

```java
protected CipherOutputStream​(
OutputStream
os)
```

Constructs a CipherOutputStream from an OutputStream without
specifying a Cipher. This has the effect of constructing a
CipherOutputStream using a NullCipher.

Note: if the specified output stream is null, a
NullPointerException may be thrown later when it is used.

**Parameters:** os

- the OutputStream object

---

#### CipherOutputStream

protected CipherOutputStream​(

OutputStream

os)

Constructs a CipherOutputStream from an OutputStream without
specifying a Cipher. This has the effect of constructing a
CipherOutputStream using a NullCipher.

Note: if the specified output stream is null, a
NullPointerException may be thrown later when it is used.

Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes the specified byte to this output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the

byte

.
**Throws:** IOException

- if an I/O error occurs.

- write

```java
public void write​(byte[] b)
throws
IOException
```

Writes

b.length

bytes from the specified byte array
to this output stream.

The

write

method of

CipherOutputStream

calls the

write

method of three arguments with the three arguments

b

,

0

, and

b.length

.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data.
**Throws:** NullPointerException

- if

b

is null.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** write(byte[], int, int)

- write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes

len

bytes from the specified byte array
starting at offset

off

to this output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.write(int)

- flush

```java
public void flush()
throws
IOException
```

Flushes this output stream by forcing any buffered output bytes
that have already been processed by the encapsulated cipher object
to be written out.

Any bytes buffered by the encapsulated cipher
and waiting to be processed by it will not be written out. For example,
if the encapsulated cipher is a block cipher, and the total number of
bytes written using one of the

write

methods is less than
the cipher's block size, no bytes will be written out.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- close

```java
public void close()
throws
IOException
```

Closes this output stream and releases any system resources
associated with this stream.

This method invokes the

doFinal

method of the encapsulated
cipher object, which causes any bytes buffered by the encapsulated
cipher to be processed. The result is written out by calling the

flush

method of this output stream.

This method resets the encapsulated cipher object to its initial state
and calls the

close

method of the underlying output
stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.flush()

,

FilterOutputStream.out

---

#### Method Detail

write

```java
public void write​(int b)
throws
IOException
```

Writes the specified byte to this output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the

byte

.
**Throws:** IOException

- if an I/O error occurs.

---

#### write

public void write​(int b)
throws

IOException

Writes the specified byte to this output stream.

write

```java
public void write​(byte[] b)
throws
IOException
```

Writes

b.length

bytes from the specified byte array
to this output stream.

The

write

method of

CipherOutputStream

calls the

write

method of three arguments with the three arguments

b

,

0

, and

b.length

.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data.
**Throws:** NullPointerException

- if

b

is null.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** write(byte[], int, int)

---

#### write

public void write​(byte[] b)
throws

IOException

Writes

b.length

bytes from the specified byte array
to this output stream.

The

write

method of

CipherOutputStream

calls the

write

method of three arguments with the three arguments

b

,

0

, and

b.length

.

The

write

method of

CipherOutputStream

calls the

write

method of three arguments with the three arguments

b

,

0

, and

b.length

.

write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes

len

bytes from the specified byte array
starting at offset

off

to this output stream.

**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.write(int)

---

#### write

public void write​(byte[] b,
int off,
int len)
throws

IOException

Writes

len

bytes from the specified byte array
starting at offset

off

to this output stream.

flush

```java
public void flush()
throws
IOException
```

Flushes this output stream by forcing any buffered output bytes
that have already been processed by the encapsulated cipher object
to be written out.

Any bytes buffered by the encapsulated cipher
and waiting to be processed by it will not be written out. For example,
if the encapsulated cipher is a block cipher, and the total number of
bytes written using one of the

write

methods is less than
the cipher's block size, no bytes will be written out.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

---

#### flush

public void flush()
throws

IOException

Flushes this output stream by forcing any buffered output bytes
that have already been processed by the encapsulated cipher object
to be written out.

Any bytes buffered by the encapsulated cipher
and waiting to be processed by it will not be written out. For example,
if the encapsulated cipher is a block cipher, and the total number of
bytes written using one of the

write

methods is less than
the cipher's block size, no bytes will be written out.

Any bytes buffered by the encapsulated cipher
and waiting to be processed by it will not be written out. For example,
if the encapsulated cipher is a block cipher, and the total number of
bytes written using one of the

write

methods is less than
the cipher's block size, no bytes will be written out.

close

```java
public void close()
throws
IOException
```

Closes this output stream and releases any system resources
associated with this stream.

This method invokes the

doFinal

method of the encapsulated
cipher object, which causes any bytes buffered by the encapsulated
cipher to be processed. The result is written out by calling the

flush

method of this output stream.

This method resets the encapsulated cipher object to its initial state
and calls the

close

method of the underlying output
stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.flush()

,

FilterOutputStream.out

---

#### close

public void close()
throws

IOException

Closes this output stream and releases any system resources
associated with this stream.

This method invokes the

doFinal

method of the encapsulated
cipher object, which causes any bytes buffered by the encapsulated
cipher to be processed. The result is written out by calling the

flush

method of this output stream.

This method resets the encapsulated cipher object to its initial state
and calls the

close

method of the underlying output
stream.

This method invokes the

doFinal

method of the encapsulated
cipher object, which causes any bytes buffered by the encapsulated
cipher to be processed. The result is written out by calling the

flush

method of this output stream.

This method resets the encapsulated cipher object to its initial state
and calls the

close

method of the underlying output
stream.

This method resets the encapsulated cipher object to its initial state
and calls the

close

method of the underlying output
stream.

---

