# Class OctetStreamData

**Source:** `java.xml.crypto\javax\xml\crypto\OctetStreamData.html`

### Class Description

```java
public class
OctetStreamData

extends
Object

implements
Data
```

A representation of a

Data

type containing an octet stream.

**All Implemented Interfaces:** Data

---

### Field Details

*No entries found.*

### Constructor Details

#### public OctetStreamData​(
InputStream
octetStream)

Creates a new

OctetStreamData

.

**Parameters:**
- octetStream

- the input stream containing the octets

**Throws:**
- NullPointerException

- if

octetStream

is

null

---

#### public OctetStreamData​(
InputStream
octetStream,

String
uri,

String
mimeType)

Creates a new

OctetStreamData

.

**Parameters:**
- octetStream

- the input stream containing the octets
- uri

- the URI String identifying the data object (may be

null

)
- mimeType

- the MIME type associated with the data object (may be

null

)

**Throws:**
- NullPointerException

- if

octetStream

is

null

---

### Method Details

#### public
InputStream
getOctetStream()

Returns the input stream of this

OctetStreamData

.

**Returns:**
- the input stream of this

OctetStreamData

.

---

#### public
String
getURI()

Returns the URI String identifying the data object represented by this

OctetStreamData

.

**Returns:**
- the URI String or

null

if not applicable

---

#### public
String
getMimeType()

Returns the MIME type associated with the data object represented by this

OctetStreamData

.

**Returns:**
- the MIME type or

null

if not applicable

---

### Additional Sections

#### Class OctetStreamData

java.lang.Object

- javax.xml.crypto.OctetStreamData

javax.xml.crypto.OctetStreamData

**All Implemented Interfaces:** Data

```java
public class
OctetStreamData

extends
Object

implements
Data
```

A representation of a

Data

type containing an octet stream.

**Since:** 1.6

public class

OctetStreamData

extends

Object

implements

Data

A representation of a

Data

type containing an octet stream.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

OctetStreamData

​(

InputStream

octetStream)

Creates a new

OctetStreamData

.

OctetStreamData

​(

InputStream

octetStream,

String

uri,

String

mimeType)

Creates a new

OctetStreamData

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getMimeType

()

Returns the MIME type associated with the data object represented by this

OctetStreamData

.

InputStream

getOctetStream

()

Returns the input stream of this

OctetStreamData

.

String

getURI

()

Returns the URI String identifying the data object represented by this

OctetStreamData

.

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

OctetStreamData

​(

InputStream

octetStream)

Creates a new

OctetStreamData

.

OctetStreamData

​(

InputStream

octetStream,

String

uri,

String

mimeType)

Creates a new

OctetStreamData

.

---

#### Constructor Summary

Creates a new

OctetStreamData

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getMimeType

()

Returns the MIME type associated with the data object represented by this

OctetStreamData

.

InputStream

getOctetStream

()

Returns the input stream of this

OctetStreamData

.

String

getURI

()

Returns the URI String identifying the data object represented by this

OctetStreamData

.

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

Returns the MIME type associated with the data object represented by this

OctetStreamData

.

Returns the input stream of this

OctetStreamData

.

Returns the URI String identifying the data object represented by this

OctetStreamData

.

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

- OctetStreamData

```java
public OctetStreamData​(
InputStream
octetStream)
```

Creates a new

OctetStreamData

.

**Parameters:** octetStream

- the input stream containing the octets
**Throws:** NullPointerException

- if

octetStream

is

null

- OctetStreamData

```java
public OctetStreamData​(
InputStream
octetStream,

String
uri,

String
mimeType)
```

Creates a new

OctetStreamData

.

**Parameters:** octetStream

- the input stream containing the octets
**Parameters:** uri

- the URI String identifying the data object (may be

null

)
**Parameters:** mimeType

- the MIME type associated with the data object (may be

null

)
**Throws:** NullPointerException

- if

octetStream

is

null

============ METHOD DETAIL ==========

- Method Detail

- getOctetStream

```java
public
InputStream
getOctetStream()
```

Returns the input stream of this

OctetStreamData

.

**Returns:** the input stream of this

OctetStreamData

.

- getURI

```java
public
String
getURI()
```

Returns the URI String identifying the data object represented by this

OctetStreamData

.

**Returns:** the URI String or

null

if not applicable

- getMimeType

```java
public
String
getMimeType()
```

Returns the MIME type associated with the data object represented by this

OctetStreamData

.

**Returns:** the MIME type or

null

if not applicable

Constructor Detail

- OctetStreamData

```java
public OctetStreamData​(
InputStream
octetStream)
```

Creates a new

OctetStreamData

.

**Parameters:** octetStream

- the input stream containing the octets
**Throws:** NullPointerException

- if

octetStream

is

null

- OctetStreamData

```java
public OctetStreamData​(
InputStream
octetStream,

String
uri,

String
mimeType)
```

Creates a new

OctetStreamData

.

**Parameters:** octetStream

- the input stream containing the octets
**Parameters:** uri

- the URI String identifying the data object (may be

null

)
**Parameters:** mimeType

- the MIME type associated with the data object (may be

null

)
**Throws:** NullPointerException

- if

octetStream

is

null

---

#### Constructor Detail

OctetStreamData

```java
public OctetStreamData​(
InputStream
octetStream)
```

Creates a new

OctetStreamData

.

**Parameters:** octetStream

- the input stream containing the octets
**Throws:** NullPointerException

- if

octetStream

is

null

---

#### OctetStreamData

public OctetStreamData​(

InputStream

octetStream)

Creates a new

OctetStreamData

.

OctetStreamData

```java
public OctetStreamData​(
InputStream
octetStream,

String
uri,

String
mimeType)
```

Creates a new

OctetStreamData

.

**Parameters:** octetStream

- the input stream containing the octets
**Parameters:** uri

- the URI String identifying the data object (may be

null

)
**Parameters:** mimeType

- the MIME type associated with the data object (may be

null

)
**Throws:** NullPointerException

- if

octetStream

is

null

---

#### OctetStreamData

public OctetStreamData​(

InputStream

octetStream,

String

uri,

String

mimeType)

Creates a new

OctetStreamData

.

Method Detail

- getOctetStream

```java
public
InputStream
getOctetStream()
```

Returns the input stream of this

OctetStreamData

.

**Returns:** the input stream of this

OctetStreamData

.

- getURI

```java
public
String
getURI()
```

Returns the URI String identifying the data object represented by this

OctetStreamData

.

**Returns:** the URI String or

null

if not applicable

- getMimeType

```java
public
String
getMimeType()
```

Returns the MIME type associated with the data object represented by this

OctetStreamData

.

**Returns:** the MIME type or

null

if not applicable

---

#### Method Detail

getOctetStream

```java
public
InputStream
getOctetStream()
```

Returns the input stream of this

OctetStreamData

.

**Returns:** the input stream of this

OctetStreamData

.

---

#### getOctetStream

public

InputStream

getOctetStream()

Returns the input stream of this

OctetStreamData

.

getURI

```java
public
String
getURI()
```

Returns the URI String identifying the data object represented by this

OctetStreamData

.

**Returns:** the URI String or

null

if not applicable

---

#### getURI

public

String

getURI()

Returns the URI String identifying the data object represented by this

OctetStreamData

.

getMimeType

```java
public
String
getMimeType()
```

Returns the MIME type associated with the data object represented by this

OctetStreamData

.

**Returns:** the MIME type or

null

if not applicable

---

#### getMimeType

public

String

getMimeType()

Returns the MIME type associated with the data object represented by this

OctetStreamData

.

---

