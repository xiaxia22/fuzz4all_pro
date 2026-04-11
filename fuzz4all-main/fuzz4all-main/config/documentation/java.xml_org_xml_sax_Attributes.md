# Interface Attributes

**Source:** `java.xml\org\xml\sax\Attributes.html`

### Class Description

```java
public interface
Attributes
```

Interface for a list of XML attributes.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This interface allows access to a list of attributes in
three different ways:

- by attribute index;
- by Namespace-qualified name; or
- by qualified (prefixed) name.

The list will not contain attributes that were declared
#IMPLIED but not specified in the start tag. It will also not
contain attributes used as Namespace declarations (xmlns*) unless
the

http://xml.org/sax/features/namespace-prefixes

feature is set to

true

(it is

false

by
default).
Because SAX2 conforms to the original "Namespaces in XML"
recommendation, it normally does not
give namespace declaration attributes a namespace URI.

Some SAX2 parsers may support using an optional feature flag
(

http://xml.org/sax/features/xmlns-uris

) to request
that those attributes be given URIs, conforming to a later
backwards-incompatible revision of that recommendation. (The
attribute's "local name" will be the prefix, or "xmlns" when
defining a default element namespace.) For portability, handler
code should always resolve that conflict, rather than requiring
parsers that can change the setting of that feature flag.

If the namespace-prefixes feature (see above) is

false

, access by qualified name may not be available; if
the

http://xml.org/sax/features/namespaces

feature is

false

, access by Namespace-qualified names may not be
available.

This interface replaces the now-deprecated SAX1

AttributeList

interface, which does not
contain Namespace support. In addition to Namespace support, it
adds the

getIndex

methods (below).

The order of attributes in the list is unspecified, and will
vary from implementation to implementation.

**All Known Subinterfaces:** Attributes2

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getLength()

Return the number of attributes in the list.

Once you know the number of attributes, you can iterate
through the list.

**Returns:**
- The number of attributes in the list.

**See Also:**
- getURI(int)

,

getLocalName(int)

,

getQName(int)

,

getType(int)

,

getValue(int)

---

#### String
getURI​(int index)

Look up an attribute's Namespace URI by index.

**Parameters:**
- index

- The attribute index (zero-based).

**Returns:**
- The Namespace URI, or the empty string if none
is available, or null if the index is out of
range.

**See Also:**
- getLength()

---

#### String
getLocalName​(int index)

Look up an attribute's local name by index.

**Parameters:**
- index

- The attribute index (zero-based).

**Returns:**
- The local name, or the empty string if Namespace
processing is not being performed, or null
if the index is out of range.

**See Also:**
- getLength()

---

#### String
getQName​(int index)

Look up an attribute's XML qualified (prefixed) name by index.

**Parameters:**
- index

- The attribute index (zero-based).

**Returns:**
- The XML qualified name, or the empty string
if none is available, or null if the index
is out of range.

**See Also:**
- getLength()

---

#### String
getType​(int index)

Look up an attribute's type by index.

The attribute type is one of the strings "CDATA", "ID",
"IDREF", "IDREFS", "NMTOKEN", "NMTOKENS", "ENTITY", "ENTITIES",
or "NOTATION" (always in upper case).

If the parser has not read a declaration for the attribute,
or if the parser does not report attribute types, then it must
return the value "CDATA" as stated in the XML 1.0 Recommendation
(clause 3.3.3, "Attribute-Value Normalization").

For an enumerated attribute that is not a notation, the
parser will report the type as "NMTOKEN".

**Parameters:**
- index

- The attribute index (zero-based).

**Returns:**
- The attribute's type as a string, or null if the
index is out of range.

**See Also:**
- getLength()

---

#### String
getValue​(int index)

Look up an attribute's value by index.

If the attribute value is a list of tokens (IDREFS,
ENTITIES, or NMTOKENS), the tokens will be concatenated
into a single string with each token separated by a
single space.

**Parameters:**
- index

- The attribute index (zero-based).

**Returns:**
- The attribute's value as a string, or null if the
index is out of range.

**See Also:**
- getLength()

