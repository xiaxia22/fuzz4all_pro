# Class CatalogManager

**Source:** `java.xml\javax\xml\catalog\CatalogManager.html`

### Class Description

```java
public final class
CatalogManager

extends
Object
```

The Catalog Manager manages the creation of XML Catalogs and Catalog Resolvers.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Catalog
catalog​(
CatalogFeatures
features,

URI
... uris)

Creates a

Catalog

object using the specified feature settings and
uri(s) to one or more catalog files.

If

uris

is empty, system property

javax.xml.catalog.files

,
as defined in

CatalogFeatures

, will be read to locate the initial
list of catalog files.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting Catalog object
will contain no Catalog elements. Any matching operation using the Catalog
will return null.

**Parameters:**
- features

- the catalog features
- uris

- uri(s) to one or more catalogs.

**Returns:**
- an instance of a

Catalog

**Throws:**
- IllegalArgumentException

- if either the URIs are not absolute
or do not have a URL protocol handler for the URI scheme
- CatalogException

- If an error occurs while parsing the catalog
- SecurityException

- if access to the resource is denied by the security manager

---

#### public static
CatalogResolver
catalogResolver​(
Catalog
catalog)

Creates an instance of a

CatalogResolver

using the specified catalog.

**Parameters:**
- catalog

- the catalog instance

**Returns:**
- an instance of a

CatalogResolver

---

#### public static
CatalogResolver
catalogResolver​(
CatalogFeatures
features,

URI
... uris)

Creates an instance of a

CatalogResolver

using the specified feature
settings and uri(s) to one or more catalog files.

If

uris

is empty, system property

javax.xml.catalog.files

,
as defined in

CatalogFeatures

, will be read to locate the initial
list of catalog files.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting CatalogResolver
object will contain no valid catalog. Any resolution operation using the
resolver therefore will return as no mapping is found. See

CatalogResolver

for the behavior when no mapping is found.

**Parameters:**
- features

- the catalog features
- uris

- the uri(s) to one or more catalogs

**Returns:**
- an instance of a

CatalogResolver

**Throws:**
- IllegalArgumentException

- if either the URIs are not absolute
or do not have a URL protocol handler for the URI scheme
- CatalogException

- If an error occurs while parsing the catalog
- SecurityException

- if access to the resource is denied by the security manager

---

### Additional Sections

#### Class CatalogManager

java.lang.Object

- javax.xml.catalog.CatalogManager

javax.xml.catalog.CatalogManager

```java
public final class
CatalogManager

extends
Object
```

The Catalog Manager manages the creation of XML Catalogs and Catalog Resolvers.

**Since:** 9

public final class

CatalogManager

extends

Object

The Catalog Manager manages the creation of XML Catalogs and Catalog Resolvers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Catalog

catalog

​(

CatalogFeatures

features,

URI

... uris)

Creates a

Catalog

object using the specified feature settings and
uri(s) to one or more catalog files.

static

CatalogResolver

catalogResolver

​(

Catalog

catalog)

Creates an instance of a

CatalogResolver

using the specified catalog.

static

CatalogResolver

catalogResolver

​(

CatalogFeatures

features,

URI

... uris)

Creates an instance of a

CatalogResolver

using the specified feature
settings and uri(s) to one or more catalog files.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Catalog

catalog

​(

CatalogFeatures

features,

URI

... uris)

Creates a

Catalog

object using the specified feature settings and
uri(s) to one or more catalog files.

static

CatalogResolver

catalogResolver

​(

Catalog

catalog)

Creates an instance of a

CatalogResolver

using the specified catalog.

static

CatalogResolver

catalogResolver

​(

CatalogFeatures

features,

URI

... uris)

Creates an instance of a

CatalogResolver

using the specified feature
settings and uri(s) to one or more catalog files.

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

Creates a

Catalog

object using the specified feature settings and
uri(s) to one or more catalog files.

Creates an instance of a

CatalogResolver

using the specified catalog.

Creates an instance of a

CatalogResolver

using the specified feature
settings and uri(s) to one or more catalog files.

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

============ METHOD DETAIL ==========

- Method Detail

- catalog

```java
public static
Catalog
catalog​(
CatalogFeatures
features,

URI
... uris)
```

Creates a

Catalog

object using the specified feature settings and
uri(s) to one or more catalog files.

If

uris

is empty, system property

javax.xml.catalog.files

