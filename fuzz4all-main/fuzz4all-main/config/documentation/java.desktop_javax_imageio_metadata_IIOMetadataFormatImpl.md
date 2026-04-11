# Class IIOMetadataFormatImpl

**Source:** `java.desktop\javax\imageio\metadata\IIOMetadataFormatImpl.html`

### Class Description

```java
public abstract class
IIOMetadataFormatImpl

extends
Object

implements
IIOMetadataFormat
```

A concrete class providing a reusable implementation of the

IIOMetadataFormat

interface. In addition, a static
instance representing the standard, plug-in neutral

javax_imageio_1.0

format is provided by the

getStandardFormatInstance

method.

In order to supply localized descriptions of elements and
attributes, a

ResourceBundle

with a base name of

this.getClass().getName() + "Resources"

should be
supplied via the usual mechanism used by

ResourceBundle.getBundle

. Briefly, the subclasser
supplies one or more additional classes according to a naming
convention (by default, the fully-qualified name of the subclass
extending

IIMetadataFormatImpl

, plus the string
"Resources", plus the country, language, and variant codes
separated by underscores). At run time, calls to

getElementDescription

or

getAttributeDescription

will attempt to load such
classes dynamically according to the supplied locale, and will use
either the element name, or the element name followed by a '/'
character followed by the attribute name as a key. This key will
be supplied to the

ResourceBundle

's

getString

method, and the resulting localized
description of the node or attribute is returned.

The subclass may supply a different base name for the resource
bundles using the

setResourceBaseName

method.

A subclass may choose its own localization mechanism, if so
desired, by overriding the supplied implementations of

getElementDescription

and

getAttributeDescription

.

**All Implemented Interfaces:** IIOMetadataFormat

---

### Field Details

#### public static final
String
standardMetadataFormatName

A

String

constant containing the standard format
name,

"javax_imageio_1.0"

.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public IIOMetadataFormatImpl​(
String
rootName,
int childPolicy)

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and child policy (other than

CHILD_POLICY_REPEAT

). Additional elements, and
their attributes and

Object

reference information
may be added using the various

add

methods.

**Parameters:**
- rootName

- the name of the root element.
- childPolicy

- one of the

CHILD_POLICY_*

constants,
other than

CHILD_POLICY_REPEAT

.

**Throws:**
- IllegalArgumentException

- if

rootName

is

null

.
- IllegalArgumentException

- if

childPolicy

is
not one of the predefined constants.

---

#### public IIOMetadataFormatImpl​(
String
rootName,
int minChildren,
int maxChildren)

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and a child policy of

CHILD_POLICY_REPEAT

. Additional elements, and
their attributes and

Object

reference information
may be added using the various

add

methods.

**Parameters:**
- rootName

- the name of the root element.
- minChildren

- the minimum number of children of the node.
- maxChildren

- the maximum number of children of the node.

**Throws:**
- IllegalArgumentException

- if

rootName

is

null

.
- IllegalArgumentException

- if

minChildren

is negative or larger than

maxChildren

.

---

### Method Details

#### protected void setResourceBaseName​(
String
resourceBaseName)

Sets a new base name for locating

ResourceBundle

s
containing descriptions of elements and attributes for this
format.

Prior to the first time this method is called, the base
name will be equal to

this.getClass().getName() + "Resources"

.

**Parameters:**
- resourceBaseName

- a

String

containing the new
base name.

**Throws:**
- IllegalArgumentException

- if

resourceBaseName

is

null

.

**See Also:**
- getResourceBaseName()

---

#### protected
String
getResourceBaseName()

Returns the currently set base name for locating

ResourceBundle

s.

**Returns:**
- a

String

containing the base name.

**See Also:**
- setResourceBaseName(java.lang.String)

---

#### protected void addElement​(
String
elementName,

String
parentName,
int childPolicy)

Adds a new element type to this metadata document format with a
child policy other than

CHILD_POLICY_REPEAT

.

**Parameters:**
- elementName

- the name of the new element.
- parentName

- the name of the element that will be the
parent of the new element.
- childPolicy

- one of the

CHILD_POLICY_*

constants, other than

CHILD_POLICY_REPEAT

,
indicating the child policy of the new element.

**Throws:**
- IllegalArgumentException

- if

parentName

is

null

, or is not a legal element name for this
format.
- IllegalArgumentException

- if

childPolicy

is not one of the predefined constants.

---

#### protected void addElement​(
String
elementName,

String
parentName,
int minChildren,
int maxChildren)

Adds a new element type to this metadata document format with a
child policy of

CHILD_POLICY_REPEAT

.

**Parameters:**
- elementName

- the name of the new element.
- parentName

- the name of the element that will be the
parent of the new element.
- minChildren

- the minimum number of children of the node.
- maxChildren

- the maximum number of children of the node.

**Throws:**
- IllegalArgumentException

- if

parentName

is

null

, or is not a legal element name for this
format.
- IllegalArgumentException

- if

minChildren

is negative or larger than

maxChildren

.

---

#### protected void addChildElement​(
String
elementName,

String
parentName)

Adds an existing element to the list of legal children for a
given parent node type.

**Parameters:**
- parentName

- the name of the element that will be the
new parent of the element.
- elementName

- the name of the element to be added as a
child.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
- IllegalArgumentException

- if

parentName

is

null

, or is not a legal element name for this
format.

---

#### protected void removeElement​(
String
elementName)

Removes an element from the format. If no element with the
given name was present, nothing happens and no exception is
thrown.

**Parameters:**
- elementName

- the name of the element to be removed.

---

#### protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,

String
defaultValue)

Adds a new attribute to a previously defined element that may
be set to an arbitrary value.

**Parameters:**
- elementName

- the name of the element.
- attrName

- the name of the attribute being added.
- dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
- required

-

true

if the attribute must be present.
- defaultValue

- the default value for the attribute, or

null

.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

.
- IllegalArgumentException

- if

dataType

is
not one of the predefined constants.

---

#### protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,

String
defaultValue,

List
<
String
> enumeratedValues)

Adds a new attribute to a previously defined element that will
be defined by a set of enumerated values.

**Parameters:**
- elementName

- the name of the element.
- attrName

- the name of the attribute being added.
- dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
- required

-

true

if the attribute must be present.
- defaultValue

- the default value for the attribute, or

null

.
- enumeratedValues

- a

List

of

String

s containing the legal values for the
attribute.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

.
- IllegalArgumentException

- if

dataType

is
not one of the predefined constants.
- IllegalArgumentException

- if

enumeratedValues

is

null

.
- IllegalArgumentException

- if

enumeratedValues

does not contain at least one
entry.
- IllegalArgumentException

- if

enumeratedValues

contains an element that is not a

String

or is

null

.

---

#### protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,

String
defaultValue,

String
minValue,

String
maxValue,
boolean minInclusive,
boolean maxInclusive)

Adds a new attribute to a previously defined element that will
be defined by a range of values.

**Parameters:**
- elementName

- the name of the element.
- attrName

- the name of the attribute being added.
- dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
- required

-

true

if the attribute must be present.
- defaultValue

- the default value for the attribute, or

null

.
- minValue

- the smallest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
attribute, as a

String

.
- maxValue

- the largest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
attribute, as a

String

.
- minInclusive

-

true

if

minValue

is inclusive.
- maxInclusive

-

true

if

maxValue

is inclusive.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

.
- IllegalArgumentException

- if

dataType

is
not one of the predefined constants.

---

#### protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,
int listMinLength,
int listMaxLength)

Adds a new attribute to a previously defined element that will
be defined by a list of values.

**Parameters:**
- elementName

- the name of the element.
- attrName

- the name of the attribute being added.
- dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
- required

-

true

if the attribute must be present.
- listMinLength

- the smallest legal number of list items.
- listMaxLength

- the largest legal number of list items.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

.
- IllegalArgumentException

- if

dataType

is
not one of the predefined constants.
- IllegalArgumentException

- if

listMinLength

is negative or larger than

listMaxLength

.

---

#### protected void addBooleanAttribute​(
String
elementName,

String
attrName,
boolean hasDefaultValue,
boolean defaultValue)

Adds a new attribute to a previously defined element that will
be defined by the enumerated values

TRUE

and

FALSE

, with a datatype of

DATATYPE_BOOLEAN

.

**Parameters:**
- elementName

- the name of the element.
- attrName

- the name of the attribute being added.
- hasDefaultValue

-

true

if a default value
should be present.
- defaultValue

- the default value for the attribute as a

boolean

, ignored if

hasDefaultValue

is

false

.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
- IllegalArgumentException

- if

attrName

is

null

.

---

#### protected void removeAttribute​(
String
elementName,

String
attrName)

Removes an attribute from a previously defined element. If no
attribute with the given name was present in the given element,
nothing happens and no exception is thrown.

**Parameters:**
- elementName

- the name of the element.
- attrName

- the name of the attribute being removed.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.

---

#### protected <T> void addObjectValue​(
String
elementName,

Class
<T> classType,
boolean required,
T defaultValue)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

is unconstrained other than by
its class type.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Parameters:**
- elementName

- the name of the element.
- classType

- a

Class

variable indicating the
legal class type for the object value.
- required

-

true

if an object value must be present.
- defaultValue

- the default value for the

Object

reference, or

null

.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.

**Type Parameters:**
- T

- the type of the object.

---

#### protected <T> void addObjectValue​(
String
elementName,

Class
<T> classType,
boolean required,
T defaultValue,

