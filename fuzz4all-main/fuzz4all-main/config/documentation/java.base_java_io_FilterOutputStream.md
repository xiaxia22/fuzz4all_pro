# Class FilterOutputStream

**Source:** `java.base\java\io\FilterOutputStream.html`

### Class Description

```java
public class
FilterOutputStream

extends
OutputStream
```

This class is the superclass of all classes that filter output
streams. These streams sit on top of an already existing output
stream (the

underlying

output stream) which it uses as its
basic sink of data, but possibly transforming the data along the
way or providing additional functionality.

The class

FilterOutputStream

itself simply overrides
all methods of

OutputStream

with versions that pass
all requests to the underlying output stream. Subclasses of

FilterOutputStream

may further override some of these
methods as well as provide additional methods and fields.

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

---

### Field Details

#### protected
OutputStream
out

The underlying output stream to be filtered.

---

### Constructor Details

#### public FilterOutputStream​(
OutputStream
out)

Creates an output stream filter built on top of the specified
underlying output stream.

**Parameters:**
- out

- the underlying output stream to be assigned to
the field

this.out

for later use, or

null

if this instance is to be
created without an underlying stream.

---

### Method Details

#### public void write​(int b)
throws
IOException

Writes the specified

byte

to this output stream.

The

write

method of

FilterOutputStream

calls the

write

method of its underlying output stream,
that is, it performs

out.write(b)

.

Implements the abstract

write

method of

OutputStream

.

**Specified by:**
- write

in class

OutputStream

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

bytes to this output stream.

The

write

method of

FilterOutputStream

calls its

write

method of three arguments with the
arguments

b

,

0

, and

b.length

.

Note that this method does not call the one-argument

write

method of its underlying output stream with
the single argument

b

.

**Overrides:**
- write

in class

OutputStream

**Parameters:**
- b

- the data to be written.

**Throws:**
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

bytes from the specified

byte

array starting at offset

off

to
this output stream.

The

write

method of

FilterOutputStream

calls the

write

method of one argument on each

byte

to output.

Note that this method does not call the

write

method
of its underlying output stream with the same arguments. Subclasses
of

FilterOutputStream

should provide a more efficient
implementation of this method.

**Overrides:**
- write

in class

OutputStream

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
- write(int)

---

#### public void flush()
throws
IOException

Flushes this output stream and forces any buffered output bytes
to be written out to the stream.

The

flush

method of

FilterOutputStream

calls the

flush

method of its underlying output stream.

**Specified by:**
- flush

in interface

Flushable

**Overrides:**
- flush

in class

OutputStream

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- out

---

#### public void close()
throws
IOException

Closes this output stream and releases any system resources
associated with the stream.

When not already closed, the

close

method of

FilterOutputStream

calls its

flush

method, and then
calls the

close

method of its underlying output stream.

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

OutputStream

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- flush()

,

out

---

### Additional Sections

#### Class FilterOutputStream

java.lang.Object

- java.io.OutputStream
- - java.io.FilterOutputStream

java.io.OutputStream

- java.io.FilterOutputStream

java.io.FilterOutputStream

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

**Direct Known Subclasses:** BufferedOutputStream

,

CheckedOutputStream

,

CipherOutputStream

,

DataOutputStream

,

DeflaterOutputStream

,

DigestOutputStream

,

InflaterOutputStream

,

PrintStream

```java
public class
FilterOutputStream

extends
OutputStream
```

This class is the superclass of all classes that filter output
streams. These streams sit on top of an already existing output
stream (the

underlying

output stream) which it uses as its
basic sink of data, but possibly transforming the data along the
way or providing additional functionality.

The class

FilterOutputStream

itself simply overrides
all methods of

OutputStream

with versions that pass
all requests to the underlying output stream. Subclasses of

FilterOutputStream

may further override some of these
methods as well as provide additional methods and fields.

**Since:** 1.0

public class

FilterOutputStream

extends

OutputStream

This class is the superclass of all classes that filter output
streams. These streams sit on top of an already existing output
stream (the

underlying

output stream) which it uses as its
basic sink of data, but possibly transforming the data along the
way or providing additional functionality.

The class

FilterOutputStream

itself simply overrides
all methods of

OutputStream

with versions that pass
all requests to the underlying output stream. Subclasses of

FilterOutputStream

may further override some of these
methods as well as provide additional methods and fields.

The class

FilterOutputStream

itself simply overrides
all methods of

OutputStream

with versions that pass
all requests to the underlying output stream. Subclasses of

FilterOutputStream

may further override some of these
methods as well as provide additional methods and fields.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

OutputStream

out

The underlying output stream to be filtered.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FilterOutputStream

​(

OutputStream

out)

Creates an output stream filter built on top of the specified
underlying output stream.

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
associated with the stream.

void

flush

()

Flushes this output stream and forces any buffered output bytes
to be written out to the stream.

void

write

​(byte[] b)

Writes

b.length

bytes to this output stream.

void

write

​(byte[] b,
int off,
int len)

Writes

len

bytes from the specified

