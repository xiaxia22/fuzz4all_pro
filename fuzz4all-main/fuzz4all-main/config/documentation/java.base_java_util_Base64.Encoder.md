# Class Base64.Encoder

**Source:** `java.base\java\util\Base64.Encoder.html`

### Class Description

```java
public static class
Base64.Encoder

extends
Object
```

This class implements an encoder for encoding byte data using
the Base64 encoding scheme as specified in RFC 4648 and RFC 2045.

Instances of

Base64.Encoder

class are safe for use by
multiple concurrent threads.

Unless otherwise noted, passing a

null

argument to
a method of this class will cause a

NullPointerException

to
be thrown.

**Enclosing class:** Base64

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public byte[] encode​(byte[] src)

Encodes all bytes from the specified byte array into a newly-allocated
byte array using the

Base64

encoding scheme. The returned byte
array is of the length of the resulting bytes.

**Parameters:**
- src

- the byte array to encode

**Returns:**
- A newly-allocated byte array containing the resulting
encoded bytes.

---

#### public int encode​(byte[] src,
byte[] dst)

Encodes all bytes from the specified byte array using the

Base64

encoding scheme, writing the resulting bytes to the
given output byte array, starting at offset 0.

It is the responsibility of the invoker of this method to make
sure the output byte array

dst

has enough space for encoding
all bytes from the input byte array. No bytes will be written to the
output byte array if the output byte array is not big enough.

**Parameters:**
- src

- the byte array to encode
- dst

- the output byte array

**Returns:**
- The number of bytes written to the output byte array

**Throws:**
- IllegalArgumentException

- if

dst

does not have enough
space for encoding all input bytes.

---

#### public
String
encodeToString​(byte[] src)

Encodes the specified byte array into a String using the

Base64

encoding scheme.

This method first encodes all input bytes into a base64 encoded
byte array and then constructs a new String by using the encoded byte
array and the

ISO-8859-1

charset.

In other words, an invocation of this method has exactly the same
effect as invoking

new String(encode(src), StandardCharsets.ISO_8859_1)

.

**Parameters:**
- src

- the byte array to encode

**Returns:**
- A String containing the resulting Base64 encoded characters

---

#### public
ByteBuffer
encode​(
ByteBuffer
buffer)

Encodes all remaining bytes from the specified byte buffer into
a newly-allocated ByteBuffer using the

Base64

encoding
scheme.

Upon return, the source buffer's position will be updated to
its limit; its limit will not have been changed. The returned
output buffer's position will be zero and its limit will be the
number of resulting encoded bytes.

**Parameters:**
- buffer

- the source ByteBuffer to encode

**Returns:**
- A newly-allocated byte buffer containing the encoded bytes.

---

#### public
OutputStream
wrap​(
OutputStream
os)

Wraps an output stream for encoding byte data using the

Base64

encoding scheme.

It is recommended to promptly close the returned output stream after
use, during which it will flush all possible leftover bytes to the underlying
output stream. Closing the returned output stream will close the underlying
output stream.

**Parameters:**
- os

- the output stream.

**Returns:**
- the output stream for encoding the byte data into the
specified Base64 encoded format

---

#### public
Base64.Encoder
withoutPadding()

Returns an encoder instance that encodes equivalently to this one,
but without adding any padding character at the end of the encoded
byte data.

The encoding scheme of this encoder instance is unaffected by
this invocation. The returned encoder instance should be used for
non-padding encoding operation.

**Returns:**
- an equivalent encoder that encodes without adding any
padding character at the end

---

### Additional Sections

#### Class Base64.Encoder

java.lang.Object

- java.util.Base64.Encoder

java.util.Base64.Encoder

**Enclosing class:** Base64

```java
public static class
Base64.Encoder

extends
Object
```

This class implements an encoder for encoding byte data using
the Base64 encoding scheme as specified in RFC 4648 and RFC 2045.

Instances of

Base64.Encoder

class are safe for use by
multiple concurrent threads.

Unless otherwise noted, passing a

null

argument to
a method of this class will cause a

NullPointerException

to
be thrown.

**Since:** 1.8
**See Also:** Base64.Decoder

public static class

Base64.Encoder

extends

Object

This class implements an encoder for encoding byte data using
the Base64 encoding scheme as specified in RFC 4648 and RFC 2045.

Instances of

Base64.Encoder

class are safe for use by
multiple concurrent threads.

Unless otherwise noted, passing a

null

argument to
a method of this class will cause a

NullPointerException

to
be thrown.

Instances of

Base64.Encoder

class are safe for use by
multiple concurrent threads.

Unless otherwise noted, passing a

null

argument to
a method of this class will cause a

NullPointerException

to
be thrown.

Unless otherwise noted, passing a

null

argument to
a method of this class will cause a

