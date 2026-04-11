# Interface IIOMetadataFormat

**Source:** `java.desktop\javax\imageio\metadata\IIOMetadataFormat.html`

### Class Description

```java
public interface
IIOMetadataFormat
```

An object describing the structure of metadata documents returned
from

IIOMetadata.getAsTree

and passed to

IIOMetadata.setFromTree

and

mergeTree

.
Document structures are described by a set of constraints on the
type and number of child elements that may belong to a given parent
element type, the names, types, and values of attributes that may
belong to an element, and the type and values of

Object

reference that may be stored at a node.

N.B: classes that implement this interface should contain a
method declared as

public static getInstance()

which
returns an instance of the class. Commonly, an implementation will
construct only a single instance and cache it for future
invocations of

getInstance

.

In the event that the plugin is provided as part of a named module,
that module must export the package containing the implementation class
to the

```java
java.desktop
```

module via a qualified export.
An unqualified export is not recommended unless also needed for
some other reason. Failing to export the package will result in
access failure at runtime.

The structures that may be described by this class are a subset
of those expressible using XML document type definitions (DTDs),
with the addition of some basic information on the datatypes of
attributes and the ability to store an

Object

reference within a node. In the future, XML Schemas could be used
to represent these structures, and many others.

The differences between

IIOMetadataFormat

-described structures and DTDs are as
follows:

- Elements may not contain text or mix text with embedded
tags.

The children of an element must conform to one of a few simple
patterns, described in the documentation for the

CHILD_*

constants;

The in-memory representation of an elements may contain a
reference to an

Object

. There is no provision for
representing such objects textually.

**All Known Implementing Classes:** IIOMetadataFormatImpl

---

### Field Details

#### static final int CHILD_POLICY_EMPTY

A constant returned by

getChildPolicy

to indicate
that an element may not have any children. In other words, it
is required to be a leaf node.

**See Also:**
- Constant Field Values

---

#### static final int CHILD_POLICY_ALL

A constant returned by

getChildPolicy

to indicate
that an element must have a single instance of each of its
legal child elements, in order. In DTD terms, the contents of
the element are defined by a sequence

a,b,c,d,...

.

**See Also:**
- Constant Field Values

---

#### static final int CHILD_POLICY_SOME

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one instance of each of its
legal child elements, in order. In DTD terms, the contents of
the element are defined by a sequence

a?,b?,c?,d?,...

.

**See Also:**
- Constant Field Values

---

#### static final int CHILD_POLICY_CHOICE

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one children, selected from
among its legal child elements. In DTD terms, the contents of
the element are defined by a selection

a|b|c|d|...

.

**See Also:**
- Constant Field Values

---

#### static final int CHILD_POLICY_SEQUENCE

A constant returned by

getChildPolicy

to indicate
that an element must have a sequence of instances of any of its
legal child elements. In DTD terms, the contents of the
element are defined by a sequence

(a|b|c|d|...)*

.

**See Also:**
- Constant Field Values

---

#### static final int CHILD_POLICY_REPEAT

A constant returned by

getChildPolicy

to indicate
that an element must have zero or more instances of its unique
legal child element. In DTD terms, the contents of the element
are defined by a starred expression

a*

.

**See Also:**
- Constant Field Values

---

#### static final int CHILD_POLICY_MAX

The largest valid

CHILD_POLICY_*

constant,
to be used for range checks.

**See Also:**
- Constant Field Values

---

#### static final int VALUE_NONE

A constant returned by

getObjectValueType

to
indicate the absence of a user object.

**See Also:**
- Constant Field Values

---

#### static final int VALUE_ARBITRARY

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a single, arbitrary value.

**See Also:**
- Constant Field Values

---

#### static final int VALUE_RANGE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values. Both the minimum
and maximum values of the range are exclusive. It is
recommended that ranges of integers be inclusive on both ends,
and that exclusive ranges be used only for floating-point data.

**See Also:**
- VALUE_RANGE_MIN_MAX_INCLUSIVE

,

Constant Field Values

---

#### static final int VALUE_RANGE_MIN_INCLUSIVE_MASK

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MIN_INCLUSIVE

, and with

VALUE_RANGE_MAX_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

Similarly, the value may be and'ed with the value of

getAttributeValueType

or

getObjectValueType

to determine if the minimum
value of the range is inclusive.

**See Also:**
- Constant Field Values

---

#### static final int VALUE_RANGE_MAX_INCLUSIVE_MASK

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MAX_INCLUSIVE

, and with

VALUE_RANGE_MIN_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

Similarly, the value may be and'ed with the value of

getAttributeValueType

or

getObjectValueType

to determine if the maximum
value of the range is inclusive.

**See Also:**
- Constant Field Values

---

#### static final int VALUE_RANGE_MIN_INCLUSIVE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values. The minimum
(but not the maximum) value of the range is inclusive.

**See Also:**
- Constant Field Values

---

#### static final int VALUE_RANGE_MAX_INCLUSIVE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values. The maximum
(but not the minimum) value of the range is inclusive.

**See Also:**
- Constant Field Values

---

#### static final int VALUE_RANGE_MIN_MAX_INCLUSIVE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values. Both the minimum
and maximum values of the range are inclusive. It is
recommended that ranges of integers be inclusive on both ends,
and that exclusive ranges be used only for floating-point data.

**See Also:**
- Constant Field Values

---

#### static final int VALUE_ENUMERATION

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set one of a number of enumerated values.
In the case of attributes, these values are

String

s; for objects, they are

Object

s implementing a given class or interface.

Attribute values of type

DATATYPE_BOOLEAN

should be marked as enumerations.

**See Also:**
- Constant Field Values

---

#### static final int VALUE_LIST

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a list or array of values. In the
case of attributes, the list will consist of
whitespace-separated values within a

String

; for
objects, an array will be used.

**See Also:**
- Constant Field Values

---

#### static final int DATATYPE_STRING

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a general Unicode
string.

**See Also:**
- Constant Field Values

---

#### static final int DATATYPE_BOOLEAN

A constant returned by

getAttributeDataType

indicating that the value of an attribute is one of the boolean
values 'true' or 'false'.
Attribute values of type DATATYPE_BOOLEAN should be marked as
enumerations, and the permitted values should be the string
literal values "TRUE" or "FALSE", although a plugin may also
recognise lower or mixed case equivalents.

**See Also:**
- Constant Field Values

---

#### static final int DATATYPE_INTEGER

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of an integer.

**See Also:**
- Constant Field Values

---

#### static final int DATATYPE_FLOAT

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a decimal floating-point number.

**See Also:**
- Constant Field Values

---

#### static final int DATATYPE_DOUBLE

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a double-precision decimal floating-point
number.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### String
getRootName()

Returns the name of the root element of the format.

**Returns:**
- a

String

.

---

#### boolean canNodeAppear​(
String
elementName,

ImageTypeSpecifier
imageType)

Returns

true

if the element (and the subtree below
it) is allowed to appear in a metadata document for an image of
the given type, defined by an

ImageTypeSpecifier

.
For example, a metadata document format might contain an
element that describes the primary colors of the image, which
would not be allowed when writing a grayscale image.

**Parameters:**
- elementName

- the name of the element being queried.
- imageType

- an

ImageTypeSpecifier

indicating
the type of the image that will be associated with the
metadata.

**Returns:**
- true

if the node is meaningful for images
of the given type.

---

#### int getElementMinChildren​(
String
elementName)

Returns the minimum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

. For
example, an element representing color primary information
might be required to have at least 3 children, one for each
primary.

**Parameters:**
- elementName

- the name of the element being queried.

**Returns:**
- an

int

.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if the named element does
not have a child policy of

CHILD_POLICY_REPEAT

.

---

#### int getElementMaxChildren​(
String
elementName)

Returns the maximum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

. For
example, an element representing an entry in an 8-bit color
palette might be allowed to repeat up to 256 times. A value of

Integer.MAX_VALUE

may be used to specify that
there is no upper bound.

**Parameters:**
- elementName

- the name of the element being queried.

**Returns:**
- an

int

.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if the named element does
not have a child policy of

CHILD_POLICY_REPEAT

.

---

#### String
getElementDescription​(
String
elementName,

Locale
locale)

Returns a

String

containing a description of the
named element, or

null

. The description will be
localized for the supplied

Locale

if possible.

If

locale

is

null

, the current
default

Locale

returned by

Locale.getLocale

will be used.

**Parameters:**
- elementName

- the name of the element.
- locale

- the

Locale

for which localization
will be attempted.

**Returns:**
- the element description.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.

---

#### int getChildPolicy​(
String
elementName)

Returns one of the constants starting with

CHILD_POLICY_

, indicating the legal pattern of
children for the named element.

**Parameters:**
- elementName

- the name of the element being queried.

**Returns:**
- one of the

CHILD_POLICY_*

constants.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.

---

#### String
[] getChildNames​(
String
elementName)

Returns an array of

String

s indicating the names
of the element which are allowed to be children of the named
element, in the order in which they should appear. If the
element cannot have children,

null

is returned.

**Parameters:**
- elementName

- the name of the element being queried.

**Returns:**
- an array of

String

s, or null.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.

---

#### String
[] getAttributeNames​(
String
elementName)

Returns an array of

String

s listing the names of
the attributes that may be associated with the named element.

**Parameters:**
- elementName

- the name of the element being queried.

**Returns:**
- an array of

String

s.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.

---

#### int getAttributeValueType​(
String
elementName,

String
attrName)

Returns one of the constants starting with

VALUE_

,
indicating whether the values of the given attribute within the
named element are arbitrary, constrained to lie within a
specified range, constrained to be one of a set of enumerated
values, or are a whitespace-separated list of arbitrary values.

**Parameters:**
- elementName

- the name of the element being queried.
- attrName

- the name of the attribute being queried.

**Returns:**
- one of the

VALUE_*

constants.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

---

#### int getAttributeDataType​(
String
elementName,

String
attrName)

Returns one of the constants starting with

DATATYPE_

, indicating the format and
interpretation of the value of the given attribute within the
named element. If

getAttributeValueType

returns

VALUE_LIST

, then the legal value is a
whitespace-spearated list of values of the returned datatype.

**Parameters:**
- elementName

- the name of the element being queried.
- attrName

- the name of the attribute being queried.

**Returns:**
- one of the

DATATYPE_*

constants.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

---

#### boolean isAttributeRequired​(
String
elementName,

String
attrName)

Returns

true

if the named attribute must be
present within the named element.

**Parameters:**
- elementName

- the name of the element being queried.
- attrName

- the name of the attribute being queried.

**Returns:**
- true

if the attribute must be present.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

---

#### String
getAttributeDefaultValue​(
String
elementName,

String
attrName)

Returns the default value of the named attribute, if it is not
explicitly present within the named element, as a

String

, or

null

if no default value
is available.

**Parameters:**
- elementName

- the name of the element being queried.
- attrName

- the name of the attribute being queried.

**Returns:**
- a

String

containing the default value, or

null

.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

---

#### String
[] getAttributeEnumerations​(
String
elementName,

String
attrName)

Returns an array of

String

s containing the legal
enumerated values for the given attribute within the named
element. This method should only be called if

getAttributeValueType

returns

VALUE_ENUMERATION

.

**Parameters:**
- elementName

- the name of the element being queried.
- attrName

- the name of the attribute being queried.

**Returns:**
- an array of

String

s.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
- IllegalArgumentException

- if the given attribute is
not defined as an enumeration.

---

#### String
getAttributeMinValue​(
String
elementName,

String
attrName)

Returns the minimum legal value for the attribute. Whether
this value is inclusive or exclusive may be determined by the
value of

getAttributeValueType

. The value is
returned as a

String

; its interpretation is
dependent on the value of

getAttributeDataType

.
This method should only be called if

getAttributeValueType

returns

VALUE_RANGE_*

.

**Parameters:**
- elementName

- the name of the element being queried.
- attrName

- the name of the attribute being queried.

**Returns:**
- a

String

containing the smallest legal
value for the attribute.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
- IllegalArgumentException

- if the given attribute is
not defined as a range.

---

#### String
getAttributeMaxValue​(
String
elementName,

String
attrName)

Returns the maximum legal value for the attribute. Whether
this value is inclusive or exclusive may be determined by the
value of

getAttributeValueType

. The value is
returned as a

String

; its interpretation is
dependent on the value of

getAttributeDataType

.
This method should only be called if

getAttributeValueType

