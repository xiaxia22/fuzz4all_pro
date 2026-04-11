# Class DocumentBuilder

**Source:** `java.xml\javax\xml\parsers\DocumentBuilder.html`

### Class Description

```java
public abstract class
DocumentBuilder

extends
Object
```

Defines the API to obtain DOM Document instances from an XML
document. Using this class, an application programmer can obtain a

Document

from XML.

An instance of this class can be obtained from the

DocumentBuilderFactory.newDocumentBuilder()

method. Once
an instance of this class is obtained, XML can be parsed from a
variety of input sources. These input sources are InputStreams,
Files, URLs, and SAX InputSources.

Note that this class reuses several classes from the SAX API. This
does not require that the implementor of the underlying DOM
implementation use a SAX parser to parse XML document into a

Document

. It merely requires that the implementation
communicate with the application using these existing APIs.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### protected DocumentBuilder()

Protected constructor

---

### Method Details

#### public void reset()

Reset this

DocumentBuilder

to its original configuration.

DocumentBuilder

is reset to the same state as when it was created with

DocumentBuilderFactory.newDocumentBuilder()

.

reset()

is designed to allow the reuse of existing

DocumentBuilder

s
thus saving resources associated with the creation of new

DocumentBuilder

s.

The reset

DocumentBuilder

is not guaranteed to have the same

EntityResolver

or

ErrorHandler

Object

s, e.g.

Object.equals(Object obj)

. It is guaranteed to have a functionally equal

EntityResolver

and

ErrorHandler

.

**Throws:**
- UnsupportedOperationException

- When implementation does not
override this method.

**Since:**
- 1.5

---

#### public
Document
parse​(
InputStream
is)
throws
SAXException
,

IOException

Parse the content of the given

InputStream

as an XML
document and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputStream

is null.

**Parameters:**
- is

- InputStream containing the content to be parsed.

**Returns:**
- Document

result of parsing the

InputStream

**Throws:**
- IOException

- If any IO errors occur.
- SAXException

- If any parse errors occur.
- IllegalArgumentException

- When

is

is

null

**See Also:**
- DocumentHandler

---

#### public
Document
parse​(
InputStream
is,

String
systemId)
throws
SAXException
,

IOException

Parse the content of the given

InputStream

as an
XML document and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputStream

is null.

**Parameters:**
- is

- InputStream containing the content to be parsed.
- systemId

- Provide a base for resolving relative URIs.

**Returns:**
- A new DOM Document object.

**Throws:**
- IOException

- If any IO errors occur.
- SAXException

- If any parse errors occur.
- IllegalArgumentException

- When

is

is

null

**See Also:**
- DocumentHandler

---

#### public
Document
parse​(
String
uri)
throws
SAXException
,

IOException

Parse the content of the given URI as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the
URI is

null

null.

**Parameters:**
- uri

- The location of the content to be parsed.

**Returns:**
- A new DOM Document object.

**Throws:**
- IOException

- If any IO errors occur.
- SAXException

- If any parse errors occur.
- IllegalArgumentException

- When

uri

is

null

**See Also:**
- DocumentHandler

---

#### public
Document
parse​(
File
f)
throws
SAXException
,

IOException

Parse the content of the given file as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

File

is

null

null.

**Parameters:**
- f

- The file containing the XML to parse.

**Returns:**
- A new DOM Document object.

**Throws:**
- IOException

- If any IO errors occur.
- SAXException

- If any parse errors occur.
- IllegalArgumentException

- When

f

is

null

**See Also:**
- DocumentHandler

---

#### public abstract
Document
parse​(
InputSource
is)
throws
SAXException
,

IOException

Parse the content of the given input source as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputSource

is

null

null.

**Parameters:**
- is

- InputSource containing the content to be parsed.

**Returns:**
- A new DOM Document object.

**Throws:**
- IOException

- If any IO errors occur.
- SAXException

- If any parse errors occur.
- IllegalArgumentException

- When

is

is

null

**See Also:**
- DocumentHandler

---

#### public abstract boolean isNamespaceAware()

Indicates whether or not this parser is configured to
understand namespaces.

**Returns:**
- true if this parser is configured to understand
namespaces; false otherwise.

---

#### public abstract boolean isValidating()

Indicates whether or not this parser is configured to
validate XML documents.

**Returns:**
- true if this parser is configured to validate
XML documents; false otherwise.