---

#### int getIndex​(
String
uri,

String
localName)

Look up the index of an attribute by Namespace name.

**Parameters:**
- uri

- The Namespace URI, or the empty string if
the name has no Namespace URI.
- localName

- The attribute's local name.

**Returns:**
- The index of the attribute, or -1 if it does not
appear in the list.

---

#### int getIndex​(
String
qName)

Look up the index of an attribute by XML qualified (prefixed) name.

**Parameters:**
- qName

- The qualified (prefixed) name.

**Returns:**
- The index of the attribute, or -1 if it does not
appear in the list.

---

#### String
getType​(
String
uri,

String
localName)

Look up an attribute's type by Namespace name.

See

getType(int)

for a description
of the possible types.

**Parameters:**
- uri

- The Namespace URI, or the empty String if the
name has no Namespace URI.
- localName

- The local name of the attribute.

**Returns:**
- The attribute type as a string, or null if the
attribute is not in the list or if Namespace
processing is not being performed.

---

#### String
getType​(
String
qName)

Look up an attribute's type by XML qualified (prefixed) name.

See

getType(int)

for a description
of the possible types.

**Parameters:**
- qName

- The XML qualified name.

**Returns:**
- The attribute type as a string, or null if the
attribute is not in the list or if qualified names
are not available.

---

#### String
getValue​(
String
uri,

String
localName)

Look up an attribute's value by Namespace name.

See

getValue(int)

for a description
of the possible values.

**Parameters:**
- uri

- The Namespace URI, or the empty String if the
name has no Namespace URI.
- localName

- The local name of the attribute.

**Returns:**
- The attribute value as a string, or null if the
attribute is not in the list.

---

#### String
getValue​(
String
qName)

Look up an attribute's value by XML qualified (prefixed) name.

See

getValue(int)

for a description
of the possible values.

**Parameters:**
- qName

- The XML qualified name.

**Returns:**
- The attribute value as a string, or null if the
attribute is not in the list or if qualified names
are not available.

---

### Additional Sections

#### Interface Attributes

**All Known Subinterfaces:** Attributes2

**All Known Implementing Classes:** Attributes2Impl

,

AttributesImpl

```java
public interface
Attributes
```

Interface for a list of XML attributes.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This interface allows access to a list of attributes in
three different ways:

- by attribute index;
- by Namespace-qualified name; or
- by qualified (prefixed) name.

The list will not contain attributes that were declared
#IMPLIED but not specified in the start tag. It will also not
contain attributes used as Namespace declarations (xmlns*) unless
the

http://xml.org/sax/features/namespace-prefixes

feature is set to

true

(it is

false

by
default).
Because SAX2 conforms to the original "Namespaces in XML"
recommendation, it normally does not
give namespace declaration attributes a namespace URI.

Some SAX2 parsers may support using an optional feature flag
(

http://xml.org/sax/features/xmlns-uris

) to request
that those attributes be given URIs, conforming to a later
backwards-incompatible revision of that recommendation. (The
attribute's "local name" will be the prefix, or "xmlns" when
defining a default element namespace.) For portability, handler
code should always resolve that conflict, rather than requiring
parsers that can change the setting of that feature flag.

If the namespace-prefixes feature (see above) is

false

, access by qualified name may not be available; if
the

http://xml.org/sax/features/namespaces

feature is

false

, access by Namespace-qualified names may not be
available.

This interface replaces the now-deprecated SAX1

AttributeList

interface, which does not
contain Namespace support. In addition to Namespace support, it
adds the

getIndex

methods (below).

The order of attributes in the list is unspecified, and will
vary from implementation to implementation.

**Since:** 1.4, SAX 2.0
**See Also:** AttributesImpl

,

DeclHandler.attributeDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String)

public interface

Attributes

Interface for a list of XML attributes.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This interface allows access to a list of attributes in
three different ways:

- by attribute index;
- by Namespace-qualified name; or
- by qualified (prefixed) name.

The list will not contain attributes that were declared
#IMPLIED but not specified in the start tag. It will also not
contain attributes used as Namespace declarations (xmlns*) unless
the