List
<? extends T> enumeratedValues)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must be one of the values
given by

enumeratedValues

.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Parameters:**
- elementName

- the name of the element.
- classType

- a

Class

variable indicating the
legal class type for the object value.
- required

-

true

if an object value must be present.
- defaultValue

- the default value for the

Object

reference, or

null

.
- enumeratedValues

- a

List

of

Object

s containing the legal values for the
object reference.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.
- IllegalArgumentException

- if

enumeratedValues

is

null

.
- IllegalArgumentException

- if

enumeratedValues

does not contain at least one
entry.
- IllegalArgumentException

- if

enumeratedValues

contains an element that is not
an instance of the class type denoted by

classType

or is

null

.

**Type Parameters:**
- T

- the type of the object.

---

#### protected <T extends
Object
&
Comparable
<? super T>> void addObjectValue​(
String
elementName,

Class
<T> classType,
T defaultValue,

Comparable
<? super T> minValue,

Comparable
<? super T> maxValue,
boolean minInclusive,
boolean maxInclusive)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must be within the range given
by

minValue

and

maxValue

.
Furthermore, the class type must implement the

Comparable

interface.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Parameters:**
- elementName

- the name of the element.
- classType

- a

Class

variable indicating the
legal class type for the object value.
- defaultValue

- the default value for the
- minValue

- the smallest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
object value, as a

String

.
- maxValue

- the largest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
object value, as a

String

.
- minInclusive

-

true

if

minValue

is inclusive.
- maxInclusive

-

true

if

maxValue

is inclusive.

**Throws:**
- IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.

**Type Parameters:**
- T

- the type of the object.

---

#### protected void addObjectValue​(
String
elementName,

Class
<?> classType,
int arrayMinLength,
int arrayMaxLength)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must an array of objects of
class type given by

classType

, with at least

arrayMinLength

and at most

arrayMaxLength

elements.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Parameters:**
- elementName

- the name of the element.
- classType

- a

Class

variable indicating the
legal class type for the object value.
- arrayMinLength

- the smallest legal length for the array.
- arrayMaxLength

- the largest legal length for the array.

**Throws:**
- IllegalArgumentException

- if

elementName

is
not a legal element name for this format.

---

#### protected void removeObjectValue​(
String
elementName)

Disallows an

Object

reference from being stored in
nodes implementing the named element.

**Parameters:**
- elementName

- the name of the element.

**Throws:**
- IllegalArgumentException

- if

elementName

is
not a legal element name for this format.

---

#### public
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

The default implementation will first locate a

ResourceBundle

using the current resource base
name set by

setResourceBaseName

and the supplied

Locale

, using the fallback mechanism described in
the comments for

ResourceBundle.getBundle

. If a

ResourceBundle

is found, the element name will be
used as a key to its

getString

method, and the
result returned. If no

ResourceBundle

is found,
or no such key is present,

null

will be returned.

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

**Specified by:**
- getElementDescription

in interface

IIOMetadataFormat

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

**See Also:**
- setResourceBaseName(java.lang.String)

---

#### public
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

The default implementation will first locate a

ResourceBundle

using the current resource base
name set by

setResourceBaseName

and the supplied

Locale

, using the fallback mechanism described in
the comments for

ResourceBundle.getBundle

. If a

ResourceBundle

is found, the element name followed
by a "/" character followed by the attribute name
(

elementName + "/" + attrName

) will be used as a
key to its

getString

method, and the result
returned. If no

ResourceBundle

is found, or no
such key is present,

null

will be returned.

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

**Specified by:**
- getAttributeDescription

in interface

IIOMetadataFormat

**Parameters:**
- elementName

- the name of the element.
- attrName

- the name of the attribute.
- locale

- the

Locale

for which localization
will be attempted, or

null

.

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

**See Also:**
- setResourceBaseName(java.lang.String)

---

#### public static
IIOMetadataFormat
getStandardFormatInstance()

Returns an

IIOMetadataFormat

object describing the
standard, plug-in neutral

javax.imageio_1.0

metadata document format described in the comment of the

javax.imageio.metadata

package.

**Returns:**
- a predefined

IIOMetadataFormat

instance.

---

### Additional Sections

#### Class IIOMetadataFormatImpl

java.lang.Object

- javax.imageio.metadata.IIOMetadataFormatImpl

javax.imageio.metadata.IIOMetadataFormatImpl

**All Implemented Interfaces:** IIOMetadataFormat

```java
public abstract class
IIOMetadataFormatImpl

extends
Object

implements
IIOMetadataFormat
```

A concrete class providing a reusable implementation of the

IIOMetadataFormat

interface. In addition, a static
instance representing the standard, plug-in neutral

javax_imageio_1.0

format is provided by the

getStandardFormatInstance

method.

In order to supply localized descriptions of elements and
attributes, a

ResourceBundle

with a base name of

this.getClass().getName() + "Resources"

should be
supplied via the usual mechanism used by

ResourceBundle.getBundle

. Briefly, the subclasser
supplies one or more additional classes according to a naming
convention (by default, the fully-qualified name of the subclass
extending

IIMetadataFormatImpl

, plus the string
"Resources", plus the country, language, and variant codes
separated by underscores). At run time, calls to

getElementDescription

or

getAttributeDescription

will attempt to load such
classes dynamically according to the supplied locale, and will use
either the element name, or the element name followed by a '/'
character followed by the attribute name as a key. This key will
be supplied to the

ResourceBundle

's

getString

method, and the resulting localized
description of the node or attribute is returned.

The subclass may supply a different base name for the resource
bundles using the

setResourceBaseName

method.

A subclass may choose its own localization mechanism, if so
desired, by overriding the supplied implementations of

getElementDescription

and

getAttributeDescription

.

**See Also:** ResourceBundle.getBundle(String,Locale)

public abstract class

IIOMetadataFormatImpl

extends

Object

implements

IIOMetadataFormat

A concrete class providing a reusable implementation of the

IIOMetadataFormat

interface. In addition, a static
instance representing the standard, plug-in neutral

javax_imageio_1.0

format is provided by the

getStandardFormatInstance

method.

In order to supply localized descriptions of elements and
attributes, a

ResourceBundle

with a base name of

this.getClass().getName() + "Resources"

should be
supplied via the usual mechanism used by

ResourceBundle.getBundle

. Briefly, the subclasser
supplies one or more additional classes according to a naming
convention (by default, the fully-qualified name of the subclass
extending

IIMetadataFormatImpl

, plus the string
"Resources", plus the country, language, and variant codes
separated by underscores). At run time, calls to

getElementDescription

or

getAttributeDescription

will attempt to load such
classes dynamically according to the supplied locale, and will use
either the element name, or the element name followed by a '/'
character followed by the attribute name as a key. This key will
be supplied to the

ResourceBundle

's

getString

method, and the resulting localized
description of the node or attribute is returned.

The subclass may supply a different base name for the resource
bundles using the

setResourceBaseName

method.

A subclass may choose its own localization mechanism, if so
desired, by overriding the supplied implementations of

getElementDescription

and

getAttributeDescription

.

In order to supply localized descriptions of elements and
attributes, a

ResourceBundle

with a base name of

this.getClass().getName() + "Resources"

should be
supplied via the usual mechanism used by

ResourceBundle.getBundle

. Briefly, the subclasser
supplies one or more additional classes according to a naming
convention (by default, the fully-qualified name of the subclass
extending

IIMetadataFormatImpl

, plus the string
"Resources", plus the country, language, and variant codes
separated by underscores). At run time, calls to

getElementDescription

or

getAttributeDescription

will attempt to load such
classes dynamically according to the supplied locale, and will use
either the element name, or the element name followed by a '/'
character followed by the attribute name as a key. This key will
be supplied to the

ResourceBundle

's

getString

method, and the resulting localized
description of the node or attribute is returned.

The subclass may supply a different base name for the resource
bundles using the

setResourceBaseName

method.

A subclass may choose its own localization mechanism, if so
desired, by overriding the supplied implementations of

getElementDescription

and

getAttributeDescription

.

The subclass may supply a different base name for the resource
bundles using the

setResourceBaseName

method.

A subclass may choose its own localization mechanism, if so
desired, by overriding the supplied implementations of

getElementDescription

and

getAttributeDescription

.

A subclass may choose its own localization mechanism, if so
desired, by overriding the supplied implementations of

getElementDescription

and

getAttributeDescription

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

standardMetadataFormatName

A

String

constant containing the standard format
name,

"javax_imageio_1.0"

.

- Fields declared in interface javax.imageio.metadata.

IIOMetadataFormat

CHILD_POLICY_ALL

,

CHILD_POLICY_CHOICE

,

CHILD_POLICY_EMPTY

,

CHILD_POLICY_MAX

,

CHILD_POLICY_REPEAT

,

CHILD_POLICY_SEQUENCE

,

CHILD_POLICY_SOME

,

DATATYPE_BOOLEAN

,

DATATYPE_DOUBLE

,

DATATYPE_FLOAT

,

DATATYPE_INTEGER

,

DATATYPE_STRING

,

VALUE_ARBITRARY

,

VALUE_ENUMERATION

,

VALUE_LIST

,

VALUE_NONE

,

VALUE_RANGE

,

VALUE_RANGE_MAX_INCLUSIVE

,

VALUE_RANGE_MAX_INCLUSIVE_MASK

,

VALUE_RANGE_MIN_INCLUSIVE

,

VALUE_RANGE_MIN_INCLUSIVE_MASK

