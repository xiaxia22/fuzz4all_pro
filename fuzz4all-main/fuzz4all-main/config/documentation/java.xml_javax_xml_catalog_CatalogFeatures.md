# Class CatalogFeatures

**Source:** `java.xml\javax\xml\catalog\CatalogFeatures.html`

### Class Description

```java
public class
CatalogFeatures

extends
Object
```

The CatalogFeatures holds a collection of features and properties.

Catalog Features

Feature

Description

Property Name

System Property [1]

jaxp.properties [1]

Value [2]

Action

Type

Value

FILES

A semicolon-delimited list of URIs to locate the catalog files.
The URIs must be absolute and have a URL protocol handler for the URI scheme.

javax.xml.catalog.files

javax.xml.catalog.files

javax.xml.catalog.files

String

URIs

Reads the first catalog as the current catalog; Loads others if no match
is found in the current catalog including delegate catalogs if any.

PREFER

Indicates the preference between the public and system
identifiers. The default value is public [3].

javax.xml.catalog.prefer

N/A

N/A

String

system

Searches system entries for a match; Searches public entries when
external identifier specifies only a public identifier

public

Searches system entries for a match; Searches public entries when
there is no matching system entry.

DEFER

Indicates that the alternative catalogs including those
specified in delegate entries or nextCatalog are not read until they are
needed. The default value is true.

javax.xml.catalog.defer [4]

javax.xml.catalog.defer

javax.xml.catalog.defer

String

true

Loads alternative catalogs as needed.

false

Loads all catalogs[5].

RESOLVE

Determines the action if there is no matching entry found after
all of the specified catalogs are exhausted. The default is strict.

javax.xml.catalog.resolve [4]

javax.xml.catalog.resolve

javax.xml.catalog.resolve

String

strict

Throws CatalogException if there is no match.

continue

Allows the XML parser to continue as if there is no match.

ignore

Tells the XML parser to skip the external references if there no match.

[1]

There is no System property for the features that marked as "N/A".

[2]

The value shall be exactly as listed in this table, case-sensitive.
Any unspecified value will result in

IllegalArgumentException

.

[3]

The Catalog specification defined complex rules on

the prefer attribute

. Although the prefer can be public or system, the
specification actually made system the preferred option, that is, no matter
the option, a system entry is always used if found. Public entries are only
considered if the prefer is public and system entries are not found. It is
therefore recommended that the prefer attribute be set as public
(which is the default).

[4]

Although non-standard attributes in the OASIS Catalog specification,

defer

and

resolve

are recognized by the Java Catalog API the
same as the

prefer

as being an attribute in the catalog entry of the
main catalog. Note that only the attributes specified for the catalog entry
of the main Catalog file will be used.

[5]

If the intention is to share an entire catalog store, it may be desirable to
set the property

javax.xml.catalog.defer

to false to allow the entire
catalog to be pre-loaded.

Scope and Order

Features and properties can be set through the catalog file, the Catalog API,
system properties, and

jaxp.properties

, with a preference in the same order.

Properties that are specified as attributes in the catalog file for the
catalog and group entries shall take preference over any of the other settings.
For example, if a

prefer

attribute is set in the catalog file as in

<catalog prefer="public">

, any other input for the "prefer" property
is not necessary or will be ignored.

Properties set through the Catalog API override those that may have been set
by system properties and/or in

jaxp.properties

. In case of multiple
interfaces, the latest in a procedure shall take preference. For

CatalogFeatures.Feature.FILES

, this means that the URI(s) specified through the methods
of the

CatalogManager

will override any that may have been entered
through the

CatalogFeatures.Builder

.

System properties when set shall override those in

jaxp.properties

.

The

jaxp.properties

file is typically in the conf directory of the Java
installation. The file is read only once by the JAXP implementation and
its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any properties in

jaxp.properties

after it has been read.

A CatalogFeatures instance can be created through its builder as illustrated
in the following sample code:

```java
CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();
```

JAXP XML Processor Support

The Catalog Features are supported throughout the JAXP processors, including
SAX and DOM (

javax.xml.parsers

), and StAX parsers (

javax.xml.stream

),
Schema Validation (

javax.xml.validation

), and XML Transformation
(

javax.xml.transform

). The features described above can be set through JAXP
factories or processors that define a setProperty or setAttribute interface.
For example, the following code snippet sets a URI to a catalog file on a SAX
parser through the

javax.xml.catalog.files

property:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");
```

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
CatalogFeatures
defaults()

Returns a CatalogFeatures instance with default settings.

**Returns:**
- a default CatalogFeatures instance

---

#### public
String
get​(
CatalogFeatures.Feature
cf)

Returns the value of the specified feature.

**Parameters:**
- cf

- the type of the Catalog feature

**Returns:**
- the value of the feature

---

#### public static
CatalogFeatures.Builder
builder()

Returns an instance of the builder for creating the CatalogFeatures object.

**Returns:**
- an instance of the builder

---

### Additional Sections

#### Class CatalogFeatures

java.lang.Object

- javax.xml.catalog.CatalogFeatures

javax.xml.catalog.CatalogFeatures

```java
public class
CatalogFeatures

extends
Object
```

The CatalogFeatures holds a collection of features and properties.

Catalog Features

Feature

Description

Property Name

System Property [1]

jaxp.properties [1]

Value [2]

Action

Type

Value

FILES

A semicolon-delimited list of URIs to locate the catalog files.
The URIs must be absolute and have a URL protocol handler for the URI scheme.

javax.xml.catalog.files

javax.xml.catalog.files

javax.xml.catalog.files

String

URIs

Reads the first catalog as the current catalog; Loads others if no match
is found in the current catalog including delegate catalogs if any.

PREFER

Indicates the preference between the public and system
identifiers. The default value is public [3].

javax.xml.catalog.prefer

N/A

N/A

String

system

Searches system entries for a match; Searches public entries when
external identifier specifies only a public identifier

public

Searches system entries for a match; Searches public entries when
there is no matching system entry.

DEFER

Indicates that the alternative catalogs including those
specified in delegate entries or nextCatalog are not read until they are
needed. The default value is true.

javax.xml.catalog.defer [4]

javax.xml.catalog.defer

javax.xml.catalog.defer

String

true

Loads alternative catalogs as needed.

false

Loads all catalogs[5].

RESOLVE

Determines the action if there is no matching entry found after
all of the specified catalogs are exhausted. The default is strict.

javax.xml.catalog.resolve [4]

javax.xml.catalog.resolve

javax.xml.catalog.resolve

String

strict

Throws CatalogException if there is no match.

continue

Allows the XML parser to continue as if there is no match.

ignore

Tells the XML parser to skip the external references if there no match.

[1]

There is no System property for the features that marked as "N/A".

[2]

The value shall be exactly as listed in this table, case-sensitive.
Any unspecified value will result in

IllegalArgumentException

.

[3]

The Catalog specification defined complex rules on

the prefer attribute

. Although the prefer can be public or system, the
specification actually made system the preferred option, that is, no matter
the option, a system entry is always used if found. Public entries are only
considered if the prefer is public and system entries are not found. It is
therefore recommended that the prefer attribute be set as public
(which is the default).

[4]

Although non-standard attributes in the OASIS Catalog specification,

defer

and

resolve

are recognized by the Java Catalog API the
same as the

prefer

as being an attribute in the catalog entry of the
main catalog. Note that only the attributes specified for the catalog entry
of the main Catalog file will be used.

[5]

If the intention is to share an entire catalog store, it may be desirable to
set the property

javax.xml.catalog.defer

to false to allow the entire
catalog to be pre-loaded.

Scope and Order

Features and properties can be set through the catalog file, the Catalog API,
system properties, and

jaxp.properties

, with a preference in the same order.

Properties that are specified as attributes in the catalog file for the
catalog and group entries shall take preference over any of the other settings.
For example, if a

prefer

attribute is set in the catalog file as in

<catalog prefer="public">

, any other input for the "prefer" property
is not necessary or will be ignored.

Properties set through the Catalog API override those that may have been set
by system properties and/or in

jaxp.properties

. In case of multiple
interfaces, the latest in a procedure shall take preference. For

CatalogFeatures.Feature.FILES

, this means that the URI(s) specified through the methods
of the

CatalogManager

will override any that may have been entered
through the

CatalogFeatures.Builder

.

System properties when set shall override those in

jaxp.properties

.

The

jaxp.properties

file is typically in the conf directory of the Java
installation. The file is read only once by the JAXP implementation and
its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any properties in

jaxp.properties

after it has been read.

A CatalogFeatures instance can be created through its builder as illustrated
in the following sample code:

```java
CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();
```

JAXP XML Processor Support

The Catalog Features are supported throughout the JAXP processors, including
SAX and DOM (

javax.xml.parsers

), and StAX parsers (

javax.xml.stream

),
Schema Validation (

javax.xml.validation

), and XML Transformation
(

javax.xml.transform

). The features described above can be set through JAXP
factories or processors that define a setProperty or setAttribute interface.
For example, the following code snippet sets a URI to a catalog file on a SAX
parser through the

javax.xml.catalog.files

property:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");
```

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

