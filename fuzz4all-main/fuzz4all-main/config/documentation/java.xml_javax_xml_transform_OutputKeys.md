# Class OutputKeys

**Source:** `java.xml\javax\xml\transform\OutputKeys.html`

### Class Description

```java
public class
OutputKeys

extends
Object
```

Provides string constants that can be used to set
output properties for a Transformer, or to retrieve
output properties from a Transformer or Templates object.

All the fields in this class are read-only.

**Since:** 1.4
**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

---

### Field Details

#### public static final
String
METHOD

method = "xml" | "html" | "text" |

expanded name

.

The value of the method property identifies the overall method that
should be used for outputting the result tree. Other non-namespaced
values may be used, such as "xhtml", but, if accepted, the handling
of such values is implementation defined. If any of the method values
are not accepted and are not namespace qualified,
then

Transformer.setOutputProperty(java.lang.String, java.lang.String)

or

Transformer.setOutputProperties(java.util.Properties)

will
throw a

IllegalArgumentException

.

**See Also:**
- section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### public static final
String
VERSION

version =

nmtoken

.

version

specifies the version of the output
method.

When the output method is "xml", the version value specifies the
version of XML to be used for outputting the result tree. The default
value for the xml output method is 1.0. When the output method is
"html", the version value indicates the version of the HTML.
The default value for the xml output method is 4.0, which specifies
that the result should be output as HTML conforming to the HTML 4.0
Recommendation [HTML]. If the output method is "text", the version
property is ignored.

**See Also:**
- section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### public static final
String
ENCODING

encoding =

string

.

encoding

specifies the preferred character
encoding that the Transformer should use to encode sequences of
characters as sequences of bytes. The value of the encoding property should be
treated case-insensitively. The value must only contain characters in
the range #x21 to #x7E (i.e., printable ASCII characters). The value
should either be a

charset

registered with the Internet
Assigned Numbers Authority

[IANA]

,

[RFC2278]

or start with

X-

.

**See Also:**
- section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### public static final
String
OMIT_XML_DECLARATION

omit-xml-declaration = "yes" | "no".

omit-xml-declaration

specifies whether the XSLT
processor should output an XML declaration; the value must be

yes

or

no

.

**See Also:**
- section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### public static final
String
STANDALONE

standalone = "yes" | "no".

standalone

specifies whether the Transformer
should output a standalone document declaration; the value must be

yes

or

no

.

**See Also:**
- section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### public static final
String
DOCTYPE_PUBLIC

doctype-public =

string

.

See the documentation for the

DOCTYPE_SYSTEM

property
for a description of what the value of the key should be.

**See Also:**
- section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### public static final
String
DOCTYPE_SYSTEM

doctype-system =

string

.

doctype-system

specifies the system identifier
to be used in the document type declaration.

If the doctype-system property is specified, the xml output method
should output a document type declaration immediately before the first
element. The name following <!DOCTYPE should be the name of the first
element. If doctype-public property is also specified, then the xml
output method should output PUBLIC followed by the public identifier
and then the system identifier; otherwise, it should output SYSTEM
followed by the system identifier. The internal subset should be empty.
The value of the doctype-public property should be ignored unless the doctype-system
property is specified.

If the doctype-public or doctype-system properties are specified,
then the html output method should output a document type declaration
immediately before the first element. The name following <!DOCTYPE
should be HTML or html. If the doctype-public property is specified,
then the output method should output PUBLIC followed by the specified
public identifier; if the doctype-system property is also specified,
it should also output the specified system identifier following the
public identifier. If the doctype-system property is specified but
the doctype-public property is not specified, then the output method
should output SYSTEM followed by the specified system identifier.

doctype-system

specifies the system identifier
to be used in the document type declaration.

**See Also:**
- section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### public static final
String
CDATA_SECTION_ELEMENTS

cdata-section-elements =

expanded names

.

cdata-section-elements

