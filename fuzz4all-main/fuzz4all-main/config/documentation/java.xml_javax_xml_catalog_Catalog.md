# Interface Catalog

**Source:** `java.xml\javax\xml\catalog\Catalog.html`

### Class Description

```java
public interface
Catalog
```

The Catalog class represents an entity Catalog as defined by

XML Catalogs, OASIS Standard V1.1, 7 October 2005

.

A catalog is an XML file that contains a root

catalog

entry with a list
of catalog entries. The entries can also be grouped with a

group

entry.
The catalog and group entries may specify

prefer

and

xml:base

attributes that set preference of public or system type of entries and base URI
to resolve relative URIs.

A catalog can be used in two situations:

- Locate the external resources with a public or system identifier;
- Locate an alternate URI reference with a URI.

For case 1, the standard defines 6 External Identifier Entries:

public, system, rewriteSystem, systemSuffix, delegatePublic, and
delegateSystem

.

While for case 2, it defines 4 URI Entries:

uri, rewriteURI, uriSuffix and delegateURI

.

In addition to the above entry types, a catalog may define nextCatalog
entries to add additional catalog entry files.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
matchSystem​(
String
systemId)

Attempts to find a matching entry in the catalog by systemId.

The method searches through the system-type entries, including

system,
rewriteSystem, systemSuffix, delegateSystem

, and

group

entries in the
current catalog in order to find a match.

Resolution follows the steps listed below:

- If a matching

system

entry exists, it is returned immediately.
- If more than one

rewriteSystem

entry matches, the matching entry with
the longest normalized

systemIdStartString

value is returned.
- If more than one

systemSuffix

entry matches, the matching entry
with the longest normalized

systemIdSuffix

value is returned.
- If more than one

delegateSystem

entry matches, the matching entry
with the longest matching

systemIdStartString

value is returned.

**Parameters:**
- systemId

- the system identifier of the entity to be matched

**Returns:**
- a URI string if a mapping is found, or null otherwise

---

#### String
matchPublic​(
String
publicId)

Attempts to find a matching entry in the catalog by publicId. The method
searches through the public-type entries, including

public,
delegatePublic

, and

group

entries in the current catalog in order to find
a match.

Refer to the description about

Feature PREFER in the table Catalog Features

in class

CatalogFeatures

. Public entries are only considered if the

prefer

is

public

and

system

entries are not found.

Resolution follows the steps listed below:

- If a matching

public

entry is found, it is returned immediately.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

publicIdStartString

value is returned.

**Parameters:**
- publicId

- the public identifier of the entity to be matched

**Returns:**
- a URI string if a mapping is found, or null otherwise

**See Also:**
- CatalogFeatures.Feature

---

#### String
matchURI​(
String
uri)

Attempts to find a matching entry in the catalog by the uri element.

The method searches through the uri-type entries, including

uri,
rewriteURI, uriSuffix, delegateURI

and

group

entries in the current
catalog in order to find a match.

Resolution follows the steps listed below:

- If a matching

uri

entry is found, it is returned immediately.
- If more than one

rewriteURI

entry matches, the matching entry with
the longest normalized

uriStartString

value is returned.
- If more than one

uriSuffix

entry matches, the matching entry with
the longest normalized

uriSuffix

value is returned.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

uriStartString

value is returned.

**Parameters:**
- uri

- the URI reference of the entity to be matched

**Returns:**
- a URI string if a mapping is found, or null otherwise

---

#### Stream
<
Catalog
> catalogs()

Returns a sequential Stream of alternative Catalogs specified using the

nextCatalog

entries in the current catalog, and as the input of
catalog files excluding the current catalog (that is, the first in the
input list) when the Catalog object is created by the

CatalogManager

.

The order of Catalogs in the returned stream is the same as the order
in which the corresponding

nextCatalog

entries appear in the
current catalog. The alternative catalogs from the input file list are
appended to the end of the stream in the order they are entered.

**Returns:**
- a sequential Stream of Catalogs

---