**Since:** 9

public class

CatalogFeatures

extends

Object

The CatalogFeatures holds a collection of features and properties.

Catalog Features

Feature

Description

Property Name

System Property [1]

jaxp.properties [1]

Value [2]

Action

Type

Value

FILES

A semicolon-delimited list of URIs to locate the catalog files.
The URIs must be absolute and have a URL protocol handler for the URI scheme.

javax.xml.catalog.files

javax.xml.catalog.files

javax.xml.catalog.files

String

URIs

Reads the first catalog as the current catalog; Loads others if no match
is found in the current catalog including delegate catalogs if any.

PREFER

Indicates the preference between the public and system
identifiers. The default value is public [3].

javax.xml.catalog.prefer

N/A

N/A

String

system

Searches system entries for a match; Searches public entries when
external identifier specifies only a public identifier

public

Searches system entries for a match; Searches public entries when
there is no matching system entry.

DEFER

Indicates that the alternative catalogs including those
specified in delegate entries or nextCatalog are not read until they are
needed. The default value is true.

javax.xml.catalog.defer [4]

javax.xml.catalog.defer

javax.xml.catalog.defer

String

true

Loads alternative catalogs as needed.

false

Loads all catalogs[5].

RESOLVE

Determines the action if there is no matching entry found after
all of the specified catalogs are exhausted. The default is strict.

javax.xml.catalog.resolve [4]

javax.xml.catalog.resolve

javax.xml.catalog.resolve

String

strict

Throws CatalogException if there is no match.

continue

Allows the XML parser to continue as if there is no match.

ignore

Tells the XML parser to skip the external references if there no match.

[1]

There is no System property for the features that marked as "N/A".

[2]

The value shall be exactly as listed in this table, case-sensitive.
Any unspecified value will result in

IllegalArgumentException

.

[3]

The Catalog specification defined complex rules on

the prefer attribute

. Although the prefer can be public or system, the
specification actually made system the preferred option, that is, no matter
the option, a system entry is always used if found. Public entries are only
considered if the prefer is public and system entries are not found. It is
therefore recommended that the prefer attribute be set as public
(which is the default).

[4]

Although non-standard attributes in the OASIS Catalog specification,

defer

and

resolve

are recognized by the Java Catalog API the
same as the

prefer

as being an attribute in the catalog entry of the
main catalog. Note that only the attributes specified for the catalog entry
of the main Catalog file will be used.

[5]

If the intention is to share an entire catalog store, it may be desirable to
set the property

javax.xml.catalog.defer

to false to allow the entire
catalog to be pre-loaded.

Scope and Order

Features and properties can be set through the catalog file, the Catalog API,
system properties, and

jaxp.properties

, with a preference in the same order.

Properties that are specified as attributes in the catalog file for the
catalog and group entries shall take preference over any of the other settings.
For example, if a

prefer

attribute is set in the catalog file as in

<catalog prefer="public">

, any other input for the "prefer" property
is not necessary or will be ignored.

Properties set through the Catalog API override those that may have been set
by system properties and/or in

jaxp.properties

. In case of multiple
interfaces, the latest in a procedure shall take preference. For

CatalogFeatures.Feature.FILES

, this means that the URI(s) specified through the methods
of the

CatalogManager

will override any that may have been entered
through the

CatalogFeatures.Builder

.

System properties when set shall override those in

jaxp.properties

.

The

jaxp.properties

file is typically in the conf directory of the Java
installation. The file is read only once by the JAXP implementation and
its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any properties in

jaxp.properties

after it has been read.

A CatalogFeatures instance can be created through its builder as illustrated
in the following sample code:

```java
CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();
```

JAXP XML Processor Support

The Catalog Features are supported throughout the JAXP processors, including
SAX and DOM (

javax.xml.parsers

), and StAX parsers (

javax.xml.stream

),
Schema Validation (

javax.xml.validation

), and XML Transformation
(

javax.xml.transform

). The features described above can be set through JAXP
factories or processors that define a setProperty or setAttribute interface.
For example, the following code snippet sets a URI to a catalog file on a SAX
parser through the

javax.xml.catalog.files

property:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");
```

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

[1]

There is no System property for the features that marked as "N/A".

[2]

The value shall be exactly as listed in this table, case-sensitive.
Any unspecified value will result in

IllegalArgumentException

.

[3]

The Catalog specification defined complex rules on

the prefer attribute

. Although the prefer can be public or system, the
specification actually made system the preferred option, that is, no matter
the option, a system entry is always used if found. Public entries are only
considered if the prefer is public and system entries are not found. It is
therefore recommended that the prefer attribute be set as public
(which is the default).

[4]

Although non-standard attributes in the OASIS Catalog specification,

defer

and

resolve

are recognized by the Java Catalog API the
same as the

prefer

as being an attribute in the catalog entry of the
main catalog. Note that only the attributes specified for the catalog entry
of the main Catalog file will be used.

[5]

If the intention is to share an entire catalog store, it may be desirable to
set the property

javax.xml.catalog.defer

to false to allow the entire
catalog to be pre-loaded.

Scope and Order

Features and properties can be set through the catalog file, the Catalog API,
system properties, and

jaxp.properties

, with a preference in the same order.

Properties that are specified as attributes in the catalog file for the
catalog and group entries shall take preference over any of the other settings.
For example, if a

prefer

attribute is set in the catalog file as in

<catalog prefer="public">

, any other input for the "prefer" property
is not necessary or will be ignored.

Properties set through the Catalog API override those that may have been set
by system properties and/or in

jaxp.properties

. In case of multiple
interfaces, the latest in a procedure shall take preference. For

CatalogFeatures.Feature.FILES

, this means that the URI(s) specified through the methods
of the

CatalogManager

will override any that may have been entered
through the

CatalogFeatures.Builder

.

System properties when set shall override those in

jaxp.properties

.

The

jaxp.properties

file is typically in the conf directory of the Java
installation. The file is read only once by the JAXP implementation and
its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any properties in

jaxp.properties

after it has been read.

A CatalogFeatures instance can be created through its builder as illustrated
in the following sample code:

```java
CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();
```

JAXP XML Processor Support

The Catalog Features are supported throughout the JAXP processors, including
SAX and DOM (

javax.xml.parsers

), and StAX parsers (

javax.xml.stream

),
Schema Validation (

javax.xml.validation

), and XML Transformation
(

javax.xml.transform

). The features described above can be set through JAXP
factories or processors that define a setProperty or setAttribute interface.
For example, the following code snippet sets a URI to a catalog file on a SAX
parser through the

javax.xml.catalog.files

property:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");
```

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

[2]

The value shall be exactly as listed in this table, case-sensitive.
Any unspecified value will result in

IllegalArgumentException

.

[3]

The Catalog specification defined complex rules on

the prefer attribute

. Although the prefer can be public or system, the
specification actually made system the preferred option, that is, no matter
the option, a system entry is always used if found. Public entries are only
considered if the prefer is public and system entries are not found. It is
therefore recommended that the prefer attribute be set as public
(which is the default).

[4]

Although non-standard attributes in the OASIS Catalog specification,

defer

and

resolve

are recognized by the Java Catalog API the
same as the

prefer

as being an attribute in the catalog entry of the
main catalog. Note that only the attributes specified for the catalog entry
of the main Catalog file will be used.

[5]

If the intention is to share an entire catalog store, it may be desirable to
set the property

javax.xml.catalog.defer

to false to allow the entire
catalog to be pre-loaded.

Scope and Order

Features and properties can be set through the catalog file, the Catalog API,
system properties, and

jaxp.properties

, with a preference in the same order.

Properties that are specified as attributes in the catalog file for the
catalog and group entries shall take preference over any of the other settings.
For example, if a

prefer

attribute is set in the catalog file as in

<catalog prefer="public">

, any other input for the "prefer" property
is not necessary or will be ignored.

Properties set through the Catalog API override those that may have been set
by system properties and/or in

jaxp.properties

. In case of multiple
interfaces, the latest in a procedure shall take preference. For

CatalogFeatures.Feature.FILES

, this means that the URI(s) specified through the methods
of the

CatalogManager

will override any that may have been entered
through the

CatalogFeatures.Builder

.

System properties when set shall override those in

jaxp.properties

.

The

jaxp.properties

file is typically in the conf directory of the Java
installation. The file is read only once by the JAXP implementation and
its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any properties in

jaxp.properties

after it has been read.

A CatalogFeatures instance can be created through its builder as illustrated
in the following sample code:

```java
CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();
```

JAXP XML Processor Support

The Catalog Features are supported throughout the JAXP processors, including
SAX and DOM (

javax.xml.parsers

), and StAX parsers (

javax.xml.stream

),
Schema Validation (

javax.xml.validation

), and XML Transformation
(

javax.xml.transform

). The features described above can be set through JAXP
factories or processors that define a setProperty or setAttribute interface.
For example, the following code snippet sets a URI to a catalog file on a SAX
parser through the

