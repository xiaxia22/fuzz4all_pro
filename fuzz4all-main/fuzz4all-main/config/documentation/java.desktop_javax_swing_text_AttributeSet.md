# Interface AttributeSet

**Source:** `java.desktop\javax\swing\text\AttributeSet.html`

### Class Description

```java
public interface
AttributeSet
```

A collection of unique attributes. This is a read-only,
immutable interface. An attribute is basically a key and
a value assigned to the key. The collection may represent
something like a style run, a logical style, etc. These
are generally used to describe features that will contribute
to some graphical representation such as a font. The
set of possible keys is unbounded and can be anything.
Typically View implementations will respond to attribute
definitions and render something to represent the attributes.

Attributes can potentially resolve in a hierarchy. If a
key doesn't resolve locally, and a resolving parent
exists, the key will be resolved through the parent.

**All Known Subinterfaces:** MutableAttributeSet

,

Style

---

### Field Details

#### static final
Object
NameAttribute

Attribute name used to name the collection of
attributes.

---

#### static final
Object
ResolveAttribute

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

---

### Constructor Details

*No entries found.*

### Method Details

#### int getAttributeCount()

Returns the number of attributes that are defined locally in this set.
Attributes that are defined in the parent set are not included.

**Returns:**
- the number of attributes >= 0

---

#### boolean isDefined​(
Object
attrName)

Checks whether the named attribute has a value specified in
the set without resolving through another attribute
set.

**Parameters:**
- attrName

- the attribute name

**Returns:**
- true if the attribute has a value specified

---

#### boolean isEqual​(
AttributeSet
attr)

Determines if the two attribute sets are equivalent.

**Parameters:**
- attr

- an attribute set

**Returns:**
- true if the sets are equivalent

---

#### AttributeSet
copyAttributes()

Returns an attribute set that is guaranteed not
to change over time.

**Returns:**
- a copy of the attribute set

---

#### Object
getAttribute​(
Object
key)

Fetches the value of the given attribute. If the value is not found
locally, the search is continued upward through the resolving
parent (if one exists) until the value is either
found or there are no more parents. If the value is not found,
null is returned.

**Parameters:**
- key

- the non-null key of the attribute binding

**Returns:**
- the value of the attribute, or

null

if not found

---

#### Enumeration
<?> getAttributeNames()

Returns an enumeration over the names of the attributes that are
defined locally in the set. Names of attributes defined in the
resolving parent, if any, are not included. The values of the

Enumeration

may be anything and are not constrained to
a particular

Object

type.

This method never returns

null

. For a set with no attributes, it
returns an empty

Enumeration

.

**Returns:**
- the names

---

#### boolean containsAttribute​(
Object
name,

Object
value)

Returns

true

if this set defines an attribute with the same
name and an equal value. If such an attribute is not found locally,
it is searched through in the resolving parent hierarchy.

**Parameters:**
- name

- the non-null attribute name
- value

- the value

**Returns:**
- true

if the set defines the attribute with an
equal value, either locally or through its resolving parent

**Throws:**
- NullPointerException

- if either

name

or

value

is

null

---

#### boolean containsAttributes​(
AttributeSet
attributes)

Returns

true

if this set defines all the attributes from the
given set with equal values. If an attribute is not found locally,
it is searched through in the resolving parent hierarchy.

**Parameters:**
- attributes

- the set of attributes to check against

**Returns:**
- true

if this set defines all the attributes with equal
values, either locally or through its resolving parent

**Throws:**
- NullPointerException

- if

attributes

is

null

---

#### AttributeSet
getResolveParent()

Gets the resolving parent.

**Returns:**
- the parent

---

### Additional Sections

#### Interface AttributeSet

**All Known Subinterfaces:** MutableAttributeSet

,

Style

**All Known Implementing Classes:** AbstractDocument.AbstractElement

,

AbstractDocument.BranchElement

,

AbstractDocument.LeafElement

,

DefaultStyledDocument.SectionElement

,

HTMLDocument.BlockElement

,

HTMLDocument.RunElement

,

SimpleAttributeSet

,

StyleContext.NamedStyle