### Additional Sections

#### Interface Catalog

```java
public interface
Catalog
```

The Catalog class represents an entity Catalog as defined by

XML Catalogs, OASIS Standard V1.1, 7 October 2005

.

A catalog is an XML file that contains a root

catalog

entry with a list
of catalog entries. The entries can also be grouped with a

group

entry.
The catalog and group entries may specify

prefer

and

xml:base

attributes that set preference of public or system type of entries and base URI
to resolve relative URIs.

A catalog can be used in two situations:

- Locate the external resources with a public or system identifier;
- Locate an alternate URI reference with a URI.

For case 1, the standard defines 6 External Identifier Entries:

public, system, rewriteSystem, systemSuffix, delegatePublic, and
delegateSystem

.

While for case 2, it defines 4 URI Entries:

uri, rewriteURI, uriSuffix and delegateURI

.

In addition to the above entry types, a catalog may define nextCatalog
entries to add additional catalog entry files.

**Since:** 9

public interface

Catalog

The Catalog class represents an entity Catalog as defined by

XML Catalogs, OASIS Standard V1.1, 7 October 2005

.

A catalog is an XML file that contains a root

catalog

entry with a list
of catalog entries. The entries can also be grouped with a

group

entry.
The catalog and group entries may specify

prefer

and

xml:base

attributes that set preference of public or system type of entries and base URI
to resolve relative URIs.

A catalog can be used in two situations:

- Locate the external resources with a public or system identifier;
- Locate an alternate URI reference with a URI.

For case 1, the standard defines 6 External Identifier Entries:

public, system, rewriteSystem, systemSuffix, delegatePublic, and
delegateSystem

.

While for case 2, it defines 4 URI Entries:

uri, rewriteURI, uriSuffix and delegateURI

.

In addition to the above entry types, a catalog may define nextCatalog
entries to add additional catalog entry files.

A catalog is an XML file that contains a root

catalog

entry with a list
of catalog entries. The entries can also be grouped with a

group

entry.
The catalog and group entries may specify

prefer

and

xml:base

attributes that set preference of public or system type of entries and base URI
to resolve relative URIs.

A catalog can be used in two situations:

- Locate the external resources with a public or system identifier;
- Locate an alternate URI reference with a URI.

For case 1, the standard defines 6 External Identifier Entries:

public, system, rewriteSystem, systemSuffix, delegatePublic, and
delegateSystem

.

While for case 2, it defines 4 URI Entries:

uri, rewriteURI, uriSuffix and delegateURI

.

In addition to the above entry types, a catalog may define nextCatalog
entries to add additional catalog entry files.

A catalog can be used in two situations:

- Locate the external resources with a public or system identifier;
- Locate an alternate URI reference with a URI.

For case 1, the standard defines 6 External Identifier Entries:

public, system, rewriteSystem, systemSuffix, delegatePublic, and
delegateSystem

.

While for case 2, it defines 4 URI Entries:

uri, rewriteURI, uriSuffix and delegateURI

.

In addition to the above entry types, a catalog may define nextCatalog
entries to add additional catalog entry files.

Locate the external resources with a public or system identifier;

Locate an alternate URI reference with a URI.

For case 1, the standard defines 6 External Identifier Entries:

public, system, rewriteSystem, systemSuffix, delegatePublic, and
delegateSystem

.

While for case 2, it defines 4 URI Entries:

uri, rewriteURI, uriSuffix and delegateURI

.

In addition to the above entry types, a catalog may define nextCatalog
entries to add additional catalog entry files.

While for case 2, it defines 4 URI Entries:

uri, rewriteURI, uriSuffix and delegateURI

.

In addition to the above entry types, a catalog may define nextCatalog
entries to add additional catalog entry files.

In addition to the above entry types, a catalog may define nextCatalog
entries to add additional catalog entry files.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Stream

<

Catalog

>

catalogs

()

Returns a sequential Stream of alternative Catalogs specified using the

nextCatalog

