# Class StAXResult

**Source:** `java.xml\javax\xml\transform\stax\StAXResult.html`

### Class Description

```java
public class
StAXResult

extends
Object

implements
Result
```

Acts as a holder for an XML

Result

in the
form of a StAX writer,i.e.

XMLStreamWriter

or

XMLEventWriter

.

StAXResult

can be used in all cases that accept
a

Result

, e.g.

Transformer

,

Validator

which accept

Result

as input.

**All Implemented Interfaces:** Result

---

### Field Details

#### public static final
String
FEATURE

If

TransformerFactory.getFeature(String name)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public StAXResult​(
XMLEventWriter
xmlEventWriter)

Creates a new instance of a

StAXResult

by supplying an

XMLEventWriter

.

XMLEventWriter

must be a
non-

null

reference.

**Parameters:**
- xmlEventWriter

-

XMLEventWriter

used to create
this

StAXResult

.

**Throws:**
- IllegalArgumentException

- If

xmlEventWriter

==

null

.

---

#### public StAXResult​(
XMLStreamWriter
xmlStreamWriter)

Creates a new instance of a

StAXResult

by supplying an

XMLStreamWriter

.

XMLStreamWriter

must be a
non-

null

reference.

**Parameters:**
- xmlStreamWriter

-

XMLStreamWriter

used to create
this

StAXResult

.

**Throws:**
- IllegalArgumentException

- If

xmlStreamWriter

==

null

.

---

### Method Details

#### public
XMLEventWriter
getXMLEventWriter()

Get the

XMLEventWriter

used by this

StAXResult

.

XMLEventWriter

will be

null

if this

StAXResult

was created with a

XMLStreamWriter

.

**Returns:**
- XMLEventWriter

used by this

StAXResult

.

---

#### public
XMLStreamWriter
getXMLStreamWriter()

Get the

XMLStreamWriter

used by this

StAXResult

.

XMLStreamWriter

will be

null

if this

StAXResult

was created with a

XMLEventWriter

.

**Returns:**
- XMLStreamWriter

used by this

StAXResult

.

---

#### public void setSystemId​(
String
systemId)

In the context of a

StAXResult

, it is not appropriate
to explicitly set the system identifier.
The

XMLEventWriter

or

XMLStreamWriter

used to construct this

StAXResult

determines the
system identifier of the XML result.

An

UnsupportedOperationException

is

always

thrown by this method.

**Specified by:**
- setSystemId

in interface

Result

**Parameters:**
- systemId

- Ignored.

**Throws:**
- UnsupportedOperationException

- Is

always

thrown by this method.

---

#### public
String
getSystemId()

The returned system identifier is always

null

.

**Specified by:**
- getSystemId

in interface

Result

**Returns:**
- The returned system identifier is always

null

.

---

### Additional Sections

#### Class StAXResult

java.lang.Object

- javax.xml.transform.stax.StAXResult

javax.xml.transform.stax.StAXResult

**All Implemented Interfaces:** Result

```java
public class
StAXResult

extends
Object

implements
Result
```

Acts as a holder for an XML

Result

in the
form of a StAX writer,i.e.

XMLStreamWriter

or

XMLEventWriter

.

StAXResult

can be used in all cases that accept
a

Result

, e.g.

Transformer

,

Validator

which accept

Result

as input.

**Since:** 1.6
**See Also:** JSR 173: Streaming API for XML

,

XMLStreamWriter

,

XMLEventWriter

public class

StAXResult

extends

Object

implements

Result

Acts as a holder for an XML

Result

in the
form of a StAX writer,i.e.

XMLStreamWriter

or

XMLEventWriter

.

StAXResult

can be used in all cases that accept
a

Result

, e.g.

Transformer

,

Validator

which accept

Result

as input.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

FEATURE

If

TransformerFactory.getFeature(String name)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

- Fields declared in interface javax.xml.transform.

Result

PI_DISABLE_OUTPUT_ESCAPING

,

PI_ENABLE_OUTPUT_ESCAPING

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StAXResult