specifies a whitespace delimited
list of the names of elements whose text node children should be output
using CDATA sections. Note that these names must use the format
described in the section Qualfied Name Representation in

javax.xml.transform

.

**See Also:**
- section 16 of the XSL Transformations (XSLT) W3C Recommendation.

,

Constant Field Values

---

#### public static final
String
INDENT

indent = "yes" | "no".

indent

specifies whether the Transformer may
add additional whitespace when outputting the result tree; the value
must be

yes

or

no

.

**See Also:**
- section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### public static final
String
MEDIA_TYPE

media-type =

string

.

media-type

specifies the media type (MIME
content type) of the data that results from outputting the result
tree. The

charset

parameter should not be specified
explicitly; instead, when the top-level media type is

text

, a

charset

parameter should be added
according to the character encoding actually used by the output
method.

**See Also:**
- s
ection 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Class OutputKeys

java.lang.Object

- javax.xml.transform.OutputKeys

javax.xml.transform.OutputKeys

```java
public class
OutputKeys

extends
Object
```

Provides string constants that can be used to set
output properties for a Transformer, or to retrieve
output properties from a Transformer or Templates object.

All the fields in this class are read-only.

**Since:** 1.4
**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

public class

OutputKeys

extends

Object

Provides string constants that can be used to set
output properties for a Transformer, or to retrieve
output properties from a Transformer or Templates object.

All the fields in this class are read-only.

All the fields in this class are read-only.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

CDATA_SECTION_ELEMENTS

cdata-section-elements =

expanded names

.

static

String

DOCTYPE_PUBLIC

doctype-public =

string

.

static

String

DOCTYPE_SYSTEM

doctype-system =

string

.

static

String

ENCODING

encoding =

string

.

static

String

INDENT

indent = "yes" | "no".

static

String

MEDIA_TYPE

media-type =

string

.

static

String

METHOD

method = "xml" | "html" | "text" |

expanded name

.

static

String

OMIT_XML_DECLARATION

omit-xml-declaration = "yes" | "no".

static

String

STANDALONE

standalone = "yes" | "no".

static

String

VERSION

version =

nmtoken

.

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

CDATA_SECTION_ELEMENTS

cdata-section-elements =

expanded names

.

static

String

DOCTYPE_PUBLIC

doctype-public =

string

.

static

String

DOCTYPE_SYSTEM

doctype-system =

string

.

static

String

ENCODING

encoding =

string

.

static

String

INDENT

indent = "yes" | "no".

static

String

MEDIA_TYPE

media-type =

string

.

static

String

METHOD

method = "xml" | "html" | "text" |

expanded name

.

static

String

OMIT_XML_DECLARATION

omit-xml-declaration = "yes" | "no".

static

String

STANDALONE

standalone = "yes" | "no".

static

String

VERSION

version =

nmtoken

.

---

#### Field Summary

cdata-section-elements =

expanded names

.

doctype-public =

string

.

doctype-system =

string

.

encoding =

string

.

indent = "yes" | "no".

media-type =

string

.

method = "xml" | "html" | "text" |

expanded name

.

omit-xml-declaration = "yes" | "no".

standalone = "yes" | "no".

version =

nmtoken

.

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

- METHOD

```java
public static final
String
METHOD
```

method = "xml" | "html" | "text" |

expanded name

.

The value of the method property identifies the overall method that
should be used for outputting the result tree. Other non-namespaced
values may be used, such as "xhtml", but, if accepted, the handling
of such values is implementation defined. If any of the method values
are not accepted and are not namespace qualified,
then

Transformer.setOutputProperty(java.lang.String, java.lang.String)

or

Transformer.setOutputProperties(java.util.Properties)

will
throw a

IllegalArgumentException

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- VERSION

```java
public static final
String
VERSION
```

version =

nmtoken

.

version

specifies the version of the output
method.

