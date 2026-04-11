# Class DocFlavor.STRING

**Source:** `java.desktop\javax\print\DocFlavor.STRING.html`

### Class Description

```java
public static class
DocFlavor.STRING

extends
DocFlavor
```

Class

DocFlavor.STRING

provides predefined static constant

DocFlavor

objects for example doc flavors using a string
(

java.lang.String

) as the print data representation class.
As such, the character set is Unicode.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### public static final
DocFlavor.STRING
TEXT_PLAIN

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

---

#### public static final
DocFlavor.STRING
TEXT_HTML

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

---

### Constructor Details

#### public STRING​(
String
mimeType)

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.lang.String"

.

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

#### Class DocFlavor.STRING

java.lang.Object

- javax.print.DocFlavor
- - javax.print.DocFlavor.STRING

javax.print.DocFlavor

- javax.print.DocFlavor.STRING

javax.print.DocFlavor.STRING

**All Implemented Interfaces:** Serializable

,

Cloneable

**Enclosing class:** DocFlavor

```java
public static class
DocFlavor.STRING

extends
DocFlavor
```

Class

DocFlavor.STRING

provides predefined static constant

DocFlavor

objects for example doc flavors using a string
(

java.lang.String

) as the print data representation class.
As such, the character set is Unicode.

**See Also:** Serialized Form

public static class

DocFlavor.STRING

extends

DocFlavor

Class

DocFlavor.STRING

provides predefined static constant

DocFlavor

objects for example doc flavors using a string
(

java.lang.String

) as the print data representation class.
As such, the character set is Unicode.

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

DocFlavor.STRING

TEXT_HTML

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

static

DocFlavor.STRING

TEXT_PLAIN

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

- Fields declared in class javax.print.

DocFlavor

hostEncoding

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

STRING

​(

String

mimeType)

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.lang.String"

.

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

DocFlavor.STRING

TEXT_HTML

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

static

DocFlavor.STRING

TEXT_PLAIN

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

- Fields declared in class javax.print.

DocFlavor

hostEncoding

---

#### Field Summary

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

Fields declared in class javax.print.

DocFlavor

hostEncoding

---

#### Fields declared in class javax.print. DocFlavor

Constructor Summary

Constructors

Constructor

Description

STRING

​(

String

mimeType)

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.lang.String"

.

---

#### Constructor Summary

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.lang.String"

.

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
DocFlavor.STRING
TEXT_PLAIN
```

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

- TEXT_HTML

```java
public static final
DocFlavor.STRING
TEXT_HTML
```

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- STRING

```java
public STRING​(
String
mimeType)
```

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.lang.String"

.

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
DocFlavor.STRING
TEXT_PLAIN
```

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

- TEXT_HTML

```java
public static final
DocFlavor.STRING
TEXT_HTML
```

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

---

#### Field Detail

TEXT_PLAIN

```java
public static final
DocFlavor.STRING
TEXT_PLAIN
```

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

---

#### TEXT_PLAIN

public static final

DocFlavor.STRING

TEXT_PLAIN

Doc flavor with MIME type =

"text/plain; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

TEXT_HTML

```java
public static final
DocFlavor.STRING
TEXT_HTML
```

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

---

#### TEXT_HTML

public static final

DocFlavor.STRING

TEXT_HTML

Doc flavor with MIME type =

"text/html; charset=utf-16"

,
print data representation class name =

"java.lang.String"

.

Constructor Detail

- STRING

```java
public STRING​(
String
mimeType)
```

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.lang.String"

.

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

STRING

```java
public STRING​(
String
mimeType)
```

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.lang.String"

.

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

#### STRING

public STRING​(

String

mimeType)

Constructs a new doc flavor with the given MIME type and a print data
representation class name of

"java.lang.String"

.

---