,
as defined in

CatalogFeatures

, will be read to locate the initial
list of catalog files.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting Catalog object
will contain no Catalog elements. Any matching operation using the Catalog
will return null.

**Parameters:** features

- the catalog features
**Parameters:** uris

- uri(s) to one or more catalogs.
**Returns:** an instance of a

Catalog
**Throws:** IllegalArgumentException

- if either the URIs are not absolute
or do not have a URL protocol handler for the URI scheme
**Throws:** CatalogException

- If an error occurs while parsing the catalog
**Throws:** SecurityException

- if access to the resource is denied by the security manager

- catalogResolver

```java
public static
CatalogResolver
catalogResolver​(
Catalog
catalog)
```

Creates an instance of a

CatalogResolver

using the specified catalog.

**Parameters:** catalog

- the catalog instance
**Returns:** an instance of a

CatalogResolver

- catalogResolver

```java
public static
CatalogResolver
catalogResolver​(
CatalogFeatures
features,

URI
... uris)
```

Creates an instance of a

CatalogResolver

using the specified feature
settings and uri(s) to one or more catalog files.

If

uris

is empty, system property

javax.xml.catalog.files

,
as defined in

CatalogFeatures

, will be read to locate the initial
list of catalog files.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting CatalogResolver
object will contain no valid catalog. Any resolution operation using the
resolver therefore will return as no mapping is found. See

CatalogResolver

for the behavior when no mapping is found.

**Parameters:** features

- the catalog features
**Parameters:** uris

- the uri(s) to one or more catalogs
**Returns:** an instance of a

CatalogResolver
**Throws:** IllegalArgumentException

- if either the URIs are not absolute
or do not have a URL protocol handler for the URI scheme
**Throws:** CatalogException

- If an error occurs while parsing the catalog
**Throws:** SecurityException

- if access to the resource is denied by the security manager

Method Detail

- catalog

```java
public static
Catalog
catalog​(
CatalogFeatures
features,

URI
... uris)
```

Creates a

Catalog

object using the specified feature settings and
uri(s) to one or more catalog files.

If

uris

is empty, system property

javax.xml.catalog.files

,
as defined in

CatalogFeatures

, will be read to locate the initial
list of catalog files.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting Catalog object
will contain no Catalog elements. Any matching operation using the Catalog
will return null.

**Parameters:** features

- the catalog features
**Parameters:** uris

- uri(s) to one or more catalogs.
**Returns:** an instance of a

Catalog
**Throws:** IllegalArgumentException

- if either the URIs are not absolute
or do not have a URL protocol handler for the URI scheme
**Throws:** CatalogException

- If an error occurs while parsing the catalog
**Throws:** SecurityException

- if access to the resource is denied by the security manager

- catalogResolver

```java
public static
CatalogResolver
catalogResolver​(
Catalog
catalog)
```

Creates an instance of a

CatalogResolver

using the specified catalog.

**Parameters:** catalog

- the catalog instance
**Returns:** an instance of a

CatalogResolver

- catalogResolver

```java
public static
CatalogResolver
catalogResolver​(
CatalogFeatures
features,

URI
... uris)
```

Creates an instance of a

CatalogResolver

using the specified feature
settings and uri(s) to one or more catalog files.

If

uris

is empty, system property

javax.xml.catalog.files

,
as defined in

CatalogFeatures

, will be read to locate the initial
list of catalog files.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting CatalogResolver
object will contain no valid catalog. Any resolution operation using the
resolver therefore will return as no mapping is found. See

CatalogResolver

for the behavior when no mapping is found.

**Parameters:** features

- the catalog features
**Parameters:** uris

- the uri(s) to one or more catalogs
**Returns:** an instance of a

CatalogResolver
**Throws:** IllegalArgumentException

- if either the URIs are not absolute
or do not have a URL protocol handler for the URI scheme
**Throws:** CatalogException

- If an error occurs while parsing the catalog
**Throws:** SecurityException

- if access to the resource is denied by the security manager

---

#### Method Detail

catalog

```java
public static
Catalog
catalog​(
CatalogFeatures
features,

URI
... uris)
```

Creates a

Catalog

object using the specified feature settings and
uri(s) to one or more catalog files.

If

uris

is empty, system property

javax.xml.catalog.files

,
as defined in

CatalogFeatures

, will be read to locate the initial
list of catalog files.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting Catalog object
will contain no Catalog elements. Any matching operation using the Catalog
will return null.

