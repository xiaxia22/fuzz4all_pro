# Class StAXSource

**Source:** `java.xml\javax\xml\transform\stax\StAXSource.html`

### Class Description

```java
public class
StAXSource

extends
Object

implements
Source
```

Acts as a holder for an XML

Source

in the
form of a StAX reader,i.e.

XMLStreamReader

or

XMLEventReader

.

StAXSource

can be used in all cases that accept
a

Source

, e.g.

Transformer

,

Validator

which accept

Source

as input.

StAXSource

s are consumed during processing
and are not reusable.

**All Implemented Interfaces:** Source

---

### Field Details

#### public static final
String
FEATURE

If

TransformerFactory.getFeature(String name)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public StAXSource​(
XMLEventReader
xmlEventReader)
throws
XMLStreamException

Creates a new instance of a

StAXSource

by supplying an

XMLEventReader

.

XMLEventReader

must be a
non-

null

reference.

XMLEventReader

must be in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

**Parameters:**
- xmlEventReader

-

XMLEventReader

used to create
this

StAXSource

.

**Throws:**
- XMLStreamException

- If

xmlEventReader

access
throws an

Exception

.
- IllegalArgumentException

- If

xmlEventReader

==

null

.
- IllegalStateException

- If

xmlEventReader

is not in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

---

#### public StAXSource​(
XMLStreamReader
xmlStreamReader)

Creates a new instance of a

StAXSource

by supplying an

XMLStreamReader

.

XMLStreamReader

must be a
non-

null

reference.

XMLStreamReader

must be in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

**Parameters:**
- xmlStreamReader

-

XMLStreamReader

used to create
this

StAXSource

.

**Throws:**
- IllegalArgumentException

- If

xmlStreamReader

==

null

.
- IllegalStateException

- If

xmlStreamReader

is not in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

---

### Method Details

#### public
XMLEventReader
getXMLEventReader()

Get the

XMLEventReader

used by this

StAXSource

.

XMLEventReader

will be

null

.
if this

StAXSource

was created with a

XMLStreamReader

.

**Returns:**
- XMLEventReader

used by this

StAXSource

.

---

#### public
XMLStreamReader
getXMLStreamReader()

Get the

XMLStreamReader

used by this

StAXSource

.

XMLStreamReader

will be

null

if this

StAXSource

was created with a

XMLEventReader

.

**Returns:**
- XMLStreamReader

used by this

StAXSource

.

---

#### public void setSystemId​(
String
systemId)

In the context of a

StAXSource

, it is not appropriate
to explicitly set the system identifier.
The

XMLStreamReader

or

XMLEventReader

used to construct this

StAXSource

determines the
system identifier of the XML source.

An

UnsupportedOperationException

is

always

thrown by this method.

**Specified by:**
- setSystemId

in interface

Source

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

Get the system identifier used by this

StAXSource

.

The

XMLStreamReader

or

XMLEventReader

used to construct this

StAXSource

is queried to determine
the system identifier of the XML source.

The system identifier may be

null

or
an empty

""

String

.

**Specified by:**
- getSystemId

in interface

Source

**Returns:**
- System identifier used by this

StAXSource

.

---

#### public boolean isEmpty()

Indicates whether the

StAXSource

object is empty. Since a

StAXSource

object can never be empty, this method always returns
false.

**Specified by:**
- isEmpty

in interface

Source

**Returns:**
- unconditionally false

---

### Additional Sections

#### Class StAXSource

java.lang.Object

- javax.xml.transform.stax.StAXSource

javax.xml.transform.stax.StAXSource

**All Implemented Interfaces:** Source

```java
public class
StAXSource

extends
Object

implements
Source
```

Acts as a holder for an XML

Source

in the
form of a StAX reader,i.e.

XMLStreamReader

or

XMLEventReader

.

StAXSource

can be used in all cases that accept
a

Source

, e.g.

Transformer

,

Validator

which accept

Source

as input.

StAXSource

s are consumed during processing
and are not reusable.

**Since:** 1.6
**See Also:** JSR 173: Streaming API for XML

,

XMLStreamReader

,

XMLEventReader

public class

StAXSource

extends

Object

implements

Source

Acts as a holder for an XML

Source

in the
form of a StAX reader,i.e.

XMLStreamReader

or

XMLEventReader

.

StAXSource

can be used in all cases that accept
a

Source

, e.g.

Transformer

,

Validator

which accept

Source

as input.

StAXSource

s are consumed during processing
and are not reusable.

StAXSource

