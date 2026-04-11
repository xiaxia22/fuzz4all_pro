# Class XMLConstants

**Source:** `java.xml\javax\xml\XMLConstants.html`

### Class Description

```java
public final class
XMLConstants

extends
Object
```

Utility class to contain basic XML values as constants.

**Since:** 1.5
**See Also:** Extensible Markup Language (XML) 1.1

,

Extensible Markup Language (XML) 1.0 (Second Edition)

,

XML 1.0 Second Edition Specification Errata

,

Namespaces in XML 1.1

,

Namespaces in XML

,

XML Schema Part 1: Structures

---

### Field Details

#### public static final
String
NULL_NS_URI

Namespace URI to use to represent that there is no Namespace.

Defined by the Namespace specification to be "".

**See Also:**
- Namespaces in XML, 5.2 Namespace Defaulting

,

Constant Field Values

---

#### public static final
String
DEFAULT_NS_PREFIX

Prefix to use to represent the default XML Namespace.

Defined by the XML specification to be "".

**See Also:**
- Namespaces in XML, 3. Qualified Names

,

Constant Field Values

---

#### public static final
String
XML_NS_URI

The official XML Namespace name URI.

Defined by the XML specification to be
"

http://www.w3.org/XML/1998/namespace

".

**See Also:**
- Namespaces in XML, 3. Qualified Names

,

Constant Field Values

---

#### public static final
String
XML_NS_PREFIX

The official XML Namespace prefix.

Defined by the XML specification to be "

xml

".

**See Also:**
- Namespaces in XML, 3. Qualified Names

,

Constant Field Values

---

#### public static final
String
XMLNS_ATTRIBUTE_NS_URI

The official XML attribute used for specifying XML Namespace
declarations,

XMLConstants.XMLNS_ATTRIBUTE

, Namespace name URI.

Defined by the XML specification to be
"

http://www.w3.org/2000/xmlns/

".

**See Also:**
- Namespaces in XML, 3. Qualified Names

,

Constant Field Values

---

#### public static final
String
XMLNS_ATTRIBUTE

The official XML attribute used for specifying XML Namespace
declarations.

It is

NOT

valid to use as a
prefix. Defined by the XML specification to be
"

xmlns

".

**See Also:**
- Namespaces in XML, 3. Qualified Names

,

Constant Field Values

---

#### public static final
String
W3C_XML_SCHEMA_NS_URI

W3C XML Schema Namespace URI.

Defined to be "

http://www.w3.org/2001/XMLSchema

".

**See Also:**
- XML Schema Part 1:
Structures, 2.6 Schema-Related Markup in Documents Being Validated

,

Constant Field Values

---

#### public static final
String
W3C_XML_SCHEMA_INSTANCE_NS_URI

W3C XML Schema Instance Namespace URI.

Defined to be "

http://www.w3.org/2001/XMLSchema-instance

".

**See Also:**
- XML Schema Part 1:
Structures, 2.6 Schema-Related Markup in Documents Being Validated

,

Constant Field Values

---

#### public static final
String
W3C_XPATH_DATATYPE_NS_URI

W3C XPath Datatype Namespace URI.

Defined to be "

http://www.w3.org/2003/11/xpath-datatypes

".

**See Also:**
- XQuery 1.0 and XPath 2.0 Data Model

,

Constant Field Values

---

#### public static final
String
XML_DTD_NS_URI

XML Document Type Declaration Namespace URI as an arbitrary value.

Since not formally defined by any existing standard, arbitrarily define to be "

http://www.w3.org/TR/REC-xml

".

**See Also:**
- Constant Field Values

---

#### public static final
String
RELAXNG_NS_URI

RELAX NG Namespace URI.

Defined to be "

http://relaxng.org/ns/structure/1.0

".

**See Also:**
- RELAX NG Specification

,

Constant Field Values

---

#### public static final
String
FEATURE_SECURE_PROCESSING

Feature for secure processing.

- true

instructs the implementation to process XML securely.
This may set limits on XML constructs to avoid conditions such as denial of service attacks.
- false

instructs the implementation to process XML in accordance with the XML specifications
ignoring security issues such as limits on XML constructs to avoid conditions such as denial of service attacks.

**See Also:**
- Constant Field Values

---

#### public static final
String
ACCESS_EXTERNAL_DTD

Property: accessExternalDTD

Restrict access to external DTDs and external Entity References to the protocols specified.
If access is denied due to the restriction of this property, a runtime exception that
is specific to the context is thrown. In the case of

SAXParser

for example,

SAXException

is thrown.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalDTD

.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

**See Also:**
- Constant Field Values

**Since:**
- 1.7

---

#### public static final
String
ACCESS_EXTERNAL_SCHEMA

Property: accessExternalSchema