,

VALUE_RANGE_MIN_MAX_INCLUSIVE

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IIOMetadataFormatImpl

​(

String

rootName,
int childPolicy)

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and child policy (other than

CHILD_POLICY_REPEAT

).

IIOMetadataFormatImpl

​(

String

rootName,
int minChildren,
int maxChildren)

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and a child policy of

CHILD_POLICY_REPEAT

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

protected void

addAttribute

​(

String

elementName,

String

attrName,
int dataType,
boolean required,
int listMinLength,
int listMaxLength)

Adds a new attribute to a previously defined element that will
be defined by a list of values.

protected void

addAttribute

​(

String

elementName,

String

attrName,
int dataType,
boolean required,

String

defaultValue)

Adds a new attribute to a previously defined element that may
be set to an arbitrary value.

protected void

addAttribute

​(

String

elementName,

String

attrName,
int dataType,
boolean required,

String

defaultValue,

String

minValue,

String

maxValue,
boolean minInclusive,
boolean maxInclusive)

Adds a new attribute to a previously defined element that will
be defined by a range of values.

protected void

addAttribute

​(

String

elementName,

String

attrName,
int dataType,
boolean required,

String

defaultValue,

List

<

String

> enumeratedValues)

Adds a new attribute to a previously defined element that will
be defined by a set of enumerated values.

protected void

addBooleanAttribute

​(

String

elementName,

String

attrName,
boolean hasDefaultValue,
boolean defaultValue)

Adds a new attribute to a previously defined element that will
be defined by the enumerated values

TRUE

and

FALSE

, with a datatype of

DATATYPE_BOOLEAN

.

protected void

addChildElement

​(

String

elementName,

String

parentName)

Adds an existing element to the list of legal children for a
given parent node type.

protected void

addElement

​(

String

elementName,

String

parentName,
int childPolicy)

Adds a new element type to this metadata document format with a
child policy other than

CHILD_POLICY_REPEAT

.

protected void

addElement

​(

String

elementName,

String

parentName,
int minChildren,
int maxChildren)

Adds a new element type to this metadata document format with a
child policy of

CHILD_POLICY_REPEAT

.

protected void

addObjectValue

​(

String

elementName,

Class

<?> classType,
int arrayMinLength,
int arrayMaxLength)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element.

protected <T> void

addObjectValue

​(

String

elementName,

Class

<T> classType,
boolean required,
T defaultValue)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element.

protected <T> void

addObjectValue

​(

String

elementName,

Class

<T> classType,
boolean required,
T defaultValue,

List

<? extends T> enumeratedValues)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element.

protected <T extends

Object

&

Comparable

<? super T>>

void

addObjectValue

​(

String

elementName,

Class

<T> classType,
T defaultValue,

Comparable

<? super T> minValue,

Comparable

<? super T> maxValue,
boolean minInclusive,
boolean maxInclusive)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element.

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

protected

String

getResourceBaseName

()

Returns the currently set base name for locating

ResourceBundle

s.

static

IIOMetadataFormat

getStandardFormatInstance

()

Returns an

IIOMetadataFormat

object describing the
standard, plug-in neutral

javax.imageio_1.0

metadata document format described in the comment of the

javax.imageio.metadata

package.

protected void

removeAttribute

​(

String

elementName,

String

attrName)

Removes an attribute from a previously defined element.

protected void

removeElement

​(

String

elementName)

Removes an element from the format.

protected void

removeObjectValue

​(

String

elementName)

Disallows an

Object

reference from being stored in
nodes implementing the named element.

protected void

setResourceBaseName

​(

String

resourceBaseName)

Sets a new base name for locating

ResourceBundle

s
containing descriptions of elements and attributes for this
format.

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

- Methods declared in interface javax.imageio.metadata.

IIOMetadataFormat

canNodeAppear

,

getAttributeDataType

,

getAttributeDefaultValue

,

getAttributeEnumerations

,

getAttributeListMaxLength

,

getAttributeListMinLength

,

getAttributeMaxValue

,

getAttributeMinValue

,

getAttributeNames

,

getAttributeValueType

,

getChildNames

,

getChildPolicy

,

getElementMaxChildren

,

getElementMinChildren

,

getObjectArrayMaxLength

,

getObjectArrayMinLength

,

getObjectClass

,

getObjectDefaultValue

,

getObjectEnumerations

,

getObjectMaxValue

,

getObjectMinValue

,

getObjectValueType

,

getRootName

,

isAttributeRequired

Field Summary

Fields

Modifier and Type

Field

Description

static

String

standardMetadataFormatName

A

String

constant containing the standard format
name,

"javax_imageio_1.0"

.

- Fields declared in interface javax.imageio.metadata.

IIOMetadataFormat

CHILD_POLICY_ALL

,

CHILD_POLICY_CHOICE

,

CHILD_POLICY_EMPTY

,

CHILD_POLICY_MAX

,

CHILD_POLICY_REPEAT

,

CHILD_POLICY_SEQUENCE

,

CHILD_POLICY_SOME

,

DATATYPE_BOOLEAN

,

DATATYPE_DOUBLE

,

DATATYPE_FLOAT

,

DATATYPE_INTEGER

,

DATATYPE_STRING

,

VALUE_ARBITRARY

,

VALUE_ENUMERATION

,

VALUE_LIST

,

VALUE_NONE

,

VALUE_RANGE

,

VALUE_RANGE_MAX_INCLUSIVE

,

VALUE_RANGE_MAX_INCLUSIVE_MASK

,

VALUE_RANGE_MIN_INCLUSIVE

,

VALUE_RANGE_MIN_INCLUSIVE_MASK

,

VALUE_RANGE_MIN_MAX_INCLUSIVE

---

#### Field Summary

A

String

constant containing the standard format
name,

"javax_imageio_1.0"

.

Fields declared in interface javax.imageio.metadata.

IIOMetadataFormat

CHILD_POLICY_ALL

,

CHILD_POLICY_CHOICE

,

CHILD_POLICY_EMPTY

,

CHILD_POLICY_MAX

,

CHILD_POLICY_REPEAT

,

CHILD_POLICY_SEQUENCE

,

CHILD_POLICY_SOME

,

DATATYPE_BOOLEAN

,

DATATYPE_DOUBLE

,

DATATYPE_FLOAT

,

DATATYPE_INTEGER

,

DATATYPE_STRING

,

VALUE_ARBITRARY

,

VALUE_ENUMERATION

,

VALUE_LIST

,

VALUE_NONE

,

VALUE_RANGE

,

VALUE_RANGE_MAX_INCLUSIVE

,

VALUE_RANGE_MAX_INCLUSIVE_MASK

,

VALUE_RANGE_MIN_INCLUSIVE

,

VALUE_RANGE_MIN_INCLUSIVE_MASK

,

VALUE_RANGE_MIN_MAX_INCLUSIVE

---

#### Fields declared in interface javax.imageio.metadata. IIOMetadataFormat

Constructor Summary

Constructors

Constructor

Description

IIOMetadataFormatImpl

​(

String

rootName,
int childPolicy)

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and child policy (other than

CHILD_POLICY_REPEAT

).

IIOMetadataFormatImpl

​(

String

rootName,
int minChildren,
int maxChildren)

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and a child policy of

CHILD_POLICY_REPEAT

.

---

#### Constructor Summary

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and child policy (other than

CHILD_POLICY_REPEAT

).

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and a child policy of

CHILD_POLICY_REPEAT

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addAttribute

​(

String

elementName,

String

attrName,
int dataType,
boolean required,
int listMinLength,
int listMaxLength)

Adds a new attribute to a previously defined element that will
be defined by a list of values.

protected void

addAttribute

​(

String

elementName,

String

attrName,
int dataType,
boolean required,

String

defaultValue)

Adds a new attribute to a previously defined element that may
be set to an arbitrary value.

protected void

addAttribute

​(

String

elementName,

String

attrName,
int dataType,
boolean required,

String

defaultValue,

String

minValue,

String

maxValue,
boolean minInclusive,
boolean maxInclusive)

Adds a new attribute to a previously defined element that will
be defined by a range of values.

protected void

addAttribute

​(

String

elementName,

String

attrName,
int dataType,
boolean required,

String

defaultValue,

List

<

String

> enumeratedValues)

Adds a new attribute to a previously defined element that will
be defined by a set of enumerated values.

protected void

addBooleanAttribute

​(

String

elementName,

String

attrName,
boolean hasDefaultValue,
boolean defaultValue)

Adds a new attribute to a previously defined element that will
be defined by the enumerated values

TRUE

and

FALSE

, with a datatype of

DATATYPE_BOOLEAN

.

protected void

addChildElement

​(

String

elementName,

String

parentName)

Adds an existing element to the list of legal children for a
given parent node type.

protected void

addElement

​(

String

elementName,

String

parentName,
int childPolicy)

Adds a new element type to this metadata document format with a
child policy other than

CHILD_POLICY_REPEAT

.

protected void

addElement

​(

String

elementName,

String

parentName,
int minChildren,
int maxChildren)

Adds a new element type to this metadata document format with a
child policy of

CHILD_POLICY_REPEAT

.

protected void

addObjectValue

​(

String

elementName,

Class

<?> classType,
int arrayMinLength,
int arrayMaxLength)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element.

protected <T> void

addObjectValue

​(

String

elementName,

Class

<T> classType,
boolean required,
T defaultValue)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element.

protected <T> void

addObjectValue