entries in the current catalog, and as the input of
catalog files excluding the current catalog (that is, the first in the
input list) when the Catalog object is created by the

CatalogManager

.

String

matchPublic

​(

String

publicId)

Attempts to find a matching entry in the catalog by publicId.

String

matchSystem

​(

String

systemId)

Attempts to find a matching entry in the catalog by systemId.

String

matchURI

​(

String

uri)

Attempts to find a matching entry in the catalog by the uri element.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Stream

<

Catalog

>

catalogs

()

Returns a sequential Stream of alternative Catalogs specified using the

nextCatalog

entries in the current catalog, and as the input of
catalog files excluding the current catalog (that is, the first in the
input list) when the Catalog object is created by the

CatalogManager

.

String

matchPublic

​(

String

publicId)

Attempts to find a matching entry in the catalog by publicId.

String

matchSystem

​(

String

systemId)

Attempts to find a matching entry in the catalog by systemId.

String

matchURI

​(

String

uri)

Attempts to find a matching entry in the catalog by the uri element.

---

#### Method Summary

Returns a sequential Stream of alternative Catalogs specified using the

nextCatalog

entries in the current catalog, and as the input of
catalog files excluding the current catalog (that is, the first in the
input list) when the Catalog object is created by the

CatalogManager

.

Attempts to find a matching entry in the catalog by publicId.

Attempts to find a matching entry in the catalog by systemId.

Attempts to find a matching entry in the catalog by the uri element.

============ METHOD DETAIL ==========

- Method Detail

- matchSystem

```java
String
matchSystem​(
String
systemId)
```

Attempts to find a matching entry in the catalog by systemId.

The method searches through the system-type entries, including

system,
rewriteSystem, systemSuffix, delegateSystem

, and

group

entries in the
current catalog in order to find a match.

Resolution follows the steps listed below:

- If a matching

system

entry exists, it is returned immediately.
- If more than one

rewriteSystem

entry matches, the matching entry with
the longest normalized

systemIdStartString

value is returned.
- If more than one

systemSuffix

entry matches, the matching entry
with the longest normalized

systemIdSuffix

value is returned.
- If more than one

delegateSystem

entry matches, the matching entry
with the longest matching

systemIdStartString

value is returned.

**Parameters:** systemId

- the system identifier of the entity to be matched
**Returns:** a URI string if a mapping is found, or null otherwise

- matchPublic

```java
String
matchPublic​(
String
publicId)
```

Attempts to find a matching entry in the catalog by publicId. The method
searches through the public-type entries, including

public,
delegatePublic

, and

group

entries in the current catalog in order to find
a match.

Refer to the description about

Feature PREFER in the table Catalog Features

in class

CatalogFeatures

. Public entries are only considered if the

prefer

is

public

and

system

entries are not found.

Resolution follows the steps listed below:

- If a matching

public

entry is found, it is returned immediately.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

publicIdStartString

value is returned.

**Parameters:** publicId

- the public identifier of the entity to be matched
**Returns:** a URI string if a mapping is found, or null otherwise
**See Also:** CatalogFeatures.Feature

- matchURI

```java
String
matchURI​(
String
uri)
```

Attempts to find a matching entry in the catalog by the uri element.

The method searches through the uri-type entries, including

uri,
rewriteURI, uriSuffix, delegateURI

and

group

entries in the current
catalog in order to find a match.

Resolution follows the steps listed below:

- If a matching

uri

entry is found, it is returned immediately.
- If more than one

rewriteURI

entry matches, the matching entry with
the longest normalized

uriStartString

value is returned.
- If more than one

uriSuffix

entry matches, the matching entry with
the longest normalized

uriSuffix

value is returned.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

uriStartString

value is returned.

**Parameters:** uri

- the URI reference of the entity to be matched
**Returns:** a URI string if a mapping is found, or null otherwise

- catalogs

```java
Stream
<
Catalog
> catalogs()
```

Returns a sequential Stream of alternative Catalogs specified using the

nextCatalog