returns

VALUE_RANGE_*

.

**Parameters:**
- elementName

- the name of the element being queried, as a

String

.
- attrName

- the name of the attribute being queried.

**Returns:**
- a

String

containing the largest legal
value for the attribute.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
- IllegalArgumentException

- if the given attribute is
not defined as a range.

---

#### int getAttributeListMinLength​(
String
elementName,

String
attrName)

Returns the minimum number of list items that may be used to
define this attribute. The attribute itself is defined as a

String

containing multiple whitespace-separated
items. This method should only be called if

getAttributeValueType

returns

VALUE_LIST

.

**Parameters:**
- elementName

- the name of the element being queried.
- attrName

- the name of the attribute being queried.

**Returns:**
- the smallest legal number of list items for the
attribute.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
- IllegalArgumentException

- if the given attribute is
not defined as a list.

---

#### int getAttributeListMaxLength​(
String
elementName,

String
attrName)

Returns the maximum number of list items that may be used to
define this attribute. A value of

Integer.MAX_VALUE

may be used to specify that
there is no upper bound. The attribute itself is defined as a

String

containing multiple whitespace-separated
items. This method should only be called if

getAttributeValueType

returns

VALUE_LIST

.

**Parameters:**
- elementName

- the name of the element being queried.
- attrName

- the name of the attribute being queried.

**Returns:**
- the largest legal number of list items for the
attribute.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
- IllegalArgumentException

- if the given attribute is
not defined as a list.

---

#### String
getAttributeDescription​(
String
elementName,

String
attrName,

Locale
locale)

Returns a

String

containing a description of the
named attribute, or

null

. The description will be
localized for the supplied

Locale

if possible.

If

locale

is

null

, the current
default

Locale

returned by

Locale.getLocale

will be used.

**Parameters:**
- elementName

- the name of the element.
- attrName

- the name of the attribute.
- locale

- the

Locale

for which localization
will be attempted.

**Returns:**
- the attribute description.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.
- IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

---

#### int getObjectValueType​(
String
elementName)

Returns one of the enumerated values starting with

VALUE_

, indicating the type of values
(enumeration, range, or array) that are allowed for the

Object

reference. If no object value can be
stored within the given element, the result of this method will
be

VALUE_NONE

.

Object

references whose legal values are
defined as a range must implement the

Comparable

interface.

**Parameters:**
- elementName

- the name of the element being queried.

**Returns:**
- one of the

VALUE_*

constants.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.

**See Also:**
- Comparable

---

#### Class
<?> getObjectClass​(
String
elementName)

Returns the

Class

type of the

Object

reference stored within the element. If this element may not
contain an

Object

reference, an

IllegalArgumentException

will be thrown. If the
class type is an array, this field indicates the underlying
class type (

e.g

, for an array of

int

s, this
method would return

int.class

).

Object

references whose legal values are
defined as a range must implement the

Comparable

interface.

**Parameters:**
- elementName

- the name of the element being queried.

**Returns:**
- a

Class

object.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).

---

#### Object
getObjectDefaultValue​(
String
elementName)

Returns an

Object

s containing the default
value for the

Object

reference within
the named element.

**Parameters:**
- elementName

- the name of the element being queried.

**Returns:**
- an

Object

.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).

---

#### Object
[] getObjectEnumerations​(
String
elementName)

Returns an array of

Object

s containing the legal
enumerated values for the

Object

reference within
the named element. This method should only be called if

getObjectValueType

returns

VALUE_ENUMERATION

.

The

Object

associated with a node that accepts
enumerated values must be equal to one of the values returned by
this method, as defined by the

==

operator (as
opposed to the

Object.equals

method).

**Parameters:**
- elementName

- the name of the element being queried.

**Returns:**
- an array of

Object

s.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
- IllegalArgumentException

- if the

Object

is not defined as an enumeration.

---

#### Comparable
<?> getObjectMinValue​(
String
elementName)

Returns the minimum legal value for the

Object

reference within the named element. Whether this value is
inclusive or exclusive may be determined by the value of

getObjectValueType

. This method should only be
called if

getObjectValueType

returns one of the
constants starting with

VALUE_RANGE

.

**Parameters:**
- elementName

- the name of the element being queried.

**Returns:**
- the smallest legal value for the attribute.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
- IllegalArgumentException

- if the

Object

is not defined as a range.

---

#### Comparable
<?> getObjectMaxValue​(
String
elementName)

Returns the maximum legal value for the

Object

reference within the named element. Whether this value is
inclusive or exclusive may be determined by the value of

getObjectValueType

. This method should only be
called if

getObjectValueType

returns one of the
constants starting with

VALUE_RANGE

.

**Parameters:**
- elementName

- the name of the element being queried.

**Returns:**
- the smallest legal value for the attribute.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
- IllegalArgumentException

- if the

Object

is not defined as a range.

---

#### int getObjectArrayMinLength​(
String
elementName)

Returns the minimum number of array elements that may be used
to define the

Object

reference within the named
element. This method should only be called if

getObjectValueType

returns

VALUE_LIST

.

**Parameters:**
- elementName

- the name of the element being queried.

**Returns:**
- the smallest valid array length for the

Object

reference.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
- IllegalArgumentException

- if the

Object

is not
an array.

---

#### int getObjectArrayMaxLength​(
String
elementName)

Returns the maximum number of array elements that may be used
to define the

Object

reference within the named
element. A value of

Integer.MAX_VALUE

may be used
to specify that there is no upper bound. This method should
only be called if

getObjectValueType

returns

VALUE_LIST

.

**Parameters:**
- elementName

- the name of the element being queried.

**Returns:**
- the largest valid array length for the

Object

reference.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
- IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
- IllegalArgumentException

- if the

Object

is not
an array.

---

### Additional Sections

#### Interface IIOMetadataFormat

**All Known Implementing Classes:** IIOMetadataFormatImpl

```java
public interface
IIOMetadataFormat
```

An object describing the structure of metadata documents returned
from

IIOMetadata.getAsTree

and passed to

IIOMetadata.setFromTree

and

mergeTree

.
Document structures are described by a set of constraints on the
type and number of child elements that may belong to a given parent
element type, the names, types, and values of attributes that may
belong to an element, and the type and values of

Object

reference that may be stored at a node.

N.B: classes that implement this interface should contain a
method declared as

public static getInstance()

which
returns an instance of the class. Commonly, an implementation will
construct only a single instance and cache it for future
invocations of

getInstance

.

In the event that the plugin is provided as part of a named module,
that module must export the package containing the implementation class
to the

```java
java.desktop
```

module via a qualified export.
An unqualified export is not recommended unless also needed for
some other reason. Failing to export the package will result in
access failure at runtime.

The structures that may be described by this class are a subset
of those expressible using XML document type definitions (DTDs),
with the addition of some basic information on the datatypes of
attributes and the ability to store an

Object

reference within a node. In the future, XML Schemas could be used
to represent these structures, and many others.

The differences between

IIOMetadataFormat

-described structures and DTDs are as
follows:

- Elements may not contain text or mix text with embedded
tags.

The children of an element must conform to one of a few simple
patterns, described in the documentation for the

CHILD_*

constants;

The in-memory representation of an elements may contain a
reference to an

Object

. There is no provision for
representing such objects textually.

public interface

IIOMetadataFormat

An object describing the structure of metadata documents returned
from

IIOMetadata.getAsTree

and passed to

IIOMetadata.setFromTree

and

mergeTree

.
Document structures are described by a set of constraints on the
type and number of child elements that may belong to a given parent
element type, the names, types, and values of attributes that may
belong to an element, and the type and values of

Object

reference that may be stored at a node.

N.B: classes that implement this interface should contain a
method declared as

public static getInstance()

which
returns an instance of the class. Commonly, an implementation will
construct only a single instance and cache it for future
invocations of

getInstance

.

In the event that the plugin is provided as part of a named module,
that module must export the package containing the implementation class
to the

```java
java.desktop
```

module via a qualified export.
An unqualified export is not recommended unless also needed for
some other reason. Failing to export the package will result in
access failure at runtime.

The structures that may be described by this class are a subset
of those expressible using XML document type definitions (DTDs),
with the addition of some basic information on the datatypes of
attributes and the ability to store an

Object

reference within a node. In the future, XML Schemas could be used
to represent these structures, and many others.

The differences between

IIOMetadataFormat

-described structures and DTDs are as
follows:

- Elements may not contain text or mix text with embedded
tags.

The children of an element must conform to one of a few simple
patterns, described in the documentation for the

CHILD_*

constants;

The in-memory representation of an elements may contain a
reference to an

Object

. There is no provision for
representing such objects textually.

N.B: classes that implement this interface should contain a
method declared as

public static getInstance()

which
returns an instance of the class. Commonly, an implementation will
construct only a single instance and cache it for future
invocations of

getInstance

.

In the event that the plugin is provided as part of a named module,
that module must export the package containing the implementation class
to the

```java
java.desktop
```

module via a qualified export.
An unqualified export is not recommended unless also needed for
some other reason. Failing to export the package will result in
access failure at runtime.

The structures that may be described by this class are a subset
of those expressible using XML document type definitions (DTDs),
with the addition of some basic information on the datatypes of
attributes and the ability to store an

Object

reference within a node. In the future, XML Schemas could be used
to represent these structures, and many others.

The differences between

IIOMetadataFormat

-described structures and DTDs are as
follows:

- Elements may not contain text or mix text with embedded
tags.

The children of an element must conform to one of a few simple
patterns, described in the documentation for the

CHILD_*

constants;

The in-memory representation of an elements may contain a
reference to an

Object

. There is no provision for
representing such objects textually.

In the event that the plugin is provided as part of a named module,
that module must export the package containing the implementation class
to the

```java
java.desktop
```

module via a qualified export.
An unqualified export is not recommended unless also needed for
some other reason. Failing to export the package will result in
access failure at runtime.

The structures that may be described by this class are a subset
of those expressible using XML document type definitions (DTDs),
with the addition of some basic information on the datatypes of
attributes and the ability to store an

Object

reference within a node. In the future, XML Schemas could be used
to represent these structures, and many others.

The differences between

IIOMetadataFormat

-described structures and DTDs are as
follows:

- Elements may not contain text or mix text with embedded
tags.

The children of an element must conform to one of a few simple
patterns, described in the documentation for the

CHILD_*

constants;

The in-memory representation of an elements may contain a
reference to an

Object

. There is no provision for
representing such objects textually.

java.desktop

The structures that may be described by this class are a subset
of those expressible using XML document type definitions (DTDs),
with the addition of some basic information on the datatypes of
attributes and the ability to store an

Object

reference within a node. In the future, XML Schemas could be used
to represent these structures, and many others.

The differences between

IIOMetadataFormat

-described structures and DTDs are as
follows:

- Elements may not contain text or mix text with embedded
tags.

The children of an element must conform to one of a few simple
patterns, described in the documentation for the

CHILD_*

constants;

The in-memory representation of an elements may contain a
reference to an

Object

. There is no provision for
representing such objects textually.

The differences between

IIOMetadataFormat

-described structures and DTDs are as
follows:

- Elements may not contain text or mix text with embedded
tags.

The children of an element must conform to one of a few simple
patterns, described in the documentation for the

CHILD_*

constants;

The in-memory representation of an elements may contain a
reference to an

Object

. There is no provision for
representing such objects textually.

Elements may not contain text or mix text with embedded
tags.

The children of an element must conform to one of a few simple
patterns, described in the documentation for the

CHILD_*

constants;

The in-memory representation of an elements may contain a
reference to an

Object

. There is no provision for
representing such objects textually.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

CHILD_POLICY_ALL

A constant returned by

getChildPolicy

to indicate
that an element must have a single instance of each of its
legal child elements, in order.

static int

CHILD_POLICY_CHOICE

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one children, selected from
among its legal child elements.

static int

CHILD_POLICY_EMPTY

A constant returned by

getChildPolicy

to indicate
that an element may not have any children.

static int

CHILD_POLICY_MAX

The largest valid

CHILD_POLICY_*

constant,
to be used for range checks.

static int

CHILD_POLICY_REPEAT

A constant returned by

getChildPolicy

to indicate
that an element must have zero or more instances of its unique
legal child element.

static int

CHILD_POLICY_SEQUENCE

A constant returned by

getChildPolicy

to indicate
that an element must have a sequence of instances of any of its
legal child elements.

static int

