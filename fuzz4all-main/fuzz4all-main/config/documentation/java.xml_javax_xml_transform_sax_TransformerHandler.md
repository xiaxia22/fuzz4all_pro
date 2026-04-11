# Interface TransformerHandler

**Source:** `java.xml\javax\xml\transform\sax\TransformerHandler.html`

### Class Description

```java
public interface
TransformerHandler

extends
ContentHandler
,
LexicalHandler
,
DTDHandler
```

A TransformerHandler
listens for SAX ContentHandler parse events and transforms
them to a Result.

**All Superinterfaces:** ContentHandler

,

DTDHandler

,

LexicalHandler

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setResult​(
Result
result)
throws
IllegalArgumentException

Set the

Result

associated with this

TransformerHandler

to be used for the transformation.

**Parameters:**
- result

- A

Result

instance, should not be

null

.

**Throws:**
- IllegalArgumentException

- if result is invalid for some reason.

---

#### void setSystemId​(
String
systemID)

Set the base ID (URI or system ID) from where relative
URLs will be resolved.

**Parameters:**
- systemID

- Base URI for the source tree.

---

#### String
getSystemId()

Get the base ID (URI or system ID) from where relative
URLs will be resolved.

**Returns:**
- The systemID that was set with

setSystemId(java.lang.String)

.

---

#### Transformer
getTransformer()

Get the

Transformer

associated with this handler, which
is needed in order to set parameters and output properties.

**Returns:**
- Transformer

associated with this

TransformerHandler

.

---

### Additional Sections

#### Interface TransformerHandler

**All Superinterfaces:** ContentHandler

,

DTDHandler

,

LexicalHandler

```java
public interface
TransformerHandler

extends
ContentHandler
,
LexicalHandler
,
DTDHandler
```

A TransformerHandler
listens for SAX ContentHandler parse events and transforms
them to a Result.

**Since:** 1.4

public interface

TransformerHandler

extends

ContentHandler

,

LexicalHandler

,

DTDHandler

A TransformerHandler
listens for SAX ContentHandler parse events and transforms
them to a Result.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getSystemId

()

Get the base ID (URI or system ID) from where relative
URLs will be resolved.

Transformer

getTransformer

()

Get the

Transformer

associated with this handler, which
is needed in order to set parameters and output properties.

void

setResult

​(

Result

result)

Set the

Result

associated with this

TransformerHandler

to be used for the transformation.

void

setSystemId

​(

String

systemID)

Set the base ID (URI or system ID) from where relative
URLs will be resolved.

- Methods declared in interface org.xml.sax.

ContentHandler

characters

,

endDocument

,

endElement

,

endPrefixMapping

,

ignorableWhitespace

,

processingInstruction

,

setDocumentLocator

,

skippedEntity

,

startDocument

,

startElement

,

startPrefixMapping

- Methods declared in interface org.xml.sax.

DTDHandler

notationDecl

,

unparsedEntityDecl

- Methods declared in interface org.xml.sax.ext.

LexicalHandler

comment

,

endCDATA

,

endDTD

,

endEntity

,

startCDATA

,

startDTD

,

startEntity

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getSystemId

()

Get the base ID (URI or system ID) from where relative
URLs will be resolved.

Transformer

getTransformer

()

Get the

Transformer

associated with this handler, which
is needed in order to set parameters and output properties.

void

setResult

​(

Result

result)

Set the

Result

associated with this

TransformerHandler

to be used for the transformation.

void

setSystemId

​(

String

systemID)

Set the base ID (URI or system ID) from where relative
URLs will be resolved.

- Methods declared in interface org.xml.sax.

ContentHandler

characters

,

endDocument

,

endElement

,

endPrefixMapping

,

ignorableWhitespace

,

processingInstruction

,

setDocumentLocator

,

skippedEntity

,

startDocument

,

startElement

,

startPrefixMapping

- Methods declared in interface org.xml.sax.

DTDHandler

notationDecl

,

unparsedEntityDecl

- Methods declared in interface org.xml.sax.ext.

LexicalHandler

comment

,

endCDATA

,

endDTD

,

endEntity

,

startCDATA

,

startDTD

,

startEntity

---

#### Method Summary

Get the base ID (URI or system ID) from where relative
URLs will be resolved.

Get the

Transformer

associated with this handler, which
is needed in order to set parameters and output properties.

Set the