When the output method is "xml", the version value specifies the
version of XML to be used for outputting the result tree. The default
value for the xml output method is 1.0. When the output method is
"html", the version value indicates the version of the HTML.
The default value for the xml output method is 4.0, which specifies
that the result should be output as HTML conforming to the HTML 4.0
Recommendation [HTML]. If the output method is "text", the version
property is ignored.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- ENCODING

```java
public static final
String
ENCODING
```

encoding =

string

.

encoding

specifies the preferred character
encoding that the Transformer should use to encode sequences of
characters as sequences of bytes. The value of the encoding property should be
treated case-insensitively. The value must only contain characters in
the range #x21 to #x7E (i.e., printable ASCII characters). The value
should either be a

charset

registered with the Internet
Assigned Numbers Authority

[IANA]

,

[RFC2278]

or start with

X-

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- OMIT_XML_DECLARATION

```java
public static final
String
OMIT_XML_DECLARATION
```

omit-xml-declaration = "yes" | "no".

omit-xml-declaration

specifies whether the XSLT
processor should output an XML declaration; the value must be

yes

or

no

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- STANDALONE

```java
public static final
String
STANDALONE
```

standalone = "yes" | "no".

standalone

specifies whether the Transformer
should output a standalone document declaration; the value must be

yes

or

no

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- DOCTYPE_PUBLIC

```java
public static final
String
DOCTYPE_PUBLIC
```

doctype-public =

string

.

See the documentation for the

DOCTYPE_SYSTEM

property
for a description of what the value of the key should be.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- DOCTYPE_SYSTEM

```java
public static final
String
DOCTYPE_SYSTEM
```

doctype-system =

string

.

doctype-system

specifies the system identifier
to be used in the document type declaration.

If the doctype-system property is specified, the xml output method
should output a document type declaration immediately before the first
element. The name following <!DOCTYPE should be the name of the first
element. If doctype-public property is also specified, then the xml
output method should output PUBLIC followed by the public identifier
and then the system identifier; otherwise, it should output SYSTEM
followed by the system identifier. The internal subset should be empty.
The value of the doctype-public property should be ignored unless the doctype-system
property is specified.

If the doctype-public or doctype-system properties are specified,
then the html output method should output a document type declaration
immediately before the first element. The name following <!DOCTYPE
should be HTML or html. If the doctype-public property is specified,
then the output method should output PUBLIC followed by the specified
public identifier; if the doctype-system property is also specified,
it should also output the specified system identifier following the
public identifier. If the doctype-system property is specified but
the doctype-public property is not specified, then the output method
should output SYSTEM followed by the specified system identifier.

doctype-system

specifies the system identifier
to be used in the document type declaration.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- CDATA_SECTION_ELEMENTS

```java
public static final
String
CDATA_SECTION_ELEMENTS
```

cdata-section-elements =

expanded names

.

cdata-section-elements

specifies a whitespace delimited
list of the names of elements whose text node children should be output
using CDATA sections. Note that these names must use the format
described in the section Qualfied Name Representation in

javax.xml.transform

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation.

,

Constant Field Values

- INDENT

```java
public static final
String
INDENT
```

indent = "yes" | "no".

indent

specifies whether the Transformer may
add additional whitespace when outputting the result tree; the value
must be

yes

or

no

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- MEDIA_TYPE

```java
public static final
String
MEDIA_TYPE
```

media-type =

string

.

media-type

specifies the media type (MIME
content type) of the data that results from outputting the result
tree. The

charset

parameter should not be specified
explicitly; instead, when the top-level media type is

text

, a

charset

parameter should be added
according to the character encoding actually used by the output
method.

**See Also:** s
ection 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

Field Detail

- METHOD

```java
public static final
String
METHOD
```

method = "xml" | "html" | "text" |

expanded name

.

The value of the method property identifies the overall method that
should be used for outputting the result tree. Other non-namespaced
values may be used, such as "xhtml", but, if accepted, the handling
of such values is implementation defined. If any of the method values
are not accepted and are not namespace qualified,
then