CHILD_POLICY_SOME

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one instance of each of its
legal child elements, in order.

static int

DATATYPE_BOOLEAN

A constant returned by

getAttributeDataType

indicating that the value of an attribute is one of the boolean
values 'true' or 'false'.

static int

DATATYPE_DOUBLE

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a double-precision decimal floating-point
number.

static int

DATATYPE_FLOAT

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a decimal floating-point number.

static int

DATATYPE_INTEGER

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of an integer.

static int

DATATYPE_STRING

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a general Unicode
string.

static int

VALUE_ARBITRARY

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a single, arbitrary value.

static int

VALUE_ENUMERATION

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set one of a number of enumerated values.

static int

VALUE_LIST

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a list or array of values.

static int

VALUE_NONE

A constant returned by

getObjectValueType

to
indicate the absence of a user object.

static int

VALUE_RANGE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values.

static int

VALUE_RANGE_MAX_INCLUSIVE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values.

static int

VALUE_RANGE_MAX_INCLUSIVE_MASK

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MAX_INCLUSIVE

, and with

VALUE_RANGE_MIN_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

static int

VALUE_RANGE_MIN_INCLUSIVE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values.

static int

VALUE_RANGE_MIN_INCLUSIVE_MASK

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MIN_INCLUSIVE

, and with

VALUE_RANGE_MAX_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

static int

VALUE_RANGE_MIN_MAX_INCLUSIVE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

canNodeAppear

​(

String

elementName,

ImageTypeSpecifier

imageType)

Returns

true

if the element (and the subtree below
it) is allowed to appear in a metadata document for an image of
the given type, defined by an

ImageTypeSpecifier

.

int

getAttributeDataType

​(

String

elementName,

String

attrName)

Returns one of the constants starting with

DATATYPE_

, indicating the format and
interpretation of the value of the given attribute within the
named element.

String

getAttributeDefaultValue

​(

String

elementName,

String

attrName)

Returns the default value of the named attribute, if it is not
explicitly present within the named element, as a

String

, or

null

if no default value
is available.

String

getAttributeDescription

​(

String

elementName,

String

attrName,

Locale

locale)

Returns a

String

containing a description of the
named attribute, or

null

.

String

[]

getAttributeEnumerations

​(

String

elementName,

String

attrName)

Returns an array of

String

s containing the legal
enumerated values for the given attribute within the named
element.

int

getAttributeListMaxLength

​(

String

elementName,

String

attrName)

Returns the maximum number of list items that may be used to
define this attribute.

int

getAttributeListMinLength

​(

String

elementName,

String

attrName)

Returns the minimum number of list items that may be used to
define this attribute.

String

getAttributeMaxValue

​(

String

elementName,

String

attrName)

Returns the maximum legal value for the attribute.

String

getAttributeMinValue

​(

String

elementName,

String

attrName)

Returns the minimum legal value for the attribute.

String

[]

getAttributeNames

​(

String

elementName)

Returns an array of

String

s listing the names of
the attributes that may be associated with the named element.

int

getAttributeValueType

​(

String

elementName,

String

attrName)

Returns one of the constants starting with

VALUE_

,
indicating whether the values of the given attribute within the
named element are arbitrary, constrained to lie within a
specified range, constrained to be one of a set of enumerated
values, or are a whitespace-separated list of arbitrary values.

String

[]

getChildNames

​(

String

elementName)

Returns an array of

String

s indicating the names
of the element which are allowed to be children of the named
element, in the order in which they should appear.

int

getChildPolicy

​(

String

elementName)

Returns one of the constants starting with

CHILD_POLICY_

, indicating the legal pattern of
children for the named element.

String

getElementDescription

​(

String

elementName,

Locale

locale)

Returns a

String

containing a description of the
named element, or

null

.

int

getElementMaxChildren

​(

String

elementName)

Returns the maximum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

.

int

getElementMinChildren

​(

String

elementName)

Returns the minimum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

.

int

getObjectArrayMaxLength

​(

String

elementName)

Returns the maximum number of array elements that may be used
to define the

Object

reference within the named
element.

int

getObjectArrayMinLength

​(

String

elementName)

Returns the minimum number of array elements that may be used
to define the

Object

reference within the named
element.

Class

<?>

getObjectClass

​(

String

elementName)

Returns the

Class

type of the

Object

reference stored within the element.

Object

getObjectDefaultValue

​(

String

elementName)

Returns an

Object

s containing the default
value for the

Object

reference within
the named element.

Object

[]

getObjectEnumerations

​(

String

elementName)

Returns an array of

Object

s containing the legal
enumerated values for the

Object

reference within
the named element.

Comparable

<?>

getObjectMaxValue

​(

String

elementName)

Returns the maximum legal value for the

Object

reference within the named element.

Comparable

<?>

getObjectMinValue

​(

String

elementName)

Returns the minimum legal value for the

Object

reference within the named element.

int

getObjectValueType

​(

String

elementName)

Returns one of the enumerated values starting with

VALUE_

, indicating the type of values
(enumeration, range, or array) that are allowed for the

Object

reference.

String

getRootName

()

Returns the name of the root element of the format.

boolean

isAttributeRequired

​(

String

elementName,

String

attrName)

Returns

true

if the named attribute must be
present within the named element.

Field Summary

Fields

Modifier and Type

Field

Description

static int

CHILD_POLICY_ALL

A constant returned by

getChildPolicy

to indicate
that an element must have a single instance of each of its
legal child elements, in order.

static int

CHILD_POLICY_CHOICE

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one children, selected from
among its legal child elements.

static int

CHILD_POLICY_EMPTY

A constant returned by

getChildPolicy

to indicate
that an element may not have any children.

static int

CHILD_POLICY_MAX

The largest valid

CHILD_POLICY_*

constant,
to be used for range checks.

static int

CHILD_POLICY_REPEAT

A constant returned by

getChildPolicy

to indicate
that an element must have zero or more instances of its unique
legal child element.

static int

CHILD_POLICY_SEQUENCE

A constant returned by

getChildPolicy

to indicate
that an element must have a sequence of instances of any of its
legal child elements.

static int

CHILD_POLICY_SOME

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one instance of each of its
legal child elements, in order.

static int

DATATYPE_BOOLEAN

A constant returned by

getAttributeDataType

indicating that the value of an attribute is one of the boolean
values 'true' or 'false'.

static int

DATATYPE_DOUBLE

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a double-precision decimal floating-point
number.

static int

DATATYPE_FLOAT

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a decimal floating-point number.

static int

DATATYPE_INTEGER

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of an integer.

static int

DATATYPE_STRING

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a general Unicode
string.

static int

VALUE_ARBITRARY

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a single, arbitrary value.

static int

VALUE_ENUMERATION

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set one of a number of enumerated values.

static int

VALUE_LIST

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a list or array of values.

static int

VALUE_NONE

A constant returned by

getObjectValueType

to
indicate the absence of a user object.

static int

VALUE_RANGE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values.

static int

VALUE_RANGE_MAX_INCLUSIVE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values.

static int

VALUE_RANGE_MAX_INCLUSIVE_MASK

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MAX_INCLUSIVE

, and with

VALUE_RANGE_MIN_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

static int

VALUE_RANGE_MIN_INCLUSIVE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values.

static int

VALUE_RANGE_MIN_INCLUSIVE_MASK

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MIN_INCLUSIVE

, and with

VALUE_RANGE_MAX_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

static int

VALUE_RANGE_MIN_MAX_INCLUSIVE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values.

---

#### Field Summary

A constant returned by

getChildPolicy

to indicate
that an element must have a single instance of each of its
legal child elements, in order.

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one children, selected from
among its legal child elements.

A constant returned by

getChildPolicy

to indicate
that an element may not have any children.

The largest valid

CHILD_POLICY_*

constant,
to be used for range checks.

A constant returned by

getChildPolicy

to indicate
that an element must have zero or more instances of its unique
legal child element.

A constant returned by

getChildPolicy

to indicate
that an element must have a sequence of instances of any of its
legal child elements.

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one instance of each of its
legal child elements, in order.

A constant returned by

getAttributeDataType

indicating that the value of an attribute is one of the boolean
values 'true' or 'false'.

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a double-precision decimal floating-point
number.

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a decimal floating-point number.

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of an integer.

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a general Unicode
string.

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a single, arbitrary value.

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set one of a number of enumerated values.

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a list or array of values.

A constant returned by

getObjectValueType

to
indicate the absence of a user object.

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values.

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values.

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MAX_INCLUSIVE

, and with

VALUE_RANGE_MIN_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MIN_INCLUSIVE

, and with

VALUE_RANGE_MAX_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

canNodeAppear

​(

String

elementName,

ImageTypeSpecifier

imageType)

Returns

true

if the element (and the subtree below
it) is allowed to appear in a metadata document for an image of
the given type, defined by an

ImageTypeSpecifier

.

int

getAttributeDataType

​(

String

elementName,

String

attrName)

Returns one of the constants starting with

DATATYPE_

, indicating the format and
interpretation of the value of the given attribute within the
named element.

String

getAttributeDefaultValue

​(

String

elementName,

String

attrName)

Returns the default value of the named attribute, if it is not
explicitly present within the named element, as a

String

, or

null

if no default value
is available.

String

getAttributeDescription

​(

String

elementName,

String

attrName,

Locale

locale)

Returns a

String

containing a description of the
named attribute, or

null

.

String

[]

getAttributeEnumerations

​(

String

elementName,

String

attrName)

Returns an array of

String

s containing the legal
enumerated values for the given attribute within the named
element.

int

getAttributeListMaxLength

​(

String

elementName,

String

attrName)

Returns the maximum number of list items that may be used to
define this attribute.

int

getAttributeListMinLength

​(

String

elementName,

String

attrName)

Returns the minimum number of list items that may be used to
define this attribute.

String

getAttributeMaxValue

​(

String

elementName,

String

attrName)

Returns the maximum legal value for the attribute.

String

getAttributeMinValue

​(

String

elementName,

String

attrName)

Returns the minimum legal value for the attribute.

String

[]

getAttributeNames

​(

String

elementName)

Returns an array of

String

s listing the names of
the attributes that may be associated with the named element.

int

getAttributeValueType

​(

String

elementName,

String

attrName)

Returns one of the constants starting with

VALUE_

,
indicating whether the values of the given attribute within the
named element are arbitrary, constrained to lie within a
specified range, constrained to be one of a set of enumerated
values, or are a whitespace-separated list of arbitrary values.

String

[]

getChildNames

​(

String

elementName)

Returns an array of

String

s indicating the names
of the element which are allowed to be children of the named
element, in the order in which they should appear.

int

getChildPolicy

​(

String

elementName)

Returns one of the constants starting with

CHILD_POLICY_

, indicating the legal pattern of
children for the named element.

String

getElementDescription

​(

String

elementName,

Locale

locale)

Returns a

String

containing a description of the
named element, or

null

.

int

getElementMaxChildren

​(

String

elementName)

Returns the maximum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

.

int

getElementMinChildren

​(

String

elementName)

Returns the minimum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

.

int

getObjectArrayMaxLength

​(

String

elementName)

Returns the maximum number of array elements that may be used
to define the

Object

reference within the named
element.

int

getObjectArrayMinLength

​(

String

elementName)

Returns the minimum number of array elements that may be used
to define the

Object

reference within the named
element.

Class

<?>

getObjectClass

​(

String

elementName)

Returns the

Class

type of the

Object

reference stored within the element.

Object

getObjectDefaultValue

​(

String

elementName)

Returns an

Object

s containing the default
value for the

Object

reference within
the named element.

Object

[]

getObjectEnumerations

​(

String

elementName)

Returns an array of

Object

s containing the legal
enumerated values for the

Object

reference within
the named element.

Comparable

<?>

getObjectMaxValue

​(

String

elementName)

Returns the maximum legal value for the

Object

reference within the named element.

Comparable

<?>

getObjectMinValue

​(

String

elementName)

Returns the minimum legal value for the

Object

reference within the named element.

int

getObjectValueType

​(

String

elementName)

Returns one of the enumerated values starting with

VALUE_

, indicating the type of values
(enumeration, range, or array) that are allowed for the

Object

reference.

String

getRootName

()

Returns the name of the root element of the format.

boolean

isAttributeRequired

​(

String

elementName,

String

attrName)

Returns

true

if the named attribute must be
present within the named element.

---

#### Method Summary

Returns

true

