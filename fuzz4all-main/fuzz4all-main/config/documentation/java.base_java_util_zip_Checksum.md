# Interface Checksum

**Source:** `java.base\java\util\zip\Checksum.html`

### Class Description

```java
public interface
Checksum
```

An interface representing a data checksum.

**All Known Implementing Classes:** Adler32

,

CRC32

,

CRC32C

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void update​(int b)

Updates the current checksum with the specified byte.

**Parameters:**
- b

- the byte to update the checksum with

---

#### default void update​(byte[] b)

Updates the current checksum with the specified array of bytes.

**Parameters:**
- b

- the array of bytes to update the checksum with

**Throws:**
- NullPointerException

- if

b

is

null

**Since:**
- 9

**Implementation Requirements:**
- This default implementation is equal to calling

update(b, 0, b.length)

.

---

#### void update​(byte[] b,
int off,
int len)

Updates the current checksum with the specified array of bytes.

**Parameters:**
- b

- the byte array to update the checksum with
- off

- the start offset of the data
- len

- the number of bytes to use for the update

---

#### default void update​(
ByteBuffer
buffer)

Updates the current checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

**Parameters:**
- buffer

- the ByteBuffer to update the checksum with

**Throws:**
- NullPointerException

- if

buffer

is

null

**Since:**
- 9

**API Note:**
- For best performance with DirectByteBuffer and other ByteBuffer
implementations without a backing array implementers of this interface
should override this method.

**Implementation Requirements:**
- The default implementation has the following behavior.

For ByteBuffers backed by an accessible byte array.

```java
update(buffer.array(),
buffer.position() + buffer.arrayOffset(),
buffer.remaining());
```

For ByteBuffers not backed by an accessible byte array.

```java
byte[] b = new byte[Math.min(buffer.remaining(), 4096)];
while (buffer.hasRemaining()) {
int length = Math.min(buffer.remaining(), b.length);
buffer.get(b, 0, length);
update(b, 0, length);
}
```

---

#### long getValue()

Returns the current checksum value.

**Returns:**
- the current checksum value

---

#### void reset()

Resets the checksum to its initial value.

---

### Additional Sections

#### Interface Checksum

**All Known Implementing Classes:** Adler32

,

CRC32

,

CRC32C

```java
public interface
Checksum
```

An interface representing a data checksum.

**Since:** 1.1

public interface

Checksum

An interface representing a data checksum.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

long

getValue

()

Returns the current checksum value.

void

reset

()

Resets the checksum to its initial value.

default void

update

​(byte[] b)

Updates the current checksum with the specified array of bytes.

void

update

​(byte[] b,
int off,
int len)

Updates the current checksum with the specified array of bytes.

void

update

​(int b)

Updates the current checksum with the specified byte.

default void

update

​(

ByteBuffer

buffer)

Updates the current checksum with the bytes from the specified buffer.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

long

getValue

()

Returns the current checksum value.

void

reset

()

Resets the checksum to its initial value.

default void

update

​(byte[] b)

Updates the current checksum with the specified array of bytes.

void

update

​(byte[] b,
int off,
int len)

Updates the current checksum with the specified array of bytes.

void

update

​(int b)

Updates the current checksum with the specified byte.

default void

update

​(

ByteBuffer

buffer)

Updates the current checksum with the bytes from the specified buffer.

---

#### Method Summary

Returns the current checksum value.

Resets the checksum to its initial value.

Updates the current checksum with the specified array of bytes.

Updates the current checksum with the specified byte.

Updates the current checksum with the bytes from the specified buffer.

============ METHOD DETAIL ==========

- Method Detail

- update

```java
void update​(int b)
```

Updates the current checksum with the specified byte.

**Parameters:** b

- the byte to update the checksum with

- update

```java
default void update​(byte[] b)
```

Updates the current checksum with the specified array of bytes.

**Implementation Requirements:** This default implementation is equal to calling

update(b, 0, b.length)

.
**Parameters:** b

- the array of bytes to update the checksum with
**Throws:** NullPointerException

- if

b

is

null
**Since:** 9

- update

```java
void update​(byte[] b,
int off,
int len)
```

Updates the current checksum with the specified array of bytes.

**Parameters:** b

- the byte array to update the checksum with
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the number of bytes to use for the update

- update

```java
default void update​(
ByteBuffer
buffer)
```

Updates the current checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

**API Note:** For best performance with DirectByteBuffer and other ByteBuffer
implementations without a backing array implementers of this interface
should override this method.
**Implementation Requirements:** The default implementation has the following behavior.

For ByteBuffers backed by an accessible byte array.

```java
update(buffer.array(),
buffer.position() + buffer.arrayOffset(),
buffer.remaining());
```

For ByteBuffers not backed by an accessible byte array.

```java
byte[] b = new byte[Math.min(buffer.remaining(), 4096)];
while (buffer.hasRemaining()) {
int length = Math.min(buffer.remaining(), b.length);
buffer.get(b, 0, length);
update(b, 0, length);
}
```
**Parameters:** buffer

