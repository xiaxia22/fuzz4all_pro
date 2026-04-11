# Class Base64

**Source:** `java.base\java\util\Base64.html`

### Class Description

```java
public class
Base64

extends
Object
```

This class consists exclusively of static methods for obtaining
encoders and decoders for the Base64 encoding scheme. The
implementation of this class supports the following types of Base64
as specified in

RFC 4648

and

RFC 2045

.

- Basic

Uses "The Base64 Alphabet" as specified in Table 1 of
RFC 4648 and RFC 2045 for encoding and decoding operation.
The encoder does not add any line feed (line separator)
character. The decoder rejects data that contains characters
outside the base64 alphabet.
- URL and Filename safe

Uses the "URL and Filename safe Base64 Alphabet" as specified
in Table 2 of RFC 4648 for encoding and decoding. The
encoder does not add any line feed (line separator) character.
The decoder rejects data that contains characters outside the
base64 alphabet.
- MIME

Uses "The Base64 Alphabet" as specified in Table 1 of
RFC 2045 for encoding and decoding operation. The encoded output
must be represented in lines of no more than 76 characters each
and uses a carriage return

'\r'

followed immediately by
a linefeed

'\n'

as the line separator. No line separator
is added to the end of the encoded output. All line separators
or other characters not found in the base64 alphabet table are
ignored in decoding operation.

Unless otherwise noted, passing a

null

argument to a
method of this class will cause a

NullPointerException

to be thrown.

**Since:** 1.8

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Base64.Encoder
getEncoder()

Returns a

Base64.Encoder

that encodes using the

Basic

type base64 encoding scheme.

**Returns:**
- A Base64 encoder.

---

#### public static
Base64.Encoder
getUrlEncoder()

Returns a

Base64.Encoder

that encodes using the

URL and Filename safe

type base64
encoding scheme.

**Returns:**
- A Base64 encoder.

---

#### public static
Base64.Encoder
getMimeEncoder()

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme.

**Returns:**
- A Base64 encoder.

---

#### public static
Base64.Encoder
getMimeEncoder​(int lineLength,
byte[] lineSeparator)

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme
with specified line length and line separators.

**Parameters:**
- lineLength

- the length of each output line (rounded down to nearest multiple
of 4). If the rounded down line length is not a positive value,
the output will not be separated in lines
- lineSeparator

- the line separator for each output line

**Returns:**
- A Base64 encoder.

**Throws:**
- IllegalArgumentException

- if

lineSeparator

includes any
character of "The Base64 Alphabet" as specified in Table 1 of
RFC 2045.

---

#### public static
Base64.Decoder
getDecoder()

Returns a

Base64.Decoder

that decodes using the

Basic

type base64 encoding scheme.

**Returns:**
- A Base64 decoder.

---

#### public static
Base64.Decoder
getUrlDecoder()

Returns a

Base64.Decoder

that decodes using the

URL and Filename safe

type base64
encoding scheme.

**Returns:**
- A Base64 decoder.

---

#### public static
Base64.Decoder
getMimeDecoder()

Returns a

Base64.Decoder

that decodes using the

MIME

type base64 decoding scheme.

**Returns:**
- A Base64 decoder.

---

### Additional Sections

#### Class Base64

java.lang.Object

- java.util.Base64

java.util.Base64

```java
public class
Base64

extends
Object
```

This class consists exclusively of static methods for obtaining
encoders and decoders for the Base64 encoding scheme. The
implementation of this class supports the following types of Base64
as specified in

RFC 4648

and

RFC 2045

.

- Basic

Uses "The Base64 Alphabet" as specified in Table 1 of
RFC 4648 and RFC 2045 for encoding and decoding operation.
The encoder does not add any line feed (line separator)
character. The decoder rejects data that contains characters
outside the base64 alphabet.
- URL and Filename safe

Uses the "URL and Filename safe Base64 Alphabet" as specified
in Table 2 of RFC 4648 for encoding and decoding. The
encoder does not add any line feed (line separator) character.
The decoder rejects data that contains characters outside the
base64 alphabet.
- MIME

Uses "The Base64 Alphabet" as specified in Table 1 of
RFC 2045 for encoding and decoding operation. The encoded output
must be represented in lines of no more than 76 characters each
and uses a carriage return

'\r'

followed immediately by
a linefeed

'\n'

as the line separator. No line separator
is added to the end of the encoded output. All line separators
or other characters not found in the base64 alphabet table are
ignored in decoding operation.

Unless otherwise noted, passing a