if the element (and the subtree below
it) is allowed to appear in a metadata document for an image of
the given type, defined by an

ImageTypeSpecifier

.

Returns one of the constants starting with

DATATYPE_

, indicating the format and
interpretation of the value of the given attribute within the
named element.

Returns the default value of the named attribute, if it is not
explicitly present within the named element, as a

String

, or

null

if no default value
is available.

Returns a

String

containing a description of the
named attribute, or

null

.

Returns an array of

String

s containing the legal
enumerated values for the given attribute within the named
element.

Returns the maximum number of list items that may be used to
define this attribute.

Returns the minimum number of list items that may be used to
define this attribute.

Returns the maximum legal value for the attribute.

Returns the minimum legal value for the attribute.

Returns an array of

String

s listing the names of
the attributes that may be associated with the named element.

Returns one of the constants starting with

VALUE_

,
indicating whether the values of the given attribute within the
named element are arbitrary, constrained to lie within a
specified range, constrained to be one of a set of enumerated
values, or are a whitespace-separated list of arbitrary values.

Returns an array of

String

s indicating the names
of the element which are allowed to be children of the named
element, in the order in which they should appear.

Returns one of the constants starting with

CHILD_POLICY_

, indicating the legal pattern of
children for the named element.

Returns a

String

containing a description of the
named element, or

null

.

Returns the maximum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

.

Returns the minimum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

.

Returns the maximum number of array elements that may be used
to define the

Object

reference within the named
element.

Returns the minimum number of array elements that may be used
to define the

Object

reference within the named
element.

Returns the

Class

type of the

Object

reference stored within the element.

Returns an

Object

s containing the default
value for the

Object

reference within
the named element.

Returns an array of

Object

s containing the legal
enumerated values for the

Object

reference within
the named element.

Returns the maximum legal value for the

Object

reference within the named element.

Returns the minimum legal value for the

Object

reference within the named element.

Returns one of the enumerated values starting with

VALUE_

, indicating the type of values
(enumeration, range, or array) that are allowed for the

Object

reference.

Returns the name of the root element of the format.

Returns

true

if the named attribute must be
present within the named element.

============ FIELD DETAIL ===========

- Field Detail

- CHILD_POLICY_EMPTY

```java
static final int CHILD_POLICY_EMPTY
```

A constant returned by

getChildPolicy

to indicate
that an element may not have any children. In other words, it
is required to be a leaf node.

**See Also:** Constant Field Values

- CHILD_POLICY_ALL

```java
static final int CHILD_POLICY_ALL
```

A constant returned by

getChildPolicy

to indicate
that an element must have a single instance of each of its
legal child elements, in order. In DTD terms, the contents of
the element are defined by a sequence

a,b,c,d,...

.

**See Also:** Constant Field Values

- CHILD_POLICY_SOME

```java
static final int CHILD_POLICY_SOME
```

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one instance of each of its
legal child elements, in order. In DTD terms, the contents of
the element are defined by a sequence

a?,b?,c?,d?,...

.

**See Also:** Constant Field Values

- CHILD_POLICY_CHOICE

```java
static final int CHILD_POLICY_CHOICE
```

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one children, selected from
among its legal child elements. In DTD terms, the contents of
the element are defined by a selection

a|b|c|d|...

.

**See Also:** Constant Field Values

- CHILD_POLICY_SEQUENCE

```java
static final int CHILD_POLICY_SEQUENCE
```

A constant returned by

getChildPolicy

to indicate
that an element must have a sequence of instances of any of its
legal child elements. In DTD terms, the contents of the
element are defined by a sequence

(a|b|c|d|...)*

.

**See Also:** Constant Field Values

- CHILD_POLICY_REPEAT

```java
static final int CHILD_POLICY_REPEAT
```

A constant returned by

getChildPolicy

to indicate
that an element must have zero or more instances of its unique
legal child element. In DTD terms, the contents of the element
are defined by a starred expression

a*

.

**See Also:** Constant Field Values

- CHILD_POLICY_MAX

```java
static final int CHILD_POLICY_MAX
```

The largest valid

CHILD_POLICY_*

constant,
to be used for range checks.

**See Also:** Constant Field Values

- VALUE_NONE

```java
static final int VALUE_NONE
```

A constant returned by

getObjectValueType

to
indicate the absence of a user object.

**See Also:** Constant Field Values

- VALUE_ARBITRARY

```java
static final int VALUE_ARBITRARY
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a single, arbitrary value.

**See Also:** Constant Field Values

- VALUE_RANGE

```java
static final int VALUE_RANGE
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values. Both the minimum
and maximum values of the range are exclusive. It is
recommended that ranges of integers be inclusive on both ends,
and that exclusive ranges be used only for floating-point data.

**See Also:** VALUE_RANGE_MIN_MAX_INCLUSIVE

,

Constant Field Values

- VALUE_RANGE_MIN_INCLUSIVE_MASK

```java
static final int VALUE_RANGE_MIN_INCLUSIVE_MASK
```

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MIN_INCLUSIVE

, and with

VALUE_RANGE_MAX_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

Similarly, the value may be and'ed with the value of

getAttributeValueType

or

getObjectValueType

to determine if the minimum
value of the range is inclusive.

**See Also:** Constant Field Values

- VALUE_RANGE_MAX_INCLUSIVE_MASK

```java
static final int VALUE_RANGE_MAX_INCLUSIVE_MASK
```

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MAX_INCLUSIVE

, and with

VALUE_RANGE_MIN_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

Similarly, the value may be and'ed with the value of

getAttributeValueType

or

getObjectValueType

to determine if the maximum
value of the range is inclusive.

**See Also:** Constant Field Values

- VALUE_RANGE_MIN_INCLUSIVE

```java
static final int VALUE_RANGE_MIN_INCLUSIVE
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values. The minimum
(but not the maximum) value of the range is inclusive.

**See Also:** Constant Field Values

- VALUE_RANGE_MAX_INCLUSIVE

```java
static final int VALUE_RANGE_MAX_INCLUSIVE
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values. The maximum
(but not the minimum) value of the range is inclusive.

**See Also:** Constant Field Values

- VALUE_RANGE_MIN_MAX_INCLUSIVE

```java
static final int VALUE_RANGE_MIN_MAX_INCLUSIVE
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values. Both the minimum
and maximum values of the range are inclusive. It is
recommended that ranges of integers be inclusive on both ends,
and that exclusive ranges be used only for floating-point data.

**See Also:** Constant Field Values

- VALUE_ENUMERATION

```java
static final int VALUE_ENUMERATION
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set one of a number of enumerated values.
In the case of attributes, these values are

String

s; for objects, they are

Object

s implementing a given class or interface.

Attribute values of type

DATATYPE_BOOLEAN

should be marked as enumerations.

**See Also:** Constant Field Values

- VALUE_LIST

```java
static final int VALUE_LIST
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a list or array of values. In the
case of attributes, the list will consist of
whitespace-separated values within a

String

; for
objects, an array will be used.

**See Also:** Constant Field Values

- DATATYPE_STRING

```java
static final int DATATYPE_STRING
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a general Unicode
string.

**See Also:** Constant Field Values

- DATATYPE_BOOLEAN

```java
static final int DATATYPE_BOOLEAN
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is one of the boolean
values 'true' or 'false'.
Attribute values of type DATATYPE_BOOLEAN should be marked as
enumerations, and the permitted values should be the string
literal values "TRUE" or "FALSE", although a plugin may also
recognise lower or mixed case equivalents.

**See Also:** Constant Field Values

- DATATYPE_INTEGER

```java
static final int DATATYPE_INTEGER
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of an integer.

**See Also:** Constant Field Values

- DATATYPE_FLOAT

```java
static final int DATATYPE_FLOAT
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a decimal floating-point number.

**See Also:** Constant Field Values

- DATATYPE_DOUBLE

```java
static final int DATATYPE_DOUBLE
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a double-precision decimal floating-point
number.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getRootName

```java
String
getRootName()
```

Returns the name of the root element of the format.

**Returns:** a

String

.

- canNodeAppear

```java
boolean canNodeAppear​(
String
elementName,

ImageTypeSpecifier
imageType)
```

Returns

true

if the element (and the subtree below
it) is allowed to appear in a metadata document for an image of
the given type, defined by an

ImageTypeSpecifier

.
For example, a metadata document format might contain an
element that describes the primary colors of the image, which
would not be allowed when writing a grayscale image.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** imageType

- an

ImageTypeSpecifier

indicating
the type of the image that will be associated with the
metadata.
**Returns:** true

if the node is meaningful for images
of the given type.

- getElementMinChildren

```java
int getElementMinChildren​(
String
elementName)
```

Returns the minimum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

. For
example, an element representing color primary information
might be required to have at least 3 children, one for each
primary.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an

int

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element does
not have a child policy of

CHILD_POLICY_REPEAT

.

- getElementMaxChildren

```java
int getElementMaxChildren​(
String
elementName)
```

Returns the maximum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

. For
example, an element representing an entry in an 8-bit color
palette might be allowed to repeat up to 256 times. A value of

Integer.MAX_VALUE

may be used to specify that
there is no upper bound.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an

int

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element does
not have a child policy of

CHILD_POLICY_REPEAT

.

- getElementDescription

```java
String
getElementDescription​(
String
elementName,

Locale
locale)
```

Returns a

String

containing a description of the
named element, or

null

. The description will be
localized for the supplied

Locale

if possible.

If

locale

is

null

, the current
default

Locale

returned by

Locale.getLocale

will be used.

**Parameters:** elementName

- the name of the element.
**Parameters:** locale

- the

Locale

for which localization
will be attempted.
**Returns:** the element description.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.

- getChildPolicy

```java
int getChildPolicy​(
String
elementName)
```

Returns one of the constants starting with

CHILD_POLICY_

, indicating the legal pattern of
children for the named element.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** one of the

CHILD_POLICY_*

constants.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.

- getChildNames

```java
String
[] getChildNames​(
String
elementName)
```

Returns an array of

String

s indicating the names
of the element which are allowed to be children of the named
element, in the order in which they should appear. If the
element cannot have children,

null

is returned.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an array of

String

s, or null.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.

- getAttributeNames

```java
String
[] getAttributeNames​(
String
elementName)
```

Returns an array of

String

s listing the names of
the attributes that may be associated with the named element.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an array of

String

s.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.

- getAttributeValueType

```java
int getAttributeValueType​(
String
elementName,

String
attrName)
```

Returns one of the constants starting with

VALUE_

,
indicating whether the values of the given attribute within the
named element are arbitrary, constrained to lie within a
specified range, constrained to be one of a set of enumerated
values, or are a whitespace-separated list of arbitrary values.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** one of the

VALUE_*

constants.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

- getAttributeDataType

```java
int getAttributeDataType​(
String
elementName,

String
attrName)
```

Returns one of the constants starting with

DATATYPE_

, indicating the format and
interpretation of the value of the given attribute within the
named element. If

getAttributeValueType

returns

VALUE_LIST

, then the legal value is a
whitespace-spearated list of values of the returned datatype.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** one of the

DATATYPE_*

constants.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

- isAttributeRequired

```java
boolean isAttributeRequired​(
String
elementName,

String
attrName)
```

Returns

true

if the named attribute must be
present within the named element.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** true

if the attribute must be present.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

- getAttributeDefaultValue

```java
String
getAttributeDefaultValue​(
String
elementName,

String
attrName)
```

Returns the default value of the named attribute, if it is not
explicitly present within the named element, as a

String

, or

null

if no default value
is available.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** a

String

containing the default value, or

null

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

- getAttributeEnumerations

```java
String
[] getAttributeEnumerations​(
String
elementName,

String
attrName)
```

Returns an array of

String

s containing the legal
enumerated values for the given attribute within the named
element. This method should only be called if

getAttributeValueType

returns

VALUE_ENUMERATION

.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** an array of

String

s.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as an enumeration.

- getAttributeMinValue

```java
String
getAttributeMinValue​(
String
elementName,

String
attrName)
```

Returns the minimum legal value for the attribute. Whether
this value is inclusive or exclusive may be determined by the
value of

getAttributeValueType

. The value is
returned as a

String

; its interpretation is
dependent on the value of

getAttributeDataType

.
This method should only be called if

getAttributeValueType

returns

VALUE_RANGE_*

.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** a

String

containing the smallest legal
value for the attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as a range.

- getAttributeMaxValue

