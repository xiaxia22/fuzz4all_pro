# Interface LSResourceResolver

**Source:** `java.xml\org\w3c\dom\ls\LSResourceResolver.html`

### Class Description

```java
public interface
LSResourceResolver
```

LSResourceResolver

provides a way for applications to
redirect references to external resources.

Applications needing to implement custom handling for external
resources can implement this interface and register their implementation
by setting the "resource-resolver" parameter of

DOMConfiguration

objects attached to

LSParser

and

LSSerializer

. It can also be register on

DOMConfiguration

objects attached to

Document

if the "LS" feature is supported.

The

LSParser

will then allow the application to intercept
any external entities, including the external DTD subset and external
parameter entities, before including them. The top-level document entity
is never passed to the

resolveResource

method.

Many DOM applications will not need to implement this interface, but it
will be especially useful for applications that build XML documents from
databases or other specialized input sources, or for applications that
use URNs.

Note:

LSResourceResolver

is based on the SAX2 [

SAX

]

EntityResolver

interface.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

**All Known Subinterfaces:** CatalogResolver

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### LSInput
resolveResource​(
String
type,

String
namespaceURI,

String
publicId,

String
systemId,

String
baseURI)

Allow the application to resolve external resources.

The

LSParser

will call this method before opening any
external resource, including the external DTD subset, external
entities referenced within the DTD, and external entities referenced
within the document element (however, the top-level document entity
is not passed to this method). The application may then request that
the

LSParser

resolve the external resource itself, that
it use an alternative URI, or that it use an entirely different input
source.

Application writers can use this method to redirect external
system identifiers to secure and/or local URI, to look up public
identifiers in a catalogue, or to read an entity from a database or
other input source (including, for example, a dialog box).

**Parameters:**
- type

- The type of the resource being resolved. For XML [

XML 1.0

] resources
(i.e. entities), applications must use the value

"http://www.w3.org/TR/REC-xml"

. For XML Schema [

XML Schema Part 1

]
, applications must use the value

"http://www.w3.org/2001/XMLSchema"

. Other types of
resources are outside the scope of this specification and therefore
should recommend an absolute URI in order to use this method.
- namespaceURI

- The namespace of the resource being resolved,
e.g. the target namespace of the XML Schema [

XML Schema Part 1

]
when resolving XML Schema resources.
- publicId

- The public identifier of the external entity being
referenced, or

null

if no public identifier was
supplied or if the resource is not an entity.
- systemId

- The system identifier, a URI reference [

IETF RFC 2396

], of the
external resource being referenced, or

null

if no
system identifier was supplied.
- baseURI

- The absolute base URI of the resource being parsed, or

null

if there is no base URI.

**Returns:**
- A

LSInput

object describing the new input
source, or

null

to request that the parser open a
regular URI connection to the resource.

---

### Additional Sections

#### Interface LSResourceResolver

**All Known Subinterfaces:** CatalogResolver

```java
public interface
LSResourceResolver
```

LSResourceResolver

provides a way for applications to
redirect references to external resources.

Applications needing to implement custom handling for external
resources can implement this interface and register their implementation
by setting the "resource-resolver" parameter of

DOMConfiguration

objects attached to

LSParser

and

LSSerializer

. It can also be register on

DOMConfiguration

objects attached to

Document

if the "LS" feature is supported.

The

LSParser

will then allow the application to intercept
any external entities, including the external DTD subset and external
parameter entities, before including them. The top-level document entity
is never passed to the

resolveResource

method.

Many DOM applications will not need to implement this interface, but it
will be especially useful for applications that build XML documents from
databases or other specialized input sources, or for applications that
use URNs.

Note:

LSResourceResolver

is based on the SAX2 [

SAX

]

EntityResolver

interface.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

**Since:** 1.5

public interface

LSResourceResolver

LSResourceResolver

provides a way for applications to
redirect references to external resources.

Applications needing to implement custom handling for external
resources can implement this interface and register their implementation
by setting the "resource-resolver" parameter of

DOMConfiguration

objects attached to

LSParser

and

LSSerializer

. It can also be register on

DOMConfiguration

objects attached to

Document

if the "LS" feature is supported.

The

LSParser