entries in the current catalog, and as the input of
catalog files excluding the current catalog (that is, the first in the
input list) when the Catalog object is created by the

CatalogManager

.

The order of Catalogs in the returned stream is the same as the order
in which the corresponding

nextCatalog

entries appear in the
current catalog. The alternative catalogs from the input file list are
appended to the end of the stream in the order they are entered.

**Returns:** a sequential Stream of Catalogs

Method Detail

- matchSystem

```java
String
matchSystem​(
String
systemId)
```

Attempts to find a matching entry in the catalog by systemId.

The method searches through the system-type entries, including

system,
rewriteSystem, systemSuffix, delegateSystem

, and

group

entries in the
current catalog in order to find a match.

Resolution follows the steps listed below:

- If a matching

system

entry exists, it is returned immediately.
- If more than one

rewriteSystem

entry matches, the matching entry with
the longest normalized

systemIdStartString

value is returned.
- If more than one

systemSuffix

entry matches, the matching entry
with the longest normalized

systemIdSuffix

value is returned.
- If more than one

delegateSystem

entry matches, the matching entry
with the longest matching

systemIdStartString

value is returned.

**Parameters:** systemId

- the system identifier of the entity to be matched
**Returns:** a URI string if a mapping is found, or null otherwise

- matchPublic

```java
String
matchPublic​(
String
publicId)
```

Attempts to find a matching entry in the catalog by publicId. The method
searches through the public-type entries, including

public,
delegatePublic

, and

group

entries in the current catalog in order to find
a match.

Refer to the description about

Feature PREFER in the table Catalog Features

in class

CatalogFeatures

. Public entries are only considered if the

prefer

is

public

and

system

entries are not found.

Resolution follows the steps listed below:

- If a matching

public

entry is found, it is returned immediately.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

publicIdStartString

value is returned.

**Parameters:** publicId

- the public identifier of the entity to be matched
**Returns:** a URI string if a mapping is found, or null otherwise
**See Also:** CatalogFeatures.Feature

- matchURI

```java
String
matchURI​(
String
uri)
```

Attempts to find a matching entry in the catalog by the uri element.

The method searches through the uri-type entries, including

uri,
rewriteURI, uriSuffix, delegateURI

and

group

entries in the current
catalog in order to find a match.

Resolution follows the steps listed below:

- If a matching

uri

entry is found, it is returned immediately.
- If more than one

rewriteURI

entry matches, the matching entry with
the longest normalized

uriStartString

value is returned.
- If more than one

uriSuffix

entry matches, the matching entry with
the longest normalized

uriSuffix

value is returned.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

uriStartString

value is returned.

**Parameters:** uri

- the URI reference of the entity to be matched
**Returns:** a URI string if a mapping is found, or null otherwise

- catalogs

```java
Stream
<
Catalog
> catalogs()
```

Returns a sequential Stream of alternative Catalogs specified using the

nextCatalog

entries in the current catalog, and as the input of
catalog files excluding the current catalog (that is, the first in the
input list) when the Catalog object is created by the

CatalogManager

.

The order of Catalogs in the returned stream is the same as the order
in which the corresponding

nextCatalog

entries appear in the
current catalog. The alternative catalogs from the input file list are
appended to the end of the stream in the order they are entered.

**Returns:** a sequential Stream of Catalogs

---

#### Method Detail

matchSystem

```java
String
matchSystem​(
String
systemId)
```

Attempts to find a matching entry in the catalog by systemId.

The method searches through the system-type entries, including

system,
rewriteSystem, systemSuffix, delegateSystem

, and

group

entries in the
current catalog in order to find a match.

Resolution follows the steps listed below:

- If a matching

system

entry exists, it is returned immediately.
- If more than one

rewriteSystem

entry matches, the matching entry with
the longest normalized

systemIdStartString

value is returned.
- If more than one

systemSuffix

entry matches, the matching entry
with the longest normalized

systemIdSuffix

value is returned.
- If more than one

delegateSystem

entry matches, the matching entry
with the longest matching