```java
String
getAttributeMaxValue​(
String
elementName,

String
attrName)
```

Returns the maximum legal value for the attribute. Whether
this value is inclusive or exclusive may be determined by the
value of

getAttributeValueType

. The value is
returned as a

String

; its interpretation is
dependent on the value of

getAttributeDataType

.
This method should only be called if

getAttributeValueType

returns

VALUE_RANGE_*

.

**Parameters:** elementName

- the name of the element being queried, as a

String

.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** a

String

containing the largest legal
value for the attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as a range.

- getAttributeListMinLength

```java
int getAttributeListMinLength​(
String
elementName,

String
attrName)
```

Returns the minimum number of list items that may be used to
define this attribute. The attribute itself is defined as a

String

containing multiple whitespace-separated
items. This method should only be called if

getAttributeValueType

returns

VALUE_LIST

.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** the smallest legal number of list items for the
attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as a list.

- getAttributeListMaxLength

```java
int getAttributeListMaxLength​(
String
elementName,

String
attrName)
```

Returns the maximum number of list items that may be used to
define this attribute. A value of

Integer.MAX_VALUE

may be used to specify that
there is no upper bound. The attribute itself is defined as a

String

containing multiple whitespace-separated
items. This method should only be called if

getAttributeValueType

returns

VALUE_LIST

.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** the largest legal number of list items for the
attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as a list.

- getAttributeDescription

```java
String
getAttributeDescription​(
String
elementName,

String
attrName,

Locale
locale)
```

Returns a

String

containing a description of the
named attribute, or

null

. The description will be
localized for the supplied

Locale

if possible.

If

locale

is

null

, the current
default

Locale

returned by

Locale.getLocale

will be used.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute.
**Parameters:** locale

- the

Locale

for which localization
will be attempted.
**Returns:** the attribute description.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

- getObjectValueType

```java
int getObjectValueType​(
String
elementName)
```

Returns one of the enumerated values starting with

VALUE_

, indicating the type of values
(enumeration, range, or array) that are allowed for the

Object

reference. If no object value can be
stored within the given element, the result of this method will
be

VALUE_NONE

.

Object

references whose legal values are
defined as a range must implement the

Comparable

interface.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** one of the

VALUE_*

constants.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**See Also:** Comparable

- getObjectClass

```java
Class
<?> getObjectClass​(
String
elementName)
```

Returns the

Class

type of the

Object

reference stored within the element. If this element may not
contain an

Object

reference, an

IllegalArgumentException

will be thrown. If the
class type is an array, this field indicates the underlying
class type (

e.g

, for an array of

int

s, this
method would return

int.class

).

Object

references whose legal values are
defined as a range must implement the

Comparable

interface.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** a

Class

object.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).

- getObjectDefaultValue

```java
Object
getObjectDefaultValue​(
String
elementName)
```

Returns an

Object

s containing the default
value for the

Object

reference within
the named element.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an

Object

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).

- getObjectEnumerations

```java
Object
[] getObjectEnumerations​(
String
elementName)
```

Returns an array of

Object

s containing the legal
enumerated values for the

Object

reference within
the named element. This method should only be called if

getObjectValueType

returns

VALUE_ENUMERATION

.

The

Object

associated with a node that accepts
enumerated values must be equal to one of the values returned by
this method, as defined by the

==

operator (as
opposed to the

Object.equals

method).

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an array of

Object

s.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not defined as an enumeration.

- getObjectMinValue

```java
Comparable
<?> getObjectMinValue​(
String
elementName)
```

Returns the minimum legal value for the

Object

reference within the named element. Whether this value is
inclusive or exclusive may be determined by the value of

getObjectValueType

. This method should only be
called if

getObjectValueType

returns one of the
constants starting with

VALUE_RANGE

.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** the smallest legal value for the attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not defined as a range.

- getObjectMaxValue

```java
Comparable
<?> getObjectMaxValue​(
String
elementName)
```

Returns the maximum legal value for the

Object

reference within the named element. Whether this value is
inclusive or exclusive may be determined by the value of

getObjectValueType

. This method should only be
called if

getObjectValueType

returns one of the
constants starting with

VALUE_RANGE

.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** the smallest legal value for the attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not defined as a range.

- getObjectArrayMinLength

```java
int getObjectArrayMinLength​(
String
elementName)
```

Returns the minimum number of array elements that may be used
to define the

Object

reference within the named
element. This method should only be called if

getObjectValueType

returns

VALUE_LIST

.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** the smallest valid array length for the

Object

reference.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not
an array.

- getObjectArrayMaxLength

```java
int getObjectArrayMaxLength​(
String
elementName)
```

Returns the maximum number of array elements that may be used
to define the

Object

reference within the named
element. A value of

Integer.MAX_VALUE

may be used
to specify that there is no upper bound. This method should
only be called if

getObjectValueType

returns

VALUE_LIST

.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** the largest valid array length for the

Object

reference.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not
an array.

Field Detail

- CHILD_POLICY_EMPTY

```java
static final int CHILD_POLICY_EMPTY
```

A constant returned by

getChildPolicy

to indicate
that an element may not have any children. In other words, it
is required to be a leaf node.

**See Also:** Constant Field Values

- CHILD_POLICY_ALL

```java
static final int CHILD_POLICY_ALL
```

A constant returned by

getChildPolicy

to indicate
that an element must have a single instance of each of its
legal child elements, in order. In DTD terms, the contents of
the element are defined by a sequence

a,b,c,d,...

.

**See Also:** Constant Field Values

- CHILD_POLICY_SOME

```java
static final int CHILD_POLICY_SOME
```

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one instance of each of its
legal child elements, in order. In DTD terms, the contents of
the element are defined by a sequence

a?,b?,c?,d?,...

.

**See Also:** Constant Field Values

- CHILD_POLICY_CHOICE

```java
static final int CHILD_POLICY_CHOICE
```

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one children, selected from
among its legal child elements. In DTD terms, the contents of
the element are defined by a selection

a|b|c|d|...

.

**See Also:** Constant Field Values

- CHILD_POLICY_SEQUENCE

```java
static final int CHILD_POLICY_SEQUENCE
```

A constant returned by

getChildPolicy

to indicate
that an element must have a sequence of instances of any of its
legal child elements. In DTD terms, the contents of the
element are defined by a sequence

(a|b|c|d|...)*

.

**See Also:** Constant Field Values

- CHILD_POLICY_REPEAT

```java
static final int CHILD_POLICY_REPEAT
```

A constant returned by

getChildPolicy

to indicate
that an element must have zero or more instances of its unique
legal child element. In DTD terms, the contents of the element
are defined by a starred expression

a*

.

**See Also:** Constant Field Values

- CHILD_POLICY_MAX

```java
static final int CHILD_POLICY_MAX
```

The largest valid

CHILD_POLICY_*

constant,
to be used for range checks.

**See Also:** Constant Field Values

- VALUE_NONE

```java
static final int VALUE_NONE
```

A constant returned by

getObjectValueType

to
indicate the absence of a user object.

**See Also:** Constant Field Values

- VALUE_ARBITRARY

```java
static final int VALUE_ARBITRARY
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a single, arbitrary value.

**See Also:** Constant Field Values

- VALUE_RANGE

```java
static final int VALUE_RANGE
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values. Both the minimum
and maximum values of the range are exclusive. It is
recommended that ranges of integers be inclusive on both ends,
and that exclusive ranges be used only for floating-point data.

**See Also:** VALUE_RANGE_MIN_MAX_INCLUSIVE

,

Constant Field Values

- VALUE_RANGE_MIN_INCLUSIVE_MASK

```java
static final int VALUE_RANGE_MIN_INCLUSIVE_MASK
```

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MIN_INCLUSIVE

, and with

VALUE_RANGE_MAX_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

Similarly, the value may be and'ed with the value of

getAttributeValueType

or

getObjectValueType

to determine if the minimum
value of the range is inclusive.

**See Also:** Constant Field Values

- VALUE_RANGE_MAX_INCLUSIVE_MASK

```java
static final int VALUE_RANGE_MAX_INCLUSIVE_MASK
```

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MAX_INCLUSIVE

, and with

VALUE_RANGE_MIN_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

Similarly, the value may be and'ed with the value of

getAttributeValueType

or

getObjectValueType

to determine if the maximum
value of the range is inclusive.

**See Also:** Constant Field Values

- VALUE_RANGE_MIN_INCLUSIVE

```java
static final int VALUE_RANGE_MIN_INCLUSIVE
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values. The minimum
(but not the maximum) value of the range is inclusive.

**See Also:** Constant Field Values

- VALUE_RANGE_MAX_INCLUSIVE

```java
static final int VALUE_RANGE_MAX_INCLUSIVE
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values. The maximum
(but not the minimum) value of the range is inclusive.

**See Also:** Constant Field Values

- VALUE_RANGE_MIN_MAX_INCLUSIVE

```java
static final int VALUE_RANGE_MIN_MAX_INCLUSIVE
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values. Both the minimum
and maximum values of the range are inclusive. It is
recommended that ranges of integers be inclusive on both ends,
and that exclusive ranges be used only for floating-point data.

**See Also:** Constant Field Values

- VALUE_ENUMERATION

```java
static final int VALUE_ENUMERATION
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set one of a number of enumerated values.
In the case of attributes, these values are

String

s; for objects, they are

Object

s implementing a given class or interface.

Attribute values of type

DATATYPE_BOOLEAN

should be marked as enumerations.

**See Also:** Constant Field Values

- VALUE_LIST

```java
static final int VALUE_LIST
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a list or array of values. In the
case of attributes, the list will consist of
whitespace-separated values within a

String

; for
objects, an array will be used.

**See Also:** Constant Field Values

- DATATYPE_STRING

```java
static final int DATATYPE_STRING
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a general Unicode
string.

**See Also:** Constant Field Values

- DATATYPE_BOOLEAN

```java
static final int DATATYPE_BOOLEAN
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is one of the boolean
values 'true' or 'false'.
Attribute values of type DATATYPE_BOOLEAN should be marked as
enumerations, and the permitted values should be the string
literal values "TRUE" or "FALSE", although a plugin may also
recognise lower or mixed case equivalents.

**See Also:** Constant Field Values

- DATATYPE_INTEGER

```java
static final int DATATYPE_INTEGER
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of an integer.

**See Also:** Constant Field Values

- DATATYPE_FLOAT

```java
static final int DATATYPE_FLOAT
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a decimal floating-point number.

**See Also:** Constant Field Values

- DATATYPE_DOUBLE

```java
static final int DATATYPE_DOUBLE
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a double-precision decimal floating-point
number.

**See Also:** Constant Field Values

---

#### Field Detail

CHILD_POLICY_EMPTY

```java
static final int CHILD_POLICY_EMPTY
```

A constant returned by

getChildPolicy

to indicate
that an element may not have any children. In other words, it
is required to be a leaf node.

**See Also:** Constant Field Values

---

#### CHILD_POLICY_EMPTY

static final int CHILD_POLICY_EMPTY

A constant returned by

getChildPolicy

to indicate
that an element may not have any children. In other words, it
is required to be a leaf node.

CHILD_POLICY_ALL

```java
static final int CHILD_POLICY_ALL
```

A constant returned by

getChildPolicy

to indicate
that an element must have a single instance of each of its
legal child elements, in order. In DTD terms, the contents of
the element are defined by a sequence

a,b,c,d,...

.

**See Also:** Constant Field Values

---

#### CHILD_POLICY_ALL

static final int CHILD_POLICY_ALL

A constant returned by

getChildPolicy

to indicate
that an element must have a single instance of each of its
legal child elements, in order. In DTD terms, the contents of
the element are defined by a sequence

a,b,c,d,...

.

CHILD_POLICY_SOME

```java
static final int CHILD_POLICY_SOME
```

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one instance of each of its
legal child elements, in order. In DTD terms, the contents of
the element are defined by a sequence

a?,b?,c?,d?,...

.

**See Also:** Constant Field Values

---

#### CHILD_POLICY_SOME

static final int CHILD_POLICY_SOME

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one instance of each of its
legal child elements, in order. In DTD terms, the contents of
the element are defined by a sequence

a?,b?,c?,d?,...

.

CHILD_POLICY_CHOICE

```java
static final int CHILD_POLICY_CHOICE
```

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one children, selected from
among its legal child elements. In DTD terms, the contents of
the element are defined by a selection

a|b|c|d|...

.

**See Also:** Constant Field Values

