# Class DocFlavor.INPUT_STREAM

**Source:** `java.desktop\javax\print\DocFlavor.INPUT_STREAM.html`

### Class Description

```java
public static class
DocFlavor.INPUT_STREAM

extends
DocFlavor
```

Class

DocFlavor.INPUT_STREAM

provides predefined static constant

DocFlavor

objects for example doc flavors using a byte stream
(

java.io.InputStream

) as the print data
representation class.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_HOST

Doc flavor with MIME type =

"text/plain"

, encoded in the host
platform encoding. See

hostEncoding

.
Print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_8

Doc flavor with MIME type =

"text/plain; charset=utf-8"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_16

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_16BE

Doc flavor with MIME type =

"text/plain; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_16LE

Doc flavor with MIME type =

"text/plain; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_US_ASCII

Doc flavor with MIME type =

"text/plain; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_HOST

Doc flavor with MIME type =

"text/html"

, encoded in the host
platform encoding. See

hostEncoding

.
Print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_8

Doc flavor with MIME type =

"text/html; charset=utf-8"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

---

#### public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_16

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_16BE

Doc flavor with MIME type =

"text/html; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_16LE

Doc flavor with MIME type =

"text/html; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_US_ASCII

Doc flavor with MIME type =

"text/html; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### public static final
DocFlavor.INPUT_STREAM
PDF

Doc flavor with MIME type =

"application/pdf"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

---

#### public static final
DocFlavor.INPUT_STREAM
POSTSCRIPT

Doc flavor with MIME type =

"application/postscript"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

---

#### public static final
DocFlavor.INPUT_STREAM
PCL

Doc flavor with MIME type =

"application/vnd.hp-PCL"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

---

#### public static final
DocFlavor.INPUT_STREAM
GIF

Doc flavor with MIME type =

"image/gif"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

---

#### public static final
DocFlavor.INPUT_STREAM
JPEG

Doc flavor with MIME type =

"image/jpeg"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

---

#### public static final
DocFlavor.INPUT_STREAM
PNG

Doc flavor with MIME type =

"image/png"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

---

#### public static final
DocFlavor.INPUT_STREAM
AUTOSENSE

Doc flavor with MIME type =

"application/octet-stream"

, print
data representation class name =

"java.io.InputStream"

(byte
stream). The client must determine that data described using this

DocFlavor

is valid for the printer.

---

### Constructor Details

#### public INPUT_STREAM​(
String
mimeType)

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.io.InputStream"

(byte
stream).

**Parameters:**
- mimeType

- MIME media type string

**Throws:**
- NullPointerException

- if

mimeType

is

null
- IllegalArgumentException

- if

mimeType

does not obey
the syntax for a MIME media type string.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class DocFlavor.INPUT_STREAM

java.lang.Object

- javax.print.DocFlavor
- - javax.print.DocFlavor.INPUT_STREAM

javax.print.DocFlavor

- javax.print.DocFlavor.INPUT_STREAM

javax.print.DocFlavor.INPUT_STREAM

**All Implemented Interfaces:** Serializable

,

Cloneable

**Enclosing class:** DocFlavor

```java
public static class
DocFlavor.INPUT_STREAM

extends
DocFlavor
```

Class

DocFlavor.INPUT_STREAM

provides predefined static constant

DocFlavor

objects for example doc flavors using a byte stream
(

java.io.InputStream

) as the print data
representation class.

**See Also:** Serialized Form

public static class

DocFlavor.INPUT_STREAM

extends

DocFlavor

Class

DocFlavor.INPUT_STREAM

provides predefined static constant

DocFlavor

objects for example doc flavors using a byte stream
(

java.io.InputStream

) as the print data
representation class.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.print.

DocFlavor

DocFlavor.BYTE_ARRAY

,

DocFlavor.CHAR_ARRAY

,

DocFlavor.INPUT_STREAM

,

DocFlavor.READER

,

DocFlavor.SERVICE_FORMATTED

,

DocFlavor.STRING