http://xml.org/sax/features/namespace-prefixes

feature is set to

true

(it is

false

by
default).
Because SAX2 conforms to the original "Namespaces in XML"
recommendation, it normally does not
give namespace declaration attributes a namespace URI.

Some SAX2 parsers may support using an optional feature flag
(

http://xml.org/sax/features/xmlns-uris

) to request
that those attributes be given URIs, conforming to a later
backwards-incompatible revision of that recommendation. (The
attribute's "local name" will be the prefix, or "xmlns" when
defining a default element namespace.) For portability, handler
code should always resolve that conflict, rather than requiring
parsers that can change the setting of that feature flag.

If the namespace-prefixes feature (see above) is

false

, access by qualified name may not be available; if
the

http://xml.org/sax/features/namespaces

feature is

false

, access by Namespace-qualified names may not be
available.

This interface replaces the now-deprecated SAX1

AttributeList

interface, which does not
contain Namespace support. In addition to Namespace support, it
adds the

getIndex

methods (below).

The order of attributes in the list is unspecified, and will
vary from implementation to implementation.

This interface allows access to a list of attributes in
three different ways:

by attribute index;

by Namespace-qualified name; or

by qualified (prefixed) name.

The list will not contain attributes that were declared
#IMPLIED but not specified in the start tag. It will also not
contain attributes used as Namespace declarations (xmlns*) unless
the

http://xml.org/sax/features/namespace-prefixes

feature is set to

true

(it is

false

by
default).
Because SAX2 conforms to the original "Namespaces in XML"
recommendation, it normally does not
give namespace declaration attributes a namespace URI.

Some SAX2 parsers may support using an optional feature flag
(

http://xml.org/sax/features/xmlns-uris

) to request
that those attributes be given URIs, conforming to a later
backwards-incompatible revision of that recommendation. (The
attribute's "local name" will be the prefix, or "xmlns" when
defining a default element namespace.) For portability, handler
code should always resolve that conflict, rather than requiring
parsers that can change the setting of that feature flag.

If the namespace-prefixes feature (see above) is

false

, access by qualified name may not be available; if
the

http://xml.org/sax/features/namespaces

feature is

false

, access by Namespace-qualified names may not be
available.

This interface replaces the now-deprecated SAX1

AttributeList

interface, which does not
contain Namespace support. In addition to Namespace support, it
adds the

getIndex

methods (below).

The order of attributes in the list is unspecified, and will
vary from implementation to implementation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getIndex

​(

String

qName)

Look up the index of an attribute by XML qualified (prefixed) name.

int

getIndex

​(

String

uri,

String

localName)

Look up the index of an attribute by Namespace name.

int

getLength

()

Return the number of attributes in the list.

String

getLocalName

​(int index)

Look up an attribute's local name by index.

String

getQName

​(int index)

Look up an attribute's XML qualified (prefixed) name by index.

String

getType

​(int index)

Look up an attribute's type by index.

String

getType

​(

String

qName)

Look up an attribute's type by XML qualified (prefixed) name.

String

getType

​(

String

uri,

String

localName)

Look up an attribute's type by Namespace name.

String

getURI

​(int index)

Look up an attribute's Namespace URI by index.

String

getValue

​(int index)

Look up an attribute's value by index.

String

getValue

​(

String

qName)

Look up an attribute's value by XML qualified (prefixed) name.

String

getValue

​(

String

uri,

String

localName)

Look up an attribute's value by Namespace name.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getIndex

​(

String

qName)

Look up the index of an attribute by XML qualified (prefixed) name.

int

getIndex

​(

String

uri,

String

localName)

Look up the index of an attribute by Namespace name.

int

getLength

()

Return the number of attributes in the list.

String

getLocalName

​(int index)

Look up an attribute's local name by index.

String

getQName

​(int index)

Look up an attribute's XML qualified (prefixed) name by index.

String

getType

​(int index)

Look up an attribute's type by index.

String

getType

​(

String

qName)

Look up an attribute's type by XML qualified (prefixed) name.

String

getType

