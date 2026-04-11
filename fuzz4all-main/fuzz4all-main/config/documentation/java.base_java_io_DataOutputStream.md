# Class DataOutputStream

**Source:** `java.base\java\io\DataOutputStream.html`

### Class Description

```java
public class
DataOutputStream

extends
FilterOutputStream

implements
DataOutput
```

A data output stream lets an application write primitive Java data
types to an output stream in a portable way. An application can
then use a data input stream to read the data back in.

**All Implemented Interfaces:** Closeable

,

DataOutput

,

Flushable

,

AutoCloseable

---

### Field Details

#### protected int written

The number of bytes written to the data output stream so far.
If this counter overflows, it will be wrapped to Integer.MAX_VALUE.

---

### Constructor Details

#### public DataOutputStream​(
OutputStream
out)

Creates a new data output stream to write data to the specified
underlying output stream. The counter

written

is
set to zero.

**Parameters:**
- out

- the underlying output stream, to be saved for later
use.

**See Also:**
- FilterOutputStream.out

---

### Method Details

#### public void write​(int b)
throws
IOException

Writes the specified byte (the low eight bits of the argument

b

) to the underlying output stream. If no exception
is thrown, the counter

written

is incremented by

1

.

Implements the

write

method of

OutputStream

.

**Specified by:**
- write

in interface

DataOutput

**Overrides:**
- write

in class

FilterOutputStream

**Parameters:**
- b

- the

byte

to be written.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.out

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

to the underlying output stream.
If no exception is thrown, the counter

written

is
incremented by

len

.

**Specified by:**
- write

in interface

DataOutput

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
- FilterOutputStream.out

---

#### public void flush()
throws
IOException

Flushes this data output stream. This forces any buffered output
bytes to be written out to the stream.

The

flush

method of

DataOutputStream

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

FilterOutputStream

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.out

,

OutputStream.flush()

---

#### public final void writeBoolean​(boolean v)
throws
IOException

Writes a

boolean

to the underlying output stream as
a 1-byte value. The value

true

is written out as the
value

(byte)1

; the value

false

is
written out as the value

(byte)0

. If no exception is
thrown, the counter

written

is incremented by

1

.

**Specified by:**
- writeBoolean

in interface

DataOutput

**Parameters:**
- v

- a

boolean

value to be written.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.out

---

#### public final void writeByte​(int v)
throws
IOException

Writes out a

byte

to the underlying output stream as
a 1-byte value. If no exception is thrown, the counter

written

is incremented by

1

.

**Specified by:**
- writeByte

in interface

DataOutput

**Parameters:**
- v

- a

byte

value to be written.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.out

---

#### public final void writeShort​(int v)
throws
IOException

Writes a

short

to the underlying output stream as two
bytes, high byte first. If no exception is thrown, the counter

written

is incremented by

2

.

**Specified by:**
- writeShort

in interface

DataOutput

**Parameters:**
- v

- a

short

to be written.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.out

---

#### public final void writeChar​(int v)
throws
IOException

Writes a

char

to the underlying output stream as a
2-byte value, high byte first. If no exception is thrown, the
counter

written

is incremented by

2

.

**Specified by:**
- writeChar

in interface

DataOutput

**Parameters:**
- v

- a

char

value to be written.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.out

---

#### public final void writeInt​(int v)
throws
IOException

Writes an

int

to the underlying output stream as four
bytes, high byte first. If no exception is thrown, the counter

written

is incremented by

4

.

**Specified by:**
- writeInt

in interface

DataOutput

**Parameters:**
- v

- an

int

to be written.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.out

---

#### public final void writeLong​(long v)
throws
IOException

Writes a

long

to the underlying output stream as eight
bytes, high byte first. In no exception is thrown, the counter

written

is incremented by

8

.

**Specified by:**
- writeLong

in interface

DataOutput

**Parameters:**
- v

- a

long

to be written.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.out

---

#### public final void writeFloat​(float v)
throws
IOException

Converts the float argument to an

int

using the

floatToIntBits

method in class

Float

,
and then writes that

int

value to the underlying
output stream as a 4-byte quantity, high byte first. If no
exception is thrown, the counter

written

is
incremented by

4

.

**Specified by:**
- writeFloat

in interface

DataOutput

**Parameters:**
- v

- a

float

value to be written.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.out

,

Float.floatToIntBits(float)

---

#### public final void writeDouble​(double v)
throws
IOException

Converts the double argument to a

long

using the

doubleToLongBits

method in class

Double

,
and then writes that

long