​(

String

elementName,

Class

<T> classType,
boolean required,
T defaultValue,

List

<? extends T> enumeratedValues)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element.

protected <T extends

Object

&

Comparable

<? super T>>

void

addObjectValue

​(

String

elementName,

Class

<T> classType,
T defaultValue,

Comparable

<? super T> minValue,

Comparable

<? super T> maxValue,
boolean minInclusive,
boolean maxInclusive)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element.

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

protected

String

getResourceBaseName

()

Returns the currently set base name for locating

ResourceBundle

s.

static

IIOMetadataFormat

getStandardFormatInstance

()

Returns an

IIOMetadataFormat

object describing the
standard, plug-in neutral

javax.imageio_1.0

metadata document format described in the comment of the

javax.imageio.metadata

package.

protected void

removeAttribute

​(

String

elementName,

String

attrName)

Removes an attribute from a previously defined element.

protected void

removeElement

​(

String

elementName)

Removes an element from the format.

protected void

removeObjectValue

​(

String

elementName)

Disallows an

Object

reference from being stored in
nodes implementing the named element.

protected void

setResourceBaseName

​(

String

resourceBaseName)

Sets a new base name for locating

ResourceBundle

s
containing descriptions of elements and attributes for this
format.

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

- Methods declared in interface javax.imageio.metadata.

IIOMetadataFormat

canNodeAppear

,

getAttributeDataType

,

getAttributeDefaultValue

,

getAttributeEnumerations

,

getAttributeListMaxLength

,

getAttributeListMinLength

,

getAttributeMaxValue

,

getAttributeMinValue

,

getAttributeNames

,

getAttributeValueType

,

getChildNames

,

getChildPolicy

,

getElementMaxChildren

,

getElementMinChildren

,

getObjectArrayMaxLength

,

getObjectArrayMinLength

,

getObjectClass

,

getObjectDefaultValue

,

getObjectEnumerations

,

getObjectMaxValue

,

getObjectMinValue

,

getObjectValueType

,

getRootName

,

isAttributeRequired

---

#### Method Summary

Adds a new attribute to a previously defined element that will
be defined by a list of values.

Adds a new attribute to a previously defined element that may
be set to an arbitrary value.

Adds a new attribute to a previously defined element that will
be defined by a range of values.

Adds a new attribute to a previously defined element that will
be defined by a set of enumerated values.

Adds a new attribute to a previously defined element that will
be defined by the enumerated values

TRUE

and

FALSE

, with a datatype of

DATATYPE_BOOLEAN

.

Adds an existing element to the list of legal children for a
given parent node type.

Adds a new element type to this metadata document format with a
child policy other than

CHILD_POLICY_REPEAT

.

Adds a new element type to this metadata document format with a
child policy of

CHILD_POLICY_REPEAT

.

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element.

Returns a

String

containing a description of the
named attribute, or

null

.

Returns a

String

containing a description of the
named element, or

null

.

Returns the currently set base name for locating

ResourceBundle

s.

Returns an

IIOMetadataFormat

object describing the
standard, plug-in neutral

javax.imageio_1.0

metadata document format described in the comment of the

javax.imageio.metadata

package.

Removes an attribute from a previously defined element.

Removes an element from the format.

Disallows an

Object

reference from being stored in
nodes implementing the named element.

Sets a new base name for locating

ResourceBundle

s
containing descriptions of elements and attributes for this
format.

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

Methods declared in interface javax.imageio.metadata.

IIOMetadataFormat

canNodeAppear

,

getAttributeDataType

,

getAttributeDefaultValue

,

getAttributeEnumerations

,

getAttributeListMaxLength

,

getAttributeListMinLength

,

getAttributeMaxValue

,

getAttributeMinValue

,

getAttributeNames

,

getAttributeValueType

,

getChildNames

,

getChildPolicy

,

getElementMaxChildren

,

getElementMinChildren

,

getObjectArrayMaxLength

,

getObjectArrayMinLength

,

getObjectClass

,

getObjectDefaultValue

,

getObjectEnumerations

,

getObjectMaxValue

,

getObjectMinValue

,

getObjectValueType

,

getRootName

,

isAttributeRequired

---

#### Methods declared in interface javax.imageio.metadata. IIOMetadataFormat

============ FIELD DETAIL ===========

- Field Detail

- standardMetadataFormatName

```java
public static final
String
standardMetadataFormatName
```

A

String

constant containing the standard format
name,

"javax_imageio_1.0"

.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- IIOMetadataFormatImpl

```java
public IIOMetadataFormatImpl​(
String
rootName,
int childPolicy)
```

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and child policy (other than

CHILD_POLICY_REPEAT

). Additional elements, and
their attributes and

Object

reference information
may be added using the various

add

methods.

**Parameters:** rootName

- the name of the root element.
**Parameters:** childPolicy

- one of the

CHILD_POLICY_*

constants,
other than

CHILD_POLICY_REPEAT

.
**Throws:** IllegalArgumentException

- if

rootName

is

null

.
**Throws:** IllegalArgumentException

- if

childPolicy

is
not one of the predefined constants.

- IIOMetadataFormatImpl

```java
public IIOMetadataFormatImpl​(
String
rootName,
int minChildren,
int maxChildren)
```

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and a child policy of

CHILD_POLICY_REPEAT

. Additional elements, and
their attributes and

Object

reference information
may be added using the various

add

methods.

**Parameters:** rootName

- the name of the root element.
**Parameters:** minChildren

- the minimum number of children of the node.
**Parameters:** maxChildren

- the maximum number of children of the node.
**Throws:** IllegalArgumentException

- if

rootName

is

null

.
**Throws:** IllegalArgumentException

- if

minChildren

is negative or larger than

maxChildren

.

============ METHOD DETAIL ==========

- Method Detail

- setResourceBaseName

```java
protected void setResourceBaseName​(
String
resourceBaseName)
```

Sets a new base name for locating

ResourceBundle

s
containing descriptions of elements and attributes for this
format.

Prior to the first time this method is called, the base
name will be equal to

this.getClass().getName() + "Resources"

.

**Parameters:** resourceBaseName

- a

String

containing the new
base name.
**Throws:** IllegalArgumentException

- if

resourceBaseName

is

null

.
**See Also:** getResourceBaseName()

- getResourceBaseName

```java
protected
String
getResourceBaseName()
```

Returns the currently set base name for locating

ResourceBundle

s.

**Returns:** a

String

containing the base name.
**See Also:** setResourceBaseName(java.lang.String)

- addElement

```java
protected void addElement​(
String
elementName,

String
parentName,
int childPolicy)
```

Adds a new element type to this metadata document format with a
child policy other than

CHILD_POLICY_REPEAT

.

**Parameters:** elementName

- the name of the new element.
**Parameters:** parentName

- the name of the element that will be the
parent of the new element.
**Parameters:** childPolicy

- one of the

CHILD_POLICY_*

constants, other than

CHILD_POLICY_REPEAT

,
indicating the child policy of the new element.
**Throws:** IllegalArgumentException

- if

parentName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

childPolicy

is not one of the predefined constants.

- addElement

```java
protected void addElement​(
String
elementName,

String
parentName,
int minChildren,
int maxChildren)
```

Adds a new element type to this metadata document format with a
child policy of

CHILD_POLICY_REPEAT

.

**Parameters:** elementName

- the name of the new element.
**Parameters:** parentName

- the name of the element that will be the
parent of the new element.
**Parameters:** minChildren

- the minimum number of children of the node.
**Parameters:** maxChildren

- the maximum number of children of the node.
**Throws:** IllegalArgumentException

- if

parentName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

minChildren

is negative or larger than

maxChildren

.

- addChildElement

```java
protected void addChildElement​(
String
elementName,

String
parentName)
```

Adds an existing element to the list of legal children for a
given parent node type.

**Parameters:** parentName

- the name of the element that will be the
new parent of the element.
**Parameters:** elementName

- the name of the element to be added as a
child.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

parentName

is

null

, or is not a legal element name for this
format.

- removeElement

```java
protected void removeElement​(
String
elementName)
```

Removes an element from the format. If no element with the
given name was present, nothing happens and no exception is
thrown.

**Parameters:** elementName

- the name of the element to be removed.

- addAttribute

```java
protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,

String
defaultValue)
```

Adds a new attribute to a previously defined element that may
be set to an arbitrary value.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
**Parameters:** required

-

true

if the attribute must be present.
**Parameters:** defaultValue

- the default value for the attribute, or

null

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the predefined constants.

- addAttribute

```java
protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,

String
defaultValue,

List
<
String
> enumeratedValues)
```

Adds a new attribute to a previously defined element that will
be defined by a set of enumerated values.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
**Parameters:** required

-

true

if the attribute must be present.
**Parameters:** defaultValue

- the default value for the attribute, or

null

.
**Parameters:** enumeratedValues

- a

List

of

String

s containing the legal values for the
attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the predefined constants.
**Throws:** IllegalArgumentException

- if

enumeratedValues

is

null

.
**Throws:** IllegalArgumentException

- if

enumeratedValues

does not contain at least one
entry.
**Throws:** IllegalArgumentException

- if

enumeratedValues

contains an element that is not a

String

or is

null

.

- addAttribute

```java
protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,

String
defaultValue,

String
minValue,

String
maxValue,
boolean minInclusive,
boolean maxInclusive)
```

Adds a new attribute to a previously defined element that will
be defined by a range of values.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
**Parameters:** required

-

true