​(

String

uri,

String

localName)

Look up an attribute's type by Namespace name.

String

getURI

​(int index)

Look up an attribute's Namespace URI by index.

String

getValue

​(int index)

Look up an attribute's value by index.

String

getValue

​(

String

qName)

Look up an attribute's value by XML qualified (prefixed) name.

String

getValue

​(

String

uri,

String

localName)

Look up an attribute's value by Namespace name.

---

#### Method Summary

Look up the index of an attribute by XML qualified (prefixed) name.

Look up the index of an attribute by Namespace name.

Return the number of attributes in the list.

Look up an attribute's local name by index.

Look up an attribute's XML qualified (prefixed) name by index.

Look up an attribute's type by index.

Look up an attribute's type by XML qualified (prefixed) name.

Look up an attribute's type by Namespace name.

Look up an attribute's Namespace URI by index.

Look up an attribute's value by index.

Look up an attribute's value by XML qualified (prefixed) name.

Look up an attribute's value by Namespace name.

============ METHOD DETAIL ==========

- Method Detail

- getLength

```java
int getLength()
```

Return the number of attributes in the list.

Once you know the number of attributes, you can iterate
through the list.

**Returns:** The number of attributes in the list.
**See Also:** getURI(int)

,

getLocalName(int)

,

getQName(int)

,

getType(int)

,

getValue(int)

- getURI

```java
String
getURI​(int index)
```

Look up an attribute's Namespace URI by index.

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The Namespace URI, or the empty string if none
is available, or null if the index is out of
range.
**See Also:** getLength()

- getLocalName

```java
String
getLocalName​(int index)
```

Look up an attribute's local name by index.

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The local name, or the empty string if Namespace
processing is not being performed, or null
if the index is out of range.
**See Also:** getLength()

- getQName

```java
String
getQName​(int index)
```

Look up an attribute's XML qualified (prefixed) name by index.

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The XML qualified name, or the empty string
if none is available, or null if the index
is out of range.
**See Also:** getLength()

- getType

```java
String
getType​(int index)
```

Look up an attribute's type by index.

The attribute type is one of the strings "CDATA", "ID",
"IDREF", "IDREFS", "NMTOKEN", "NMTOKENS", "ENTITY", "ENTITIES",
or "NOTATION" (always in upper case).

If the parser has not read a declaration for the attribute,
or if the parser does not report attribute types, then it must
return the value "CDATA" as stated in the XML 1.0 Recommendation
(clause 3.3.3, "Attribute-Value Normalization").

For an enumerated attribute that is not a notation, the
parser will report the type as "NMTOKEN".

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The attribute's type as a string, or null if the
index is out of range.
**See Also:** getLength()

- getValue

```java
String
getValue​(int index)
```

Look up an attribute's value by index.

If the attribute value is a list of tokens (IDREFS,
ENTITIES, or NMTOKENS), the tokens will be concatenated
into a single string with each token separated by a
single space.

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The attribute's value as a string, or null if the
index is out of range.
**See Also:** getLength()

- getIndex

```java
int getIndex​(
String
uri,

String
localName)
```

Look up the index of an attribute by Namespace name.

**Parameters:** uri

- The Namespace URI, or the empty string if
the name has no Namespace URI.
**Parameters:** localName

- The attribute's local name.
**Returns:** The index of the attribute, or -1 if it does not
appear in the list.

- getIndex

```java
int getIndex​(
String
qName)
```

Look up the index of an attribute by XML qualified (prefixed) name.

**Parameters:** qName

- The qualified (prefixed) name.
**Returns:** The index of the attribute, or -1 if it does not
appear in the list.

- getType

```java
String
getType​(
String
uri,

String
localName)
```

Look up an attribute's type by Namespace name.

See

getType(int)

for a description
of the possible types.

**Parameters:** uri

- The Namespace URI, or the empty String if the
name has no Namespace URI.
**Parameters:** localName

- The local name of the attribute.
**Returns:** The attribute type as a string, or null if the
attribute is not in the list or if Namespace
processing is not being performed.

- getType