value to the underlying
output stream as an 8-byte quantity, high byte first. If no
exception is thrown, the counter

written

is
incremented by

8

.

**Specified by:**
- writeDouble

in interface

DataOutput

**Parameters:**
- v

- a

double

value to be written.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.out

,

Double.doubleToLongBits(double)

---

#### public final void writeBytes​(
String
s)
throws
IOException

Writes out the string to the underlying output stream as a
sequence of bytes. Each character in the string is written out, in
sequence, by discarding its high eight bits. If no exception is
thrown, the counter

written

is incremented by the
length of

s

.

**Specified by:**
- writeBytes

in interface

DataOutput

**Parameters:**
- s

- a string of bytes to be written.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterOutputStream.out

---

#### public final void writeChars​(
String
s)
throws
IOException

Writes a string to the underlying output stream as a sequence of
characters. Each character is written to the data output stream as
if by the

writeChar

method. If no exception is
thrown, the counter

written

is incremented by twice
the length of

s

.

**Specified by:**
- writeChars

in interface

DataOutput

**Parameters:**
- s

- a

String

value to be written.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- writeChar(int)

,

FilterOutputStream.out

---

#### public final void writeUTF​(
String
str)
throws
IOException

Writes a string to the underlying output stream using

modified UTF-8

encoding in a machine-independent manner.

First, two bytes are written to the output stream as if by the

writeShort

method giving the number of bytes to
follow. This value is the number of bytes actually written out,
not the length of the string. Following the length, each character
of the string is output, in sequence, using the modified UTF-8 encoding
for the character. If no exception is thrown, the counter

written

is incremented by the total number of
bytes written to the output stream. This will be at least two
plus the length of

str

, and at most two plus
thrice the length of

str

.

**Specified by:**
- writeUTF

in interface

DataOutput

**Parameters:**
- str

- a string to be written.

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public final int size()

Returns the current value of the counter

written

,
the number of bytes written to this data output stream so far.
If the counter overflows, it will be wrapped to Integer.MAX_VALUE.

**Returns:**
- the value of the

written

field.

**See Also:**
- written

---

### Additional Sections

#### Class DataOutputStream

java.lang.Object

- java.io.OutputStream
- - java.io.FilterOutputStream
- - java.io.DataOutputStream

java.io.OutputStream

- java.io.FilterOutputStream
- - java.io.DataOutputStream

java.io.FilterOutputStream

- java.io.DataOutputStream

java.io.DataOutputStream

**All Implemented Interfaces:** Closeable

,

DataOutput

,

Flushable

,

AutoCloseable

```java
public class
DataOutputStream

extends
FilterOutputStream

implements
DataOutput
```

A data output stream lets an application write primitive Java data
types to an output stream in a portable way. An application can
then use a data input stream to read the data back in.

**Since:** 1.0
**See Also:** DataInputStream

public class

DataOutputStream

extends

FilterOutputStream

implements

DataOutput

A data output stream lets an application write primitive Java data
types to an output stream in a portable way. An application can
then use a data input stream to read the data back in.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

written

The number of bytes written to the data output stream so far.

- Fields declared in class java.io.

FilterOutputStream

out

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DataOutputStream

​(

OutputStream

out)

Creates a new data output stream to write data to the specified
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

flush

()

Flushes this data output stream.

int

size

()

Returns the current value of the counter

written

,
the number of bytes written to this data output stream so far.

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

to the underlying output stream.

void

write

​(int b)

Writes the specified byte (the low eight bits of the argument

b

) to the underlying output stream.

void

writeBoolean

​(boolean v)

Writes a

boolean

to the underlying output stream as
a 1-byte value.

void

writeByte

​(int v)

Writes out a

byte

to the underlying output stream as
a 1-byte value.

void

writeBytes

​(

String

s)

Writes out the string to the underlying output stream as a
sequence of bytes.

void

writeChar

​(int v)

Writes a

char

to the underlying output stream as a
2-byte value, high byte first.

void

writeChars

​(

String

s)

Writes a string to the underlying output stream as a sequence of
characters.

void

writeDouble

​(double v)

Converts the double argument to a

long

using the

doubleToLongBits

method in class

Double

,
and then writes that

long

value to the underlying
output stream as an 8-byte quantity, high byte first.

void

writeFloat

​(float v)

Converts the float argument to an

int

using the

floatToIntBits

method in class

Float

,
and then writes that

int

value to the underlying
output stream as a 4-byte quantity, high byte first.

void

writeInt

​(int v)

Writes an

int