Transformer.setOutputProperty(java.lang.String, java.lang.String)

or

Transformer.setOutputProperties(java.util.Properties)

will
throw a

IllegalArgumentException

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- VERSION

```java
public static final
String
VERSION
```

version =

nmtoken

.

version

specifies the version of the output
method.

When the output method is "xml", the version value specifies the
version of XML to be used for outputting the result tree. The default
value for the xml output method is 1.0. When the output method is
"html", the version value indicates the version of the HTML.
The default value for the xml output method is 4.0, which specifies
that the result should be output as HTML conforming to the HTML 4.0
Recommendation [HTML]. If the output method is "text", the version
property is ignored.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- ENCODING

```java
public static final
String
ENCODING
```

encoding =

string

.

encoding

specifies the preferred character
encoding that the Transformer should use to encode sequences of
characters as sequences of bytes. The value of the encoding property should be
treated case-insensitively. The value must only contain characters in
the range #x21 to #x7E (i.e., printable ASCII characters). The value
should either be a

charset

registered with the Internet
Assigned Numbers Authority

[IANA]

,

[RFC2278]

or start with

X-

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- OMIT_XML_DECLARATION

```java
public static final
String
OMIT_XML_DECLARATION
```

omit-xml-declaration = "yes" | "no".

omit-xml-declaration

specifies whether the XSLT
processor should output an XML declaration; the value must be

yes

or

no

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- STANDALONE

```java
public static final
String
STANDALONE
```

standalone = "yes" | "no".

standalone

specifies whether the Transformer
should output a standalone document declaration; the value must be

yes

or

no

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- DOCTYPE_PUBLIC

```java
public static final
String
DOCTYPE_PUBLIC
```

doctype-public =

string

.

See the documentation for the

DOCTYPE_SYSTEM

property
for a description of what the value of the key should be.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- DOCTYPE_SYSTEM

```java
public static final
String
DOCTYPE_SYSTEM
```

doctype-system =

string

.

doctype-system

specifies the system identifier
to be used in the document type declaration.

If the doctype-system property is specified, the xml output method
should output a document type declaration immediately before the first
element. The name following <!DOCTYPE should be the name of the first
element. If doctype-public property is also specified, then the xml
output method should output PUBLIC followed by the public identifier
and then the system identifier; otherwise, it should output SYSTEM
followed by the system identifier. The internal subset should be empty.
The value of the doctype-public property should be ignored unless the doctype-system
property is specified.

If the doctype-public or doctype-system properties are specified,
then the html output method should output a document type declaration
immediately before the first element. The name following <!DOCTYPE
should be HTML or html. If the doctype-public property is specified,
then the output method should output PUBLIC followed by the specified
public identifier; if the doctype-system property is also specified,
it should also output the specified system identifier following the
public identifier. If the doctype-system property is specified but
the doctype-public property is not specified, then the output method
should output SYSTEM followed by the specified system identifier.

doctype-system

specifies the system identifier
to be used in the document type declaration.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- CDATA_SECTION_ELEMENTS

```java
public static final
String
CDATA_SECTION_ELEMENTS
```

cdata-section-elements =

expanded names

.

cdata-section-elements

specifies a whitespace delimited
list of the names of elements whose text node children should be output
using CDATA sections. Note that these names must use the format
described in the section Qualfied Name Representation in

javax.xml.transform

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation.

,

Constant Field Values

- INDENT

```java
public static final
String
INDENT
```

indent = "yes" | "no".

indent

specifies whether the Transformer may
add additional whitespace when outputting the result tree; the value
must be

yes

or

no

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

- MEDIA_TYPE

```java
public static final
String
MEDIA_TYPE
```

media-type =

string

.

media-type

specifies the media type (MIME
content type) of the data that results from outputting the result
tree. The

charset

parameter should not be specified
explicitly; instead, when the top-level media type is

text

