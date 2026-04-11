# Class ByteArrayInputStream

**Source:** `java.base\java\io\ByteArrayInputStream.html`

### Class Description

```java
public class
ByteArrayInputStream

extends
InputStream
```

A

ByteArrayInputStream

contains
an internal buffer that contains bytes that
may be read from the stream. An internal
counter keeps track of the next byte to
be supplied by the

read

method.

Closing a

ByteArrayInputStream

has no effect. The methods in
this class can be called after the stream has been closed without
generating an

IOException

.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

#### protected byte[] buf

An array of bytes that was provided
by the creator of the stream. Elements

buf[0]

through

buf[count-1]

are the
only bytes that can ever be read from the
stream; element

buf[pos]

is
the next byte to be read.

---

#### protected int pos

The index of the next character to read from the input stream buffer.
This value should always be nonnegative
and not larger than the value of

count

.
The next byte to be read from the input stream buffer
will be

buf[pos]

.

---

#### protected int mark

The currently marked position in the stream.
ByteArrayInputStream objects are marked at position zero by
default when constructed. They may be marked at another
position within the buffer by the

mark()

method.
The current buffer position is set to this point by the

reset()

method.

If no mark has been set, then the value of mark is the offset
passed to the constructor (or 0 if the offset was not supplied).

**Since:**
- 1.1

---

#### protected int count

The index one greater than the last valid character in the input
stream buffer.
This value should always be nonnegative
and not larger than the length of

buf

.
It is one greater than the position of
the last byte within

buf

that
can ever be read from the input stream buffer.

---

### Constructor Details

#### public ByteArrayInputStream​(byte[] buf)

Creates a

ByteArrayInputStream

so that it uses

buf

as its
buffer array.
The buffer array is not copied.
The initial value of

pos

is

0

and the initial value
of

count

is the length of

buf

.

**Parameters:**
- buf

- the input buffer.

---

#### public ByteArrayInputStream​(byte[] buf,
int offset,
int length)

Creates

ByteArrayInputStream

that uses

buf

as its
buffer array. The initial value of

pos

is

offset

and the initial value
of

count

is the minimum of

offset+length

and

buf.length

.
The buffer array is not copied. The buffer's mark is
set to the specified offset.

**Parameters:**
- buf

- the input buffer.
- offset

- the offset in the buffer of the first byte to read.
- length

- the maximum number of bytes to read from the buffer.

---

### Method Details

#### public int read()

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

is returned.

This

read

method
cannot block.

**Specified by:**
- read

in class

InputStream

**Returns:**
- the next byte of data, or

-1

if the end of the
stream has been reached.

---

#### public int read​(byte[] b,
int off,
int len)

Reads up to

len

bytes of data into an array of bytes from this
input stream. If

pos

equals

count

, then

-1

is
returned to indicate end of file. Otherwise, the number

k

of
bytes read is equal to the smaller of

len

and

count-pos

.
If

k

is positive, then bytes

buf[pos]

through

buf[pos+k-1]

are copied into

b[off]

through

b[off+k-1]

in the manner performed by

System.arraycopy

.
The value

k

is added into

pos

and

k

is returned.

This

read

method cannot block.

**Overrides:**
- read

in class

InputStream

**Parameters:**
- b

- the buffer into which the data is read.
- off

- the start offset in the destination array

b
- len

- the maximum number of bytes read.

**Returns:**
- the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.

**Throws:**
- NullPointerException

- If

b

is

null

.
- IndexOutOfBoundsException

- If

off

is negative,

len

is negative, or

len

is greater than

b.length - off

**See Also:**
- InputStream.read()

---

#### public long skip​(long n)

Skips

n

bytes of input from this input stream. Fewer
bytes might be skipped if the end of the input stream is reached.
The actual number

k

of bytes to be skipped is equal to the smaller
of

n

and

count-pos

.
The value

k

is added into

pos

and

k