,

DocFlavor.URL

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

DocFlavor.INPUT_STREAM

AUTOSENSE

Doc flavor with MIME type =

"application/octet-stream"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

GIF

Doc flavor with MIME type =

"image/gif"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

JPEG

Doc flavor with MIME type =

"image/jpeg"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

PCL

Doc flavor with MIME type =

"application/vnd.hp-PCL"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

PDF

Doc flavor with MIME type =

"application/pdf"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

PNG

Doc flavor with MIME type =

"image/png"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

POSTSCRIPT

Doc flavor with MIME type =

"application/postscript"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

TEXT_HTML_HOST

Doc flavor with MIME type =

"text/html"

, encoded in the host
platform encoding.

static

DocFlavor.INPUT_STREAM

TEXT_HTML_US_ASCII

Doc flavor with MIME type =

"text/html; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_HTML_UTF_16

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_HTML_UTF_16BE

Doc flavor with MIME type =

"text/html; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_HTML_UTF_16LE

Doc flavor with MIME type =

"text/html; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_HTML_UTF_8

Doc flavor with MIME type =

"text/html; charset=utf-8"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

TEXT_PLAIN_HOST

Doc flavor with MIME type =

"text/plain"

, encoded in the host
platform encoding.

static

DocFlavor.INPUT_STREAM

TEXT_PLAIN_US_ASCII

Doc flavor with MIME type =

"text/plain; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_PLAIN_UTF_16

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_PLAIN_UTF_16BE

Doc flavor with MIME type =

"text/plain; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_PLAIN_UTF_16LE

Doc flavor with MIME type =

"text/plain; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_PLAIN_UTF_8

Doc flavor with MIME type =

"text/plain; charset=utf-8"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

- Fields declared in class javax.print.

DocFlavor

hostEncoding

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

INPUT_STREAM

​(

String

mimeType)

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.io.InputStream"

(byte
stream).

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.print.

DocFlavor

equals

,

getMediaSubtype

,

getMediaType

,

getMimeType

,

getParameter

,

getRepresentationClassName

,

hashCode

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Nested Class Summary

- Nested classes/interfaces declared in class javax.print.

DocFlavor

DocFlavor.BYTE_ARRAY

,

DocFlavor.CHAR_ARRAY

,

DocFlavor.INPUT_STREAM

,

DocFlavor.READER

,

DocFlavor.SERVICE_FORMATTED

,

DocFlavor.STRING

,

DocFlavor.URL

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.print.

DocFlavor

DocFlavor.BYTE_ARRAY

,

DocFlavor.CHAR_ARRAY

,

DocFlavor.INPUT_STREAM

,

DocFlavor.READER

,

DocFlavor.SERVICE_FORMATTED

,

DocFlavor.STRING

,

DocFlavor.URL

---

#### Nested classes/interfaces declared in class javax.print. DocFlavor

Field Summary

Fields

Modifier and Type

Field

Description

static

DocFlavor.INPUT_STREAM

AUTOSENSE

Doc flavor with MIME type =

"application/octet-stream"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

GIF

Doc flavor with MIME type =

"image/gif"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

JPEG

Doc flavor with MIME type =

"image/jpeg"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

PCL

Doc flavor with MIME type =

"application/vnd.hp-PCL"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

PDF

Doc flavor with MIME type =

"application/pdf"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

PNG

Doc flavor with MIME type =

"image/png"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

POSTSCRIPT

Doc flavor with MIME type =

"application/postscript"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

TEXT_HTML_HOST

Doc flavor with MIME type =

"text/html"

, encoded in the host
platform encoding.

static

DocFlavor.INPUT_STREAM

TEXT_HTML_US_ASCII

Doc flavor with MIME type =

"text/html; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_HTML_UTF_16

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_HTML_UTF_16BE

Doc flavor with MIME type =

"text/html; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_HTML_UTF_16LE

Doc flavor with MIME type =

"text/html; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_HTML_UTF_8

Doc flavor with MIME type =

