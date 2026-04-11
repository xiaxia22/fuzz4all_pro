# Interface CatalogResolver

**Source:** `java.xml\javax\xml\catalog\CatalogResolver.html`

### Class Description

```java
public interface
CatalogResolver

extends
EntityResolver
,
XMLResolver
,
URIResolver
,
LSResourceResolver
```

A Catalog Resolver that implements SAX

EntityResolver

,
StAX

XMLResolver

,
DOM LS

LSResourceResolver

used by Schema Validation, and
Transform

URIResolver

, and resolves
external references using catalogs.

The

Catalog Standard

distinguished

external identifiers

from

uri entries

as being used to solely identify DTDs, while

uri entries

for
other resources such as stylesheets and schema. The Java APIs, such as

XMLResolver

and

LSResourceResolver

however, make no such distinction.
In consistent with the existing Java API, this CatalogResolver recognizes a
system identifier as a URI and will search both

system

and

uri

entries in a catalog in order to find a matching entry.

The search is started in the current catalog. If a match is found,
no further attempt will be made. Only if there is no match in the current
catalog, will alternate catalogs including delegate and next catalogs be considered.

Search Order

The resolver will first search the system-type of entries with the specified

systemId

. The system entries include

system

,

rewriteSystem

and

systemSuffix

entries.

If no match is found,

public

entries may be searched in accordance with
the

prefer

attribute.

The

prefer

attribute

: if the

prefer

is public,
and there is no match found through the system entries,

public

entries
will be considered. If it is not specified, the

prefer

is public
by default (Note that by the OASIS standard, system entries will always
be considered before public entries. Prefer public means that public entries
will be matched when both system and public identifiers are specified.
In general therefore, prefer public is recommended.)

If no match is found with the

systemId

and

public

identifier,
the resolver will continue searching

uri

entries
with the specified

systemId

or

href

. The

uri

entries
include

uri

,

rewriteURI

, and

uriSuffix

entries.

Error Handling

The interfaces that the CatalogResolver extend specified checked exceptions, including:

- SAXException

and

IOException

by

EntityResolver.resolveEntity(java.lang.String, java.lang.String)
- XMLStreamException

by

XMLResolver.resolveEntity(java.lang.String, java.lang.String, java.lang.String, java.lang.String)
- TransformerException

by

URIResolver.resolve(java.lang.String, java.lang.String)

The CatalogResolver however, will throw

CatalogException

only when

javax.xml.catalog.resolve

is specified as

strict

.
For applications that expect to handle the checked Exceptions, it may be
necessary to use a custom resolver to wrap the CatalogResolver or implement it
with a

Catalog

object.

**All Superinterfaces:** EntityResolver

,

LSResourceResolver

,

URIResolver

,

XMLResolver

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### InputSource
resolveEntity​(
String
publicId,

String
systemId)

Implements

EntityResolver

. The method searches through
the catalog entries in the main and alternative catalogs to attempt to find
a match with the specified

publicId

or systemId.

**Specified by:**
- resolveEntity

in interface

EntityResolver

**Parameters:**
- publicId

- the public identifier of the external entity being
referenced, or null if none was supplied
- systemId

- the system identifier of the external entity being
referenced. A system identifier is required on all external entities. XML
requires a system identifier on all external entities, so this value is
always specified.

**Returns:**
- a

InputSource

object if a mapping is found.
If no mapping is found, returns a

InputSource

object
containing an empty

Reader

if the

javax.xml.catalog.resolve

property is set to

ignore

;
returns null if the

javax.xml.catalog.resolve

property is set to

continue

.

**Throws:**
- CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict

**See Also:**
- InputSource

---

#### Source
resolve​(
String
href,

String
base)

Implements URIResolver. The method searches through the catalog entries
in the main and alternative catalogs to attempt to find a match
with the specified

href

attribute. The

href

attribute will
be used literally, with no attempt to be made absolute to the

base

.

If the value is a URN, the

href

attribute is recognized as a

publicId

, and used to search

public

entries.
If the value is a URI, it is taken as a

systemId

, and used to
search both

system

and

uri

entries.

**Specified by:**
- resolve

in interface

URIResolver

**Parameters:**
- href

- the href attribute that specifies the URI of a style sheet,
which may be relative or absolute
- base

- The base URI against which the href attribute will be made
absolute if the absolute URI is required

**Returns:**
- a

Source

object if a mapping is found.
If no mapping is found, returns an empty

Source

object if the

javax.xml.catalog.resolve

property is set to

ignore

;
returns a

Source

object with the original URI
(href, or href resolved with base if base is not null) if the

javax.xml.catalog.resolve

property is set to

continue

.

**Throws:**
- CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict

---

#### InputStream
resolveEntity​(
String
publicId,

String
systemId,

String
baseUri,

String
namespace)

Implements

XMLResolver

. For the purpose of resolving

publicId

and

systemId

, this method is equivalent to

resolveEntity(java.lang.String, java.lang.String)

.

The