```java
String
getType​(
String
qName)
```

Look up an attribute's type by XML qualified (prefixed) name.

See

getType(int)

for a description
of the possible types.

**Parameters:** qName

- The XML qualified name.
**Returns:** The attribute type as a string, or null if the
attribute is not in the list or if qualified names
are not available.

- getValue

```java
String
getValue​(
String
uri,

String
localName)
```

Look up an attribute's value by Namespace name.

See

getValue(int)

for a description
of the possible values.

**Parameters:** uri

- The Namespace URI, or the empty String if the
name has no Namespace URI.
**Parameters:** localName

- The local name of the attribute.
**Returns:** The attribute value as a string, or null if the
attribute is not in the list.

- getValue

```java
String
getValue​(
String
qName)
```

Look up an attribute's value by XML qualified (prefixed) name.

See

getValue(int)

for a description
of the possible values.

**Parameters:** qName

- The XML qualified name.
**Returns:** The attribute value as a string, or null if the
attribute is not in the list or if qualified names
are not available.

Method Detail

- getLength

```java
int getLength()
```

Return the number of attributes in the list.

Once you know the number of attributes, you can iterate
through the list.

**Returns:** The number of attributes in the list.
**See Also:** getURI(int)

,

getLocalName(int)

,

getQName(int)

,

getType(int)

,

getValue(int)

- getURI

```java
String
getURI​(int index)
```

Look up an attribute's Namespace URI by index.

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The Namespace URI, or the empty string if none
is available, or null if the index is out of
range.
**See Also:** getLength()

- getLocalName

```java
String
getLocalName​(int index)
```

Look up an attribute's local name by index.

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The local name, or the empty string if Namespace
processing is not being performed, or null
if the index is out of range.
**See Also:** getLength()

- getQName

```java
String
getQName​(int index)
```

Look up an attribute's XML qualified (prefixed) name by index.

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The XML qualified name, or the empty string
if none is available, or null if the index
is out of range.
**See Also:** getLength()

- getType

```java
String
getType​(int index)
```

Look up an attribute's type by index.

The attribute type is one of the strings "CDATA", "ID",
"IDREF", "IDREFS", "NMTOKEN", "NMTOKENS", "ENTITY", "ENTITIES",
or "NOTATION" (always in upper case).

If the parser has not read a declaration for the attribute,
or if the parser does not report attribute types, then it must
return the value "CDATA" as stated in the XML 1.0 Recommendation
(clause 3.3.3, "Attribute-Value Normalization").

For an enumerated attribute that is not a notation, the
parser will report the type as "NMTOKEN".

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The attribute's type as a string, or null if the
index is out of range.
**See Also:** getLength()

- getValue

```java
String
getValue​(int index)
```

Look up an attribute's value by index.

If the attribute value is a list of tokens (IDREFS,
ENTITIES, or NMTOKENS), the tokens will be concatenated
into a single string with each token separated by a
single space.

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The attribute's value as a string, or null if the
index is out of range.
**See Also:** getLength()

- getIndex

```java
int getIndex​(
String
uri,

String
localName)
```

Look up the index of an attribute by Namespace name.

**Parameters:** uri

- The Namespace URI, or the empty string if
the name has no Namespace URI.
**Parameters:** localName

- The attribute's local name.
**Returns:** The index of the attribute, or -1 if it does not
appear in the list.

- getIndex

```java
int getIndex​(
String
qName)
```

Look up the index of an attribute by XML qualified (prefixed) name.

**Parameters:** qName

- The qualified (prefixed) name.
**Returns:** The index of the attribute, or -1 if it does not
appear in the list.

- getType

```java
String
getType​(
String
uri,

String
localName)
```

Look up an attribute's type by Namespace name.

See

getType(int)

for a description
of the possible types.

**Parameters:** uri

- The Namespace URI, or the empty String if the
name has no Namespace URI.
**Parameters:** localName

- The local name of the attribute.
**Returns:** The attribute type as a string, or null if the
attribute is not in the list or if Namespace
processing is not being performed.

- getType

```java
String
getType​(
String
qName)
```