byte

array starting at offset

off

to
this output stream.

void

write

​(int b)

Writes the specified

byte

to this output stream.

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

Fields

Modifier and Type

Field

Description

protected

OutputStream

out

The underlying output stream to be filtered.

---

#### Field Summary

The underlying output stream to be filtered.

Constructor Summary

Constructors

Constructor

Description

FilterOutputStream

​(

OutputStream

out)

Creates an output stream filter built on top of the specified
underlying output stream.

---

#### Constructor Summary

Creates an output stream filter built on top of the specified
underlying output stream.

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
associated with the stream.

void

flush

()

Flushes this output stream and forces any buffered output bytes
to be written out to the stream.

void

write

​(byte[] b)

Writes

b.length

bytes to this output stream.

void

write

​(byte[] b,
int off,
int len)

Writes

len

bytes from the specified

byte

array starting at offset

off

to
this output stream.

void

write

​(int b)

Writes the specified

byte

to this output stream.

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
associated with the stream.

Flushes this output stream and forces any buffered output bytes
to be written out to the stream.

Writes

b.length

bytes to this output stream.

Writes

len

bytes from the specified

byte

array starting at offset

off

to
this output stream.

Writes the specified

byte

to this output stream.

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

============ FIELD DETAIL ===========

- Field Detail

- out

```java
protected
OutputStream
out
```

The underlying output stream to be filtered.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FilterOutputStream

```java
public FilterOutputStream​(
OutputStream
out)
```

Creates an output stream filter built on top of the specified
underlying output stream.

**Parameters:** out

- the underlying output stream to be assigned to
the field

this.out

for later use, or

null

if this instance is to be
created without an underlying stream.

============ METHOD DETAIL ==========

- Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes the specified

byte

to this output stream.

The

write

method of

FilterOutputStream

calls the

write

method of its underlying output stream,
that is, it performs

out.write(b)

.

Implements the abstract

write

method of

OutputStream

.

**Specified by:** write

in class

OutputStream
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

bytes to this output stream.

The

write

method of

FilterOutputStream

calls its

write

method of three arguments with the
arguments

b

,

0

, and

b.length

.

Note that this method does not call the one-argument

write

method of its underlying output stream with
the single argument

b

.

**Overrides:** write

in class

OutputStream
**Parameters:** b

- the data to be written.
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

bytes from the specified

byte

array starting at offset

off

to
this output stream.

The

write

method of

FilterOutputStream

calls the

write

method of one argument on each

byte

to output.

Note that this method does not call the

write

method
of its underlying output stream with the same arguments. Subclasses
of

FilterOutputStream

should provide a more efficient
implementation of this method.

**Overrides:** write

in class

OutputStream
**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** write(int)

- flush

```java
public void flush()
throws
IOException
```

Flushes this output stream and forces any buffered output bytes
to be written out to the stream.

The

flush

method of

FilterOutputStream

calls the

flush

method of its underlying output stream.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

OutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** out

- close

```java
public void close()
throws
IOException
```

Closes this output stream and releases any system resources
associated with the stream.

When not already closed, the

close

method of

FilterOutputStream

calls its

flush

method, and then
calls the

close

method of its underlying output stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

OutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** flush()

,

out

Field Detail

- out

```java
protected
OutputStream
out
```

The underlying output stream to be filtered.

---

#### Field Detail

out

```java
protected
OutputStream
out
```

The underlying output stream to be filtered.

---

#### out

protected

OutputStream

out

The underlying output stream to be filtered.

Constructor Detail

- FilterOutputStream

```java
public FilterOutputStream​(
OutputStream
out)
```

Creates an output stream filter built on top of the specified
underlying output stream.

**Parameters:** out

- the underlying output stream to be assigned to
the field

this.out

for later use, or

null

if this instance is to be
created without an underlying stream.

---

#### Constructor Detail

FilterOutputStream

```java
public FilterOutputStream​(
OutputStream
out)
```

Creates an output stream filter built on top of the specified
underlying output stream.

**Parameters:** out

- the underlying output stream to be assigned to
the field

this.out

for later use, or

null

if this instance is to be
created without an underlying stream.

---

#### FilterOutputStream

public FilterOutputStream​(

OutputStream

out)

Creates an output stream filter built on top of the specified
underlying output stream.

Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes the specified

byte

to this output stream.

The

write

method of

FilterOutputStream

calls the

write

method of its underlying output stream,
that is, it performs

out.write(b)

.

Implements the abstract

write

method of

OutputStream

.

**Specified by:** write

in class

OutputStream
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

bytes to this output stream.

The

write

method of

FilterOutputStream

calls its

write

method of three arguments with the
arguments

b

,

0

, and

b.length

.

Note that this method does not call the one-argument

write

method of its underlying output stream with
the single argument

b

.

**Overrides:** write

in class

OutputStream
**Parameters:** b

- the data to be written.
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

bytes from the specified

byte

array starting at offset

off

to
this output stream.

The

write

method of

FilterOutputStream

calls the

write

method of one argument on each