, a

charset

parameter should be added
according to the character encoding actually used by the output
method.

**See Also:** s
ection 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### Field Detail

METHOD

```java
public static final
String
METHOD
```

method = "xml" | "html" | "text" |

expanded name

.

The value of the method property identifies the overall method that
should be used for outputting the result tree. Other non-namespaced
values may be used, such as "xhtml", but, if accepted, the handling
of such values is implementation defined. If any of the method values
are not accepted and are not namespace qualified,
then

Transformer.setOutputProperty(java.lang.String, java.lang.String)

or

Transformer.setOutputProperties(java.util.Properties)

will
throw a

IllegalArgumentException

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### METHOD

public static final

String

METHOD

method = "xml" | "html" | "text" |

expanded name

.

The value of the method property identifies the overall method that
should be used for outputting the result tree. Other non-namespaced
values may be used, such as "xhtml", but, if accepted, the handling
of such values is implementation defined. If any of the method values
are not accepted and are not namespace qualified,
then

Transformer.setOutputProperty(java.lang.String, java.lang.String)

or

Transformer.setOutputProperties(java.util.Properties)

will
throw a

IllegalArgumentException

.

The value of the method property identifies the overall method that
should be used for outputting the result tree. Other non-namespaced
values may be used, such as "xhtml", but, if accepted, the handling
of such values is implementation defined. If any of the method values
are not accepted and are not namespace qualified,
then

Transformer.setOutputProperty(java.lang.String, java.lang.String)

or

Transformer.setOutputProperties(java.util.Properties)

will
throw a

IllegalArgumentException

.

VERSION

```java
public static final
String
VERSION
```

version =

nmtoken

.

version

specifies the version of the output
method.

When the output method is "xml", the version value specifies the
version of XML to be used for outputting the result tree. The default
value for the xml output method is 1.0. When the output method is
"html", the version value indicates the version of the HTML.
The default value for the xml output method is 4.0, which specifies
that the result should be output as HTML conforming to the HTML 4.0
Recommendation [HTML]. If the output method is "text", the version
property is ignored.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### VERSION

public static final

String

VERSION

version =

nmtoken

.

version

specifies the version of the output
method.

When the output method is "xml", the version value specifies the
version of XML to be used for outputting the result tree. The default
value for the xml output method is 1.0. When the output method is
"html", the version value indicates the version of the HTML.
The default value for the xml output method is 4.0, which specifies
that the result should be output as HTML conforming to the HTML 4.0
Recommendation [HTML]. If the output method is "text", the version
property is ignored.

version

specifies the version of the output
method.

When the output method is "xml", the version value specifies the
version of XML to be used for outputting the result tree. The default
value for the xml output method is 1.0. When the output method is
"html", the version value indicates the version of the HTML.
The default value for the xml output method is 4.0, which specifies
that the result should be output as HTML conforming to the HTML 4.0
Recommendation [HTML]. If the output method is "text", the version
property is ignored.

ENCODING

```java
public static final
String
ENCODING
```

encoding =

string

.

encoding

specifies the preferred character
encoding that the Transformer should use to encode sequences of
characters as sequences of bytes. The value of the encoding property should be
treated case-insensitively. The value must only contain characters in
the range #x21 to #x7E (i.e., printable ASCII characters). The value
should either be a

charset

registered with the Internet
Assigned Numbers Authority

[IANA]

,

[RFC2278]

or start with

X-

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### ENCODING

public static final

String

ENCODING

encoding =

string

.

encoding

specifies the preferred character
encoding that the Transformer should use to encode sequences of
characters as sequences of bytes. The value of the encoding property should be
treated case-insensitively. The value must only contain characters in
the range #x21 to #x7E (i.e., printable ASCII characters). The value
should either be a

charset

registered with the Internet
Assigned Numbers Authority

[IANA]

,

[RFC2278]

or start with

X-

.

encoding