---

#### public abstract void setEntityResolver​(
EntityResolver
er)

Specify the

EntityResolver

to be used to resolve
entities present in the XML document to be parsed. Setting
this to

null

will result in the underlying
implementation using it's own default implementation and
behavior.

**Parameters:**
- er

- The

EntityResolver

to be used to resolve entities
present in the XML document to be parsed.

---

#### public abstract void setErrorHandler​(
ErrorHandler
eh)

Specify the

ErrorHandler

to be used by the parser.
Setting this to

null

will result in the underlying
implementation using it's own default implementation and
behavior.

**Parameters:**
- eh

- The

ErrorHandler

to be used by the parser.

---

#### public abstract
Document
newDocument()

Obtain a new instance of a DOM

Document

object
to build a DOM tree with.

**Returns:**
- A new instance of a DOM Document object.

---

#### public abstract
DOMImplementation
getDOMImplementation()

Obtain an instance of a

DOMImplementation

object.

**Returns:**
- A new instance of a

DOMImplementation

.

---

#### public
Schema
getSchema()

Get a reference to the the

Schema

being used by
the XML processor.

If no schema is being used,

null

is returned.

**Returns:**
- Schema

being used or

null

if none in use

**Throws:**
- UnsupportedOperationException

- When implementation does not
override this method

**Since:**
- 1.5

---

#### public boolean isXIncludeAware()

Get the XInclude processing mode for this parser.

**Returns:**
- the return value of
the

DocumentBuilderFactory.isXIncludeAware()

when this parser was created from factory.

**Throws:**
- UnsupportedOperationException

- When implementation does not
override this method

**See Also:**
- DocumentBuilderFactory.setXIncludeAware(boolean)

**Since:**
- 1.5

---

### Additional Sections

#### Class DocumentBuilder

java.lang.Object

- javax.xml.parsers.DocumentBuilder

javax.xml.parsers.DocumentBuilder

```java
public abstract class
DocumentBuilder

extends
Object
```

Defines the API to obtain DOM Document instances from an XML
document. Using this class, an application programmer can obtain a

Document

from XML.

An instance of this class can be obtained from the

DocumentBuilderFactory.newDocumentBuilder()

method. Once
an instance of this class is obtained, XML can be parsed from a
variety of input sources. These input sources are InputStreams,
Files, URLs, and SAX InputSources.

Note that this class reuses several classes from the SAX API. This
does not require that the implementor of the underlying DOM
implementation use a SAX parser to parse XML document into a

Document

. It merely requires that the implementation
communicate with the application using these existing APIs.

**Since:** 1.4

public abstract class

DocumentBuilder

extends

Object

Defines the API to obtain DOM Document instances from an XML
document. Using this class, an application programmer can obtain a

Document

from XML.

An instance of this class can be obtained from the

DocumentBuilderFactory.newDocumentBuilder()

method. Once
an instance of this class is obtained, XML can be parsed from a
variety of input sources. These input sources are InputStreams,
Files, URLs, and SAX InputSources.

Note that this class reuses several classes from the SAX API. This
does not require that the implementor of the underlying DOM
implementation use a SAX parser to parse XML document into a

Document

. It merely requires that the implementation
communicate with the application using these existing APIs.

An instance of this class can be obtained from the

DocumentBuilderFactory.newDocumentBuilder()

method. Once
an instance of this class is obtained, XML can be parsed from a
variety of input sources. These input sources are InputStreams,
Files, URLs, and SAX InputSources.

Note that this class reuses several classes from the SAX API. This
does not require that the implementor of the underlying DOM
implementation use a SAX parser to parse XML document into a

Document

. It merely requires that the implementation
communicate with the application using these existing APIs.

Note that this class reuses several classes from the SAX API. This
does not require that the implementor of the underlying DOM
implementation use a SAX parser to parse XML document into a

Document

. It merely requires that the implementation
communicate with the application using these existing APIs.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DocumentBuilder

()

Protected constructor

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

DOMImplementation

getDOMImplementation

()

Obtain an instance of a

DOMImplementation

object.

Schema

getSchema

()

Get a reference to the the

Schema

being used by
the XML processor.

abstract boolean

isNamespaceAware

()

Indicates whether or not this parser is configured to
understand namespaces.

abstract boolean

isValidating

()