is returned.

**Overrides:**
- skip

in class

InputStream

**Parameters:**
- n

- the number of bytes to be skipped.

**Returns:**
- the actual number of bytes skipped.

---

#### public int available()

Returns the number of remaining bytes that can be read (or skipped over)
from this input stream.

The value returned is

count - pos

,
which is the number of bytes remaining to be read from the input buffer.

**Overrides:**
- available

in class

InputStream

**Returns:**
- the number of remaining bytes that can be read (or skipped
over) from this input stream without blocking.

---

#### public boolean markSupported()

Tests if this

InputStream

supports mark/reset. The

markSupported

method of

ByteArrayInputStream

always returns

true

.

**Overrides:**
- markSupported

in class

InputStream

**Returns:**
- true

if this stream instance supports the mark
and reset methods;

false

otherwise.

**See Also:**
- InputStream.mark(int)

,

InputStream.reset()

**Since:**
- 1.1

---

#### public void mark​(int readAheadLimit)

Set the current marked position in the stream.
ByteArrayInputStream objects are marked at position zero by
default when constructed. They may be marked at another
position within the buffer by this method.

If no mark has been set, then the value of the mark is the
offset passed to the constructor (or 0 if the offset was not
supplied).

Note: The

readAheadLimit

for this class
has no meaning.

**Overrides:**
- mark

in class

InputStream

**Parameters:**
- readAheadLimit

- the maximum limit of bytes that can be read before
the mark position becomes invalid.

**See Also:**
- InputStream.reset()

**Since:**
- 1.1

---

#### public void reset()

Resets the buffer to the marked position. The marked position
is 0 unless another position was marked or an offset was specified
in the constructor.

**Overrides:**
- reset

in class

InputStream

**See Also:**
- InputStream.mark(int)

,

IOException

---

#### public void close()
throws
IOException

Closing a

ByteArrayInputStream

has no effect. The methods in
this class can be called after the stream has been closed without
generating an

IOException

.

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

InputStream

**Throws:**
- IOException

- if an I/O error occurs.

---

### Additional Sections

#### Class ByteArrayInputStream

java.lang.Object

- java.io.InputStream
- - java.io.ByteArrayInputStream

java.io.InputStream

- java.io.ByteArrayInputStream

java.io.ByteArrayInputStream

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
public class
ByteArrayInputStream

