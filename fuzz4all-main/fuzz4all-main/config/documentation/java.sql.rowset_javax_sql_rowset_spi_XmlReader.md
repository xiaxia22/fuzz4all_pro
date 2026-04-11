# Interface XmlReader

**Source:** `java.sql.rowset\javax\sql\rowset\spi\XmlReader.html`

### Class Description

```java
public interface
XmlReader

extends
RowSetReader
```

A specialized interface that facilitates an extension of the

SyncProvider

abstract class for XML orientated
synchronization providers.

SyncProvider

implementations that supply XML data reader
capabilities such as output XML stream capabilities can implement this
interface to provide standard

XmlReader

objects to

WebRowSet

implementations.

An

XmlReader

object is registered as the
XML reader for a

WebRowSet

by being assigned to the
rowset's

xmlReader

field. When the

WebRowSet

object's

readXml

method is invoked, it in turn invokes
its XML reader's

readXML

method.

**All Superinterfaces:** RowSetReader

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void readXML​(
WebRowSet
caller,

Reader
reader)
throws
SQLException

Reads and parses the given

WebRowSet

object from the given
input stream in XML format. The

xmlReader

field of the
given

WebRowSet

object must contain this

XmlReader

object.

If a parsing error occurs, the exception that is thrown will
include information about the location of the error in the
original XML document.

**Parameters:**
- caller

- the

WebRowSet

object to be parsed, whose

xmlReader

field must contain a reference to
this

XmlReader

object
- reader

- the

java.io.Reader

object from which

caller

will be read

**Throws:**
- SQLException

- if a database access error occurs or
this

XmlReader

object is not the reader
for the given rowset

---

### Additional Sections

#### Interface XmlReader

**All Superinterfaces:** RowSetReader

```java
public interface
XmlReader

extends
RowSetReader
```

A specialized interface that facilitates an extension of the

SyncProvider

abstract class for XML orientated
synchronization providers.

SyncProvider

implementations that supply XML data reader
capabilities such as output XML stream capabilities can implement this
interface to provide standard

XmlReader

objects to

WebRowSet

implementations.

An

XmlReader

object is registered as the
XML reader for a

WebRowSet

by being assigned to the
rowset's

xmlReader

field. When the

WebRowSet

object's

readXml

method is invoked, it in turn invokes
its XML reader's

readXML

method.

**Since:** 1.5

public interface

XmlReader

extends

RowSetReader

A specialized interface that facilitates an extension of the

SyncProvider

abstract class for XML orientated
synchronization providers.

SyncProvider

implementations that supply XML data reader
capabilities such as output XML stream capabilities can implement this
interface to provide standard

XmlReader

objects to

WebRowSet

implementations.

An

XmlReader

object is registered as the
XML reader for a

WebRowSet

by being assigned to the
rowset's

xmlReader

field. When the

WebRowSet

object's

readXml

method is invoked, it in turn invokes
its XML reader's

readXML

method.

SyncProvider

implementations that supply XML data reader
capabilities such as output XML stream capabilities can implement this
interface to provide standard

XmlReader

objects to

WebRowSet

implementations.

An

XmlReader

object is registered as the
XML reader for a

WebRowSet

by being assigned to the
rowset's

xmlReader

field. When the

WebRowSet

object's

readXml

method is invoked, it in turn invokes
its XML reader's

readXML

method.

An

XmlReader

object is registered as the
XML reader for a

WebRowSet

by being assigned to the
rowset's

xmlReader

field. When the

WebRowSet

object's

readXml

method is invoked, it in turn invokes
its XML reader's

readXML

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

readXML

​(

WebRowSet

caller,

Reader

reader)

Reads and parses the given

WebRowSet

object from the given
input stream in XML format.

- Methods declared in interface javax.sql.

RowSetReader

readData

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

readXML

​(

WebRowSet

caller,

Reader

reader)

Reads and parses the given

WebRowSet

object from the given
input stream in XML format.

- Methods declared in interface javax.sql.

RowSetReader

readData

---

#### Method Summary

Reads and parses the given

WebRowSet

object from the given
input stream in XML format.

Methods declared in interface javax.sql.

RowSetReader

readData

---

#### Methods declared in interface javax.sql. RowSetReader

============ METHOD DETAIL ==========

- Method Detail

- readXML

```java
void readXML​(
WebRowSet
caller,

Reader
reader)
throws
SQLException
```

Reads and parses the given

WebRowSet

object from the given
input stream in XML format. The

xmlReader

field of the
given

WebRowSet

object must contain this

XmlReader

object.

If a parsing error occurs, the exception that is thrown will
include information about the location of the error in the
original XML document.

**Parameters:** caller

- the

WebRowSet

object to be parsed, whose

xmlReader

field must contain a reference to
this

XmlReader

object
**Parameters:** reader

- the

java.io.Reader

object from which

caller

will be read
**Throws:** SQLException

- if a database access error occurs or
this

XmlReader

object is not the reader
for the given rowset

Method Detail

- readXML

```java
void readXML​(
WebRowSet
caller,

Reader
reader)
throws
SQLException
```

Reads and parses the given

WebRowSet

object from the given
input stream in XML format. The

xmlReader

field of the
given

WebRowSet

object must contain this

XmlReader

object.

If a parsing error occurs, the exception that is thrown will
include information about the location of the error in the
original XML document.

**Parameters:** caller

- the

WebRowSet

object to be parsed, whose

xmlReader

field must contain a reference to
this

XmlReader

object
**Parameters:** reader

- the

java.io.Reader

object from which

caller

will be read
**Throws:** SQLException

- if a database access error occurs or
this

XmlReader

object is not the reader
for the given rowset

---

#### Method Detail

readXML

```java
void readXML​(
WebRowSet
caller,

Reader
reader)
throws
SQLException
```

Reads and parses the given

WebRowSet

object from the given
input stream in XML format. The

xmlReader

field of the
given

WebRowSet

object must contain this

XmlReader

object.

If a parsing error occurs, the exception that is thrown will
include information about the location of the error in the
original XML document.

**Parameters:** caller

- the

WebRowSet

object to be parsed, whose

xmlReader

field must contain a reference to
this

XmlReader

object
**Parameters:** reader

- the

java.io.Reader

object from which

caller

will be read
**Throws:** SQLException

- if a database access error occurs or
this

XmlReader

object is not the reader
for the given rowset

---

#### readXML

void readXML​(

WebRowSet

caller,

Reader

reader)
throws

SQLException

Reads and parses the given

WebRowSet

object from the given
input stream in XML format. The

xmlReader

field of the
given

WebRowSet

object must contain this

XmlReader

object.

If a parsing error occurs, the exception that is thrown will
include information about the location of the error in the
original XML document.

If a parsing error occurs, the exception that is thrown will
include information about the location of the error in the
original XML document.

---

