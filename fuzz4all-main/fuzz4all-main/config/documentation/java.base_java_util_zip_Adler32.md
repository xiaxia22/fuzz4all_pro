# Class Adler32

**Source:** `java.base\java\util\zip\Adler32.html`

### Class Description

```java
public class
Adler32

extends
Object

implements
Checksum
```

A class that can be used to compute the Adler-32 checksum of a data
stream. An Adler-32 checksum is almost as reliable as a CRC-32 but
can be computed much faster.

Passing a

null

argument to a method in this class will cause
a

NullPointerException

to be thrown.

**All Implemented Interfaces:** Checksum

---

### Field Details

*No entries found.*

### Constructor Details

#### public Adler32()

Creates a new Adler32 object.

---

### Method Details

#### public void update​(int b)

Updates the checksum with the specified byte (the low eight
bits of the argument b).

**Specified by:**
- update

in interface

Checksum

**Parameters:**
- b

- the byte to update the checksum with

---

#### public void update​(byte[] b,
int off,
int len)

Updates the checksum with the specified array of bytes.

**Specified by:**
- update

in interface

Checksum

**Parameters:**
- b

- the byte array to update the checksum with
- off

- the start offset of the data
- len

- the number of bytes to use for the update

**Throws:**
- ArrayIndexOutOfBoundsException

- if

off

is negative, or

len

is negative, or

off+len

is negative or greater than the length of
the array

b

.

---

#### public void update​(
ByteBuffer
buffer)

Updates the checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

**Specified by:**
- update

in interface

Checksum

**Parameters:**
- buffer

- the ByteBuffer to update the checksum with

**Since:**
- 1.8

---

#### public void reset()

Resets the checksum to initial value.

**Specified by:**
- reset

in interface

Checksum

---

#### public long getValue()

Returns the checksum value.

**Specified by:**
- getValue

in interface

Checksum

**Returns:**
- the current checksum value

---

### Additional Sections

#### Class Adler32

java.lang.Object

- java.util.zip.Adler32

java.util.zip.Adler32

**All Implemented Interfaces:** Checksum

```java
public class
Adler32

extends
Object

implements
Checksum
```

A class that can be used to compute the Adler-32 checksum of a data
stream. An Adler-32 checksum is almost as reliable as a CRC-32 but
can be computed much faster.

Passing a

null

argument to a method in this class will cause
a

NullPointerException

to be thrown.

**Since:** 1.1

public class

Adler32

extends

Object

implements

Checksum

A class that can be used to compute the Adler-32 checksum of a data
stream. An Adler-32 checksum is almost as reliable as a CRC-32 but
can be computed much faster.

Passing a

null

argument to a method in this class will cause
a

NullPointerException

to be thrown.

Passing a

null

argument to a method in this class will cause
a

NullPointerException

to be thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Adler32

()

Creates a new Adler32 object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

getValue

()

Returns the checksum value.

void

reset

()

Resets the checksum to initial value.

void

update

​(byte[] b,
int off,
int len)

Updates the checksum with the specified array of bytes.

void

update

​(int b)

Updates the checksum with the specified byte (the low eight
bits of the argument b).

void

update

​(

ByteBuffer

buffer)

Updates the checksum with the bytes from the specified buffer.

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

- Methods declared in interface java.util.zip.

Checksum

update

Constructor Summary

Constructors

Constructor

Description

Adler32

()

Creates a new Adler32 object.

---

#### Constructor Summary

Creates a new Adler32 object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

getValue

()

Returns the checksum value.

void

reset

()

Resets the checksum to initial value.

void

update

​(byte[] b,
int off,
int len)

Updates the checksum with the specified array of bytes.

void

update

​(int b)

Updates the checksum with the specified byte (the low eight
bits of the argument b).

void

update

​(

ByteBuffer

buffer)

Updates the checksum with the bytes from the specified buffer.

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

- Methods declared in interface java.util.zip.

Checksum

update

---

#### Method Summary

Returns the checksum value.

Resets the checksum to initial value.

Updates the checksum with the specified array of bytes.

Updates the checksum with the specified byte (the low eight
bits of the argument b).

Updates the checksum with the bytes from the specified buffer.

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

Methods declared in interface java.util.zip.

Checksum

update

---