extends
InputStream
```

A

ByteArrayInputStream

contains
an internal buffer that contains bytes that
may be read from the stream. An internal
counter keeps track of the next byte to
be supplied by the

read

method.

Closing a

ByteArrayInputStream

has no effect. The methods in
this class can be called after the stream has been closed without
generating an

IOException

.

**Since:** 1.0
**See Also:** StringBufferInputStream

public class

ByteArrayInputStream

extends

InputStream

A

ByteArrayInputStream

contains
an internal buffer that contains bytes that
may be read from the stream. An internal
counter keeps track of the next byte to
be supplied by the

read

method.

Closing a

ByteArrayInputStream

has no effect. The methods in
this class can be called after the stream has been closed without
generating an

IOException

.

Closing a

ByteArrayInputStream

has no effect. The methods in
this class can be called after the stream has been closed without
generating an

IOException

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected byte[]

buf

An array of bytes that was provided
by the creator of the stream.

protected int

count

The index one greater than the last valid character in the input
stream buffer.

protected int

mark

The currently marked position in the stream.

protected int

pos

The index of the next character to read from the input stream buffer.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ByteArrayInputStream

​(byte[] buf)

Creates a

ByteArrayInputStream

so that it uses

buf

as its
buffer array.

ByteArrayInputStream

​(byte[] buf,
int offset,
int length)

Creates

ByteArrayInputStream

that uses

buf

as its
buffer array.

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

Returns the number of remaining bytes that can be read (or skipped over)
from this input stream.

void

close

()

Closing a

ByteArrayInputStream

has no effect.

void

mark

​(int readAheadLimit)

Set the current marked position in the stream.

boolean

markSupported

()

Tests if this

InputStream

supports mark/reset.

int

read

()

Reads the next byte of data from this input stream.

int

read

​(byte[] b,
int off,
int len)

Reads up to

len

bytes of data into an array of bytes from this
input stream.

void

reset

()

Resets the buffer to the marked position.

long

skip

​(long n)

Skips

n

bytes of input from this input stream.

- Methods declared in class java.io.

InputStream

nullInputStream

,

read

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

Fields

Modifier and Type

Field

Description

protected byte[]

buf

An array of bytes that was provided
by the creator of the stream.

protected int

count

The index one greater than the last valid character in the input
stream buffer.

protected int

mark

The currently marked position in the stream.

protected int

pos

The index of the next character to read from the input stream buffer.

---

#### Field Summary

An array of bytes that was provided
by the creator of the stream.

The index one greater than the last valid character in the input
stream buffer.

The currently marked position in the stream.

The index of the next character to read from the input stream buffer.

Constructor Summary

Constructors

Constructor

Description

ByteArrayInputStream

​(byte[] buf)

Creates a

ByteArrayInputStream

so that it uses

buf

as its
buffer array.

ByteArrayInputStream

​(byte[] buf,
int offset,
int length)

Creates

ByteArrayInputStream

that uses

buf

as its
buffer array.

---

#### Constructor Summary

Creates a

ByteArrayInputStream

so that it uses

buf

as its
buffer array.

Creates

ByteArrayInputStream

that uses

buf

as its
buffer array.

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

Returns the number of remaining bytes that can be read (or skipped over)
from this input stream.

void

close

()

Closing a

ByteArrayInputStream

has no effect.

void

mark

​(int readAheadLimit)

Set the current marked position in the stream.

boolean

markSupported

()

Tests if this

InputStream

supports mark/reset.

int

read

()

Reads the next byte of data from this input stream.

int

read

​(byte[] b,
int off,
int len)

Reads up to

len

bytes of data into an array of bytes from this
input stream.

void

reset

()

Resets the buffer to the marked position.

long

skip

​(long n)

Skips

n

bytes of input from this input stream.

- Methods declared in class java.io.

InputStream

nullInputStream

,

read

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

Returns the number of remaining bytes that can be read (or skipped over)
from this input stream.

Closing a

ByteArrayInputStream

has no effect.

Set the current marked position in the stream.

Tests if this

InputStream

supports mark/reset.

Reads the next byte of data from this input stream.

Reads up to

len

bytes of data into an array of bytes from this
input stream.

Resets the buffer to the marked position.

Skips

n

bytes of input from this input stream.

Methods declared in class java.io.

InputStream

nullInputStream

,

read

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

============ FIELD DETAIL ===========

- Field Detail

- buf

```java
protected byte[] buf
```

An array of bytes that was provided
by the creator of the stream. Elements

buf[0]

through

buf[count-1]

are the
only bytes that can ever be read from the
stream; element

buf[pos]

is
the next byte to be read.

- pos

```java
protected int pos
```

The index of the next character to read from the input stream buffer.
This value should always be nonnegative
and not larger than the value of

count

.
The next byte to be read from the input stream buffer
will be

buf[pos]

.

- mark

```java
protected int mark
```

The currently marked position in the stream.
ByteArrayInputStream objects are marked at position zero by
default when constructed. They may be marked at another
position within the buffer by the

mark()

method.
The current buffer position is set to this point by the

reset()

method.

If no mark has been set, then the value of mark is the offset
passed to the constructor (or 0 if the offset was not supplied).

**Since:** 1.1

- count

```java
protected int count
```

The index one greater than the last valid character in the input
stream buffer.
This value should always be nonnegative
and not larger than the length of

buf

.
It is one greater than the position of
the last byte within

buf

that
can ever be read from the input stream buffer.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ByteArrayInputStream

```java
public ByteArrayInputStream​(byte[] buf)
```

Creates a

ByteArrayInputStream

so that it uses

buf

as its
buffer array.
The buffer array is not copied.
The initial value of

pos

is

0

and the initial value
of

count

is the length of

buf

.

**Parameters:** buf

- the input buffer.

- ByteArrayInputStream

```java
public ByteArrayInputStream​(byte[] buf,
int offset,
int length)
```

Creates

ByteArrayInputStream

that uses

buf

as its
buffer array. The initial value of

pos

is

offset

and the initial value
of

count

is the minimum of

offset+length

and

buf.length

.
The buffer array is not copied. The buffer's mark is
set to the specified offset.

**Parameters:** buf

- the input buffer.
**Parameters:** offset

- the offset in the buffer of the first byte to read.
**Parameters:** length

- the maximum number of bytes to read from the buffer.

============ METHOD DETAIL ==========

- Method Detail

- read

```java
public int read()
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

