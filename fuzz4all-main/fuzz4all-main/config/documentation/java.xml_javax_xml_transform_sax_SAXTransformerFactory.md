# Class SAXTransformerFactory

**Source:** `java.xml\javax\xml\transform\sax\SAXTransformerFactory.html`

### Class Description

```java
public abstract class
SAXTransformerFactory

extends
TransformerFactory
```

This class extends TransformerFactory to provide SAX-specific
factory methods. It provides two types of ContentHandlers,
one for creating Transformers, the other for creating Templates
objects.

If an application wants to set the ErrorHandler or EntityResolver
for an XMLReader used during a transformation, it should use a URIResolver
to return the SAXSource which provides (with getXMLReader) a reference to
the XMLReader.

**Since:** 1.4

---

### Field Details

#### public static final
String
FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the TransformerFactory returned from

TransformerFactory.newInstance()

may
be safely cast to a SAXTransformerFactory.

**See Also:**
- Constant Field Values

---

#### public static final
String
FEATURE_XMLFILTER

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the

newXMLFilter(Source src)

and

newXMLFilter(Templates templates)

methods are supported.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### protected SAXTransformerFactory()

The default constructor is protected on purpose.

---

### Method Details

#### public abstract
TransformerHandler
newTransformerHandler​(
Source
src)
throws
TransformerConfigurationException

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the transformation
instructions specified by the argument.

**Parameters:**
- src

- The Source of the transformation instructions.

**Returns:**
- TransformerHandler ready to transform SAX events.

**Throws:**
- TransformerConfigurationException

- If for some reason the
TransformerHandler can not be created.

---

#### public abstract
TransformerHandler
newTransformerHandler​(
Templates
templates)
throws
TransformerConfigurationException

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the Templates argument.

**Parameters:**
- templates

- The compiled transformation instructions.

**Returns:**
- TransformerHandler ready to transform SAX events.

**Throws:**
- TransformerConfigurationException

- If for some reason the
TransformerHandler can not be created.

---

#### public abstract
TransformerHandler
newTransformerHandler()
throws
TransformerConfigurationException

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result. The transformation
is defined as an identity (or copy) transformation, for example
to copy a series of SAX parse events into a DOM tree.

**Returns:**
- A non-null reference to a TransformerHandler, that may
be used as a ContentHandler for SAX parse events.

**Throws:**
- TransformerConfigurationException

- If for some reason the
TransformerHandler cannot be created.

---

#### public abstract
TemplatesHandler
newTemplatesHandler()
throws
TransformerConfigurationException

Get a TemplatesHandler object that can process SAX
ContentHandler events into a Templates object.

**Returns:**
- A non-null reference to a TransformerHandler, that may
be used as a ContentHandler for SAX parse events.

**Throws:**
- TransformerConfigurationException

- If for some reason the
TemplatesHandler cannot be created.

---

#### public abstract
XMLFilter
newXMLFilter​(
Source
src)
throws
TransformerConfigurationException

Create an XMLFilter that uses the given Source as the
transformation instructions.

**Parameters:**
- src

- The Source of the transformation instructions.

**Returns:**
- An XMLFilter object, or null if this feature is not supported.

**Throws:**
- TransformerConfigurationException

- If for some reason the
TemplatesHandler cannot be created.

---

#### public abstract
XMLFilter
newXMLFilter​(
Templates
templates)
throws
TransformerConfigurationException

Create an XMLFilter, based on the Templates argument..

**Parameters:**
- templates

- The compiled transformation instructions.

**Returns:**
- An XMLFilter object, or null if this feature is not supported.

**Throws:**
- TransformerConfigurationException

- If for some reason the
TemplatesHandler cannot be created.

---

### Additional Sections

#### Class SAXTransformerFactory

java.lang.Object

- javax.xml.transform.TransformerFactory
- - javax.xml.transform.sax.SAXTransformerFactory

javax.xml.transform.TransformerFactory

- javax.xml.transform.sax.SAXTransformerFactory

javax.xml.transform.sax.SAXTransformerFactory

