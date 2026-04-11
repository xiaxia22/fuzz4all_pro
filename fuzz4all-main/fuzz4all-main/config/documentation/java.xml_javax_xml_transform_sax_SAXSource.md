# Class SAXSource

**Source:** `java.xml\javax\xml\transform\sax\SAXSource.html`

### Class Description

```java
public class
SAXSource

extends
Object

implements
Source
```

Acts as an holder for SAX-style Source.

Note that XSLT requires namespace support. Attempting to transform an
input source that is not
generated with a namespace-aware parser may result in errors.
Parsers can be made namespace aware by calling the

SAXParserFactory.setNamespaceAware(boolean awareness)

method.

**All Implemented Interfaces:** Source

---

### Field Details

#### public static final
String
FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public SAXSource()

Zero-argument default constructor. If this constructor is used, and
no SAX source is set using

setInputSource(InputSource inputSource)

, then the

Transformer

will
create an empty source

InputSource

using

new InputSource()

.

**See Also:**
- Transformer.transform(Source xmlSource, Result outputTarget)

---

#### public SAXSource​(
XMLReader
reader,

InputSource
inputSource)

Create a

SAXSource

, using an

XMLReader

and a SAX InputSource. The

Transformer

or

SAXTransformerFactory

will set itself
to be the reader's

ContentHandler

, and then will call
reader.parse(inputSource).

**Parameters:**
- reader

- An XMLReader to be used for the parse.
- inputSource

- A SAX input source reference that must be non-null
and that will be passed to the reader parse method.

---

#### public SAXSource​(
InputSource
inputSource)

Create a

SAXSource

, using a SAX

InputSource

.
The

Transformer

or

SAXTransformerFactory

creates a
reader (if setXMLReader is not used), sets itself as
the reader's

ContentHandler

, and calls
reader.parse(inputSource).

**Parameters:**
- inputSource

- An input source reference that must be non-null
and that will be passed to the parse method of the reader.

---

### Method Details

#### public void setXMLReader​(
XMLReader
reader)

Set the XMLReader to be used for the Source.

**Parameters:**
- reader

- A valid XMLReader or XMLFilter reference.

---

#### public
XMLReader
getXMLReader()

Get the XMLReader to be used for the Source.

**Returns:**
- A valid XMLReader or XMLFilter reference, or null.

---

#### public void setInputSource​(
InputSource
inputSource)

Set the SAX InputSource to be used for the Source.

**Parameters:**
- inputSource

- A valid InputSource reference.

---

#### public
InputSource
getInputSource()

Get the SAX InputSource to be used for the Source.

**Returns:**
- A valid InputSource reference, or null.

---

#### public void setSystemId​(
String
systemId)

Set the system identifier for this Source. If an input source
has already been set, it will set the system ID or that
input source, otherwise it will create a new input source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
no byte stream or character stream is specified).

**Specified by:**
- setSystemId

in interface

Source

**Parameters:**
- systemId

- The system identifier as a URI string.

---

#### public
String
getSystemId()

Get the base ID (URI or system ID) from where URIs
will be resolved.

**Specified by:**
- getSystemId

in interface

Source

**Returns:**
- Base URL for the

Source

, or

null

.

---

#### public static
InputSource
sourceToInputSource​(
Source
source)

Attempt to obtain a SAX InputSource object from a Source
object.

**Parameters:**
- source

- Must be a non-null Source reference.

**Returns:**
- An InputSource, or null if Source can not be converted.

---

#### public boolean isEmpty()

Indicates whether the

SAXSource

object is empty. Empty is
defined as follows:

- if the system identifier and

InputSource

are

null

;
- if the system identifier is

null

, and the

InputSource

is empty.

**Specified by:**
- isEmpty

in interface

Source

**Returns:**
- true if the

SAXSource

object is empty, false otherwise

---

### Additional Sections

#### Class SAXSource

java.lang.Object

- javax.xml.transform.sax.SAXSource

