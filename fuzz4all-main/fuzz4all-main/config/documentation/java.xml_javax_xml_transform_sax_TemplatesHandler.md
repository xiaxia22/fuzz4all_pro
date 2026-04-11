# Interface TemplatesHandler

**Source:** `java.xml\javax\xml\transform\sax\TemplatesHandler.html`

### Class Description

```java
public interface
TemplatesHandler

extends
ContentHandler
```

A SAX ContentHandler that may be used to process SAX
parse events (parsing transformation instructions) into a Templates object.

Note that TemplatesHandler does not need to implement LexicalHandler.

**All Superinterfaces:** ContentHandler

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Templates
getTemplates()

When a TemplatesHandler object is used as a ContentHandler
for the parsing of transformation instructions, it creates a Templates object,
which the caller can get once the SAX events have been completed.

**Returns:**
- The Templates object that was created during
the SAX event process, or null if no Templates object has
been created.

---

#### void setSystemId​(
String
systemID)

Set the base ID (URI or system ID) for the Templates object
created by this builder. This must be set in order to
resolve relative URIs in the stylesheet. This must be
called before the startDocument event.

**Parameters:**
- systemID

- Base URI for this stylesheet.

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

### Additional Sections

#### Interface TemplatesHandler

**All Superinterfaces:** ContentHandler

```java
public interface
TemplatesHandler

extends
ContentHandler
```

A SAX ContentHandler that may be used to process SAX
parse events (parsing transformation instructions) into a Templates object.

Note that TemplatesHandler does not need to implement LexicalHandler.

**Since:** 1.4

public interface

TemplatesHandler

extends

ContentHandler

A SAX ContentHandler that may be used to process SAX
parse events (parsing transformation instructions) into a Templates object.

Note that TemplatesHandler does not need to implement LexicalHandler.

Note that TemplatesHandler does not need to implement LexicalHandler.

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

Templates

getTemplates

()

When a TemplatesHandler object is used as a ContentHandler
for the parsing of transformation instructions, it creates a Templates object,
which the caller can get once the SAX events have been completed.

void

setSystemId

​(

String

systemID)

Set the base ID (URI or system ID) for the Templates object
created by this builder.

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

Templates

getTemplates

()

When a TemplatesHandler object is used as a ContentHandler
for the parsing of transformation instructions, it creates a Templates object,
which the caller can get once the SAX events have been completed.

void

setSystemId

​(

String

systemID)

Set the base ID (URI or system ID) for the Templates object
created by this builder.

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

---

#### Method Summary

Get the base ID (URI or system ID) from where relative
URLs will be resolved.

When a TemplatesHandler object is used as a ContentHandler
for the parsing of transformation instructions, it creates a Templates object,
which the caller can get once the SAX events have been completed.

Set the base ID (URI or system ID) for the Templates object
created by this builder.

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

============ METHOD DETAIL ==========

- Method Detail

- getTemplates

```java
Templates
getTemplates()
```

When a TemplatesHandler object is used as a ContentHandler
for the parsing of transformation instructions, it creates a Templates object,
which the caller can get once the SAX events have been completed.

**Returns:** The Templates object that was created during
the SAX event process, or null if no Templates object has
been created.

- setSystemId

```java
void setSystemId​(
String
systemID)
```

Set the base ID (URI or system ID) for the Templates object
created by this builder. This must be set in order to
resolve relative URIs in the stylesheet. This must be
called before the startDocument event.

**Parameters:** systemID

- Base URI for this stylesheet.

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

Method Detail

- getTemplates

```java
Templates
getTemplates()
```

When a TemplatesHandler object is used as a ContentHandler
for the parsing of transformation instructions, it creates a Templates object,
which the caller can get once the SAX events have been completed.

**Returns:** The Templates object that was created during
the SAX event process, or null if no Templates object has
been created.

- setSystemId

```java
void setSystemId​(
String
systemID)
```

Set the base ID (URI or system ID) for the Templates object
created by this builder. This must be set in order to
resolve relative URIs in the stylesheet. This must be
called before the startDocument event.

**Parameters:** systemID

- Base URI for this stylesheet.

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

---

#### Method Detail

getTemplates

```java
Templates
getTemplates()
```

When a TemplatesHandler object is used as a ContentHandler
for the parsing of transformation instructions, it creates a Templates object,
which the caller can get once the SAX events have been completed.

**Returns:** The Templates object that was created during
the SAX event process, or null if no Templates object has
been created.

---

#### getTemplates

Templates

getTemplates()

When a TemplatesHandler object is used as a ContentHandler
for the parsing of transformation instructions, it creates a Templates object,
which the caller can get once the SAX events have been completed.

setSystemId

```java
void setSystemId​(
String
systemID)
```

Set the base ID (URI or system ID) for the Templates object
created by this builder. This must be set in order to
resolve relative URIs in the stylesheet. This must be
called before the startDocument event.

**Parameters:** systemID

- Base URI for this stylesheet.

---

#### setSystemId

void setSystemId​(

String

systemID)

Set the base ID (URI or system ID) for the Templates object
created by this builder. This must be set in order to
resolve relative URIs in the stylesheet. This must be
called before the startDocument event.

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

---