```java
public abstract class
SAXTransformerFactory

extends
TransformerFactory
```

This class extends TransformerFactory to provide SAX-specific
factory methods. It provides two types of ContentHandlers,
one for creating Transformers, the other for creating Templates
objects.

If an application wants to set the ErrorHandler or EntityResolver
for an XMLReader used during a transformation, it should use a URIResolver
to return the SAXSource which provides (with getXMLReader) a reference to
the XMLReader.

**Since:** 1.4

public abstract class

SAXTransformerFactory

extends

TransformerFactory

This class extends TransformerFactory to provide SAX-specific
factory methods. It provides two types of ContentHandlers,
one for creating Transformers, the other for creating Templates
objects.

If an application wants to set the ErrorHandler or EntityResolver
for an XMLReader used during a transformation, it should use a URIResolver
to return the SAXSource which provides (with getXMLReader) a reference to
the XMLReader.

If an application wants to set the ErrorHandler or EntityResolver
for an XMLReader used during a transformation, it should use a URIResolver
to return the SAXSource which provides (with getXMLReader) a reference to
the XMLReader.

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
the TransformerFactory returned from

TransformerFactory.newInstance()

may
be safely cast to a SAXTransformerFactory.

static

String

FEATURE_XMLFILTER

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the

newXMLFilter(Source src)

and

newXMLFilter(Templates templates)

methods are supported.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SAXTransformerFactory

()

The default constructor is protected on purpose.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

TemplatesHandler

newTemplatesHandler

()

Get a TemplatesHandler object that can process SAX
ContentHandler events into a Templates object.

abstract

TransformerHandler

newTransformerHandler

()

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result.

abstract

TransformerHandler

newTransformerHandler

​(

Source

src)

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the transformation
instructions specified by the argument.

abstract

TransformerHandler

newTransformerHandler

​(

Templates

templates)

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the Templates argument.

abstract

XMLFilter

newXMLFilter

​(

Source

src)

Create an XMLFilter that uses the given Source as the
transformation instructions.

abstract

XMLFilter

newXMLFilter

​(

Templates

templates)

Create an XMLFilter, based on the Templates argument..

- Methods declared in class javax.xml.transform.

TransformerFactory

getAssociatedStylesheet

,

getAttribute

,

getErrorListener

,

getFeature

,

getURIResolver

,

newDefaultInstance

,

newInstance

,

newInstance

,

newTemplates

,

newTransformer

,

newTransformer

,

setAttribute

,

setErrorListener

,

setFeature

,

setURIResolver

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
the TransformerFactory returned from

TransformerFactory.newInstance()

may
be safely cast to a SAXTransformerFactory.

static

String

FEATURE_XMLFILTER

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the

newXMLFilter(Source src)

and

newXMLFilter(Templates templates)

methods are supported.

---

#### Field Summary

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the TransformerFactory returned from

TransformerFactory.newInstance()

may
be safely cast to a SAXTransformerFactory.

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the

newXMLFilter(Source src)

and

newXMLFilter(Templates templates)

methods are supported.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SAXTransformerFactory

()

The default constructor is protected on purpose.

---

#### Constructor Summary

The default constructor is protected on purpose.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

TemplatesHandler

newTemplatesHandler

()

Get a TemplatesHandler object that can process SAX
ContentHandler events into a Templates object.

abstract

TransformerHandler

newTransformerHandler

()

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result.

abstract

TransformerHandler

newTransformerHandler

​(

Source

src)

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the transformation
instructions specified by the argument.

abstract

TransformerHandler

newTransformerHandler

​(

Templates

templates)

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the Templates argument.

abstract

XMLFilter

newXMLFilter

​(

Source

src)

Create an XMLFilter that uses the given Source as the
transformation instructions.

abstract

XMLFilter

newXMLFilter

​(

Templates

templates)

Create an XMLFilter, based on the Templates argument..

- Methods declared in class javax.xml.transform.

TransformerFactory

getAssociatedStylesheet

,

getAttribute

