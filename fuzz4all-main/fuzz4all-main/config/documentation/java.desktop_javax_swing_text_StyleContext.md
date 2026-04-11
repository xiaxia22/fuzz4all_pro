# Class StyleContext

**Source:** `java.desktop\javax\swing\text\StyleContext.html`

### Class Description

```java
public class
StyleContext

extends
Object

implements
Serializable
,
AbstractDocument.AttributeContext
```

A pool of styles and their associated resources. This class determines
the lifetime of a group of resources by being a container that holds
caches for various resources such as font and color that get reused
by the various style definitions. This can be shared by multiple
documents if desired to maximize the sharing of related resources.

This class also provides efficient support for small sets of attributes
and compresses them by sharing across uses and taking advantage of
their immutable nature. Since many styles are replicated, the potential
for sharing is significant, and copies can be extremely cheap.
Larger sets reduce the possibility of sharing, and therefore revert
automatically to a less space-efficient implementation.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

,

AbstractDocument.AttributeContext

---

### Field Details

#### public static final
String
DEFAULT_STYLE

The name given to the default logical style attached
to paragraphs.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public StyleContext()

Creates a new StyleContext object.

---

### Method Details

#### public static final
StyleContext
getDefaultStyleContext()

Returns default AttributeContext shared by all documents that
don't bother to define/supply their own context.

**Returns:**
- the context

---

#### public
Style
addStyle​(
String
nm,

Style
parent)

Adds a new style into the style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

**Parameters:**
- nm

- the name of the style (must be unique within the
collection of named styles in the document). The name may
be null if the style is unnamed, but the caller is responsible
for managing the reference returned as an unnamed style can't
be fetched by name. An unnamed style may be useful for things
like character attribute overrides such as found in a style
run.
- parent

- the parent style. This may be null if unspecified
attributes need not be resolved in some other style.

**Returns:**
- the created style

---

#### public void removeStyle​(
String
nm)

Removes a named style previously added to the document.

**Parameters:**
- nm

- the name of the style to remove

---

#### public
Style
getStyle​(
String
nm)

Fetches a named style previously added to the document

**Parameters:**
- nm

- the name of the style

**Returns:**
- the style

---

#### public
Enumeration
<?> getStyleNames()

Fetches the names of the styles defined.

**Returns:**
- the list of names as an enumeration

---

#### public void addChangeListener​(
ChangeListener
l)

Adds a listener to track when styles are added
or removed.

**Parameters:**
- l

- the change listener

---

#### public void removeChangeListener​(
ChangeListener
l)

Removes a listener that was tracking styles being
added or removed.

**Parameters:**
- l

- the change listener

---

#### public
ChangeListener
[] getChangeListeners()

Returns an array of all the

ChangeListener

s added
to this StyleContext with addChangeListener().

**Returns:**
- all of the

ChangeListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### public
Font
getFont​(
AttributeSet
attr)

Gets the font from an attribute set. This is
implemented to try and fetch a cached font
for the given AttributeSet, and if that fails
the font features are resolved and the
font is fetched from the low-level font cache.

**Parameters:**
- attr

- the attribute set

**Returns:**
- the font

---

#### public
Color
getForeground​(
AttributeSet
attr)

Takes a set of attributes and turn it into a foreground color
specification. This might be used to specify things
like brighter, more hue, etc. By default it simply returns
the value specified by the StyleConstants.Foreground attribute.

**Parameters:**
- attr

- the set of attributes

**Returns:**
- the color

---

#### public
Color
getBackground​(
AttributeSet
attr)

Takes a set of attributes and turn it into a background color
specification. This might be used to specify things
like brighter, more hue, etc. By default it simply returns
the value specified by the StyleConstants.Background attribute.

**Parameters:**
- attr

- the set of attributes

**Returns:**
- the color

---

#### public
Font
getFont​(
String
family,
int style,
int size)

Gets a new font. This returns a Font from a cache
if a cached font exists. If not, a Font is added to
the cache. This is basically a low-level cache for
1.1 font features.

**Parameters:**
- family

- the font family (such as "Monospaced")
- style

- the style of the font (such as Font.PLAIN)
- size

- the point size >= 1

**Returns:**
- the new font

---

#### public
FontMetrics
getFontMetrics​(
Font
f)

Returns font metrics for a font.

**Parameters:**
- f

- the font

**Returns:**
- the metrics

---

#### public
AttributeSet
addAttribute​(
AttributeSet
old,

Object
name,

Object
value)

Adds an attribute to the given set, and returns
the new representative set.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- addAttribute

in interface

AbstractDocument.AttributeContext

**Parameters:**
- old

- the old attribute set
- name

- the non-null attribute name
- value

- the attribute value

**Returns:**
- the updated attribute set

**See Also:**
- MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

---

#### public
AttributeSet
addAttributes​(
AttributeSet
old,

AttributeSet
attr)

Adds a set of attributes to the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- addAttributes

in interface

AbstractDocument.AttributeContext

**Parameters:**
- old

- the old attribute set
- attr

- the attributes to add

**Returns:**
- the updated attribute set

**See Also:**
- MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

---

#### public
AttributeSet
removeAttribute​(
AttributeSet
old,

Object
name)

Removes an attribute from the set.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- removeAttribute

in interface

AbstractDocument.AttributeContext

**Parameters:**
- old

- the old set of attributes
- name

- the non-null attribute name

**Returns:**
- the updated attribute set

**See Also:**
- MutableAttributeSet.removeAttribute(java.lang.Object)

---

#### public
AttributeSet
removeAttributes​(
AttributeSet
old,

Enumeration
<?> names)

Removes a set of attributes for the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- removeAttributes

in interface

AbstractDocument.AttributeContext

**Parameters:**
- old

- the old attribute set
- names

- the attribute names

**Returns:**
- the updated attribute set

**See Also:**
- MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

---

#### public
AttributeSet
removeAttributes​(
AttributeSet
old,

AttributeSet
attrs)

Removes a set of attributes for the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- removeAttributes

in interface

AbstractDocument.AttributeContext

**Parameters:**
- old

- the old attribute set
- attrs

- the attributes

**Returns:**
- the updated attribute set

**See Also:**
- MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

---

#### public
AttributeSet
getEmptySet()

Fetches an empty AttributeSet.

**Specified by:**
- getEmptySet

in interface

AbstractDocument.AttributeContext

**Returns:**
- the set

---

#### public void reclaim​(
AttributeSet
a)

Returns a set no longer needed by the MutableAttributeSet implementation.
This is useful for operation under 1.1 where there are no weak
references. This would typically be called by the finalize method
of the MutableAttributeSet implementation.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:**
- reclaim

in interface

AbstractDocument.AttributeContext

**Parameters:**
- a

- the set to reclaim

---

#### protected int getCompressionThreshold()

Returns the maximum number of key/value pairs to try and
compress into unique/immutable sets. Any sets above this
limit will use hashtables and be a MutableAttributeSet.

**Returns:**
- the threshold

---

#### protected
StyleContext.SmallAttributeSet
createSmallAttributeSet​(
AttributeSet
a)

Create a compact set of attributes that might be shared.
This is a hook for subclasses that want to alter the
behavior of SmallAttributeSet. This can be reimplemented
to return an AttributeSet that provides some sort of
attribute conversion.