---

#### CHILD_POLICY_CHOICE

static final int CHILD_POLICY_CHOICE

A constant returned by

getChildPolicy

to indicate
that an element must have zero or one children, selected from
among its legal child elements. In DTD terms, the contents of
the element are defined by a selection

a|b|c|d|...

.

CHILD_POLICY_SEQUENCE

```java
static final int CHILD_POLICY_SEQUENCE
```

A constant returned by

getChildPolicy

to indicate
that an element must have a sequence of instances of any of its
legal child elements. In DTD terms, the contents of the
element are defined by a sequence

(a|b|c|d|...)*

.

**See Also:** Constant Field Values

---

#### CHILD_POLICY_SEQUENCE

static final int CHILD_POLICY_SEQUENCE

A constant returned by

getChildPolicy

to indicate
that an element must have a sequence of instances of any of its
legal child elements. In DTD terms, the contents of the
element are defined by a sequence

(a|b|c|d|...)*

.

CHILD_POLICY_REPEAT

```java
static final int CHILD_POLICY_REPEAT
```

A constant returned by

getChildPolicy

to indicate
that an element must have zero or more instances of its unique
legal child element. In DTD terms, the contents of the element
are defined by a starred expression

a*

.

**See Also:** Constant Field Values

---

#### CHILD_POLICY_REPEAT

static final int CHILD_POLICY_REPEAT

A constant returned by

getChildPolicy

to indicate
that an element must have zero or more instances of its unique
legal child element. In DTD terms, the contents of the element
are defined by a starred expression

a*

.

CHILD_POLICY_MAX

```java
static final int CHILD_POLICY_MAX
```

The largest valid

CHILD_POLICY_*

constant,
to be used for range checks.

**See Also:** Constant Field Values

---

#### CHILD_POLICY_MAX

static final int CHILD_POLICY_MAX

The largest valid

CHILD_POLICY_*

constant,
to be used for range checks.

VALUE_NONE

```java
static final int VALUE_NONE
```

A constant returned by

getObjectValueType

to
indicate the absence of a user object.

**See Also:** Constant Field Values

---

#### VALUE_NONE

static final int VALUE_NONE

A constant returned by

getObjectValueType

to
indicate the absence of a user object.

VALUE_ARBITRARY

```java
static final int VALUE_ARBITRARY
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a single, arbitrary value.

**See Also:** Constant Field Values

---

#### VALUE_ARBITRARY

static final int VALUE_ARBITRARY

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a single, arbitrary value.

VALUE_RANGE

```java
static final int VALUE_RANGE
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values. Both the minimum
and maximum values of the range are exclusive. It is
recommended that ranges of integers be inclusive on both ends,
and that exclusive ranges be used only for floating-point data.

**See Also:** VALUE_RANGE_MIN_MAX_INCLUSIVE

,

Constant Field Values

---

#### VALUE_RANGE

static final int VALUE_RANGE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values. Both the minimum
and maximum values of the range are exclusive. It is
recommended that ranges of integers be inclusive on both ends,
and that exclusive ranges be used only for floating-point data.

VALUE_RANGE_MIN_INCLUSIVE_MASK

```java
static final int VALUE_RANGE_MIN_INCLUSIVE_MASK
```

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MIN_INCLUSIVE

, and with

VALUE_RANGE_MAX_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

Similarly, the value may be and'ed with the value of

getAttributeValueType

or

getObjectValueType

to determine if the minimum
value of the range is inclusive.

**See Also:** Constant Field Values

---

#### VALUE_RANGE_MIN_INCLUSIVE_MASK

static final int VALUE_RANGE_MIN_INCLUSIVE_MASK

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MIN_INCLUSIVE

, and with

VALUE_RANGE_MAX_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

Similarly, the value may be and'ed with the value of

getAttributeValueType

or

getObjectValueType

to determine if the minimum
value of the range is inclusive.

Similarly, the value may be and'ed with the value of

getAttributeValueType

or

getObjectValueType

to determine if the minimum
value of the range is inclusive.

VALUE_RANGE_MAX_INCLUSIVE_MASK

```java
static final int VALUE_RANGE_MAX_INCLUSIVE_MASK
```

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MAX_INCLUSIVE

, and with

VALUE_RANGE_MIN_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

Similarly, the value may be and'ed with the value of

getAttributeValueType

or

getObjectValueType

to determine if the maximum
value of the range is inclusive.

**See Also:** Constant Field Values

---

#### VALUE_RANGE_MAX_INCLUSIVE_MASK

static final int VALUE_RANGE_MAX_INCLUSIVE_MASK

A value that may be or'ed with

VALUE_RANGE

to
obtain

VALUE_RANGE_MAX_INCLUSIVE

, and with

VALUE_RANGE_MIN_INCLUSIVE

to obtain

VALUE_RANGE_MIN_MAX_INCLUSIVE

.

Similarly, the value may be and'ed with the value of

getAttributeValueType

or

getObjectValueType

to determine if the maximum
value of the range is inclusive.

Similarly, the value may be and'ed with the value of

getAttributeValueType

or

getObjectValueType

to determine if the maximum
value of the range is inclusive.

VALUE_RANGE_MIN_INCLUSIVE

```java
static final int VALUE_RANGE_MIN_INCLUSIVE
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values. The minimum
(but not the maximum) value of the range is inclusive.

**See Also:** Constant Field Values

---

#### VALUE_RANGE_MIN_INCLUSIVE

static final int VALUE_RANGE_MIN_INCLUSIVE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values. The minimum
(but not the maximum) value of the range is inclusive.

VALUE_RANGE_MAX_INCLUSIVE

```java
static final int VALUE_RANGE_MAX_INCLUSIVE
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values. The maximum
(but not the minimum) value of the range is inclusive.

**See Also:** Constant Field Values

---

#### VALUE_RANGE_MAX_INCLUSIVE

static final int VALUE_RANGE_MAX_INCLUSIVE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a range of values. The maximum
(but not the minimum) value of the range is inclusive.

VALUE_RANGE_MIN_MAX_INCLUSIVE

```java
static final int VALUE_RANGE_MIN_MAX_INCLUSIVE
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values. Both the minimum
and maximum values of the range are inclusive. It is
recommended that ranges of integers be inclusive on both ends,
and that exclusive ranges be used only for floating-point data.

**See Also:** Constant Field Values

---

#### VALUE_RANGE_MIN_MAX_INCLUSIVE

static final int VALUE_RANGE_MIN_MAX_INCLUSIVE

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set a range of values. Both the minimum
and maximum values of the range are inclusive. It is
recommended that ranges of integers be inclusive on both ends,
and that exclusive ranges be used only for floating-point data.

VALUE_ENUMERATION

```java
static final int VALUE_ENUMERATION
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set one of a number of enumerated values.
In the case of attributes, these values are

String

s; for objects, they are

Object

s implementing a given class or interface.

Attribute values of type

DATATYPE_BOOLEAN

should be marked as enumerations.

**See Also:** Constant Field Values

---

#### VALUE_ENUMERATION

static final int VALUE_ENUMERATION

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set one of a number of enumerated values.
In the case of attributes, these values are

String

s; for objects, they are

Object

s implementing a given class or interface.

Attribute values of type

DATATYPE_BOOLEAN

should be marked as enumerations.

Attribute values of type

DATATYPE_BOOLEAN

should be marked as enumerations.

VALUE_LIST

```java
static final int VALUE_LIST
```

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a list or array of values. In the
case of attributes, the list will consist of
whitespace-separated values within a

String

; for
objects, an array will be used.

**See Also:** Constant Field Values

---

#### VALUE_LIST

static final int VALUE_LIST

A constant returned by

getAttributeValueType

and

getObjectValueType

to indicate that the attribute
or user object may be set to a list or array of values. In the
case of attributes, the list will consist of
whitespace-separated values within a

String

; for
objects, an array will be used.

DATATYPE_STRING

```java
static final int DATATYPE_STRING
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a general Unicode
string.

**See Also:** Constant Field Values

---

#### DATATYPE_STRING

static final int DATATYPE_STRING

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a general Unicode
string.

DATATYPE_BOOLEAN

```java
static final int DATATYPE_BOOLEAN
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is one of the boolean
values 'true' or 'false'.
Attribute values of type DATATYPE_BOOLEAN should be marked as
enumerations, and the permitted values should be the string
literal values "TRUE" or "FALSE", although a plugin may also
recognise lower or mixed case equivalents.

**See Also:** Constant Field Values

---

#### DATATYPE_BOOLEAN

static final int DATATYPE_BOOLEAN

A constant returned by

getAttributeDataType

indicating that the value of an attribute is one of the boolean
values 'true' or 'false'.
Attribute values of type DATATYPE_BOOLEAN should be marked as
enumerations, and the permitted values should be the string
literal values "TRUE" or "FALSE", although a plugin may also
recognise lower or mixed case equivalents.

DATATYPE_INTEGER

```java
static final int DATATYPE_INTEGER
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of an integer.

**See Also:** Constant Field Values

---

#### DATATYPE_INTEGER

static final int DATATYPE_INTEGER

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of an integer.

DATATYPE_FLOAT

```java
static final int DATATYPE_FLOAT
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a decimal floating-point number.

**See Also:** Constant Field Values

---

#### DATATYPE_FLOAT

static final int DATATYPE_FLOAT

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a decimal floating-point number.

DATATYPE_DOUBLE

```java
static final int DATATYPE_DOUBLE
```

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a double-precision decimal floating-point
number.

**See Also:** Constant Field Values

---

#### DATATYPE_DOUBLE

static final int DATATYPE_DOUBLE

A constant returned by

getAttributeDataType

indicating that the value of an attribute is a string
representation of a double-precision decimal floating-point
number.

Method Detail

- getRootName

```java
String
getRootName()
```

Returns the name of the root element of the format.

**Returns:** a

String

.

- canNodeAppear

```java
boolean canNodeAppear​(
String
elementName,

ImageTypeSpecifier
imageType)
```

Returns

true

if the element (and the subtree below
it) is allowed to appear in a metadata document for an image of
the given type, defined by an

ImageTypeSpecifier

.
For example, a metadata document format might contain an
element that describes the primary colors of the image, which
would not be allowed when writing a grayscale image.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** imageType

- an

ImageTypeSpecifier

indicating
the type of the image that will be associated with the
metadata.
**Returns:** true

if the node is meaningful for images
of the given type.

- getElementMinChildren

```java
int getElementMinChildren​(
String
elementName)
```

Returns the minimum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

. For
example, an element representing color primary information
might be required to have at least 3 children, one for each
primary.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an

int

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element does
not have a child policy of

CHILD_POLICY_REPEAT

.

- getElementMaxChildren

```java
int getElementMaxChildren​(
String
elementName)
```

Returns the maximum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

. For
example, an element representing an entry in an 8-bit color
palette might be allowed to repeat up to 256 times. A value of

Integer.MAX_VALUE

may be used to specify that
there is no upper bound.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an

int

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element does
not have a child policy of

CHILD_POLICY_REPEAT

.

- getElementDescription

```java
String
getElementDescription​(
String
elementName,

Locale
locale)
```

Returns a

String

containing a description of the
named element, or

null

. The description will be
localized for the supplied

Locale

if possible.

If

locale

is

null

, the current
default

Locale

returned by

Locale.getLocale

will be used.

**Parameters:** elementName

- the name of the element.
**Parameters:** locale

- the

Locale

for which localization
will be attempted.
**Returns:** the element description.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.

- getChildPolicy

```java
int getChildPolicy​(
String
elementName)
```

Returns one of the constants starting with

CHILD_POLICY_

, indicating the legal pattern of
children for the named element.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** one of the

CHILD_POLICY_*

constants.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.

- getChildNames

```java
String
[] getChildNames​(
String
elementName)
```

Returns an array of

String

s indicating the names
of the element which are allowed to be children of the named
element, in the order in which they should appear. If the
element cannot have children,

null

is returned.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an array of

String

s, or null.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.

- getAttributeNames

```java
String
[] getAttributeNames​(
String
elementName)
```

Returns an array of

String

s listing the names of
the attributes that may be associated with the named element.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an array of

String

s.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.

- getAttributeValueType

```java
int getAttributeValueType​(
String
elementName,

String
attrName)
```

Returns one of the constants starting with

VALUE_

