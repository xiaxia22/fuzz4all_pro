# Interface XmlWriter

**Source:** `java.sql.rowset\javax\sql\rowset\spi\XmlWriter.html`

### Class Description

```java
public interface
XmlWriter

extends
RowSetWriter
```

A specialized interface that facilitates an extension of the

SyncProvider

abstract class for XML orientated
synchronization providers.

SyncProvider

implementations that supply XML data writer
capabilities such as output XML stream capabilities can implement this
interface to provide standard

XmlWriter

objects to

WebRowSet

implementations.

Writing a

WebRowSet

object includes printing the
rowset's data, metadata, and properties, all with the
appropriate XML tags.

**All Superinterfaces:** RowSetWriter

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void writeXML​(
WebRowSet
caller,

Writer
writer)
throws
SQLException

Writes the given

WebRowSet

object to the specified

java.io.Writer

output stream as an XML document.
This document includes the rowset's data, metadata, and properties
plus the appropriate XML tags.

The

caller

parameter must be a

WebRowSet

object whose

XmlWriter

field contains a reference to
this

XmlWriter

object.

**Parameters:**
- caller

- the

WebRowSet

instance to be written,
for which this

XmlWriter

object is the writer
- writer

- the

java.io.Writer

object that serves
as the output stream for writing

caller

as
an XML document

**Throws:**
- SQLException

- if a database access error occurs or
this

XmlWriter

object is not the writer
for the given

WebRowSet

object

---

### Additional Sections

#### Interface XmlWriter

**All Superinterfaces:** RowSetWriter

```java
public interface
XmlWriter

extends
RowSetWriter
```

A specialized interface that facilitates an extension of the

SyncProvider

abstract class for XML orientated
synchronization providers.

SyncProvider

implementations that supply XML data writer
capabilities such as output XML stream capabilities can implement this
interface to provide standard

XmlWriter

objects to

WebRowSet

implementations.

Writing a

WebRowSet

object includes printing the
rowset's data, metadata, and properties, all with the
appropriate XML tags.

**Since:** 1.5

public interface

XmlWriter

extends

RowSetWriter

A specialized interface that facilitates an extension of the

SyncProvider

abstract class for XML orientated
synchronization providers.

SyncProvider

implementations that supply XML data writer
capabilities such as output XML stream capabilities can implement this
interface to provide standard

XmlWriter

objects to

WebRowSet

implementations.

Writing a

WebRowSet

object includes printing the
rowset's data, metadata, and properties, all with the
appropriate XML tags.

SyncProvider

implementations that supply XML data writer
capabilities such as output XML stream capabilities can implement this
interface to provide standard

XmlWriter

objects to

WebRowSet

implementations.

Writing a

WebRowSet

object includes printing the
rowset's data, metadata, and properties, all with the
appropriate XML tags.

Writing a

WebRowSet

object includes printing the
rowset's data, metadata, and properties, all with the
appropriate XML tags.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

writeXML

​(

WebRowSet

caller,

Writer

writer)

Writes the given

WebRowSet

object to the specified

java.io.Writer

output stream as an XML document.

- Methods declared in interface javax.sql.

RowSetWriter

writeData

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

writeXML

​(

WebRowSet

caller,

Writer

writer)

Writes the given

WebRowSet

object to the specified

java.io.Writer

output stream as an XML document.

- Methods declared in interface javax.sql.

RowSetWriter

writeData

---

#### Method Summary

Writes the given

WebRowSet

object to the specified

java.io.Writer

output stream as an XML document.

Methods declared in interface javax.sql.

RowSetWriter

writeData

---

#### Methods declared in interface javax.sql. RowSetWriter

============ METHOD DETAIL ==========

- Method Detail

- writeXML

```java
void writeXML​(
WebRowSet
caller,

Writer
writer)
throws
SQLException
```

Writes the given

WebRowSet

object to the specified

java.io.Writer

output stream as an XML document.
This document includes the rowset's data, metadata, and properties
plus the appropriate XML tags.

The

caller

parameter must be a

WebRowSet

object whose

XmlWriter

field contains a reference to
this

XmlWriter

object.

**Parameters:** caller

- the

WebRowSet

instance to be written,
for which this

XmlWriter

object is the writer
**Parameters:** writer

- the

java.io.Writer

object that serves
as the output stream for writing

caller

as
an XML document
**Throws:** SQLException

- if a database access error occurs or
this

XmlWriter

object is not the writer
for the given

WebRowSet

object

Method Detail

- writeXML

```java
void writeXML​(
WebRowSet
caller,

Writer
writer)
throws
SQLException
```

Writes the given

WebRowSet

object to the specified

java.io.Writer

output stream as an XML document.
This document includes the rowset's data, metadata, and properties
plus the appropriate XML tags.

The

caller

parameter must be a

WebRowSet

object whose

XmlWriter

field contains a reference to
this

XmlWriter

object.

**Parameters:** caller

- the

WebRowSet

instance to be written,
for which this

XmlWriter

object is the writer
**Parameters:** writer

- the

java.io.Writer

object that serves
as the output stream for writing

caller

as
an XML document
**Throws:** SQLException

- if a database access error occurs or
this

XmlWriter

object is not the writer
for the given

WebRowSet

object

---

#### Method Detail

writeXML

```java
void writeXML​(
WebRowSet
caller,

Writer
writer)
throws
SQLException
```

Writes the given

WebRowSet

object to the specified

java.io.Writer

output stream as an XML document.
This document includes the rowset's data, metadata, and properties
plus the appropriate XML tags.

The

caller

parameter must be a

WebRowSet

object whose

XmlWriter

field contains a reference to
this

XmlWriter

object.

**Parameters:** caller

- the

WebRowSet

instance to be written,
for which this

XmlWriter

object is the writer
**Parameters:** writer

- the

java.io.Writer

object that serves
as the output stream for writing

caller

as
an XML document
**Throws:** SQLException

- if a database access error occurs or
this

XmlWriter

object is not the writer
for the given

WebRowSet

object

---

#### writeXML

void writeXML​(

WebRowSet

caller,

Writer

writer)
throws

SQLException

Writes the given

WebRowSet

object to the specified

java.io.Writer

output stream as an XML document.
This document includes the rowset's data, metadata, and properties
plus the appropriate XML tags.

The

caller

parameter must be a

WebRowSet

object whose

XmlWriter

field contains a reference to
this

XmlWriter

object.

The

caller

parameter must be a

WebRowSet

object whose

XmlWriter

field contains a reference to
this

XmlWriter

object.

---