**Parameters:**
- a

- The set of attributes to be represented in the
the compact form.

**Returns:**
- a compact set of attributes that might be shared

---

#### protected
MutableAttributeSet
createLargeAttributeSet​(
AttributeSet
a)

Create a large set of attributes that should trade off
space for time. This set will not be shared. This is
a hook for subclasses that want to alter the behavior
of the larger attribute storage format (which is
SimpleAttributeSet by default). This can be reimplemented
to return a MutableAttributeSet that provides some sort of
attribute conversion.

**Parameters:**
- a

- The set of attributes to be represented in the
the larger form.

**Returns:**
- a large set of attributes that should trade off
space for time

---

#### public
String
toString()

Converts a StyleContext to a String.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string

---

#### public void writeAttributes​(
ObjectOutputStream
out,

AttributeSet
a)
throws
IOException

Context-specific handling of writing out attributes

**Parameters:**
- out

- the output stream
- a

- the attribute set

**Throws:**
- IOException

- on any I/O error

---

#### public void readAttributes​(
ObjectInputStream
in,

MutableAttributeSet
a)
throws
ClassNotFoundException
,

IOException

Context-specific handling of reading in attributes

**Parameters:**
- in

- the object stream to read the attribute data from.
- a

- the attribute set to place the attribute
definitions in.

**Throws:**
- ClassNotFoundException

- passed upward if encountered
when reading the object stream.
- IOException

- passed upward if encountered when
reading the object stream.

---

#### public static void writeAttributeSet​(
ObjectOutputStream
out,

AttributeSet
a)
throws
IOException

Writes a set of attributes to the given object stream
for the purpose of serialization. This will take
special care to deal with static attribute keys that
have been registered wit the

registerStaticAttributeKey

method.
Any attribute key not registered as a static key
will be serialized directly. All values are expected
to be serializable.

**Parameters:**
- out

- the output stream
- a

- the attribute set

**Throws:**
- IOException

- on any I/O error

---

#### public static void readAttributeSet​(
ObjectInputStream
in,

MutableAttributeSet
a)
throws
ClassNotFoundException
,

IOException

Reads a set of attributes from the given object input
stream that have been previously written out with

writeAttributeSet

. This will try to restore
keys that were static objects to the static objects in
the current virtual machine considering only those keys
that have been registered with the

registerStaticAttributeKey

method.
The attributes retrieved from the stream will be placed
into the given mutable set.

**Parameters:**
- in

- the object stream to read the attribute data from.
- a

- the attribute set to place the attribute
definitions in.

**Throws:**
- ClassNotFoundException

- passed upward if encountered
when reading the object stream.
- IOException

- passed upward if encountered when
reading the object stream.

---

#### public static void registerStaticAttributeKey​(
Object
key)

Registers an object as a static object that is being
used as a key in attribute sets. This allows the key
to be treated specially for serialization.

For operation under a 1.1 virtual machine, this
uses the value returned by

toString

concatenated to the classname. The value returned
by toString should not have the class reference
in it (ie it should be reimplemented from the
definition in Object) in order to be the same when
recomputed later.

**Parameters:**
- key

- the non-null object key

---

#### public static
Object
getStaticAttribute​(
Object
key)

Returns the object previously registered with

registerStaticAttributeKey

.

**Parameters:**
- key

- the object key

**Returns:**
- Returns the object previously registered with

registerStaticAttributeKey

---

#### public static
Object
getStaticAttributeKey​(
Object
key)

Returns the String that

key

will be registered with.

**Parameters:**
- key

- the object key

**Returns:**
- the String that

key

will be registered with

**See Also:**
- getStaticAttribute(java.lang.Object)

,

registerStaticAttributeKey(java.lang.Object)

---

### Additional Sections

#### Class StyleContext

java.lang.Object

- javax.swing.text.StyleContext

javax.swing.text.StyleContext

**All Implemented Interfaces:** Serializable

,

AbstractDocument.AttributeContext

**Direct Known Subclasses:** StyleSheet

```java
public class
StyleContext

extends
Object

implements
Serializable
,
AbstractDocument.AttributeContext
```

A pool of styles and their associated resources. This class determines
the lifetime of a group of resources by being a container that holds
caches for various resources such as font and color that get reused
by the various style definitions. This can be shared by multiple
documents if desired to maximize the sharing of related resources.

This class also provides efficient support for small sets of attributes
and compresses them by sharing across uses and taking advantage of
their immutable nature. Since many styles are replicated, the potential
for sharing is significant, and copies can be extremely cheap.
Larger sets reduce the possibility of sharing, and therefore revert
automatically to a less space-efficient implementation.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** Serialized Form

public class

StyleContext

extends

Object

implements

Serializable

,

AbstractDocument.AttributeContext

A pool of styles and their associated resources. This class determines
the lifetime of a group of resources by being a container that holds
caches for various resources such as font and color that get reused
by the various style definitions. This can be shared by multiple
documents if desired to maximize the sharing of related resources.

This class also provides efficient support for small sets of attributes
and compresses them by sharing across uses and taking advantage of
their immutable nature. Since many styles are replicated, the potential
for sharing is significant, and copies can be extremely cheap.
Larger sets reduce the possibility of sharing, and therefore revert
automatically to a less space-efficient implementation.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

This class also provides efficient support for small sets of attributes
and compresses them by sharing across uses and taking advantage of
their immutable nature. Since many styles are replicated, the potential
for sharing is significant, and copies can be extremely cheap.
Larger sets reduce the possibility of sharing, and therefore revert
automatically to a less space-efficient implementation.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

StyleContext.NamedStyle

A collection of attributes, typically used to represent
character and paragraph styles.

class

StyleContext.SmallAttributeSet

This class holds a small number of attributes in an array.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

DEFAULT_STYLE

The name given to the default logical style attached
to paragraphs.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StyleContext

()

Creates a new StyleContext object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AttributeSet

addAttribute

​(

AttributeSet

old,

Object

name,

Object

value)

Adds an attribute to the given set, and returns
the new representative set.

AttributeSet

addAttributes

​(

AttributeSet

old,

AttributeSet

attr)

Adds a set of attributes to the element.

void

addChangeListener

​(

ChangeListener

l)

Adds a listener to track when styles are added
or removed.

Style

addStyle

​(

String

nm,

Style

parent)

Adds a new style into the style hierarchy.

protected

MutableAttributeSet

createLargeAttributeSet

​(

AttributeSet

a)

Create a large set of attributes that should trade off
space for time.

protected

StyleContext.SmallAttributeSet

createSmallAttributeSet

​(

AttributeSet

a)

Create a compact set of attributes that might be shared.

Color

getBackground

​(

AttributeSet

attr)

Takes a set of attributes and turn it into a background color
specification.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this StyleContext with addChangeListener().

protected int

getCompressionThreshold

()

Returns the maximum number of key/value pairs to try and
compress into unique/immutable sets.

static

StyleContext

getDefaultStyleContext

()

Returns default AttributeContext shared by all documents that
don't bother to define/supply their own context.

AttributeSet

getEmptySet

()

Fetches an empty AttributeSet.

Font

getFont

​(

String

family,
int style,
int size)

Gets a new font.

Font

getFont

​(

AttributeSet

attr)

Gets the font from an attribute set.

FontMetrics

