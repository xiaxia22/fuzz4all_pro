# Interface XMLResolver

**Source:** `java.xml\javax\xml\stream\XMLResolver.html`

### Class Description

```java
public interface
XMLResolver
```

This interface is used to resolve resources during an XML parse. If an application wishes to
perform custom entity resolution it must register an instance of this interface with
the XMLInputFactory using the setXMLResolver method.

**All Known Subinterfaces:** CatalogResolver

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
resolveEntity​(
String
publicID,

String
systemID,

String
baseURI,

String
namespace)
throws
XMLStreamException

Retrieves a resource. This resource can be of the following three return types:
(1) java.io.InputStream (2) javax.xml.stream.XMLStreamReader (3) java.xml.stream.XMLEventReader.
If this method returns null the processor will attempt to resolve the entity using its
default mechanism.

**Parameters:**
- publicID

- The public identifier of the external entity being referenced, or null if none was supplied.
- systemID

- The system identifier of the external entity being referenced.
- baseURI

- Absolute base URI associated with systemId.
- namespace

- The namespace of the entity to resolve.

**Returns:**
- The resource requested or null.

**Throws:**
- XMLStreamException

- if there was a failure attempting to resolve the resource.

---

### Additional Sections

#### Interface XMLResolver

**All Known Subinterfaces:** CatalogResolver

```java
public interface
XMLResolver
```

This interface is used to resolve resources during an XML parse. If an application wishes to
perform custom entity resolution it must register an instance of this interface with
the XMLInputFactory using the setXMLResolver method.

**Since:** 1.6

public interface

XMLResolver

This interface is used to resolve resources during an XML parse. If an application wishes to
perform custom entity resolution it must register an instance of this interface with
the XMLInputFactory using the setXMLResolver method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

resolveEntity

​(

String

publicID,

String

systemID,

String

baseURI,

String

namespace)

Retrieves a resource.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

resolveEntity

​(

String

publicID,

String

systemID,

String

baseURI,

String

namespace)

Retrieves a resource.

---

#### Method Summary

Retrieves a resource.

============ METHOD DETAIL ==========

- Method Detail

- resolveEntity

```java
Object
resolveEntity​(
String
publicID,

String
systemID,

String
baseURI,

String
namespace)
throws
XMLStreamException
```

Retrieves a resource. This resource can be of the following three return types:
(1) java.io.InputStream (2) javax.xml.stream.XMLStreamReader (3) java.xml.stream.XMLEventReader.
If this method returns null the processor will attempt to resolve the entity using its
default mechanism.

**Parameters:** publicID

- The public identifier of the external entity being referenced, or null if none was supplied.
**Parameters:** systemID

- The system identifier of the external entity being referenced.
**Parameters:** baseURI

- Absolute base URI associated with systemId.
**Parameters:** namespace

- The namespace of the entity to resolve.
**Returns:** The resource requested or null.
**Throws:** XMLStreamException

- if there was a failure attempting to resolve the resource.

Method Detail

- resolveEntity

```java
Object
resolveEntity​(
String
publicID,

String
systemID,

String
baseURI,

String
namespace)
throws
XMLStreamException
```

Retrieves a resource. This resource can be of the following three return types:
(1) java.io.InputStream (2) javax.xml.stream.XMLStreamReader (3) java.xml.stream.XMLEventReader.
If this method returns null the processor will attempt to resolve the entity using its
default mechanism.

**Parameters:** publicID

- The public identifier of the external entity being referenced, or null if none was supplied.
**Parameters:** systemID

- The system identifier of the external entity being referenced.
**Parameters:** baseURI

- Absolute base URI associated with systemId.
**Parameters:** namespace

- The namespace of the entity to resolve.
**Returns:** The resource requested or null.
**Throws:** XMLStreamException

- if there was a failure attempting to resolve the resource.

---

#### Method Detail

resolveEntity

```java
Object
resolveEntity​(
String
publicID,

String
systemID,

String
baseURI,

String
namespace)
throws
XMLStreamException
```

Retrieves a resource. This resource can be of the following three return types:
(1) java.io.InputStream (2) javax.xml.stream.XMLStreamReader (3) java.xml.stream.XMLEventReader.
If this method returns null the processor will attempt to resolve the entity using its
default mechanism.

**Parameters:** publicID

- The public identifier of the external entity being referenced, or null if none was supplied.
**Parameters:** systemID

- The system identifier of the external entity being referenced.
**Parameters:** baseURI

- Absolute base URI associated with systemId.
**Parameters:** namespace

- The namespace of the entity to resolve.
**Returns:** The resource requested or null.
**Throws:** XMLStreamException

- if there was a failure attempting to resolve the resource.

---

#### resolveEntity

Object

resolveEntity​(

String

publicID,

String

systemID,

String

baseURI,

String

namespace)
throws

XMLStreamException

Retrieves a resource. This resource can be of the following three return types:
(1) java.io.InputStream (2) javax.xml.stream.XMLStreamReader (3) java.xml.stream.XMLEventReader.
If this method returns null the processor will attempt to resolve the entity using its
default mechanism.

---