systemId

will be used literally, with no attempt to be made
absolute to the

baseUri

. The

baseUri

and

namespace

are not used in the search for a match in a catalog. However, a relative

systemId

in an xml source may have been made absolute by the parser
with the

baseURI

, thus making it unable to find a

system

entry.
In such a case, a

systemSuffix

entry is recommended over a

system

entry.

**Specified by:**
- resolveEntity

in interface

XMLResolver

**Parameters:**
- publicId

- the public identifier of the external entity being
referenced, or null if none was supplied
- systemId

- the system identifier of the external entity being
referenced. A system identifier is required on all external entities. XML
requires a system identifier on all external entities, so this value is
always specified.
- baseUri

- the absolute base URI, not used by the CatalogResolver
- namespace

- the namespace of the entity to resolve, not used by the
CatalogResolver.

**Returns:**
- an

InputStream

object if a mapping is found; null
if no mapping is found and the

javax.xml.catalog.resolve

property
is set to

continue

or

ignore

. Note that for XMLResolver,
it is not possible to ignore a reference,

ignore

is therefore
treated the same as

continue

.

**Throws:**
- CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict

---

#### LSInput
resolveResource​(
String
type,

String
namespaceUri,

String
publicId,

String
systemId,

String
baseUri)

Implements

LSResourceResolver

. For the purpose of
resolving

publicId

and

systemId

, this method is equivalent
to

resolveEntity(java.lang.String, java.lang.String)

.

The

systemId

will be used literally, with no attempt to be made
absolute to the

baseUri

. The

baseUri

,

namespaceUri

and

type

are not used in the search for a match in a catalog.
However, a relative

systemId

in a source may have been made absolute
by the parser with the

baseURI

, thus making it unable to find a

system

entry. In such a case, a

systemSuffix

entry is
recommended over a

system

entry.

**Specified by:**
- resolveResource

in interface

LSResourceResolver

**Parameters:**
- type

- the type of the resource being resolved,
not used by the CatalogResolver
- namespaceUri

- the namespace of the resource being resolved,
not used by the CatalogResolver
- publicId

- the public identifier of the external entity being
referenced, or

null

if no public identifier was
supplied or if the resource is not an entity.
- systemId

- the system identifier, a URI reference of the
external resource being referenced
- baseUri

- the absolute base URI, not used by the CatalogResolver

**Returns:**
- a

LSInput

object if a mapping is found; null
if no mapping is found and the

javax.xml.catalog.resolve

property
is set to

continue

or

ignore

. Note that for

LSResourceResolver

, it is not possible to ignore a
reference,

ignore

is therefore treated the same as

continue

.

**Throws:**
- CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict

---

### Additional Sections

#### Interface CatalogResolver

**All Superinterfaces:** EntityResolver

,

LSResourceResolver

,

URIResolver

,

XMLResolver

```java
public interface
CatalogResolver

extends
EntityResolver
,
XMLResolver
,
URIResolver
,
LSResourceResolver
```

A Catalog Resolver that implements SAX

EntityResolver

,
StAX

XMLResolver

,
DOM LS

LSResourceResolver

used by Schema Validation, and
Transform

URIResolver

, and resolves
external references using catalogs.

The

Catalog Standard

distinguished

external identifiers

from

uri entries

as being used to solely identify DTDs, while

uri entries

for
other resources such as stylesheets and schema. The Java APIs, such as

XMLResolver

and

LSResourceResolver

however, make no such distinction.
In consistent with the existing Java API, this CatalogResolver recognizes a
system identifier as a URI and will search both

system

and

uri

entries in a catalog in order to find a matching entry.

The search is started in the current catalog. If a match is found,
no further attempt will be made. Only if there is no match in the current
catalog, will alternate catalogs including delegate and next catalogs be considered.

Search Order

The resolver will first search the system-type of entries with the specified

systemId

. The system entries include

system

,

rewriteSystem

and

systemSuffix

entries.

If no match is found,

public

entries may be searched in accordance with
the

prefer

attribute.

The

prefer

attribute

: if the

prefer

is public,
and there is no match found through the system entries,

public

entries
will be considered. If it is not specified, the

prefer

is public
by default (Note that by the OASIS standard, system entries will always
be considered before public entries. Prefer public means that public entries
will be matched when both system and public identifiers are specified.
In general therefore, prefer public is recommended.)

If no match is found with the

systemId

and

public

identifier,
the resolver will continue searching

uri

entries
with the specified

systemId

or

href

. The

uri

entries
include

uri

,

rewriteURI

, and

uriSuffix

entries.

Error Handling

The interfaces that the CatalogResolver extend specified checked exceptions, including:

- SAXException

and

IOException

by

EntityResolver.resolveEntity(java.lang.String, java.lang.String)
- XMLStreamException

by

XMLResolver.resolveEntity(java.lang.String, java.lang.String, java.lang.String, java.lang.String)
- TransformerException

by

URIResolver.resolve(java.lang.String, java.lang.String)