s are consumed during processing
and are not reusable.

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
the Transformer supports Source input of this type.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StAXSource

​(

XMLEventReader

xmlEventReader)

Creates a new instance of a

StAXSource

by supplying an

XMLEventReader

.

StAXSource

​(

XMLStreamReader

xmlStreamReader)

Creates a new instance of a

StAXSource

by supplying an

XMLStreamReader

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

Get the system identifier used by this

StAXSource

.

XMLEventReader

getXMLEventReader

()

Get the

XMLEventReader

used by this

StAXSource

.

XMLStreamReader

getXMLStreamReader

()

Get the

XMLStreamReader

used by this

StAXSource

.

boolean

isEmpty

()

Indicates whether the

StAXSource

object is empty.

void

setSystemId

​(

String

systemId)

In the context of a

StAXSource

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
the Transformer supports Source input of this type.

---

#### Field Summary

If

TransformerFactory.getFeature(String name)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

Constructor Summary

Constructors

Constructor

Description

StAXSource

​(

XMLEventReader

xmlEventReader)

Creates a new instance of a

StAXSource

by supplying an

XMLEventReader

.

StAXSource

​(

XMLStreamReader

xmlStreamReader)

Creates a new instance of a

StAXSource

by supplying an

XMLStreamReader

.

---

#### Constructor Summary

Creates a new instance of a

StAXSource

by supplying an

XMLEventReader

.

Creates a new instance of a

StAXSource

by supplying an

XMLStreamReader

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

Get the system identifier used by this

StAXSource

.

XMLEventReader

getXMLEventReader

()

Get the

XMLEventReader

used by this

StAXSource

.

XMLStreamReader

getXMLStreamReader

()

Get the

XMLStreamReader

used by this

StAXSource

.

boolean

isEmpty

()

Indicates whether the

StAXSource

object is empty.

void

setSystemId

​(

String

systemId)

In the context of a

StAXSource

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

Get the system identifier used by this

StAXSource

.

Get the

XMLEventReader

used by this

StAXSource

.

Get the

XMLStreamReader

used by this

StAXSource

.

Indicates whether the

StAXSource

object is empty.

In the context of a

StAXSource

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
the Transformer supports Source input of this type.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StAXSource

```java
public StAXSource​(
XMLEventReader
xmlEventReader)
throws
XMLStreamException
```

Creates a new instance of a

StAXSource

by supplying an

XMLEventReader

.

XMLEventReader

must be a
non-

null

reference.

XMLEventReader

must be in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

**Parameters:** xmlEventReader

-

XMLEventReader

used to create
this

StAXSource

.
**Throws:** XMLStreamException

- If

xmlEventReader

access
throws an

Exception

.
**Throws:** IllegalArgumentException

- If

xmlEventReader

==

null

.
**Throws:** IllegalStateException

- If

xmlEventReader

is not in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

- StAXSource

```java
public StAXSource​(
XMLStreamReader
xmlStreamReader)
```

Creates a new instance of a

StAXSource

by supplying an

XMLStreamReader

.

XMLStreamReader

must be a
non-

null

reference.

XMLStreamReader

must be in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

**Parameters:** xmlStreamReader

-

XMLStreamReader

used to create
this

StAXSource

.
**Throws:** IllegalArgumentException

- If

xmlStreamReader

==

null

.
**Throws:** IllegalStateException

- If

xmlStreamReader

is not in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

============ METHOD DETAIL ==========

- Method Detail

- getXMLEventReader

```java
public
XMLEventReader
getXMLEventReader()
```

Get the

XMLEventReader

used by this

StAXSource

.

XMLEventReader

will be

null

.
if this

StAXSource

was created with a

XMLStreamReader

.

**Returns:** XMLEventReader

used by this

StAXSource

.

- getXMLStreamReader

```java
public
XMLStreamReader
getXMLStreamReader()
```

Get the

XMLStreamReader

used by this

StAXSource

.

XMLStreamReader

will be

null

if this

StAXSource

was created with a

XMLEventReader

.

**Returns:** XMLStreamReader

used by this

StAXSource

.

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

In the context of a

StAXSource

, it is not appropriate
to explicitly set the system identifier.
The

XMLStreamReader

or

XMLEventReader

used to construct this

StAXSource

determines the
system identifier of the XML source.

An

UnsupportedOperationException

is

always

thrown by this method.

**Specified by:** setSystemId

in interface

Source
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

Get the system identifier used by this

StAXSource

.

The

XMLStreamReader

or

XMLEventReader

used to construct this

StAXSource

is queried to determine
the system identifier of the XML source.