"text/html; charset=utf-8"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

static

DocFlavor.INPUT_STREAM

TEXT_PLAIN_HOST

Doc flavor with MIME type =

"text/plain"

, encoded in the host
platform encoding.

static

DocFlavor.INPUT_STREAM

TEXT_PLAIN_US_ASCII

Doc flavor with MIME type =

"text/plain; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_PLAIN_UTF_16

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_PLAIN_UTF_16BE

Doc flavor with MIME type =

"text/plain; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_PLAIN_UTF_16LE

Doc flavor with MIME type =

"text/plain; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

static

DocFlavor.INPUT_STREAM

TEXT_PLAIN_UTF_8

Doc flavor with MIME type =

"text/plain; charset=utf-8"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

- Fields declared in class javax.print.

DocFlavor

hostEncoding

---

#### Field Summary

Doc flavor with MIME type =

"application/octet-stream"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

Doc flavor with MIME type =

"image/gif"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

Doc flavor with MIME type =

"image/jpeg"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

Doc flavor with MIME type =

"application/vnd.hp-PCL"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

Doc flavor with MIME type =

"application/pdf"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

Doc flavor with MIME type =

"image/png"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

Doc flavor with MIME type =

"application/postscript"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

Doc flavor with MIME type =

"text/html"

, encoded in the host
platform encoding.

Doc flavor with MIME type =

"text/html; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

Doc flavor with MIME type =

"text/html; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

Doc flavor with MIME type =

"text/html; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

Doc flavor with MIME type =

"text/html; charset=utf-8"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

Doc flavor with MIME type =

"text/plain"

, encoded in the host
platform encoding.

Doc flavor with MIME type =

"text/plain; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

Doc flavor with MIME type =

"text/plain; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

Doc flavor with MIME type =

"text/plain; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

Doc flavor with MIME type =

"text/plain; charset=utf-8"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

Fields declared in class javax.print.

DocFlavor

hostEncoding

---

#### Fields declared in class javax.print. DocFlavor

Constructor Summary

Constructors

Constructor

Description

INPUT_STREAM

​(

String

mimeType)

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.io.InputStream"

(byte
stream).

---

#### Constructor Summary

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.io.InputStream"

(byte
stream).

Method Summary

- Methods declared in class javax.print.

DocFlavor

equals

,

getMediaSubtype

,

getMediaType

,

getMimeType

,

getParameter

,

getRepresentationClassName

,

hashCode

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Methods declared in class javax.print.

DocFlavor

equals

,

getMediaSubtype

,

getMediaType

,

getMimeType

,

getParameter

,

getRepresentationClassName

,

hashCode

,

toString

---

#### Methods declared in class javax.print. DocFlavor

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

- TEXT_PLAIN_HOST

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_HOST
```

Doc flavor with MIME type =

"text/plain"

, encoded in the host
platform encoding. See

hostEncoding

.
Print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_PLAIN_UTF_8

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_8
```

Doc flavor with MIME type =

"text/plain; charset=utf-8"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_PLAIN_UTF_16

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_16
```

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_PLAIN_UTF_16BE

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_16BE
```

Doc flavor with MIME type =

"text/plain; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_PLAIN_UTF_16LE

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_16LE
```

Doc flavor with MIME type =

"text/plain; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_PLAIN_US_ASCII

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_US_ASCII
```

Doc flavor with MIME type =

"text/plain; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_HTML_HOST

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_HOST
```

Doc flavor with MIME type =

"text/html"

, encoded in the host
platform encoding. See

hostEncoding

.
Print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_HTML_UTF_8

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_8
```

Doc flavor with MIME type =

"text/html; charset=utf-8"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

- TEXT_HTML_UTF_16

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_16
```

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_HTML_UTF_16BE

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_16BE
```

Doc flavor with MIME type =

"text/html; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_HTML_UTF_16LE

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_16LE
```

Doc flavor with MIME type =

"text/html; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_HTML_US_ASCII

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_US_ASCII
```