to the underlying output stream as four
bytes, high byte first.

void

writeLong

​(long v)

Writes a

long

to the underlying output stream as eight
bytes, high byte first.

void

writeShort

​(int v)

Writes a

short

to the underlying output stream as two
bytes, high byte first.

void

writeUTF

​(

String

str)

Writes a string to the underlying output stream using

modified UTF-8

encoding in a machine-independent manner.

- Methods declared in class java.io.

FilterOutputStream

close

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.io.

DataOutput

write

Field Summary

Fields

Modifier and Type

Field

Description

protected int

written

The number of bytes written to the data output stream so far.

- Fields declared in class java.io.

FilterOutputStream

out

---

#### Field Summary

The number of bytes written to the data output stream so far.

Fields declared in class java.io.

FilterOutputStream

out

---

#### Fields declared in class java.io. FilterOutputStream

Constructor Summary

Constructors

Constructor

Description

DataOutputStream

​(

OutputStream

out)

Creates a new data output stream to write data to the specified
underlying output stream.

---

#### Constructor Summary

Creates a new data output stream to write data to the specified
underlying output stream.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

flush

()

Flushes this data output stream.

int

size

()

Returns the current value of the counter

written

,
the number of bytes written to this data output stream so far.

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

to the underlying output stream.

void

write

​(int b)

Writes the specified byte (the low eight bits of the argument

b

) to the underlying output stream.

void

writeBoolean

​(boolean v)

Writes a

boolean

to the underlying output stream as
a 1-byte value.

void

writeByte

​(int v)

Writes out a

byte

to the underlying output stream as
a 1-byte value.

void

writeBytes

​(

String

s)

Writes out the string to the underlying output stream as a
sequence of bytes.

void

writeChar

​(int v)

Writes a

char

to the underlying output stream as a
2-byte value, high byte first.

void

writeChars

​(

String

s)

Writes a string to the underlying output stream as a sequence of
characters.

void

writeDouble

​(double v)

Converts the double argument to a

long

using the

doubleToLongBits

method in class

Double

,
and then writes that

long

value to the underlying
output stream as an 8-byte quantity, high byte first.

void

writeFloat

​(float v)

Converts the float argument to an

int

using the

floatToIntBits

method in class

Float

,
and then writes that

int

value to the underlying
output stream as a 4-byte quantity, high byte first.

void

writeInt

​(int v)

Writes an

int

to the underlying output stream as four
bytes, high byte first.

void

writeLong

​(long v)

Writes a

long

to the underlying output stream as eight
bytes, high byte first.

void

writeShort

​(int v)

Writes a

short

to the underlying output stream as two
bytes, high byte first.

void

writeUTF

​(

String

str)

Writes a string to the underlying output stream using

modified UTF-8

encoding in a machine-independent manner.

- Methods declared in class java.io.

FilterOutputStream

close

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.io.

DataOutput

write

---

#### Method Summary

Flushes this data output stream.

Returns the current value of the counter

written

,
the number of bytes written to this data output stream so far.

Writes

len

bytes from the specified byte array
starting at offset

off

to the underlying output stream.

Writes the specified byte (the low eight bits of the argument

b

) to the underlying output stream.

Writes a

boolean

to the underlying output stream as
a 1-byte value.

Writes out a

byte

to the underlying output stream as
a 1-byte value.

Writes out the string to the underlying output stream as a
sequence of bytes.

Writes a

char

to the underlying output stream as a
2-byte value, high byte first.

Writes a string to the underlying output stream as a sequence of
characters.

Converts the double argument to a

long

using the

doubleToLongBits

method in class

Double

,
and then writes that

long

value to the underlying
output stream as an 8-byte quantity, high byte first.

Converts the float argument to an

int

using the

floatToIntBits

method in class

Float

,
and then writes that

int

value to the underlying
output stream as a 4-byte quantity, high byte first.

Writes an

int

to the underlying output stream as four
bytes, high byte first.

Writes a

long

to the underlying output stream as eight
bytes, high byte first.

Writes a

short

to the underlying output stream as two
bytes, high byte first.

Writes a string to the underlying output stream using

modified UTF-8

encoding in a machine-independent manner.

Methods declared in class java.io.

FilterOutputStream

close

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

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.io.

DataOutput

write

---

#### Methods declared in interface java.io. DataOutput

============ FIELD DETAIL ===========

- Field Detail

- written

```java
protected int written
```

The number of bytes written to the data output stream so far.
If this counter overflows, it will be wrapped to Integer.MAX_VALUE.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DataOutputStream