will then allow the application to intercept
any external entities, including the external DTD subset and external
parameter entities, before including them. The top-level document entity
is never passed to the

resolveResource

method.

Many DOM applications will not need to implement this interface, but it
will be especially useful for applications that build XML documents from
databases or other specialized input sources, or for applications that
use URNs.

Note:

LSResourceResolver

is based on the SAX2 [

SAX

]

EntityResolver

interface.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

Applications needing to implement custom handling for external
resources can implement this interface and register their implementation
by setting the "resource-resolver" parameter of

DOMConfiguration

objects attached to

LSParser

and

LSSerializer

. It can also be register on

DOMConfiguration

objects attached to

Document

if the "LS" feature is supported.

The

LSParser

will then allow the application to intercept
any external entities, including the external DTD subset and external
parameter entities, before including them. The top-level document entity
is never passed to the

resolveResource

method.

Many DOM applications will not need to implement this interface, but it
will be especially useful for applications that build XML documents from
databases or other specialized input sources, or for applications that
use URNs.

Note:

LSResourceResolver

is based on the SAX2 [

SAX

]

EntityResolver

interface.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

The

LSParser

will then allow the application to intercept
any external entities, including the external DTD subset and external
parameter entities, before including them. The top-level document entity
is never passed to the

resolveResource

method.

Many DOM applications will not need to implement this interface, but it
will be especially useful for applications that build XML documents from
databases or other specialized input sources, or for applications that
use URNs.

Note:

LSResourceResolver

is based on the SAX2 [

SAX

]

EntityResolver

interface.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

Many DOM applications will not need to implement this interface, but it
will be especially useful for applications that build XML documents from
databases or other specialized input sources, or for applications that
use URNs.

Note:

LSResourceResolver

is based on the SAX2 [

SAX

]

EntityResolver

interface.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

Note:

LSResourceResolver

is based on the SAX2 [

SAX

]

EntityResolver

interface.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

LSInput

resolveResource

​(

String

type,

String

namespaceURI,

String

publicId,

String

systemId,

String

baseURI)

Allow the application to resolve external resources.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

LSInput

resolveResource

​(

String

type,

String

namespaceURI,

String

publicId,

String

systemId,

String

baseURI)

Allow the application to resolve external resources.

---

#### Method Summary

Allow the application to resolve external resources.

============ METHOD DETAIL ==========

- Method Detail

- resolveResource

```java
LSInput
resolveResource​(
String
type,

String
namespaceURI,

String
publicId,

String
systemId,

String
baseURI)
```

Allow the application to resolve external resources.

The

LSParser

will call this method before opening any
external resource, including the external DTD subset, external
entities referenced within the DTD, and external entities referenced
within the document element (however, the top-level document entity
is not passed to this method). The application may then request that
the

LSParser

resolve the external resource itself, that
it use an alternative URI, or that it use an entirely different input
source.

Application writers can use this method to redirect external
system identifiers to secure and/or local URI, to look up public
identifiers in a catalogue, or to read an entity from a database or
other input source (including, for example, a dialog box).

**Parameters:** type

- The type of the resource being resolved. For XML [

XML 1.0

] resources
(i.e. entities), applications must use the value

"http://www.w3.org/TR/REC-xml"

. For XML Schema [

XML Schema Part 1

]
, applications must use the value

"http://www.w3.org/2001/XMLSchema"

. Other types of
resources are outside the scope of this specification and therefore
should recommend an absolute URI in order to use this method.
**Parameters:** namespaceURI

- The namespace of the resource being resolved,
e.g. the target namespace of the XML Schema [

XML Schema Part 1

]
when resolving XML Schema resources.
**Parameters:** publicId

- The public identifier of the external entity being
referenced, or

null

if no public identifier was
supplied or if the resource is not an entity.
**Parameters:** systemId

- The system identifier, a URI reference [

IETF RFC 2396

], of the
external resource being referenced, or

null

if no
system identifier was supplied.
**Parameters:** baseURI

- The absolute base URI of the resource being parsed, or

null

if there is no base URI.
**Returns:** A

LSInput

object describing the new input
source, or

null

to request that the parser open a
regular URI connection to the resource.

Method Detail

- resolveResource