javax.xml.transform.sax.SAXSource

**All Implemented Interfaces:** Source

```java
public class
SAXSource

extends
Object

implements
Source
```

Acts as an holder for SAX-style Source.

Note that XSLT requires namespace support. Attempting to transform an
input source that is not
generated with a namespace-aware parser may result in errors.
Parsers can be made namespace aware by calling the

SAXParserFactory.setNamespaceAware(boolean awareness)

method.

**Since:** 1.4

public class

SAXSource

extends

Object

implements

Source

Acts as an holder for SAX-style Source.

Note that XSLT requires namespace support. Attempting to transform an
input source that is not
generated with a namespace-aware parser may result in errors.
Parsers can be made namespace aware by calling the

SAXParserFactory.setNamespaceAware(boolean awareness)

method.

Acts as an holder for SAX-style Source.

Note that XSLT requires namespace support. Attempting to transform an
input source that is not
generated with a namespace-aware parser may result in errors.
Parsers can be made namespace aware by calling the

SAXParserFactory.setNamespaceAware(boolean awareness)

method.

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

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SAXSource

()

Zero-argument default constructor.

SAXSource

​(

InputSource

inputSource)

Create a

SAXSource

, using a SAX

InputSource

.

SAXSource

​(

XMLReader

reader,

InputSource

inputSource)

Create a

SAXSource

, using an

XMLReader

and a SAX InputSource.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

InputSource

getInputSource

()

Get the SAX InputSource to be used for the Source.

String

getSystemId

()

Get the base ID (URI or system ID) from where URIs
will be resolved.

XMLReader

getXMLReader

()

Get the XMLReader to be used for the Source.

boolean

isEmpty

()

Indicates whether the

SAXSource

object is empty.

void

setInputSource

​(

InputSource

inputSource)

Set the SAX InputSource to be used for the Source.

void

setSystemId

​(

String

systemId)

Set the system identifier for this Source.

void

setXMLReader

​(

XMLReader

reader)

Set the XMLReader to be used for the Source.

static

InputSource

sourceToInputSource

​(

Source

source)

Attempt to obtain a SAX InputSource object from a Source
object.

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

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

---

#### Field Summary

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

Constructor Summary

Constructors

Constructor

Description

SAXSource

()

Zero-argument default constructor.

SAXSource

​(

InputSource

inputSource)

Create a

SAXSource

, using a SAX

InputSource

.

SAXSource

​(

XMLReader

reader,

InputSource

inputSource)

Create a

SAXSource

, using an

XMLReader

and a SAX InputSource.

---

#### Constructor Summary

Zero-argument default constructor.

Create a

SAXSource

, using a SAX

InputSource

.

Create a

SAXSource

, using an

XMLReader

and a SAX InputSource.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

InputSource

getInputSource

()

Get the SAX InputSource to be used for the Source.

String

getSystemId

()

Get the base ID (URI or system ID) from where URIs
will be resolved.

XMLReader

getXMLReader

()

Get the XMLReader to be used for the Source.

boolean

isEmpty

()

Indicates whether the

SAXSource

object is empty.

void

setInputSource

​(

InputSource

inputSource)

Set the SAX InputSource to be used for the Source.

void

setSystemId

​(

String

systemId)

Set the system identifier for this Source.

void

setXMLReader

​(

XMLReader

reader)

Set the XMLReader to be used for the Source.

static

InputSource

sourceToInputSource

​(

Source

source)

Attempt to obtain a SAX InputSource object from a Source
object.

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

Get the SAX InputSource to be used for the Source.

Get the base ID (URI or system ID) from where URIs
will be resolved.

Get the XMLReader to be used for the Source.

Indicates whether the

SAXSource

object is empty.

Set the SAX InputSource to be used for the Source.

Set the system identifier for this Source.

Set the XMLReader to be used for the Source.

Attempt to obtain a SAX InputSource object from a Source
object.

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

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SAXSource