Restrict access to the protocols specified for external reference set by the
schemaLocation attribute, Import and Include element. If access is denied
due to the restriction of this property, a runtime exception that is specific
to the context is thrown. In the case of

SchemaFactory

for example, org.xml.sax.SAXException is thrown.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalSchema

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

**See Also:**
- Constant Field Values

**Since:**
- 1.7

---

#### public static final
String
ACCESS_EXTERNAL_STYLESHEET

Property: accessExternalStylesheet

Restrict access to the protocols specified for external references set by the
stylesheet processing instruction, Import and Include element, and document function.
If access is denied due to the restriction of this property, a runtime exception
that is specific to the context is thrown. In the case of constructing new

Transformer

for example,

TransformerConfigurationException

will be thrown by the

TransformerFactory

.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalStylesheet

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

**See Also:**
- Constant Field Values

**Since:**
- 1.7

---

#### public static final
String
USE_CATALOG

Feature: useCatalog

Instructs XML processors to use XML Catalogs to resolve entity references.
Catalogs may be set through JAXP factories, system properties, or
jaxp.properties by using the

javax.xml.catalog.files

property
defined in

CatalogFeatures

.
The following code enables Catalog on SAX parser:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true);
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "catalog.xml");
```

Value:

a boolean. If the value is true, and a catalog is set,
the XML parser will resolve external references using

CatalogResolver

. If the value is false,
XML Catalog is ignored even if one is set. The default value is true.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.useCatalog

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
value of the property.

**See Also:**
- Constant Field Values

**Since:**
- 9

---

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Class XMLConstants

java.lang.Object

- javax.xml.XMLConstants

javax.xml.XMLConstants

```java
public final class
XMLConstants