```java
LSInput
resolveResource​(
String
type,

String
namespaceURI,

String
publicId,

String
systemId,

String
baseURI)
```

Allow the application to resolve external resources.

The

LSParser

will call this method before opening any
external resource, including the external DTD subset, external
entities referenced within the DTD, and external entities referenced
within the document element (however, the top-level document entity
is not passed to this method). The application may then request that
the

LSParser

resolve the external resource itself, that
it use an alternative URI, or that it use an entirely different input
source.

Application writers can use this method to redirect external
system identifiers to secure and/or local URI, to look up public
identifiers in a catalogue, or to read an entity from a database or
other input source (including, for example, a dialog box).

**Parameters:** type

- The type of the resource being resolved. For XML [

XML 1.0

] resources
(i.e. entities), applications must use the value

"http://www.w3.org/TR/REC-xml"

. For XML Schema [

XML Schema Part 1

]
, applications must use the value

"http://www.w3.org/2001/XMLSchema"

. Other types of
resources are outside the scope of this specification and therefore
should recommend an absolute URI in order to use this method.
**Parameters:** namespaceURI

- The namespace of the resource being resolved,
e.g. the target namespace of the XML Schema [

XML Schema Part 1

]
when resolving XML Schema resources.
**Parameters:** publicId

- The public identifier of the external entity being
referenced, or

null

if no public identifier was
supplied or if the resource is not an entity.
**Parameters:** systemId

- The system identifier, a URI reference [

IETF RFC 2396

], of the
external resource being referenced, or

null

if no
system identifier was supplied.
**Parameters:** baseURI

- The absolute base URI of the resource being parsed, or

null

if there is no base URI.
**Returns:** A

LSInput

object describing the new input
source, or

null

to request that the parser open a
regular URI connection to the resource.

---

#### Method Detail

resolveResource

```java
LSInput
resolveResource​(
String
type,

String
namespaceURI,

String
publicId,

String
systemId,

String
baseURI)
```

Allow the application to resolve external resources.

The

LSParser

will call this method before opening any
external resource, including the external DTD subset, external
entities referenced within the DTD, and external entities referenced
within the document element (however, the top-level document entity
is not passed to this method). The application may then request that
the

LSParser

resolve the external resource itself, that
it use an alternative URI, or that it use an entirely different input
source.

Application writers can use this method to redirect external
system identifiers to secure and/or local URI, to look up public
identifiers in a catalogue, or to read an entity from a database or
other input source (including, for example, a dialog box).

**Parameters:** type

- The type of the resource being resolved. For XML [

XML 1.0

] resources
(i.e. entities), applications must use the value

"http://www.w3.org/TR/REC-xml"

. For XML Schema [

XML Schema Part 1

]
, applications must use the value

"http://www.w3.org/2001/XMLSchema"

. Other types of
resources are outside the scope of this specification and therefore
should recommend an absolute URI in order to use this method.
**Parameters:** namespaceURI

- The namespace of the resource being resolved,
e.g. the target namespace of the XML Schema [

XML Schema Part 1

]
when resolving XML Schema resources.
**Parameters:** publicId

- The public identifier of the external entity being
referenced, or

null

if no public identifier was
supplied or if the resource is not an entity.
**Parameters:** systemId

- The system identifier, a URI reference [

IETF RFC 2396

], of the
external resource being referenced, or

null

if no
system identifier was supplied.
**Parameters:** baseURI

- The absolute base URI of the resource being parsed, or

null

if there is no base URI.
**Returns:** A

LSInput

object describing the new input
source, or

null

to request that the parser open a
regular URI connection to the resource.

---

#### resolveResource

LSInput

resolveResource​(

String

type,

String

namespaceURI,

String

publicId,

String

systemId,

String

baseURI)

Allow the application to resolve external resources.

The

LSParser

will call this method before opening any
external resource, including the external DTD subset, external
entities referenced within the DTD, and external entities referenced
within the document element (however, the top-level document entity
is not passed to this method). The application may then request that
the

LSParser

resolve the external resource itself, that
it use an alternative URI, or that it use an entirely different input
source.

Application writers can use this method to redirect external
system identifiers to secure and/or local URI, to look up public
identifiers in a catalogue, or to read an entity from a database or
other input source (including, for example, a dialog box).

---