```java
public SAXSource()
```

Zero-argument default constructor. If this constructor is used, and
no SAX source is set using

setInputSource(InputSource inputSource)

, then the

Transformer

will
create an empty source

InputSource

using

new InputSource()

.

**See Also:** Transformer.transform(Source xmlSource, Result outputTarget)

- SAXSource

```java
public SAXSource​(
XMLReader
reader,

InputSource
inputSource)
```

Create a

SAXSource

, using an

XMLReader

and a SAX InputSource. The

Transformer

or

SAXTransformerFactory

will set itself
to be the reader's

ContentHandler

, and then will call
reader.parse(inputSource).

**Parameters:** reader

- An XMLReader to be used for the parse.
**Parameters:** inputSource

- A SAX input source reference that must be non-null
and that will be passed to the reader parse method.

- SAXSource

```java
public SAXSource​(
InputSource
inputSource)
```

Create a

SAXSource

, using a SAX

InputSource

.
The

Transformer

or

SAXTransformerFactory

creates a
reader (if setXMLReader is not used), sets itself as
the reader's

ContentHandler

, and calls
reader.parse(inputSource).

**Parameters:** inputSource

- An input source reference that must be non-null
and that will be passed to the parse method of the reader.

============ METHOD DETAIL ==========

- Method Detail

- setXMLReader

```java
public void setXMLReader​(
XMLReader
reader)
```

Set the XMLReader to be used for the Source.

**Parameters:** reader

- A valid XMLReader or XMLFilter reference.

- getXMLReader

```java
public
XMLReader
getXMLReader()
```

Get the XMLReader to be used for the Source.

**Returns:** A valid XMLReader or XMLFilter reference, or null.

- setInputSource

```java
public void setInputSource​(
InputSource
inputSource)
```

Set the SAX InputSource to be used for the Source.

**Parameters:** inputSource

- A valid InputSource reference.

- getInputSource

```java
public
InputSource
getInputSource()
```

Get the SAX InputSource to be used for the Source.

**Returns:** A valid InputSource reference, or null.

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the system identifier for this Source. If an input source
has already been set, it will set the system ID or that
input source, otherwise it will create a new input source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
no byte stream or character stream is specified).

**Specified by:** setSystemId

in interface

Source
**Parameters:** systemId

- The system identifier as a URI string.

- getSystemId

```java
public
String
getSystemId()
```

Get the base ID (URI or system ID) from where URIs
will be resolved.

**Specified by:** getSystemId

in interface

Source
**Returns:** Base URL for the

Source

, or

null

.

- sourceToInputSource

```java
public static
InputSource
sourceToInputSource​(
Source
source)
```

Attempt to obtain a SAX InputSource object from a Source
object.

**Parameters:** source

- Must be a non-null Source reference.
**Returns:** An InputSource, or null if Source can not be converted.

- isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

SAXSource

object is empty. Empty is
defined as follows:

- if the system identifier and

InputSource

are

null

;
- if the system identifier is

null

, and the

InputSource

is empty.

**Specified by:** isEmpty

in interface

Source
**Returns:** true if the

SAXSource

object is empty, false otherwise

Field Detail

- FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(java.lang.String)

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

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

**See Also:** Constant Field Values

---

#### FEATURE

public static final

String

FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

Constructor Detail

- SAXSource

```java
public SAXSource()
```

Zero-argument default constructor. If this constructor is used, and
no SAX source is set using

setInputSource(InputSource inputSource)

, then the

Transformer

will
create an empty source

InputSource

using

new InputSource()

.

**See Also:** Transformer.transform(Source xmlSource, Result outputTarget)

- SAXSource

```java
public SAXSource​(
XMLReader
reader,

InputSource
inputSource)
```

Create a

SAXSource

, using an

XMLReader

and a SAX InputSource. The

Transformer

or

SAXTransformerFactory

will set itself
to be the reader's

ContentHandler

, and then will call
reader.parse(inputSource).