is returned.

This

read

method
cannot block.

**Specified by:** read

in class

InputStream
**Returns:** the next byte of data, or

-1

if the end of the
stream has been reached.

- read

```java
public int read​(byte[] b,
int off,
int len)
```

Reads up to

len

bytes of data into an array of bytes from this
input stream. If

pos

equals

count

, then

-1

is
returned to indicate end of file. Otherwise, the number

k

of
bytes read is equal to the smaller of

len

and

count-pos

.
If

k

is positive, then bytes

buf[pos]

through

buf[pos+k-1]

are copied into

b[off]

through

b[off+k-1]

in the manner performed by

System.arraycopy

.
The value

k

is added into

pos

and

k

is returned.

This

read

method cannot block.

**Overrides:** read

in class

InputStream
**Parameters:** b

- the buffer into which the data is read.
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** NullPointerException

- If

b

is

null

.
**Throws:** IndexOutOfBoundsException

- If

off

is negative,

len

is negative, or

len

is greater than

b.length - off
**See Also:** InputStream.read()

- skip

```java
public long skip​(long n)
```

Skips

n

bytes of input from this input stream. Fewer
bytes might be skipped if the end of the input stream is reached.
The actual number

k

of bytes to be skipped is equal to the smaller
of

n

and

count-pos

.
The value

k

is added into

pos

and

k

is returned.

**Overrides:** skip

in class

InputStream
**Parameters:** n

- the number of bytes to be skipped.
**Returns:** the actual number of bytes skipped.

- available

```java
public int available()
```

Returns the number of remaining bytes that can be read (or skipped over)
from this input stream.

The value returned is

count - pos

,
which is the number of bytes remaining to be read from the input buffer.

**Overrides:** available

in class

InputStream
**Returns:** the number of remaining bytes that can be read (or skipped
over) from this input stream without blocking.

- markSupported

```java
public boolean markSupported()
```

Tests if this

InputStream

supports mark/reset. The

markSupported

method of

ByteArrayInputStream

always returns

true

.

**Overrides:** markSupported

in class

InputStream
**Returns:** true

if this stream instance supports the mark
and reset methods;

false

otherwise.
**Since:** 1.1
**See Also:** InputStream.mark(int)

,

InputStream.reset()

- mark

```java
public void mark​(int readAheadLimit)
```

Set the current marked position in the stream.
ByteArrayInputStream objects are marked at position zero by
default when constructed. They may be marked at another
position within the buffer by this method.

If no mark has been set, then the value of the mark is the
offset passed to the constructor (or 0 if the offset was not
supplied).

Note: The

readAheadLimit

for this class
has no meaning.

**Overrides:** mark

in class

InputStream
**Parameters:** readAheadLimit

- the maximum limit of bytes that can be read before
the mark position becomes invalid.
**Since:** 1.1
**See Also:** InputStream.reset()