,
indicating whether the values of the given attribute within the
named element are arbitrary, constrained to lie within a
specified range, constrained to be one of a set of enumerated
values, or are a whitespace-separated list of arbitrary values.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** one of the

VALUE_*

constants.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

- getAttributeDataType

```java
int getAttributeDataType​(
String
elementName,

String
attrName)
```

Returns one of the constants starting with

DATATYPE_

, indicating the format and
interpretation of the value of the given attribute within the
named element. If

getAttributeValueType

returns

VALUE_LIST

, then the legal value is a
whitespace-spearated list of values of the returned datatype.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** one of the

DATATYPE_*

constants.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

- isAttributeRequired

```java
boolean isAttributeRequired​(
String
elementName,

String
attrName)
```

Returns

true

if the named attribute must be
present within the named element.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** true

if the attribute must be present.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

- getAttributeDefaultValue

```java
String
getAttributeDefaultValue​(
String
elementName,

String
attrName)
```

Returns the default value of the named attribute, if it is not
explicitly present within the named element, as a

String

, or

null

if no default value
is available.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** a

String

containing the default value, or

null

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

- getAttributeEnumerations

```java
String
[] getAttributeEnumerations​(
String
elementName,

String
attrName)
```

Returns an array of

String

s containing the legal
enumerated values for the given attribute within the named
element. This method should only be called if

getAttributeValueType

returns

VALUE_ENUMERATION

.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** an array of

String

s.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as an enumeration.

- getAttributeMinValue

```java
String
getAttributeMinValue​(
String
elementName,

String
attrName)
```

Returns the minimum legal value for the attribute. Whether
this value is inclusive or exclusive may be determined by the
value of

getAttributeValueType

. The value is
returned as a

String

; its interpretation is
dependent on the value of

getAttributeDataType

.
This method should only be called if

getAttributeValueType

returns

VALUE_RANGE_*

.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** a

String

containing the smallest legal
value for the attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as a range.

- getAttributeMaxValue

```java
String
getAttributeMaxValue​(
String
elementName,

String
attrName)
```

Returns the maximum legal value for the attribute. Whether
this value is inclusive or exclusive may be determined by the
value of

getAttributeValueType

. The value is
returned as a

String

; its interpretation is
dependent on the value of

getAttributeDataType

.
This method should only be called if

getAttributeValueType

returns

VALUE_RANGE_*

.

**Parameters:** elementName

- the name of the element being queried, as a

String

.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** a

String

containing the largest legal
value for the attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as a range.

- getAttributeListMinLength

```java
int getAttributeListMinLength​(
String
elementName,

String
attrName)
```

Returns the minimum number of list items that may be used to
define this attribute. The attribute itself is defined as a

String

containing multiple whitespace-separated
items. This method should only be called if

getAttributeValueType

returns

VALUE_LIST

.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** the smallest legal number of list items for the
attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as a list.

- getAttributeListMaxLength

```java
int getAttributeListMaxLength​(
String
elementName,

String
attrName)
```

Returns the maximum number of list items that may be used to
define this attribute. A value of

Integer.MAX_VALUE

may be used to specify that
there is no upper bound. The attribute itself is defined as a

String

containing multiple whitespace-separated
items. This method should only be called if

getAttributeValueType

returns

VALUE_LIST

.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** the largest legal number of list items for the
attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as a list.

- getAttributeDescription

```java
String
getAttributeDescription​(
String
elementName,

String
attrName,

Locale
locale)
```

Returns a

String

containing a description of the
named attribute, or

null

. The description will be
localized for the supplied

Locale

if possible.

If

locale

is

null

, the current
default

Locale

returned by

Locale.getLocale

will be used.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute.
**Parameters:** locale

- the

Locale

for which localization
will be attempted.
**Returns:** the attribute description.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

- getObjectValueType

```java
int getObjectValueType​(
String
elementName)
```

Returns one of the enumerated values starting with

VALUE_

, indicating the type of values
(enumeration, range, or array) that are allowed for the

Object

reference. If no object value can be
stored within the given element, the result of this method will
be

VALUE_NONE

.

Object

references whose legal values are
defined as a range must implement the

Comparable

interface.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** one of the

VALUE_*

constants.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**See Also:** Comparable

- getObjectClass

```java
Class
<?> getObjectClass​(
String
elementName)
```

Returns the

Class

type of the

Object

reference stored within the element. If this element may not
contain an

Object

reference, an

IllegalArgumentException

will be thrown. If the
class type is an array, this field indicates the underlying
class type (

e.g

, for an array of

int

s, this
method would return

int.class

).

Object

references whose legal values are
defined as a range must implement the

Comparable

interface.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** a

Class

object.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).

- getObjectDefaultValue

```java
Object
getObjectDefaultValue​(
String
elementName)
```

Returns an

Object

s containing the default
value for the

Object

reference within
the named element.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an

Object

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).

- getObjectEnumerations

```java
Object
[] getObjectEnumerations​(
String
elementName)
```

Returns an array of

Object

s containing the legal
enumerated values for the

Object

reference within
the named element. This method should only be called if

getObjectValueType

returns

VALUE_ENUMERATION

.

The

Object

associated with a node that accepts
enumerated values must be equal to one of the values returned by
this method, as defined by the

==

operator (as
opposed to the

Object.equals

method).

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an array of

Object

s.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not defined as an enumeration.

- getObjectMinValue

```java
Comparable
<?> getObjectMinValue​(
String
elementName)
```

Returns the minimum legal value for the

Object

reference within the named element. Whether this value is
inclusive or exclusive may be determined by the value of

getObjectValueType

. This method should only be
called if

getObjectValueType

returns one of the
constants starting with

VALUE_RANGE

.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** the smallest legal value for the attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not defined as a range.

- getObjectMaxValue

```java
Comparable
<?> getObjectMaxValue​(
String
elementName)
```

Returns the maximum legal value for the

Object

reference within the named element. Whether this value is
inclusive or exclusive may be determined by the value of

getObjectValueType

. This method should only be
called if

getObjectValueType

returns one of the
constants starting with

VALUE_RANGE

.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** the smallest legal value for the attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not defined as a range.

- getObjectArrayMinLength

```java
int getObjectArrayMinLength​(
String
elementName)
```

Returns the minimum number of array elements that may be used
to define the

Object

reference within the named
element. This method should only be called if

getObjectValueType

returns

VALUE_LIST

.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** the smallest valid array length for the

Object

reference.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not
an array.

- getObjectArrayMaxLength

```java
int getObjectArrayMaxLength​(
String
elementName)
```

Returns the maximum number of array elements that may be used
to define the

Object

reference within the named
element. A value of

Integer.MAX_VALUE

may be used
to specify that there is no upper bound. This method should
only be called if

getObjectValueType

returns

VALUE_LIST

.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** the largest valid array length for the

Object

reference.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not
an array.

---

#### Method Detail

getRootName

```java
String
getRootName()
```

Returns the name of the root element of the format.

**Returns:** a

String

.

---

#### getRootName

String

getRootName()

Returns the name of the root element of the format.

canNodeAppear

```java
boolean canNodeAppear​(
String
elementName,

ImageTypeSpecifier
imageType)
```

Returns

true

if the element (and the subtree below
it) is allowed to appear in a metadata document for an image of
the given type, defined by an

ImageTypeSpecifier

.
For example, a metadata document format might contain an
element that describes the primary colors of the image, which
would not be allowed when writing a grayscale image.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** imageType

- an

ImageTypeSpecifier

indicating
the type of the image that will be associated with the
metadata.
**Returns:** true

if the node is meaningful for images
of the given type.

---

#### canNodeAppear

boolean canNodeAppear​(

String

elementName,

ImageTypeSpecifier

imageType)

Returns

true

if the element (and the subtree below
it) is allowed to appear in a metadata document for an image of
the given type, defined by an

ImageTypeSpecifier

.
For example, a metadata document format might contain an
element that describes the primary colors of the image, which
would not be allowed when writing a grayscale image.

getElementMinChildren

```java
int getElementMinChildren​(
String
elementName)
```

Returns the minimum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

. For
example, an element representing color primary information
might be required to have at least 3 children, one for each
primary.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an

int

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element does
not have a child policy of

CHILD_POLICY_REPEAT

.

---

#### getElementMinChildren

int getElementMinChildren​(

String

elementName)

Returns the minimum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

. For
example, an element representing color primary information
might be required to have at least 3 children, one for each
primary.

getElementMaxChildren

```java
int getElementMaxChildren​(
String
elementName)
```

Returns the maximum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

. For
example, an element representing an entry in an 8-bit color
palette might be allowed to repeat up to 256 times. A value of

Integer.MAX_VALUE

may be used to specify that
there is no upper bound.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an

int

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element does
not have a child policy of

CHILD_POLICY_REPEAT

.

---

#### getElementMaxChildren

int getElementMaxChildren​(

String

elementName)

Returns the maximum number of children of the named element
with child policy

CHILD_POLICY_REPEAT

. For
example, an element representing an entry in an 8-bit color
palette might be allowed to repeat up to 256 times. A value of

Integer.MAX_VALUE

may be used to specify that
there is no upper bound.

getElementDescription

```java
String
getElementDescription​(
String
elementName,

Locale
locale)
```

Returns a

String

containing a description of the
named element, or

null

. The description will be
localized for the supplied

Locale

if possible.

If

locale

is

null

, the current
default

Locale

returned by

Locale.getLocale

will be used.

**Parameters:** elementName

- the name of the element.
**Parameters:** locale

- the

Locale

for which localization
will be attempted.
**Returns:** the element description.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.

---

#### getElementDescription

String

getElementDescription​(

String

elementName,

Locale

locale)

Returns a

String

containing a description of the
named element, or

null

. The description will be
localized for the supplied

Locale

if possible.

If

locale

is

null

, the current
default

Locale

returned by

Locale.getLocale

will be used.

If

locale

is

null

, the current
default

Locale

returned by

Locale.getLocale

will be used.

getChildPolicy

```java
int getChildPolicy​(
String
elementName)
```

Returns one of the constants starting with

CHILD_POLICY_

, indicating the legal pattern of
children for the named element.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** one of the

CHILD_POLICY_*

constants.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.

---

#### getChildPolicy

int getChildPolicy​(

String

elementName)

Returns one of the constants starting with

CHILD_POLICY_

, indicating the legal pattern of
children for the named element.

getChildNames

```java
String
[] getChildNames​(
String
elementName)
```

Returns an array of

String

s indicating the names
of the element which are allowed to be children of the named
element, in the order in which they should appear. If the
element cannot have children,

null

is returned.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an array of

String

s, or null.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.

---

#### getChildNames

String

[] getChildNames​(

String

elementName)

Returns an array of

String

s indicating the names
of the element which are allowed to be children of the named
element, in the order in which they should appear. If the
element cannot have children,

null

is returned.

getAttributeNames

```java
String
[] getAttributeNames​(
String
elementName)
```

Returns an array of

String

s listing the names of
the attributes that may be associated with the named element.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an array of

String

s.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.

---

#### getAttributeNames

String

[] getAttributeNames​(

String

elementName)

Returns an array of

String

s listing the names of
the attributes that may be associated with the named element.

getAttributeValueType

```java
int getAttributeValueType​(
String
elementName,

String
attrName)
```

Returns one of the constants starting with

VALUE_

,
indicating whether the values of the given attribute within the
named element are arbitrary, constrained to lie within a
specified range, constrained to be one of a set of enumerated
values, or are a whitespace-separated list of arbitrary values.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** one of the

VALUE_*

constants.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

---

#### getAttributeValueType

int getAttributeValueType​(

String

elementName,

String

attrName)

Returns one of the constants starting with

VALUE_

,
indicating whether the values of the given attribute within the
named element are arbitrary, constrained to lie within a
specified range, constrained to be one of a set of enumerated
values, or are a whitespace-separated list of arbitrary values.

getAttributeDataType

```java
int getAttributeDataType​(
String
elementName,

String
attrName)
```

Returns one of the constants starting with

DATATYPE_

, indicating the format and
interpretation of the value of the given attribute within the
named element. If

getAttributeValueType

returns

VALUE_LIST

, then the legal value is a
whitespace-spearated list of values of the returned datatype.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** one of the

DATATYPE_*

constants.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

---

#### getAttributeDataType

int getAttributeDataType​(

String

elementName,

String

attrName)

Returns one of the constants starting with

DATATYPE_

, indicating the format and
interpretation of the value of the given attribute within the
named element. If

getAttributeValueType

