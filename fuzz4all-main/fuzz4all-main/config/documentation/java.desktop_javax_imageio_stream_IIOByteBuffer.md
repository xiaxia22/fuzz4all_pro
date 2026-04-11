# Class IIOByteBuffer

**Source:** `java.desktop\javax\imageio\stream\IIOByteBuffer.html`

### Class Description

```java
public class
IIOByteBuffer

extends
Object
```

A class representing a mutable reference to an array of bytes and
an offset and length within that array.

IIOByteBuffer

is used by

ImageInputStream

to supply a sequence of bytes
to the caller, possibly with fewer copies than using the conventional

read

methods that take a user-supplied byte array.

The byte array referenced by an

IIOByteBuffer

will
generally be part of an internal data structure belonging to an

ImageReader

implementation; its contents should be
considered read-only and must not be modified.

---

### Field Details

*No entries found.*

### Constructor Details

#### public IIOByteBuffer​(byte[] data,
int offset,
int length)

Constructs an

IIOByteBuffer

that references a
given byte array, offset, and length.

**Parameters:**
- data

- a byte array.
- offset

- an int offset within the array.
- length

- an int specifying the length of the data of
interest within byte array, in bytes.

---

### Method Details

#### public byte[] getData()

Returns a reference to the byte array. The returned value should
be treated as read-only, and only the portion specified by the
values of

getOffset

and

getLength

should
be used.

**Returns:**
- a byte array reference.

**See Also:**
- getOffset()

,

getLength()

,

setData(byte[])

---

#### public void setData​(byte[] data)

Updates the array reference that will be returned by subsequent calls
to the

getData

method.

**Parameters:**
- data

- a byte array reference containing the new data value.

**See Also:**
- getData()

---

#### public int getOffset()

Returns the offset within the byte array returned by

getData

at which the data of interest start.

**Returns:**
- an int offset.

**See Also:**
- getData()

,

getLength()

,

setOffset(int)

---

#### public void setOffset​(int offset)

Updates the value that will be returned by subsequent calls
to the

getOffset

method.

**Parameters:**
- offset

- an int containing the new offset value.

**See Also:**
- getOffset()

---

#### public int getLength()

Returns the length of the data of interest within the byte
array returned by

getData

.

**Returns:**
- an int length.

**See Also:**
- getData()

,

getOffset()

,

setLength(int)

---

#### public void setLength​(int length)

Updates the value that will be returned by subsequent calls
to the

getLength

method.

**Parameters:**
- length

- an int containing the new length value.

**See Also:**
- getLength()

---

### Additional Sections

#### Class IIOByteBuffer

java.lang.Object

- javax.imageio.stream.IIOByteBuffer

javax.imageio.stream.IIOByteBuffer

```java
public class
IIOByteBuffer

extends
Object
```

A class representing a mutable reference to an array of bytes and
an offset and length within that array.

IIOByteBuffer

is used by

ImageInputStream

to supply a sequence of bytes
to the caller, possibly with fewer copies than using the conventional

read

methods that take a user-supplied byte array.

The byte array referenced by an

IIOByteBuffer

will
generally be part of an internal data structure belonging to an

ImageReader

implementation; its contents should be
considered read-only and must not be modified.

public class

IIOByteBuffer

extends

Object

A class representing a mutable reference to an array of bytes and
an offset and length within that array.

IIOByteBuffer

is used by

ImageInputStream

to supply a sequence of bytes
to the caller, possibly with fewer copies than using the conventional

read

methods that take a user-supplied byte array.

The byte array referenced by an

IIOByteBuffer

will
generally be part of an internal data structure belonging to an

ImageReader

implementation; its contents should be
considered read-only and must not be modified.

The byte array referenced by an

IIOByteBuffer

will
generally be part of an internal data structure belonging to an

ImageReader

implementation; its contents should be
considered read-only and must not be modified.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IIOByteBuffer

​(byte[] data,
int offset,
int length)

Constructs an

IIOByteBuffer

that references a
given byte array, offset, and length.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getData

()