,

StyleContext.SmallAttributeSet

```java
public interface
AttributeSet
```

A collection of unique attributes. This is a read-only,
immutable interface. An attribute is basically a key and
a value assigned to the key. The collection may represent
something like a style run, a logical style, etc. These
are generally used to describe features that will contribute
to some graphical representation such as a font. The
set of possible keys is unbounded and can be anything.
Typically View implementations will respond to attribute
definitions and render something to represent the attributes.

Attributes can potentially resolve in a hierarchy. If a
key doesn't resolve locally, and a resolving parent
exists, the key will be resolved through the parent.

**See Also:** MutableAttributeSet

public interface

AttributeSet

A collection of unique attributes. This is a read-only,
immutable interface. An attribute is basically a key and
a value assigned to the key. The collection may represent
something like a style run, a logical style, etc. These
are generally used to describe features that will contribute
to some graphical representation such as a font. The
set of possible keys is unbounded and can be anything.
Typically View implementations will respond to attribute
definitions and render something to represent the attributes.

Attributes can potentially resolve in a hierarchy. If a
key doesn't resolve locally, and a resolving parent
exists, the key will be resolved through the parent.

Attributes can potentially resolve in a hierarchy. If a
key doesn't resolve locally, and a resolving parent
exists, the key will be resolved through the parent.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

AttributeSet.CharacterAttribute

This interface is the type signature that is expected
to be present on any attribute key that contributes to
character level presentation.

static interface

AttributeSet.ColorAttribute

This interface is the type signature that is expected
to be present on any attribute key that contributes to
presentation of color.

static interface

AttributeSet.FontAttribute

This interface is the type signature that is expected
to be present on any attribute key that contributes to
the determination of what font to use to render some
text.

static interface

AttributeSet.ParagraphAttribute

This interface is the type signature that is expected
to be present on any attribute key that contributes to
the paragraph level presentation.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Object

NameAttribute

Attribute name used to name the collection of
attributes.

static

Object

ResolveAttribute

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

containsAttribute

​(

Object

name,

Object

value)

Returns

true

if this set defines an attribute with the same
name and an equal value.

boolean

containsAttributes

​(

AttributeSet

attributes)

Returns

true

if this set defines all the attributes from the
given set with equal values.

AttributeSet

copyAttributes

()

Returns an attribute set that is guaranteed not
to change over time.

Object

getAttribute

​(

Object

key)

Fetches the value of the given attribute.

int

getAttributeCount

()

Returns the number of attributes that are defined locally in this set.

Enumeration

<?>

getAttributeNames

()

Returns an enumeration over the names of the attributes that are
defined locally in the set.

AttributeSet

getResolveParent

()

Gets the resolving parent.

boolean

isDefined

​(

Object

attrName)

Checks whether the named attribute has a value specified in
the set without resolving through another attribute
set.

boolean

isEqual

​(

AttributeSet

attr)

Determines if the two attribute sets are equivalent.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

AttributeSet.CharacterAttribute

This interface is the type signature that is expected
to be present on any attribute key that contributes to
character level presentation.

static interface

AttributeSet.ColorAttribute

This interface is the type signature that is expected
to be present on any attribute key that contributes to
presentation of color.

static interface

AttributeSet.FontAttribute

This interface is the type signature that is expected
to be present on any attribute key that contributes to
the determination of what font to use to render some
text.

static interface

AttributeSet.ParagraphAttribute

This interface is the type signature that is expected
to be present on any attribute key that contributes to
the paragraph level presentation.

---

#### Nested Class Summary

This interface is the type signature that is expected
to be present on any attribute key that contributes to
character level presentation.

This interface is the type signature that is expected
to be present on any attribute key that contributes to
presentation of color.

This interface is the type signature that is expected
to be present on any attribute key that contributes to
the determination of what font to use to render some
text.

This interface is the type signature that is expected
to be present on any attribute key that contributes to
the paragraph level presentation.

Field Summary

Fields

Modifier and Type

Field

Description

static

Object

NameAttribute

Attribute name used to name the collection of
attributes.

static

Object

ResolveAttribute

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