returns

VALUE_LIST

, then the legal value is a
whitespace-spearated list of values of the returned datatype.

isAttributeRequired

```java
boolean isAttributeRequired​(
String
elementName,

String
attrName)
```

Returns

true

if the named attribute must be
present within the named element.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** true

if the attribute must be present.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

---

#### isAttributeRequired

boolean isAttributeRequired​(

String

elementName,

String

attrName)

Returns

true

if the named attribute must be
present within the named element.

getAttributeDefaultValue

```java
String
getAttributeDefaultValue​(
String
elementName,

String
attrName)
```

Returns the default value of the named attribute, if it is not
explicitly present within the named element, as a

String

, or

null

if no default value
is available.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** a

String

containing the default value, or

null

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

---

#### getAttributeDefaultValue

String

getAttributeDefaultValue​(

String

elementName,

String

attrName)

Returns the default value of the named attribute, if it is not
explicitly present within the named element, as a

String

, or

null

if no default value
is available.

getAttributeEnumerations

```java
String
[] getAttributeEnumerations​(
String
elementName,

String
attrName)
```

Returns an array of

String

s containing the legal
enumerated values for the given attribute within the named
element. This method should only be called if

getAttributeValueType

returns

VALUE_ENUMERATION

.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** an array of

String

s.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as an enumeration.

---

#### getAttributeEnumerations

String

[] getAttributeEnumerations​(

String

elementName,

String

attrName)

Returns an array of

String

s containing the legal
enumerated values for the given attribute within the named
element. This method should only be called if

getAttributeValueType

returns

VALUE_ENUMERATION

.

getAttributeMinValue

```java
String
getAttributeMinValue​(
String
elementName,

String
attrName)
```

Returns the minimum legal value for the attribute. Whether
this value is inclusive or exclusive may be determined by the
value of

getAttributeValueType

. The value is
returned as a

String

; its interpretation is
dependent on the value of

getAttributeDataType

.
This method should only be called if

getAttributeValueType

returns

VALUE_RANGE_*

.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** a

String

containing the smallest legal
value for the attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as a range.

---

#### getAttributeMinValue

String

getAttributeMinValue​(

String

elementName,

String

attrName)

Returns the minimum legal value for the attribute. Whether
this value is inclusive or exclusive may be determined by the
value of

getAttributeValueType

. The value is
returned as a

String

; its interpretation is
dependent on the value of

getAttributeDataType

.
This method should only be called if

getAttributeValueType

returns

VALUE_RANGE_*

.

getAttributeMaxValue

```java
String
getAttributeMaxValue​(
String
elementName,

String
attrName)
```

Returns the maximum legal value for the attribute. Whether
this value is inclusive or exclusive may be determined by the
value of

getAttributeValueType

. The value is
returned as a

String

; its interpretation is
dependent on the value of

getAttributeDataType

.
This method should only be called if

getAttributeValueType

returns

VALUE_RANGE_*

.

**Parameters:** elementName

- the name of the element being queried, as a

String

.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** a

String

containing the largest legal
value for the attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as a range.

---

#### getAttributeMaxValue

String

getAttributeMaxValue​(

String

elementName,

String

attrName)

Returns the maximum legal value for the attribute. Whether
this value is inclusive or exclusive may be determined by the
value of

getAttributeValueType

. The value is
returned as a

String

; its interpretation is
dependent on the value of

getAttributeDataType

.
This method should only be called if

getAttributeValueType

returns

VALUE_RANGE_*

.

getAttributeListMinLength

```java
int getAttributeListMinLength​(
String
elementName,

String
attrName)
```

Returns the minimum number of list items that may be used to
define this attribute. The attribute itself is defined as a

String

containing multiple whitespace-separated
items. This method should only be called if

getAttributeValueType

returns

VALUE_LIST

.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** the smallest legal number of list items for the
attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as a list.

---

#### getAttributeListMinLength

int getAttributeListMinLength​(

String

elementName,

String

attrName)

Returns the minimum number of list items that may be used to
define this attribute. The attribute itself is defined as a

String

containing multiple whitespace-separated
items. This method should only be called if

getAttributeValueType

returns

VALUE_LIST

.

getAttributeListMaxLength

```java
int getAttributeListMaxLength​(
String
elementName,

String
attrName)
```

Returns the maximum number of list items that may be used to
define this attribute. A value of

Integer.MAX_VALUE

may be used to specify that
there is no upper bound. The attribute itself is defined as a

String

containing multiple whitespace-separated
items. This method should only be called if

getAttributeValueType

returns

VALUE_LIST

.

**Parameters:** elementName

- the name of the element being queried.
**Parameters:** attrName

- the name of the attribute being queried.
**Returns:** the largest legal number of list items for the
attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.
**Throws:** IllegalArgumentException

- if the given attribute is
not defined as a list.

---

#### getAttributeListMaxLength

int getAttributeListMaxLength​(

String

elementName,

String

attrName)

Returns the maximum number of list items that may be used to
define this attribute. A value of

Integer.MAX_VALUE

may be used to specify that
there is no upper bound. The attribute itself is defined as a

String

containing multiple whitespace-separated
items. This method should only be called if

getAttributeValueType

returns

VALUE_LIST

.

getAttributeDescription

```java
String
getAttributeDescription​(
String
elementName,

String
attrName,

Locale
locale)
```

Returns a

String

containing a description of the
named attribute, or

null

. The description will be
localized for the supplied

Locale

if possible.

If

locale

is

null

, the current
default

Locale

returned by

Locale.getLocale

will be used.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute.
**Parameters:** locale

- the

Locale

for which localization
will be attempted.
**Returns:** the attribute description.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

or is not a legal attribute name for this
element.

---

#### getAttributeDescription

String

getAttributeDescription​(

String

elementName,

String

attrName,

Locale

locale)

Returns a

String

containing a description of the
named attribute, or

null

. The description will be
localized for the supplied

Locale

if possible.

If

locale

is

null

, the current
default

Locale

returned by

Locale.getLocale

will be used.

If

locale

is

null

, the current
default

Locale

returned by

Locale.getLocale

will be used.

getObjectValueType

```java
int getObjectValueType​(
String
elementName)
```

Returns one of the enumerated values starting with

VALUE_

, indicating the type of values
(enumeration, range, or array) that are allowed for the

Object

reference. If no object value can be
stored within the given element, the result of this method will
be

VALUE_NONE

.

Object

references whose legal values are
defined as a range must implement the

Comparable

interface.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** one of the

VALUE_*

constants.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**See Also:** Comparable

---

#### getObjectValueType

int getObjectValueType​(

String

elementName)

Returns one of the enumerated values starting with

VALUE_

, indicating the type of values
(enumeration, range, or array) that are allowed for the

Object

reference. If no object value can be
stored within the given element, the result of this method will
be

VALUE_NONE

.

Object

references whose legal values are
defined as a range must implement the

Comparable

interface.

Object

references whose legal values are
defined as a range must implement the

Comparable

interface.

getObjectClass

```java
Class
<?> getObjectClass​(
String
elementName)
```

Returns the

Class

type of the

Object

reference stored within the element. If this element may not
contain an

Object

reference, an

IllegalArgumentException

will be thrown. If the
class type is an array, this field indicates the underlying
class type (

e.g

, for an array of

int

s, this
method would return

int.class

).

Object

references whose legal values are
defined as a range must implement the

Comparable

interface.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** a

Class

object.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).

---

#### getObjectClass

Class

<?> getObjectClass​(

String

elementName)

Returns the

Class

type of the

Object

reference stored within the element. If this element may not
contain an

Object

reference, an

IllegalArgumentException

will be thrown. If the
class type is an array, this field indicates the underlying
class type (

e.g

, for an array of

int

s, this
method would return

int.class

).

Object

references whose legal values are
defined as a range must implement the

Comparable

interface.

Object

references whose legal values are
defined as a range must implement the

Comparable

interface.

getObjectDefaultValue

```java
Object
getObjectDefaultValue​(
String
elementName)
```

Returns an

Object

s containing the default
value for the

Object

reference within
the named element.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an

Object

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).

---

#### getObjectDefaultValue

Object

getObjectDefaultValue​(

String

elementName)

Returns an

Object

s containing the default
value for the

Object

reference within
the named element.

getObjectEnumerations

```java
Object
[] getObjectEnumerations​(
String
elementName)
```

Returns an array of

Object

s containing the legal
enumerated values for the

Object

reference within
the named element. This method should only be called if

getObjectValueType

returns

VALUE_ENUMERATION

.

The

Object

associated with a node that accepts
enumerated values must be equal to one of the values returned by
this method, as defined by the

==

operator (as
opposed to the

Object.equals

method).

**Parameters:** elementName

- the name of the element being queried.
**Returns:** an array of

Object

s.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not defined as an enumeration.

---

#### getObjectEnumerations

Object

[] getObjectEnumerations​(

String

elementName)

Returns an array of

Object

s containing the legal
enumerated values for the

Object

reference within
the named element. This method should only be called if

getObjectValueType

returns

VALUE_ENUMERATION

.

The

Object

associated with a node that accepts
enumerated values must be equal to one of the values returned by
this method, as defined by the

==

operator (as
opposed to the

Object.equals

method).

The

Object

associated with a node that accepts
enumerated values must be equal to one of the values returned by
this method, as defined by the

==

operator (as
opposed to the

Object.equals

method).

getObjectMinValue

```java
Comparable
<?> getObjectMinValue​(
String
elementName)
```

Returns the minimum legal value for the

Object

reference within the named element. Whether this value is
inclusive or exclusive may be determined by the value of

getObjectValueType

. This method should only be
called if

getObjectValueType

returns one of the
constants starting with

VALUE_RANGE

.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** the smallest legal value for the attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not defined as a range.

---

#### getObjectMinValue

Comparable

<?> getObjectMinValue​(

String

elementName)

Returns the minimum legal value for the

Object

reference within the named element. Whether this value is
inclusive or exclusive may be determined by the value of

getObjectValueType

. This method should only be
called if

getObjectValueType

returns one of the
constants starting with

VALUE_RANGE

.

getObjectMaxValue

```java
Comparable
<?> getObjectMaxValue​(
String
elementName)
```

Returns the maximum legal value for the

Object

reference within the named element. Whether this value is
inclusive or exclusive may be determined by the value of

getObjectValueType

. This method should only be
called if

getObjectValueType

returns one of the
constants starting with

VALUE_RANGE

.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** the smallest legal value for the attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not defined as a range.

---

#### getObjectMaxValue

Comparable

<?> getObjectMaxValue​(

String

elementName)

Returns the maximum legal value for the

Object

reference within the named element. Whether this value is
inclusive or exclusive may be determined by the value of

getObjectValueType

. This method should only be
called if

getObjectValueType

returns one of the
constants starting with

VALUE_RANGE

.

getObjectArrayMinLength

```java
int getObjectArrayMinLength​(
String
elementName)
```

Returns the minimum number of array elements that may be used
to define the

Object

reference within the named
element. This method should only be called if

getObjectValueType

returns

VALUE_LIST

.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** the smallest valid array length for the

Object

reference.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not
an array.

---

#### getObjectArrayMinLength

int getObjectArrayMinLength​(

String

elementName)

Returns the minimum number of array elements that may be used
to define the

Object

reference within the named
element. This method should only be called if

getObjectValueType

returns

VALUE_LIST

.

getObjectArrayMaxLength

```java
int getObjectArrayMaxLength​(
String
elementName)
```

Returns the maximum number of array elements that may be used
to define the

Object

reference within the named
element. A value of

Integer.MAX_VALUE

may be used
to specify that there is no upper bound. This method should
only be called if

getObjectValueType

returns

VALUE_LIST

.

**Parameters:** elementName

- the name of the element being queried.
**Returns:** the largest valid array length for the

Object

reference.
**Throws:** IllegalArgumentException

- if

elementName

is

null

or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if the named element cannot
contain an object value (

i.e.

, if

getObjectValueType(elementName) == VALUE_NONE

).
**Throws:** IllegalArgumentException

- if the

Object

is not
an array.

---

#### getObjectArrayMaxLength

int getObjectArrayMaxLength​(

String

elementName)

Returns the maximum number of array elements that may be used
to define the

Object

reference within the named
element. A value of

Integer.MAX_VALUE

may be used
to specify that there is no upper bound. This method should
only be called if

getObjectValueType

returns

VALUE_LIST

.

---