extends
Object
```

Utility class to contain basic XML values as constants.

**Since:** 1.5
**See Also:** Extensible Markup Language (XML) 1.1

,

Extensible Markup Language (XML) 1.0 (Second Edition)

,

XML 1.0 Second Edition Specification Errata

,

Namespaces in XML 1.1

,

Namespaces in XML

,

XML Schema Part 1: Structures

public final class

XMLConstants

extends

Object

Utility class to contain basic XML values as constants.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

ACCESS_EXTERNAL_DTD

Property: accessExternalDTD

static

String

ACCESS_EXTERNAL_SCHEMA

Property: accessExternalSchema

static

String

ACCESS_EXTERNAL_STYLESHEET

Property: accessExternalStylesheet

static

String

DEFAULT_NS_PREFIX

Prefix to use to represent the default XML Namespace.

static

String

FEATURE_SECURE_PROCESSING

Feature for secure processing.

static

String

NULL_NS_URI

Namespace URI to use to represent that there is no Namespace.

static

String

RELAXNG_NS_URI

RELAX NG Namespace URI.

static

String

USE_CATALOG

Feature: useCatalog

static

String

W3C_XML_SCHEMA_INSTANCE_NS_URI

W3C XML Schema Instance Namespace URI.

static

String

W3C_XML_SCHEMA_NS_URI

W3C XML Schema Namespace URI.

static

String

W3C_XPATH_DATATYPE_NS_URI

W3C XPath Datatype Namespace URI.

static

String

XML_DTD_NS_URI

XML Document Type Declaration Namespace URI as an arbitrary value.

static

String

XML_NS_PREFIX

The official XML Namespace prefix.

static

String

XML_NS_URI

The official XML Namespace name URI.

static

String

XMLNS_ATTRIBUTE

The official XML attribute used for specifying XML Namespace
declarations.

static

String

XMLNS_ATTRIBUTE_NS_URI

The official XML attribute used for specifying XML Namespace
declarations,

XMLConstants.XMLNS_ATTRIBUTE

, Namespace name URI.

========== METHOD SUMMARY ===========

- Method Summary

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

ACCESS_EXTERNAL_DTD

Property: accessExternalDTD

static

String

ACCESS_EXTERNAL_SCHEMA

Property: accessExternalSchema

static

String

ACCESS_EXTERNAL_STYLESHEET

Property: accessExternalStylesheet

static

String

DEFAULT_NS_PREFIX

Prefix to use to represent the default XML Namespace.

static

String

FEATURE_SECURE_PROCESSING

Feature for secure processing.

static

String

NULL_NS_URI

Namespace URI to use to represent that there is no Namespace.

static

String

RELAXNG_NS_URI

RELAX NG Namespace URI.

static

String

USE_CATALOG

Feature: useCatalog

static

String

W3C_XML_SCHEMA_INSTANCE_NS_URI

W3C XML Schema Instance Namespace URI.

static

String

W3C_XML_SCHEMA_NS_URI

W3C XML Schema Namespace URI.

static

String

W3C_XPATH_DATATYPE_NS_URI

W3C XPath Datatype Namespace URI.

static

String

XML_DTD_NS_URI

XML Document Type Declaration Namespace URI as an arbitrary value.

static

String

XML_NS_PREFIX

The official XML Namespace prefix.

static

String

XML_NS_URI

The official XML Namespace name URI.

static

String

XMLNS_ATTRIBUTE

The official XML attribute used for specifying XML Namespace
declarations.

static

String

XMLNS_ATTRIBUTE_NS_URI

The official XML attribute used for specifying XML Namespace
declarations,

XMLConstants.XMLNS_ATTRIBUTE

, Namespace name URI.

---

#### Field Summary

Property: accessExternalDTD

Property: accessExternalSchema

Property: accessExternalStylesheet

Prefix to use to represent the default XML Namespace.

Feature for secure processing.

Namespace URI to use to represent that there is no Namespace.

RELAX NG Namespace URI.

Feature: useCatalog

W3C XML Schema Instance Namespace URI.

W3C XML Schema Namespace URI.

W3C XPath Datatype Namespace URI.

XML Document Type Declaration Namespace URI as an arbitrary value.

The official XML Namespace prefix.

The official XML Namespace name URI.

The official XML attribute used for specifying XML Namespace
declarations.

The official XML attribute used for specifying XML Namespace
declarations,

XMLConstants.XMLNS_ATTRIBUTE

, Namespace name URI.

Method Summary

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

============ FIELD DETAIL ===========

- Field Detail

- NULL_NS_URI

```java
public static final
String
NULL_NS_URI
```

Namespace URI to use to represent that there is no Namespace.

Defined by the Namespace specification to be "".

**See Also:** Namespaces in XML, 5.2 Namespace Defaulting

,

Constant Field Values

- DEFAULT_NS_PREFIX

```java
public static final
String
DEFAULT_NS_PREFIX
```

Prefix to use to represent the default XML Namespace.

Defined by the XML specification to be "".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

- XML_NS_URI

```java
public static final
String
XML_NS_URI
```

The official XML Namespace name URI.

Defined by the XML specification to be
"

http://www.w3.org/XML/1998/namespace

".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

- XML_NS_PREFIX

```java
public static final
String
XML_NS_PREFIX
```

The official XML Namespace prefix.

Defined by the XML specification to be "

xml

".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

- XMLNS_ATTRIBUTE_NS_URI

```java
public static final
String
XMLNS_ATTRIBUTE_NS_URI
```

The official XML attribute used for specifying XML Namespace
declarations,

XMLConstants.XMLNS_ATTRIBUTE

, Namespace name URI.

Defined by the XML specification to be
"

http://www.w3.org/2000/xmlns/

".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

- XMLNS_ATTRIBUTE

```java
public static final
String
XMLNS_ATTRIBUTE
```

The official XML attribute used for specifying XML Namespace
declarations.

It is

NOT

valid to use as a
prefix. Defined by the XML specification to be
"

xmlns

".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

- W3C_XML_SCHEMA_NS_URI

```java
public static final
String
W3C_XML_SCHEMA_NS_URI
```

W3C XML Schema Namespace URI.

Defined to be "

http://www.w3.org/2001/XMLSchema

".

**See Also:** XML Schema Part 1:
Structures, 2.6 Schema-Related Markup in Documents Being Validated

,

Constant Field Values

- W3C_XML_SCHEMA_INSTANCE_NS_URI

```java
public static final
String
W3C_XML_SCHEMA_INSTANCE_NS_URI
```

W3C XML Schema Instance Namespace URI.

Defined to be "

http://www.w3.org/2001/XMLSchema-instance

".

**See Also:** XML Schema Part 1:
Structures, 2.6 Schema-Related Markup in Documents Being Validated

,

Constant Field Values

- W3C_XPATH_DATATYPE_NS_URI

```java
public static final
String
W3C_XPATH_DATATYPE_NS_URI
```

W3C XPath Datatype Namespace URI.

Defined to be "

http://www.w3.org/2003/11/xpath-datatypes

".

**See Also:** XQuery 1.0 and XPath 2.0 Data Model

,

Constant Field Values

- XML_DTD_NS_URI

```java
public static final
String
XML_DTD_NS_URI
```

XML Document Type Declaration Namespace URI as an arbitrary value.

Since not formally defined by any existing standard, arbitrarily define to be "

http://www.w3.org/TR/REC-xml

".

**See Also:** Constant Field Values

- RELAXNG_NS_URI

```java
public static final
String
RELAXNG_NS_URI
```

RELAX NG Namespace URI.

Defined to be "

http://relaxng.org/ns/structure/1.0

".

**See Also:** RELAX NG Specification

,

Constant Field Values

- FEATURE_SECURE_PROCESSING

```java
public static final
String
FEATURE_SECURE_PROCESSING
```

Feature for secure processing.

- true

instructs the implementation to process XML securely.
This may set limits on XML constructs to avoid conditions such as denial of service attacks.
- false

instructs the implementation to process XML in accordance with the XML specifications
ignoring security issues such as limits on XML constructs to avoid conditions such as denial of service attacks.

**See Also:** Constant Field Values

- ACCESS_EXTERNAL_DTD

```java
public static final
String
ACCESS_EXTERNAL_DTD
```

Property: accessExternalDTD

Restrict access to external DTDs and external Entity References to the protocols specified.
If access is denied due to the restriction of this property, a runtime exception that
is specific to the context is thrown. In the case of

SAXParser

for example,

SAXException

is thrown.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalDTD

.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

**Since:** 1.7
**See Also:** Constant Field Values

- ACCESS_EXTERNAL_SCHEMA

```java
public static final
String
ACCESS_EXTERNAL_SCHEMA
```

Property: accessExternalSchema

Restrict access to the protocols specified for external reference set by the
schemaLocation attribute, Import and Include element. If access is denied
due to the restriction of this property, a runtime exception that is specific
to the context is thrown. In the case of

SchemaFactory

for example, org.xml.sax.SAXException is thrown.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalSchema

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

**Since:** 1.7
**See Also:** Constant Field Values

- ACCESS_EXTERNAL_STYLESHEET

```java
public static final
String
ACCESS_EXTERNAL_STYLESHEET
```

Property: accessExternalStylesheet

Restrict access to the protocols specified for external references set by the
stylesheet processing instruction, Import and Include element, and document function.
If access is denied due to the restriction of this property, a runtime exception
that is specific to the context is thrown. In the case of constructing new

Transformer

for example,

TransformerConfigurationException

will be thrown by the

TransformerFactory

.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalStylesheet

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

**Since:** 1.7
**See Also:** Constant Field Values

- USE_CATALOG

```java
public static final
String
USE_CATALOG
```

Feature: useCatalog

Instructs XML processors to use XML Catalogs to resolve entity references.
Catalogs may be set through JAXP factories, system properties, or
jaxp.properties by using the

javax.xml.catalog.files

property
defined in

CatalogFeatures

.
The following code enables Catalog on SAX parser:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true);
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "catalog.xml");
```