---

#### Field Summary

Attribute name used to name the collection of
attributes.

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

containsAttribute

​(

Object

name,

Object

value)

Returns

true

if this set defines an attribute with the same
name and an equal value.

boolean

containsAttributes

​(

AttributeSet

attributes)

Returns

true

if this set defines all the attributes from the
given set with equal values.

AttributeSet

copyAttributes

()

Returns an attribute set that is guaranteed not
to change over time.

Object

getAttribute

​(

Object

key)

Fetches the value of the given attribute.

int

getAttributeCount

()

Returns the number of attributes that are defined locally in this set.

Enumeration

<?>

getAttributeNames

()

Returns an enumeration over the names of the attributes that are
defined locally in the set.

AttributeSet

getResolveParent

()

Gets the resolving parent.

boolean

isDefined

​(

Object

attrName)

Checks whether the named attribute has a value specified in
the set without resolving through another attribute
set.

boolean

isEqual

​(

AttributeSet

attr)

Determines if the two attribute sets are equivalent.

---

#### Method Summary

Returns

true

if this set defines an attribute with the same
name and an equal value.

Returns

true

if this set defines all the attributes from the
given set with equal values.

Returns an attribute set that is guaranteed not
to change over time.

Fetches the value of the given attribute.

Returns the number of attributes that are defined locally in this set.

Returns an enumeration over the names of the attributes that are
defined locally in the set.

Gets the resolving parent.

Checks whether the named attribute has a value specified in
the set without resolving through another attribute
set.

Determines if the two attribute sets are equivalent.

============ FIELD DETAIL ===========

- Field Detail

- NameAttribute

```java
static final
Object
NameAttribute
```

Attribute name used to name the collection of
attributes.

- ResolveAttribute

```java
static final
Object
ResolveAttribute
```

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

============ METHOD DETAIL ==========

- Method Detail

- getAttributeCount

```java
int getAttributeCount()
```

Returns the number of attributes that are defined locally in this set.
Attributes that are defined in the parent set are not included.

**Returns:** the number of attributes >= 0

- isDefined

```java
boolean isDefined​(
Object
attrName)
```

Checks whether the named attribute has a value specified in
the set without resolving through another attribute
set.

**Parameters:** attrName

- the attribute name
**Returns:** true if the attribute has a value specified

- isEqual

```java
boolean isEqual​(
AttributeSet
attr)
```

Determines if the two attribute sets are equivalent.

**Parameters:** attr

- an attribute set
**Returns:** true if the sets are equivalent

- copyAttributes

```java
AttributeSet
copyAttributes()
```

Returns an attribute set that is guaranteed not
to change over time.

**Returns:** a copy of the attribute set

- getAttribute

```java
Object
getAttribute​(
Object
key)
```

Fetches the value of the given attribute. If the value is not found
locally, the search is continued upward through the resolving
parent (if one exists) until the value is either
found or there are no more parents. If the value is not found,
null is returned.

**Parameters:** key

- the non-null key of the attribute binding
**Returns:** the value of the attribute, or

null

if not found

- getAttributeNames

```java
Enumeration
<?> getAttributeNames()
```

Returns an enumeration over the names of the attributes that are
defined locally in the set. Names of attributes defined in the
resolving parent, if any, are not included. The values of the

Enumeration

may be anything and are not constrained to
a particular

Object

type.

This method never returns

null

. For a set with no attributes, it
returns an empty

Enumeration

.

**Returns:** the names

- containsAttribute

```java
boolean containsAttribute​(
Object
name,

Object
value)
```

Returns

true

if this set defines an attribute with the same
name and an equal value. If such an attribute is not found locally,
it is searched through in the resolving parent hierarchy.

**Parameters:** name

- the non-null attribute name
**Parameters:** value

- the value
**Returns:** true

if the set defines the attribute with an
equal value, either locally or through its resolving parent
**Throws:** NullPointerException

- if either

name

or

value

is

null

- containsAttributes

```java
boolean containsAttributes​(
AttributeSet
attributes)
```

Returns

true