getFontMetrics

​(

Font

f)

Returns font metrics for a font.

Color

getForeground

​(

AttributeSet

attr)

Takes a set of attributes and turn it into a foreground color
specification.

static

Object

getStaticAttribute

​(

Object

key)

Returns the object previously registered with

registerStaticAttributeKey

.

static

Object

getStaticAttributeKey

​(

Object

key)

Returns the String that

key

will be registered with.

Style

getStyle

​(

String

nm)

Fetches a named style previously added to the document

Enumeration

<?>

getStyleNames

()

Fetches the names of the styles defined.

void

readAttributes

​(

ObjectInputStream

in,

MutableAttributeSet

a)

Context-specific handling of reading in attributes

static void

readAttributeSet

​(

ObjectInputStream

in,

MutableAttributeSet

a)

Reads a set of attributes from the given object input
stream that have been previously written out with

writeAttributeSet

.

void

reclaim

​(

AttributeSet

a)

Returns a set no longer needed by the MutableAttributeSet implementation.

static void

registerStaticAttributeKey

​(

Object

key)

Registers an object as a static object that is being
used as a key in attribute sets.

AttributeSet

removeAttribute

​(

AttributeSet

old,

Object

name)

Removes an attribute from the set.

AttributeSet

removeAttributes

​(

AttributeSet

old,

Enumeration

<?> names)

Removes a set of attributes for the element.

AttributeSet

removeAttributes

​(

AttributeSet

old,

AttributeSet

attrs)

Removes a set of attributes for the element.

void

removeChangeListener

​(

ChangeListener

l)

Removes a listener that was tracking styles being
added or removed.

void

removeStyle

​(

String

nm)

Removes a named style previously added to the document.

String

toString

()

Converts a StyleContext to a String.

void

writeAttributes

​(

ObjectOutputStream

out,

AttributeSet

a)

Context-specific handling of writing out attributes

static void

writeAttributeSet

​(

ObjectOutputStream

out,

AttributeSet

a)

Writes a set of attributes to the given object stream
for the purpose of serialization.

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

class

StyleContext.NamedStyle

A collection of attributes, typically used to represent
character and paragraph styles.

class

StyleContext.SmallAttributeSet

This class holds a small number of attributes in an array.

---

#### Nested Class Summary

A collection of attributes, typically used to represent
character and paragraph styles.

This class holds a small number of attributes in an array.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

DEFAULT_STYLE

The name given to the default logical style attached
to paragraphs.

---

#### Field Summary

The name given to the default logical style attached
to paragraphs.

Constructor Summary

Constructors

Constructor

Description

StyleContext

()

Creates a new StyleContext object.

---

#### Constructor Summary

Creates a new StyleContext object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AttributeSet

addAttribute

​(

AttributeSet

old,

Object

name,

Object

value)

Adds an attribute to the given set, and returns
the new representative set.

AttributeSet

addAttributes

​(

AttributeSet

old,

AttributeSet

attr)

Adds a set of attributes to the element.

void

addChangeListener

​(

ChangeListener

l)

Adds a listener to track when styles are added
or removed.

Style

addStyle

​(

String

nm,

Style

parent)

Adds a new style into the style hierarchy.

protected

MutableAttributeSet

createLargeAttributeSet

​(

AttributeSet

a)

Create a large set of attributes that should trade off
space for time.

protected

StyleContext.SmallAttributeSet

createSmallAttributeSet

​(

AttributeSet

a)

Create a compact set of attributes that might be shared.

Color

getBackground

​(

AttributeSet

attr)

Takes a set of attributes and turn it into a background color
specification.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this StyleContext with addChangeListener().

protected int

getCompressionThreshold

()

Returns the maximum number of key/value pairs to try and
compress into unique/immutable sets.

static

StyleContext

getDefaultStyleContext

()

Returns default AttributeContext shared by all documents that
don't bother to define/supply their own context.

AttributeSet

getEmptySet

()

Fetches an empty AttributeSet.

Font

getFont

​(

String

family,
int style,
int size)

Gets a new font.

Font

getFont

​(

AttributeSet

attr)

Gets the font from an attribute set.

FontMetrics

getFontMetrics

​(

Font

f)

Returns font metrics for a font.

Color

getForeground

​(

AttributeSet

attr)

Takes a set of attributes and turn it into a foreground color
specification.

static

Object

getStaticAttribute

​(

Object

key)

Returns the object previously registered with

registerStaticAttributeKey

.

static

Object

getStaticAttributeKey

​(

Object

key)

Returns the String that

key

will be registered with.

Style

getStyle

​(

String

nm)

Fetches a named style previously added to the document

Enumeration

<?>

getStyleNames

()

Fetches the names of the styles defined.

void

readAttributes

​(

ObjectInputStream

in,

MutableAttributeSet

a)

Context-specific handling of reading in attributes

static void

readAttributeSet

​(

ObjectInputStream

in,

MutableAttributeSet

a)

Reads a set of attributes from the given object input
stream that have been previously written out with

writeAttributeSet

.

void

reclaim

​(

AttributeSet

a)

Returns a set no longer needed by the MutableAttributeSet implementation.

static void

registerStaticAttributeKey

​(

Object

key)

Registers an object as a static object that is being
used as a key in attribute sets.

AttributeSet

removeAttribute

​(

AttributeSet

old,

Object

name)

Removes an attribute from the set.

AttributeSet

removeAttributes

​(

AttributeSet

old,

Enumeration

<?> names)

Removes a set of attributes for the element.

AttributeSet

removeAttributes

​(

AttributeSet

old,

AttributeSet

attrs)

Removes a set of attributes for the element.

void

removeChangeListener

​(

ChangeListener

l)

Removes a listener that was tracking styles being
added or removed.

void

removeStyle

​(

String

nm)

Removes a named style previously added to the document.

String

toString

()

Converts a StyleContext to a String.

void

writeAttributes

​(

ObjectOutputStream

out,

AttributeSet

a)

Context-specific handling of writing out attributes

static void

writeAttributeSet

​(

ObjectOutputStream

out,

AttributeSet

a)

Writes a set of attributes to the given object stream
for the purpose of serialization.

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

wait

,

wait

,

wait

---

#### Method Summary

Adds an attribute to the given set, and returns
the new representative set.

Adds a set of attributes to the element.

Adds a listener to track when styles are added
or removed.

Adds a new style into the style hierarchy.

Create a large set of attributes that should trade off
space for time.

Create a compact set of attributes that might be shared.

Takes a set of attributes and turn it into a background color
specification.

Returns an array of all the

ChangeListener

s added
to this StyleContext with addChangeListener().

Returns the maximum number of key/value pairs to try and
compress into unique/immutable sets.

Returns default AttributeContext shared by all documents that
don't bother to define/supply their own context.

Fetches an empty AttributeSet.

Gets a new font.

Gets the font from an attribute set.

Returns font metrics for a font.

Takes a set of attributes and turn it into a foreground color
specification.

Returns the object previously registered with

registerStaticAttributeKey

.

Returns the String that

key

will be registered with.

Fetches a named style previously added to the document

Fetches the names of the styles defined.

Context-specific handling of reading in attributes

Reads a set of attributes from the given object input
stream that have been previously written out with

writeAttributeSet

.

Returns a set no longer needed by the MutableAttributeSet implementation.