if the attribute must be present.
**Parameters:** defaultValue

- the default value for the attribute, or

null

.
**Parameters:** minValue

- the smallest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
attribute, as a

String

.
**Parameters:** maxValue

- the largest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
attribute, as a

String

.
**Parameters:** minInclusive

-

true

if

minValue

is inclusive.
**Parameters:** maxInclusive

-

true

if

maxValue

is inclusive.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the predefined constants.

- addAttribute

```java
protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,
int listMinLength,
int listMaxLength)
```

Adds a new attribute to a previously defined element that will
be defined by a list of values.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
**Parameters:** required

-

true

if the attribute must be present.
**Parameters:** listMinLength

- the smallest legal number of list items.
**Parameters:** listMaxLength

- the largest legal number of list items.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the predefined constants.
**Throws:** IllegalArgumentException

- if

listMinLength

is negative or larger than

listMaxLength

.

- addBooleanAttribute

```java
protected void addBooleanAttribute​(
String
elementName,

String
attrName,
boolean hasDefaultValue,
boolean defaultValue)
```

Adds a new attribute to a previously defined element that will
be defined by the enumerated values

TRUE

and

FALSE

, with a datatype of

DATATYPE_BOOLEAN

.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** hasDefaultValue

-

true

if a default value
should be present.
**Parameters:** defaultValue

- the default value for the attribute as a

boolean

, ignored if

hasDefaultValue

is

false

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.

- removeAttribute

```java
protected void removeAttribute​(
String
elementName,

String
attrName)
```

Removes an attribute from a previously defined element. If no
attribute with the given name was present in the given element,
nothing happens and no exception is thrown.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being removed.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.

- addObjectValue

```java
protected <T> void addObjectValue​(
String
elementName,

Class
<T> classType,
boolean required,
T defaultValue)
```

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

is unconstrained other than by
its class type.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Type Parameters:** T

- the type of the object.
**Parameters:** elementName

- the name of the element.
**Parameters:** classType

- a

Class

variable indicating the
legal class type for the object value.
**Parameters:** required

-

true

if an object value must be present.
**Parameters:** defaultValue

- the default value for the

Object

reference, or

null

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.

- addObjectValue

```java
protected <T> void addObjectValue​(
String
elementName,

Class
<T> classType,
boolean required,
T defaultValue,

List
<? extends T> enumeratedValues)
```

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must be one of the values
given by

enumeratedValues

.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Type Parameters:** T

- the type of the object.
**Parameters:** elementName

- the name of the element.
**Parameters:** classType

- a

Class

variable indicating the
legal class type for the object value.
**Parameters:** required

-

true

if an object value must be present.
**Parameters:** defaultValue

- the default value for the

Object

reference, or

null

.
**Parameters:** enumeratedValues

- a

List

of

Object

s containing the legal values for the
object reference.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.
**Throws:** IllegalArgumentException

- if

enumeratedValues

is

null

.
**Throws:** IllegalArgumentException

- if

enumeratedValues

does not contain at least one
entry.
**Throws:** IllegalArgumentException

- if

enumeratedValues

contains an element that is not
an instance of the class type denoted by

classType

or is

null

.

- addObjectValue

```java
protected <T extends
Object
&
Comparable
<? super T>> void addObjectValue​(
String
elementName,

Class
<T> classType,
T defaultValue,

Comparable
<? super T> minValue,

Comparable
<? super T> maxValue,
boolean minInclusive,
boolean maxInclusive)
```

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must be within the range given
by

minValue

and

maxValue

.
Furthermore, the class type must implement the

Comparable

interface.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Type Parameters:** T

- the type of the object.
**Parameters:** elementName

- the name of the element.
**Parameters:** classType

- a

Class

variable indicating the
legal class type for the object value.
**Parameters:** defaultValue

- the default value for the
**Parameters:** minValue

- the smallest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
object value, as a

String

.
**Parameters:** maxValue

- the largest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
object value, as a

String

.
**Parameters:** minInclusive

-

true

if

minValue

is inclusive.
**Parameters:** maxInclusive

-

true

if

maxValue

is inclusive.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.

- addObjectValue

```java
protected void addObjectValue​(
String
elementName,

Class
<?> classType,
int arrayMinLength,
int arrayMaxLength)
```

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must an array of objects of
class type given by

classType

, with at least

arrayMinLength

and at most

arrayMaxLength

elements.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Parameters:** elementName

- the name of the element.
**Parameters:** classType

- a

Class

variable indicating the
legal class type for the object value.
**Parameters:** arrayMinLength

- the smallest legal length for the array.
**Parameters:** arrayMaxLength

- the largest legal length for the array.
**Throws:** IllegalArgumentException

- if

elementName

is
not a legal element name for this format.

- removeObjectValue

```java
protected void removeObjectValue​(
String
elementName)
```

Disallows an

Object

reference from being stored in
nodes implementing the named element.

**Parameters:** elementName

- the name of the element.
**Throws:** IllegalArgumentException

- if

elementName

is
not a legal element name for this format.

- getElementDescription

```java
public
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

The default implementation will first locate a

ResourceBundle

using the current resource base
name set by

setResourceBaseName

and the supplied

Locale

, using the fallback mechanism described in
the comments for

ResourceBundle.getBundle

. If a

ResourceBundle

is found, the element name will be
used as a key to its

getString

method, and the
result returned. If no

ResourceBundle

is found,
or no such key is present,

null

will be returned.

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

**Specified by:** getElementDescription

in interface

IIOMetadataFormat
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
**See Also:** setResourceBaseName(java.lang.String)

- getAttributeDescription

```java
public
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

The default implementation will first locate a

ResourceBundle

using the current resource base
name set by

setResourceBaseName

and the supplied

Locale

, using the fallback mechanism described in
the comments for

ResourceBundle.getBundle

. If a

ResourceBundle

is found, the element name followed
by a "/" character followed by the attribute name
(

elementName + "/" + attrName

) will be used as a
key to its

getString

method, and the result
returned. If no

ResourceBundle

is found, or no
such key is present,

null

will be returned.

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

**Specified by:** getAttributeDescription

in interface

IIOMetadataFormat
**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute.
**Parameters:** locale

- the

Locale

for which localization
will be attempted, or

null

.
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
**See Also:** setResourceBaseName(java.lang.String)

- getStandardFormatInstance

```java
public static
IIOMetadataFormat
getStandardFormatInstance()
```

Returns an

IIOMetadataFormat

object describing the
standard, plug-in neutral

javax.imageio_1.0

metadata document format described in the comment of the

javax.imageio.metadata

package.

**Returns:** a predefined

IIOMetadataFormat

instance.

Field Detail

- standardMetadataFormatName

```java
public static final
String
standardMetadataFormatName
```

A

String

constant containing the standard format
name,

"javax_imageio_1.0"

.

**See Also:** Constant Field Values

---

#### Field Detail

standardMetadataFormatName

```java
public static final
String
standardMetadataFormatName
```

A

String

constant containing the standard format
name,

"javax_imageio_1.0"

.

**See Also:** Constant Field Values

---

#### standardMetadataFormatName

public static final

String

standardMetadataFormatName

A

String

constant containing the standard format
name,

"javax_imageio_1.0"

.

Constructor Detail

- IIOMetadataFormatImpl

```java
public IIOMetadataFormatImpl​(
String
rootName,
int childPolicy)
```

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and child policy (other than

CHILD_POLICY_REPEAT

). Additional elements, and
their attributes and

Object

reference information
may be added using the various

add

methods.

**Parameters:** rootName

- the name of the root element.
**Parameters:** childPolicy

- one of the

CHILD_POLICY_*

constants,
other than

CHILD_POLICY_REPEAT

.
**Throws:** IllegalArgumentException

- if

rootName

is

null

.
**Throws:** IllegalArgumentException

- if

childPolicy

is
not one of the predefined constants.

- IIOMetadataFormatImpl

```java
public IIOMetadataFormatImpl​(
String
rootName,
int minChildren,
int maxChildren)
```

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and a child policy of

CHILD_POLICY_REPEAT

. Additional elements, and
their attributes and

Object

reference information
may be added using the various

add

methods.

**Parameters:** rootName

- the name of the root element.
**Parameters:** minChildren

- the minimum number of children of the node.
**Parameters:** maxChildren

- the maximum number of children of the node.
**Throws:** IllegalArgumentException

- if

rootName

is

null

.
**Throws:** IllegalArgumentException

- if

minChildren

is negative or larger than

maxChildren

.

---

#### Constructor Detail

IIOMetadataFormatImpl

```java
public IIOMetadataFormatImpl​(
String
rootName,
int childPolicy)
```

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and child policy (other than

CHILD_POLICY_REPEAT

). Additional elements, and
their attributes and

Object

reference information
may be added using the various

add

methods.

**Parameters:** rootName

- the name of the root element.
**Parameters:** childPolicy

- one of the

CHILD_POLICY_*

constants,
other than

CHILD_POLICY_REPEAT

.
**Throws:** IllegalArgumentException

- if

rootName

is

null

.
**Throws:** IllegalArgumentException

- if

childPolicy

is
not one of the predefined constants.

---

#### IIOMetadataFormatImpl

public IIOMetadataFormatImpl​(

String

rootName,
int childPolicy)

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and child policy (other than

CHILD_POLICY_REPEAT

). Additional elements, and
their attributes and

Object

reference information
may be added using the various

add

methods.

IIOMetadataFormatImpl