```java
public DataOutputStream​(
OutputStream
out)
```

Creates a new data output stream to write data to the specified
underlying output stream. The counter

written

is
set to zero.

**Parameters:** out

- the underlying output stream, to be saved for later
use.
**See Also:** FilterOutputStream.out

============ METHOD DETAIL ==========

- Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes the specified byte (the low eight bits of the argument

b

) to the underlying output stream. If no exception
is thrown, the counter

written

is incremented by

1

.

Implements the

write

method of

OutputStream

.

**Specified by:** write

in interface

DataOutput
**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the

byte

to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

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

to the underlying output stream.
If no exception is thrown, the counter

written

is
incremented by

len

.

**Specified by:** write

in interface

DataOutput
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
**See Also:** FilterOutputStream.out

- flush

```java
public void flush()
throws
IOException
```

Flushes this data output stream. This forces any buffered output
bytes to be written out to the stream.

The

flush

method of

DataOutputStream

calls the

flush

method of its underlying output stream.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

,

OutputStream.flush()

- writeBoolean

```java
public final void writeBoolean​(boolean v)
throws
IOException
```

Writes a

boolean

to the underlying output stream as
a 1-byte value. The value

true

is written out as the
value

(byte)1

; the value

false

is
written out as the value

(byte)0

. If no exception is
thrown, the counter

written

is incremented by

1

.

**Specified by:** writeBoolean

in interface

DataOutput
**Parameters:** v

- a

boolean

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeByte

```java
public final void writeByte​(int v)
throws
IOException
```

Writes out a

byte

to the underlying output stream as
a 1-byte value. If no exception is thrown, the counter

written

is incremented by

1

.

**Specified by:** writeByte

in interface

DataOutput
**Parameters:** v

- a

byte

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeShort

```java
public final void writeShort​(int v)
throws
IOException
```

Writes a

short

to the underlying output stream as two
bytes, high byte first. If no exception is thrown, the counter

written

is incremented by

2

.

**Specified by:** writeShort

in interface

DataOutput
**Parameters:** v

- a

short

to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeChar

```java
public final void writeChar​(int v)
throws
IOException
```

Writes a

char

to the underlying output stream as a
2-byte value, high byte first. If no exception is thrown, the
counter

written

is incremented by

2

.

**Specified by:** writeChar

in interface

DataOutput
**Parameters:** v

- a

char

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeInt

```java
public final void writeInt​(int v)
throws
IOException
```

Writes an

int

to the underlying output stream as four
bytes, high byte first. If no exception is thrown, the counter

written

is incremented by

4

.

**Specified by:** writeInt

in interface

DataOutput
**Parameters:** v

- an

int

to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeLong

```java
public final void writeLong​(long v)
throws
IOException
```

Writes a

long

to the underlying output stream as eight
bytes, high byte first. In no exception is thrown, the counter

written

is incremented by

8

.

**Specified by:** writeLong

in interface

DataOutput
**Parameters:** v

- a

long

to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeFloat

```java
public final void writeFloat​(float v)
throws
IOException
```

Converts the float argument to an

int

using the

floatToIntBits

method in class

Float

,
and then writes that

int

value to the underlying
output stream as a 4-byte quantity, high byte first. If no
exception is thrown, the counter

written

is
incremented by

4

.

**Specified by:** writeFloat

in interface

DataOutput
**Parameters:** v

- a

float

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

,

Float.floatToIntBits(float)

- writeDouble

```java
public final void writeDouble​(double v)
throws
IOException
```

Converts the double argument to a

long

using the

doubleToLongBits

method in class

Double

,
and then writes that

long

value to the underlying
output stream as an 8-byte quantity, high byte first. If no
exception is thrown, the counter

written

is
incremented by

8

.

**Specified by:** writeDouble

in interface

DataOutput
**Parameters:** v

- a

double

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

,

Double.doubleToLongBits(double)

- writeBytes

```java
public final void writeBytes​(
String
s)
throws
IOException
```

Writes out the string to the underlying output stream as a
sequence of bytes. Each character in the string is written out, in
sequence, by discarding its high eight bits. If no exception is
thrown, the counter

written

is incremented by the
length of

s

.

**Specified by:** writeBytes

in interface

DataOutput
**Parameters:** s

- a string of bytes to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeChars

```java
public final void writeChars​(
String
s)
throws
IOException
```

Writes a string to the underlying output stream as a sequence of
characters. Each character is written to the data output stream as
if by the

writeChar

method. If no exception is
thrown, the counter

written