Value:

a boolean. If the value is true, and a catalog is set,
the XML parser will resolve external references using

CatalogResolver

. If the value is false,
XML Catalog is ignored even if one is set. The default value is true.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.useCatalog

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
value of the property.

**Since:** 9
**See Also:** Constant Field Values

Field Detail

- NULL_NS_URI

```java
public static final
String
NULL_NS_URI
```

Namespace URI to use to represent that there is no Namespace.

Defined by the Namespace specification to be "".

**See Also:** Namespaces in XML, 5.2 Namespace Defaulting

,

Constant Field Values

- DEFAULT_NS_PREFIX

```java
public static final
String
DEFAULT_NS_PREFIX
```

Prefix to use to represent the default XML Namespace.

Defined by the XML specification to be "".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

- XML_NS_URI

```java
public static final
String
XML_NS_URI
```

The official XML Namespace name URI.

Defined by the XML specification to be
"

http://www.w3.org/XML/1998/namespace

".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

- XML_NS_PREFIX

```java
public static final
String
XML_NS_PREFIX
```

The official XML Namespace prefix.

Defined by the XML specification to be "

xml

".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

- XMLNS_ATTRIBUTE_NS_URI

```java
public static final
String
XMLNS_ATTRIBUTE_NS_URI
```

The official XML attribute used for specifying XML Namespace
declarations,

XMLConstants.XMLNS_ATTRIBUTE

, Namespace name URI.

Defined by the XML specification to be
"

http://www.w3.org/2000/xmlns/

".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

- XMLNS_ATTRIBUTE

```java
public static final
String
XMLNS_ATTRIBUTE
```

The official XML attribute used for specifying XML Namespace
declarations.

It is

NOT

valid to use as a
prefix. Defined by the XML specification to be
"

xmlns

".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

- W3C_XML_SCHEMA_NS_URI

```java
public static final
String
W3C_XML_SCHEMA_NS_URI
```

W3C XML Schema Namespace URI.

Defined to be "

http://www.w3.org/2001/XMLSchema

".

**See Also:** XML Schema Part 1:
Structures, 2.6 Schema-Related Markup in Documents Being Validated

,

Constant Field Values

- W3C_XML_SCHEMA_INSTANCE_NS_URI

```java
public static final
String
W3C_XML_SCHEMA_INSTANCE_NS_URI
```

W3C XML Schema Instance Namespace URI.

Defined to be "

http://www.w3.org/2001/XMLSchema-instance

".

**See Also:** XML Schema Part 1:
Structures, 2.6 Schema-Related Markup in Documents Being Validated

,

Constant Field Values

- W3C_XPATH_DATATYPE_NS_URI