```java
public IIOMetadataFormatImpl​(
String
rootName,
int minChildren,
int maxChildren)
```

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and a child policy of

CHILD_POLICY_REPEAT

. Additional elements, and
their attributes and

Object

reference information
may be added using the various

add

methods.

**Parameters:** rootName

- the name of the root element.
**Parameters:** minChildren

- the minimum number of children of the node.
**Parameters:** maxChildren

- the maximum number of children of the node.
**Throws:** IllegalArgumentException

- if

rootName

is

null

.
**Throws:** IllegalArgumentException

- if

minChildren

is negative or larger than

maxChildren

.

---

#### IIOMetadataFormatImpl

public IIOMetadataFormatImpl​(

String

rootName,
int minChildren,
int maxChildren)

Constructs a blank

IIOMetadataFormatImpl

instance,
with a given root element name and a child policy of

CHILD_POLICY_REPEAT

. Additional elements, and
their attributes and

Object

reference information
may be added using the various

add

methods.

Method Detail

- setResourceBaseName

```java
protected void setResourceBaseName​(
String
resourceBaseName)
```

Sets a new base name for locating

ResourceBundle

s
containing descriptions of elements and attributes for this
format.

Prior to the first time this method is called, the base
name will be equal to

this.getClass().getName() + "Resources"

.

**Parameters:** resourceBaseName

- a

String

containing the new
base name.
**Throws:** IllegalArgumentException

- if

resourceBaseName

is

null

.
**See Also:** getResourceBaseName()

- getResourceBaseName

```java
protected
String
getResourceBaseName()
```

Returns the currently set base name for locating

ResourceBundle

s.

**Returns:** a

String

containing the base name.
**See Also:** setResourceBaseName(java.lang.String)

- addElement

```java
protected void addElement​(
String
elementName,

String
parentName,
int childPolicy)
```

Adds a new element type to this metadata document format with a
child policy other than

CHILD_POLICY_REPEAT

.

**Parameters:** elementName

- the name of the new element.
**Parameters:** parentName

- the name of the element that will be the
parent of the new element.
**Parameters:** childPolicy

- one of the

CHILD_POLICY_*

constants, other than

CHILD_POLICY_REPEAT

,
indicating the child policy of the new element.
**Throws:** IllegalArgumentException

- if

parentName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

childPolicy

is not one of the predefined constants.

- addElement

```java
protected void addElement​(
String
elementName,

String
parentName,
int minChildren,
int maxChildren)
```

Adds a new element type to this metadata document format with a
child policy of

CHILD_POLICY_REPEAT

.

**Parameters:** elementName

- the name of the new element.
**Parameters:** parentName

- the name of the element that will be the
parent of the new element.
**Parameters:** minChildren

- the minimum number of children of the node.
**Parameters:** maxChildren

- the maximum number of children of the node.
**Throws:** IllegalArgumentException

- if

parentName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

minChildren

is negative or larger than

maxChildren

.

- addChildElement

```java
protected void addChildElement​(
String
elementName,

String
parentName)
```

Adds an existing element to the list of legal children for a
given parent node type.

**Parameters:** parentName

- the name of the element that will be the
new parent of the element.
**Parameters:** elementName

- the name of the element to be added as a
child.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

parentName

is

null

, or is not a legal element name for this
format.

- removeElement

```java
protected void removeElement​(
String
elementName)
```

Removes an element from the format. If no element with the
given name was present, nothing happens and no exception is
thrown.

**Parameters:** elementName

- the name of the element to be removed.

- addAttribute

```java
protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,

String
defaultValue)
```

Adds a new attribute to a previously defined element that may
be set to an arbitrary value.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
**Parameters:** required

-

true

if the attribute must be present.
**Parameters:** defaultValue

- the default value for the attribute, or

null

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the predefined constants.

- addAttribute

```java
protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,

String
defaultValue,

List
<
String
> enumeratedValues)
```

Adds a new attribute to a previously defined element that will
be defined by a set of enumerated values.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
**Parameters:** required

-

true

if the attribute must be present.
**Parameters:** defaultValue

- the default value for the attribute, or

null

.
**Parameters:** enumeratedValues

- a

List

of

String

s containing the legal values for the
attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the predefined constants.
**Throws:** IllegalArgumentException

- if

enumeratedValues

is

null

.
**Throws:** IllegalArgumentException

- if

enumeratedValues

does not contain at least one
entry.
**Throws:** IllegalArgumentException

- if

enumeratedValues

contains an element that is not a

String

or is

null

.

- addAttribute

```java
protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,

String
defaultValue,

String
minValue,

String
maxValue,
boolean minInclusive,
boolean maxInclusive)
```

Adds a new attribute to a previously defined element that will
be defined by a range of values.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
**Parameters:** required

-

true

if the attribute must be present.
**Parameters:** defaultValue

- the default value for the attribute, or

null

.
**Parameters:** minValue

- the smallest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
attribute, as a

String

.
**Parameters:** maxValue

- the largest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
attribute, as a

String

.
**Parameters:** minInclusive

-

true

if

minValue

is inclusive.
**Parameters:** maxInclusive

-

true

if

maxValue

is inclusive.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the predefined constants.

- addAttribute

```java
protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,
int listMinLength,
int listMaxLength)
```

Adds a new attribute to a previously defined element that will
be defined by a list of values.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
**Parameters:** required

-

true

if the attribute must be present.
**Parameters:** listMinLength

- the smallest legal number of list items.
**Parameters:** listMaxLength

- the largest legal number of list items.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the predefined constants.
**Throws:** IllegalArgumentException

- if

listMinLength

is negative or larger than

listMaxLength

.

- addBooleanAttribute

```java
protected void addBooleanAttribute​(
String
elementName,

String
attrName,
boolean hasDefaultValue,
boolean defaultValue)
```

Adds a new attribute to a previously defined element that will
be defined by the enumerated values

TRUE

and

FALSE

, with a datatype of

DATATYPE_BOOLEAN

.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** hasDefaultValue

-

true

if a default value
should be present.
**Parameters:** defaultValue

- the default value for the attribute as a

boolean

, ignored if

hasDefaultValue

is

false

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.

- removeAttribute

```java
protected void removeAttribute​(
String
elementName,

String
attrName)
```

Removes an attribute from a previously defined element. If no
attribute with the given name was present in the given element,
nothing happens and no exception is thrown.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being removed.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.

- addObjectValue

```java
protected <T> void addObjectValue​(
String
elementName,

Class
<T> classType,
boolean required,
T defaultValue)
```

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

is unconstrained other than by
its class type.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Type Parameters:** T

- the type of the object.
**Parameters:** elementName

- the name of the element.
**Parameters:** classType

- a

Class

variable indicating the
legal class type for the object value.
**Parameters:** required

-

true

if an object value must be present.
**Parameters:** defaultValue

- the default value for the

Object

reference, or

null

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.

- addObjectValue

```java
protected <T> void addObjectValue​(
String
elementName,

Class
<T> classType,
boolean required,
T defaultValue,

List
<? extends T> enumeratedValues)
```

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must be one of the values
given by

enumeratedValues

.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Type Parameters:** T

- the type of the object.
**Parameters:** elementName

- the name of the element.
**Parameters:** classType

- a

Class

variable indicating the
legal class type for the object value.
**Parameters:** required

-

true

if an object value must be present.
**Parameters:** defaultValue

- the default value for the

Object

reference, or

null

.
**Parameters:** enumeratedValues

- a

List

of

Object

s containing the legal values for the
object reference.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.
**Throws:** IllegalArgumentException

- if

enumeratedValues

is

null

.
**Throws:** IllegalArgumentException

- if

enumeratedValues

does not contain at least one
entry.
**Throws:** IllegalArgumentException

- if

enumeratedValues

contains an element that is not
an instance of the class type denoted by

classType

or is

null

.

- addObjectValue

```java
protected <T extends
Object
&
Comparable
<? super T>> void addObjectValue​(
String
elementName,

Class
<T> classType,
T defaultValue,

Comparable
<? super T> minValue,

Comparable
<? super T> maxValue,
boolean minInclusive,
boolean maxInclusive)
```

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must be within the range given
by

minValue

and

maxValue

.
Furthermore, the class type must implement the

Comparable

interface.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Type Parameters:** T

- the type of the object.
**Parameters:** elementName

- the name of the element.
**Parameters:** classType

- a

Class

variable indicating the
legal class type for the object value.
**Parameters:** defaultValue

- the default value for the
**Parameters:** minValue

- the smallest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
object value, as a

String

.
**Parameters:** maxValue

- the largest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
object value, as a

String

.
**Parameters:** minInclusive

-

true

if

minValue

is inclusive.
**Parameters:** maxInclusive

-

true

if

maxValue

is inclusive.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.

- addObjectValue

```java
protected void addObjectValue​(
String
elementName,

Class
<?> classType,
int arrayMinLength,
int arrayMaxLength)
```

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must an array of objects of
class type given by

classType

, with at least

arrayMinLength

and at most

arrayMaxLength

elements.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Parameters:** elementName

- the name of the element.
**Parameters:** classType

- a

Class

variable indicating the
legal class type for the object value.
**Parameters:** arrayMinLength

- the smallest legal length for the array.
**Parameters:** arrayMaxLength

- the largest legal length for the array.
**Throws:** IllegalArgumentException

- if

elementName

is
not a legal element name for this format.

- removeObjectValue

```java
protected void removeObjectValue​(
String
elementName)
```

Disallows an