Indicates whether or not this parser is configured to
validate XML documents.

boolean

isXIncludeAware

()

Get the XInclude processing mode for this parser.

abstract

Document

newDocument

()

Obtain a new instance of a DOM

Document

object
to build a DOM tree with.

Document

parse

​(

File

f)

Parse the content of the given file as an XML document
and return a new DOM

Document

object.

Document

parse

​(

InputStream

is)

Parse the content of the given

InputStream

as an XML
document and return a new DOM

Document

object.

Document

parse

​(

InputStream

is,

String

systemId)

Parse the content of the given

InputStream

as an
XML document and return a new DOM

Document

object.

Document

parse

​(

String

uri)

Parse the content of the given URI as an XML document
and return a new DOM

Document

object.

abstract

Document

parse

​(

InputSource

is)

Parse the content of the given input source as an XML document
and return a new DOM

Document

object.

void

reset

()

Reset this

DocumentBuilder

to its original configuration.

abstract void

setEntityResolver

​(

EntityResolver

er)

Specify the

EntityResolver

to be used to resolve
entities present in the XML document to be parsed.

abstract void

setErrorHandler

​(

ErrorHandler

eh)

Specify the

ErrorHandler

to be used by the parser.

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

Modifier

Constructor

Description

protected

DocumentBuilder

()

Protected constructor

---

#### Constructor Summary

Protected constructor

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

DOMImplementation

getDOMImplementation

()

Obtain an instance of a

DOMImplementation

object.

Schema

getSchema

()

Get a reference to the the

Schema

being used by
the XML processor.

abstract boolean

isNamespaceAware

()

Indicates whether or not this parser is configured to
understand namespaces.

abstract boolean

isValidating

()

Indicates whether or not this parser is configured to
validate XML documents.

boolean

isXIncludeAware

()

Get the XInclude processing mode for this parser.

abstract

Document

newDocument

()

Obtain a new instance of a DOM

Document

object
to build a DOM tree with.

Document

parse

​(

File

f)

Parse the content of the given file as an XML document
and return a new DOM

Document

object.

Document

parse

​(

InputStream

is)

Parse the content of the given

InputStream

as an XML
document and return a new DOM

Document

object.

Document

parse

​(

InputStream

is,

String

systemId)

Parse the content of the given

InputStream

as an
XML document and return a new DOM

Document

object.

Document

parse

​(

String

uri)

Parse the content of the given URI as an XML document
and return a new DOM

Document

object.

abstract

Document

parse

​(

InputSource

is)

Parse the content of the given input source as an XML document
and return a new DOM

Document

object.

void

reset

()

Reset this

DocumentBuilder

to its original configuration.

abstract void

setEntityResolver

​(

EntityResolver

er)

Specify the

EntityResolver

to be used to resolve
entities present in the XML document to be parsed.

abstract void

setErrorHandler

​(

ErrorHandler

eh)

Specify the

ErrorHandler

to be used by the parser.

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

Obtain an instance of a

DOMImplementation

object.

Get a reference to the the

Schema

being used by
the XML processor.

Indicates whether or not this parser is configured to
understand namespaces.

Indicates whether or not this parser is configured to
validate XML documents.

Get the XInclude processing mode for this parser.

Obtain a new instance of a DOM

Document

object
to build a DOM tree with.

Parse the content of the given file as an XML document
and return a new DOM

Document

object.

Parse the content of the given

InputStream

as an XML
document and return a new DOM

Document

object.

Parse the content of the given

InputStream

as an
XML document and return a new DOM

Document

object.

Parse the content of the given URI as an XML document
and return a new DOM

Document

object.

Parse the content of the given input source as an XML document
and return a new DOM

Document

object.

Reset this

DocumentBuilder

to its original configuration.

Specify the

EntityResolver

to be used to resolve
entities present in the XML document to be parsed.

Specify the

ErrorHandler

to be used by the parser.

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

- DocumentBuilder

```java
protected DocumentBuilder()
```

Protected constructor

============ METHOD DETAIL ==========

- Method Detail

- reset

```java
public void reset()
```

Reset this

DocumentBuilder

to its original configuration.

DocumentBuilder

is reset to the same state as when it was created with

DocumentBuilderFactory.newDocumentBuilder()

.

reset()

is designed to allow the reuse of existing

DocumentBuilder

s
thus saving resources associated with the creation of new