Registers an object as a static object that is being
used as a key in attribute sets.

Removes an attribute from the set.

Removes a set of attributes for the element.

Removes a listener that was tracking styles being
added or removed.

Removes a named style previously added to the document.

Converts a StyleContext to a String.

Context-specific handling of writing out attributes

Writes a set of attributes to the given object stream
for the purpose of serialization.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- DEFAULT_STYLE

```java
public static final
String
DEFAULT_STYLE
```

The name given to the default logical style attached
to paragraphs.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StyleContext

```java
public StyleContext()
```

Creates a new StyleContext object.

============ METHOD DETAIL ==========

- Method Detail

- getDefaultStyleContext

```java
public static final
StyleContext
getDefaultStyleContext()
```

Returns default AttributeContext shared by all documents that
don't bother to define/supply their own context.

**Returns:** the context

- addStyle

```java
public
Style
addStyle​(
String
nm,

Style
parent)
```

Adds a new style into the style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

**Parameters:** nm

- the name of the style (must be unique within the
collection of named styles in the document). The name may
be null if the style is unnamed, but the caller is responsible
for managing the reference returned as an unnamed style can't
be fetched by name. An unnamed style may be useful for things
like character attribute overrides such as found in a style
run.
**Parameters:** parent

- the parent style. This may be null if unspecified
attributes need not be resolved in some other style.
**Returns:** the created style

- removeStyle

```java
public void removeStyle​(
String
nm)
```

Removes a named style previously added to the document.

**Parameters:** nm

- the name of the style to remove

- getStyle

```java
public
Style
getStyle​(
String
nm)
```

Fetches a named style previously added to the document

**Parameters:** nm

- the name of the style
**Returns:** the style

- getStyleNames

```java
public
Enumeration
<?> getStyleNames()
```

Fetches the names of the styles defined.

**Returns:** the list of names as an enumeration

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a listener to track when styles are added
or removed.

**Parameters:** l

- the change listener

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a listener that was tracking styles being
added or removed.

**Parameters:** l

- the change listener

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this StyleContext with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- getFont

```java
public
Font
getFont​(
AttributeSet
attr)
```

Gets the font from an attribute set. This is
implemented to try and fetch a cached font
for the given AttributeSet, and if that fails
the font features are resolved and the
font is fetched from the low-level font cache.

**Parameters:** attr

- the attribute set
**Returns:** the font

- getForeground

```java
public
Color
getForeground​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a foreground color
specification. This might be used to specify things
like brighter, more hue, etc. By default it simply returns
the value specified by the StyleConstants.Foreground attribute.

**Parameters:** attr

- the set of attributes
**Returns:** the color

- getBackground

```java
public
Color
getBackground​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a background color
specification. This might be used to specify things
like brighter, more hue, etc. By default it simply returns
the value specified by the StyleConstants.Background attribute.

**Parameters:** attr

- the set of attributes
**Returns:** the color

- getFont

```java
public
Font
getFont​(
String
family,
int style,
int size)
```

Gets a new font. This returns a Font from a cache
if a cached font exists. If not, a Font is added to
the cache. This is basically a low-level cache for
1.1 font features.

**Parameters:** family

- the font family (such as "Monospaced")
**Parameters:** style

- the style of the font (such as Font.PLAIN)
**Parameters:** size

- the point size >= 1
**Returns:** the new font

- getFontMetrics

```java
public
FontMetrics
getFontMetrics​(
Font
f)
```

Returns font metrics for a font.

**Parameters:** f

- the font
**Returns:** the metrics

- addAttribute

```java
public
AttributeSet
addAttribute​(
AttributeSet
old,

Object
name,

Object
value)
```

Adds an attribute to the given set, and returns
the new representative set.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** addAttribute

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old attribute set
**Parameters:** name

- the non-null attribute name
**Parameters:** value

- the attribute value
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

- addAttributes

```java
public
AttributeSet
addAttributes​(
AttributeSet
old,

AttributeSet
attr)
```

Adds a set of attributes to the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** addAttributes

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old attribute set
**Parameters:** attr

- the attributes to add
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

- removeAttribute

```java
public
AttributeSet
removeAttribute​(
AttributeSet
old,

Object
name)
```

Removes an attribute from the set.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** removeAttribute

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old set of attributes
**Parameters:** name

- the non-null attribute name
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttribute(java.lang.Object)

- removeAttributes

```java
public
AttributeSet
removeAttributes​(
AttributeSet
old,

Enumeration
<?> names)
```

Removes a set of attributes for the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** removeAttributes

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old attribute set
**Parameters:** names

- the attribute names
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

- removeAttributes

```java
public
AttributeSet
removeAttributes​(
AttributeSet
old,

AttributeSet
attrs)
```

Removes a set of attributes for the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** removeAttributes

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old attribute set
**Parameters:** attrs

- the attributes
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

- getEmptySet

```java
public
AttributeSet
getEmptySet()
```

Fetches an empty AttributeSet.

**Specified by:** getEmptySet

in interface

AbstractDocument.AttributeContext
**Returns:** the set

- reclaim

```java
public void reclaim​(
AttributeSet
a)
```

Returns a set no longer needed by the MutableAttributeSet implementation.
This is useful for operation under 1.1 where there are no weak
references. This would typically be called by the finalize method
of the MutableAttributeSet implementation.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** reclaim

in interface

AbstractDocument.AttributeContext
**Parameters:** a

- the set to reclaim

- getCompressionThreshold

```java
protected int getCompressionThreshold()
```

Returns the maximum number of key/value pairs to try and
compress into unique/immutable sets. Any sets above this
limit will use hashtables and be a MutableAttributeSet.

**Returns:** the threshold

- createSmallAttributeSet

```java
protected
StyleContext.SmallAttributeSet
createSmallAttributeSet​(
AttributeSet
a)
```

Create a compact set of attributes that might be shared.
This is a hook for subclasses that want to alter the
behavior of SmallAttributeSet. This can be reimplemented
to return an AttributeSet that provides some sort of
attribute conversion.

**Parameters:** a

- The set of attributes to be represented in the
the compact form.
**Returns:** a compact set of attributes that might be shared

- createLargeAttributeSet

```java
protected
MutableAttributeSet
createLargeAttributeSet​(
AttributeSet
a)
```

Create a large set of attributes that should trade off
space for time. This set will not be shared. This is
a hook for subclasses that want to alter the behavior
of the larger attribute storage format (which is
SimpleAttributeSet by default). This can be reimplemented
to return a MutableAttributeSet that provides some sort of
attribute conversion.

**Parameters:** a

- The set of attributes to be represented in the
the larger form.
**Returns:** a large set of attributes that should trade off
space for time

- toString

```java
public
String
toString()
```

Converts a StyleContext to a String.

**Overrides:** toString

in class

Object
**Returns:** the string

- writeAttributes

```java
public void writeAttributes​(
ObjectOutputStream
out,

AttributeSet
a)
throws
IOException
```

Context-specific handling of writing out attributes

**Parameters:** out

- the output stream
**Parameters:** a

- the attribute set
**Throws:** IOException

- on any I/O error

- readAttributes

```java
public void readAttributes​(
ObjectInputStream
in,

MutableAttributeSet
a)
throws
ClassNotFoundException
,

IOException
```