- reset

```java
public void reset()
```

Resets the buffer to the marked position. The marked position
is 0 unless another position was marked or an offset was specified
in the constructor.

**Overrides:** reset

in class

InputStream
**See Also:** InputStream.mark(int)

,

IOException

- close

```java
public void close()
throws
IOException
```

Closing a

ByteArrayInputStream

has no effect. The methods in
this class can be called after the stream has been closed without
generating an

IOException

.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

InputStream
**Throws:** IOException

- if an I/O error occurs.

Field Detail

- buf

```java
protected byte[] buf
```

An array of bytes that was provided
by the creator of the stream. Elements

buf[0]

through

buf[count-1]

are the
only bytes that can ever be read from the
stream; element

buf[pos]

is
the next byte to be read.

- pos

```java
protected int pos
```

The index of the next character to read from the input stream buffer.
This value should always be nonnegative
and not larger than the value of

count

.
The next byte to be read from the input stream buffer
will be

buf[pos]

.

- mark

```java
protected int mark
```

The currently marked position in the stream.
ByteArrayInputStream objects are marked at position zero by
default when constructed. They may be marked at another
position within the buffer by the

mark()

method.
The current buffer position is set to this point by the

reset()

method.

If no mark has been set, then the value of mark is the offset
passed to the constructor (or 0 if the offset was not supplied).

**Since:** 1.1

- count

```java
protected int count
```

The index one greater than the last valid character in the input
stream buffer.
This value should always be nonnegative
and not larger than the length of

buf

.
It is one greater than the position of
the last byte within

buf

that
can ever be read from the input stream buffer.

---

#### Field Detail

buf

```java
protected byte[] buf
```

An array of bytes that was provided
by the creator of the stream. Elements

buf[0]

through

buf[count-1]

are the
only bytes that can ever be read from the
stream; element

buf[pos]

is
the next byte to be read.

---

#### buf

protected byte[] buf

An array of bytes that was provided
by the creator of the stream. Elements

buf[0]

through

buf[count-1]

are the
only bytes that can ever be read from the
stream; element

buf[pos]

is
the next byte to be read.

pos

```java
protected int pos
```

The index of the next character to read from the input stream buffer.
This value should always be nonnegative
and not larger than the value of

count

.
The next byte to be read from the input stream buffer
will be

buf[pos]

.

---

#### pos

protected int pos

The index of the next character to read from the input stream buffer.
This value should always be nonnegative
and not larger than the value of

count

.
The next byte to be read from the input stream buffer
will be

buf[pos]

.

mark

```java
protected int mark
```

The currently marked position in the stream.
ByteArrayInputStream objects are marked at position zero by
default when constructed. They may be marked at another
position within the buffer by the

mark()

method.
The current buffer position is set to this point by the

reset()

method.

If no mark has been set, then the value of mark is the offset
passed to the constructor (or 0 if the offset was not supplied).

**Since:** 1.1

---

#### mark

protected int mark

The currently marked position in the stream.
ByteArrayInputStream objects are marked at position zero by
default when constructed. They may be marked at another
position within the buffer by the

mark()

method.
The current buffer position is set to this point by the

reset()

method.

If no mark has been set, then the value of mark is the offset
passed to the constructor (or 0 if the offset was not supplied).

If no mark has been set, then the value of mark is the offset
passed to the constructor (or 0 if the offset was not supplied).

count

```java
protected int count
```

The index one greater than the last valid character in the input
stream buffer.
This value should always be nonnegative
and not larger than the length of

buf

.
It is one greater than the position of
the last byte within

buf

that
can ever be read from the input stream buffer.

---

#### count

protected int count

The index one greater than the last valid character in the input
stream buffer.
This value should always be nonnegative
and not larger than the length of

buf

.
It is one greater than the position of
the last byte within

buf

that
can ever be read from the input stream buffer.

Constructor Detail

- ByteArrayInputStream