null

argument to a
method of this class will cause a

NullPointerException

to be thrown.

**Since:** 1.8

public class

Base64

extends

Object

This class consists exclusively of static methods for obtaining
encoders and decoders for the Base64 encoding scheme. The
implementation of this class supports the following types of Base64
as specified in

RFC 4648

and

RFC 2045

.

- Basic

Uses "The Base64 Alphabet" as specified in Table 1 of
RFC 4648 and RFC 2045 for encoding and decoding operation.
The encoder does not add any line feed (line separator)
character. The decoder rejects data that contains characters
outside the base64 alphabet.
- URL and Filename safe

Uses the "URL and Filename safe Base64 Alphabet" as specified
in Table 2 of RFC 4648 for encoding and decoding. The
encoder does not add any line feed (line separator) character.
The decoder rejects data that contains characters outside the
base64 alphabet.
- MIME

Uses "The Base64 Alphabet" as specified in Table 1 of
RFC 2045 for encoding and decoding operation. The encoded output
must be represented in lines of no more than 76 characters each
and uses a carriage return

'\r'

followed immediately by
a linefeed

'\n'

as the line separator. No line separator
is added to the end of the encoded output. All line separators
or other characters not found in the base64 alphabet table are
ignored in decoding operation.

Unless otherwise noted, passing a

null

argument to a
method of this class will cause a

NullPointerException

to be thrown.

Basic

Uses "The Base64 Alphabet" as specified in Table 1 of
RFC 4648 and RFC 2045 for encoding and decoding operation.
The encoder does not add any line feed (line separator)
character. The decoder rejects data that contains characters
outside the base64 alphabet.

URL and Filename safe

Uses the "URL and Filename safe Base64 Alphabet" as specified
in Table 2 of RFC 4648 for encoding and decoding. The
encoder does not add any line feed (line separator) character.
The decoder rejects data that contains characters outside the
base64 alphabet.

MIME

Uses "The Base64 Alphabet" as specified in Table 1 of
RFC 2045 for encoding and decoding operation. The encoded output
must be represented in lines of no more than 76 characters each
and uses a carriage return

'\r'

followed immediately by
a linefeed

'\n'

as the line separator. No line separator
is added to the end of the encoded output. All line separators
or other characters not found in the base64 alphabet table are
ignored in decoding operation.

Uses "The Base64 Alphabet" as specified in Table 1 of
RFC 4648 and RFC 2045 for encoding and decoding operation.
The encoder does not add any line feed (line separator)
character. The decoder rejects data that contains characters
outside the base64 alphabet.

Uses the "URL and Filename safe Base64 Alphabet" as specified
in Table 2 of RFC 4648 for encoding and decoding. The
encoder does not add any line feed (line separator) character.
The decoder rejects data that contains characters outside the
base64 alphabet.

Uses "The Base64 Alphabet" as specified in Table 1 of
RFC 2045 for encoding and decoding operation. The encoded output
must be represented in lines of no more than 76 characters each
and uses a carriage return

'\r'

followed immediately by
a linefeed

'\n'

as the line separator. No line separator
is added to the end of the encoded output. All line separators
or other characters not found in the base64 alphabet table are
ignored in decoding operation.

Unless otherwise noted, passing a

null

argument to a
method of this class will cause a

NullPointerException

to be thrown.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Base64.Decoder

This class implements a decoder for decoding byte data using the
Base64 encoding scheme as specified in RFC 4648 and RFC 2045.

static class

Base64.Encoder

This class implements an encoder for encoding byte data using
the Base64 encoding scheme as specified in RFC 4648 and RFC 2045.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Base64.Decoder

getDecoder

()

Returns a

Base64.Decoder

that decodes using the

Basic

type base64 encoding scheme.

static

Base64.Encoder

getEncoder

()

Returns a

Base64.Encoder

that encodes using the

Basic

type base64 encoding scheme.

static

Base64.Decoder

getMimeDecoder

()

Returns a

Base64.Decoder

that decodes using the

MIME

type base64 decoding scheme.

static

Base64.Encoder

getMimeEncoder

()

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme.

static

Base64.Encoder

getMimeEncoder

​(int lineLength,
byte[] lineSeparator)

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme
with specified line length and line separators.

static

Base64.Decoder

getUrlDecoder

()

Returns a

Base64.Decoder

that decodes using the

URL and Filename safe

type base64
encoding scheme.

static

Base64.Encoder

getUrlEncoder

()

Returns a

Base64.Encoder