is incremented by twice
the length of

s

.

**Specified by:** writeChars

in interface

DataOutput
**Parameters:** s

- a

String

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** writeChar(int)

,

FilterOutputStream.out

- writeUTF

```java
public final void writeUTF​(
String
str)
throws
IOException
```

Writes a string to the underlying output stream using

modified UTF-8

encoding in a machine-independent manner.

First, two bytes are written to the output stream as if by the

writeShort

method giving the number of bytes to
follow. This value is the number of bytes actually written out,
not the length of the string. Following the length, each character
of the string is output, in sequence, using the modified UTF-8 encoding
for the character. If no exception is thrown, the counter

written

is incremented by the total number of
bytes written to the output stream. This will be at least two
plus the length of

str

, and at most two plus
thrice the length of

str

.

**Specified by:** writeUTF

in interface

DataOutput
**Parameters:** str

- a string to be written.
**Throws:** IOException

- if an I/O error occurs.

- size

```java
public final int size()
```

Returns the current value of the counter

written

,
the number of bytes written to this data output stream so far.
If the counter overflows, it will be wrapped to Integer.MAX_VALUE.

**Returns:** the value of the

written

field.
**See Also:** written

Field Detail

- written

```java
protected int written
```

The number of bytes written to the data output stream so far.
If this counter overflows, it will be wrapped to Integer.MAX_VALUE.

---

#### Field Detail

written

```java
protected int written
```

The number of bytes written to the data output stream so far.
If this counter overflows, it will be wrapped to Integer.MAX_VALUE.

---

#### written

protected int written

The number of bytes written to the data output stream so far.
If this counter overflows, it will be wrapped to Integer.MAX_VALUE.

Constructor Detail

- DataOutputStream

```java
public DataOutputStream​(
OutputStream
out)
```

Creates a new data output stream to write data to the specified
underlying output stream. The counter

written

is
set to zero.

**Parameters:** out

- the underlying output stream, to be saved for later
use.
**See Also:** FilterOutputStream.out

---

#### Constructor Detail

DataOutputStream

```java
public DataOutputStream​(
OutputStream
out)
```

Creates a new data output stream to write data to the specified
underlying output stream. The counter

written

is
set to zero.

**Parameters:** out

- the underlying output stream, to be saved for later
use.
**See Also:** FilterOutputStream.out

---

#### DataOutputStream

public DataOutputStream​(

OutputStream

out)

Creates a new data output stream to write data to the specified
underlying output stream. The counter

written

is
set to zero.

Method Detail

- write

```java
public void write​(int b)
throws
IOException
```

Writes the specified byte (the low eight bits of the argument

b

) to the underlying output stream. If no exception
is thrown, the counter

written

is incremented by

1

.

Implements the

write

method of

OutputStream

.

**Specified by:** write

in interface

DataOutput
**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the

byte

to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

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

to the underlying output stream.
If no exception is thrown, the counter

written

is
incremented by

len

.

**Specified by:** write

in interface

DataOutput
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
**See Also:** FilterOutputStream.out

- flush

```java
public void flush()
throws
IOException
```

Flushes this data output stream. This forces any buffered output
bytes to be written out to the stream.

The

flush

method of

DataOutputStream

calls the

flush

method of its underlying output stream.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

,

OutputStream.flush()

- writeBoolean

```java
public final void writeBoolean​(boolean v)
throws
IOException
```

Writes a

boolean

to the underlying output stream as
a 1-byte value. The value

true

is written out as the
value

(byte)1

; the value

false

is
written out as the value

(byte)0

. If no exception is
thrown, the counter

written

is incremented by

1

.

**Specified by:** writeBoolean

in interface

DataOutput
**Parameters:** v

- a

boolean

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeByte

```java
public final void writeByte​(int v)
throws
IOException
```

Writes out a

byte

to the underlying output stream as
a 1-byte value. If no exception is thrown, the counter

written

is incremented by

1

.

**Specified by:** writeByte

in interface

DataOutput
**Parameters:** v

- a

byte

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeShort

```java
public final void writeShort​(int v)
throws
IOException
```

Writes a

short

to the underlying output stream as two
bytes, high byte first. If no exception is thrown, the counter

written

is incremented by

2

.

**Specified by:** writeShort

in interface

DataOutput
**Parameters:** v

- a

short

to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeChar

```java
public final void writeChar​(int v)
throws
IOException
```

Writes a

char

to the underlying output stream as a
2-byte value, high byte first. If no exception is thrown, the
counter

written

is incremented by

2

.