- the ByteBuffer to update the checksum with
**Throws:** NullPointerException

- if

buffer

is

null
**Since:** 9

- getValue

```java
long getValue()
```

Returns the current checksum value.

**Returns:** the current checksum value

- reset

```java
void reset()
```

Resets the checksum to its initial value.

Method Detail

- update

```java
void update​(int b)
```

Updates the current checksum with the specified byte.

**Parameters:** b

- the byte to update the checksum with

- update

```java
default void update​(byte[] b)
```

Updates the current checksum with the specified array of bytes.

**Implementation Requirements:** This default implementation is equal to calling

update(b, 0, b.length)

.
**Parameters:** b

- the array of bytes to update the checksum with
**Throws:** NullPointerException

- if

b

is

null
**Since:** 9

- update

```java
void update​(byte[] b,
int off,
int len)
```

Updates the current checksum with the specified array of bytes.

**Parameters:** b

- the byte array to update the checksum with
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the number of bytes to use for the update

- update

```java
default void update​(
ByteBuffer
buffer)
```

Updates the current checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

**API Note:** For best performance with DirectByteBuffer and other ByteBuffer
implementations without a backing array implementers of this interface
should override this method.
**Implementation Requirements:** The default implementation has the following behavior.

For ByteBuffers backed by an accessible byte array.

```java
update(buffer.array(),
buffer.position() + buffer.arrayOffset(),
buffer.remaining());
```

For ByteBuffers not backed by an accessible byte array.

```java
byte[] b = new byte[Math.min(buffer.remaining(), 4096)];
while (buffer.hasRemaining()) {
int length = Math.min(buffer.remaining(), b.length);
buffer.get(b, 0, length);
update(b, 0, length);
}
```
**Parameters:** buffer

- the ByteBuffer to update the checksum with
**Throws:** NullPointerException

- if

buffer

is

null
**Since:** 9

- getValue

```java
long getValue()
```

Returns the current checksum value.

**Returns:** the current checksum value

- reset

```java
void reset()
```

Resets the checksum to its initial value.

---

#### Method Detail

update

```java
void update​(int b)
```

Updates the current checksum with the specified byte.

**Parameters:** b

- the byte to update the checksum with

---

#### update

void update​(int b)

Updates the current checksum with the specified byte.

update

```java
default void update​(byte[] b)
```

Updates the current checksum with the specified array of bytes.

**Implementation Requirements:** This default implementation is equal to calling

update(b, 0, b.length)

.
**Parameters:** b

- the array of bytes to update the checksum with
**Throws:** NullPointerException

- if

b

is

null
**Since:** 9

---

#### update

default void update​(byte[] b)

Updates the current checksum with the specified array of bytes.

update

```java
void update​(byte[] b,
int off,
int len)
```

Updates the current checksum with the specified array of bytes.

**Parameters:** b

- the byte array to update the checksum with
**Parameters:** off

- the start offset of the data
**Parameters:** len

- the number of bytes to use for the update

---

#### update

void update​(byte[] b,
int off,
int len)

Updates the current checksum with the specified array of bytes.

update

```java
default void update​(
ByteBuffer
buffer)
```

Updates the current checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

**API Note:** For best performance with DirectByteBuffer and other ByteBuffer
implementations without a backing array implementers of this interface
should override this method.
**Implementation Requirements:** The default implementation has the following behavior.

For ByteBuffers backed by an accessible byte array.

```java
update(buffer.array(),
buffer.position() + buffer.arrayOffset(),
buffer.remaining());
```

For ByteBuffers not backed by an accessible byte array.

```java
byte[] b = new byte[Math.min(buffer.remaining(), 4096)];
while (buffer.hasRemaining()) {
int length = Math.min(buffer.remaining(), b.length);
buffer.get(b, 0, length);
update(b, 0, length);
}
```
**Parameters:** buffer

- the ByteBuffer to update the checksum with
**Throws:** NullPointerException

- if

buffer

is

null
**Since:** 9

---

#### update

default void update​(

ByteBuffer

buffer)

Updates the current checksum with the bytes from the specified buffer.

The checksum is updated with the remaining bytes in the buffer, starting
at the buffer's position. Upon return, the buffer's position will be
updated to its limit; its limit will not have been changed.

update(buffer.array(),
buffer.position() + buffer.arrayOffset(),
buffer.remaining());

byte[] b = new byte[Math.min(buffer.remaining(), 4096)];
while (buffer.hasRemaining()) {
int length = Math.min(buffer.remaining(), b.length);
buffer.get(b, 0, length);
update(b, 0, length);
}

getValue

```java
long getValue()
```

Returns the current checksum value.

**Returns:** the current checksum value

---

#### getValue

long getValue()

Returns the current checksum value.

reset

```java
void reset()
```

Resets the checksum to its initial value.

---

#### reset

void reset()

Resets the checksum to its initial value.

---

