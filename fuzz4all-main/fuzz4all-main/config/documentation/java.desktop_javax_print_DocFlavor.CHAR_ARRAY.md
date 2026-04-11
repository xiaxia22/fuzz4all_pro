# Class DocFlavor.CHAR_ARRAY

**Source:** `java.desktop\javax\print\DocFlavor.CHAR_ARRAY.html`

### Class Description

```java
public static class
DocFlavor.CHAR_ARRAY

extends
DocFlavor
```

Class

DocFlavor.CHAR_ARRAY

provides predefined static constant

DocFlavor

objects for example doc flavors using a character array
(

char[]

) as the print data representation class. As such, the
character set is Unicode.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### public static final
DocFlavor.CHAR_ARRAY
TEXT_PLAIN

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

---

#### public static final
DocFlavor.CHAR_ARRAY
TEXT_HTML

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

---

### Constructor Details

#### public CHAR_ARRAY​(
String
mimeType)

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"[C"

(character array).

**Parameters:**
- mimeType

- MIME media type string. If it is a text media type,
it is assumed to contain a

"charset=utf-16"

parameter.

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
the syntax for a MIME media type string

---

### Method Details

*No entries found.*

### Additional Sections

#### Class DocFlavor.CHAR_ARRAY

java.lang.Object

- javax.print.DocFlavor
- - javax.print.DocFlavor.CHAR_ARRAY

javax.print.DocFlavor

- javax.print.DocFlavor.CHAR_ARRAY

javax.print.DocFlavor.CHAR_ARRAY

**All Implemented Interfaces:** Serializable

,

Cloneable

**Enclosing class:** DocFlavor

```java
public static class
DocFlavor.CHAR_ARRAY

extends
DocFlavor
```

Class

DocFlavor.CHAR_ARRAY

provides predefined static constant

DocFlavor

objects for example doc flavors using a character array
(

char[]

) as the print data representation class. As such, the
character set is Unicode.

**See Also:** Serialized Form

public static class

DocFlavor.CHAR_ARRAY

extends

DocFlavor

Class

DocFlavor.CHAR_ARRAY

provides predefined static constant

DocFlavor

objects for example doc flavors using a character array
(

char[]

) as the print data representation class. As such, the
character set is Unicode.

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

DocFlavor.CHAR_ARRAY

TEXT_HTML

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

static

DocFlavor.CHAR_ARRAY

TEXT_PLAIN

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

- Fields declared in class javax.print.

DocFlavor

hostEncoding

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CHAR_ARRAY

​(

String

mimeType)

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"[C"

(character array).

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

DocFlavor.CHAR_ARRAY

TEXT_HTML

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

static

DocFlavor.CHAR_ARRAY

TEXT_PLAIN

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

- Fields declared in class javax.print.

DocFlavor

hostEncoding

---

#### Field Summary

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

Fields declared in class javax.print.

DocFlavor

hostEncoding

---

#### Fields declared in class javax.print. DocFlavor

Constructor Summary

Constructors

Constructor

Description

CHAR_ARRAY

​(

String

mimeType)

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"[C"

(character array).

---

#### Constructor Summary

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"[C"

(character array).

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

- TEXT_PLAIN

```java
public static final
DocFlavor.CHAR_ARRAY
TEXT_PLAIN
```

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

- TEXT_HTML

```java
public static final
DocFlavor.CHAR_ARRAY
TEXT_HTML
```

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CHAR_ARRAY

```java
public CHAR_ARRAY​(
String
mimeType)
```

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"[C"

(character array).

**Parameters:** mimeType

- MIME media type string. If it is a text media type,
it is assumed to contain a

"charset=utf-16"

parameter.
**Throws:** NullPointerException

- if

mimeType

is

null
**Throws:** IllegalArgumentException

- if

mimeType

does not obey
the syntax for a MIME media type string

Field Detail

- TEXT_PLAIN

```java
public static final
DocFlavor.CHAR_ARRAY
TEXT_PLAIN
```

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

- TEXT_HTML

```java
public static final
DocFlavor.CHAR_ARRAY
TEXT_HTML
```

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

---

#### Field Detail

TEXT_PLAIN

```java
public static final
DocFlavor.CHAR_ARRAY
TEXT_PLAIN
```

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

---

#### TEXT_PLAIN

public static final

DocFlavor.CHAR_ARRAY

TEXT_PLAIN

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

TEXT_HTML

```java
public static final
DocFlavor.CHAR_ARRAY
TEXT_HTML
```

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

---

#### TEXT_HTML

public static final

DocFlavor.CHAR_ARRAY

TEXT_HTML

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"[C"

(character
array).

Constructor Detail

- CHAR_ARRAY

```java
public CHAR_ARRAY​(
String
mimeType)
```

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"[C"

(character array).

**Parameters:** mimeType

- MIME media type string. If it is a text media type,
it is assumed to contain a

"charset=utf-16"

parameter.
**Throws:** NullPointerException

- if

mimeType

is

null
**Throws:** IllegalArgumentException

- if

mimeType

does not obey
the syntax for a MIME media type string

---

#### Constructor Detail

CHAR_ARRAY

```java
public CHAR_ARRAY​(
String
mimeType)
```

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"[C"

(character array).

**Parameters:** mimeType

- MIME media type string. If it is a text media type,
it is assumed to contain a

"charset=utf-16"

parameter.
**Throws:** NullPointerException

- if

mimeType

is

null
**Throws:** IllegalArgumentException

- if

mimeType

does not obey
the syntax for a MIME media type string

---

#### CHAR_ARRAY

public CHAR_ARRAY​(

String

mimeType)

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"[C"

(character array).

---