Doc flavor with MIME type =

"text/html; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

- PDF

```java
public static final
DocFlavor.INPUT_STREAM
PDF
```

Doc flavor with MIME type =

"application/pdf"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

- POSTSCRIPT

```java
public static final
DocFlavor.INPUT_STREAM
POSTSCRIPT
```

Doc flavor with MIME type =

"application/postscript"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

- PCL

```java
public static final
DocFlavor.INPUT_STREAM
PCL
```

Doc flavor with MIME type =

"application/vnd.hp-PCL"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

- GIF

```java
public static final
DocFlavor.INPUT_STREAM
GIF
```

Doc flavor with MIME type =

"image/gif"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

- JPEG

```java
public static final
DocFlavor.INPUT_STREAM
JPEG
```

Doc flavor with MIME type =

"image/jpeg"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

- PNG

```java
public static final
DocFlavor.INPUT_STREAM
PNG
```

Doc flavor with MIME type =

"image/png"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

- AUTOSENSE

```java
public static final
DocFlavor.INPUT_STREAM
AUTOSENSE
```

Doc flavor with MIME type =

"application/octet-stream"

, print
data representation class name =

"java.io.InputStream"

(byte
stream). The client must determine that data described using this

DocFlavor

is valid for the printer.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- INPUT_STREAM

```java
public INPUT_STREAM​(
String
mimeType)
```

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.io.InputStream"

(byte
stream).

**Parameters:** mimeType

- MIME media type string
**Throws:** NullPointerException

- if

mimeType

is

null
**Throws:** IllegalArgumentException

- if

mimeType

does not obey
the syntax for a MIME media type string.

Field Detail

- TEXT_PLAIN_HOST

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_HOST
```

Doc flavor with MIME type =

"text/plain"

, encoded in the host
platform encoding. See

hostEncoding

.
Print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_PLAIN_UTF_8

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_8
```

Doc flavor with MIME type =

"text/plain; charset=utf-8"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_PLAIN_UTF_16

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_16
```

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_PLAIN_UTF_16BE

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_16BE
```

Doc flavor with MIME type =

"text/plain; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_PLAIN_UTF_16LE

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_16LE
```

Doc flavor with MIME type =

"text/plain; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_PLAIN_US_ASCII

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_US_ASCII
```

Doc flavor with MIME type =

"text/plain; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_HTML_HOST

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_HOST
```

Doc flavor with MIME type =

"text/html"

, encoded in the host
platform encoding. See

hostEncoding

.
Print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_HTML_UTF_8

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_8
```

Doc flavor with MIME type =

"text/html; charset=utf-8"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

- TEXT_HTML_UTF_16

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_16
```

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_HTML_UTF_16BE

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_16BE
```

Doc flavor with MIME type =

"text/html; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_HTML_UTF_16LE

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_16LE
```

Doc flavor with MIME type =

"text/html; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

- TEXT_HTML_US_ASCII

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_US_ASCII
```

Doc flavor with MIME type =

"text/html; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

- PDF

```java
public static final
DocFlavor.INPUT_STREAM
PDF
```

Doc flavor with MIME type =

"application/pdf"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

- POSTSCRIPT

```java
public static final
DocFlavor.INPUT_STREAM
POSTSCRIPT
```

Doc flavor with MIME type =

"application/postscript"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

- PCL

```java
public static final
DocFlavor.INPUT_STREAM
PCL
```

Doc flavor with MIME type =

"application/vnd.hp-PCL"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

- GIF

```java
public static final
DocFlavor.INPUT_STREAM
GIF
```

Doc flavor with MIME type =

"image/gif"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

- JPEG

```java
public static final
DocFlavor.INPUT_STREAM
JPEG
```

Doc flavor with MIME type =

"image/jpeg"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

- PNG

```java
public static final
DocFlavor.INPUT_STREAM
PNG
```

Doc flavor with MIME type =

"image/png"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

- AUTOSENSE

```java
public static final
DocFlavor.INPUT_STREAM
AUTOSENSE
```