The CatalogResolver however, will throw

CatalogException

only when

javax.xml.catalog.resolve

is specified as

strict

.
For applications that expect to handle the checked Exceptions, it may be
necessary to use a custom resolver to wrap the CatalogResolver or implement it
with a

Catalog

object.

**Since:** 9

public interface

CatalogResolver

extends

EntityResolver

,

XMLResolver

,

URIResolver

,

LSResourceResolver

A Catalog Resolver that implements SAX

EntityResolver

,
StAX

XMLResolver

,
DOM LS

LSResourceResolver

used by Schema Validation, and
Transform

URIResolver

, and resolves
external references using catalogs.

The

Catalog Standard

distinguished

external identifiers

from

uri entries

as being used to solely identify DTDs, while

uri entries

for
other resources such as stylesheets and schema. The Java APIs, such as

XMLResolver

and

LSResourceResolver

however, make no such distinction.
In consistent with the existing Java API, this CatalogResolver recognizes a
system identifier as a URI and will search both

system

and

uri

entries in a catalog in order to find a matching entry.

The search is started in the current catalog. If a match is found,
no further attempt will be made. Only if there is no match in the current
catalog, will alternate catalogs including delegate and next catalogs be considered.

Search Order

The resolver will first search the system-type of entries with the specified

systemId

. The system entries include

system

,

rewriteSystem

and

systemSuffix

entries.

If no match is found,

public

entries may be searched in accordance with
the

prefer

attribute.

The

prefer

attribute

: if the

prefer

is public,
and there is no match found through the system entries,

public

entries
will be considered. If it is not specified, the

prefer

is public
by default (Note that by the OASIS standard, system entries will always
be considered before public entries. Prefer public means that public entries
will be matched when both system and public identifiers are specified.
In general therefore, prefer public is recommended.)

If no match is found with the

systemId

and

public

identifier,
the resolver will continue searching

uri

entries
with the specified

systemId

or

href

. The

uri

entries
include

uri

,

rewriteURI

, and

uriSuffix

entries.

Error Handling

The interfaces that the CatalogResolver extend specified checked exceptions, including:

- SAXException

and

IOException

by

EntityResolver.resolveEntity(java.lang.String, java.lang.String)
- XMLStreamException

by

XMLResolver.resolveEntity(java.lang.String, java.lang.String, java.lang.String, java.lang.String)
- TransformerException

by

URIResolver.resolve(java.lang.String, java.lang.String)

The CatalogResolver however, will throw

CatalogException

only when

javax.xml.catalog.resolve

is specified as

strict

.
For applications that expect to handle the checked Exceptions, it may be
necessary to use a custom resolver to wrap the CatalogResolver or implement it
with a

Catalog

object.

The

Catalog Standard

distinguished

external identifiers

from

uri entries

as being used to solely identify DTDs, while

uri entries

for
other resources such as stylesheets and schema. The Java APIs, such as

XMLResolver

and

LSResourceResolver

however, make no such distinction.
In consistent with the existing Java API, this CatalogResolver recognizes a
system identifier as a URI and will search both

system

and

uri

entries in a catalog in order to find a matching entry.

The search is started in the current catalog. If a match is found,
no further attempt will be made. Only if there is no match in the current
catalog, will alternate catalogs including delegate and next catalogs be considered.

Search Order

The resolver will first search the system-type of entries with the specified

systemId

. The system entries include

system

,

rewriteSystem

and

systemSuffix

entries.

If no match is found,

public

entries may be searched in accordance with
the

prefer

attribute.

The

prefer

attribute

: if the

prefer

is public,
and there is no match found through the system entries,

public

entries
will be considered. If it is not specified, the

prefer

is public
by default (Note that by the OASIS standard, system entries will always
be considered before public entries. Prefer public means that public entries
will be matched when both system and public identifiers are specified.
In general therefore, prefer public is recommended.)

If no match is found with the

systemId

and

public

identifier,
the resolver will continue searching

uri

entries
with the specified

systemId

or

href

. The

uri

entries
include

uri

,

rewriteURI

, and

uriSuffix

entries.

Error Handling

The interfaces that the CatalogResolver extend specified checked exceptions, including:

- SAXException

and

IOException

by

EntityResolver.resolveEntity(java.lang.String, java.lang.String)
- XMLStreamException

by

XMLResolver.resolveEntity(java.lang.String, java.lang.String, java.lang.String, java.lang.String)
- TransformerException

by

URIResolver.resolve(java.lang.String, java.lang.String)

The CatalogResolver however, will throw

CatalogException

only when

javax.xml.catalog.resolve

is specified as

strict

.
For applications that expect to handle the checked Exceptions, it may be
necessary to use a custom resolver to wrap the CatalogResolver or implement it
with a

Catalog

object.

The search is started in the current catalog. If a match is found,
no further attempt will be made. Only if there is no match in the current
catalog, will alternate catalogs including delegate and next catalogs be considered.

Search Order

The resolver will first search the system-type of entries with the specified