that encodes using the

URL and Filename safe

type base64
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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Base64.Decoder

This class implements a decoder for decoding byte data using the
Base64 encoding scheme as specified in RFC 4648 and RFC 2045.

static class

Base64.Encoder

This class implements an encoder for encoding byte data using
the Base64 encoding scheme as specified in RFC 4648 and RFC 2045.

---

#### Nested Class Summary

This class implements a decoder for decoding byte data using the
Base64 encoding scheme as specified in RFC 4648 and RFC 2045.

This class implements an encoder for encoding byte data using
the Base64 encoding scheme as specified in RFC 4648 and RFC 2045.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Base64.Decoder

getDecoder

()

Returns a

Base64.Decoder

that decodes using the

Basic

type base64 encoding scheme.

static

Base64.Encoder

getEncoder

()

Returns a

Base64.Encoder

that encodes using the

Basic

type base64 encoding scheme.

static

Base64.Decoder

getMimeDecoder

()

Returns a

Base64.Decoder

that decodes using the

MIME

type base64 decoding scheme.

static

Base64.Encoder

getMimeEncoder

()

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme.

static

Base64.Encoder

getMimeEncoder

​(int lineLength,
byte[] lineSeparator)

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme
with specified line length and line separators.

static

Base64.Decoder

getUrlDecoder

()

Returns a

Base64.Decoder

that decodes using the

URL and Filename safe

type base64
encoding scheme.

static

Base64.Encoder

getUrlEncoder

()

Returns a

Base64.Encoder

that encodes using the

URL and Filename safe

type base64
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

Returns a

Base64.Decoder

that decodes using the

Basic

type base64 encoding scheme.

Returns a

Base64.Encoder

that encodes using the

Basic

type base64 encoding scheme.

Returns a

Base64.Decoder

that decodes using the

MIME

type base64 decoding scheme.

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme.

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme
with specified line length and line separators.

Returns a

Base64.Decoder

that decodes using the

URL and Filename safe

type base64
encoding scheme.

Returns a

Base64.Encoder

that encodes using the

URL and Filename safe

type base64
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

- getEncoder

```java
public static
Base64.Encoder
getEncoder()
```

Returns a

Base64.Encoder

that encodes using the

Basic

type base64 encoding scheme.

**Returns:** A Base64 encoder.

- getUrlEncoder

```java
public static
Base64.Encoder
getUrlEncoder()
```

Returns a

Base64.Encoder

that encodes using the

URL and Filename safe

type base64
encoding scheme.

**Returns:** A Base64 encoder.

- getMimeEncoder

```java
public static
Base64.Encoder
getMimeEncoder()
```

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme.

**Returns:** A Base64 encoder.

- getMimeEncoder

```java
public static
Base64.Encoder
getMimeEncoder​(int lineLength,
byte[] lineSeparator)
```

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme
with specified line length and line separators.

**Parameters:** lineLength

- the length of each output line (rounded down to nearest multiple
of 4). If the rounded down line length is not a positive value,
the output will not be separated in lines
**Parameters:** lineSeparator

- the line separator for each output line
**Returns:** A Base64 encoder.
**Throws:** IllegalArgumentException

- if

lineSeparator

includes any
character of "The Base64 Alphabet" as specified in Table 1 of
RFC 2045.

- getDecoder

```java
public static
Base64.Decoder
getDecoder()
```

Returns a

Base64.Decoder

that decodes using the

Basic

type base64 encoding scheme.

**Returns:** A Base64 decoder.

- getUrlDecoder

```java
public static
Base64.Decoder
getUrlDecoder()
```

Returns a

Base64.Decoder

that decodes using the

URL and Filename safe

type base64
encoding scheme.

**Returns:** A Base64 decoder.

- getMimeDecoder

```java
public static
Base64.Decoder
getMimeDecoder()
```

Returns a

Base64.Decoder

that decodes using the

MIME

type base64 decoding scheme.

**Returns:** A Base64 decoder.

Method Detail

- getEncoder

```java
public static
Base64.Encoder
getEncoder()
```

Returns a

Base64.Encoder

that encodes using the

Basic

type base64 encoding scheme.

**Returns:** A Base64 encoder.

- getUrlEncoder

```java
public static
Base64.Encoder
getUrlEncoder()
```

Returns a

Base64.Encoder

that encodes using the

URL and Filename safe

type base64
encoding scheme.

**Returns:** A Base64 encoder.

- getMimeEncoder

