# Class CRC32C

**Source:** `java.base\java\util\zip\CRC32C.html`

### Class Description

```java
public final class
CRC32C

extends
Object

implements
Checksum
```

A class that can be used to compute the CRC-32C of a data stream.

CRC-32C is defined in

RFC
3720

: Internet Small Computer Systems Interface (iSCSI).

Passing a

null

argument to a method in this class will cause a

NullPointerException

to be thrown.

**All Implemented Interfaces:** Checksum

---

### Field Details

*No entries found.*

### Constructor Details

#### public CRC32C()

Creates a new CRC32C object.

---

### Method Details

#### public void update​(int b)

Updates the CRC-32C checksum with the specified byte (the low eight bits
of the argument b).

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

Updates the CRC-32C checksum with the specified array of bytes.

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

Updates the CRC-32C checksum with the bytes from the specified buffer.

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

---

#### public void reset()

Resets CRC-32C to initial value.

**Specified by:**
- reset

in interface

Checksum

---

#### public long getValue()

Returns CRC-32C value.

**Specified by:**
- getValue

in interface

Checksum

**Returns:**
- the current checksum value

---

### Additional Sections

#### Class CRC32C

java.lang.Object

- java.util.zip.CRC32C

java.util.zip.CRC32C

**All Implemented Interfaces:** Checksum

```java
public final class
CRC32C

extends
Object

implements
Checksum
```

A class that can be used to compute the CRC-32C of a data stream.

CRC-32C is defined in

RFC
3720

: Internet Small Computer Systems Interface (iSCSI).

Passing a

null

argument to a method in this class will cause a

NullPointerException

to be thrown.

**Since:** 9

public final class

CRC32C

extends

Object

implements

Checksum

A class that can be used to compute the CRC-32C of a data stream.

CRC-32C is defined in

RFC
3720

: Internet Small Computer Systems Interface (iSCSI).

Passing a

null

argument to a method in this class will cause a

NullPointerException

to be thrown.

CRC-32C is defined in

RFC
3720

: Internet Small Computer Systems Interface (iSCSI).

Passing a

null

argument to a method in this class will cause a

NullPointerException

to be thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CRC32C

()

Creates a new CRC32C object.

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

Returns CRC-32C value.

void

reset

()

Resets CRC-32C to initial value.

void

update

​(byte[] b,
int off,
int len)

Updates the CRC-32C checksum with the specified array of bytes.

void

update

​(int b)

Updates the CRC-32C checksum with the specified byte (the low eight bits
of the argument b).

void

update

​(

ByteBuffer

buffer)

Updates the CRC-32C checksum with the bytes from the specified buffer.

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

CRC32C

()

Creates a new CRC32C object.

---

#### Constructor Summary

Creates a new CRC32C object.

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

Returns CRC-32C value.

void

reset

()

Resets CRC-32C to initial value.

void

update

​(byte[] b,
int off,
int len)

Updates the CRC-32C checksum with the specified array of bytes.

void

update

​(int b)

Updates the CRC-32C checksum with the specified byte (the low eight bits
of the argument b).

void

update

​(

ByteBuffer

buffer)

Updates the CRC-32C checksum with the bytes from the specified buffer.

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

Returns CRC-32C value.

Resets CRC-32C to initial value.

Updates the CRC-32C checksum with the specified array of bytes.

Updates the CRC-32C checksum with the specified byte (the low eight bits
of the argument b).

Updates the CRC-32C checksum with the bytes from the specified buffer.

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

- CRC32C

```java
public CRC32C()
```

Creates a new CRC32C object.

============ METHOD DETAIL ==========

- Method Detail

- update

```java
public void update​(int b)
```

Updates the CRC-32C checksum with the specified byte (the low eight bits
of the argument b).

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

Updates the CRC-32C checksum with the specified array of bytes.

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

Updates the CRC-32C checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

**Specified by:** update

in interface

Checksum
**Parameters:** buffer

- the ByteBuffer to update the checksum with

- reset

```java
public void reset()
```

Resets CRC-32C to initial value.

**Specified by:** reset

in interface

Checksum

- getValue

```java
public long getValue()
```

Returns CRC-32C value.

**Specified by:** getValue

in interface

Checksum
**Returns:** the current checksum value

Constructor Detail

- CRC32C

```java
public CRC32C()
```

Creates a new CRC32C object.

---

#### Constructor Detail

CRC32C

```java
public CRC32C()
```

Creates a new CRC32C object.

---

#### CRC32C

public CRC32C()

Creates a new CRC32C object.

Method Detail

- update

```java
public void update​(int b)
```

Updates the CRC-32C checksum with the specified byte (the low eight bits
of the argument b).

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

Updates the CRC-32C checksum with the specified array of bytes.

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

Updates the CRC-32C checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

**Specified by:** update

in interface

Checksum
**Parameters:** buffer

- the ByteBuffer to update the checksum with

- reset

```java
public void reset()
```

Resets CRC-32C to initial value.

**Specified by:** reset

in interface

Checksum

- getValue

```java
public long getValue()
```

Returns CRC-32C value.

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

Updates the CRC-32C checksum with the specified byte (the low eight bits
of the argument b).

**Specified by:** update

in interface

Checksum
**Parameters:** b

- the byte to update the checksum with

---

#### update

public void update​(int b)

Updates the CRC-32C checksum with the specified byte (the low eight bits
of the argument b).

update

```java
public void update​(byte[] b,
int off,
int len)
```

Updates the CRC-32C checksum with the specified array of bytes.

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

Updates the CRC-32C checksum with the specified array of bytes.

update

```java
public void update​(
ByteBuffer
buffer)
```

Updates the CRC-32C checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

**Specified by:** update

in interface

Checksum
**Parameters:** buffer

- the ByteBuffer to update the checksum with

---

#### update

public void update​(

ByteBuffer

buffer)

Updates the CRC-32C checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

reset

```java
public void reset()
```

Resets CRC-32C to initial value.

**Specified by:** reset

in interface

Checksum

---

#### reset

public void reset()

Resets CRC-32C to initial value.

getValue

```java
public long getValue()
```

Returns CRC-32C value.

**Specified by:** getValue

in interface

Checksum
**Returns:** the current checksum value

---

#### getValue

public long getValue()

Returns CRC-32C value.

---