javax.xml.catalog.files

property:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");
```

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

[3]

The Catalog specification defined complex rules on

the prefer attribute

. Although the prefer can be public or system, the
specification actually made system the preferred option, that is, no matter
the option, a system entry is always used if found. Public entries are only
considered if the prefer is public and system entries are not found. It is
therefore recommended that the prefer attribute be set as public
(which is the default).

[4]

Although non-standard attributes in the OASIS Catalog specification,

defer

and

resolve

are recognized by the Java Catalog API the
same as the

prefer

as being an attribute in the catalog entry of the
main catalog. Note that only the attributes specified for the catalog entry
of the main Catalog file will be used.

[5]

If the intention is to share an entire catalog store, it may be desirable to
set the property

javax.xml.catalog.defer

to false to allow the entire
catalog to be pre-loaded.

Scope and Order

Features and properties can be set through the catalog file, the Catalog API,
system properties, and

jaxp.properties

, with a preference in the same order.

Properties that are specified as attributes in the catalog file for the
catalog and group entries shall take preference over any of the other settings.
For example, if a

prefer

attribute is set in the catalog file as in

<catalog prefer="public">

, any other input for the "prefer" property
is not necessary or will be ignored.

Properties set through the Catalog API override those that may have been set
by system properties and/or in

jaxp.properties

. In case of multiple
interfaces, the latest in a procedure shall take preference. For

CatalogFeatures.Feature.FILES

, this means that the URI(s) specified through the methods
of the

CatalogManager

will override any that may have been entered
through the

CatalogFeatures.Builder

.

System properties when set shall override those in

jaxp.properties

.

The

jaxp.properties

file is typically in the conf directory of the Java
installation. The file is read only once by the JAXP implementation and
its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any properties in

jaxp.properties

after it has been read.

A CatalogFeatures instance can be created through its builder as illustrated
in the following sample code:

```java
CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();
```

JAXP XML Processor Support

The Catalog Features are supported throughout the JAXP processors, including
SAX and DOM (

javax.xml.parsers

), and StAX parsers (

javax.xml.stream

),
Schema Validation (

javax.xml.validation

), and XML Transformation
(

javax.xml.transform

). The features described above can be set through JAXP
factories or processors that define a setProperty or setAttribute interface.
For example, the following code snippet sets a URI to a catalog file on a SAX
parser through the

javax.xml.catalog.files

property:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");
```

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

[4]

Although non-standard attributes in the OASIS Catalog specification,

defer

and

resolve

are recognized by the Java Catalog API the
same as the

prefer

as being an attribute in the catalog entry of the
main catalog. Note that only the attributes specified for the catalog entry
of the main Catalog file will be used.

[5]

If the intention is to share an entire catalog store, it may be desirable to
set the property

javax.xml.catalog.defer

to false to allow the entire
catalog to be pre-loaded.

Scope and Order

Features and properties can be set through the catalog file, the Catalog API,
system properties, and

jaxp.properties

, with a preference in the same order.

Properties that are specified as attributes in the catalog file for the
catalog and group entries shall take preference over any of the other settings.
For example, if a

prefer

attribute is set in the catalog file as in

<catalog prefer="public">

, any other input for the "prefer" property
is not necessary or will be ignored.

Properties set through the Catalog API override those that may have been set
by system properties and/or in

jaxp.properties

. In case of multiple
interfaces, the latest in a procedure shall take preference. For

CatalogFeatures.Feature.FILES

, this means that the URI(s) specified through the methods
of the

CatalogManager

will override any that may have been entered
through the

CatalogFeatures.Builder

.

System properties when set shall override those in

jaxp.properties

.

The

jaxp.properties

file is typically in the conf directory of the Java
installation. The file is read only once by the JAXP implementation and
its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any properties in

jaxp.properties

after it has been read.

A CatalogFeatures instance can be created through its builder as illustrated
in the following sample code:

```java
CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();
```

JAXP XML Processor Support

The Catalog Features are supported throughout the JAXP processors, including
SAX and DOM (

javax.xml.parsers

), and StAX parsers (

javax.xml.stream

),
Schema Validation (

javax.xml.validation

), and XML Transformation
(

javax.xml.transform

). The features described above can be set through JAXP
factories or processors that define a setProperty or setAttribute interface.
For example, the following code snippet sets a URI to a catalog file on a SAX
parser through the

