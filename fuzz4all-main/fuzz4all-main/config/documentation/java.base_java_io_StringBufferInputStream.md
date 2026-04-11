# Class StringBufferInputStream

**Source:** `java.base\java\io\StringBufferInputStream.html`

### Class Description

```java
@Deprecated

public class
StringBufferInputStream

extends
InputStream
```

This class allows an application to create an input stream in
which the bytes read are supplied by the contents of a string.
Applications can also read bytes from a byte array by using a

ByteArrayInputStream

.

Only the low eight bits of each character in the string are used by
this class.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

#### protected
String
buffer

The string from which bytes are read.

---

#### protected int pos

The index of the next character to read from the input stream buffer.

**See Also:**
- buffer

---

#### protected int count

The number of valid characters in the input stream buffer.

**See Also:**
- buffer

---

### Constructor Details

#### public StringBufferInputStream​(
String
s)

Creates a string input stream to read data from the specified string.

**Parameters:**
- s

- the underlying input buffer.

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

The

read

method of

StringBufferInputStream

cannot block. It returns the
low eight bits of the next character in this input stream's buffer.

**Specified by:**
- read

in class

InputStream

**Returns:**
- the next byte of data, or

-1

if the end of the
stream is reached.

---

#### public int read​(byte[] b,
int off,
int len)

Reads up to

len

bytes of data from this input stream
into an array of bytes.

The

read

method of

StringBufferInputStream

cannot block. It copies the
low eight bits from the characters in this input stream's buffer into
the byte array argument.

**Overrides:**
- read

in class

InputStream

**Parameters:**
- b

- the buffer into which the data is read.
- off

- the start offset of the data.
- len

- the maximum number of bytes read.

**Returns:**
- the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.

**See Also:**
- InputStream.read()

---

#### public long skip​(long n)

Skips

n

bytes of input from this input stream. Fewer
bytes might be skipped if the end of the input stream is reached.

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

Returns the number of bytes that can be read from the input
stream without blocking.

**Overrides:**
- available

in class

InputStream

**Returns:**
- the value of

count - pos

, which is the
number of bytes remaining to be read from the input buffer.

---

#### public void reset()

Resets the input stream to begin reading from the first character
of this input stream's underlying buffer.

**Overrides:**
- reset

in class

InputStream

**See Also:**
- InputStream.mark(int)

,

IOException

---

### Additional Sections

#### Class StringBufferInputStream

java.lang.Object

- java.io.InputStream
- - java.io.StringBufferInputStream

java.io.InputStream

- java.io.StringBufferInputStream

java.io.StringBufferInputStream

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
@Deprecated

public class
StringBufferInputStream