**Parameters:** features

- the catalog features
**Parameters:** uris

- uri(s) to one or more catalogs.
**Returns:** an instance of a

Catalog
**Throws:** IllegalArgumentException

- if either the URIs are not absolute
or do not have a URL protocol handler for the URI scheme
**Throws:** CatalogException

- If an error occurs while parsing the catalog
**Throws:** SecurityException

- if access to the resource is denied by the security manager

---

#### catalog

public static

Catalog

catalog​(

CatalogFeatures

features,

URI

... uris)

Creates a

Catalog

object using the specified feature settings and
uri(s) to one or more catalog files.

If

uris

is empty, system property

javax.xml.catalog.files

,
as defined in

CatalogFeatures

, will be read to locate the initial
list of catalog files.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting Catalog object
will contain no Catalog elements. Any matching operation using the Catalog
will return null.

If

uris

is empty, system property

javax.xml.catalog.files

,
as defined in

CatalogFeatures

, will be read to locate the initial
list of catalog files.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting Catalog object
will contain no Catalog elements. Any matching operation using the Catalog
will return null.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting Catalog object
will contain no Catalog elements. Any matching operation using the Catalog
will return null.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting Catalog object
will contain no Catalog elements. Any matching operation using the Catalog
will return null.

catalogResolver

```java
public static
CatalogResolver
catalogResolver​(
Catalog
catalog)
```

Creates an instance of a

CatalogResolver

using the specified catalog.

**Parameters:** catalog

- the catalog instance
**Returns:** an instance of a

CatalogResolver

---

#### catalogResolver

public static

CatalogResolver

catalogResolver​(

Catalog

catalog)

Creates an instance of a

CatalogResolver

using the specified catalog.

catalogResolver

```java
public static
CatalogResolver
catalogResolver​(
CatalogFeatures
features,

URI
... uris)
```

Creates an instance of a

CatalogResolver

using the specified feature
settings and uri(s) to one or more catalog files.

If

uris

is empty, system property

javax.xml.catalog.files

,
as defined in

CatalogFeatures

, will be read to locate the initial
list of catalog files.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting CatalogResolver
object will contain no valid catalog. Any resolution operation using the
resolver therefore will return as no mapping is found. See

CatalogResolver

for the behavior when no mapping is found.

**Parameters:** features

- the catalog features
**Parameters:** uris

- the uri(s) to one or more catalogs
**Returns:** an instance of a

CatalogResolver
**Throws:** IllegalArgumentException

- if either the URIs are not absolute
or do not have a URL protocol handler for the URI scheme
**Throws:** CatalogException

- If an error occurs while parsing the catalog
**Throws:** SecurityException

- if access to the resource is denied by the security manager

---

#### catalogResolver

public static

CatalogResolver

catalogResolver​(

CatalogFeatures

features,

URI

... uris)

Creates an instance of a

CatalogResolver

using the specified feature
settings and uri(s) to one or more catalog files.

If

uris

is empty, system property

javax.xml.catalog.files

,
as defined in

CatalogFeatures

, will be read to locate the initial
list of catalog files.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting CatalogResolver
object will contain no valid catalog. Any resolution operation using the
resolver therefore will return as no mapping is found. See

CatalogResolver

for the behavior when no mapping is found.

If

uris

is empty, system property

javax.xml.catalog.files

,
as defined in

CatalogFeatures

, will be read to locate the initial
list of catalog files.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting CatalogResolver
object will contain no valid catalog. Any resolution operation using the
resolver therefore will return as no mapping is found. See

CatalogResolver

for the behavior when no mapping is found.

If multiple catalog files are specified through the

uris

argument or

javax.xml.catalog.files

property, the first entry is considered
the main catalog, while others are treated as alternative catalogs after
those referenced by the

nextCatalog

elements in the main catalog.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting CatalogResolver
object will contain no valid catalog. Any resolution operation using the
resolver therefore will return as no mapping is found. See

CatalogResolver

for the behavior when no mapping is found.

As specified in

XML Catalogs, OASIS Standard V1.1

, if a catalog entry is invalid, it
is ignored. In case all entries are invalid, the resulting CatalogResolver
object will contain no valid catalog. Any resolution operation using the
resolver therefore will return as no mapping is found. See

CatalogResolver

for the behavior when no mapping is found.

---