```java
public ByteArrayInputStream​(byte[] buf)
```

Creates a

ByteArrayInputStream

so that it uses

buf

as its
buffer array.
The buffer array is not copied.
The initial value of

pos

is

0

and the initial value
of

count

is the length of

buf

.

**Parameters:** buf

- the input buffer.

- ByteArrayInputStream

```java
public ByteArrayInputStream​(byte[] buf,
int offset,
int length)
```

Creates

ByteArrayInputStream

that uses

buf

as its
buffer array. The initial value of

pos

is

offset

and the initial value
of

count

is the minimum of

offset+length

and

buf.length

.
The buffer array is not copied. The buffer's mark is
set to the specified offset.

**Parameters:** buf

- the input buffer.
**Parameters:** offset

- the offset in the buffer of the first byte to read.
**Parameters:** length

- the maximum number of bytes to read from the buffer.

---

#### Constructor Detail

ByteArrayInputStream

```java
public ByteArrayInputStream​(byte[] buf)
```

Creates a

ByteArrayInputStream

so that it uses

buf

as its
buffer array.
The buffer array is not copied.
The initial value of

pos

is

0

and the initial value
of

count

is the length of

buf

.

**Parameters:** buf

- the input buffer.

---

#### ByteArrayInputStream

public ByteArrayInputStream​(byte[] buf)

Creates a

ByteArrayInputStream

so that it uses

buf

as its
buffer array.
The buffer array is not copied.
The initial value of

pos

is

0

and the initial value
of

count

is the length of

buf

.

ByteArrayInputStream

```java
public ByteArrayInputStream​(byte[] buf,
int offset,
int length)
```

Creates

ByteArrayInputStream

that uses

buf

as its
buffer array. The initial value of

pos

is

offset

and the initial value
of

count

is the minimum of

offset+length

and

buf.length

.
The buffer array is not copied. The buffer's mark is
set to the specified offset.

**Parameters:** buf

- the input buffer.
**Parameters:** offset

- the offset in the buffer of the first byte to read.
**Parameters:** length

- the maximum number of bytes to read from the buffer.

---

#### ByteArrayInputStream

public ByteArrayInputStream​(byte[] buf,
int offset,
int length)

Creates

ByteArrayInputStream

that uses

buf

as its
buffer array. The initial value of

pos

is

offset

and the initial value
of

count

is the minimum of

offset+length

and

buf.length

.
The buffer array is not copied. The buffer's mark is
set to the specified offset.

Method Detail

- read