**Specified by:** writeChar

in interface

DataOutput
**Parameters:** v

- a

char

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeInt

```java
public final void writeInt​(int v)
throws
IOException
```

Writes an

int

to the underlying output stream as four
bytes, high byte first. If no exception is thrown, the counter

written

is incremented by

4

.

**Specified by:** writeInt

in interface

DataOutput
**Parameters:** v

- an

int

to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeLong

```java
public final void writeLong​(long v)
throws
IOException
```

Writes a

long

to the underlying output stream as eight
bytes, high byte first. In no exception is thrown, the counter

written

is incremented by

8

.

**Specified by:** writeLong

in interface

DataOutput
**Parameters:** v

- a

long

to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeFloat

```java
public final void writeFloat​(float v)
throws
IOException
```

Converts the float argument to an

int

using the

floatToIntBits

method in class

Float

,
and then writes that

int

value to the underlying
output stream as a 4-byte quantity, high byte first. If no
exception is thrown, the counter

written

is
incremented by

4

.

**Specified by:** writeFloat

in interface

DataOutput
**Parameters:** v

- a

float

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

,

Float.floatToIntBits(float)

- writeDouble

```java
public final void writeDouble​(double v)
throws
IOException
```

Converts the double argument to a

long

using the

doubleToLongBits

method in class

Double

,
and then writes that

long

value to the underlying
output stream as an 8-byte quantity, high byte first. If no
exception is thrown, the counter

written

is
incremented by

8

.

**Specified by:** writeDouble

in interface

DataOutput
**Parameters:** v

- a

double

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

,

Double.doubleToLongBits(double)

- writeBytes

```java
public final void writeBytes​(
String
s)
throws
IOException
```

Writes out the string to the underlying output stream as a
sequence of bytes. Each character in the string is written out, in
sequence, by discarding its high eight bits. If no exception is
thrown, the counter

written

is incremented by the
length of

s

.

**Specified by:** writeBytes

in interface

DataOutput
**Parameters:** s

- a string of bytes to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

- writeChars

```java
public final void writeChars​(
String
s)
throws
IOException
```

Writes a string to the underlying output stream as a sequence of
characters. Each character is written to the data output stream as
if by the

writeChar

method. If no exception is
thrown, the counter

written

is incremented by twice
the length of

s

.

**Specified by:** writeChars

in interface

DataOutput
**Parameters:** s

- a

String

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** writeChar(int)

,

FilterOutputStream.out

- writeUTF

```java
public final void writeUTF​(
String
str)
throws
IOException
```

Writes a string to the underlying output stream using

modified UTF-8

encoding in a machine-independent manner.

First, two bytes are written to the output stream as if by the

writeShort

method giving the number of bytes to
follow. This value is the number of bytes actually written out,
not the length of the string. Following the length, each character
of the string is output, in sequence, using the modified UTF-8 encoding
for the character. If no exception is thrown, the counter

written

is incremented by the total number of
bytes written to the output stream. This will be at least two
plus the length of

str

, and at most two plus
thrice the length of

str

.

**Specified by:** writeUTF

in interface

DataOutput
**Parameters:** str

- a string to be written.
**Throws:** IOException

- if an I/O error occurs.

- size

```java
public final int size()
```

Returns the current value of the counter

written

,
the number of bytes written to this data output stream so far.
If the counter overflows, it will be wrapped to Integer.MAX_VALUE.

**Returns:** the value of the

written

field.
**See Also:** written

---

#### Method Detail

write

```java
public void write​(int b)
throws
IOException
```

Writes the specified byte (the low eight bits of the argument

b

) to the underlying output stream. If no exception
is thrown, the counter

written

is incremented by

1

.

Implements the

write

method of

OutputStream

.

**Specified by:** write

in interface

DataOutput
**Overrides:** write

in class

FilterOutputStream
**Parameters:** b

- the

byte

to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

---

#### write

public void write​(int b)
throws

IOException

Writes the specified byte (the low eight bits of the argument

b

) to the underlying output stream. If no exception
is thrown, the counter

written

is incremented by

1

.

Implements the

write

method of

OutputStream

.

Implements the

write

method of

OutputStream

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

to the underlying output stream.
If no exception is thrown, the counter

written

is
incremented by

len

.

**Specified by:** write

in interface

DataOutput
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
**See Also:** FilterOutputStream.out

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

to the underlying output stream.
If no exception is thrown, the counter

written

is
incremented by

len

.

flush

```java
public void flush()
throws
IOException
```