Context-specific handling of reading in attributes

**Parameters:** in

- the object stream to read the attribute data from.
**Parameters:** a

- the attribute set to place the attribute
definitions in.
**Throws:** ClassNotFoundException

- passed upward if encountered
when reading the object stream.
**Throws:** IOException

- passed upward if encountered when
reading the object stream.

- writeAttributeSet

```java
public static void writeAttributeSet​(
ObjectOutputStream
out,

AttributeSet
a)
throws
IOException
```

Writes a set of attributes to the given object stream
for the purpose of serialization. This will take
special care to deal with static attribute keys that
have been registered wit the

registerStaticAttributeKey

method.
Any attribute key not registered as a static key
will be serialized directly. All values are expected
to be serializable.

**Parameters:** out

- the output stream
**Parameters:** a

- the attribute set
**Throws:** IOException

- on any I/O error

- readAttributeSet

```java
public static void readAttributeSet​(
ObjectInputStream
in,

MutableAttributeSet
a)
throws
ClassNotFoundException
,

IOException
```

Reads a set of attributes from the given object input
stream that have been previously written out with

writeAttributeSet

. This will try to restore
keys that were static objects to the static objects in
the current virtual machine considering only those keys
that have been registered with the

registerStaticAttributeKey

method.
The attributes retrieved from the stream will be placed
into the given mutable set.

**Parameters:** in

- the object stream to read the attribute data from.
**Parameters:** a

- the attribute set to place the attribute
definitions in.
**Throws:** ClassNotFoundException

- passed upward if encountered
when reading the object stream.
**Throws:** IOException

- passed upward if encountered when
reading the object stream.

- registerStaticAttributeKey

```java
public static void registerStaticAttributeKey​(
Object
key)
```

Registers an object as a static object that is being
used as a key in attribute sets. This allows the key
to be treated specially for serialization.

For operation under a 1.1 virtual machine, this
uses the value returned by

toString

concatenated to the classname. The value returned
by toString should not have the class reference
in it (ie it should be reimplemented from the
definition in Object) in order to be the same when
recomputed later.

**Parameters:** key

- the non-null object key

- getStaticAttribute

```java
public static
Object
getStaticAttribute​(
Object
key)
```

Returns the object previously registered with

registerStaticAttributeKey

.

**Parameters:** key

- the object key
**Returns:** Returns the object previously registered with

registerStaticAttributeKey

- getStaticAttributeKey

```java
public static
Object
getStaticAttributeKey​(
Object
key)
```

Returns the String that

key

will be registered with.

**Parameters:** key

- the object key
**Returns:** the String that

key

will be registered with
**See Also:** getStaticAttribute(java.lang.Object)

,

registerStaticAttributeKey(java.lang.Object)

Field Detail

- DEFAULT_STYLE

```java
public static final
String
DEFAULT_STYLE
```

The name given to the default logical style attached
to paragraphs.

**See Also:** Constant Field Values

---

#### Field Detail

DEFAULT_STYLE

```java
public static final
String
DEFAULT_STYLE
```

The name given to the default logical style attached
to paragraphs.

**See Also:** Constant Field Values

---

#### DEFAULT_STYLE

public static final

String

DEFAULT_STYLE

The name given to the default logical style attached
to paragraphs.

Constructor Detail

- StyleContext

```java
public StyleContext()
```

Creates a new StyleContext object.

---

#### Constructor Detail

StyleContext

```java
public StyleContext()
```

Creates a new StyleContext object.

---

#### StyleContext

public StyleContext()

Creates a new StyleContext object.

Method Detail

- getDefaultStyleContext

```java
public static final
StyleContext
getDefaultStyleContext()
```

Returns default AttributeContext shared by all documents that
don't bother to define/supply their own context.

**Returns:** the context

- addStyle

```java
public
Style
addStyle​(
String
nm,

Style
parent)
```

Adds a new style into the style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

**Parameters:** nm

- the name of the style (must be unique within the
collection of named styles in the document). The name may
be null if the style is unnamed, but the caller is responsible
for managing the reference returned as an unnamed style can't
be fetched by name. An unnamed style may be useful for things
like character attribute overrides such as found in a style
run.
**Parameters:** parent

- the parent style. This may be null if unspecified
attributes need not be resolved in some other style.
**Returns:** the created style

- removeStyle

```java
public void removeStyle​(
String
nm)
```

Removes a named style previously added to the document.

**Parameters:** nm

- the name of the style to remove

- getStyle

```java
public
Style
getStyle​(
String
nm)
```

Fetches a named style previously added to the document

**Parameters:** nm

- the name of the style
**Returns:** the style

- getStyleNames

```java
public
Enumeration
<?> getStyleNames()
```

Fetches the names of the styles defined.

**Returns:** the list of names as an enumeration

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a listener to track when styles are added
or removed.

**Parameters:** l

- the change listener

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a listener that was tracking styles being
added or removed.

**Parameters:** l

- the change listener

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this StyleContext with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- getFont

```java
public
Font
getFont​(
AttributeSet
attr)
```

Gets the font from an attribute set. This is
implemented to try and fetch a cached font
for the given AttributeSet, and if that fails
the font features are resolved and the
font is fetched from the low-level font cache.

**Parameters:** attr

- the attribute set
**Returns:** the font

- getForeground

```java
public
Color
getForeground​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a foreground color
specification. This might be used to specify things
like brighter, more hue, etc. By default it simply returns
the value specified by the StyleConstants.Foreground attribute.

**Parameters:** attr

- the set of attributes
**Returns:** the color

- getBackground

```java
public
Color
getBackground​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a background color
specification. This might be used to specify things
like brighter, more hue, etc. By default it simply returns
the value specified by the StyleConstants.Background attribute.

**Parameters:** attr

- the set of attributes
**Returns:** the color

- getFont

```java
public
Font
getFont​(
String
family,
int style,
int size)
```

Gets a new font. This returns a Font from a cache
if a cached font exists. If not, a Font is added to
the cache. This is basically a low-level cache for
1.1 font features.

**Parameters:** family

- the font family (such as "Monospaced")
**Parameters:** style

- the style of the font (such as Font.PLAIN)
**Parameters:** size

- the point size >= 1
**Returns:** the new font

- getFontMetrics

```java
public
FontMetrics
getFontMetrics​(
Font
f)
```

Returns font metrics for a font.

**Parameters:** f

- the font
**Returns:** the metrics

- addAttribute

```java
public
AttributeSet
addAttribute​(
AttributeSet
old,

Object
name,

Object
value)
```

Adds an attribute to the given set, and returns
the new representative set.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** addAttribute

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old attribute set
**Parameters:** name

- the non-null attribute name
**Parameters:** value

- the attribute value
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

- addAttributes

```java
public
AttributeSet
addAttributes​(
AttributeSet
old,

AttributeSet
attr)
```

Adds a set of attributes to the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** addAttributes

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old attribute set
**Parameters:** attr

- the attributes to add
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

- removeAttribute

```java
public
AttributeSet
removeAttribute​(
AttributeSet
old,

Object
name)
```

Removes an attribute from the set.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** removeAttribute

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old set of attributes
**Parameters:** name

- the non-null attribute name
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttribute(java.lang.Object)

- removeAttributes

```java
public
AttributeSet
removeAttributes​(
AttributeSet
old,

Enumeration
<?> names)
```