specifies the preferred character
encoding that the Transformer should use to encode sequences of
characters as sequences of bytes. The value of the encoding property should be
treated case-insensitively. The value must only contain characters in
the range #x21 to #x7E (i.e., printable ASCII characters). The value
should either be a

charset

registered with the Internet
Assigned Numbers Authority

[IANA]

,

[RFC2278]

or start with

X-

.

OMIT_XML_DECLARATION

```java
public static final
String
OMIT_XML_DECLARATION
```

omit-xml-declaration = "yes" | "no".

omit-xml-declaration

specifies whether the XSLT
processor should output an XML declaration; the value must be

yes

or

no

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### OMIT_XML_DECLARATION

public static final

String

OMIT_XML_DECLARATION

omit-xml-declaration = "yes" | "no".

omit-xml-declaration

specifies whether the XSLT
processor should output an XML declaration; the value must be

yes

or

no

.

omit-xml-declaration

specifies whether the XSLT
processor should output an XML declaration; the value must be

yes

or

no

.

STANDALONE

```java
public static final
String
STANDALONE
```

standalone = "yes" | "no".

standalone

specifies whether the Transformer
should output a standalone document declaration; the value must be

yes

or

no

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### STANDALONE

public static final

String

STANDALONE

standalone = "yes" | "no".

standalone

specifies whether the Transformer
should output a standalone document declaration; the value must be

yes

or

no

.

standalone

specifies whether the Transformer
should output a standalone document declaration; the value must be

yes

or

no

.

DOCTYPE_PUBLIC

```java
public static final
String
DOCTYPE_PUBLIC
```

doctype-public =

string

.

See the documentation for the

DOCTYPE_SYSTEM

property
for a description of what the value of the key should be.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### DOCTYPE_PUBLIC

public static final

String

DOCTYPE_PUBLIC

doctype-public =

string

.

See the documentation for the

DOCTYPE_SYSTEM

property
for a description of what the value of the key should be.

See the documentation for the

DOCTYPE_SYSTEM

property
for a description of what the value of the key should be.

DOCTYPE_SYSTEM

```java
public static final
String
DOCTYPE_SYSTEM
```

doctype-system =

string

.

doctype-system

specifies the system identifier
to be used in the document type declaration.

If the doctype-system property is specified, the xml output method
should output a document type declaration immediately before the first
element. The name following <!DOCTYPE should be the name of the first
element. If doctype-public property is also specified, then the xml
output method should output PUBLIC followed by the public identifier
and then the system identifier; otherwise, it should output SYSTEM
followed by the system identifier. The internal subset should be empty.
The value of the doctype-public property should be ignored unless the doctype-system
property is specified.

If the doctype-public or doctype-system properties are specified,
then the html output method should output a document type declaration
immediately before the first element. The name following <!DOCTYPE
should be HTML or html. If the doctype-public property is specified,
then the output method should output PUBLIC followed by the specified
public identifier; if the doctype-system property is also specified,
it should also output the specified system identifier following the
public identifier. If the doctype-system property is specified but
the doctype-public property is not specified, then the output method
should output SYSTEM followed by the specified system identifier.

doctype-system

specifies the system identifier
to be used in the document type declaration.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### DOCTYPE_SYSTEM

public static final

String

DOCTYPE_SYSTEM

doctype-system =

string

.

doctype-system

specifies the system identifier
to be used in the document type declaration.

If the doctype-system property is specified, the xml output method
should output a document type declaration immediately before the first
element. The name following <!DOCTYPE should be the name of the first
element. If doctype-public property is also specified, then the xml
output method should output PUBLIC followed by the public identifier
and then the system identifier; otherwise, it should output SYSTEM
followed by the system identifier. The internal subset should be empty.
The value of the doctype-public property should be ignored unless the doctype-system
property is specified.