if this set defines all the attributes from the
given set with equal values. If an attribute is not found locally,
it is searched through in the resolving parent hierarchy.

**Parameters:** attributes

- the set of attributes to check against
**Returns:** true

if this set defines all the attributes with equal
values, either locally or through its resolving parent
**Throws:** NullPointerException

- if

attributes

is

null

- getResolveParent

```java
AttributeSet
getResolveParent()
```

Gets the resolving parent.

**Returns:** the parent

Field Detail

- NameAttribute

```java
static final
Object
NameAttribute
```

Attribute name used to name the collection of
attributes.

- ResolveAttribute

```java
static final
Object
ResolveAttribute
```

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

---

#### Field Detail

NameAttribute

```java
static final
Object
NameAttribute
```

Attribute name used to name the collection of
attributes.

---

#### NameAttribute

static final

Object

NameAttribute

Attribute name used to name the collection of
attributes.

ResolveAttribute

```java
static final
Object
ResolveAttribute
```

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

---

#### ResolveAttribute

static final

Object

ResolveAttribute

Attribute name used to identify the resolving parent
set of attributes, if one is defined.

Method Detail

- getAttributeCount

```java
int getAttributeCount()
```

Returns the number of attributes that are defined locally in this set.
Attributes that are defined in the parent set are not included.

**Returns:** the number of attributes >= 0

- isDefined

```java
boolean isDefined​(
Object
attrName)
```

Checks whether the named attribute has a value specified in
the set without resolving through another attribute
set.

**Parameters:** attrName

- the attribute name
**Returns:** true if the attribute has a value specified

- isEqual

```java
boolean isEqual​(
AttributeSet
attr)
```

Determines if the two attribute sets are equivalent.

**Parameters:** attr

- an attribute set
**Returns:** true if the sets are equivalent

- copyAttributes

```java
AttributeSet
copyAttributes()
```

Returns an attribute set that is guaranteed not
to change over time.

**Returns:** a copy of the attribute set

- getAttribute

```java
Object
getAttribute​(
Object
key)
```

Fetches the value of the given attribute. If the value is not found
locally, the search is continued upward through the resolving
parent (if one exists) until the value is either
found or there are no more parents. If the value is not found,
null is returned.

**Parameters:** key

- the non-null key of the attribute binding
**Returns:** the value of the attribute, or

null

if not found

- getAttributeNames

```java
Enumeration
<?> getAttributeNames()
```

Returns an enumeration over the names of the attributes that are
defined locally in the set. Names of attributes defined in the
resolving parent, if any, are not included. The values of the

Enumeration

may be anything and are not constrained to
a particular

Object

type.

This method never returns

null

. For a set with no attributes, it
returns an empty

Enumeration

.

**Returns:** the names

- containsAttribute

```java
boolean containsAttribute​(
Object
name,

Object
value)
```

Returns

true

if this set defines an attribute with the same
name and an equal value. If such an attribute is not found locally,
it is searched through in the resolving parent hierarchy.

**Parameters:** name

- the non-null attribute name
**Parameters:** value

- the value
**Returns:** true

if the set defines the attribute with an
equal value, either locally or through its resolving parent
**Throws:** NullPointerException

- if either

name

or

value

is

null

- containsAttributes

```java
boolean containsAttributes​(
AttributeSet
attributes)
```

Returns

true

if this set defines all the attributes from the
given set with equal values. If an attribute is not found locally,
it is searched through in the resolving parent hierarchy.

**Parameters:** attributes

- the set of attributes to check against
**Returns:** true

if this set defines all the attributes with equal
values, either locally or through its resolving parent
**Throws:** NullPointerException

- if

attributes

is

null

- getResolveParent

```java
AttributeSet
getResolveParent()
```

Gets the resolving parent.

**Returns:** the parent

---

#### Method Detail

getAttributeCount

```java
int getAttributeCount()
```

Returns the number of attributes that are defined locally in this set.
Attributes that are defined in the parent set are not included.

**Returns:** the number of attributes >= 0

---

#### getAttributeCount

int getAttributeCount()

Returns the number of attributes that are defined locally in this set.
Attributes that are defined in the parent set are not included.