​(

XMLEventWriter

xmlEventWriter)

Creates a new instance of a

StAXResult

by supplying an

XMLEventWriter

.

StAXResult

​(

XMLStreamWriter

xmlStreamWriter)

Creates a new instance of a

StAXResult

by supplying an

XMLStreamWriter

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

getSystemId

()

The returned system identifier is always

null

.

XMLEventWriter

getXMLEventWriter

()

Get the

XMLEventWriter

used by this

StAXResult

.

XMLStreamWriter

getXMLStreamWriter

()

Get the

XMLStreamWriter

used by this

StAXResult

.

void

setSystemId

​(

String

systemId)

In the context of a

StAXResult

, it is not appropriate
to explicitly set the system identifier.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

FEATURE

If

TransformerFactory.getFeature(String name)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

- Fields declared in interface javax.xml.transform.

Result

PI_DISABLE_OUTPUT_ESCAPING

,

PI_ENABLE_OUTPUT_ESCAPING

---

#### Field Summary

If

TransformerFactory.getFeature(String name)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

Fields declared in interface javax.xml.transform.

Result

PI_DISABLE_OUTPUT_ESCAPING

,

PI_ENABLE_OUTPUT_ESCAPING

---

#### Fields declared in interface javax.xml.transform. Result

Constructor Summary

Constructors

Constructor

Description

StAXResult

​(

XMLEventWriter

xmlEventWriter)

Creates a new instance of a

StAXResult

by supplying an

XMLEventWriter

.

StAXResult

​(

XMLStreamWriter

xmlStreamWriter)

Creates a new instance of a

StAXResult

by supplying an

XMLStreamWriter

.

---

#### Constructor Summary

Creates a new instance of a

StAXResult

by supplying an

XMLEventWriter

.

Creates a new instance of a

StAXResult

by supplying an

XMLStreamWriter

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getSystemId

()

The returned system identifier is always

null

.

XMLEventWriter

getXMLEventWriter

()

Get the

XMLEventWriter

used by this

StAXResult

.

XMLStreamWriter

getXMLStreamWriter

()

Get the

XMLStreamWriter

used by this

StAXResult

.

void

setSystemId

​(

String

systemId)

In the context of a

StAXResult

, it is not appropriate
to explicitly set the system identifier.

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

The returned system identifier is always

null

.

Get the

XMLEventWriter

used by this

StAXResult

.

Get the

XMLStreamWriter

used by this

StAXResult

.

In the context of a

StAXResult

, it is not appropriate
to explicitly set the system identifier.

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

============ FIELD DETAIL ===========

- Field Detail

- FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(String name)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StAXResult

```java
public StAXResult​(
XMLEventWriter
xmlEventWriter)
```

Creates a new instance of a

StAXResult

by supplying an

XMLEventWriter

.

XMLEventWriter

must be a
non-

null

reference.

**Parameters:** xmlEventWriter

-

XMLEventWriter

used to create
this

StAXResult

.
**Throws:** IllegalArgumentException

- If

xmlEventWriter

==

null

.

- StAXResult

```java
public StAXResult​(
XMLStreamWriter
xmlStreamWriter)
```

Creates a new instance of a

StAXResult

by supplying an

XMLStreamWriter

.

XMLStreamWriter

must be a
non-

null

reference.

**Parameters:** xmlStreamWriter

-

XMLStreamWriter

used to create
this

StAXResult

.
**Throws:** IllegalArgumentException

- If

xmlStreamWriter

==

null

.

============ METHOD DETAIL ==========

- Method Detail

- getXMLEventWriter

```java
public
XMLEventWriter
getXMLEventWriter()
```

Get the

XMLEventWriter

used by this

StAXResult

.

XMLEventWriter

will be

null

if this

StAXResult

was created with a

XMLStreamWriter

.

**Returns:** XMLEventWriter

used by this

StAXResult

.

- getXMLStreamWriter

```java
public
XMLStreamWriter
getXMLStreamWriter()
```