Returns a reference to the byte array.

int

getLength

()

Returns the length of the data of interest within the byte
array returned by

getData

.

int

getOffset

()

Returns the offset within the byte array returned by

getData

at which the data of interest start.

void

setData

​(byte[] data)

Updates the array reference that will be returned by subsequent calls
to the

getData

method.

void

setLength

​(int length)

Updates the value that will be returned by subsequent calls
to the

getLength

method.

void

setOffset

​(int offset)

Updates the value that will be returned by subsequent calls
to the

getOffset

method.

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

Constructor Summary

Constructors

Constructor

Description

IIOByteBuffer

​(byte[] data,
int offset,
int length)

Constructs an

IIOByteBuffer

that references a
given byte array, offset, and length.

---

#### Constructor Summary

Constructs an

IIOByteBuffer

that references a
given byte array, offset, and length.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getData

()

Returns a reference to the byte array.

int

getLength

()

Returns the length of the data of interest within the byte
array returned by

getData

.

int

getOffset

()

Returns the offset within the byte array returned by

getData

at which the data of interest start.

void

setData

​(byte[] data)

Updates the array reference that will be returned by subsequent calls
to the

getData

method.

void

setLength

​(int length)

Updates the value that will be returned by subsequent calls
to the

getLength

method.

void

setOffset

​(int offset)

Updates the value that will be returned by subsequent calls
to the

getOffset

method.

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

Returns a reference to the byte array.

Returns the length of the data of interest within the byte
array returned by

getData

.

Returns the offset within the byte array returned by

getData

at which the data of interest start.

Updates the array reference that will be returned by subsequent calls
to the

getData

method.

Updates the value that will be returned by subsequent calls
to the

getLength

method.

Updates the value that will be returned by subsequent calls
to the

getOffset

method.

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

- IIOByteBuffer

```java
public IIOByteBuffer​(byte[] data,
int offset,
int length)
```

Constructs an

IIOByteBuffer

that references a
given byte array, offset, and length.

**Parameters:** data

- a byte array.
**Parameters:** offset

- an int offset within the array.
**Parameters:** length

- an int specifying the length of the data of
interest within byte array, in bytes.

============ METHOD DETAIL ==========

- Method Detail

- getData

```java
public byte[] getData()
```

Returns a reference to the byte array. The returned value should
be treated as read-only, and only the portion specified by the
values of

getOffset

and

getLength

should
be used.

**Returns:** a byte array reference.
**See Also:** getOffset()

,

getLength()

,

setData(byte[])

- setData

```java
public void setData​(byte[] data)
```

Updates the array reference that will be returned by subsequent calls
to the

getData

method.

**Parameters:** data

- a byte array reference containing the new data value.
**See Also:** getData()

- getOffset

```java
public int getOffset()
```

Returns the offset within the byte array returned by

getData

at which the data of interest start.

**Returns:** an int offset.
**See Also:** getData()

,

getLength()

,

setOffset(int)

- setOffset

```java
public void setOffset​(int offset)
```

Updates the value that will be returned by subsequent calls
to the

getOffset

method.

**Parameters:** offset

- an int containing the new offset value.
**See Also:** getOffset()

- getLength

```java
public int getLength()
```

Returns the length of the data of interest within the byte
array returned by

getData

.

**Returns:** an int length.
**See Also:** getData()

,

getOffset()

,

setLength(int)

- setLength

```java
public void setLength​(int length)
```

Updates the value that will be returned by subsequent calls
to the

getLength

method.

**Parameters:** length

- an int containing the new length value.
**See Also:** getLength()

Constructor Detail

- IIOByteBuffer

```java
public IIOByteBuffer​(byte[] data,
int offset,
int length)
```

Constructs an

IIOByteBuffer

that references a
given byte array, offset, and length.

**Parameters:** data

- a byte array.
**Parameters:** offset

- an int offset within the array.
**Parameters:** length

- an int specifying the length of the data of
interest within byte array, in bytes.

---

#### Constructor Detail

IIOByteBuffer