javax.xml.catalog.files

property:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");
```

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

[5]

If the intention is to share an entire catalog store, it may be desirable to
set the property

javax.xml.catalog.defer

to false to allow the entire
catalog to be pre-loaded.

Scope and Order

Features and properties can be set through the catalog file, the Catalog API,
system properties, and

jaxp.properties

, with a preference in the same order.

Properties that are specified as attributes in the catalog file for the
catalog and group entries shall take preference over any of the other settings.
For example, if a

prefer

attribute is set in the catalog file as in

<catalog prefer="public">

, any other input for the "prefer" property
is not necessary or will be ignored.

Properties set through the Catalog API override those that may have been set
by system properties and/or in

jaxp.properties

. In case of multiple
interfaces, the latest in a procedure shall take preference. For

CatalogFeatures.Feature.FILES

, this means that the URI(s) specified through the methods
of the

CatalogManager

will override any that may have been entered
through the

CatalogFeatures.Builder

.

System properties when set shall override those in

jaxp.properties

.

The

jaxp.properties

file is typically in the conf directory of the Java
installation. The file is read only once by the JAXP implementation and
its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any properties in

jaxp.properties

after it has been read.

A CatalogFeatures instance can be created through its builder as illustrated
in the following sample code:

```java
CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();
```

JAXP XML Processor Support

The Catalog Features are supported throughout the JAXP processors, including
SAX and DOM (

javax.xml.parsers

), and StAX parsers (

javax.xml.stream

),
Schema Validation (

javax.xml.validation

), and XML Transformation
(

javax.xml.transform

). The features described above can be set through JAXP
factories or processors that define a setProperty or setAttribute interface.
For example, the following code snippet sets a URI to a catalog file on a SAX
parser through the

javax.xml.catalog.files

property:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");
```

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

---

#### Scope and Order

Properties that are specified as attributes in the catalog file for the
catalog and group entries shall take preference over any of the other settings.
For example, if a

prefer

attribute is set in the catalog file as in

<catalog prefer="public">

, any other input for the "prefer" property
is not necessary or will be ignored.

Properties set through the Catalog API override those that may have been set
by system properties and/or in

jaxp.properties

. In case of multiple
interfaces, the latest in a procedure shall take preference. For

CatalogFeatures.Feature.FILES

, this means that the URI(s) specified through the methods
of the

CatalogManager

will override any that may have been entered
through the

CatalogFeatures.Builder

.

System properties when set shall override those in

jaxp.properties

.

The

jaxp.properties

file is typically in the conf directory of the Java
installation. The file is read only once by the JAXP implementation and
its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any properties in

jaxp.properties

after it has been read.

A CatalogFeatures instance can be created through its builder as illustrated
in the following sample code:

```java
CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();
```

JAXP XML Processor Support

The Catalog Features are supported throughout the JAXP processors, including
SAX and DOM (

javax.xml.parsers

), and StAX parsers (

javax.xml.stream

),
Schema Validation (

javax.xml.validation

), and XML Transformation
(

javax.xml.transform

). The features described above can be set through JAXP
factories or processors that define a setProperty or setAttribute interface.
For example, the following code snippet sets a URI to a catalog file on a SAX
parser through the

javax.xml.catalog.files

property:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");
```

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

Properties set through the Catalog API override those that may have been set
by system properties and/or in

jaxp.properties

. In case of multiple
interfaces, the latest in a procedure shall take preference. For

CatalogFeatures.Feature.FILES

, this means that the URI(s) specified through the methods
of the

CatalogManager

will override any that may have been entered
through the

CatalogFeatures.Builder

.

System properties when set shall override those in

jaxp.properties

.

The

jaxp.properties

file is typically in the conf directory of the Java
installation. The file is read only once by the JAXP implementation and
its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any properties in

jaxp.properties

after it has been read.

A CatalogFeatures instance can be created through its builder as illustrated
in the following sample code:

```java
CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();
```

JAXP XML Processor Support

The Catalog Features are supported throughout the JAXP processors, including
SAX and DOM (

javax.xml.parsers

), and StAX parsers (

javax.xml.stream

),
Schema Validation (

javax.xml.validation

), and XML Transformation
(

javax.xml.transform

). The features described above can be set through JAXP
factories or processors that define a setProperty or setAttribute interface.
For example, the following code snippet sets a URI to a catalog file on a SAX
parser through the

javax.xml.catalog.files

property:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");
```

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

System properties when set shall override those in

jaxp.properties

.

The

jaxp.properties