byte

to output.

Note that this method does not call the

write

method
of its underlying output stream with the same arguments. Subclasses
of

FilterOutputStream

should provide a more efficient
implementation of this method.

**Overrides:** write

in class

OutputStream
**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** write(int)

- flush

```java
public void flush()
throws
IOException
```

Flushes this output stream and forces any buffered output bytes
to be written out to the stream.

The

flush

method of

FilterOutputStream

calls the

flush

method of its underlying output stream.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

OutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** out

- close

```java
public void close()
throws
IOException
```

Closes this output stream and releases any system resources
associated with the stream.

When not already closed, the

close

method of

FilterOutputStream

calls its

flush

method, and then
calls the

close

method of its underlying output stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

OutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** flush()

,

out

---

#### Method Detail

write

```java
public void write​(int b)
throws
IOException
```

Writes the specified

byte

to this output stream.

The

write

method of

FilterOutputStream

calls the

write

method of its underlying output stream,
that is, it performs

out.write(b)

.

Implements the abstract

write

method of

OutputStream

.

**Specified by:** write

in class

OutputStream
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

Writes the specified

byte

to this output stream.

The

write

method of

FilterOutputStream

calls the

write

method of its underlying output stream,
that is, it performs

out.write(b)

.

Implements the abstract

write

method of

OutputStream

.

The

write

method of

FilterOutputStream

calls the

write

method of its underlying output stream,
that is, it performs

out.write(b)

.

Implements the abstract

write

method of

OutputStream

.

Implements the abstract

write

method of

OutputStream

.

write

```java
public void write​(byte[] b)
throws
IOException
```

Writes

b.length

bytes to this output stream.

The

write

method of

FilterOutputStream

calls its

write

method of three arguments with the
arguments

b

,

0

, and

b.length

.

Note that this method does not call the one-argument

write

method of its underlying output stream with
the single argument

b

.

**Overrides:** write

in class

OutputStream
**Parameters:** b

- the data to be written.
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

bytes to this output stream.

The

write

method of

FilterOutputStream

calls its

write

method of three arguments with the
arguments

b

,

0

, and

b.length

.

Note that this method does not call the one-argument

write

method of its underlying output stream with
the single argument

b

.

The

write

method of

FilterOutputStream

calls its

write

method of three arguments with the
arguments

b

,

0

, and

b.length

.

Note that this method does not call the one-argument

write

method of its underlying output stream with
the single argument

b

.

Note that this method does not call the one-argument

write

method of its underlying output stream with
the single argument

b

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

bytes from the specified

byte

array starting at offset

off

to
this output stream.

The

write

method of

FilterOutputStream

calls the

write

method of one argument on each

byte

to output.

Note that this method does not call the

write

method
of its underlying output stream with the same arguments. Subclasses
of

FilterOutputStream

should provide a more efficient
implementation of this method.

**Overrides:** write

in class

OutputStream
**Parameters:** b

- the data.
**Parameters:** off

- the start offset in the data.
**Parameters:** len

- the number of bytes to write.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** write(int)

---

#### write

public void write​(byte[] b,
int off,
int len)
throws

IOException

Writes

len

bytes from the specified

byte

array starting at offset

off

to
this output stream.

The

write

method of

FilterOutputStream

calls the

write

method of one argument on each

byte

to output.

Note that this method does not call the

write

method
of its underlying output stream with the same arguments. Subclasses
of

FilterOutputStream

should provide a more efficient
implementation of this method.

The

write

method of

FilterOutputStream

calls the

write

method of one argument on each

byte

to output.

Note that this method does not call the

write

method
of its underlying output stream with the same arguments. Subclasses
of

FilterOutputStream

should provide a more efficient
implementation of this method.

Note that this method does not call the

write

method
of its underlying output stream with the same arguments. Subclasses
of

FilterOutputStream

should provide a more efficient
implementation of this method.

flush

```java
public void flush()
throws
IOException
```

Flushes this output stream and forces any buffered output bytes
to be written out to the stream.

The

flush

method of

FilterOutputStream

calls the

flush

method of its underlying output stream.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

OutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** out

---

#### flush

public void flush()
throws

IOException

Flushes this output stream and forces any buffered output bytes
to be written out to the stream.

The

flush

method of

FilterOutputStream

calls the

flush

method of its underlying output stream.

The

flush

method of

FilterOutputStream

calls the

flush

method of its underlying output stream.

close

```java
public void close()
throws
IOException
```

Closes this output stream and releases any system resources
associated with the stream.

When not already closed, the

close

method of

FilterOutputStream

calls its

flush

method, and then
calls the

close

method of its underlying output stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

OutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** flush()

,

out

---

#### close

public void close()
throws

IOException

Closes this output stream and releases any system resources
associated with the stream.

When not already closed, the

close

method of

FilterOutputStream

calls its

flush

method, and then
calls the

close

method of its underlying output stream.

When not already closed, the

close

method of

FilterOutputStream

calls its

flush

method, and then
calls the

close

method of its underlying output stream.

---