```java
public IIOByteBuffer​(byte[] data,
int offset,
int length)
```

Constructs an

IIOByteBuffer

that references a
given byte array, offset, and length.

**Parameters:** data

- a byte array.
**Parameters:** offset

- an int offset within the array.
**Parameters:** length

- an int specifying the length of the data of
interest within byte array, in bytes.

---

#### IIOByteBuffer

public IIOByteBuffer​(byte[] data,
int offset,
int length)

Constructs an

IIOByteBuffer

that references a
given byte array, offset, and length.

Method Detail

- getData

```java
public byte[] getData()
```

Returns a reference to the byte array. The returned value should
be treated as read-only, and only the portion specified by the
values of

getOffset

and

getLength

should
be used.

**Returns:** a byte array reference.
**See Also:** getOffset()

,

getLength()

,

setData(byte[])

- setData

```java
public void setData​(byte[] data)
```

Updates the array reference that will be returned by subsequent calls
to the

getData

method.

**Parameters:** data

- a byte array reference containing the new data value.
**See Also:** getData()

- getOffset

```java
public int getOffset()
```

Returns the offset within the byte array returned by

getData

at which the data of interest start.

**Returns:** an int offset.
**See Also:** getData()

,

getLength()

,

setOffset(int)

- setOffset

```java
public void setOffset​(int offset)
```

Updates the value that will be returned by subsequent calls
to the

getOffset

method.

**Parameters:** offset

- an int containing the new offset value.
**See Also:** getOffset()

- getLength

```java
public int getLength()
```

Returns the length of the data of interest within the byte
array returned by

getData

.

**Returns:** an int length.
**See Also:** getData()

,

getOffset()

,

setLength(int)

- setLength

```java
public void setLength​(int length)
```

Updates the value that will be returned by subsequent calls
to the

getLength

method.

**Parameters:** length

- an int containing the new length value.
**See Also:** getLength()

---

#### Method Detail

getData

```java
public byte[] getData()
```

Returns a reference to the byte array. The returned value should
be treated as read-only, and only the portion specified by the
values of

getOffset

and

getLength

should
be used.

**Returns:** a byte array reference.
**See Also:** getOffset()

,

getLength()

,

setData(byte[])

---

#### getData

public byte[] getData()

Returns a reference to the byte array. The returned value should
be treated as read-only, and only the portion specified by the
values of

getOffset

and

getLength

should
be used.

setData

```java
public void setData​(byte[] data)
```

Updates the array reference that will be returned by subsequent calls
to the

getData

method.

**Parameters:** data

- a byte array reference containing the new data value.
**See Also:** getData()

---

#### setData

public void setData​(byte[] data)

Updates the array reference that will be returned by subsequent calls
to the

getData

method.

getOffset

```java
public int getOffset()
```

Returns the offset within the byte array returned by

getData

at which the data of interest start.

**Returns:** an int offset.
**See Also:** getData()

,

getLength()

,

setOffset(int)

---

#### getOffset

public int getOffset()

Returns the offset within the byte array returned by

getData

at which the data of interest start.

setOffset

```java
public void setOffset​(int offset)
```

Updates the value that will be returned by subsequent calls
to the

getOffset

method.

**Parameters:** offset

- an int containing the new offset value.
**See Also:** getOffset()

---

#### setOffset

public void setOffset​(int offset)

Updates the value that will be returned by subsequent calls
to the

getOffset

method.

getLength

```java
public int getLength()
```

Returns the length of the data of interest within the byte
array returned by

getData

.

**Returns:** an int length.
**See Also:** getData()

,

getOffset()

,

setLength(int)

---

#### getLength

public int getLength()

Returns the length of the data of interest within the byte
array returned by

getData

.

setLength

```java
public void setLength​(int length)
```

Updates the value that will be returned by subsequent calls
to the

getLength

method.

**Parameters:** length

- an int containing the new length value.
**See Also:** getLength()

---

#### setLength

public void setLength​(int length)

Updates the value that will be returned by subsequent calls
to the

getLength

method.

---