systemId

. The system entries include

system

,

rewriteSystem

and

systemSuffix

entries.

If no match is found,

public

entries may be searched in accordance with
the

prefer

attribute.

The

prefer

attribute

: if the

prefer

is public,
and there is no match found through the system entries,

public

entries
will be considered. If it is not specified, the

prefer

is public
by default (Note that by the OASIS standard, system entries will always
be considered before public entries. Prefer public means that public entries
will be matched when both system and public identifiers are specified.
In general therefore, prefer public is recommended.)

If no match is found with the

systemId

and

public

identifier,
the resolver will continue searching

uri

entries
with the specified

systemId

or

href

. The

uri

entries
include

uri

,

rewriteURI

, and

uriSuffix

entries.

Error Handling

The interfaces that the CatalogResolver extend specified checked exceptions, including:

- SAXException

and

IOException

by

EntityResolver.resolveEntity(java.lang.String, java.lang.String)
- XMLStreamException

by

XMLResolver.resolveEntity(java.lang.String, java.lang.String, java.lang.String, java.lang.String)
- TransformerException

by

URIResolver.resolve(java.lang.String, java.lang.String)

The CatalogResolver however, will throw

CatalogException

only when

javax.xml.catalog.resolve

is specified as

strict

.
For applications that expect to handle the checked Exceptions, it may be
necessary to use a custom resolver to wrap the CatalogResolver or implement it
with a

Catalog

object.

---

#### Search Order

If no match is found,

public

entries may be searched in accordance with
the

prefer

attribute.

The

prefer

attribute

: if the

prefer

is public,
and there is no match found through the system entries,

public

entries
will be considered. If it is not specified, the

prefer

is public
by default (Note that by the OASIS standard, system entries will always
be considered before public entries. Prefer public means that public entries
will be matched when both system and public identifiers are specified.
In general therefore, prefer public is recommended.)

If no match is found with the

systemId

and

public

identifier,
the resolver will continue searching

uri

entries
with the specified

systemId

or

href

. The

uri

entries
include

uri

,

rewriteURI

, and

uriSuffix

entries.

Error Handling

The interfaces that the CatalogResolver extend specified checked exceptions, including:

- SAXException

and

IOException

by

EntityResolver.resolveEntity(java.lang.String, java.lang.String)
- XMLStreamException

by

XMLResolver.resolveEntity(java.lang.String, java.lang.String, java.lang.String, java.lang.String)
- TransformerException

by

URIResolver.resolve(java.lang.String, java.lang.String)

The CatalogResolver however, will throw

CatalogException

only when

javax.xml.catalog.resolve

is specified as

strict

.
For applications that expect to handle the checked Exceptions, it may be
necessary to use a custom resolver to wrap the CatalogResolver or implement it
with a

Catalog

object.

The

prefer

attribute

: if the

prefer

is public,
and there is no match found through the system entries,

public

entries
will be considered. If it is not specified, the

prefer

is public
by default (Note that by the OASIS standard, system entries will always
be considered before public entries. Prefer public means that public entries
will be matched when both system and public identifiers are specified.
In general therefore, prefer public is recommended.)

If no match is found with the

systemId

and

public

identifier,
the resolver will continue searching

uri

entries
with the specified

systemId

or

href

. The

uri

entries
include

uri

,

rewriteURI

, and

uriSuffix

entries.

Error Handling

The interfaces that the CatalogResolver extend specified checked exceptions, including:

- SAXException

and

IOException

by

EntityResolver.resolveEntity(java.lang.String, java.lang.String)
- XMLStreamException

by

XMLResolver.resolveEntity(java.lang.String, java.lang.String, java.lang.String, java.lang.String)
- TransformerException

by

URIResolver.resolve(java.lang.String, java.lang.String)

The CatalogResolver however, will throw

CatalogException

only when

javax.xml.catalog.resolve

is specified as

strict

.
For applications that expect to handle the checked Exceptions, it may be
necessary to use a custom resolver to wrap the CatalogResolver or implement it
with a

Catalog

object.

If no match is found with the

systemId

and

public

identifier,
the resolver will continue searching

uri

entries
with the specified

systemId

or

href

. The

uri

entries
include

uri

,

rewriteURI

, and

uriSuffix

entries.

Error Handling

The interfaces that the CatalogResolver extend specified checked exceptions, including:

- SAXException

and

IOException

by

EntityResolver.resolveEntity(java.lang.String, java.lang.String)
- XMLStreamException

by

XMLResolver.resolveEntity(java.lang.String, java.lang.String, java.lang.String, java.lang.String)
- TransformerException

by

URIResolver.resolve(java.lang.String, java.lang.String)

The CatalogResolver however, will throw

CatalogException

only when

javax.xml.catalog.resolve

is specified as

strict

.
For applications that expect to handle the checked Exceptions, it may be
necessary to use a custom resolver to wrap the CatalogResolver or implement it
with a

Catalog

object.

---

#### Error Handling