,

getErrorListener

,

getFeature

,

getURIResolver

,

newDefaultInstance

,

newInstance

,

newInstance

,

newTemplates

,

newTransformer

,

newTransformer

,

setAttribute

,

setErrorListener

,

setFeature

,

setURIResolver

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

Get a TemplatesHandler object that can process SAX
ContentHandler events into a Templates object.

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result.

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the transformation
instructions specified by the argument.

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the Templates argument.

Create an XMLFilter that uses the given Source as the
transformation instructions.

Create an XMLFilter, based on the Templates argument..

Methods declared in class javax.xml.transform.

TransformerFactory

getAssociatedStylesheet

,

getAttribute

,

getErrorListener

,

getFeature

,

getURIResolver

,

newDefaultInstance

,

newInstance

,

newInstance

,

newTemplates

,

newTransformer

,

newTransformer

,

setAttribute

,

setErrorListener

,

setFeature

,

setURIResolver

---

#### Methods declared in class javax.xml.transform. TransformerFactory

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
the TransformerFactory returned from

TransformerFactory.newInstance()

may
be safely cast to a SAXTransformerFactory.

**See Also:** Constant Field Values

- FEATURE_XMLFILTER

```java
public static final
String
FEATURE_XMLFILTER
```

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the

newXMLFilter(Source src)

and

newXMLFilter(Templates templates)

methods are supported.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SAXTransformerFactory

```java
protected SAXTransformerFactory()
```

The default constructor is protected on purpose.

============ METHOD DETAIL ==========

- Method Detail

- newTransformerHandler

```java
public abstract
TransformerHandler
newTransformerHandler​(
Source
src)
throws
TransformerConfigurationException
```

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the transformation
instructions specified by the argument.

**Parameters:** src

- The Source of the transformation instructions.
**Returns:** TransformerHandler ready to transform SAX events.
**Throws:** TransformerConfigurationException

- If for some reason the
TransformerHandler can not be created.

- newTransformerHandler

```java
public abstract
TransformerHandler
newTransformerHandler​(
Templates
templates)
throws
TransformerConfigurationException
```

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the Templates argument.

**Parameters:** templates

- The compiled transformation instructions.
**Returns:** TransformerHandler ready to transform SAX events.
**Throws:** TransformerConfigurationException

- If for some reason the
TransformerHandler can not be created.

- newTransformerHandler

```java
public abstract
TransformerHandler
newTransformerHandler()
throws
TransformerConfigurationException
```

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result. The transformation
is defined as an identity (or copy) transformation, for example
to copy a series of SAX parse events into a DOM tree.

**Returns:** A non-null reference to a TransformerHandler, that may
be used as a ContentHandler for SAX parse events.
**Throws:** TransformerConfigurationException

- If for some reason the
TransformerHandler cannot be created.

- newTemplatesHandler

```java
public abstract
TemplatesHandler
newTemplatesHandler()
throws
TransformerConfigurationException
```

Get a TemplatesHandler object that can process SAX
ContentHandler events into a Templates object.

**Returns:** A non-null reference to a TransformerHandler, that may
be used as a ContentHandler for SAX parse events.
**Throws:** TransformerConfigurationException

- If for some reason the
TemplatesHandler cannot be created.

- newXMLFilter

```java
public abstract
XMLFilter
newXMLFilter​(
Source
src)
throws
TransformerConfigurationException
```

Create an XMLFilter that uses the given Source as the
transformation instructions.

**Parameters:** src

- The Source of the transformation instructions.
**Returns:** An XMLFilter object, or null if this feature is not supported.
**Throws:** TransformerConfigurationException

- If for some reason the
TemplatesHandler cannot be created.

- newXMLFilter

```java
public abstract
XMLFilter
newXMLFilter​(
Templates
templates)
throws
TransformerConfigurationException
```

Create an XMLFilter, based on the Templates argument..

**Parameters:** templates

- The compiled transformation instructions.
**Returns:** An XMLFilter object, or null if this feature is not supported.
**Throws:** TransformerConfigurationException