```java
public static
Base64.Encoder
getMimeEncoder()
```

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme.

**Returns:** A Base64 encoder.

- getMimeEncoder

```java
public static
Base64.Encoder
getMimeEncoder​(int lineLength,
byte[] lineSeparator)
```

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme
with specified line length and line separators.

**Parameters:** lineLength

- the length of each output line (rounded down to nearest multiple
of 4). If the rounded down line length is not a positive value,
the output will not be separated in lines
**Parameters:** lineSeparator

- the line separator for each output line
**Returns:** A Base64 encoder.
**Throws:** IllegalArgumentException

- if

lineSeparator

includes any
character of "The Base64 Alphabet" as specified in Table 1 of
RFC 2045.

- getDecoder

```java
public static
Base64.Decoder
getDecoder()
```

Returns a

Base64.Decoder

that decodes using the

Basic

type base64 encoding scheme.

**Returns:** A Base64 decoder.

- getUrlDecoder

```java
public static
Base64.Decoder
getUrlDecoder()
```

Returns a

Base64.Decoder

that decodes using the

URL and Filename safe

type base64
encoding scheme.

**Returns:** A Base64 decoder.

- getMimeDecoder

```java
public static
Base64.Decoder
getMimeDecoder()
```

Returns a

Base64.Decoder

that decodes using the

MIME

type base64 decoding scheme.

**Returns:** A Base64 decoder.

---

#### Method Detail

getEncoder

```java
public static
Base64.Encoder
getEncoder()
```

Returns a

Base64.Encoder

that encodes using the

Basic

type base64 encoding scheme.

**Returns:** A Base64 encoder.

---

#### getEncoder

public static

Base64.Encoder

getEncoder()

Returns a

Base64.Encoder

that encodes using the

Basic

type base64 encoding scheme.

getUrlEncoder

```java
public static
Base64.Encoder
getUrlEncoder()
```

Returns a

Base64.Encoder

that encodes using the

URL and Filename safe

type base64
encoding scheme.

**Returns:** A Base64 encoder.

---

#### getUrlEncoder

public static

Base64.Encoder

getUrlEncoder()

Returns a

Base64.Encoder

that encodes using the

URL and Filename safe

type base64
encoding scheme.

getMimeEncoder

```java
public static
Base64.Encoder
getMimeEncoder()
```

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme.

**Returns:** A Base64 encoder.

---

#### getMimeEncoder

public static

Base64.Encoder

getMimeEncoder()

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme.

getMimeEncoder

```java
public static
Base64.Encoder
getMimeEncoder​(int lineLength,
byte[] lineSeparator)
```

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme
with specified line length and line separators.

**Parameters:** lineLength

- the length of each output line (rounded down to nearest multiple
of 4). If the rounded down line length is not a positive value,
the output will not be separated in lines
**Parameters:** lineSeparator

- the line separator for each output line
**Returns:** A Base64 encoder.
**Throws:** IllegalArgumentException

- if

lineSeparator

includes any
character of "The Base64 Alphabet" as specified in Table 1 of
RFC 2045.

---

#### getMimeEncoder

public static

Base64.Encoder

getMimeEncoder​(int lineLength,
byte[] lineSeparator)

Returns a

Base64.Encoder

that encodes using the

MIME

type base64 encoding scheme
with specified line length and line separators.

getDecoder

```java
public static
Base64.Decoder
getDecoder()
```

Returns a

Base64.Decoder

that decodes using the

Basic

type base64 encoding scheme.

**Returns:** A Base64 decoder.

---

#### getDecoder

public static

Base64.Decoder

getDecoder()

Returns a

Base64.Decoder

that decodes using the

Basic

type base64 encoding scheme.

getUrlDecoder

```java
public static
Base64.Decoder
getUrlDecoder()
```

Returns a

Base64.Decoder

that decodes using the

URL and Filename safe

type base64
encoding scheme.

**Returns:** A Base64 decoder.

---

#### getUrlDecoder

public static

Base64.Decoder

getUrlDecoder()

Returns a

Base64.Decoder

that decodes using the

URL and Filename safe

type base64
encoding scheme.

getMimeDecoder

```java
public static
Base64.Decoder
getMimeDecoder()
```

Returns a

Base64.Decoder

that decodes using the

MIME

type base64 decoding scheme.

**Returns:** A Base64 decoder.

---

#### getMimeDecoder

public static

Base64.Decoder

getMimeDecoder()

Returns a

Base64.Decoder

that decodes using the

MIME

type base64 decoding scheme.

---