Object

reference from being stored in
nodes implementing the named element.

**Parameters:** elementName

- the name of the element.
**Throws:** IllegalArgumentException

- if

elementName

is
not a legal element name for this format.

- getElementDescription

```java
public
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

The default implementation will first locate a

ResourceBundle

using the current resource base
name set by

setResourceBaseName

and the supplied

Locale

, using the fallback mechanism described in
the comments for

ResourceBundle.getBundle

. If a

ResourceBundle

is found, the element name will be
used as a key to its

getString

method, and the
result returned. If no

ResourceBundle

is found,
or no such key is present,

null

will be returned.

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

**Specified by:** getElementDescription

in interface

IIOMetadataFormat
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
**See Also:** setResourceBaseName(java.lang.String)

- getAttributeDescription

```java
public
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

The default implementation will first locate a

ResourceBundle

using the current resource base
name set by

setResourceBaseName

and the supplied

Locale

, using the fallback mechanism described in
the comments for

ResourceBundle.getBundle

. If a

ResourceBundle

is found, the element name followed
by a "/" character followed by the attribute name
(

elementName + "/" + attrName

) will be used as a
key to its

getString

method, and the result
returned. If no

ResourceBundle

is found, or no
such key is present,

null

will be returned.

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

**Specified by:** getAttributeDescription

in interface

IIOMetadataFormat
**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute.
**Parameters:** locale

- the

Locale

for which localization
will be attempted, or

null

.
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
**See Also:** setResourceBaseName(java.lang.String)

- getStandardFormatInstance

```java
public static
IIOMetadataFormat
getStandardFormatInstance()
```

Returns an

IIOMetadataFormat

object describing the
standard, plug-in neutral

javax.imageio_1.0

metadata document format described in the comment of the

javax.imageio.metadata

package.

**Returns:** a predefined

IIOMetadataFormat

instance.

---

#### Method Detail

setResourceBaseName

```java
protected void setResourceBaseName​(
String
resourceBaseName)
```

Sets a new base name for locating

ResourceBundle

s
containing descriptions of elements and attributes for this
format.

Prior to the first time this method is called, the base
name will be equal to

this.getClass().getName() + "Resources"

.

**Parameters:** resourceBaseName

- a

String

containing the new
base name.
**Throws:** IllegalArgumentException

- if

resourceBaseName

is

null

.
**See Also:** getResourceBaseName()

---

#### setResourceBaseName

protected void setResourceBaseName​(

String

resourceBaseName)

Sets a new base name for locating

ResourceBundle

s
containing descriptions of elements and attributes for this
format.

Prior to the first time this method is called, the base
name will be equal to

this.getClass().getName() + "Resources"

.

Prior to the first time this method is called, the base
name will be equal to

this.getClass().getName() + "Resources"

.

getResourceBaseName

```java
protected
String
getResourceBaseName()
```

Returns the currently set base name for locating

ResourceBundle

s.

**Returns:** a

String

containing the base name.
**See Also:** setResourceBaseName(java.lang.String)

---

#### getResourceBaseName

protected

String

getResourceBaseName()

Returns the currently set base name for locating

ResourceBundle

s.

addElement

```java
protected void addElement​(
String
elementName,

String
parentName,
int childPolicy)
```

Adds a new element type to this metadata document format with a
child policy other than

CHILD_POLICY_REPEAT

.

**Parameters:** elementName

- the name of the new element.
**Parameters:** parentName

- the name of the element that will be the
parent of the new element.
**Parameters:** childPolicy

- one of the

CHILD_POLICY_*

constants, other than

CHILD_POLICY_REPEAT

,
indicating the child policy of the new element.
**Throws:** IllegalArgumentException

- if

parentName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

childPolicy

is not one of the predefined constants.

---

#### addElement

protected void addElement​(

String

elementName,

String

parentName,
int childPolicy)

Adds a new element type to this metadata document format with a
child policy other than

CHILD_POLICY_REPEAT

.

addElement

```java
protected void addElement​(
String
elementName,

String
parentName,
int minChildren,
int maxChildren)
```

Adds a new element type to this metadata document format with a
child policy of

CHILD_POLICY_REPEAT

.

**Parameters:** elementName

- the name of the new element.
**Parameters:** parentName

- the name of the element that will be the
parent of the new element.
**Parameters:** minChildren

- the minimum number of children of the node.
**Parameters:** maxChildren

- the maximum number of children of the node.
**Throws:** IllegalArgumentException

- if

parentName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

minChildren

is negative or larger than

maxChildren

.

---

#### addElement

protected void addElement​(

String

elementName,

String

parentName,
int minChildren,
int maxChildren)

Adds a new element type to this metadata document format with a
child policy of

CHILD_POLICY_REPEAT

.

addChildElement

```java
protected void addChildElement​(
String
elementName,

String
parentName)
```

Adds an existing element to the list of legal children for a
given parent node type.

**Parameters:** parentName

- the name of the element that will be the
new parent of the element.
**Parameters:** elementName

- the name of the element to be added as a
child.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

parentName

is

null

, or is not a legal element name for this
format.

---

#### addChildElement

protected void addChildElement​(

String

elementName,

String

parentName)

Adds an existing element to the list of legal children for a
given parent node type.

removeElement

```java
protected void removeElement​(
String
elementName)
```

Removes an element from the format. If no element with the
given name was present, nothing happens and no exception is
thrown.

**Parameters:** elementName

- the name of the element to be removed.

---

#### removeElement

protected void removeElement​(

String

elementName)

Removes an element from the format. If no element with the
given name was present, nothing happens and no exception is
thrown.

addAttribute

```java
protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,

String
defaultValue)
```

Adds a new attribute to a previously defined element that may
be set to an arbitrary value.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
**Parameters:** required

-

true

if the attribute must be present.
**Parameters:** defaultValue

- the default value for the attribute, or

null

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the predefined constants.

---

#### addAttribute

protected void addAttribute​(

String

elementName,

String

attrName,
int dataType,
boolean required,

String

defaultValue)

Adds a new attribute to a previously defined element that may
be set to an arbitrary value.

addAttribute

```java
protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,

String
defaultValue,

List
<
String
> enumeratedValues)
```

Adds a new attribute to a previously defined element that will
be defined by a set of enumerated values.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
**Parameters:** required

-

true

if the attribute must be present.
**Parameters:** defaultValue

- the default value for the attribute, or

null

.
**Parameters:** enumeratedValues

- a

List

of

String

s containing the legal values for the
attribute.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the predefined constants.
**Throws:** IllegalArgumentException

- if

enumeratedValues

is

null

.
**Throws:** IllegalArgumentException

- if

enumeratedValues

does not contain at least one
entry.
**Throws:** IllegalArgumentException

- if

enumeratedValues

contains an element that is not a

String

or is

null

.

---

#### addAttribute

protected void addAttribute​(

String

elementName,

String

attrName,
int dataType,
boolean required,

String

defaultValue,

List

<

String

> enumeratedValues)

Adds a new attribute to a previously defined element that will
be defined by a set of enumerated values.

addAttribute

```java
protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,

String
defaultValue,

String
minValue,

String
maxValue,
boolean minInclusive,
boolean maxInclusive)
```

Adds a new attribute to a previously defined element that will
be defined by a range of values.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
**Parameters:** required

-

true

if the attribute must be present.
**Parameters:** defaultValue

- the default value for the attribute, or

null

.
**Parameters:** minValue

- the smallest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
attribute, as a

String

.
**Parameters:** maxValue

- the largest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
attribute, as a

String

.
**Parameters:** minInclusive

-

true

if

minValue

is inclusive.
**Parameters:** maxInclusive

-

true

if

maxValue

is inclusive.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the predefined constants.

---

#### addAttribute

protected void addAttribute​(

String

elementName,

String

attrName,
int dataType,
boolean required,

String

defaultValue,

String

minValue,

String

maxValue,
boolean minInclusive,
boolean maxInclusive)

Adds a new attribute to a previously defined element that will
be defined by a range of values.

addAttribute

```java
protected void addAttribute​(
String
elementName,

String
attrName,
int dataType,
boolean required,
int listMinLength,
int listMaxLength)
```

Adds a new attribute to a previously defined element that will
be defined by a list of values.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** dataType

- the data type (string format) of the attribute,
one of the

DATATYPE_*

constants.
**Parameters:** required

-

true

if the attribute must be present.
**Parameters:** listMinLength

- the smallest legal number of list items.
**Parameters:** listMaxLength

- the largest legal number of list items.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the predefined constants.
**Throws:** IllegalArgumentException

- if

listMinLength

is negative or larger than

listMaxLength

.

---

#### addAttribute

protected void addAttribute​(

String

elementName,

String

attrName,
int dataType,
boolean required,
int listMinLength,
int listMaxLength)

Adds a new attribute to a previously defined element that will
be defined by a list of values.

addBooleanAttribute

```java
protected void addBooleanAttribute​(
String
elementName,

String
attrName,
boolean hasDefaultValue,
boolean defaultValue)
```

Adds a new attribute to a previously defined element that will
be defined by the enumerated values

TRUE

and

FALSE

, with a datatype of

DATATYPE_BOOLEAN

.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being added.
**Parameters:** hasDefaultValue

-

true

if a default value
should be present.
**Parameters:** defaultValue

- the default value for the attribute as a

boolean

, ignored if

hasDefaultValue

is

false

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.
**Throws:** IllegalArgumentException

- if

attrName

is

null

.