Doc flavor with MIME type =

"application/octet-stream"

, print
data representation class name =

"java.io.InputStream"

(byte
stream). The client must determine that data described using this

DocFlavor

is valid for the printer.

---

#### Field Detail

TEXT_PLAIN_HOST

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_HOST
```

Doc flavor with MIME type =

"text/plain"

, encoded in the host
platform encoding. See

hostEncoding

.
Print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### TEXT_PLAIN_HOST

public static final

DocFlavor.INPUT_STREAM

TEXT_PLAIN_HOST

Doc flavor with MIME type =

"text/plain"

, encoded in the host
platform encoding. See

hostEncoding

.
Print data representation class name =

"java.io.InputStream"

(byte stream).

TEXT_PLAIN_UTF_8

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_8
```

Doc flavor with MIME type =

"text/plain; charset=utf-8"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### TEXT_PLAIN_UTF_8

public static final

DocFlavor.INPUT_STREAM

TEXT_PLAIN_UTF_8

Doc flavor with MIME type =

"text/plain; charset=utf-8"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

TEXT_PLAIN_UTF_16

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_16
```

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### TEXT_PLAIN_UTF_16

public static final

DocFlavor.INPUT_STREAM

TEXT_PLAIN_UTF_16

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

TEXT_PLAIN_UTF_16BE

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_16BE
```

Doc flavor with MIME type =

"text/plain; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### TEXT_PLAIN_UTF_16BE

public static final

DocFlavor.INPUT_STREAM

TEXT_PLAIN_UTF_16BE

Doc flavor with MIME type =

"text/plain; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

TEXT_PLAIN_UTF_16LE

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_UTF_16LE
```

Doc flavor with MIME type =

"text/plain; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### TEXT_PLAIN_UTF_16LE

public static final

DocFlavor.INPUT_STREAM

TEXT_PLAIN_UTF_16LE

Doc flavor with MIME type =

"text/plain; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

TEXT_PLAIN_US_ASCII

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_PLAIN_US_ASCII
```

Doc flavor with MIME type =

"text/plain; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### TEXT_PLAIN_US_ASCII

public static final

DocFlavor.INPUT_STREAM

TEXT_PLAIN_US_ASCII

Doc flavor with MIME type =

"text/plain; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

TEXT_HTML_HOST

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_HOST
```

Doc flavor with MIME type =

"text/html"

, encoded in the host
platform encoding. See

hostEncoding

.
Print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### TEXT_HTML_HOST

public static final

DocFlavor.INPUT_STREAM

TEXT_HTML_HOST

Doc flavor with MIME type =

"text/html"

, encoded in the host
platform encoding. See

hostEncoding

.
Print data representation class name =

"java.io.InputStream"

(byte stream).

TEXT_HTML_UTF_8

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_8
```

Doc flavor with MIME type =

"text/html; charset=utf-8"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

---

#### TEXT_HTML_UTF_8

public static final

DocFlavor.INPUT_STREAM

TEXT_HTML_UTF_8

Doc flavor with MIME type =

"text/html; charset=utf-8"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

TEXT_HTML_UTF_16

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_16
```

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### TEXT_HTML_UTF_16

public static final

DocFlavor.INPUT_STREAM

TEXT_HTML_UTF_16

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

TEXT_HTML_UTF_16BE

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_16BE
```

Doc flavor with MIME type =

"text/html; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### TEXT_HTML_UTF_16BE

public static final

DocFlavor.INPUT_STREAM

TEXT_HTML_UTF_16BE

Doc flavor with MIME type =

"text/html; charset=utf-16be"