Get the

XMLStreamWriter

used by this

StAXResult

.

XMLStreamWriter

will be

null

if this

StAXResult

was created with a

XMLEventWriter

.

**Returns:** XMLStreamWriter

used by this

StAXResult

.

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

In the context of a

StAXResult

, it is not appropriate
to explicitly set the system identifier.
The

XMLEventWriter

or

XMLStreamWriter

used to construct this

StAXResult

determines the
system identifier of the XML result.

An

UnsupportedOperationException

is

always

thrown by this method.

**Specified by:** setSystemId

in interface

Result
**Parameters:** systemId

- Ignored.
**Throws:** UnsupportedOperationException

- Is

always

thrown by this method.

- getSystemId

```java
public
String
getSystemId()
```

The returned system identifier is always

null

.

**Specified by:** getSystemId

in interface

Result
**Returns:** The returned system identifier is always

null

.

Field Detail

- FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(String name)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

**See Also:** Constant Field Values

---

#### Field Detail

FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(String name)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

**See Also:** Constant Field Values

---

#### FEATURE

public static final

String

FEATURE

If

TransformerFactory.getFeature(String name)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

Constructor Detail

- StAXResult

```java
public StAXResult​(
XMLEventWriter
xmlEventWriter)
```

Creates a new instance of a

StAXResult

by supplying an

XMLEventWriter

.

XMLEventWriter

must be a
non-

null

reference.

**Parameters:** xmlEventWriter

-

XMLEventWriter

used to create
this

StAXResult

.
**Throws:** IllegalArgumentException

- If

xmlEventWriter

==

null

.

- StAXResult

```java
public StAXResult​(
XMLStreamWriter
xmlStreamWriter)
```

Creates a new instance of a

StAXResult

by supplying an

XMLStreamWriter

.

XMLStreamWriter

must be a
non-

null

reference.

**Parameters:** xmlStreamWriter

-

XMLStreamWriter

used to create
this

StAXResult

.
**Throws:** IllegalArgumentException

- If

xmlStreamWriter

==

null

.

---

#### Constructor Detail

StAXResult

```java
public StAXResult​(
XMLEventWriter
xmlEventWriter)
```

Creates a new instance of a

StAXResult

by supplying an

XMLEventWriter

.

XMLEventWriter

must be a
non-

null

reference.

**Parameters:** xmlEventWriter

-

XMLEventWriter

used to create
this

StAXResult

.
**Throws:** IllegalArgumentException

- If

xmlEventWriter

==

null

.

---

#### StAXResult

public StAXResult​(

XMLEventWriter

xmlEventWriter)

Creates a new instance of a

StAXResult

by supplying an

XMLEventWriter

.

XMLEventWriter

must be a
non-

null

reference.

Creates a new instance of a

StAXResult

by supplying an

XMLEventWriter

.

XMLEventWriter

must be a
non-

null

reference.

StAXResult

```java
public StAXResult​(
XMLStreamWriter
xmlStreamWriter)
```

Creates a new instance of a

StAXResult

by supplying an

XMLStreamWriter

.

XMLStreamWriter

must be a
non-

null

reference.

**Parameters:** xmlStreamWriter

-

XMLStreamWriter

used to create
this

StAXResult

.
**Throws:** IllegalArgumentException

- If

xmlStreamWriter

==

null

.

---

#### StAXResult

public StAXResult​(

XMLStreamWriter

xmlStreamWriter)

Creates a new instance of a

StAXResult

by supplying an

XMLStreamWriter

.

XMLStreamWriter

must be a
non-

null

reference.

Creates a new instance of a

StAXResult

by supplying an

XMLStreamWriter

.

XMLStreamWriter

must be a
non-

null

reference.

Method Detail

- getXMLEventWriter

```java
public
XMLEventWriter
getXMLEventWriter()
```

Get the

XMLEventWriter

used by this

StAXResult

.

XMLEventWriter

will be

null

if this

StAXResult

was created with a

XMLStreamWriter

.

**Returns:** XMLEventWriter