```java
public int read()
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

is returned.

This

read

method
cannot block.

**Specified by:** read

in class

InputStream
**Returns:** the next byte of data, or

-1

if the end of the
stream has been reached.

- read

```java
public int read​(byte[] b,
int off,
int len)
```

Reads up to

len

bytes of data into an array of bytes from this
input stream. If

pos

equals

count

, then

-1

is
returned to indicate end of file. Otherwise, the number

k

of
bytes read is equal to the smaller of

len

and

count-pos

.
If

k

is positive, then bytes

buf[pos]

through

buf[pos+k-1]

are copied into

b[off]

through

b[off+k-1]

in the manner performed by

System.arraycopy

.
The value

k

is added into

pos

and

k

is returned.

This

read

method cannot block.

**Overrides:** read

in class

InputStream
**Parameters:** b

- the buffer into which the data is read.
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** NullPointerException

- If

b

is

null

.
**Throws:** IndexOutOfBoundsException

- If

off

is negative,

len

is negative, or

len

is greater than

b.length - off
**See Also:** InputStream.read()

- skip

```java
public long skip​(long n)
```

Skips

n

bytes of input from this input stream. Fewer
bytes might be skipped if the end of the input stream is reached.
The actual number

k

of bytes to be skipped is equal to the smaller
of

n

and

count-pos

.
The value

k

is added into

pos

and

k

is returned.

**Overrides:** skip

in class

InputStream
**Parameters:** n

- the number of bytes to be skipped.
**Returns:** the actual number of bytes skipped.

- available

```java
public int available()
```

Returns the number of remaining bytes that can be read (or skipped over)
from this input stream.

The value returned is

count - pos

,
which is the number of bytes remaining to be read from the input buffer.

**Overrides:** available

in class

InputStream
**Returns:** the number of remaining bytes that can be read (or skipped
over) from this input stream without blocking.

- markSupported

```java
public boolean markSupported()
```

Tests if this

InputStream

supports mark/reset. The

markSupported

method of

ByteArrayInputStream

always returns

true

.

**Overrides:** markSupported

in class

InputStream
**Returns:** true

if this stream instance supports the mark
and reset methods;

false

otherwise.
**Since:** 1.1
**See Also:** InputStream.mark(int)

,

InputStream.reset()

- mark

```java
public void mark​(int readAheadLimit)
```

Set the current marked position in the stream.
ByteArrayInputStream objects are marked at position zero by
default when constructed. They may be marked at another
position within the buffer by this method.

If no mark has been set, then the value of the mark is the
offset passed to the constructor (or 0 if the offset was not
supplied).

Note: The

readAheadLimit

for this class
has no meaning.

**Overrides:** mark

in class

InputStream
**Parameters:** readAheadLimit

- the maximum limit of bytes that can be read before
the mark position becomes invalid.
**Since:** 1.1
**See Also:** InputStream.reset()

- reset

```java
public void reset()
```

Resets the buffer to the marked position. The marked position
is 0 unless another position was marked or an offset was specified
in the constructor.

**Overrides:** reset

in class

InputStream
**See Also:** InputStream.mark(int)

,

IOException

- close

```java
public void close()
throws
IOException
```

Closing a

ByteArrayInputStream

has no effect. The methods in
this class can be called after the stream has been closed without
generating an

IOException

.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

InputStream
**Throws:** IOException

- if an I/O error occurs.

---

#### Method Detail

read

```java
public int read()
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

is returned.

This

read

method
cannot block.

**Specified by:** read

in class

InputStream
**Returns:** the next byte of data, or

-1

if the end of the
stream has been reached.

---

#### read

public int read()

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

is returned.

This

read

method
cannot block.

This

read

method
cannot block.

read

```java
public int read​(byte[] b,
int off,
int len)
```

Reads up to

len

bytes of data into an array of bytes from this
input stream. If

pos

equals

count

, then

-1

is
returned to indicate end of file. Otherwise, the number

k

of
bytes read is equal to the smaller of

len

and

count-pos

.
If

k

is positive, then bytes

buf[pos]

through

buf[pos+k-1]

are copied into

b[off]

through

b[off+k-1]

in the manner performed by

System.arraycopy

.
The value

k

is added into

pos

and

k

is returned.

This

read

method cannot block.

**Overrides:** read

in class

InputStream
**Parameters:** b

- the buffer into which the data is read.
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** NullPointerException

- If

b

is

null

.
**Throws:** IndexOutOfBoundsException

- If

off

is negative,

len

is negative, or

len

is greater than

b.length - off
**See Also:** InputStream.read()

---

#### read

public int read​(byte[] b,
int off,
int len)

Reads up to

len

bytes of data into an array of bytes from this
input stream. If

pos

equals

count

, then

-1

is
returned to indicate end of file. Otherwise, the number

k

of
bytes read is equal to the smaller of

len

and

count-pos

.
If

k

is positive, then bytes

buf[pos]

through

buf[pos+k-1]

are copied into

b[off]

through

b[off+k-1]

in the manner performed by

System.arraycopy

.
The value

k

is added into

pos

and

k

is returned.

This

read

method cannot block.

This

read

method cannot block.

skip

```java
public long skip​(long n)
```

Skips

n