**Parameters:** reader

- An XMLReader to be used for the parse.
**Parameters:** inputSource

- A SAX input source reference that must be non-null
and that will be passed to the reader parse method.

- SAXSource

```java
public SAXSource​(
InputSource
inputSource)
```

Create a

SAXSource

, using a SAX

InputSource

.
The

Transformer

or

SAXTransformerFactory

creates a
reader (if setXMLReader is not used), sets itself as
the reader's

ContentHandler

, and calls
reader.parse(inputSource).

**Parameters:** inputSource

- An input source reference that must be non-null
and that will be passed to the parse method of the reader.

---

#### Constructor Detail

SAXSource

```java
public SAXSource()
```

Zero-argument default constructor. If this constructor is used, and
no SAX source is set using

setInputSource(InputSource inputSource)

, then the

Transformer

will
create an empty source

InputSource

using

new InputSource()

.

**See Also:** Transformer.transform(Source xmlSource, Result outputTarget)

---

#### SAXSource

public SAXSource()

Zero-argument default constructor. If this constructor is used, and
no SAX source is set using

setInputSource(InputSource inputSource)

, then the

Transformer

will
create an empty source

InputSource

using

new InputSource()

.

SAXSource

```java
public SAXSource​(
XMLReader
reader,

InputSource
inputSource)
```

Create a

SAXSource

, using an

XMLReader

and a SAX InputSource. The

Transformer

or

SAXTransformerFactory

will set itself
to be the reader's

ContentHandler

, and then will call
reader.parse(inputSource).

**Parameters:** reader

- An XMLReader to be used for the parse.
**Parameters:** inputSource

- A SAX input source reference that must be non-null
and that will be passed to the reader parse method.

---

#### SAXSource

public SAXSource​(

XMLReader

reader,

InputSource

inputSource)

Create a

SAXSource

, using an

XMLReader

and a SAX InputSource. The

Transformer

or

SAXTransformerFactory

will set itself
to be the reader's

ContentHandler

, and then will call
reader.parse(inputSource).

SAXSource

```java
public SAXSource​(
InputSource
inputSource)
```

Create a

SAXSource

, using a SAX

InputSource

.
The

Transformer

or

SAXTransformerFactory

creates a
reader (if setXMLReader is not used), sets itself as
the reader's

ContentHandler

, and calls
reader.parse(inputSource).

**Parameters:** inputSource

- An input source reference that must be non-null
and that will be passed to the parse method of the reader.

---

#### SAXSource

public SAXSource​(

InputSource

inputSource)

Create a

SAXSource

, using a SAX

InputSource

.
The

Transformer

or

SAXTransformerFactory

creates a
reader (if setXMLReader is not used), sets itself as
the reader's

ContentHandler

, and calls
reader.parse(inputSource).

Method Detail

- setXMLReader

```java
public void setXMLReader​(
XMLReader
reader)
```

Set the XMLReader to be used for the Source.

**Parameters:** reader

- A valid XMLReader or XMLFilter reference.

- getXMLReader

```java
public
XMLReader
getXMLReader()
```

Get the XMLReader to be used for the Source.

**Returns:** A valid XMLReader or XMLFilter reference, or null.

- setInputSource

```java
public void setInputSource​(
InputSource
inputSource)
```

Set the SAX InputSource to be used for the Source.

**Parameters:** inputSource

- A valid InputSource reference.

- getInputSource

```java
public
InputSource
getInputSource()
```

Get the SAX InputSource to be used for the Source.

**Returns:** A valid InputSource reference, or null.

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the system identifier for this Source. If an input source
has already been set, it will set the system ID or that
input source, otherwise it will create a new input source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
no byte stream or character stream is specified).

**Specified by:** setSystemId

in interface

Source
**Parameters:** systemId

- The system identifier as a URI string.

- getSystemId

```java
public
String
getSystemId()
```

Get the base ID (URI or system ID) from where URIs
will be resolved.