```java
public static final
String
W3C_XPATH_DATATYPE_NS_URI
```

W3C XPath Datatype Namespace URI.

Defined to be "

http://www.w3.org/2003/11/xpath-datatypes

".

**See Also:** XQuery 1.0 and XPath 2.0 Data Model

,

Constant Field Values

- XML_DTD_NS_URI

```java
public static final
String
XML_DTD_NS_URI
```

XML Document Type Declaration Namespace URI as an arbitrary value.

Since not formally defined by any existing standard, arbitrarily define to be "

http://www.w3.org/TR/REC-xml

".

**See Also:** Constant Field Values

- RELAXNG_NS_URI

```java
public static final
String
RELAXNG_NS_URI
```

RELAX NG Namespace URI.

Defined to be "

http://relaxng.org/ns/structure/1.0

".

**See Also:** RELAX NG Specification

,

Constant Field Values

- FEATURE_SECURE_PROCESSING

```java
public static final
String
FEATURE_SECURE_PROCESSING
```

Feature for secure processing.

- true

instructs the implementation to process XML securely.
This may set limits on XML constructs to avoid conditions such as denial of service attacks.
- false

instructs the implementation to process XML in accordance with the XML specifications
ignoring security issues such as limits on XML constructs to avoid conditions such as denial of service attacks.

**See Also:** Constant Field Values

- ACCESS_EXTERNAL_DTD

```java
public static final
String
ACCESS_EXTERNAL_DTD
```

Property: accessExternalDTD

Restrict access to external DTDs and external Entity References to the protocols specified.
If access is denied due to the restriction of this property, a runtime exception that
is specific to the context is thrown. In the case of

SAXParser

for example,

SAXException

is thrown.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalDTD

.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

**Since:** 1.7
**See Also:** Constant Field Values

- ACCESS_EXTERNAL_SCHEMA

```java
public static final
String
ACCESS_EXTERNAL_SCHEMA
```

Property: accessExternalSchema

Restrict access to the protocols specified for external reference set by the
schemaLocation attribute, Import and Include element. If access is denied
due to the restriction of this property, a runtime exception that is specific
to the context is thrown. In the case of

SchemaFactory

for example, org.xml.sax.SAXException is thrown.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalSchema

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

**Since:** 1.7
**See Also:** Constant Field Values

- ACCESS_EXTERNAL_STYLESHEET

```java
public static final
String
ACCESS_EXTERNAL_STYLESHEET
```

Property: accessExternalStylesheet

Restrict access to the protocols specified for external references set by the
stylesheet processing instruction, Import and Include element, and document function.
If access is denied due to the restriction of this property, a runtime exception
that is specific to the context is thrown. In the case of constructing new

Transformer

for example,

TransformerConfigurationException

will be thrown by the

TransformerFactory

.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalStylesheet

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

**Since:** 1.7
**See Also:** Constant Field Values

- USE_CATALOG

```java
public static final
String
USE_CATALOG
```

Feature: useCatalog

Instructs XML processors to use XML Catalogs to resolve entity references.
Catalogs may be set through JAXP factories, system properties, or
jaxp.properties by using the

javax.xml.catalog.files

property
defined in

CatalogFeatures