(big-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

TEXT_HTML_UTF_16LE

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_UTF_16LE
```

Doc flavor with MIME type =

"text/html; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### TEXT_HTML_UTF_16LE

public static final

DocFlavor.INPUT_STREAM

TEXT_HTML_UTF_16LE

Doc flavor with MIME type =

"text/html; charset=utf-16le"

(little-endian byte ordering), print data representation class name =

"java.io.InputStream"

(byte stream).

TEXT_HTML_US_ASCII

```java
public static final
DocFlavor.INPUT_STREAM
TEXT_HTML_US_ASCII
```

Doc flavor with MIME type =

"text/html; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

---

#### TEXT_HTML_US_ASCII

public static final

DocFlavor.INPUT_STREAM

TEXT_HTML_US_ASCII

Doc flavor with MIME type =

"text/html; charset=us-ascii"

,
print data representation class name =

"java.io.InputStream"

(byte stream).

PDF

```java
public static final
DocFlavor.INPUT_STREAM
PDF
```

Doc flavor with MIME type =

"application/pdf"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

---

#### PDF

public static final

DocFlavor.INPUT_STREAM

PDF

Doc flavor with MIME type =

"application/pdf"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

POSTSCRIPT

```java
public static final
DocFlavor.INPUT_STREAM
POSTSCRIPT
```

Doc flavor with MIME type =

"application/postscript"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

---

#### POSTSCRIPT

public static final

DocFlavor.INPUT_STREAM

POSTSCRIPT

Doc flavor with MIME type =

"application/postscript"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

PCL

```java
public static final
DocFlavor.INPUT_STREAM
PCL
```

Doc flavor with MIME type =

"application/vnd.hp-PCL"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

---

#### PCL

public static final

DocFlavor.INPUT_STREAM

PCL

Doc flavor with MIME type =

"application/vnd.hp-PCL"

, print
data representation class name =

"java.io.InputStream"

(byte
stream).

GIF

```java
public static final
DocFlavor.INPUT_STREAM
GIF
```

Doc flavor with MIME type =

"image/gif"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

---

#### GIF

public static final

DocFlavor.INPUT_STREAM

GIF

Doc flavor with MIME type =

"image/gif"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

JPEG

```java
public static final
DocFlavor.INPUT_STREAM
JPEG
```

Doc flavor with MIME type =

"image/jpeg"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

---

#### JPEG

public static final

DocFlavor.INPUT_STREAM

JPEG

Doc flavor with MIME type =

"image/jpeg"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

PNG

```java
public static final
DocFlavor.INPUT_STREAM
PNG
```

Doc flavor with MIME type =

"image/png"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

---

#### PNG

public static final

DocFlavor.INPUT_STREAM

PNG

Doc flavor with MIME type =

"image/png"

, print data
representation class name =

"java.io.InputStream"

(byte
stream).

AUTOSENSE

```java
public static final
DocFlavor.INPUT_STREAM
AUTOSENSE
```

Doc flavor with MIME type =

"application/octet-stream"

, print
data representation class name =

"java.io.InputStream"

(byte
stream). The client must determine that data described using this

DocFlavor

is valid for the printer.

---

#### AUTOSENSE

public static final

DocFlavor.INPUT_STREAM

AUTOSENSE

Doc flavor with MIME type =

"application/octet-stream"

, print
data representation class name =

"java.io.InputStream"

(byte
stream). The client must determine that data described using this

DocFlavor

is valid for the printer.

Constructor Detail

- INPUT_STREAM

```java
public INPUT_STREAM​(
String
mimeType)
```

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.io.InputStream"

(byte
stream).

**Parameters:** mimeType

- MIME media type string
**Throws:** NullPointerException

- if

mimeType

is

null
**Throws:** IllegalArgumentException

- if

mimeType

does not obey
the syntax for a MIME media type string.

---

#### Constructor Detail

INPUT_STREAM

```java
public INPUT_STREAM​(
String
mimeType)
```

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.io.InputStream"

(byte
stream).

**Parameters:** mimeType

- MIME media type string
**Throws:** NullPointerException

- if

mimeType

is

null
**Throws:** IllegalArgumentException

- if

mimeType

does not obey
the syntax for a MIME media type string.

---

#### INPUT_STREAM

public INPUT_STREAM​(

String

mimeType)

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.io.InputStream"

(byte
stream).

---