Removes a set of attributes for the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** removeAttributes

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old attribute set
**Parameters:** names

- the attribute names
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

- removeAttributes

```java
public
AttributeSet
removeAttributes​(
AttributeSet
old,

AttributeSet
attrs)
```

Removes a set of attributes for the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** removeAttributes

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old attribute set
**Parameters:** attrs

- the attributes
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

- getEmptySet

```java
public
AttributeSet
getEmptySet()
```

Fetches an empty AttributeSet.

**Specified by:** getEmptySet

in interface

AbstractDocument.AttributeContext
**Returns:** the set

- reclaim

```java
public void reclaim​(
AttributeSet
a)
```

Returns a set no longer needed by the MutableAttributeSet implementation.
This is useful for operation under 1.1 where there are no weak
references. This would typically be called by the finalize method
of the MutableAttributeSet implementation.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** reclaim

in interface

AbstractDocument.AttributeContext
**Parameters:** a

- the set to reclaim

- getCompressionThreshold

```java
protected int getCompressionThreshold()
```

Returns the maximum number of key/value pairs to try and
compress into unique/immutable sets. Any sets above this
limit will use hashtables and be a MutableAttributeSet.

**Returns:** the threshold

- createSmallAttributeSet

```java
protected
StyleContext.SmallAttributeSet
createSmallAttributeSet​(
AttributeSet
a)
```

Create a compact set of attributes that might be shared.
This is a hook for subclasses that want to alter the
behavior of SmallAttributeSet. This can be reimplemented
to return an AttributeSet that provides some sort of
attribute conversion.

**Parameters:** a

- The set of attributes to be represented in the
the compact form.
**Returns:** a compact set of attributes that might be shared

- createLargeAttributeSet

```java
protected
MutableAttributeSet
createLargeAttributeSet​(
AttributeSet
a)
```

Create a large set of attributes that should trade off
space for time. This set will not be shared. This is
a hook for subclasses that want to alter the behavior
of the larger attribute storage format (which is
SimpleAttributeSet by default). This can be reimplemented
to return a MutableAttributeSet that provides some sort of
attribute conversion.

**Parameters:** a

- The set of attributes to be represented in the
the larger form.
**Returns:** a large set of attributes that should trade off
space for time

- toString

```java
public
String
toString()
```

Converts a StyleContext to a String.

**Overrides:** toString

in class

Object
**Returns:** the string

- writeAttributes

```java
public void writeAttributes​(
ObjectOutputStream
out,

AttributeSet
a)
throws
IOException
```

Context-specific handling of writing out attributes

**Parameters:** out

- the output stream
**Parameters:** a

- the attribute set
**Throws:** IOException

- on any I/O error

- readAttributes

```java
public void readAttributes​(
ObjectInputStream
in,

MutableAttributeSet
a)
throws
ClassNotFoundException
,

IOException
```

Context-specific handling of reading in attributes

**Parameters:** in

- the object stream to read the attribute data from.
**Parameters:** a

- the attribute set to place the attribute
definitions in.
**Throws:** ClassNotFoundException

- passed upward if encountered
when reading the object stream.
**Throws:** IOException

- passed upward if encountered when
reading the object stream.

- writeAttributeSet

```java
public static void writeAttributeSet​(
ObjectOutputStream
out,

AttributeSet
a)
throws
IOException
```

Writes a set of attributes to the given object stream
for the purpose of serialization. This will take
special care to deal with static attribute keys that
have been registered wit the

registerStaticAttributeKey

method.
Any attribute key not registered as a static key
will be serialized directly. All values are expected
to be serializable.

**Parameters:** out

- the output stream
**Parameters:** a

- the attribute set
**Throws:** IOException

- on any I/O error

- readAttributeSet

```java
public static void readAttributeSet​(
ObjectInputStream
in,

MutableAttributeSet
a)
throws
ClassNotFoundException
,

IOException
```

Reads a set of attributes from the given object input
stream that have been previously written out with

writeAttributeSet

. This will try to restore
keys that were static objects to the static objects in
the current virtual machine considering only those keys
that have been registered with the

registerStaticAttributeKey

method.
The attributes retrieved from the stream will be placed
into the given mutable set.

**Parameters:** in

- the object stream to read the attribute data from.
**Parameters:** a

- the attribute set to place the attribute
definitions in.
**Throws:** ClassNotFoundException

- passed upward if encountered
when reading the object stream.
**Throws:** IOException

- passed upward if encountered when
reading the object stream.

- registerStaticAttributeKey

```java
public static void registerStaticAttributeKey​(
Object
key)
```

Registers an object as a static object that is being
used as a key in attribute sets. This allows the key
to be treated specially for serialization.

For operation under a 1.1 virtual machine, this
uses the value returned by

toString

concatenated to the classname. The value returned
by toString should not have the class reference
in it (ie it should be reimplemented from the
definition in Object) in order to be the same when
recomputed later.

**Parameters:** key

- the non-null object key

- getStaticAttribute

```java
public static
Object
getStaticAttribute​(
Object
key)
```

Returns the object previously registered with

registerStaticAttributeKey

.

**Parameters:** key

- the object key
**Returns:** Returns the object previously registered with

registerStaticAttributeKey

- getStaticAttributeKey

```java
public static
Object
getStaticAttributeKey​(
Object
key)
```

Returns the String that

key

will be registered with.

**Parameters:** key

- the object key
**Returns:** the String that

key

will be registered with
**See Also:** getStaticAttribute(java.lang.Object)

,

registerStaticAttributeKey(java.lang.Object)

---

#### Method Detail

getDefaultStyleContext

```java
public static final
StyleContext
getDefaultStyleContext()
```

Returns default AttributeContext shared by all documents that
don't bother to define/supply their own context.

**Returns:** the context

---

#### getDefaultStyleContext

public static final

StyleContext

getDefaultStyleContext()

Returns default AttributeContext shared by all documents that
don't bother to define/supply their own context.

addStyle

```java
public
Style
addStyle​(
String
nm,

Style
parent)
```

Adds a new style into the style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

**Parameters:** nm

- the name of the style (must be unique within the
collection of named styles in the document). The name may
be null if the style is unnamed, but the caller is responsible
for managing the reference returned as an unnamed style can't
be fetched by name. An unnamed style may be useful for things
like character attribute overrides such as found in a style
run.
**Parameters:** parent

- the parent style. This may be null if unspecified
attributes need not be resolved in some other style.
**Returns:** the created style

---

#### addStyle

public

Style

addStyle​(

String

nm,

Style

parent)

Adds a new style into the style hierarchy. Style attributes
resolve from bottom up so an attribute specified in a child
will override an attribute specified in the parent.

removeStyle

```java
public void removeStyle​(
String
nm)
```

Removes a named style previously added to the document.

**Parameters:** nm

- the name of the style to remove

---

#### removeStyle

public void removeStyle​(

String

nm)

Removes a named style previously added to the document.

getStyle

```java
public
Style
getStyle​(
String
nm)
```

Fetches a named style previously added to the document

**Parameters:** nm

- the name of the style
**Returns:** the style

---

#### getStyle

public

Style

getStyle​(

String

nm)

Fetches a named style previously added to the document

getStyleNames

```java
public
Enumeration
<?> getStyleNames()
```