Look up an attribute's type by XML qualified (prefixed) name.

See

getType(int)

for a description
of the possible types.

**Parameters:** qName

- The XML qualified name.
**Returns:** The attribute type as a string, or null if the
attribute is not in the list or if qualified names
are not available.

- getValue

```java
String
getValue​(
String
uri,

String
localName)
```

Look up an attribute's value by Namespace name.

See

getValue(int)

for a description
of the possible values.

**Parameters:** uri

- The Namespace URI, or the empty String if the
name has no Namespace URI.
**Parameters:** localName

- The local name of the attribute.
**Returns:** The attribute value as a string, or null if the
attribute is not in the list.

- getValue

```java
String
getValue​(
String
qName)
```

Look up an attribute's value by XML qualified (prefixed) name.

See

getValue(int)

for a description
of the possible values.

**Parameters:** qName

- The XML qualified name.
**Returns:** The attribute value as a string, or null if the
attribute is not in the list or if qualified names
are not available.

---

#### Method Detail

getLength

```java
int getLength()
```

Return the number of attributes in the list.

Once you know the number of attributes, you can iterate
through the list.

**Returns:** The number of attributes in the list.
**See Also:** getURI(int)

,

getLocalName(int)

,

getQName(int)

,

getType(int)

,

getValue(int)

---

#### getLength

int getLength()

Return the number of attributes in the list.

Once you know the number of attributes, you can iterate
through the list.

Once you know the number of attributes, you can iterate
through the list.

getURI

```java
String
getURI​(int index)
```

Look up an attribute's Namespace URI by index.

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The Namespace URI, or the empty string if none
is available, or null if the index is out of
range.
**See Also:** getLength()

---

#### getURI

String

getURI​(int index)

Look up an attribute's Namespace URI by index.

getLocalName

```java
String
getLocalName​(int index)
```

Look up an attribute's local name by index.

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The local name, or the empty string if Namespace
processing is not being performed, or null
if the index is out of range.
**See Also:** getLength()

---

#### getLocalName

String

getLocalName​(int index)

Look up an attribute's local name by index.

getQName

```java
String
getQName​(int index)
```

Look up an attribute's XML qualified (prefixed) name by index.

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The XML qualified name, or the empty string
if none is available, or null if the index
is out of range.
**See Also:** getLength()

---

#### getQName

String

getQName​(int index)

Look up an attribute's XML qualified (prefixed) name by index.

getType

```java
String
getType​(int index)
```

Look up an attribute's type by index.

The attribute type is one of the strings "CDATA", "ID",
"IDREF", "IDREFS", "NMTOKEN", "NMTOKENS", "ENTITY", "ENTITIES",
or "NOTATION" (always in upper case).

If the parser has not read a declaration for the attribute,
or if the parser does not report attribute types, then it must
return the value "CDATA" as stated in the XML 1.0 Recommendation
(clause 3.3.3, "Attribute-Value Normalization").

For an enumerated attribute that is not a notation, the
parser will report the type as "NMTOKEN".

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The attribute's type as a string, or null if the
index is out of range.
**See Also:** getLength()

---

#### getType

String

getType​(int index)

Look up an attribute's type by index.

The attribute type is one of the strings "CDATA", "ID",
"IDREF", "IDREFS", "NMTOKEN", "NMTOKENS", "ENTITY", "ENTITIES",
or "NOTATION" (always in upper case).

If the parser has not read a declaration for the attribute,
or if the parser does not report attribute types, then it must
return the value "CDATA" as stated in the XML 1.0 Recommendation
(clause 3.3.3, "Attribute-Value Normalization").

For an enumerated attribute that is not a notation, the
parser will report the type as "NMTOKEN".

The attribute type is one of the strings "CDATA", "ID",
"IDREF", "IDREFS", "NMTOKEN", "NMTOKENS", "ENTITY", "ENTITIES",
or "NOTATION" (always in upper case).

If the parser has not read a declaration for the attribute,
or if the parser does not report attribute types, then it must
return the value "CDATA" as stated in the XML 1.0 Recommendation
(clause 3.3.3, "Attribute-Value Normalization").