NullPointerException

to
be thrown.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

encode

​(byte[] src)

Encodes all bytes from the specified byte array into a newly-allocated
byte array using the

Base64

encoding scheme.

int

encode

​(byte[] src,
byte[] dst)

Encodes all bytes from the specified byte array using the

Base64

encoding scheme, writing the resulting bytes to the
given output byte array, starting at offset 0.

ByteBuffer

encode

​(

ByteBuffer

buffer)

Encodes all remaining bytes from the specified byte buffer into
a newly-allocated ByteBuffer using the

Base64

encoding
scheme.

String

encodeToString

​(byte[] src)

Encodes the specified byte array into a String using the

Base64

encoding scheme.

Base64.Encoder

withoutPadding

()

Returns an encoder instance that encodes equivalently to this one,
but without adding any padding character at the end of the encoded
byte data.

OutputStream

wrap

​(

OutputStream

os)

Wraps an output stream for encoding byte data using the

Base64

encoding scheme.

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

encode

​(byte[] src)

Encodes all bytes from the specified byte array into a newly-allocated
byte array using the

Base64

encoding scheme.

int

encode

​(byte[] src,
byte[] dst)

Encodes all bytes from the specified byte array using the

Base64

encoding scheme, writing the resulting bytes to the
given output byte array, starting at offset 0.

ByteBuffer

encode

​(

ByteBuffer

buffer)

Encodes all remaining bytes from the specified byte buffer into
a newly-allocated ByteBuffer using the

Base64

encoding
scheme.

String

encodeToString

​(byte[] src)

Encodes the specified byte array into a String using the

Base64

encoding scheme.

Base64.Encoder

withoutPadding

()

Returns an encoder instance that encodes equivalently to this one,
but without adding any padding character at the end of the encoded
byte data.

OutputStream

wrap

​(

OutputStream

os)

Wraps an output stream for encoding byte data using the

Base64

encoding scheme.

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

Encodes all bytes from the specified byte array into a newly-allocated
byte array using the

Base64

encoding scheme.

Encodes all bytes from the specified byte array using the

Base64

encoding scheme, writing the resulting bytes to the
given output byte array, starting at offset 0.

Encodes all remaining bytes from the specified byte buffer into
a newly-allocated ByteBuffer using the

Base64

encoding
scheme.

Encodes the specified byte array into a String using the

Base64

encoding scheme.

Returns an encoder instance that encodes equivalently to this one,
but without adding any padding character at the end of the encoded
byte data.

Wraps an output stream for encoding byte data using the

Base64

encoding scheme.

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

============ METHOD DETAIL ==========

- Method Detail

- encode

```java
public byte[] encode​(byte[] src)
```

Encodes all bytes from the specified byte array into a newly-allocated
byte array using the

Base64

encoding scheme. The returned byte
array is of the length of the resulting bytes.

**Parameters:** src

- the byte array to encode
**Returns:** A newly-allocated byte array containing the resulting
encoded bytes.

- encode

```java
public int encode​(byte[] src,
byte[] dst)
```

Encodes all bytes from the specified byte array using the

Base64

encoding scheme, writing the resulting bytes to the
given output byte array, starting at offset 0.

It is the responsibility of the invoker of this method to make
sure the output byte array

dst

has enough space for encoding
all bytes from the input byte array. No bytes will be written to the
output byte array if the output byte array is not big enough.

**Parameters:** src

- the byte array to encode
**Parameters:** dst

- the output byte array
**Returns:** The number of bytes written to the output byte array
**Throws:** IllegalArgumentException

- if

dst

does not have enough
space for encoding all input bytes.

- encodeToString

```java
public
String
encodeToString​(byte[] src)
```

Encodes the specified byte array into a String using the

Base64

encoding scheme.

This method first encodes all input bytes into a base64 encoded
byte array and then constructs a new String by using the encoded byte
array and the

ISO-8859-1

charset.

In other words, an invocation of this method has exactly the same
effect as invoking

new String(encode(src), StandardCharsets.ISO_8859_1)

.

**Parameters:** src

- the byte array to encode
**Returns:** A String containing the resulting Base64 encoded characters

- encode

```java
public
ByteBuffer
encode​(
ByteBuffer
buffer)
```

Encodes all remaining bytes from the specified byte buffer into
a newly-allocated ByteBuffer using the

Base64

encoding
scheme.

Upon return, the source buffer's position will be updated to
its limit; its limit will not have been changed. The returned
output buffer's position will be zero and its limit will be the
number of resulting encoded bytes.

**Parameters:** buffer

- the source ByteBuffer to encode
**Returns:** A newly-allocated byte buffer containing the encoded bytes.

- wrap

```java
public
OutputStream
wrap​(
OutputStream
os)
```