Result

associated with this

TransformerHandler

to be used for the transformation.

Set the base ID (URI or system ID) from where relative
URLs will be resolved.

Methods declared in interface org.xml.sax.

ContentHandler

characters

,

endDocument

,

endElement

,

endPrefixMapping

,

ignorableWhitespace

,

processingInstruction

,

setDocumentLocator

,

skippedEntity

,

startDocument

,

startElement

,

startPrefixMapping

---

#### Methods declared in interface org.xml.sax. ContentHandler

Methods declared in interface org.xml.sax.

DTDHandler

notationDecl

,

unparsedEntityDecl

---

#### Methods declared in interface org.xml.sax. DTDHandler

Methods declared in interface org.xml.sax.ext.

LexicalHandler

comment

,

endCDATA

,

endDTD

,

endEntity

,

startCDATA

,

startDTD

,

startEntity

---

#### Methods declared in interface org.xml.sax.ext. LexicalHandler

============ METHOD DETAIL ==========

- Method Detail

- setResult

```java
void setResult​(
Result
result)
throws
IllegalArgumentException
```

Set the

Result

associated with this

TransformerHandler

to be used for the transformation.

**Parameters:** result

- A

Result

instance, should not be

null

.
**Throws:** IllegalArgumentException

- if result is invalid for some reason.

- setSystemId

```java
void setSystemId​(
String
systemID)
```

Set the base ID (URI or system ID) from where relative
URLs will be resolved.

**Parameters:** systemID

- Base URI for the source tree.

- getSystemId

```java
String
getSystemId()
```

Get the base ID (URI or system ID) from where relative
URLs will be resolved.

**Returns:** The systemID that was set with

setSystemId(java.lang.String)

.

- getTransformer

```java
Transformer
getTransformer()
```

Get the

Transformer

associated with this handler, which
is needed in order to set parameters and output properties.

**Returns:** Transformer

associated with this

TransformerHandler

.

Method Detail

- setResult

```java
void setResult​(
Result
result)
throws
IllegalArgumentException
```

Set the

Result

associated with this

TransformerHandler

to be used for the transformation.

**Parameters:** result

- A

Result

instance, should not be

null

.
**Throws:** IllegalArgumentException

- if result is invalid for some reason.

- setSystemId

```java
void setSystemId​(
String
systemID)
```

Set the base ID (URI or system ID) from where relative
URLs will be resolved.

**Parameters:** systemID

- Base URI for the source tree.

- getSystemId

```java
String
getSystemId()
```

Get the base ID (URI or system ID) from where relative
URLs will be resolved.

**Returns:** The systemID that was set with

setSystemId(java.lang.String)

.

- getTransformer

```java
Transformer
getTransformer()
```

Get the

Transformer

associated with this handler, which
is needed in order to set parameters and output properties.

**Returns:** Transformer

associated with this

TransformerHandler

.

---

#### Method Detail

setResult

```java
void setResult​(
Result
result)
throws
IllegalArgumentException
```

Set the

Result

associated with this

TransformerHandler

to be used for the transformation.

**Parameters:** result

- A

Result

instance, should not be

null

.
**Throws:** IllegalArgumentException

- if result is invalid for some reason.

---

#### setResult

void setResult​(

Result

result)
throws

IllegalArgumentException

Set the

Result

associated with this

TransformerHandler

to be used for the transformation.

setSystemId

```java
void setSystemId​(
String
systemID)
```

Set the base ID (URI or system ID) from where relative
URLs will be resolved.

**Parameters:** systemID

- Base URI for the source tree.

---

#### setSystemId

void setSystemId​(

String

systemID)

Set the base ID (URI or system ID) from where relative
URLs will be resolved.

getSystemId

```java
String
getSystemId()
```

Get the base ID (URI or system ID) from where relative
URLs will be resolved.

**Returns:** The systemID that was set with

setSystemId(java.lang.String)

.

---

#### getSystemId

String

getSystemId()

Get the base ID (URI or system ID) from where relative
URLs will be resolved.

getTransformer

```java
Transformer
getTransformer()
```

Get the

Transformer

associated with this handler, which
is needed in order to set parameters and output properties.

**Returns:** Transformer

associated with this

TransformerHandler

.

---

#### getTransformer

Transformer

getTransformer()

Get the

Transformer

associated with this handler, which
is needed in order to set parameters and output properties.

---