#### Methods declared in interface java.util.zip. Checksum

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Adler32

```java
public Adler32()
```

Creates a new Adler32 object.

============ METHOD DETAIL ==========

- Method Detail

- update

```java
public void update​(int b)
```

Updates the checksum with the specified byte (the low eight
bits of the argument b).

**Specified by:** update

in interface

Checksum
**Parameters:** b

- the byte to update the checksum with

- update

```java
public void update​(byte[] b,
int off,
int len)
```

Updates the checksum with the specified array of bytes.

**Specified by:** update

in interface

Checksum
**Parameters:** b

- the byte array to update the checksum with
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the number of bytes to use for the update
**Throws:** ArrayIndexOutOfBoundsException

- if

off

is negative, or

len

is negative, or

off+len

is negative or greater than the length of
the array

b

.

- update

```java
public void update​(
ByteBuffer
buffer)
```

Updates the checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

**Specified by:** update

in interface

Checksum
**Parameters:** buffer

- the ByteBuffer to update the checksum with
**Since:** 1.8

- reset

```java
public void reset()
```

Resets the checksum to initial value.

**Specified by:** reset

in interface

Checksum

- getValue

```java
public long getValue()
```

Returns the checksum value.

**Specified by:** getValue

in interface

Checksum
**Returns:** the current checksum value

Constructor Detail

- Adler32

```java
public Adler32()
```

Creates a new Adler32 object.

---

#### Constructor Detail

Adler32

```java
public Adler32()
```

Creates a new Adler32 object.

---

#### Adler32

public Adler32()

Creates a new Adler32 object.

Method Detail

- update

```java
public void update​(int b)
```

Updates the checksum with the specified byte (the low eight
bits of the argument b).

**Specified by:** update

in interface

Checksum
**Parameters:** b

- the byte to update the checksum with

- update

```java
public void update​(byte[] b,
int off,
int len)
```

Updates the checksum with the specified array of bytes.

**Specified by:** update

in interface

Checksum
**Parameters:** b

- the byte array to update the checksum with
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the number of bytes to use for the update
**Throws:** ArrayIndexOutOfBoundsException

- if

off

is negative, or

len

is negative, or

off+len

is negative or greater than the length of
the array

b

.

- update

```java
public void update​(
ByteBuffer
buffer)
```

Updates the checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

**Specified by:** update

in interface

Checksum
**Parameters:** buffer

- the ByteBuffer to update the checksum with
**Since:** 1.8

- reset

```java
public void reset()
```

Resets the checksum to initial value.

**Specified by:** reset

in interface

Checksum

- getValue

```java
public long getValue()
```

Returns the checksum value.

**Specified by:** getValue

in interface

Checksum
**Returns:** the current checksum value

---

#### Method Detail

update

```java
public void update​(int b)
```

Updates the checksum with the specified byte (the low eight
bits of the argument b).

**Specified by:** update

in interface

Checksum
**Parameters:** b

- the byte to update the checksum with

---

#### update

public void update​(int b)

Updates the checksum with the specified byte (the low eight
bits of the argument b).

update

```java
public void update​(byte[] b,
int off,
int len)
```

Updates the checksum with the specified array of bytes.

**Specified by:** update

in interface

Checksum
**Parameters:** b

- the byte array to update the checksum with
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the number of bytes to use for the update
**Throws:** ArrayIndexOutOfBoundsException

- if

off

is negative, or

len

is negative, or

off+len

is negative or greater than the length of
the array

b

.

---

#### update

public void update​(byte[] b,
int off,
int len)

Updates the checksum with the specified array of bytes.

update

```java
public void update​(
ByteBuffer
buffer)
```

Updates the checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

**Specified by:** update

in interface

Checksum
**Parameters:** buffer

- the ByteBuffer to update the checksum with
**Since:** 1.8

---

#### update

public void update​(

ByteBuffer

buffer)

Updates the checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

reset

```java
public void reset()
```

Resets the checksum to initial value.

**Specified by:** reset

in interface

Checksum

---

#### reset

public void reset()

Resets the checksum to initial value.

getValue

```java
public long getValue()
```

Returns the checksum value.

**Specified by:** getValue

in interface

Checksum
**Returns:** the current checksum value

---

#### getValue

public long getValue()

Returns the checksum value.

---