SAXException

and

IOException

by

EntityResolver.resolveEntity(java.lang.String, java.lang.String)

XMLStreamException

by

XMLResolver.resolveEntity(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

TransformerException

by

URIResolver.resolve(java.lang.String, java.lang.String)

The CatalogResolver however, will throw

CatalogException

only when

javax.xml.catalog.resolve

is specified as

strict

.
For applications that expect to handle the checked Exceptions, it may be
necessary to use a custom resolver to wrap the CatalogResolver or implement it
with a

Catalog

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Source

resolve

​(

String

href,

String

base)

Implements URIResolver.

InputSource

resolveEntity

​(

String

publicId,

String

systemId)

Implements

EntityResolver

.

InputStream

resolveEntity

​(

String

publicId,

String

systemId,

String

baseUri,

String

namespace)

Implements

XMLResolver

.

LSInput

resolveResource

​(

String

type,

String

namespaceUri,

String

publicId,

String

systemId,

String

baseUri)

Implements

LSResourceResolver

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Source

resolve

​(

String

href,

String

base)

Implements URIResolver.

InputSource

resolveEntity

​(

String

publicId,

String

systemId)

Implements

EntityResolver

.

InputStream

resolveEntity

​(

String

publicId,

String

systemId,

String

baseUri,

String

namespace)

Implements

XMLResolver

.

LSInput

resolveResource

​(

String

type,

String

namespaceUri,

String

publicId,

String

systemId,

String

baseUri)

Implements

LSResourceResolver

.

---

#### Method Summary

Implements URIResolver.

Implements

EntityResolver

.

Implements

XMLResolver

.

Implements

LSResourceResolver

.

============ METHOD DETAIL ==========

- Method Detail

- resolveEntity

```java
InputSource
resolveEntity​(
String
publicId,

String
systemId)
```

Implements

EntityResolver

. The method searches through
the catalog entries in the main and alternative catalogs to attempt to find
a match with the specified

publicId

or systemId.

**Specified by:** resolveEntity

in interface

EntityResolver
**Parameters:** publicId

- the public identifier of the external entity being
referenced, or null if none was supplied
**Parameters:** systemId

- the system identifier of the external entity being
referenced. A system identifier is required on all external entities. XML
requires a system identifier on all external entities, so this value is
always specified.
**Returns:** a

InputSource

object if a mapping is found.
If no mapping is found, returns a

InputSource

object
containing an empty

Reader

if the

javax.xml.catalog.resolve

property is set to

ignore

;
returns null if the

javax.xml.catalog.resolve

property is set to

continue

.
**Throws:** CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict
**See Also:** InputSource

- resolve

```java
Source
resolve​(
String
href,

String
base)
```

Implements URIResolver. The method searches through the catalog entries
in the main and alternative catalogs to attempt to find a match
with the specified

href

attribute. The

href

attribute will
be used literally, with no attempt to be made absolute to the

base

.

If the value is a URN, the

href

attribute is recognized as a

publicId

, and used to search

public

entries.
If the value is a URI, it is taken as a

systemId

, and used to
search both

system

and

uri

entries.

**Specified by:** resolve

in interface

URIResolver
**Parameters:** href

- the href attribute that specifies the URI of a style sheet,
which may be relative or absolute
**Parameters:** base

- The base URI against which the href attribute will be made
absolute if the absolute URI is required
**Returns:** a

Source

object if a mapping is found.
If no mapping is found, returns an empty

Source

object if the

javax.xml.catalog.resolve

property is set to

ignore

;
returns a

Source

object with the original URI
(href, or href resolved with base if base is not null) if the

javax.xml.catalog.resolve

property is set to

continue

.
**Throws:** CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict

- resolveEntity

```java
InputStream
resolveEntity​(
String
publicId,

String
systemId,

String
baseUri,

String
namespace)
```

Implements

XMLResolver

. For the purpose of resolving

publicId

and

systemId

, this method is equivalent to

resolveEntity(java.lang.String, java.lang.String)

.

The

systemId

will be used literally, with no attempt to be made
absolute to the

baseUri

. The

baseUri

and

namespace

are not used in the search for a match in a catalog. However, a relative

systemId

in an xml source may have been made absolute by the parser
with the

baseURI

, thus making it unable to find a

system

entry.
In such a case, a

systemSuffix

entry is recommended over a

system

entry.

**Specified by:** resolveEntity

in interface

XMLResolver
**Parameters:** publicId

- the public identifier of the external entity being
referenced, or null if none was supplied
**Parameters:** systemId

- the system identifier of the external entity being
referenced. A system identifier is required on all external entities. XML
requires a system identifier on all external entities, so this value is
always specified.
**Parameters:** baseUri

- the absolute base URI, not used by the CatalogResolver
**Parameters:** namespace

- the namespace of the entity to resolve, not used by the
CatalogResolver.
**Returns:** an

InputStream

object if a mapping is found; null
if no mapping is found and the

javax.xml.catalog.resolve

property
is set to

continue

or

ignore

. Note that for XMLResolver,
it is not possible to ignore a reference,

ignore

is therefore
treated the same as

continue

.
**Throws:** CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict

- resolveResource

```java
LSInput
resolveResource​(
String
type,

String
namespaceUri,

String
publicId,

String
systemId,

String
baseUri)
```

Implements

LSResourceResolver

. For the purpose of
resolving

publicId

and

systemId

, this method is equivalent
to

resolveEntity(java.lang.String, java.lang.String)

.

The

systemId

will be used literally, with no attempt to be made
absolute to the

baseUri

. The

baseUri

,

namespaceUri

and

type

are not used in the search for a match in a catalog.
However, a relative

systemId

in a source may have been made absolute
by the parser with the

baseURI

, thus making it unable to find a

system

entry. In such a case, a

systemSuffix

entry is
recommended over a

system

entry.

**Specified by:** resolveResource

in interface

LSResourceResolver
**Parameters:** type

- the type of the resource being resolved,
not used by the CatalogResolver
**Parameters:** namespaceUri

- the namespace of the resource being resolved,
not used by the CatalogResolver
**Parameters:** publicId

- the public identifier of the external entity being
referenced, or

null

if no public identifier was
supplied or if the resource is not an entity.
**Parameters:** systemId

- the system identifier, a URI reference of the
external resource being referenced
**Parameters:** baseUri

- the absolute base URI, not used by the CatalogResolver
**Returns:** a

LSInput

object if a mapping is found; null
if no mapping is found and the

javax.xml.catalog.resolve

property
is set to

continue

or

ignore

. Note that for

LSResourceResolver

, it is not possible to ignore a
reference,

ignore

is therefore treated the same as

continue

.
**Throws:** CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict

Method Detail

- resolveEntity

```java
InputSource
resolveEntity​(
String
publicId,

String
systemId)
```

Implements

EntityResolver

. The method searches through
the catalog entries in the main and alternative catalogs to attempt to find
a match with the specified

publicId

or systemId.

**Specified by:** resolveEntity

in interface

EntityResolver
**Parameters:** publicId

- the public identifier of the external entity being
referenced, or null if none was supplied
**Parameters:** systemId

- the system identifier of the external entity being
referenced. A system identifier is required on all external entities. XML
requires a system identifier on all external entities, so this value is
always specified.
**Returns:** a

InputSource

object if a mapping is found.
If no mapping is found, returns a

InputSource

object
containing an empty

Reader

if the

javax.xml.catalog.resolve

property is set to

ignore

;
returns null if the

javax.xml.catalog.resolve

property is set to

continue

.
**Throws:** CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict
**See Also:** InputSource

- resolve

```java
Source
resolve​(
String
href,

String
base)
```

Implements URIResolver. The method searches through the catalog entries
in the main and alternative catalogs to attempt to find a match
with the specified

href

attribute. The

href

attribute will
be used literally, with no attempt to be made absolute to the

base

.

If the value is a URN, the

href

attribute is recognized as a

publicId

, and used to search

public

entries.
If the value is a URI, it is taken as a

systemId

, and used to
search both

system

and

uri

entries.

**Specified by:** resolve

in interface

URIResolver
**Parameters:** href

- the href attribute that specifies the URI of a style sheet,
which may be relative or absolute
**Parameters:** base

- The base URI against which the href attribute will be made
absolute if the absolute URI is required
**Returns:** a

Source

object if a mapping is found.
If no mapping is found, returns an empty

Source

object if the

javax.xml.catalog.resolve

property is set to

ignore

;
returns a

Source

object with the original URI
(href, or href resolved with base if base is not null) if the

javax.xml.catalog.resolve

property is set to

continue

.
**Throws:** CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict

- resolveEntity

```java
InputStream
resolveEntity​(
String
publicId,

String
systemId,

String
baseUri,

String
namespace)
```

Implements

XMLResolver

. For the purpose of resolving

publicId

and

systemId

, this method is equivalent to

resolveEntity(java.lang.String, java.lang.String)

.

The

systemId

will be used literally, with no attempt to be made
absolute to the

baseUri

. The

baseUri

and

namespace

are not used in the search for a match in a catalog. However, a relative

systemId

in an xml source may have been made absolute by the parser
with the

baseURI

, thus making it unable to find a

system

entry.
In such a case, a

systemSuffix

entry is recommended over a

system

entry.

**Specified by:** resolveEntity

in interface

XMLResolver
**Parameters:** publicId

- the public identifier of the external entity being
referenced, or null if none was supplied
**Parameters:** systemId

- the system identifier of the external entity being
referenced. A system identifier is required on all external entities. XML
requires a system identifier on all external entities, so this value is
always specified.
**Parameters:** baseUri

- the absolute base URI, not used by the CatalogResolver
**Parameters:** namespace

- the namespace of the entity to resolve, not used by the
CatalogResolver.
**Returns:** an

InputStream

object if a mapping is found; null
if no mapping is found and the

javax.xml.catalog.resolve

property
is set to

continue

or

ignore

. Note that for XMLResolver,
it is not possible to ignore a reference,

ignore

is therefore
treated the same as

continue

.
**Throws:** CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict

- resolveResource

```java
LSInput
resolveResource​(
String
type,

String
namespaceUri,

String
publicId,

String
systemId,

String
baseUri)
```

Implements

LSResourceResolver

. For the purpose of
resolving

publicId

and

systemId

, this method is equivalent
to

resolveEntity(java.lang.String, java.lang.String)

.

The

systemId

will be used literally, with no attempt to be made
absolute to the

baseUri

. The

baseUri

,

namespaceUri

and

type

are not used in the search for a match in a catalog.
However, a relative

systemId

in a source may have been made absolute
by the parser with the

baseURI

, thus making it unable to find a

system

entry. In such a case, a

systemSuffix

entry is
recommended over a

system

entry.

**Specified by:** resolveResource

in interface

LSResourceResolver
**Parameters:** type

- the type of the resource being resolved,
not used by the CatalogResolver
**Parameters:** namespaceUri

- the namespace of the resource being resolved,
not used by the CatalogResolver
**Parameters:** publicId

- the public identifier of the external entity being
referenced, or

null

if no public identifier was
supplied or if the resource is not an entity.
**Parameters:** systemId

- the system identifier, a URI reference of the
external resource being referenced
**Parameters:** baseUri

- the absolute base URI, not used by the CatalogResolver
**Returns:** a

LSInput

object if a mapping is found; null
if no mapping is found and the

javax.xml.catalog.resolve

property
is set to

continue

or

ignore

. Note that for

LSResourceResolver

, it is not possible to ignore a
reference,

ignore

is therefore treated the same as

continue

.
**Throws:** CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict

---

#### Method Detail

resolveEntity

```java
InputSource
resolveEntity​(
String
publicId,

String
systemId)
```

Implements

EntityResolver

. The method searches through
the catalog entries in the main and alternative catalogs to attempt to find
a match with the specified

publicId

or systemId.

**Specified by:** resolveEntity

in interface

EntityResolver
**Parameters:** publicId

- the public identifier of the external entity being
referenced, or null if none was supplied
**Parameters:** systemId

- the system identifier of the external entity being
referenced. A system identifier is required on all external entities. XML
requires a system identifier on all external entities, so this value is
always specified.
**Returns:** a

InputSource

object if a mapping is found.
If no mapping is found, returns a

InputSource

object
containing an empty

Reader

if the

javax.xml.catalog.resolve

property is set to

ignore

;
returns null if the

javax.xml.catalog.resolve

property is set to

continue

.
**Throws:** CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict
**See Also:** InputSource

---

#### resolveEntity

InputSource

resolveEntity​(

String

publicId,

String

systemId)

Implements

EntityResolver

. The method searches through
the catalog entries in the main and alternative catalogs to attempt to find
a match with the specified

publicId

or systemId.

resolve

```java
Source
resolve​(
String
href,

String
base)
```

Implements URIResolver. The method searches through the catalog entries
in the main and alternative catalogs to attempt to find a match
with the specified

href

attribute. The

href

attribute will
be used literally, with no attempt to be made absolute to the

base

.

If the value is a URN, the

href

attribute is recognized as a

publicId

, and used to search

public

entries.
If the value is a URI, it is taken as a

systemId

, and used to
search both

system

and

uri

entries.

**Specified by:** resolve

in interface

URIResolver
**Parameters:** href

- the href attribute that specifies the URI of a style sheet,
which may be relative or absolute
**Parameters:** base

- The base URI against which the href attribute will be made
absolute if the absolute URI is required
**Returns:** a

Source

object if a mapping is found.
If no mapping is found, returns an empty

Source

object if the

javax.xml.catalog.resolve

property is set to

ignore

;
returns a

Source

object with the original URI
(href, or href resolved with base if base is not null) if the

javax.xml.catalog.resolve

property is set to

continue

.
**Throws:** CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict

---

#### resolve

Source

resolve​(

String

href,

String

base)

Implements URIResolver. The method searches through the catalog entries
in the main and alternative catalogs to attempt to find a match
with the specified

href

attribute. The

href

attribute will
be used literally, with no attempt to be made absolute to the

base

.

If the value is a URN, the

href

attribute is recognized as a

publicId

, and used to search

public

entries.
If the value is a URI, it is taken as a

systemId

, and used to
search both

system

and

uri

entries.

If the value is a URN, the

href

attribute is recognized as a

publicId

, and used to search

public

entries.
If the value is a URI, it is taken as a

systemId

, and used to
search both

system

and

uri

entries.

resolveEntity

```java
InputStream
resolveEntity​(
String
publicId,

String
systemId,

String
baseUri,

String
namespace)
```

Implements

XMLResolver

. For the purpose of resolving

publicId

and

systemId

, this method is equivalent to

resolveEntity(java.lang.String, java.lang.String)

.

The

systemId

will be used literally, with no attempt to be made
absolute to the

baseUri

. The

baseUri

and

namespace

are not used in the search for a match in a catalog. However, a relative

systemId

in an xml source may have been made absolute by the parser
with the

baseURI

, thus making it unable to find a

system

entry.
In such a case, a

systemSuffix

entry is recommended over a

system

entry.

**Specified by:** resolveEntity

in interface

XMLResolver
**Parameters:** publicId

- the public identifier of the external entity being
referenced, or null if none was supplied
**Parameters:** systemId

- the system identifier of the external entity being
referenced. A system identifier is required on all external entities. XML
requires a system identifier on all external entities, so this value is
always specified.
**Parameters:** baseUri

- the absolute base URI, not used by the CatalogResolver
**Parameters:** namespace

- the namespace of the entity to resolve, not used by the
CatalogResolver.
**Returns:** an

InputStream

object if a mapping is found; null
if no mapping is found and the

javax.xml.catalog.resolve

property
is set to

continue

or

ignore

. Note that for XMLResolver,
it is not possible to ignore a reference,

ignore

is therefore
treated the same as

continue

.
**Throws:** CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict

---

#### resolveEntity

InputStream

resolveEntity​(

String

publicId,

String

systemId,

String

baseUri,

String

namespace)

Implements

XMLResolver

. For the purpose of resolving

publicId

and

systemId

, this method is equivalent to

resolveEntity(java.lang.String, java.lang.String)

.

The

systemId

will be used literally, with no attempt to be made
absolute to the

baseUri

. The

baseUri

and

namespace

are not used in the search for a match in a catalog. However, a relative

systemId

in an xml source may have been made absolute by the parser
with the

baseURI

, thus making it unable to find a

system

entry.
In such a case, a

systemSuffix

entry is recommended over a

system

entry.

The

systemId

will be used literally, with no attempt to be made
absolute to the

baseUri

. The

baseUri

and

namespace

are not used in the search for a match in a catalog. However, a relative

systemId

in an xml source may have been made absolute by the parser
with the

baseURI

, thus making it unable to find a

system

entry.
In such a case, a

systemSuffix

entry is recommended over a

system

entry.

resolveResource

```java
LSInput
resolveResource​(
String
type,

String
namespaceUri,

String
publicId,

String
systemId,

String
baseUri)
```

Implements

LSResourceResolver

. For the purpose of
resolving

publicId

and

systemId

, this method is equivalent
to

resolveEntity(java.lang.String, java.lang.String)

.

The

systemId

will be used literally, with no attempt to be made
absolute to the

baseUri

. The

baseUri

,

namespaceUri

and

type

are not used in the search for a match in a catalog.
However, a relative

systemId

in a source may have been made absolute
by the parser with the

baseURI

, thus making it unable to find a

system

entry. In such a case, a

systemSuffix

entry is
recommended over a

system

entry.

**Specified by:** resolveResource

in interface

LSResourceResolver
**Parameters:** type

- the type of the resource being resolved,
not used by the CatalogResolver
**Parameters:** namespaceUri

- the namespace of the resource being resolved,
not used by the CatalogResolver
**Parameters:** publicId

- the public identifier of the external entity being
referenced, or

null

if no public identifier was
supplied or if the resource is not an entity.
**Parameters:** systemId

- the system identifier, a URI reference of the
external resource being referenced
**Parameters:** baseUri

- the absolute base URI, not used by the CatalogResolver
**Returns:** a

LSInput

object if a mapping is found; null
if no mapping is found and the

javax.xml.catalog.resolve

property
is set to

continue

or

ignore

. Note that for

LSResourceResolver

, it is not possible to ignore a
reference,

ignore

is therefore treated the same as

continue

.
**Throws:** CatalogException

- if no mapping is found and

javax.xml.catalog.resolve

is specified as

strict

---

#### resolveResource

LSInput

resolveResource​(

String

type,

String

namespaceUri,

String

publicId,

String

systemId,

String

baseUri)

Implements

LSResourceResolver

. For the purpose of
resolving

publicId

and

systemId

, this method is equivalent
to

resolveEntity(java.lang.String, java.lang.String)

.

The

systemId

will be used literally, with no attempt to be made
absolute to the

baseUri

. The

baseUri

,

namespaceUri

and

type

are not used in the search for a match in a catalog.
However, a relative

systemId

in a source may have been made absolute
by the parser with the

baseURI

, thus making it unable to find a

system

entry. In such a case, a

systemSuffix

entry is
recommended over a

system

entry.

The

systemId

will be used literally, with no attempt to be made
absolute to the

baseUri

. The

baseUri

,

namespaceUri

and

type

are not used in the search for a match in a catalog.
However, a relative

systemId

in a source may have been made absolute
by the parser with the

baseURI

, thus making it unable to find a

system

entry. In such a case, a

systemSuffix

entry is
recommended over a

system

entry.

---