DocumentBuilder

s.

The reset

DocumentBuilder

is not guaranteed to have the same

EntityResolver

or

ErrorHandler

Object

s, e.g.

Object.equals(Object obj)

. It is guaranteed to have a functionally equal

EntityResolver

and

ErrorHandler

.

**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

- parse

```java
public
Document
parse​(
InputStream
is)
throws
SAXException
,

IOException
```

Parse the content of the given

InputStream

as an XML
document and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputStream

is null.

**Parameters:** is

- InputStream containing the content to be parsed.
**Returns:** Document

result of parsing the

InputStream
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

is

is

null
**See Also:** DocumentHandler

- parse

```java
public
Document
parse​(
InputStream
is,

String
systemId)
throws
SAXException
,

IOException
```

Parse the content of the given

InputStream

as an
XML document and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputStream

is null.

**Parameters:** is

- InputStream containing the content to be parsed.
**Parameters:** systemId

- Provide a base for resolving relative URIs.
**Returns:** A new DOM Document object.
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

is

is

null
**See Also:** DocumentHandler

- parse

```java
public
Document
parse​(
String
uri)
throws
SAXException
,

IOException
```

Parse the content of the given URI as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the
URI is

null

null.

**Parameters:** uri

- The location of the content to be parsed.
**Returns:** A new DOM Document object.
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

uri

is

null
**See Also:** DocumentHandler

- parse

```java
public
Document
parse​(
File
f)
throws
SAXException
,

IOException
```

Parse the content of the given file as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

File

is

null

null.

**Parameters:** f

- The file containing the XML to parse.
**Returns:** A new DOM Document object.
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

f

is

null
**See Also:** DocumentHandler

- parse

```java
public abstract
Document
parse​(
InputSource
is)
throws
SAXException
,

IOException
```

Parse the content of the given input source as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputSource

is

null

null.

**Parameters:** is

- InputSource containing the content to be parsed.
**Returns:** A new DOM Document object.
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

is

is

null
**See Also:** DocumentHandler

- isNamespaceAware

```java
public abstract boolean isNamespaceAware()
```

Indicates whether or not this parser is configured to
understand namespaces.

**Returns:** true if this parser is configured to understand
namespaces; false otherwise.

- isValidating

```java
public abstract boolean isValidating()
```

Indicates whether or not this parser is configured to
validate XML documents.

**Returns:** true if this parser is configured to validate
XML documents; false otherwise.

- setEntityResolver

```java
public abstract void setEntityResolver​(
EntityResolver
er)
```

Specify the

EntityResolver

to be used to resolve
entities present in the XML document to be parsed. Setting
this to

null

will result in the underlying
implementation using it's own default implementation and
behavior.

**Parameters:** er

- The

EntityResolver

to be used to resolve entities
present in the XML document to be parsed.

- setErrorHandler

```java
public abstract void setErrorHandler​(
ErrorHandler
eh)
```

Specify the

ErrorHandler

to be used by the parser.
Setting this to

null

will result in the underlying
implementation using it's own default implementation and
behavior.

**Parameters:** eh

- The

ErrorHandler

to be used by the parser.

- newDocument

```java
public abstract
Document
newDocument()
```

Obtain a new instance of a DOM

Document

object
to build a DOM tree with.

**Returns:** A new instance of a DOM Document object.

- getDOMImplementation

```java
public abstract
DOMImplementation
getDOMImplementation()
```

Obtain an instance of a

DOMImplementation

object.

**Returns:** A new instance of a

DOMImplementation

.

- getSchema

```java
public
Schema
getSchema()
```

Get a reference to the the

Schema

being used by
the XML processor.

If no schema is being used,

null

is returned.

**Returns:** Schema

being used or

null

if none in use
**Throws:** UnsupportedOperationException

- When implementation does not
override this method
**Since:** 1.5

- isXIncludeAware

```java
public boolean isXIncludeAware()
```

Get the XInclude processing mode for this parser.

**Returns:** the return value of
the

DocumentBuilderFactory.isXIncludeAware()

when this parser was created from factory.
**Throws:** UnsupportedOperationException

- When implementation does not
override this method
**Since:** 1.5
**See Also:** DocumentBuilderFactory.setXIncludeAware(boolean)

Constructor Detail

- DocumentBuilder

```java
protected DocumentBuilder()
```