Flushes this data output stream. This forces any buffered output
bytes to be written out to the stream.

The

flush

method of

DataOutputStream

calls the

flush

method of its underlying output stream.

**Specified by:** flush

in interface

Flushable
**Overrides:** flush

in class

FilterOutputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

,

OutputStream.flush()

---

#### flush

public void flush()
throws

IOException

Flushes this data output stream. This forces any buffered output
bytes to be written out to the stream.

The

flush

method of

DataOutputStream

calls the

flush

method of its underlying output stream.

The

flush

method of

DataOutputStream

calls the

flush

method of its underlying output stream.

writeBoolean

```java
public final void writeBoolean​(boolean v)
throws
IOException
```

Writes a

boolean

to the underlying output stream as
a 1-byte value. The value

true

is written out as the
value

(byte)1

; the value

false

is
written out as the value

(byte)0

. If no exception is
thrown, the counter

written

is incremented by

1

.

**Specified by:** writeBoolean

in interface

DataOutput
**Parameters:** v

- a

boolean

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

---

#### writeBoolean

public final void writeBoolean​(boolean v)
throws

IOException

Writes a

boolean

to the underlying output stream as
a 1-byte value. The value

true

is written out as the
value

(byte)1

; the value

false

is
written out as the value

(byte)0

. If no exception is
thrown, the counter

written

is incremented by

1

.

writeByte

```java
public final void writeByte​(int v)
throws
IOException
```

Writes out a

byte

to the underlying output stream as
a 1-byte value. If no exception is thrown, the counter

written

is incremented by

1

.

**Specified by:** writeByte

in interface

DataOutput
**Parameters:** v

- a

byte

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

---

#### writeByte

public final void writeByte​(int v)
throws

IOException

Writes out a

byte

to the underlying output stream as
a 1-byte value. If no exception is thrown, the counter

written

is incremented by

1

.

writeShort

```java
public final void writeShort​(int v)
throws
IOException
```

Writes a

short

to the underlying output stream as two
bytes, high byte first. If no exception is thrown, the counter

written

is incremented by

2

.

**Specified by:** writeShort

in interface

DataOutput
**Parameters:** v

- a

short

to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

---

#### writeShort

public final void writeShort​(int v)
throws

IOException

Writes a

short

to the underlying output stream as two
bytes, high byte first. If no exception is thrown, the counter

written

is incremented by

2

.

writeChar

```java
public final void writeChar​(int v)
throws
IOException
```

Writes a

char

to the underlying output stream as a
2-byte value, high byte first. If no exception is thrown, the
counter

written

is incremented by

2

.

**Specified by:** writeChar

in interface

DataOutput
**Parameters:** v

- a

char

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

---

#### writeChar

public final void writeChar​(int v)
throws

IOException

Writes a

char

to the underlying output stream as a
2-byte value, high byte first. If no exception is thrown, the
counter

written

is incremented by

2

.

writeInt

```java
public final void writeInt​(int v)
throws
IOException
```

Writes an

int

to the underlying output stream as four
bytes, high byte first. If no exception is thrown, the counter

written

is incremented by

4

.

**Specified by:** writeInt

in interface

DataOutput
**Parameters:** v

- an

int

to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

---

#### writeInt

public final void writeInt​(int v)
throws

IOException

Writes an

int

to the underlying output stream as four
bytes, high byte first. If no exception is thrown, the counter

written

is incremented by

4

.

writeLong

```java
public final void writeLong​(long v)
throws
IOException
```

Writes a

long

to the underlying output stream as eight
bytes, high byte first. In no exception is thrown, the counter

written

is incremented by

8

.

**Specified by:** writeLong

in interface

DataOutput
**Parameters:** v

- a

long

to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

---

#### writeLong

public final void writeLong​(long v)
throws

IOException

Writes a

long

to the underlying output stream as eight
bytes, high byte first. In no exception is thrown, the counter

written

is incremented by

8

.

writeFloat

```java
public final void writeFloat​(float v)
throws
IOException
```

Converts the float argument to an

int

using the

floatToIntBits

method in class

Float

,
and then writes that

int

value to the underlying
output stream as a 4-byte quantity, high byte first. If no
exception is thrown, the counter

written

is
incremented by

4

.

**Specified by:** writeFloat

in interface

DataOutput
**Parameters:** v

- a

float

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

,

Float.floatToIntBits(float)

---

#### writeFloat

public final void writeFloat​(float v)
throws

IOException

Converts the float argument to an

int

using the

floatToIntBits

method in class

Float

,
and then writes that

int