If the doctype-public or doctype-system properties are specified,
then the html output method should output a document type declaration
immediately before the first element. The name following <!DOCTYPE
should be HTML or html. If the doctype-public property is specified,
then the output method should output PUBLIC followed by the specified
public identifier; if the doctype-system property is also specified,
it should also output the specified system identifier following the
public identifier. If the doctype-system property is specified but
the doctype-public property is not specified, then the output method
should output SYSTEM followed by the specified system identifier.

doctype-system

specifies the system identifier
to be used in the document type declaration.

doctype-system

specifies the system identifier
to be used in the document type declaration.

If the doctype-system property is specified, the xml output method
should output a document type declaration immediately before the first
element. The name following <!DOCTYPE should be the name of the first
element. If doctype-public property is also specified, then the xml
output method should output PUBLIC followed by the public identifier
and then the system identifier; otherwise, it should output SYSTEM
followed by the system identifier. The internal subset should be empty.
The value of the doctype-public property should be ignored unless the doctype-system
property is specified.

If the doctype-public or doctype-system properties are specified,
then the html output method should output a document type declaration
immediately before the first element. The name following <!DOCTYPE
should be HTML or html. If the doctype-public property is specified,
then the output method should output PUBLIC followed by the specified
public identifier; if the doctype-system property is also specified,
it should also output the specified system identifier following the
public identifier. If the doctype-system property is specified but
the doctype-public property is not specified, then the output method
should output SYSTEM followed by the specified system identifier.

CDATA_SECTION_ELEMENTS

```java
public static final
String
CDATA_SECTION_ELEMENTS
```

cdata-section-elements =

expanded names

.

cdata-section-elements

specifies a whitespace delimited
list of the names of elements whose text node children should be output
using CDATA sections. Note that these names must use the format
described in the section Qualfied Name Representation in

javax.xml.transform

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation.

,

Constant Field Values

---

#### CDATA_SECTION_ELEMENTS

public static final

String

CDATA_SECTION_ELEMENTS

cdata-section-elements =

expanded names

.

cdata-section-elements

specifies a whitespace delimited
list of the names of elements whose text node children should be output
using CDATA sections. Note that these names must use the format
described in the section Qualfied Name Representation in

javax.xml.transform

.

cdata-section-elements

specifies a whitespace delimited
list of the names of elements whose text node children should be output
using CDATA sections. Note that these names must use the format
described in the section Qualfied Name Representation in

javax.xml.transform

.

INDENT

```java
public static final
String
INDENT
```

indent = "yes" | "no".

indent

specifies whether the Transformer may
add additional whitespace when outputting the result tree; the value
must be

yes

or

no

.

**See Also:** section 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### INDENT

public static final

String

INDENT

indent = "yes" | "no".

indent

specifies whether the Transformer may
add additional whitespace when outputting the result tree; the value
must be

yes

or

no

.

indent

specifies whether the Transformer may
add additional whitespace when outputting the result tree; the value
must be

yes

or

no

.

MEDIA_TYPE

```java
public static final
String
MEDIA_TYPE
```

media-type =

string

.

media-type

specifies the media type (MIME
content type) of the data that results from outputting the result
tree. The

charset

parameter should not be specified
explicitly; instead, when the top-level media type is

text

, a

charset

parameter should be added
according to the character encoding actually used by the output
method.

**See Also:** s
ection 16 of the XSL Transformations (XSLT) W3C Recommendation

,

Constant Field Values

---

#### MEDIA_TYPE

public static final

String

MEDIA_TYPE

media-type =

string

.

media-type

specifies the media type (MIME
content type) of the data that results from outputting the result
tree. The

charset

parameter should not be specified
explicitly; instead, when the top-level media type is

text

, a

charset

parameter should be added
according to the character encoding actually used by the output
method.

media-type

specifies the media type (MIME
content type) of the data that results from outputting the result
tree. The

charset

parameter should not be specified
explicitly; instead, when the top-level media type is

text

, a

charset

parameter should be added
according to the character encoding actually used by the output
method.

---