Protected constructor

---

#### Constructor Detail

DocumentBuilder

```java
protected DocumentBuilder()
```

Protected constructor

---

#### DocumentBuilder

protected DocumentBuilder()

Protected constructor

Method Detail

- reset

```java
public void reset()
```

Reset this

DocumentBuilder

to its original configuration.

DocumentBuilder

is reset to the same state as when it was created with

DocumentBuilderFactory.newDocumentBuilder()

.

reset()

is designed to allow the reuse of existing

DocumentBuilder

s
thus saving resources associated with the creation of new

DocumentBuilder

s.

The reset

DocumentBuilder

is not guaranteed to have the same

EntityResolver

or

ErrorHandler

Object

s, e.g.

Object.equals(Object obj)

. It is guaranteed to have a functionally equal

EntityResolver

and

ErrorHandler

.

**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

- parse

```java
public
Document
parse​(
InputStream
is)
throws
SAXException
,

IOException
```

Parse the content of the given

InputStream

as an XML
document and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputStream

is null.

**Parameters:** is

- InputStream containing the content to be parsed.
**Returns:** Document

result of parsing the

InputStream
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

is

is

null
**See Also:** DocumentHandler

- parse

```java
public
Document
parse​(
InputStream
is,

String
systemId)
throws
SAXException
,

IOException
```

Parse the content of the given

InputStream

as an
XML document and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputStream

is null.

**Parameters:** is

- InputStream containing the content to be parsed.
**Parameters:** systemId

- Provide a base for resolving relative URIs.
**Returns:** A new DOM Document object.
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

is

is

null
**See Also:** DocumentHandler

- parse

```java
public
Document
parse​(
String
uri)
throws
SAXException
,

IOException
```

Parse the content of the given URI as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the
URI is

null

null.

**Parameters:** uri

- The location of the content to be parsed.
**Returns:** A new DOM Document object.
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

uri

is

null
**See Also:** DocumentHandler

- parse

```java
public
Document
parse​(
File
f)
throws
SAXException
,

IOException
```

Parse the content of the given file as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

File

is

null

null.

**Parameters:** f

- The file containing the XML to parse.
**Returns:** A new DOM Document object.
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

f

is

null
**See Also:** DocumentHandler

- parse

```java
public abstract
Document
parse​(
InputSource
is)
throws
SAXException
,

IOException
```

Parse the content of the given input source as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputSource

is

null

null.

**Parameters:** is

- InputSource containing the content to be parsed.
**Returns:** A new DOM Document object.
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

is

is

null
**See Also:** DocumentHandler

- isNamespaceAware

```java
public abstract boolean isNamespaceAware()
```

Indicates whether or not this parser is configured to
understand namespaces.

**Returns:** true if this parser is configured to understand
namespaces; false otherwise.

- isValidating

```java
public abstract boolean isValidating()
```

Indicates whether or not this parser is configured to
validate XML documents.

**Returns:** true if this parser is configured to validate
XML documents; false otherwise.

- setEntityResolver

```java
public abstract void setEntityResolver​(
EntityResolver
er)
```

Specify the

EntityResolver

to be used to resolve
entities present in the XML document to be parsed. Setting
this to

null

will result in the underlying
implementation using it's own default implementation and
behavior.

**Parameters:** er

- The

EntityResolver

to be used to resolve entities
present in the XML document to be parsed.

- setErrorHandler

```java
public abstract void setErrorHandler​(
ErrorHandler
eh)
```

Specify the

ErrorHandler

to be used by the parser.
Setting this to

null

will result in the underlying
implementation using it's own default implementation and
behavior.

**Parameters:** eh

- The

ErrorHandler

to be used by the parser.

- newDocument

```java
public abstract
Document
newDocument()
```

Obtain a new instance of a DOM

Document

object
to build a DOM tree with.

**Returns:** A new instance of a DOM Document object.

- getDOMImplementation

```java
public abstract
DOMImplementation
getDOMImplementation()
```

Obtain an instance of a

DOMImplementation

object.

**Returns:** A new instance of a

DOMImplementation

.

- getSchema

```java
public
Schema
getSchema()
```

Get a reference to the the

Schema

being used by
the XML processor.

If no schema is being used,

null

is returned.

**Returns:** Schema

being used or

null

if none in use
**Throws:** UnsupportedOperationException