- If for some reason the
TemplatesHandler cannot be created.

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
the TransformerFactory returned from

TransformerFactory.newInstance()

may
be safely cast to a SAXTransformerFactory.

**See Also:** Constant Field Values

- FEATURE_XMLFILTER

```java
public static final
String
FEATURE_XMLFILTER
```

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the

newXMLFilter(Source src)

and

newXMLFilter(Templates templates)

methods are supported.

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
the TransformerFactory returned from

TransformerFactory.newInstance()

may
be safely cast to a SAXTransformerFactory.

**See Also:** Constant Field Values

---

#### FEATURE

public static final

String

FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the TransformerFactory returned from

TransformerFactory.newInstance()

may
be safely cast to a SAXTransformerFactory.

FEATURE_XMLFILTER

```java
public static final
String
FEATURE_XMLFILTER
```

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the

newXMLFilter(Source src)

and

newXMLFilter(Templates templates)

methods are supported.

**See Also:** Constant Field Values

---

#### FEATURE_XMLFILTER

public static final

String

FEATURE_XMLFILTER

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the

newXMLFilter(Source src)

and

newXMLFilter(Templates templates)

methods are supported.

Constructor Detail

- SAXTransformerFactory

```java
protected SAXTransformerFactory()
```

The default constructor is protected on purpose.

---

#### Constructor Detail

SAXTransformerFactory

```java
protected SAXTransformerFactory()
```

The default constructor is protected on purpose.

---

#### SAXTransformerFactory

protected SAXTransformerFactory()

The default constructor is protected on purpose.

Method Detail

- newTransformerHandler

```java
public abstract
TransformerHandler
newTransformerHandler​(
Source
src)
throws
TransformerConfigurationException
```

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the transformation
instructions specified by the argument.

**Parameters:** src

- The Source of the transformation instructions.
**Returns:** TransformerHandler ready to transform SAX events.
**Throws:** TransformerConfigurationException

- If for some reason the
TransformerHandler can not be created.

- newTransformerHandler

```java
public abstract
TransformerHandler
newTransformerHandler​(
Templates
templates)
throws
TransformerConfigurationException
```

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the Templates argument.

**Parameters:** templates

- The compiled transformation instructions.
**Returns:** TransformerHandler ready to transform SAX events.
**Throws:** TransformerConfigurationException

- If for some reason the
TransformerHandler can not be created.

- newTransformerHandler

```java
public abstract
TransformerHandler
newTransformerHandler()
throws
TransformerConfigurationException
```

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result. The transformation
is defined as an identity (or copy) transformation, for example
to copy a series of SAX parse events into a DOM tree.

**Returns:** A non-null reference to a TransformerHandler, that may
be used as a ContentHandler for SAX parse events.
**Throws:** TransformerConfigurationException

- If for some reason the
TransformerHandler cannot be created.

- newTemplatesHandler

```java
public abstract
TemplatesHandler
newTemplatesHandler()
throws
TransformerConfigurationException
```

Get a TemplatesHandler object that can process SAX
ContentHandler events into a Templates object.

**Returns:** A non-null reference to a TransformerHandler, that may
be used as a ContentHandler for SAX parse events.
**Throws:** TransformerConfigurationException

- If for some reason the
TemplatesHandler cannot be created.

- newXMLFilter

```java
public abstract
XMLFilter
newXMLFilter​(
Source
src)
throws
TransformerConfigurationException
```

Create an XMLFilter that uses the given Source as the
transformation instructions.

**Parameters:** src

- The Source of the transformation instructions.
**Returns:** An XMLFilter object, or null if this feature is not supported.
**Throws:** TransformerConfigurationException

- If for some reason the
TemplatesHandler cannot be created.

- newXMLFilter

```java
public abstract
XMLFilter
newXMLFilter​(
Templates
templates)
throws
TransformerConfigurationException
```

Create an XMLFilter, based on the Templates argument..

**Parameters:** templates