systemIdStartString

value is returned.

**Parameters:** systemId

- the system identifier of the entity to be matched
**Returns:** a URI string if a mapping is found, or null otherwise

---

#### matchSystem

String

matchSystem​(

String

systemId)

Attempts to find a matching entry in the catalog by systemId.

The method searches through the system-type entries, including

system,
rewriteSystem, systemSuffix, delegateSystem

, and

group

entries in the
current catalog in order to find a match.

Resolution follows the steps listed below:

- If a matching

system

entry exists, it is returned immediately.
- If more than one

rewriteSystem

entry matches, the matching entry with
the longest normalized

systemIdStartString

value is returned.
- If more than one

systemSuffix

entry matches, the matching entry
with the longest normalized

systemIdSuffix

value is returned.
- If more than one

delegateSystem

entry matches, the matching entry
with the longest matching

systemIdStartString

value is returned.

The method searches through the system-type entries, including

system,
rewriteSystem, systemSuffix, delegateSystem

, and

group

entries in the
current catalog in order to find a match.

Resolution follows the steps listed below:

- If a matching

system

entry exists, it is returned immediately.
- If more than one

rewriteSystem

entry matches, the matching entry with
the longest normalized

systemIdStartString

value is returned.
- If more than one

systemSuffix

entry matches, the matching entry
with the longest normalized

systemIdSuffix

value is returned.
- If more than one

delegateSystem

entry matches, the matching entry
with the longest matching

systemIdStartString

value is returned.

Resolution follows the steps listed below:

- If a matching

system

entry exists, it is returned immediately.
- If more than one

rewriteSystem

entry matches, the matching entry with
the longest normalized

systemIdStartString

value is returned.
- If more than one

systemSuffix

entry matches, the matching entry
with the longest normalized

systemIdSuffix

value is returned.
- If more than one

delegateSystem

entry matches, the matching entry
with the longest matching

systemIdStartString

value is returned.

If a matching

system

entry exists, it is returned immediately.

If more than one

rewriteSystem

entry matches, the matching entry with
the longest normalized

systemIdStartString

value is returned.

If more than one

systemSuffix

entry matches, the matching entry
with the longest normalized

systemIdSuffix

value is returned.

If more than one

delegateSystem

entry matches, the matching entry
with the longest matching

systemIdStartString

value is returned.

matchPublic

```java
String
matchPublic​(
String
publicId)
```

Attempts to find a matching entry in the catalog by publicId. The method
searches through the public-type entries, including

public,
delegatePublic

, and

group

entries in the current catalog in order to find
a match.

Refer to the description about

Feature PREFER in the table Catalog Features

in class

CatalogFeatures

. Public entries are only considered if the

prefer

is

public

and

system

entries are not found.

Resolution follows the steps listed below:

- If a matching

public

entry is found, it is returned immediately.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

publicIdStartString

value is returned.

**Parameters:** publicId

- the public identifier of the entity to be matched
**Returns:** a URI string if a mapping is found, or null otherwise
**See Also:** CatalogFeatures.Feature

---

#### matchPublic

String

matchPublic​(

String

publicId)

Attempts to find a matching entry in the catalog by publicId. The method
searches through the public-type entries, including

public,
delegatePublic

, and

group

entries in the current catalog in order to find
a match.

Refer to the description about

Feature PREFER in the table Catalog Features

in class

CatalogFeatures

. Public entries are only considered if the

prefer

is

public

and

system

entries are not found.

Resolution follows the steps listed below:

- If a matching

public

entry is found, it is returned immediately.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

publicIdStartString

value is returned.

Refer to the description about

Feature PREFER in the table Catalog Features

in class

CatalogFeatures

. Public entries are only considered if the

prefer

is

public

and

system

entries are not found.

Resolution follows the steps listed below:

- If a matching

public

entry is found, it is returned immediately.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

publicIdStartString

value is returned.

Resolution follows the steps listed below:

- If a matching

public

entry is found, it is returned immediately.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

publicIdStartString