value to the underlying
output stream as a 4-byte quantity, high byte first. If no
exception is thrown, the counter

written

is
incremented by

4

.

writeDouble

```java
public final void writeDouble​(double v)
throws
IOException
```

Converts the double argument to a

long

using the

doubleToLongBits

method in class

Double

,
and then writes that

long

value to the underlying
output stream as an 8-byte quantity, high byte first. If no
exception is thrown, the counter

written

is
incremented by

8

.

**Specified by:** writeDouble

in interface

DataOutput
**Parameters:** v

- a

double

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

,

Double.doubleToLongBits(double)

---

#### writeDouble

public final void writeDouble​(double v)
throws

IOException

Converts the double argument to a

long

using the

doubleToLongBits

method in class

Double

,
and then writes that

long

value to the underlying
output stream as an 8-byte quantity, high byte first. If no
exception is thrown, the counter

written

is
incremented by

8

.

writeBytes

```java
public final void writeBytes​(
String
s)
throws
IOException
```

Writes out the string to the underlying output stream as a
sequence of bytes. Each character in the string is written out, in
sequence, by discarding its high eight bits. If no exception is
thrown, the counter

written

is incremented by the
length of

s

.

**Specified by:** writeBytes

in interface

DataOutput
**Parameters:** s

- a string of bytes to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterOutputStream.out

---

#### writeBytes

public final void writeBytes​(

String

s)
throws

IOException

Writes out the string to the underlying output stream as a
sequence of bytes. Each character in the string is written out, in
sequence, by discarding its high eight bits. If no exception is
thrown, the counter

written

is incremented by the
length of

s

.

writeChars

```java
public final void writeChars​(
String
s)
throws
IOException
```

Writes a string to the underlying output stream as a sequence of
characters. Each character is written to the data output stream as
if by the

writeChar

method. If no exception is
thrown, the counter

written

is incremented by twice
the length of

s

.

**Specified by:** writeChars

in interface

DataOutput
**Parameters:** s

- a

String

value to be written.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** writeChar(int)

,

FilterOutputStream.out

---

#### writeChars

public final void writeChars​(

String

s)
throws

IOException

Writes a string to the underlying output stream as a sequence of
characters. Each character is written to the data output stream as
if by the

writeChar

method. If no exception is
thrown, the counter

written

is incremented by twice
the length of

s

.

writeUTF

```java
public final void writeUTF​(
String
str)
throws
IOException
```

Writes a string to the underlying output stream using

modified UTF-8

encoding in a machine-independent manner.

First, two bytes are written to the output stream as if by the

writeShort

method giving the number of bytes to
follow. This value is the number of bytes actually written out,
not the length of the string. Following the length, each character
of the string is output, in sequence, using the modified UTF-8 encoding
for the character. If no exception is thrown, the counter

written

is incremented by the total number of
bytes written to the output stream. This will be at least two
plus the length of

str

, and at most two plus
thrice the length of

str

.

**Specified by:** writeUTF

in interface

DataOutput
**Parameters:** str

- a string to be written.
**Throws:** IOException

- if an I/O error occurs.

---

#### writeUTF

public final void writeUTF​(

String

str)
throws

IOException

Writes a string to the underlying output stream using

modified UTF-8

encoding in a machine-independent manner.

First, two bytes are written to the output stream as if by the

writeShort

method giving the number of bytes to
follow. This value is the number of bytes actually written out,
not the length of the string. Following the length, each character
of the string is output, in sequence, using the modified UTF-8 encoding
for the character. If no exception is thrown, the counter

written

is incremented by the total number of
bytes written to the output stream. This will be at least two
plus the length of

str

, and at most two plus
thrice the length of

str

.

First, two bytes are written to the output stream as if by the

writeShort

method giving the number of bytes to
follow. This value is the number of bytes actually written out,
not the length of the string. Following the length, each character
of the string is output, in sequence, using the modified UTF-8 encoding
for the character. If no exception is thrown, the counter

written

is incremented by the total number of
bytes written to the output stream. This will be at least two
plus the length of

str

, and at most two plus
thrice the length of

str

.

size

```java
public final int size()
```

Returns the current value of the counter

written

,
the number of bytes written to this data output stream so far.
If the counter overflows, it will be wrapped to Integer.MAX_VALUE.

**Returns:** the value of the

written

field.
**See Also:** written

---

#### size

public final int size()

Returns the current value of the counter

written

,
the number of bytes written to this data output stream so far.
If the counter overflows, it will be wrapped to Integer.MAX_VALUE.

---