used by this

StAXResult

.

- getXMLStreamWriter

```java
public
XMLStreamWriter
getXMLStreamWriter()
```

Get the

XMLStreamWriter

used by this

StAXResult

.

XMLStreamWriter

will be

null

if this

StAXResult

was created with a

XMLEventWriter

.

**Returns:** XMLStreamWriter

used by this

StAXResult

.

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

In the context of a

StAXResult

, it is not appropriate
to explicitly set the system identifier.
The

XMLEventWriter

or

XMLStreamWriter

used to construct this

StAXResult

determines the
system identifier of the XML result.

An

UnsupportedOperationException

is

always

thrown by this method.

**Specified by:** setSystemId

in interface

Result
**Parameters:** systemId

- Ignored.
**Throws:** UnsupportedOperationException

- Is

always

thrown by this method.

- getSystemId

```java
public
String
getSystemId()
```

The returned system identifier is always

null

.

**Specified by:** getSystemId

in interface

Result
**Returns:** The returned system identifier is always

null

.

---

#### Method Detail

getXMLEventWriter

```java
public
XMLEventWriter
getXMLEventWriter()
```

Get the

XMLEventWriter

used by this

StAXResult

.

XMLEventWriter

will be

null

if this

StAXResult

was created with a

XMLStreamWriter

.

**Returns:** XMLEventWriter

used by this

StAXResult

.

---

#### getXMLEventWriter

public

XMLEventWriter

getXMLEventWriter()

Get the

XMLEventWriter

used by this

StAXResult

.

XMLEventWriter

will be

null

if this

StAXResult

was created with a

XMLStreamWriter

.

Get the

XMLEventWriter

used by this

StAXResult

.

XMLEventWriter

will be

null

if this

StAXResult

was created with a

XMLStreamWriter

.

getXMLStreamWriter

```java
public
XMLStreamWriter
getXMLStreamWriter()
```

Get the

XMLStreamWriter

used by this

StAXResult

.

XMLStreamWriter

will be

null

if this

StAXResult

was created with a

XMLEventWriter

.

**Returns:** XMLStreamWriter

used by this

StAXResult

.

---

#### getXMLStreamWriter

public

XMLStreamWriter

getXMLStreamWriter()

Get the

XMLStreamWriter

used by this

StAXResult

.

XMLStreamWriter

will be

null

if this

StAXResult

was created with a

XMLEventWriter

.

Get the

XMLStreamWriter

used by this

StAXResult

.

XMLStreamWriter

will be

null

if this

StAXResult

was created with a

XMLEventWriter

.

setSystemId

```java
public void setSystemId​(
String
systemId)
```

In the context of a

StAXResult

, it is not appropriate
to explicitly set the system identifier.
The

XMLEventWriter

or

XMLStreamWriter

used to construct this

StAXResult

determines the
system identifier of the XML result.

An

UnsupportedOperationException

is

always

thrown by this method.

**Specified by:** setSystemId

in interface

Result
**Parameters:** systemId

- Ignored.
**Throws:** UnsupportedOperationException

- Is

always

thrown by this method.

---

#### setSystemId

public void setSystemId​(

String

systemId)

In the context of a

StAXResult

, it is not appropriate
to explicitly set the system identifier.
The

XMLEventWriter

or

XMLStreamWriter

used to construct this

StAXResult

determines the
system identifier of the XML result.

An

UnsupportedOperationException

is

always

thrown by this method.

In the context of a

StAXResult

, it is not appropriate
to explicitly set the system identifier.
The

XMLEventWriter

or

XMLStreamWriter

used to construct this

StAXResult

determines the
system identifier of the XML result.

An

UnsupportedOperationException

is

always

thrown by this method.

getSystemId

```java
public
String
getSystemId()
```

The returned system identifier is always

null

.

**Specified by:** getSystemId

in interface

Result
**Returns:** The returned system identifier is always

null

.

---

#### getSystemId

public

String

getSystemId()

The returned system identifier is always

null

.

---