bytes of input from this input stream. Fewer
bytes might be skipped if the end of the input stream is reached.
The actual number

k

of bytes to be skipped is equal to the smaller
of

n

and

count-pos

.
The value

k

is added into

pos

and

k

is returned.

**Overrides:** skip

in class

InputStream
**Parameters:** n

- the number of bytes to be skipped.
**Returns:** the actual number of bytes skipped.

---

#### skip

public long skip​(long n)

Skips

n

bytes of input from this input stream. Fewer
bytes might be skipped if the end of the input stream is reached.
The actual number

k

of bytes to be skipped is equal to the smaller
of

n

and

count-pos

.
The value

k

is added into

pos

and

k

is returned.

available

```java
public int available()
```

Returns the number of remaining bytes that can be read (or skipped over)
from this input stream.

The value returned is

count - pos

,
which is the number of bytes remaining to be read from the input buffer.

**Overrides:** available

in class

InputStream
**Returns:** the number of remaining bytes that can be read (or skipped
over) from this input stream without blocking.

---

#### available

public int available()

Returns the number of remaining bytes that can be read (or skipped over)
from this input stream.

The value returned is

count - pos

,
which is the number of bytes remaining to be read from the input buffer.

The value returned is

count - pos

,
which is the number of bytes remaining to be read from the input buffer.

markSupported

```java
public boolean markSupported()
```

Tests if this

InputStream

supports mark/reset. The

markSupported

method of

ByteArrayInputStream

always returns

true

.

**Overrides:** markSupported

in class

InputStream
**Returns:** true

if this stream instance supports the mark
and reset methods;

false

otherwise.
**Since:** 1.1
**See Also:** InputStream.mark(int)

,

InputStream.reset()

---

#### markSupported

public boolean markSupported()

Tests if this

InputStream

supports mark/reset. The

markSupported

method of

ByteArrayInputStream

always returns

true

.

mark

```java
public void mark​(int readAheadLimit)
```

Set the current marked position in the stream.
ByteArrayInputStream objects are marked at position zero by
default when constructed. They may be marked at another
position within the buffer by this method.

If no mark has been set, then the value of the mark is the
offset passed to the constructor (or 0 if the offset was not
supplied).

Note: The

readAheadLimit

for this class
has no meaning.

**Overrides:** mark

in class

InputStream
**Parameters:** readAheadLimit

- the maximum limit of bytes that can be read before
the mark position becomes invalid.
**Since:** 1.1
**See Also:** InputStream.reset()

---

#### mark

public void mark​(int readAheadLimit)

Set the current marked position in the stream.
ByteArrayInputStream objects are marked at position zero by
default when constructed. They may be marked at another
position within the buffer by this method.

If no mark has been set, then the value of the mark is the
offset passed to the constructor (or 0 if the offset was not
supplied).

Note: The

readAheadLimit

for this class
has no meaning.

If no mark has been set, then the value of the mark is the
offset passed to the constructor (or 0 if the offset was not
supplied).

Note: The

readAheadLimit

for this class
has no meaning.

Note: The

readAheadLimit

for this class
has no meaning.

reset

```java
public void reset()
```

Resets the buffer to the marked position. The marked position
is 0 unless another position was marked or an offset was specified
in the constructor.

**Overrides:** reset

in class

InputStream
**See Also:** InputStream.mark(int)

,

IOException

---

#### reset

public void reset()

Resets the buffer to the marked position. The marked position
is 0 unless another position was marked or an offset was specified
in the constructor.

close

```java
public void close()
throws
IOException
```

Closing a

ByteArrayInputStream

has no effect. The methods in
this class can be called after the stream has been closed without
generating an

IOException

.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

InputStream
**Throws:** IOException

- if an I/O error occurs.

---

#### close

public void close()
throws

IOException

Closing a

ByteArrayInputStream

has no effect. The methods in
this class can be called after the stream has been closed without
generating an

IOException

.

---