- The compiled transformation instructions.
**Returns:** An XMLFilter object, or null if this feature is not supported.
**Throws:** TransformerConfigurationException

- If for some reason the
TemplatesHandler cannot be created.

---

#### Method Detail

newTransformerHandler

```java
public abstract
TransformerHandler
newTransformerHandler​(
Source
src)
throws
TransformerConfigurationException
```

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the transformation
instructions specified by the argument.

**Parameters:** src

- The Source of the transformation instructions.
**Returns:** TransformerHandler ready to transform SAX events.
**Throws:** TransformerConfigurationException

- If for some reason the
TransformerHandler can not be created.

---

#### newTransformerHandler

public abstract

TransformerHandler

newTransformerHandler​(

Source

src)
throws

TransformerConfigurationException

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the transformation
instructions specified by the argument.

newTransformerHandler

```java
public abstract
TransformerHandler
newTransformerHandler​(
Templates
templates)
throws
TransformerConfigurationException
```

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the Templates argument.

**Parameters:** templates

- The compiled transformation instructions.
**Returns:** TransformerHandler ready to transform SAX events.
**Throws:** TransformerConfigurationException

- If for some reason the
TransformerHandler can not be created.

---

#### newTransformerHandler

public abstract

TransformerHandler

newTransformerHandler​(

Templates

templates)
throws

TransformerConfigurationException

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result, based on the Templates argument.

newTransformerHandler

```java
public abstract
TransformerHandler
newTransformerHandler()
throws
TransformerConfigurationException
```

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result. The transformation
is defined as an identity (or copy) transformation, for example
to copy a series of SAX parse events into a DOM tree.

**Returns:** A non-null reference to a TransformerHandler, that may
be used as a ContentHandler for SAX parse events.
**Throws:** TransformerConfigurationException

- If for some reason the
TransformerHandler cannot be created.

---

#### newTransformerHandler

public abstract

TransformerHandler

newTransformerHandler()
throws

TransformerConfigurationException

Get a TransformerHandler object that can process SAX
ContentHandler events into a Result. The transformation
is defined as an identity (or copy) transformation, for example
to copy a series of SAX parse events into a DOM tree.

newTemplatesHandler

```java
public abstract
TemplatesHandler
newTemplatesHandler()
throws
TransformerConfigurationException
```

Get a TemplatesHandler object that can process SAX
ContentHandler events into a Templates object.

**Returns:** A non-null reference to a TransformerHandler, that may
be used as a ContentHandler for SAX parse events.
**Throws:** TransformerConfigurationException

- If for some reason the
TemplatesHandler cannot be created.

---

#### newTemplatesHandler

public abstract

TemplatesHandler

newTemplatesHandler()
throws

TransformerConfigurationException

Get a TemplatesHandler object that can process SAX
ContentHandler events into a Templates object.

newXMLFilter

```java
public abstract
XMLFilter
newXMLFilter​(
Source
src)
throws
TransformerConfigurationException
```

Create an XMLFilter that uses the given Source as the
transformation instructions.

**Parameters:** src

- The Source of the transformation instructions.
**Returns:** An XMLFilter object, or null if this feature is not supported.
**Throws:** TransformerConfigurationException

- If for some reason the
TemplatesHandler cannot be created.

---

#### newXMLFilter

public abstract

XMLFilter

newXMLFilter​(

Source

src)
throws

TransformerConfigurationException

Create an XMLFilter that uses the given Source as the
transformation instructions.

newXMLFilter

```java
public abstract
XMLFilter
newXMLFilter​(
Templates
templates)
throws
TransformerConfigurationException
```

Create an XMLFilter, based on the Templates argument..

**Parameters:** templates

- The compiled transformation instructions.
**Returns:** An XMLFilter object, or null if this feature is not supported.
**Throws:** TransformerConfigurationException

- If for some reason the
TemplatesHandler cannot be created.

---

#### newXMLFilter

public abstract

XMLFilter

newXMLFilter​(

Templates

templates)
throws

TransformerConfigurationException

Create an XMLFilter, based on the Templates argument..

---