.
The following code enables Catalog on SAX parser:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true);
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "catalog.xml");
```

Value:

a boolean. If the value is true, and a catalog is set,
the XML parser will resolve external references using

CatalogResolver

. If the value is false,
XML Catalog is ignored even if one is set. The default value is true.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.useCatalog

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
value of the property.

**Since:** 9
**See Also:** Constant Field Values

---

#### Field Detail

NULL_NS_URI

```java
public static final
String
NULL_NS_URI
```

Namespace URI to use to represent that there is no Namespace.

Defined by the Namespace specification to be "".

**See Also:** Namespaces in XML, 5.2 Namespace Defaulting

,

Constant Field Values

---

#### NULL_NS_URI

public static final

String

NULL_NS_URI

Namespace URI to use to represent that there is no Namespace.

Defined by the Namespace specification to be "".

Defined by the Namespace specification to be "".

DEFAULT_NS_PREFIX

```java
public static final
String
DEFAULT_NS_PREFIX
```

Prefix to use to represent the default XML Namespace.

Defined by the XML specification to be "".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

---

#### DEFAULT_NS_PREFIX

public static final

String

DEFAULT_NS_PREFIX

Prefix to use to represent the default XML Namespace.

Defined by the XML specification to be "".

Defined by the XML specification to be "".

XML_NS_URI

```java
public static final
String
XML_NS_URI
```

The official XML Namespace name URI.

Defined by the XML specification to be
"

http://www.w3.org/XML/1998/namespace

".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

---

#### XML_NS_URI

public static final

String

XML_NS_URI

The official XML Namespace name URI.

Defined by the XML specification to be
"

http://www.w3.org/XML/1998/namespace

".

Defined by the XML specification to be
"

http://www.w3.org/XML/1998/namespace

".

XML_NS_PREFIX

```java
public static final
String
XML_NS_PREFIX
```

The official XML Namespace prefix.

Defined by the XML specification to be "

xml

".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

---

#### XML_NS_PREFIX

public static final

String

XML_NS_PREFIX

The official XML Namespace prefix.

Defined by the XML specification to be "

xml

".

Defined by the XML specification to be "

xml

".

XMLNS_ATTRIBUTE_NS_URI

```java
public static final
String
XMLNS_ATTRIBUTE_NS_URI
```

The official XML attribute used for specifying XML Namespace
declarations,

XMLConstants.XMLNS_ATTRIBUTE

, Namespace name URI.

Defined by the XML specification to be
"

http://www.w3.org/2000/xmlns/

".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

---

#### XMLNS_ATTRIBUTE_NS_URI

public static final

String

XMLNS_ATTRIBUTE_NS_URI

The official XML attribute used for specifying XML Namespace
declarations,

XMLConstants.XMLNS_ATTRIBUTE

, Namespace name URI.

Defined by the XML specification to be
"

http://www.w3.org/2000/xmlns/

".

Defined by the XML specification to be
"

http://www.w3.org/2000/xmlns/

".

XMLNS_ATTRIBUTE

```java
public static final
String
XMLNS_ATTRIBUTE
```

The official XML attribute used for specifying XML Namespace
declarations.

It is

NOT

valid to use as a
prefix. Defined by the XML specification to be
"

xmlns

".

**See Also:** Namespaces in XML, 3. Qualified Names

,

Constant Field Values

---

#### XMLNS_ATTRIBUTE

public static final

String

XMLNS_ATTRIBUTE

The official XML attribute used for specifying XML Namespace
declarations.

It is

NOT

valid to use as a
prefix. Defined by the XML specification to be
"

xmlns

".

It is

NOT

valid to use as a
prefix. Defined by the XML specification to be
"

xmlns

".

W3C_XML_SCHEMA_NS_URI

```java
public static final
String
W3C_XML_SCHEMA_NS_URI
```

W3C XML Schema Namespace URI.

Defined to be "

http://www.w3.org/2001/XMLSchema

".

**See Also:** XML Schema Part 1:
Structures, 2.6 Schema-Related Markup in Documents Being Validated

,

Constant Field Values

---

#### W3C_XML_SCHEMA_NS_URI

public static final

String

W3C_XML_SCHEMA_NS_URI

W3C XML Schema Namespace URI.

Defined to be "

http://www.w3.org/2001/XMLSchema

".

Defined to be "

http://www.w3.org/2001/XMLSchema

".

W3C_XML_SCHEMA_INSTANCE_NS_URI

```java
public static final
String
W3C_XML_SCHEMA_INSTANCE_NS_URI
```

W3C XML Schema Instance Namespace URI.

Defined to be "

http://www.w3.org/2001/XMLSchema-instance

".

**See Also:** XML Schema Part 1:
Structures, 2.6 Schema-Related Markup in Documents Being Validated

,

Constant Field Values

---

#### W3C_XML_SCHEMA_INSTANCE_NS_URI

public static final

String

W3C_XML_SCHEMA_INSTANCE_NS_URI

W3C XML Schema Instance Namespace URI.

Defined to be "

http://www.w3.org/2001/XMLSchema-instance

".

Defined to be "

http://www.w3.org/2001/XMLSchema-instance

".

W3C_XPATH_DATATYPE_NS_URI

```java
public static final
String
W3C_XPATH_DATATYPE_NS_URI
```

W3C XPath Datatype Namespace URI.

Defined to be "

http://www.w3.org/2003/11/xpath-datatypes

".

**See Also:** XQuery 1.0 and XPath 2.0 Data Model

,

Constant Field Values

---

#### W3C_XPATH_DATATYPE_NS_URI

public static final

String

W3C_XPATH_DATATYPE_NS_URI

W3C XPath Datatype Namespace URI.

Defined to be "

http://www.w3.org/2003/11/xpath-datatypes

".

Defined to be "

http://www.w3.org/2003/11/xpath-datatypes

".

XML_DTD_NS_URI

```java
public static final
String
XML_DTD_NS_URI
```

XML Document Type Declaration Namespace URI as an arbitrary value.

Since not formally defined by any existing standard, arbitrarily define to be "

http://www.w3.org/TR/REC-xml

".

**See Also:** Constant Field Values

---

#### XML_DTD_NS_URI

public static final

String

XML_DTD_NS_URI

XML Document Type Declaration Namespace URI as an arbitrary value.

Since not formally defined by any existing standard, arbitrarily define to be "

http://www.w3.org/TR/REC-xml

".

Since not formally defined by any existing standard, arbitrarily define to be "

http://www.w3.org/TR/REC-xml

".

RELAXNG_NS_URI

```java
public static final
String
RELAXNG_NS_URI
```

RELAX NG Namespace URI.

Defined to be "

http://relaxng.org/ns/structure/1.0

".

**See Also:** RELAX NG Specification

,

Constant Field Values

---

#### RELAXNG_NS_URI

public static final

String

RELAXNG_NS_URI

RELAX NG Namespace URI.

Defined to be "

http://relaxng.org/ns/structure/1.0

".

Defined to be "

http://relaxng.org/ns/structure/1.0

".

FEATURE_SECURE_PROCESSING

```java
public static final
String
FEATURE_SECURE_PROCESSING
```

Feature for secure processing.

- true

instructs the implementation to process XML securely.
This may set limits on XML constructs to avoid conditions such as denial of service attacks.
- false

instructs the implementation to process XML in accordance with the XML specifications
ignoring security issues such as limits on XML constructs to avoid conditions such as denial of service attacks.

**See Also:** Constant Field Values

---

#### FEATURE_SECURE_PROCESSING

public static final

String

FEATURE_SECURE_PROCESSING

Feature for secure processing.

- true

instructs the implementation to process XML securely.
This may set limits on XML constructs to avoid conditions such as denial of service attacks.
- false

instructs the implementation to process XML in accordance with the XML specifications
ignoring security issues such as limits on XML constructs to avoid conditions such as denial of service attacks.

true

instructs the implementation to process XML securely.
This may set limits on XML constructs to avoid conditions such as denial of service attacks.

false

instructs the implementation to process XML in accordance with the XML specifications
ignoring security issues such as limits on XML constructs to avoid conditions such as denial of service attacks.

ACCESS_EXTERNAL_DTD

```java
public static final
String
ACCESS_EXTERNAL_DTD
```

Property: accessExternalDTD

Restrict access to external DTDs and external Entity References to the protocols specified.
If access is denied due to the restriction of this property, a runtime exception that
is specific to the context is thrown. In the case of

SAXParser

for example,

SAXException

is thrown.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalDTD

.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

**Since:** 1.7
**See Also:** Constant Field Values

---

#### ACCESS_EXTERNAL_DTD

public static final

String

ACCESS_EXTERNAL_DTD

Property: accessExternalDTD

Restrict access to external DTDs and external Entity References to the protocols specified.
If access is denied due to the restriction of this property, a runtime exception that
is specific to the context is thrown. In the case of

SAXParser

for example,

SAXException

is thrown.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalDTD

.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

Restrict access to external DTDs and external Entity References to the protocols specified.
If access is denied due to the restriction of this property, a runtime exception that
is specific to the context is thrown. In the case of

SAXParser

for example,

SAXException

is thrown.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalDTD

.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalDTD

.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalDTD

.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

an empty string to deny all access to external references;

a specific protocol, such as file, to give permission to only the protocol;

the keyword "all" to grant permission to all protocols.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalDTD

.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalDTD

.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

ACCESS_EXTERNAL_SCHEMA

```java
public static final
String
ACCESS_EXTERNAL_SCHEMA
```

Property: accessExternalSchema

Restrict access to the protocols specified for external reference set by the
schemaLocation attribute, Import and Include element. If access is denied
due to the restriction of this property, a runtime exception that is specific
to the context is thrown. In the case of

SchemaFactory

for example, org.xml.sax.SAXException is thrown.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalSchema

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

**Since:** 1.7
**See Also:** Constant Field Values

---

#### ACCESS_EXTERNAL_SCHEMA

public static final

String

ACCESS_EXTERNAL_SCHEMA

Property: accessExternalSchema

Restrict access to the protocols specified for external reference set by the
schemaLocation attribute, Import and Include element. If access is denied
due to the restriction of this property, a runtime exception that is specific
to the context is thrown. In the case of

SchemaFactory

for example, org.xml.sax.SAXException is thrown.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalSchema

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

Property: accessExternalSchema

Restrict access to the protocols specified for external reference set by the
schemaLocation attribute, Import and Include element. If access is denied
due to the restriction of this property, a runtime exception that is specific
to the context is thrown. In the case of

SchemaFactory

for example, org.xml.sax.SAXException is thrown.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalSchema

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalSchema

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalSchema

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

an empty string to deny all access to external references;

a specific protocol, such as file, to give permission to only the protocol;

the keyword "all" to grant permission to all protocols.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalSchema

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalSchema

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

ACCESS_EXTERNAL_STYLESHEET

```java
public static final
String
ACCESS_EXTERNAL_STYLESHEET
```

Property: accessExternalStylesheet

Restrict access to the protocols specified for external references set by the
stylesheet processing instruction, Import and Include element, and document function.
If access is denied due to the restriction of this property, a runtime exception
that is specific to the context is thrown. In the case of constructing new

Transformer

for example,

TransformerConfigurationException

will be thrown by the

TransformerFactory

.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalStylesheet

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

**Since:** 1.7
**See Also:** Constant Field Values

---

#### ACCESS_EXTERNAL_STYLESHEET

public static final

String

ACCESS_EXTERNAL_STYLESHEET

Property: accessExternalStylesheet

Restrict access to the protocols specified for external references set by the
stylesheet processing instruction, Import and Include element, and document function.
If access is denied due to the restriction of this property, a runtime exception
that is specific to the context is thrown. In the case of constructing new

Transformer

for example,

TransformerConfigurationException

will be thrown by the

TransformerFactory

.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalStylesheet

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

Restrict access to the protocols specified for external references set by the
stylesheet processing instruction, Import and Include element, and document function.
If access is denied due to the restriction of this property, a runtime exception
that is specific to the context is thrown. In the case of constructing new

Transformer

for example,

TransformerConfigurationException

will be thrown by the

TransformerFactory

.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalStylesheet

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

Value:

a list of protocols separated by comma. A protocol is the scheme portion of a

URI

, or in the case of the JAR protocol, "jar" plus the scheme portion
separated by colon.
A scheme is defined as:

scheme = alpha *( alpha | digit | "+" | "-" | "." )

where alpha = a-z and A-Z.

And the JAR protocol:

jar[:scheme]

Protocols including the keyword "jar" are case-insensitive. Any whitespaces as defined by

Character.isSpaceChar(char)

in the value will be ignored.
Examples of protocols are file, http, jar:file.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalStylesheet

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

Default value:

The default value is implementation specific and therefore not specified.
The following options are provided for consideration:

- an empty string to deny all access to external references;
- a specific protocol, such as file, to give permission to only the protocol;
- the keyword "all" to grant permission to all protocols.

When FEATURE_SECURE_PROCESSING is enabled, it is recommended that implementations
restrict external connections by default, though this may cause problems for applications
that process XML/XSD/XSL with external references.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalStylesheet

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

an empty string to deny all access to external references;

a specific protocol, such as file, to give permission to only the protocol;

the keyword "all" to grant permission to all protocols.

Granting all access:

the keyword "all" grants permission to all protocols.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalStylesheet

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.accessExternalStylesheet

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
of the property.

USE_CATALOG

```java
public static final
String
USE_CATALOG
```

Feature: useCatalog

Instructs XML processors to use XML Catalogs to resolve entity references.
Catalogs may be set through JAXP factories, system properties, or
jaxp.properties by using the

javax.xml.catalog.files

property
defined in

CatalogFeatures

.
The following code enables Catalog on SAX parser:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true);
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "catalog.xml");
```