Wraps an output stream for encoding byte data using the

Base64

encoding scheme.

It is recommended to promptly close the returned output stream after
use, during which it will flush all possible leftover bytes to the underlying
output stream. Closing the returned output stream will close the underlying
output stream.

**Parameters:** os

- the output stream.
**Returns:** the output stream for encoding the byte data into the
specified Base64 encoded format

- withoutPadding

```java
public
Base64.Encoder
withoutPadding()
```

Returns an encoder instance that encodes equivalently to this one,
but without adding any padding character at the end of the encoded
byte data.

The encoding scheme of this encoder instance is unaffected by
this invocation. The returned encoder instance should be used for
non-padding encoding operation.

**Returns:** an equivalent encoder that encodes without adding any
padding character at the end

Method Detail

- encode

```java
public byte[] encode​(byte[] src)
```

Encodes all bytes from the specified byte array into a newly-allocated
byte array using the

Base64

encoding scheme. The returned byte
array is of the length of the resulting bytes.

**Parameters:** src

- the byte array to encode
**Returns:** A newly-allocated byte array containing the resulting
encoded bytes.

- encode

```java
public int encode​(byte[] src,
byte[] dst)
```

Encodes all bytes from the specified byte array using the

Base64

encoding scheme, writing the resulting bytes to the
given output byte array, starting at offset 0.

It is the responsibility of the invoker of this method to make
sure the output byte array

dst

has enough space for encoding
all bytes from the input byte array. No bytes will be written to the
output byte array if the output byte array is not big enough.

**Parameters:** src

- the byte array to encode
**Parameters:** dst

- the output byte array
**Returns:** The number of bytes written to the output byte array
**Throws:** IllegalArgumentException

- if

dst

does not have enough
space for encoding all input bytes.

- encodeToString

```java
public
String
encodeToString​(byte[] src)
```

Encodes the specified byte array into a String using the

Base64

encoding scheme.

This method first encodes all input bytes into a base64 encoded
byte array and then constructs a new String by using the encoded byte
array and the

ISO-8859-1

charset.

In other words, an invocation of this method has exactly the same
effect as invoking

new String(encode(src), StandardCharsets.ISO_8859_1)

.

**Parameters:** src

- the byte array to encode
**Returns:** A String containing the resulting Base64 encoded characters

- encode

```java
public
ByteBuffer
encode​(
ByteBuffer
buffer)
```

Encodes all remaining bytes from the specified byte buffer into
a newly-allocated ByteBuffer using the

Base64

encoding
scheme.

Upon return, the source buffer's position will be updated to
its limit; its limit will not have been changed. The returned
output buffer's position will be zero and its limit will be the
number of resulting encoded bytes.

**Parameters:** buffer

- the source ByteBuffer to encode
**Returns:** A newly-allocated byte buffer containing the encoded bytes.

- wrap

```java
public
OutputStream
wrap​(
OutputStream
os)
```

Wraps an output stream for encoding byte data using the

Base64

encoding scheme.

It is recommended to promptly close the returned output stream after
use, during which it will flush all possible leftover bytes to the underlying
output stream. Closing the returned output stream will close the underlying
output stream.

**Parameters:** os

- the output stream.
**Returns:** the output stream for encoding the byte data into the
specified Base64 encoded format

- withoutPadding

```java
public
Base64.Encoder
withoutPadding()
```

Returns an encoder instance that encodes equivalently to this one,
but without adding any padding character at the end of the encoded
byte data.

The encoding scheme of this encoder instance is unaffected by
this invocation. The returned encoder instance should be used for
non-padding encoding operation.

**Returns:** an equivalent encoder that encodes without adding any
padding character at the end

---

#### Method Detail

encode

```java
public byte[] encode​(byte[] src)
```

Encodes all bytes from the specified byte array into a newly-allocated
byte array using the

Base64

encoding scheme. The returned byte
array is of the length of the resulting bytes.

**Parameters:** src

- the byte array to encode
**Returns:** A newly-allocated byte array containing the resulting
encoded bytes.

---

#### encode

public byte[] encode​(byte[] src)

Encodes all bytes from the specified byte array into a newly-allocated
byte array using the

Base64

encoding scheme. The returned byte
array is of the length of the resulting bytes.

encode

```java
public int encode​(byte[] src,
byte[] dst)
```

Encodes all bytes from the specified byte array using the

Base64

encoding scheme, writing the resulting bytes to the
given output byte array, starting at offset 0.

It is the responsibility of the invoker of this method to make
sure the output byte array

dst

has enough space for encoding
all bytes from the input byte array. No bytes will be written to the
output byte array if the output byte array is not big enough.

**Parameters:** src

- the byte array to encode
**Parameters:** dst