- When implementation does not
override this method
**Since:** 1.5

- isXIncludeAware

```java
public boolean isXIncludeAware()
```

Get the XInclude processing mode for this parser.

**Returns:** the return value of
the

DocumentBuilderFactory.isXIncludeAware()

when this parser was created from factory.
**Throws:** UnsupportedOperationException

- When implementation does not
override this method
**Since:** 1.5
**See Also:** DocumentBuilderFactory.setXIncludeAware(boolean)

---

#### Method Detail

reset

```java
public void reset()
```

Reset this

DocumentBuilder

to its original configuration.

DocumentBuilder

is reset to the same state as when it was created with

DocumentBuilderFactory.newDocumentBuilder()

.

reset()

is designed to allow the reuse of existing

DocumentBuilder

s
thus saving resources associated with the creation of new

DocumentBuilder

s.

The reset

DocumentBuilder

is not guaranteed to have the same

EntityResolver

or

ErrorHandler

Object

s, e.g.

Object.equals(Object obj)

. It is guaranteed to have a functionally equal

EntityResolver

and

ErrorHandler

.

**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

---

#### reset

public void reset()

Reset this

DocumentBuilder

to its original configuration.

DocumentBuilder

is reset to the same state as when it was created with

DocumentBuilderFactory.newDocumentBuilder()

.

reset()

is designed to allow the reuse of existing

DocumentBuilder

s
thus saving resources associated with the creation of new

DocumentBuilder

s.

The reset

DocumentBuilder

is not guaranteed to have the same

EntityResolver

or

ErrorHandler

Object

s, e.g.

Object.equals(Object obj)

. It is guaranteed to have a functionally equal

EntityResolver

and

ErrorHandler

.

Reset this

DocumentBuilder

to its original configuration.

DocumentBuilder

is reset to the same state as when it was created with

DocumentBuilderFactory.newDocumentBuilder()

.

reset()

is designed to allow the reuse of existing

DocumentBuilder

s
thus saving resources associated with the creation of new

DocumentBuilder

s.

The reset

DocumentBuilder

is not guaranteed to have the same

EntityResolver

or

ErrorHandler

Object

s, e.g.

Object.equals(Object obj)

. It is guaranteed to have a functionally equal

EntityResolver

and

ErrorHandler

.

parse

```java
public
Document
parse​(
InputStream
is)
throws
SAXException
,

IOException
```

Parse the content of the given

InputStream

as an XML
document and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputStream

is null.

**Parameters:** is

- InputStream containing the content to be parsed.
**Returns:** Document

result of parsing the

InputStream
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

is

is

null
**See Also:** DocumentHandler

---

#### parse

public

Document

parse​(

InputStream

is)
throws

SAXException

,

IOException

Parse the content of the given

InputStream

as an XML
document and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputStream

is null.

parse

```java
public
Document
parse​(
InputStream
is,

String
systemId)
throws
SAXException
,

IOException
```

Parse the content of the given

InputStream

as an
XML document and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputStream

is null.

**Parameters:** is

- InputStream containing the content to be parsed.
**Parameters:** systemId

- Provide a base for resolving relative URIs.
**Returns:** A new DOM Document object.
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

is

is

null
**See Also:** DocumentHandler

---

#### parse

public

Document

parse​(

InputStream

is,

String

systemId)
throws

SAXException

,

IOException

Parse the content of the given

InputStream

as an
XML document and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputStream

is null.

parse

```java
public
Document
parse​(
String
uri)
throws
SAXException
,

IOException
```

Parse the content of the given URI as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the
URI is

null

null.

**Parameters:** uri

- The location of the content to be parsed.
**Returns:** A new DOM Document object.
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

uri

is

null
**See Also:** DocumentHandler

---

#### parse

public

Document

parse​(

String

uri)
throws

SAXException

,

IOException

Parse the content of the given URI as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the
URI is

null

null.

parse

```java
public
Document
parse​(
File
f)
throws
SAXException
,

IOException
```

Parse the content of the given file as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

File

is

null

null.

**Parameters:** f

- The file containing the XML to parse.
**Returns:** A new DOM Document object.
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

f

is

null
**See Also:** DocumentHandler

---

#### parse

public

Document

parse​(

File

f)
throws

SAXException

,

IOException

Parse the content of the given file as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

File

is

null

null.

parse