For an enumerated attribute that is not a notation, the
parser will report the type as "NMTOKEN".

getValue

```java
String
getValue​(int index)
```

Look up an attribute's value by index.

If the attribute value is a list of tokens (IDREFS,
ENTITIES, or NMTOKENS), the tokens will be concatenated
into a single string with each token separated by a
single space.

**Parameters:** index

- The attribute index (zero-based).
**Returns:** The attribute's value as a string, or null if the
index is out of range.
**See Also:** getLength()

---

#### getValue

String

getValue​(int index)

Look up an attribute's value by index.

If the attribute value is a list of tokens (IDREFS,
ENTITIES, or NMTOKENS), the tokens will be concatenated
into a single string with each token separated by a
single space.

If the attribute value is a list of tokens (IDREFS,
ENTITIES, or NMTOKENS), the tokens will be concatenated
into a single string with each token separated by a
single space.

getIndex

```java
int getIndex​(
String
uri,

String
localName)
```

Look up the index of an attribute by Namespace name.

**Parameters:** uri

- The Namespace URI, or the empty string if
the name has no Namespace URI.
**Parameters:** localName

- The attribute's local name.
**Returns:** The index of the attribute, or -1 if it does not
appear in the list.

---

#### getIndex

int getIndex​(

String

uri,

String

localName)

Look up the index of an attribute by Namespace name.

getIndex

```java
int getIndex​(
String
qName)
```

Look up the index of an attribute by XML qualified (prefixed) name.

**Parameters:** qName

- The qualified (prefixed) name.
**Returns:** The index of the attribute, or -1 if it does not
appear in the list.

---

#### getIndex

int getIndex​(

String

qName)

Look up the index of an attribute by XML qualified (prefixed) name.

getType

```java
String
getType​(
String
uri,

String
localName)
```

Look up an attribute's type by Namespace name.

See

getType(int)

for a description
of the possible types.

**Parameters:** uri

- The Namespace URI, or the empty String if the
name has no Namespace URI.
**Parameters:** localName

- The local name of the attribute.
**Returns:** The attribute type as a string, or null if the
attribute is not in the list or if Namespace
processing is not being performed.

---

#### getType

String

getType​(

String

uri,

String

localName)

Look up an attribute's type by Namespace name.

See

getType(int)

for a description
of the possible types.

See

getType(int)

for a description
of the possible types.

getType

```java
String
getType​(
String
qName)
```

Look up an attribute's type by XML qualified (prefixed) name.

See

getType(int)

for a description
of the possible types.

**Parameters:** qName

- The XML qualified name.
**Returns:** The attribute type as a string, or null if the
attribute is not in the list or if qualified names
are not available.

---

#### getType

String

getType​(

String

qName)

Look up an attribute's type by XML qualified (prefixed) name.

See

getType(int)

for a description
of the possible types.

See

getType(int)

for a description
of the possible types.

getValue

```java
String
getValue​(
String
uri,

String
localName)
```

Look up an attribute's value by Namespace name.

See

getValue(int)

for a description
of the possible values.

**Parameters:** uri

- The Namespace URI, or the empty String if the
name has no Namespace URI.
**Parameters:** localName

- The local name of the attribute.
**Returns:** The attribute value as a string, or null if the
attribute is not in the list.

---

#### getValue

String

getValue​(

String

uri,

String

localName)

Look up an attribute's value by Namespace name.

See

getValue(int)

for a description
of the possible values.

See

getValue(int)

for a description
of the possible values.

getValue

```java
String
getValue​(
String
qName)
```

Look up an attribute's value by XML qualified (prefixed) name.

See

getValue(int)

for a description
of the possible values.

**Parameters:** qName

- The XML qualified name.
**Returns:** The attribute value as a string, or null if the
attribute is not in the list or if qualified names
are not available.

---

#### getValue

String

getValue​(

String

qName)

Look up an attribute's value by XML qualified (prefixed) name.

See

getValue(int)

for a description
of the possible values.

See

getValue(int)

for a description
of the possible values.

---