- the output byte array
**Returns:** The number of bytes written to the output byte array
**Throws:** IllegalArgumentException

- if

dst

does not have enough
space for encoding all input bytes.

---

#### encode

public int encode​(byte[] src,
byte[] dst)

Encodes all bytes from the specified byte array using the

Base64

encoding scheme, writing the resulting bytes to the
given output byte array, starting at offset 0.

It is the responsibility of the invoker of this method to make
sure the output byte array

dst

has enough space for encoding
all bytes from the input byte array. No bytes will be written to the
output byte array if the output byte array is not big enough.

It is the responsibility of the invoker of this method to make
sure the output byte array

dst

has enough space for encoding
all bytes from the input byte array. No bytes will be written to the
output byte array if the output byte array is not big enough.

encodeToString

```java
public
String
encodeToString​(byte[] src)
```

Encodes the specified byte array into a String using the

Base64

encoding scheme.

This method first encodes all input bytes into a base64 encoded
byte array and then constructs a new String by using the encoded byte
array and the

ISO-8859-1

charset.

In other words, an invocation of this method has exactly the same
effect as invoking

new String(encode(src), StandardCharsets.ISO_8859_1)

.

**Parameters:** src

- the byte array to encode
**Returns:** A String containing the resulting Base64 encoded characters

---

#### encodeToString

public

String

encodeToString​(byte[] src)

Encodes the specified byte array into a String using the

Base64

encoding scheme.

This method first encodes all input bytes into a base64 encoded
byte array and then constructs a new String by using the encoded byte
array and the

ISO-8859-1

charset.

In other words, an invocation of this method has exactly the same
effect as invoking

new String(encode(src), StandardCharsets.ISO_8859_1)

.

This method first encodes all input bytes into a base64 encoded
byte array and then constructs a new String by using the encoded byte
array and the

ISO-8859-1

charset.

In other words, an invocation of this method has exactly the same
effect as invoking

new String(encode(src), StandardCharsets.ISO_8859_1)

.

In other words, an invocation of this method has exactly the same
effect as invoking

new String(encode(src), StandardCharsets.ISO_8859_1)

.

encode

```java
public
ByteBuffer
encode​(
ByteBuffer
buffer)
```

Encodes all remaining bytes from the specified byte buffer into
a newly-allocated ByteBuffer using the

Base64

encoding
scheme.

Upon return, the source buffer's position will be updated to
its limit; its limit will not have been changed. The returned
output buffer's position will be zero and its limit will be the
number of resulting encoded bytes.

**Parameters:** buffer

- the source ByteBuffer to encode
**Returns:** A newly-allocated byte buffer containing the encoded bytes.

---

#### encode

public

ByteBuffer

encode​(

ByteBuffer

buffer)

Encodes all remaining bytes from the specified byte buffer into
a newly-allocated ByteBuffer using the

Base64

encoding
scheme.

Upon return, the source buffer's position will be updated to
its limit; its limit will not have been changed. The returned
output buffer's position will be zero and its limit will be the
number of resulting encoded bytes.

wrap

```java
public
OutputStream
wrap​(
OutputStream
os)
```

Wraps an output stream for encoding byte data using the

Base64

encoding scheme.

It is recommended to promptly close the returned output stream after
use, during which it will flush all possible leftover bytes to the underlying
output stream. Closing the returned output stream will close the underlying
output stream.

**Parameters:** os

- the output stream.
**Returns:** the output stream for encoding the byte data into the
specified Base64 encoded format

---

#### wrap

public

OutputStream

wrap​(

OutputStream

os)

Wraps an output stream for encoding byte data using the

Base64

encoding scheme.

It is recommended to promptly close the returned output stream after
use, during which it will flush all possible leftover bytes to the underlying
output stream. Closing the returned output stream will close the underlying
output stream.

It is recommended to promptly close the returned output stream after
use, during which it will flush all possible leftover bytes to the underlying
output stream. Closing the returned output stream will close the underlying
output stream.

withoutPadding

```java
public
Base64.Encoder
withoutPadding()
```

Returns an encoder instance that encodes equivalently to this one,
but without adding any padding character at the end of the encoded
byte data.

The encoding scheme of this encoder instance is unaffected by
this invocation. The returned encoder instance should be used for
non-padding encoding operation.

**Returns:** an equivalent encoder that encodes without adding any
padding character at the end

---

#### withoutPadding

public

Base64.Encoder

withoutPadding()

Returns an encoder instance that encodes equivalently to this one,
but without adding any padding character at the end of the encoded
byte data.

The encoding scheme of this encoder instance is unaffected by
this invocation. The returned encoder instance should be used for
non-padding encoding operation.

The encoding scheme of this encoder instance is unaffected by
this invocation. The returned encoder instance should be used for
non-padding encoding operation.

---