```java
public abstract
Document
parse​(
InputSource
is)
throws
SAXException
,

IOException
```

Parse the content of the given input source as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputSource

is

null

null.

**Parameters:** is

- InputSource containing the content to be parsed.
**Returns:** A new DOM Document object.
**Throws:** IOException

- If any IO errors occur.
**Throws:** SAXException

- If any parse errors occur.
**Throws:** IllegalArgumentException

- When

is

is

null
**See Also:** DocumentHandler

---

#### parse

public abstract

Document

parse​(

InputSource

is)
throws

SAXException

,

IOException

Parse the content of the given input source as an XML document
and return a new DOM

Document

object.
An

IllegalArgumentException

is thrown if the

InputSource

is

null

null.

isNamespaceAware

```java
public abstract boolean isNamespaceAware()
```

Indicates whether or not this parser is configured to
understand namespaces.

**Returns:** true if this parser is configured to understand
namespaces; false otherwise.

---

#### isNamespaceAware

public abstract boolean isNamespaceAware()

Indicates whether or not this parser is configured to
understand namespaces.

isValidating

```java
public abstract boolean isValidating()
```

Indicates whether or not this parser is configured to
validate XML documents.

**Returns:** true if this parser is configured to validate
XML documents; false otherwise.

---

#### isValidating

public abstract boolean isValidating()

Indicates whether or not this parser is configured to
validate XML documents.

setEntityResolver

```java
public abstract void setEntityResolver​(
EntityResolver
er)
```

Specify the

EntityResolver

to be used to resolve
entities present in the XML document to be parsed. Setting
this to

null

will result in the underlying
implementation using it's own default implementation and
behavior.

**Parameters:** er

- The

EntityResolver

to be used to resolve entities
present in the XML document to be parsed.

---

#### setEntityResolver

public abstract void setEntityResolver​(

EntityResolver

er)

Specify the

EntityResolver

to be used to resolve
entities present in the XML document to be parsed. Setting
this to

null

will result in the underlying
implementation using it's own default implementation and
behavior.

setErrorHandler

```java
public abstract void setErrorHandler​(
ErrorHandler
eh)
```

Specify the

ErrorHandler

to be used by the parser.
Setting this to

null

will result in the underlying
implementation using it's own default implementation and
behavior.

**Parameters:** eh

- The

ErrorHandler

to be used by the parser.

---

#### setErrorHandler

public abstract void setErrorHandler​(

ErrorHandler

eh)

Specify the

ErrorHandler

to be used by the parser.
Setting this to

null

will result in the underlying
implementation using it's own default implementation and
behavior.

newDocument

```java
public abstract
Document
newDocument()
```

Obtain a new instance of a DOM

Document

object
to build a DOM tree with.

**Returns:** A new instance of a DOM Document object.

---

#### newDocument

public abstract

Document

newDocument()

Obtain a new instance of a DOM

Document

object
to build a DOM tree with.

getDOMImplementation

```java
public abstract
DOMImplementation
getDOMImplementation()
```

Obtain an instance of a

DOMImplementation

object.

**Returns:** A new instance of a

DOMImplementation

.

---

#### getDOMImplementation

public abstract

DOMImplementation

getDOMImplementation()

Obtain an instance of a

DOMImplementation

object.

getSchema

```java
public
Schema
getSchema()
```

Get a reference to the the

Schema

being used by
the XML processor.

If no schema is being used,

null

is returned.

**Returns:** Schema

being used or

null

if none in use
**Throws:** UnsupportedOperationException

- When implementation does not
override this method
**Since:** 1.5

---

#### getSchema

public

Schema

getSchema()

Get a reference to the the

Schema

being used by
the XML processor.

If no schema is being used,

null

is returned.

Get a reference to the the

Schema

being used by
the XML processor.

If no schema is being used,

null

is returned.

isXIncludeAware

```java
public boolean isXIncludeAware()
```

Get the XInclude processing mode for this parser.

**Returns:** the return value of
the

DocumentBuilderFactory.isXIncludeAware()

when this parser was created from factory.
**Throws:** UnsupportedOperationException

- When implementation does not
override this method
**Since:** 1.5
**See Also:** DocumentBuilderFactory.setXIncludeAware(boolean)

---

#### isXIncludeAware

public boolean isXIncludeAware()

Get the XInclude processing mode for this parser.

---