extends
InputStream
```

Deprecated.

This class does not properly convert characters into bytes. As
of JDK 1.1, the preferred way to create a stream from a
string is via the

StringReader

class.

This class allows an application to create an input stream in
which the bytes read are supplied by the contents of a string.
Applications can also read bytes from a byte array by using a

ByteArrayInputStream

.

Only the low eight bits of each character in the string are used by
this class.

**Since:** 1.0
**See Also:** ByteArrayInputStream

,

StringReader

@Deprecated

public class

StringBufferInputStream

extends

InputStream

This class allows an application to create an input stream in
which the bytes read are supplied by the contents of a string.
Applications can also read bytes from a byte array by using a

ByteArrayInputStream

.

Only the low eight bits of each character in the string are used by
this class.

Only the low eight bits of each character in the string are used by
this class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

String

buffer

Deprecated.

The string from which bytes are read.

protected int

count

Deprecated.

The number of valid characters in the input stream buffer.

protected int

pos

Deprecated.

The index of the next character to read from the input stream buffer.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StringBufferInputStream

​(

String

s)

Deprecated.

Creates a string input stream to read data from the specified string.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

int

available

()

Deprecated.

Returns the number of bytes that can be read from the input
stream without blocking.

int

read

()

Deprecated.

Reads the next byte of data from this input stream.

int

read

​(byte[] b,
int off,
int len)

Deprecated.

Reads up to

len

bytes of data from this input stream
into an array of bytes.

void

reset

()

Deprecated.

Resets the input stream to begin reading from the first character
of this input stream's underlying buffer.

long

skip

​(long n)

Deprecated.

Skips

n

bytes of input from this input stream.

- Methods declared in class java.io.

InputStream

close

,

mark

,

markSupported

,

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

protected

String

buffer

Deprecated.

The string from which bytes are read.

protected int

count

Deprecated.

The number of valid characters in the input stream buffer.

protected int

pos

Deprecated.

The index of the next character to read from the input stream buffer.

---

#### Field Summary

Deprecated.

The string from which bytes are read.

The number of valid characters in the input stream buffer.

The index of the next character to read from the input stream buffer.

Constructor Summary

Constructors

Constructor

Description

StringBufferInputStream

​(

String

s)

Deprecated.

Creates a string input stream to read data from the specified string.

---

#### Constructor Summary

Deprecated.

Creates a string input stream to read data from the specified string.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

int

available

()

Deprecated.

Returns the number of bytes that can be read from the input
stream without blocking.

int

read

()

Deprecated.

Reads the next byte of data from this input stream.

int

read

​(byte[] b,
int off,
int len)

Deprecated.

Reads up to

len

bytes of data from this input stream
into an array of bytes.

void

reset

()

Deprecated.

Resets the input stream to begin reading from the first character
of this input stream's underlying buffer.

long

skip

​(long n)

Deprecated.

Skips

n

bytes of input from this input stream.

- Methods declared in class java.io.

InputStream

close

,

mark

,

markSupported

,

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

Deprecated.

Returns the number of bytes that can be read from the input
stream without blocking.

Reads the next byte of data from this input stream.

Reads up to

len

bytes of data from this input stream
into an array of bytes.

Resets the input stream to begin reading from the first character
of this input stream's underlying buffer.

Skips

n

bytes of input from this input stream.

Methods declared in class java.io.

InputStream

close

,

mark

,

markSupported

,

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

- buffer

```java
protected
String
buffer
```

Deprecated.

The string from which bytes are read.

- pos

```java
protected int pos
```

Deprecated.

The index of the next character to read from the input stream buffer.

**See Also:** buffer

- count

```java
protected int count
```

Deprecated.

The number of valid characters in the input stream buffer.

**See Also:** buffer

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StringBufferInputStream

```java
public StringBufferInputStream​(
String
s)
```

Deprecated.

Creates a string input stream to read data from the specified string.

**Parameters:** s

- the underlying input buffer.

============ METHOD DETAIL ==========

- Method Detail

- read

```java
public int read()
```

Deprecated.

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

The

read

method of

StringBufferInputStream

cannot block. It returns the
low eight bits of the next character in this input stream's buffer.

**Specified by:** read

in class

InputStream
**Returns:** the next byte of data, or

-1

if the end of the
stream is reached.

- read

```java
public int read​(byte[] b,
int off,
int len)
```

Deprecated.

Reads up to

len

bytes of data from this input stream
into an array of bytes.

The

read

method of

StringBufferInputStream

cannot block. It copies the
low eight bits from the characters in this input stream's buffer into
the byte array argument.

**Overrides:** read

in class

InputStream
**Parameters:** b

- the buffer into which the data is read.
**Parameters:** off

- the start offset of the data.
**Parameters:** len

- the maximum number of bytes read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**See Also:** InputStream.read()

- skip

```java
public long skip​(long n)
```

Deprecated.

Skips

n

bytes of input from this input stream. Fewer
bytes might be skipped if the end of the input stream is reached.

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

Deprecated.

Returns the number of bytes that can be read from the input
stream without blocking.

**Overrides:** available

in class

InputStream
**Returns:** the value of

count - pos

, which is the
number of bytes remaining to be read from the input buffer.

- reset

```java
public void reset()
```

Deprecated.

Resets the input stream to begin reading from the first character
of this input stream's underlying buffer.

**Overrides:** reset

in class

InputStream
**See Also:** InputStream.mark(int)

,

IOException

Field Detail

- buffer

```java
protected
String
buffer
```

Deprecated.

The string from which bytes are read.

- pos

```java
protected int pos
```

Deprecated.

The index of the next character to read from the input stream buffer.

**See Also:** buffer

- count

```java
protected int count
```

Deprecated.

The number of valid characters in the input stream buffer.

**See Also:** buffer

---

#### Field Detail

buffer

```java
protected
String
buffer
```

Deprecated.

The string from which bytes are read.

---

#### buffer

protected

String

buffer

The string from which bytes are read.

pos

```java
protected int pos
```

Deprecated.

The index of the next character to read from the input stream buffer.

**See Also:** buffer

---

#### pos

protected int pos

The index of the next character to read from the input stream buffer.

count

```java
protected int count
```

Deprecated.

The number of valid characters in the input stream buffer.

**See Also:** buffer

---

#### count

protected int count

The number of valid characters in the input stream buffer.

Constructor Detail

- StringBufferInputStream

```java
public StringBufferInputStream​(
String
s)
```

Deprecated.

Creates a string input stream to read data from the specified string.

**Parameters:** s

- the underlying input buffer.

---

#### Constructor Detail

StringBufferInputStream

```java
public StringBufferInputStream​(
String
s)
```

Deprecated.

Creates a string input stream to read data from the specified string.

**Parameters:** s

- the underlying input buffer.

---

#### StringBufferInputStream

public StringBufferInputStream​(

String

s)

Creates a string input stream to read data from the specified string.

Method Detail

- read

```java
public int read()
```

Deprecated.

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

The

read

method of

StringBufferInputStream

cannot block. It returns the
low eight bits of the next character in this input stream's buffer.

**Specified by:** read

in class

InputStream
**Returns:** the next byte of data, or

-1

if the end of the
stream is reached.

- read

```java
public int read​(byte[] b,
int off,
int len)
```

Deprecated.

Reads up to

len

bytes of data from this input stream
into an array of bytes.

The

read

method of

StringBufferInputStream

cannot block. It copies the
low eight bits from the characters in this input stream's buffer into
the byte array argument.

**Overrides:** read

in class

InputStream
**Parameters:** b

- the buffer into which the data is read.
**Parameters:** off

- the start offset of the data.
**Parameters:** len

- the maximum number of bytes read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**See Also:** InputStream.read()

- skip

```java
public long skip​(long n)
```

Deprecated.

Skips

n

bytes of input from this input stream. Fewer
bytes might be skipped if the end of the input stream is reached.

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

Deprecated.

Returns the number of bytes that can be read from the input
stream without blocking.

**Overrides:** available

in class

InputStream
**Returns:** the value of

count - pos

, which is the
number of bytes remaining to be read from the input buffer.

- reset

```java
public void reset()
```

Deprecated.

Resets the input stream to begin reading from the first character
of this input stream's underlying buffer.

**Overrides:** reset

in class

InputStream
**See Also:** InputStream.mark(int)

,

IOException

---

#### Method Detail

read

```java
public int read()
```

Deprecated.

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

The

read

method of

StringBufferInputStream

cannot block. It returns the
low eight bits of the next character in this input stream's buffer.

**Specified by:** read

in class

InputStream
**Returns:** the next byte of data, or

-1

if the end of the
stream is reached.

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

The

read

method of

StringBufferInputStream

cannot block. It returns the
low eight bits of the next character in this input stream's buffer.

The

read

method of

StringBufferInputStream

cannot block. It returns the
low eight bits of the next character in this input stream's buffer.

read

```java
public int read​(byte[] b,
int off,
int len)
```

Deprecated.

Reads up to

len

bytes of data from this input stream
into an array of bytes.

The

read

method of

StringBufferInputStream

cannot block. It copies the
low eight bits from the characters in this input stream's buffer into
the byte array argument.

**Overrides:** read

in class

InputStream
**Parameters:** b

- the buffer into which the data is read.
**Parameters:** off

- the start offset of the data.
**Parameters:** len

- the maximum number of bytes read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**See Also:** InputStream.read()

---

#### read

public int read​(byte[] b,
int off,
int len)

Reads up to

len

bytes of data from this input stream
into an array of bytes.

The

read

method of

StringBufferInputStream

cannot block. It copies the
low eight bits from the characters in this input stream's buffer into
the byte array argument.

The

read

method of

StringBufferInputStream

cannot block. It copies the
low eight bits from the characters in this input stream's buffer into
the byte array argument.

skip

```java
public long skip​(long n)
```

Deprecated.

Skips

n

bytes of input from this input stream. Fewer
bytes might be skipped if the end of the input stream is reached.

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

available

```java
public int available()
```

Deprecated.

Returns the number of bytes that can be read from the input
stream without blocking.

**Overrides:** available

in class

InputStream
**Returns:** the value of

count - pos

, which is the
number of bytes remaining to be read from the input buffer.

---

#### available

public int available()

Returns the number of bytes that can be read from the input
stream without blocking.

reset

```java
public void reset()
```

Deprecated.

Resets the input stream to begin reading from the first character
of this input stream's underlying buffer.

**Overrides:** reset

in class

InputStream
**See Also:** InputStream.mark(int)

,

IOException

---

#### reset

public void reset()

Resets the input stream to begin reading from the first character
of this input stream's underlying buffer.

---