Fetches the names of the styles defined.

**Returns:** the list of names as an enumeration

---

#### getStyleNames

public

Enumeration

<?> getStyleNames()

Fetches the names of the styles defined.

addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a listener to track when styles are added
or removed.

**Parameters:** l

- the change listener

---

#### addChangeListener

public void addChangeListener​(

ChangeListener

l)

Adds a listener to track when styles are added
or removed.

removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a listener that was tracking styles being
added or removed.

**Parameters:** l

- the change listener

---

#### removeChangeListener

public void removeChangeListener​(

ChangeListener

l)

Removes a listener that was tracking styles being
added or removed.

getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this StyleContext with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getChangeListeners

public

ChangeListener

[] getChangeListeners()

Returns an array of all the

ChangeListener

s added
to this StyleContext with addChangeListener().

getFont

```java
public
Font
getFont​(
AttributeSet
attr)
```

Gets the font from an attribute set. This is
implemented to try and fetch a cached font
for the given AttributeSet, and if that fails
the font features are resolved and the
font is fetched from the low-level font cache.

**Parameters:** attr

- the attribute set
**Returns:** the font

---

#### getFont

public

Font

getFont​(

AttributeSet

attr)

Gets the font from an attribute set. This is
implemented to try and fetch a cached font
for the given AttributeSet, and if that fails
the font features are resolved and the
font is fetched from the low-level font cache.

getForeground

```java
public
Color
getForeground​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a foreground color
specification. This might be used to specify things
like brighter, more hue, etc. By default it simply returns
the value specified by the StyleConstants.Foreground attribute.

**Parameters:** attr

- the set of attributes
**Returns:** the color

---

#### getForeground

public

Color

getForeground​(

AttributeSet

attr)

Takes a set of attributes and turn it into a foreground color
specification. This might be used to specify things
like brighter, more hue, etc. By default it simply returns
the value specified by the StyleConstants.Foreground attribute.

getBackground

```java
public
Color
getBackground​(
AttributeSet
attr)
```

Takes a set of attributes and turn it into a background color
specification. This might be used to specify things
like brighter, more hue, etc. By default it simply returns
the value specified by the StyleConstants.Background attribute.

**Parameters:** attr

- the set of attributes
**Returns:** the color

---

#### getBackground

public

Color

getBackground​(

AttributeSet

attr)

Takes a set of attributes and turn it into a background color
specification. This might be used to specify things
like brighter, more hue, etc. By default it simply returns
the value specified by the StyleConstants.Background attribute.

getFont

```java
public
Font
getFont​(
String
family,
int style,
int size)
```

Gets a new font. This returns a Font from a cache
if a cached font exists. If not, a Font is added to
the cache. This is basically a low-level cache for
1.1 font features.

**Parameters:** family

- the font family (such as "Monospaced")
**Parameters:** style

- the style of the font (such as Font.PLAIN)
**Parameters:** size

- the point size >= 1
**Returns:** the new font

---

#### getFont

public

Font

getFont​(

String

family,
int style,
int size)

Gets a new font. This returns a Font from a cache
if a cached font exists. If not, a Font is added to
the cache. This is basically a low-level cache for
1.1 font features.

getFontMetrics

```java
public
FontMetrics
getFontMetrics​(
Font
f)
```

Returns font metrics for a font.

**Parameters:** f

- the font
**Returns:** the metrics

---

#### getFontMetrics

public

FontMetrics

getFontMetrics​(

Font

f)

Returns font metrics for a font.

addAttribute

```java
public
AttributeSet
addAttribute​(
AttributeSet
old,

Object
name,

Object
value)
```

Adds an attribute to the given set, and returns
the new representative set.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** addAttribute

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old attribute set
**Parameters:** name

- the non-null attribute name
**Parameters:** value

- the attribute value
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

---

#### addAttribute

public

AttributeSet

addAttribute​(

AttributeSet

old,

Object

name,

Object

value)

Adds an attribute to the given set, and returns
the new representative set.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

addAttributes

```java
public
AttributeSet
addAttributes​(
AttributeSet
old,

AttributeSet
attr)
```

Adds a set of attributes to the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** addAttributes

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old attribute set
**Parameters:** attr

- the attributes to add
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.addAttribute(java.lang.Object, java.lang.Object)

---

#### addAttributes

public

AttributeSet

addAttributes​(

AttributeSet

old,

AttributeSet

attr)

Adds a set of attributes to the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

removeAttribute

```java
public
AttributeSet
removeAttribute​(
AttributeSet
old,

Object
name)
```

Removes an attribute from the set.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** removeAttribute

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old set of attributes
**Parameters:** name

- the non-null attribute name
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttribute(java.lang.Object)

---

#### removeAttribute

public

AttributeSet

removeAttribute​(

AttributeSet

old,

Object

name)

Removes an attribute from the set.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

removeAttributes

```java
public
AttributeSet
removeAttributes​(
AttributeSet
old,

Enumeration
<?> names)
```

Removes a set of attributes for the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** removeAttributes

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old attribute set
**Parameters:** names

- the attribute names
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

---

#### removeAttributes

public

AttributeSet

removeAttributes​(

AttributeSet

old,

Enumeration

<?> names)

Removes a set of attributes for the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

removeAttributes

```java
public
AttributeSet
removeAttributes​(
AttributeSet
old,

AttributeSet
attrs)
```

Removes a set of attributes for the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** removeAttributes

in interface

AbstractDocument.AttributeContext
**Parameters:** old

- the old attribute set
**Parameters:** attrs

- the attributes
**Returns:** the updated attribute set
**See Also:** MutableAttributeSet.removeAttributes(java.util.Enumeration<?>)

---

#### removeAttributes

public

AttributeSet

removeAttributes​(

AttributeSet

old,

AttributeSet

attrs)

Removes a set of attributes for the element.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

getEmptySet

```java
public
AttributeSet
getEmptySet()
```

Fetches an empty AttributeSet.

**Specified by:** getEmptySet

in interface

AbstractDocument.AttributeContext
**Returns:** the set

---

#### getEmptySet

public

AttributeSet

getEmptySet()

Fetches an empty AttributeSet.

reclaim

```java
public void reclaim​(
AttributeSet
a)
```

Returns a set no longer needed by the MutableAttributeSet implementation.
This is useful for operation under 1.1 where there are no weak
references. This would typically be called by the finalize method
of the MutableAttributeSet implementation.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

**Specified by:** reclaim

in interface

AbstractDocument.AttributeContext
**Parameters:** a

- the set to reclaim

---

#### reclaim

public void reclaim​(

AttributeSet

a)

Returns a set no longer needed by the MutableAttributeSet implementation.
This is useful for operation under 1.1 where there are no weak
references. This would typically be called by the finalize method
of the MutableAttributeSet implementation.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

getCompressionThreshold

```java
protected int getCompressionThreshold()
```

Returns the maximum number of key/value pairs to try and
compress into unique/immutable sets. Any sets above this
limit will use hashtables and be a MutableAttributeSet.

**Returns:** the threshold

---

#### getCompressionThreshold

protected int getCompressionThreshold()

Returns the maximum number of key/value pairs to try and
compress into unique/immutable sets. Any sets above this
limit will use hashtables and be a MutableAttributeSet.

createSmallAttributeSet

```java
protected
StyleContext.SmallAttributeSet
createSmallAttributeSet​(
AttributeSet
a)
```

Create a compact set of attributes that might be shared.
This is a hook for subclasses that want to alter the
behavior of SmallAttributeSet. This can be reimplemented
to return an AttributeSet that provides some sort of
attribute conversion.

**Parameters:** a

- The set of attributes to be represented in the
the compact form.
**Returns:** a compact set of attributes that might be shared

---

#### createSmallAttributeSet

protected

StyleContext.SmallAttributeSet

createSmallAttributeSet​(

AttributeSet

a)

Create a compact set of attributes that might be shared.
This is a hook for subclasses that want to alter the
behavior of SmallAttributeSet. This can be reimplemented
to return an AttributeSet that provides some sort of
attribute conversion.

createLargeAttributeSet

```java
protected
MutableAttributeSet
createLargeAttributeSet​(
AttributeSet
a)
```

Create a large set of attributes that should trade off
space for time. This set will not be shared. This is
a hook for subclasses that want to alter the behavior
of the larger attribute storage format (which is
SimpleAttributeSet by default). This can be reimplemented
to return a MutableAttributeSet that provides some sort of
attribute conversion.

**Parameters:** a

- The set of attributes to be represented in the
the larger form.
**Returns:** a large set of attributes that should trade off
space for time

---

#### createLargeAttributeSet

protected

MutableAttributeSet

createLargeAttributeSet​(

AttributeSet

a)

Create a large set of attributes that should trade off
space for time. This set will not be shared. This is
a hook for subclasses that want to alter the behavior
of the larger attribute storage format (which is
SimpleAttributeSet by default). This can be reimplemented
to return a MutableAttributeSet that provides some sort of
attribute conversion.

toString

```java
public
String
toString()
```

Converts a StyleContext to a String.

**Overrides:** toString

in class

Object
**Returns:** the string

---

#### toString

public

String

toString()

Converts a StyleContext to a String.

writeAttributes

```java
public void writeAttributes​(
ObjectOutputStream
out,

AttributeSet
a)
throws
IOException
```

Context-specific handling of writing out attributes

**Parameters:** out

- the output stream
**Parameters:** a

- the attribute set
**Throws:** IOException

- on any I/O error

---

#### writeAttributes

public void writeAttributes​(

ObjectOutputStream

out,

AttributeSet

a)
throws

IOException

Context-specific handling of writing out attributes

readAttributes

```java
public void readAttributes​(
ObjectInputStream
in,

MutableAttributeSet
a)
throws
ClassNotFoundException
,

