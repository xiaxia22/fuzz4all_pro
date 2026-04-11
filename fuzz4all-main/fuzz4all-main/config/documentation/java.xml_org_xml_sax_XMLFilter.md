# Interface XMLFilter

**Source:** `java.xml\org\xml\sax\XMLFilter.html`

### Class Description

```java
public interface
XMLFilter

extends
XMLReader
```

Interface for an XML filter.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

An XML filter is like an XML reader, except that it obtains its
events from another XML reader rather than a primary source like
an XML document or database. Filters can modify a stream of
events as they pass on to the final application.

The XMLFilterImpl helper class provides a convenient base
for creating SAX2 filters, by passing on all

EntityResolver

,

DTDHandler

,

ContentHandler

and

ErrorHandler

events automatically.

**All Superinterfaces:** XMLReader

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setParent​(
XMLReader
parent)

Set the parent reader.

This method allows the application to link the filter to
a parent reader (which may be another filter). The argument
may not be null.

**Parameters:**
- parent

- The parent reader.

---

#### XMLReader
getParent()

Get the parent reader.

This method allows the application to query the parent
reader (which may be another filter). It is generally a
bad idea to perform any operations on the parent reader
directly: they should all pass through this filter.

**Returns:**
- The parent filter, or null if none has been set.

---

### Additional Sections

#### Interface XMLFilter

**All Superinterfaces:** XMLReader

**All Known Implementing Classes:** XMLFilterImpl

```java
public interface
XMLFilter

extends
XMLReader
```

Interface for an XML filter.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

An XML filter is like an XML reader, except that it obtains its
events from another XML reader rather than a primary source like
an XML document or database. Filters can modify a stream of
events as they pass on to the final application.

The XMLFilterImpl helper class provides a convenient base
for creating SAX2 filters, by passing on all

EntityResolver

,

DTDHandler

,

ContentHandler

and

ErrorHandler

events automatically.

**Since:** 1.4, SAX 2.0
**See Also:** XMLFilterImpl

public interface

XMLFilter

extends

XMLReader

Interface for an XML filter.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

An XML filter is like an XML reader, except that it obtains its
events from another XML reader rather than a primary source like
an XML document or database. Filters can modify a stream of
events as they pass on to the final application.

The XMLFilterImpl helper class provides a convenient base
for creating SAX2 filters, by passing on all

EntityResolver

,

DTDHandler

,

ContentHandler

and

ErrorHandler

events automatically.

An XML filter is like an XML reader, except that it obtains its
events from another XML reader rather than a primary source like
an XML document or database. Filters can modify a stream of
events as they pass on to the final application.

The XMLFilterImpl helper class provides a convenient base
for creating SAX2 filters, by passing on all

EntityResolver

,

DTDHandler

,

ContentHandler

and

ErrorHandler

events automatically.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

XMLReader

getParent

()

Get the parent reader.

void

setParent

​(

XMLReader

parent)

Set the parent reader.

- Methods declared in interface org.xml.sax.

XMLReader

getContentHandler

,

getDTDHandler

,

getEntityResolver

,

getErrorHandler

,

getFeature

,

getProperty

,

parse

,

parse

,

setContentHandler

,

setDTDHandler

,

setEntityResolver

,

setErrorHandler

,

setFeature

,

setProperty

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

XMLReader

getParent

()

Get the parent reader.

void

setParent

​(

XMLReader

parent)

Set the parent reader.

- Methods declared in interface org.xml.sax.

XMLReader

getContentHandler

,

getDTDHandler

,

getEntityResolver

,

getErrorHandler

,

getFeature

,

getProperty

,

parse

,

parse

,

setContentHandler

,

setDTDHandler

,

setEntityResolver

,

setErrorHandler

,

setFeature

,

setProperty

---

#### Method Summary

Get the parent reader.

Set the parent reader.

Methods declared in interface org.xml.sax.

XMLReader

getContentHandler

,

getDTDHandler

,

getEntityResolver

,

getErrorHandler

,

getFeature

,

getProperty

,

parse

,

parse

,

setContentHandler

,

setDTDHandler

,

setEntityResolver

,

setErrorHandler

,

setFeature

,

setProperty

---

#### Methods declared in interface org.xml.sax. XMLReader

============ METHOD DETAIL ==========

- Method Detail

- setParent

```java
void setParent​(
XMLReader
parent)
```

Set the parent reader.

This method allows the application to link the filter to
a parent reader (which may be another filter). The argument
may not be null.

**Parameters:** parent

- The parent reader.

- getParent

```java
XMLReader
getParent()
```

Get the parent reader.

This method allows the application to query the parent
reader (which may be another filter). It is generally a
bad idea to perform any operations on the parent reader
directly: they should all pass through this filter.

**Returns:** The parent filter, or null if none has been set.

Method Detail

- setParent

```java
void setParent​(
XMLReader
parent)
```

Set the parent reader.

This method allows the application to link the filter to
a parent reader (which may be another filter). The argument
may not be null.

**Parameters:** parent

- The parent reader.

- getParent

```java
XMLReader
getParent()
```

Get the parent reader.

This method allows the application to query the parent
reader (which may be another filter). It is generally a
bad idea to perform any operations on the parent reader
directly: they should all pass through this filter.

**Returns:** The parent filter, or null if none has been set.

---

#### Method Detail

setParent

```java
void setParent​(
XMLReader
parent)
```

Set the parent reader.

This method allows the application to link the filter to
a parent reader (which may be another filter). The argument
may not be null.

**Parameters:** parent

- The parent reader.

---

#### setParent

void setParent​(

XMLReader

parent)

Set the parent reader.

This method allows the application to link the filter to
a parent reader (which may be another filter). The argument
may not be null.

This method allows the application to link the filter to
a parent reader (which may be another filter). The argument
may not be null.

getParent

```java
XMLReader
getParent()
```

Get the parent reader.

This method allows the application to query the parent
reader (which may be another filter). It is generally a
bad idea to perform any operations on the parent reader
directly: they should all pass through this filter.

**Returns:** The parent filter, or null if none has been set.

---

#### getParent

XMLReader

getParent()

Get the parent reader.

This method allows the application to query the parent
reader (which may be another filter). It is generally a
bad idea to perform any operations on the parent reader
directly: they should all pass through this filter.

This method allows the application to query the parent
reader (which may be another filter). It is generally a
bad idea to perform any operations on the parent reader
directly: they should all pass through this filter.

---