The system identifier may be

null

or
an empty

""

String

.

**Specified by:** getSystemId

in interface

Source
**Returns:** System identifier used by this

StAXSource

.

- isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

StAXSource

object is empty. Since a

StAXSource

object can never be empty, this method always returns
false.

**Specified by:** isEmpty

in interface

Source
**Returns:** unconditionally false

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
the Transformer supports Source input of this type.

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
the Transformer supports Source input of this type.

**See Also:** Constant Field Values

---

#### FEATURE

public static final

String

FEATURE

If

TransformerFactory.getFeature(String name)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

Constructor Detail

- StAXSource

```java
public StAXSource​(
XMLEventReader
xmlEventReader)
throws
XMLStreamException
```

Creates a new instance of a

StAXSource

by supplying an

XMLEventReader

.

XMLEventReader

must be a
non-

null

reference.

XMLEventReader

must be in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

**Parameters:** xmlEventReader

-

XMLEventReader

used to create
this

StAXSource

.
**Throws:** XMLStreamException

- If

xmlEventReader

access
throws an

Exception

.
**Throws:** IllegalArgumentException

- If

xmlEventReader

==

null

.
**Throws:** IllegalStateException

- If

xmlEventReader

is not in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

- StAXSource

```java
public StAXSource​(
XMLStreamReader
xmlStreamReader)
```

Creates a new instance of a

StAXSource

by supplying an

XMLStreamReader

.

XMLStreamReader

must be a
non-

null

reference.

XMLStreamReader

must be in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

**Parameters:** xmlStreamReader

-

XMLStreamReader

used to create
this

StAXSource

.
**Throws:** IllegalArgumentException

- If

xmlStreamReader

==

null

.
**Throws:** IllegalStateException

- If

xmlStreamReader

is not in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

---

#### Constructor Detail

StAXSource

```java
public StAXSource​(
XMLEventReader
xmlEventReader)
throws
XMLStreamException
```

Creates a new instance of a

StAXSource

by supplying an

XMLEventReader

.

XMLEventReader

must be a
non-

null

reference.

XMLEventReader

must be in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

**Parameters:** xmlEventReader

-

XMLEventReader

used to create
this

StAXSource

.
**Throws:** XMLStreamException

- If

xmlEventReader

access
throws an

Exception

.
**Throws:** IllegalArgumentException

- If

xmlEventReader

==

null

.
**Throws:** IllegalStateException

- If

xmlEventReader

is not in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

---

#### StAXSource

public StAXSource​(

XMLEventReader

xmlEventReader)
throws

XMLStreamException

Creates a new instance of a

StAXSource

by supplying an

XMLEventReader

.

XMLEventReader

must be a
non-

null

reference.

XMLEventReader

must be in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

Creates a new instance of a

StAXSource

by supplying an

XMLEventReader

.

XMLEventReader

must be a
non-

null

reference.

XMLEventReader

must be in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

StAXSource

```java
public StAXSource​(
XMLStreamReader
xmlStreamReader)
```

Creates a new instance of a

StAXSource

by supplying an

XMLStreamReader

.

XMLStreamReader

must be a
non-

null

reference.

XMLStreamReader

must be in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

**Parameters:** xmlStreamReader

-

XMLStreamReader

used to create
this

StAXSource

.
**Throws:** IllegalArgumentException

- If

xmlStreamReader

==

null

.
**Throws:** IllegalStateException

- If

xmlStreamReader

is not in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

---

#### StAXSource

public StAXSource​(

XMLStreamReader

xmlStreamReader)

Creates a new instance of a

StAXSource

by supplying an

XMLStreamReader

.

XMLStreamReader

must be a
non-

null

reference.

XMLStreamReader

must be in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

Creates a new instance of a

StAXSource

by supplying an

XMLStreamReader

.

XMLStreamReader

must be a
non-

null

reference.

XMLStreamReader

must be in

XMLStreamConstants.START_DOCUMENT

or

XMLStreamConstants.START_ELEMENT

state.

Method Detail

- getXMLEventReader

```java
public
XMLEventReader
getXMLEventReader()
```

Get the

XMLEventReader

used by this

StAXSource

.

XMLEventReader

will be

null

.
if this

StAXSource

was created with a

XMLStreamReader

.

**Returns:** XMLEventReader

used by this

StAXSource

.

- getXMLStreamReader

```java
public
XMLStreamReader
getXMLStreamReader()
```

Get the

XMLStreamReader

used by this

StAXSource

.

XMLStreamReader

will be

null