IOException
```

Context-specific handling of reading in attributes

**Parameters:** in

- the object stream to read the attribute data from.
**Parameters:** a

- the attribute set to place the attribute
definitions in.
**Throws:** ClassNotFoundException

- passed upward if encountered
when reading the object stream.
**Throws:** IOException

- passed upward if encountered when
reading the object stream.

---

#### readAttributes

public void readAttributes​(

ObjectInputStream

in,

MutableAttributeSet

a)
throws

ClassNotFoundException

,

IOException

Context-specific handling of reading in attributes

writeAttributeSet

```java
public static void writeAttributeSet​(
ObjectOutputStream
out,

AttributeSet
a)
throws
IOException
```

Writes a set of attributes to the given object stream
for the purpose of serialization. This will take
special care to deal with static attribute keys that
have been registered wit the

registerStaticAttributeKey

method.
Any attribute key not registered as a static key
will be serialized directly. All values are expected
to be serializable.

**Parameters:** out

- the output stream
**Parameters:** a

- the attribute set
**Throws:** IOException

- on any I/O error

---

#### writeAttributeSet

public static void writeAttributeSet​(

ObjectOutputStream

out,

AttributeSet

a)
throws

IOException

Writes a set of attributes to the given object stream
for the purpose of serialization. This will take
special care to deal with static attribute keys that
have been registered wit the

registerStaticAttributeKey

method.
Any attribute key not registered as a static key
will be serialized directly. All values are expected
to be serializable.

readAttributeSet

```java
public static void readAttributeSet​(
ObjectInputStream
in,

MutableAttributeSet
a)
throws
ClassNotFoundException
,

IOException
```

Reads a set of attributes from the given object input
stream that have been previously written out with

writeAttributeSet

. This will try to restore
keys that were static objects to the static objects in
the current virtual machine considering only those keys
that have been registered with the

registerStaticAttributeKey

method.
The attributes retrieved from the stream will be placed
into the given mutable set.

**Parameters:** in

- the object stream to read the attribute data from.
**Parameters:** a

- the attribute set to place the attribute
definitions in.
**Throws:** ClassNotFoundException

- passed upward if encountered
when reading the object stream.
**Throws:** IOException

- passed upward if encountered when
reading the object stream.

---

#### readAttributeSet

public static void readAttributeSet​(

ObjectInputStream

in,

MutableAttributeSet

a)
throws

ClassNotFoundException

,

IOException

Reads a set of attributes from the given object input
stream that have been previously written out with

writeAttributeSet

. This will try to restore
keys that were static objects to the static objects in
the current virtual machine considering only those keys
that have been registered with the

registerStaticAttributeKey

method.
The attributes retrieved from the stream will be placed
into the given mutable set.

registerStaticAttributeKey

```java
public static void registerStaticAttributeKey​(
Object
key)
```

Registers an object as a static object that is being
used as a key in attribute sets. This allows the key
to be treated specially for serialization.

For operation under a 1.1 virtual machine, this
uses the value returned by

toString

concatenated to the classname. The value returned
by toString should not have the class reference
in it (ie it should be reimplemented from the
definition in Object) in order to be the same when
recomputed later.

**Parameters:** key

- the non-null object key

---

#### registerStaticAttributeKey

public static void registerStaticAttributeKey​(

Object

key)

Registers an object as a static object that is being
used as a key in attribute sets. This allows the key
to be treated specially for serialization.

For operation under a 1.1 virtual machine, this
uses the value returned by

toString

concatenated to the classname. The value returned
by toString should not have the class reference
in it (ie it should be reimplemented from the
definition in Object) in order to be the same when
recomputed later.

For operation under a 1.1 virtual machine, this
uses the value returned by

toString

concatenated to the classname. The value returned
by toString should not have the class reference
in it (ie it should be reimplemented from the
definition in Object) in order to be the same when
recomputed later.

getStaticAttribute

```java
public static
Object
getStaticAttribute​(
Object
key)
```

Returns the object previously registered with

registerStaticAttributeKey

.

**Parameters:** key

- the object key
**Returns:** Returns the object previously registered with

registerStaticAttributeKey

---

#### getStaticAttribute

public static

Object

getStaticAttribute​(

Object

key)

Returns the object previously registered with

registerStaticAttributeKey

.

getStaticAttributeKey

```java
public static
Object
getStaticAttributeKey​(
Object
key)
```

Returns the String that

key

will be registered with.

**Parameters:** key

- the object key
**Returns:** the String that

key

will be registered with
**See Also:** getStaticAttribute(java.lang.Object)

,

registerStaticAttributeKey(java.lang.Object)

---

#### getStaticAttributeKey

public static

Object

getStaticAttributeKey​(

Object

key)

Returns the String that

key

will be registered with.

---