value is returned.

If a matching

public

entry is found, it is returned immediately.

If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

publicIdStartString

value is returned.

matchURI

```java
String
matchURI​(
String
uri)
```

Attempts to find a matching entry in the catalog by the uri element.

The method searches through the uri-type entries, including

uri,
rewriteURI, uriSuffix, delegateURI

and

group

entries in the current
catalog in order to find a match.

Resolution follows the steps listed below:

- If a matching

uri

entry is found, it is returned immediately.
- If more than one

rewriteURI

entry matches, the matching entry with
the longest normalized

uriStartString

value is returned.
- If more than one

uriSuffix

entry matches, the matching entry with
the longest normalized

uriSuffix

value is returned.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

uriStartString

value is returned.

**Parameters:** uri

- the URI reference of the entity to be matched
**Returns:** a URI string if a mapping is found, or null otherwise

---

#### matchURI

String

matchURI​(

String

uri)

Attempts to find a matching entry in the catalog by the uri element.

The method searches through the uri-type entries, including

uri,
rewriteURI, uriSuffix, delegateURI

and

group

entries in the current
catalog in order to find a match.

Resolution follows the steps listed below:

- If a matching

uri

entry is found, it is returned immediately.
- If more than one

rewriteURI

entry matches, the matching entry with
the longest normalized

uriStartString

value is returned.
- If more than one

uriSuffix

entry matches, the matching entry with
the longest normalized

uriSuffix

value is returned.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

uriStartString

value is returned.

The method searches through the uri-type entries, including

uri,
rewriteURI, uriSuffix, delegateURI

and

group

entries in the current
catalog in order to find a match.

Resolution follows the steps listed below:

- If a matching

uri

entry is found, it is returned immediately.
- If more than one

rewriteURI

entry matches, the matching entry with
the longest normalized

uriStartString

value is returned.
- If more than one

uriSuffix

entry matches, the matching entry with
the longest normalized

uriSuffix

value is returned.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

uriStartString

value is returned.

Resolution follows the steps listed below:

- If a matching

uri

entry is found, it is returned immediately.
- If more than one

rewriteURI

entry matches, the matching entry with
the longest normalized

uriStartString

value is returned.
- If more than one

uriSuffix

entry matches, the matching entry with
the longest normalized

uriSuffix

value is returned.
- If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

uriStartString

value is returned.

If a matching

uri

entry is found, it is returned immediately.

If more than one

rewriteURI

entry matches, the matching entry with
the longest normalized

uriStartString

value is returned.

If more than one

uriSuffix

entry matches, the matching entry with
the longest normalized

uriSuffix

value is returned.

If more than one

delegatePublic

entry matches, the matching entry
with the longest matching

uriStartString

value is returned.

catalogs

```java
Stream
<
Catalog
> catalogs()
```

Returns a sequential Stream of alternative Catalogs specified using the

nextCatalog

entries in the current catalog, and as the input of
catalog files excluding the current catalog (that is, the first in the
input list) when the Catalog object is created by the

CatalogManager

.

The order of Catalogs in the returned stream is the same as the order
in which the corresponding

nextCatalog

entries appear in the
current catalog. The alternative catalogs from the input file list are
appended to the end of the stream in the order they are entered.

**Returns:** a sequential Stream of Catalogs

---

#### catalogs

Stream

<

Catalog

> catalogs()

Returns a sequential Stream of alternative Catalogs specified using the

nextCatalog

entries in the current catalog, and as the input of
catalog files excluding the current catalog (that is, the first in the
input list) when the Catalog object is created by the

CatalogManager

.

The order of Catalogs in the returned stream is the same as the order
in which the corresponding

nextCatalog

entries appear in the
current catalog. The alternative catalogs from the input file list are
appended to the end of the stream in the order they are entered.

The order of Catalogs in the returned stream is the same as the order
in which the corresponding

nextCatalog

entries appear in the
current catalog. The alternative catalogs from the input file list are
appended to the end of the stream in the order they are entered.

---