isDefined

```java
boolean isDefined​(
Object
attrName)
```

Checks whether the named attribute has a value specified in
the set without resolving through another attribute
set.

**Parameters:** attrName

- the attribute name
**Returns:** true if the attribute has a value specified

---

#### isDefined

boolean isDefined​(

Object

attrName)

Checks whether the named attribute has a value specified in
the set without resolving through another attribute
set.

isEqual

```java
boolean isEqual​(
AttributeSet
attr)
```

Determines if the two attribute sets are equivalent.

**Parameters:** attr

- an attribute set
**Returns:** true if the sets are equivalent

---

#### isEqual

boolean isEqual​(

AttributeSet

attr)

Determines if the two attribute sets are equivalent.

copyAttributes

```java
AttributeSet
copyAttributes()
```

Returns an attribute set that is guaranteed not
to change over time.

**Returns:** a copy of the attribute set

---

#### copyAttributes

AttributeSet

copyAttributes()

Returns an attribute set that is guaranteed not
to change over time.

getAttribute

```java
Object
getAttribute​(
Object
key)
```

Fetches the value of the given attribute. If the value is not found
locally, the search is continued upward through the resolving
parent (if one exists) until the value is either
found or there are no more parents. If the value is not found,
null is returned.

**Parameters:** key

- the non-null key of the attribute binding
**Returns:** the value of the attribute, or

null

if not found

---

#### getAttribute

Object

getAttribute​(

Object

key)

Fetches the value of the given attribute. If the value is not found
locally, the search is continued upward through the resolving
parent (if one exists) until the value is either
found or there are no more parents. If the value is not found,
null is returned.

getAttributeNames

```java
Enumeration
<?> getAttributeNames()
```

Returns an enumeration over the names of the attributes that are
defined locally in the set. Names of attributes defined in the
resolving parent, if any, are not included. The values of the

Enumeration

may be anything and are not constrained to
a particular

Object

type.

This method never returns

null

. For a set with no attributes, it
returns an empty

Enumeration

.

**Returns:** the names

---

#### getAttributeNames

Enumeration

<?> getAttributeNames()

Returns an enumeration over the names of the attributes that are
defined locally in the set. Names of attributes defined in the
resolving parent, if any, are not included. The values of the

Enumeration

may be anything and are not constrained to
a particular

Object

type.

This method never returns

null

. For a set with no attributes, it
returns an empty

Enumeration

.

This method never returns

null

. For a set with no attributes, it
returns an empty

Enumeration

.

containsAttribute

```java
boolean containsAttribute​(
Object
name,

Object
value)
```

Returns

true

if this set defines an attribute with the same
name and an equal value. If such an attribute is not found locally,
it is searched through in the resolving parent hierarchy.

**Parameters:** name

- the non-null attribute name
**Parameters:** value

- the value
**Returns:** true

if the set defines the attribute with an
equal value, either locally or through its resolving parent
**Throws:** NullPointerException

- if either

name

or

value

is

null

---

#### containsAttribute

boolean containsAttribute​(

Object

name,

Object

value)

Returns

true

if this set defines an attribute with the same
name and an equal value. If such an attribute is not found locally,
it is searched through in the resolving parent hierarchy.

containsAttributes

```java
boolean containsAttributes​(
AttributeSet
attributes)
```

Returns

true

if this set defines all the attributes from the
given set with equal values. If an attribute is not found locally,
it is searched through in the resolving parent hierarchy.

**Parameters:** attributes

- the set of attributes to check against
**Returns:** true

if this set defines all the attributes with equal
values, either locally or through its resolving parent
**Throws:** NullPointerException

- if

attributes

is

null

---

#### containsAttributes

boolean containsAttributes​(

AttributeSet

attributes)

Returns

true

if this set defines all the attributes from the
given set with equal values. If an attribute is not found locally,
it is searched through in the resolving parent hierarchy.

getResolveParent

```java
AttributeSet
getResolveParent()
```

Gets the resolving parent.

**Returns:** the parent

---

#### getResolveParent

AttributeSet

getResolveParent()

Gets the resolving parent.

---