file is typically in the conf directory of the Java
installation. The file is read only once by the JAXP implementation and
its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any properties in

jaxp.properties

after it has been read.

A CatalogFeatures instance can be created through its builder as illustrated
in the following sample code:

```java
CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();
```

JAXP XML Processor Support

The Catalog Features are supported throughout the JAXP processors, including
SAX and DOM (

javax.xml.parsers

), and StAX parsers (

javax.xml.stream

),
Schema Validation (

javax.xml.validation

), and XML Transformation
(

javax.xml.transform

). The features described above can be set through JAXP
factories or processors that define a setProperty or setAttribute interface.
For example, the following code snippet sets a URI to a catalog file on a SAX
parser through the

javax.xml.catalog.files

property:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");
```

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

The

jaxp.properties

file is typically in the conf directory of the Java
installation. The file is read only once by the JAXP implementation and
its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any properties in

jaxp.properties

after it has been read.

A CatalogFeatures instance can be created through its builder as illustrated
in the following sample code:

```java
CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();
```

JAXP XML Processor Support

The Catalog Features are supported throughout the JAXP processors, including
SAX and DOM (

javax.xml.parsers

), and StAX parsers (

javax.xml.stream

),
Schema Validation (

javax.xml.validation

), and XML Transformation
(

javax.xml.transform

). The features described above can be set through JAXP
factories or processors that define a setProperty or setAttribute interface.
For example, the following code snippet sets a URI to a catalog file on a SAX
parser through the

javax.xml.catalog.files

property:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");
```

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

A CatalogFeatures instance can be created through its builder as illustrated
in the following sample code:

```java
CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();
```

JAXP XML Processor Support

The Catalog Features are supported throughout the JAXP processors, including
SAX and DOM (

javax.xml.parsers

), and StAX parsers (

javax.xml.stream

),
Schema Validation (

javax.xml.validation

), and XML Transformation
(

javax.xml.transform

). The features described above can be set through JAXP
factories or processors that define a setProperty or setAttribute interface.
For example, the following code snippet sets a URI to a catalog file on a SAX
parser through the

javax.xml.catalog.files

property:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");
```

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

CatalogFeatures f = CatalogFeatures.builder()
.with(Feature.FILES, "file:///etc/xml/catalog")
.with(Feature.PREFER, "public")
.with(Feature.DEFER, "true")
.with(Feature.RESOLVE, "ignore")
.build();

---

#### JAXP XML Processor Support

SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true); [1]
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "file:///etc/xml/catalog");

[1] Note that this statement is not required since the default value of

USE_CATALOG

is true.

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

The JAXP Processors' support for Catalog depends on both the

USE_CATALOG

feature and the
existence of valid Catalog file(s). A JAXP processor will use the Catalog
only when the feature is true and valid Catalog file(s) are specified through
the

javax.xml.catalog.files

property. It will make no attempt to use
the Catalog if either

USE_CATALOG

is set to false, or there is no Catalog file specified.

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

The JAXP processors will observe the default settings of the

CatalogFeatures

. The processors, for example, will
report an Exception by default when no matching entry is found since the
default value of the

javax.xml.catalog.resolve

property is strict.

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

The JAXP processors give preference to user-specified custom resolvers. If such
a resolver is registered, it will be used over the CatalogResolver. If it returns
null however, the processors will continue resolving with the CatalogResolver.
If it returns an empty source, no attempt will be made by the CatalogResolver.

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

The Catalog support is available for any process in the JAXP library that
supports a resolver. The following table lists all such processes.

Processes with Catalog Support

Processes with Catalog Support

Process

Catalog Entry Type

Example

DTDs and external entities

public, system

```java
The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>
```

XInclude

uri

```java
The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
```

XSD import

uri

```java
The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>
```

XSD include

uri

```java
The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
```

XSL import and include

uri

```java
The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>
```

XSL document function

uri

```java
The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>
```

---

#### Processes with Catalog Support

The following DTD reference:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

Can be resolved using the following Catalog entry:
<public publicId="-//W3C//DTD XHTML 1.0 Strict//EN" uri="catalog/xhtml1-strict.dtd"/>
or
<systemSuffix systemIdSuffix="html1-strict.dtd" uri="catalog/xhtml1-strict.dtd"/>

The following XInclude element:
<xi:include href="http://openjdk.java.net/xml/disclaimer.xml"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xml/disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>
or
<uriSuffix uriSuffix="disclaimer.xml" uri="file:///pathto/local/disclaimer.xml"/>

The following import element:
<xsd:import namespace="http://openjdk.java.net/xsd/XSDImport_person"
schemaLocation="http://openjdk.java.net/xsd/XSDImport_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="XSDImport_person.xsd" uri="file:///pathto/local/XSDImport_person.xsd"/>
or
<uriSuffix uriSuffix="http://openjdk.java.net/xsd/XSDImport_person" uri="file:///pathto/local/XSDImport_person.xsd"/>

The following include element:
<xsd:include schemaLocation="http://openjdk.java.net/xsd/XSDInclude_person.xsd"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsd/XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>
or
<uriSuffix uriSuffix="XSDInclude_person.xsd" uri="file:///pathto/local/XSDInclude_person.xsd"/>

The following include element:
<xsl:include href="http://openjdk.java.net/xsl/include.xsl"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/include.xsl" uri="file:///pathto/local/include.xsl"/>
or
<uriSuffix uriSuffix="include.xsl" uri="file:///pathto/local/include.xsl"/>

The document in the following element:
<xsl:variable name="dummy" select="document('http://openjdk.java.net/xsl/list.xml')"/>

can be resolved using a URI entry:
<uri name="http://openjdk.java.net/xsl/list.xml" uri="file:///pathto/local/list.xml"/>
or
<uriSuffix uriSuffix="list.xml" uri="file:///pathto/local/list.xml"/>

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

CatalogFeatures.Builder

The Builder class for building the CatalogFeatures object.

static class

CatalogFeatures.Feature

A Feature type as defined in the

Catalog Features table

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

CatalogFeatures.Builder

builder

()

Returns an instance of the builder for creating the CatalogFeatures object.

static

CatalogFeatures

defaults

()

Returns a CatalogFeatures instance with default settings.

String

get

​(

CatalogFeatures.Feature

cf)

Returns the value of the specified feature.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

CatalogFeatures.Builder

The Builder class for building the CatalogFeatures object.

static class

CatalogFeatures.Feature

A Feature type as defined in the

Catalog Features table

.

---

#### Nested Class Summary

The Builder class for building the CatalogFeatures object.

A Feature type as defined in the

Catalog Features table

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

CatalogFeatures.Builder

builder

()

Returns an instance of the builder for creating the CatalogFeatures object.

static

CatalogFeatures

defaults

()

Returns a CatalogFeatures instance with default settings.

String

get

​(

CatalogFeatures.Feature

cf)

Returns the value of the specified feature.

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

Returns an instance of the builder for creating the CatalogFeatures object.

Returns a CatalogFeatures instance with default settings.

Returns the value of the specified feature.

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

- defaults

```java
public static
CatalogFeatures
defaults()
```

Returns a CatalogFeatures instance with default settings.

**Returns:** a default CatalogFeatures instance

- get

```java
public
String
get​(
CatalogFeatures.Feature
cf)
```

Returns the value of the specified feature.

**Parameters:** cf

- the type of the Catalog feature
**Returns:** the value of the feature

- builder

```java
public static
CatalogFeatures.Builder
builder()
```

Returns an instance of the builder for creating the CatalogFeatures object.

**Returns:** an instance of the builder

Method Detail

- defaults

```java
public static
CatalogFeatures
defaults()
```

Returns a CatalogFeatures instance with default settings.

**Returns:** a default CatalogFeatures instance

- get

```java
public
String
get​(
CatalogFeatures.Feature
cf)
```

Returns the value of the specified feature.

**Parameters:** cf

- the type of the Catalog feature
**Returns:** the value of the feature

- builder

```java
public static
CatalogFeatures.Builder
builder()
```

Returns an instance of the builder for creating the CatalogFeatures object.

**Returns:** an instance of the builder

---

#### Method Detail

defaults

```java
public static
CatalogFeatures
defaults()
```

Returns a CatalogFeatures instance with default settings.

**Returns:** a default CatalogFeatures instance

---

#### defaults

public static

CatalogFeatures

defaults()

Returns a CatalogFeatures instance with default settings.

get

```java
public
String
get​(
CatalogFeatures.Feature
cf)
```

Returns the value of the specified feature.

**Parameters:** cf

- the type of the Catalog feature
**Returns:** the value of the feature

---

#### get

public

String

get​(

CatalogFeatures.Feature

cf)

Returns the value of the specified feature.

builder

```java
public static
CatalogFeatures.Builder
builder()
```

Returns an instance of the builder for creating the CatalogFeatures object.

**Returns:** an instance of the builder

---

#### builder

public static

CatalogFeatures.Builder

builder()

Returns an instance of the builder for creating the CatalogFeatures object.

---