Value:

a boolean. If the value is true, and a catalog is set,
the XML parser will resolve external references using

CatalogResolver

. If the value is false,
XML Catalog is ignored even if one is set. The default value is true.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.useCatalog

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
value of the property.

**Since:** 9
**See Also:** Constant Field Values

---

#### USE_CATALOG

public static final

String

USE_CATALOG

Feature: useCatalog

Instructs XML processors to use XML Catalogs to resolve entity references.
Catalogs may be set through JAXP factories, system properties, or
jaxp.properties by using the

javax.xml.catalog.files

property
defined in

CatalogFeatures

.
The following code enables Catalog on SAX parser:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true);
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "catalog.xml");
```

Value:

a boolean. If the value is true, and a catalog is set,
the XML parser will resolve external references using

CatalogResolver

. If the value is false,
XML Catalog is ignored even if one is set. The default value is true.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.useCatalog

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
value of the property.

Instructs XML processors to use XML Catalogs to resolve entity references.
Catalogs may be set through JAXP factories, system properties, or
jaxp.properties by using the

javax.xml.catalog.files

property
defined in

CatalogFeatures

.
The following code enables Catalog on SAX parser:

```java
SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true);
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "catalog.xml");
```

Value:

a boolean. If the value is true, and a catalog is set,
the XML parser will resolve external references using

CatalogResolver

. If the value is false,
XML Catalog is ignored even if one is set. The default value is true.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.useCatalog

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
value of the property.

SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.USE_CATALOG, true);
SAXParser parser = spf.newSAXParser();
parser.setProperty(CatalogFeatures.Feature.FILES.getPropertyName(), "catalog.xml");

Value:

a boolean. If the value is true, and a catalog is set,
the XML parser will resolve external references using

CatalogResolver

. If the value is false,
XML Catalog is ignored even if one is set. The default value is true.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.useCatalog

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
value of the property.

System Property:

The value of this property can be set or overridden by
system property

javax.xml.useCatalog

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
value of the property.

jaxp.properties:

This configuration file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. If the file exists and the system
property is specified, its value will be used to override the default
value of the property.

---