**Specified by:** getSystemId

in interface

Source
**Returns:** Base URL for the

Source

, or

null

.

- sourceToInputSource

```java
public static
InputSource
sourceToInputSource​(
Source
source)
```

Attempt to obtain a SAX InputSource object from a Source
object.

**Parameters:** source

- Must be a non-null Source reference.
**Returns:** An InputSource, or null if Source can not be converted.

- isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

SAXSource

object is empty. Empty is
defined as follows:

- if the system identifier and

InputSource

are

null

;
- if the system identifier is

null

, and the

InputSource

is empty.

**Specified by:** isEmpty

in interface

Source
**Returns:** true if the

SAXSource

object is empty, false otherwise

---

#### Method Detail

setXMLReader

```java
public void setXMLReader​(
XMLReader
reader)
```

Set the XMLReader to be used for the Source.

**Parameters:** reader

- A valid XMLReader or XMLFilter reference.

---

#### setXMLReader

public void setXMLReader​(

XMLReader

reader)

Set the XMLReader to be used for the Source.

getXMLReader

```java
public
XMLReader
getXMLReader()
```

Get the XMLReader to be used for the Source.

**Returns:** A valid XMLReader or XMLFilter reference, or null.

---

#### getXMLReader

public

XMLReader

getXMLReader()

Get the XMLReader to be used for the Source.

setInputSource

```java
public void setInputSource​(
InputSource
inputSource)
```

Set the SAX InputSource to be used for the Source.

**Parameters:** inputSource

- A valid InputSource reference.

---

#### setInputSource

public void setInputSource​(

InputSource

inputSource)

Set the SAX InputSource to be used for the Source.

getInputSource

```java
public
InputSource
getInputSource()
```

Get the SAX InputSource to be used for the Source.

**Returns:** A valid InputSource reference, or null.

---

#### getInputSource

public

InputSource

getInputSource()

Get the SAX InputSource to be used for the Source.

setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the system identifier for this Source. If an input source
has already been set, it will set the system ID or that
input source, otherwise it will create a new input source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
no byte stream or character stream is specified).

**Specified by:** setSystemId

in interface

Source
**Parameters:** systemId

- The system identifier as a URI string.

---

#### setSystemId

public void setSystemId​(

String

systemId)

Set the system identifier for this Source. If an input source
has already been set, it will set the system ID or that
input source, otherwise it will create a new input source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
no byte stream or character stream is specified).

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
no byte stream or character stream is specified).

getSystemId

```java
public
String
getSystemId()
```

Get the base ID (URI or system ID) from where URIs
will be resolved.

**Specified by:** getSystemId

in interface

Source
**Returns:** Base URL for the

Source

, or

null

.

---

#### getSystemId

public

String

getSystemId()

Get the base ID (URI or system ID) from where URIs
will be resolved.

sourceToInputSource

```java
public static
InputSource
sourceToInputSource​(
Source
source)
```

Attempt to obtain a SAX InputSource object from a Source
object.

**Parameters:** source

- Must be a non-null Source reference.
**Returns:** An InputSource, or null if Source can not be converted.

---

#### sourceToInputSource

public static

InputSource

sourceToInputSource​(

Source

source)

Attempt to obtain a SAX InputSource object from a Source
object.

isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

SAXSource

object is empty. Empty is
defined as follows:

- if the system identifier and

InputSource

are

null

;
- if the system identifier is

null

, and the

InputSource

is empty.

**Specified by:** isEmpty

in interface

Source
**Returns:** true if the

SAXSource

object is empty, false otherwise

---

#### isEmpty

public boolean isEmpty()

Indicates whether the

SAXSource

object is empty. Empty is
defined as follows:

- if the system identifier and

InputSource

are

null

;
- if the system identifier is

null

, and the

InputSource

is empty.

if the system identifier and

InputSource

are

null

;

if the system identifier is

null

, and the

InputSource

is empty.

---