---

#### addBooleanAttribute

protected void addBooleanAttribute​(

String

elementName,

String

attrName,
boolean hasDefaultValue,
boolean defaultValue)

Adds a new attribute to a previously defined element that will
be defined by the enumerated values

TRUE

and

FALSE

, with a datatype of

DATATYPE_BOOLEAN

.

removeAttribute

```java
protected void removeAttribute​(
String
elementName,

String
attrName)
```

Removes an attribute from a previously defined element. If no
attribute with the given name was present in the given element,
nothing happens and no exception is thrown.

**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute being removed.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.

---

#### removeAttribute

protected void removeAttribute​(

String

elementName,

String

attrName)

Removes an attribute from a previously defined element. If no
attribute with the given name was present in the given element,
nothing happens and no exception is thrown.

addObjectValue

```java
protected <T> void addObjectValue​(
String
elementName,

Class
<T> classType,
boolean required,
T defaultValue)
```

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

is unconstrained other than by
its class type.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Type Parameters:** T

- the type of the object.
**Parameters:** elementName

- the name of the element.
**Parameters:** classType

- a

Class

variable indicating the
legal class type for the object value.
**Parameters:** required

-

true

if an object value must be present.
**Parameters:** defaultValue

- the default value for the

Object

reference, or

null

.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.

---

#### addObjectValue

protected <T> void addObjectValue​(

String

elementName,

Class

<T> classType,
boolean required,
T defaultValue)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

is unconstrained other than by
its class type.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

addObjectValue

```java
protected <T> void addObjectValue​(
String
elementName,

Class
<T> classType,
boolean required,
T defaultValue,

List
<? extends T> enumeratedValues)
```

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must be one of the values
given by

enumeratedValues

.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Type Parameters:** T

- the type of the object.
**Parameters:** elementName

- the name of the element.
**Parameters:** classType

- a

Class

variable indicating the
legal class type for the object value.
**Parameters:** required

-

true

if an object value must be present.
**Parameters:** defaultValue

- the default value for the

Object

reference, or

null

.
**Parameters:** enumeratedValues

- a

List

of

Object

s containing the legal values for the
object reference.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this format.
**Throws:** IllegalArgumentException

- if

enumeratedValues

is

null

.
**Throws:** IllegalArgumentException

- if

enumeratedValues

does not contain at least one
entry.
**Throws:** IllegalArgumentException

- if

enumeratedValues

contains an element that is not
an instance of the class type denoted by

classType

or is

null

.

---

#### addObjectValue

protected <T> void addObjectValue​(

String

elementName,

Class

<T> classType,
boolean required,
T defaultValue,

List

<? extends T> enumeratedValues)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must be one of the values
given by

enumeratedValues

.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

addObjectValue

```java
protected <T extends
Object
&
Comparable
<? super T>> void addObjectValue​(
String
elementName,

Class
<T> classType,
T defaultValue,

Comparable
<? super T> minValue,

Comparable
<? super T> maxValue,
boolean minInclusive,
boolean maxInclusive)
```

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must be within the range given
by

minValue

and

maxValue

.
Furthermore, the class type must implement the

Comparable

interface.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Type Parameters:** T

- the type of the object.
**Parameters:** elementName

- the name of the element.
**Parameters:** classType

- a

Class

variable indicating the
legal class type for the object value.
**Parameters:** defaultValue

- the default value for the
**Parameters:** minValue

- the smallest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
object value, as a

String

.
**Parameters:** maxValue

- the largest (inclusive or exclusive depending
on the value of

minInclusive

) legal value for the
object value, as a

String

.
**Parameters:** minInclusive

-

true

if

minValue

is inclusive.
**Parameters:** maxInclusive

-

true

if

maxValue

is inclusive.
**Throws:** IllegalArgumentException

- if

elementName

is

null

, or is not a legal element name for this
format.

---

#### addObjectValue

protected <T extends

Object

&

Comparable

<? super T>> void addObjectValue​(

String

elementName,

Class

<T> classType,
T defaultValue,

Comparable

<? super T> minValue,

Comparable

<? super T> maxValue,
boolean minInclusive,
boolean maxInclusive)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must be within the range given
by

minValue

and

maxValue

.
Furthermore, the class type must implement the

Comparable

interface.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

addObjectValue

```java
protected void addObjectValue​(
String
elementName,

Class
<?> classType,
int arrayMinLength,
int arrayMaxLength)
```

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must an array of objects of
class type given by

classType

, with at least

arrayMinLength

and at most

arrayMaxLength

elements.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

**Parameters:** elementName

- the name of the element.
**Parameters:** classType

- a

Class

variable indicating the
legal class type for the object value.
**Parameters:** arrayMinLength

- the smallest legal length for the array.
**Parameters:** arrayMaxLength

- the largest legal length for the array.
**Throws:** IllegalArgumentException

- if

elementName

is
not a legal element name for this format.

---

#### addObjectValue

protected void addObjectValue​(

String

elementName,

Class

<?> classType,
int arrayMinLength,
int arrayMaxLength)

Allows an

Object

reference of a given class type
to be stored in nodes implementing the named element. The
value of the

Object

must an array of objects of
class type given by

classType

, with at least

arrayMinLength

and at most

arrayMaxLength

elements.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

If an

Object

reference was previously allowed,
the previous settings are overwritten.

removeObjectValue

```java
protected void removeObjectValue​(
String
elementName)
```

Disallows an

Object

reference from being stored in
nodes implementing the named element.

**Parameters:** elementName

- the name of the element.
**Throws:** IllegalArgumentException

- if

elementName

is
not a legal element name for this format.

---

#### removeObjectValue

protected void removeObjectValue​(

String

elementName)

Disallows an

Object

reference from being stored in
nodes implementing the named element.

getElementDescription

```java
public
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

The default implementation will first locate a

ResourceBundle

using the current resource base
name set by

setResourceBaseName

and the supplied

Locale

, using the fallback mechanism described in
the comments for

ResourceBundle.getBundle

. If a

ResourceBundle

is found, the element name will be
used as a key to its

getString

method, and the
result returned. If no

ResourceBundle

is found,
or no such key is present,

null

will be returned.

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

**Specified by:** getElementDescription

in interface

IIOMetadataFormat
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
**See Also:** setResourceBaseName(java.lang.String)

---

#### getElementDescription

public

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

The default implementation will first locate a

ResourceBundle

using the current resource base
name set by

setResourceBaseName

and the supplied

Locale

, using the fallback mechanism described in
the comments for

ResourceBundle.getBundle

. If a

ResourceBundle

is found, the element name will be
used as a key to its

getString

method, and the
result returned. If no

ResourceBundle

is found,
or no such key is present,

null

will be returned.

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

The default implementation will first locate a

ResourceBundle

using the current resource base
name set by

setResourceBaseName

and the supplied

Locale

, using the fallback mechanism described in
the comments for

ResourceBundle.getBundle

. If a

ResourceBundle

is found, the element name will be
used as a key to its

getString

method, and the
result returned. If no

ResourceBundle

is found,
or no such key is present,

null

will be returned.

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

getAttributeDescription

```java
public
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

The default implementation will first locate a

ResourceBundle

using the current resource base
name set by

setResourceBaseName

and the supplied

Locale

, using the fallback mechanism described in
the comments for

ResourceBundle.getBundle

. If a

ResourceBundle

is found, the element name followed
by a "/" character followed by the attribute name
(

elementName + "/" + attrName

) will be used as a
key to its

getString

method, and the result
returned. If no

ResourceBundle

is found, or no
such key is present,

null

will be returned.

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

**Specified by:** getAttributeDescription

in interface

IIOMetadataFormat
**Parameters:** elementName

- the name of the element.
**Parameters:** attrName

- the name of the attribute.
**Parameters:** locale

- the

Locale

for which localization
will be attempted, or

null

.
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
**See Also:** setResourceBaseName(java.lang.String)

---

#### getAttributeDescription

public

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

The default implementation will first locate a

ResourceBundle

using the current resource base
name set by

setResourceBaseName

and the supplied

Locale

, using the fallback mechanism described in
the comments for

ResourceBundle.getBundle

. If a

ResourceBundle

is found, the element name followed
by a "/" character followed by the attribute name
(

elementName + "/" + attrName

) will be used as a
key to its

getString

method, and the result
returned. If no

ResourceBundle

is found, or no
such key is present,

null

will be returned.

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

The default implementation will first locate a

ResourceBundle

using the current resource base
name set by

setResourceBaseName

and the supplied

Locale

, using the fallback mechanism described in
the comments for

ResourceBundle.getBundle

. If a

ResourceBundle

is found, the element name followed
by a "/" character followed by the attribute name
(

elementName + "/" + attrName

) will be used as a
key to its

getString

method, and the result
returned. If no

ResourceBundle

is found, or no
such key is present,

null

will be returned.

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

getStandardFormatInstance

```java
public static
IIOMetadataFormat
getStandardFormatInstance()
```

Returns an

IIOMetadataFormat

object describing the
standard, plug-in neutral

javax.imageio_1.0

metadata document format described in the comment of the

javax.imageio.metadata

package.

**Returns:** a predefined

IIOMetadataFormat

instance.

---

#### getStandardFormatInstance

public static

IIOMetadataFormat

getStandardFormatInstance()

Returns an

IIOMetadataFormat

object describing the
standard, plug-in neutral

javax.imageio_1.0

metadata document format described in the comment of the

javax.imageio.metadata

package.

---