if this

StAXSource

was created with a

XMLEventReader

.

**Returns:** XMLStreamReader

used by this

StAXSource

.

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

In the context of a

StAXSource

, it is not appropriate
to explicitly set the system identifier.
The

XMLStreamReader

or

XMLEventReader

used to construct this

StAXSource

determines the
system identifier of the XML source.

An

UnsupportedOperationException

is

always

thrown by this method.

**Specified by:** setSystemId

in interface

Source
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

Get the system identifier used by this

StAXSource

.

The

XMLStreamReader

or

XMLEventReader

used to construct this

StAXSource

is queried to determine
the system identifier of the XML source.

The system identifier may be

null

or
an empty

""

String

.

**Specified by:** getSystemId

in interface

Source
**Returns:** System identifier used by this

StAXSource

.

- isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

StAXSource

object is empty. Since a

StAXSource

object can never be empty, this method always returns
false.

**Specified by:** isEmpty

in interface

Source
**Returns:** unconditionally false

---

#### Method Detail

getXMLEventReader

```java
public
XMLEventReader
getXMLEventReader()
```

Get the

XMLEventReader

used by this

StAXSource

.

XMLEventReader

will be

null

.
if this

StAXSource

was created with a

XMLStreamReader

.

**Returns:** XMLEventReader

used by this

StAXSource

.

---

#### getXMLEventReader

public

XMLEventReader

getXMLEventReader()

Get the

XMLEventReader

used by this

StAXSource

.

XMLEventReader

will be

null

.
if this

StAXSource

was created with a

XMLStreamReader

.

Get the

XMLEventReader

used by this

StAXSource

.

XMLEventReader

will be

null

.
if this

StAXSource

was created with a

XMLStreamReader

.

getXMLStreamReader

```java
public
XMLStreamReader
getXMLStreamReader()
```

Get the

XMLStreamReader

used by this

StAXSource

.

XMLStreamReader

will be

null

if this

StAXSource

was created with a

XMLEventReader

.

**Returns:** XMLStreamReader

used by this

StAXSource

.

---

#### getXMLStreamReader

public

XMLStreamReader

getXMLStreamReader()

Get the

XMLStreamReader

used by this

StAXSource

.

XMLStreamReader

will be

null

if this

StAXSource

was created with a

XMLEventReader

.

Get the

XMLStreamReader

used by this

StAXSource

.

XMLStreamReader

will be

null

if this

StAXSource

was created with a

XMLEventReader

.

setSystemId

```java
public void setSystemId​(
String
systemId)
```

In the context of a

StAXSource

, it is not appropriate
to explicitly set the system identifier.
The

XMLStreamReader

or

XMLEventReader

used to construct this

StAXSource

determines the
system identifier of the XML source.

An

UnsupportedOperationException

is

always

thrown by this method.

**Specified by:** setSystemId

in interface

Source
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

StAXSource

, it is not appropriate
to explicitly set the system identifier.
The

XMLStreamReader

or

XMLEventReader

used to construct this

StAXSource

determines the
system identifier of the XML source.

An

UnsupportedOperationException

is

always

thrown by this method.

In the context of a

StAXSource

, it is not appropriate
to explicitly set the system identifier.
The

XMLStreamReader

or

XMLEventReader

used to construct this

StAXSource

determines the
system identifier of the XML source.

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

Get the system identifier used by this

StAXSource

.

The

XMLStreamReader

or

XMLEventReader

used to construct this

StAXSource

is queried to determine
the system identifier of the XML source.

The system identifier may be

null

or
an empty

""

String

.

**Specified by:** getSystemId

in interface

Source
**Returns:** System identifier used by this

StAXSource

.

---

#### getSystemId

public

String

getSystemId()

Get the system identifier used by this

StAXSource

.

The

XMLStreamReader

or

XMLEventReader

used to construct this

StAXSource

is queried to determine
the system identifier of the XML source.

The system identifier may be

null

or
an empty

""

String

.

Get the system identifier used by this

StAXSource

.

The

XMLStreamReader

or

XMLEventReader

used to construct this

StAXSource

is queried to determine
the system identifier of the XML source.

The system identifier may be

null

or
an empty

""

String

.

isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

StAXSource

object is empty. Since a

StAXSource

object can never be empty, this method always returns
false.

**Specified by:** isEmpty

in interface

Source
**Returns:** unconditionally false

---

#### isEmpty

public boolean isEmpty()

Indicates whether the

StAXSource

object is empty. Since a

StAXSource

object can never be empty, this method always returns
false.

---

