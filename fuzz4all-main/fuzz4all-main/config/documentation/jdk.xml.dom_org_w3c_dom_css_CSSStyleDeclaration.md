# Interface CSSStyleDeclaration

**Source:** `jdk.xml.dom\org\w3c\dom\css\CSSStyleDeclaration.html`

### Class Description

```java
public interface
CSSStyleDeclaration
```

The

CSSStyleDeclaration

interface represents a single CSS
declaration block. This interface may be used to determine the style
properties currently set in a block or to set style properties explicitly
within the block.

While an implementation may not recognize all CSS properties within a
CSS declaration block, it is expected to provide access to all specified
properties in the style sheet through the

CSSStyleDeclaration

interface. Furthermore, implementations that support a specific level of
CSS should correctly handle CSS shorthand properties for that level. For
a further discussion of shorthand properties, see the

CSS2Properties

interface.

This interface is also used to provide a read-only access to the
computed values of an element. See also the

ViewCSS

interface. The CSS Object Model doesn't provide an access to the
specified or actual values of the CSS cascade.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getCssText()

The parsable textual representation of the declaration block
(excluding the surrounding curly braces). Setting this attribute will
result in the parsing of the new value and resetting of all the
properties in the declaration block including the removal or addition
of properties.

---

#### void setCssText​(
String
cssText)
throws
DOMException

The parsable textual representation of the declaration block
(excluding the surrounding curly braces). Setting this attribute will
result in the parsing of the new value and resetting of all the
properties in the declaration block including the removal or addition
of properties.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this declaration is
readonly or a property is readonly.

---

#### String
getPropertyValue​(
String
propertyName)

Used to retrieve the value of a CSS property if it has been explicitly
set within this declaration block.

**Parameters:**
- propertyName

- The name of the CSS property. See the CSS
property index.

**Returns:**
- Returns the value of the property if it has been explicitly
set for this declaration block. Returns the empty string if the
property has not been set.

---

#### CSSValue
getPropertyCSSValue​(
String
propertyName)

Used to retrieve the object representation of the value of a CSS
property if it has been explicitly set within this declaration block.
This method returns

null

if the property is a shorthand
property. Shorthand property values can only be accessed and modified
as strings, using the

getPropertyValue

and

setProperty

methods.

**Parameters:**
- propertyName

- The name of the CSS property. See the CSS
property index.

**Returns:**
- Returns the value of the property if it has been explicitly
set for this declaration block. Returns

null

if the
property has not been set.

---

#### String
removeProperty​(
String
propertyName)
throws
DOMException

Used to remove a CSS property if it has been explicitly set within
this declaration block.

**Parameters:**
- propertyName

- The name of the CSS property. See the CSS
property index.

**Returns:**
- Returns the value of the property if it has been explicitly
set for this declaration block. Returns the empty string if the
property has not been set or the property name does not correspond
to a known CSS property.

**Throws:**
- DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if this declaration is readonly
or the property is readonly.

---

#### String
getPropertyPriority​(
String
propertyName)

Used to retrieve the priority of a CSS property (e.g. the

"important"

qualifier) if the priority has been
explicitly set in this declaration block.

**Parameters:**
- propertyName

- The name of the CSS property. See the CSS
property index.

**Returns:**
- A string representing the priority (e.g.

"important"

) if the property has been explicitly set
in this declaration block and has a priority specified. The empty
string otherwise.

---

#### void setProperty​(
String
propertyName,

String
value,

String
priority)
throws
DOMException

Used to set a property value and priority within this declaration
block.

setProperty

permits to modify a property or add a
new one in the declaration block. Any call to this method may modify
the order of properties in the

item

method.

**Parameters:**
- propertyName

- The name of the CSS property. See the CSS
property index.
- value

- The new value of the property.
- priority

- The new priority of the property (e.g.

"important"

) or the empty string if none.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the specified value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this declaration is
readonly or the property is readonly.

---

#### int getLength()

The number of properties that have been explicitly set in this
declaration block. The range of valid indices is 0 to length-1
inclusive.

---

#### String
item​(int index)

Used to retrieve the properties that have been explicitly set in this
declaration block. The order of the properties retrieved using this
method does not have to be the order in which they were set. This
method can be used to iterate over all properties in this declaration
block.

**Parameters:**
- index

- Index of the property name to retrieve.

**Returns:**
- The name of the property at this ordinal position. The empty
string if no property exists at this position.

---

#### CSSRule
getParentRule()

The CSS rule that contains this declaration block or

null

if this

CSSStyleDeclaration

is not attached to a

CSSRule

.

---

### Additional Sections

#### Interface CSSStyleDeclaration

```java
public interface
CSSStyleDeclaration
```

The

CSSStyleDeclaration

interface represents a single CSS
declaration block. This interface may be used to determine the style
properties currently set in a block or to set style properties explicitly
within the block.

While an implementation may not recognize all CSS properties within a
CSS declaration block, it is expected to provide access to all specified
properties in the style sheet through the

CSSStyleDeclaration

interface. Furthermore, implementations that support a specific level of
CSS should correctly handle CSS shorthand properties for that level. For
a further discussion of shorthand properties, see the

CSS2Properties

interface.

This interface is also used to provide a read-only access to the
computed values of an element. See also the

ViewCSS

interface. The CSS Object Model doesn't provide an access to the
specified or actual values of the CSS cascade.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

CSSStyleDeclaration

The

CSSStyleDeclaration

interface represents a single CSS
declaration block. This interface may be used to determine the style
properties currently set in a block or to set style properties explicitly
within the block.

While an implementation may not recognize all CSS properties within a
CSS declaration block, it is expected to provide access to all specified
properties in the style sheet through the

CSSStyleDeclaration

interface. Furthermore, implementations that support a specific level of
CSS should correctly handle CSS shorthand properties for that level. For
a further discussion of shorthand properties, see the

CSS2Properties

interface.

This interface is also used to provide a read-only access to the
computed values of an element. See also the

ViewCSS

interface. The CSS Object Model doesn't provide an access to the
specified or actual values of the CSS cascade.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

While an implementation may not recognize all CSS properties within a
CSS declaration block, it is expected to provide access to all specified
properties in the style sheet through the

CSSStyleDeclaration

interface. Furthermore, implementations that support a specific level of
CSS should correctly handle CSS shorthand properties for that level. For
a further discussion of shorthand properties, see the

CSS2Properties

interface.

This interface is also used to provide a read-only access to the
computed values of an element. See also the

ViewCSS

interface. The CSS Object Model doesn't provide an access to the
specified or actual values of the CSS cascade.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

This interface is also used to provide a read-only access to the
computed values of an element. See also the

ViewCSS

interface. The CSS Object Model doesn't provide an access to the
specified or actual values of the CSS cascade.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getCssText

()

The parsable textual representation of the declaration block
(excluding the surrounding curly braces).

int

getLength

()

The number of properties that have been explicitly set in this
declaration block.

CSSRule

getParentRule

()

The CSS rule that contains this declaration block or

null

if this

CSSStyleDeclaration

is not attached to a

CSSRule

.

CSSValue

getPropertyCSSValue

​(

String

propertyName)

Used to retrieve the object representation of the value of a CSS
property if it has been explicitly set within this declaration block.

String

getPropertyPriority

​(

String

propertyName)

Used to retrieve the priority of a CSS property (e.g. the

"important"

qualifier) if the priority has been
explicitly set in this declaration block.

String

getPropertyValue

​(

String

propertyName)

Used to retrieve the value of a CSS property if it has been explicitly
set within this declaration block.

String

item

​(int index)

Used to retrieve the properties that have been explicitly set in this
declaration block.

String

removeProperty

​(

String

propertyName)

Used to remove a CSS property if it has been explicitly set within
this declaration block.

void

setCssText

​(

String

cssText)

The parsable textual representation of the declaration block
(excluding the surrounding curly braces).

void

setProperty

​(

String

propertyName,

String

value,

String

priority)

Used to set a property value and priority within this declaration
block.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getCssText

()

The parsable textual representation of the declaration block
(excluding the surrounding curly braces).

int

getLength

()

The number of properties that have been explicitly set in this
declaration block.

CSSRule

getParentRule

()

The CSS rule that contains this declaration block or

null

if this

CSSStyleDeclaration

is not attached to a

CSSRule

.

CSSValue

getPropertyCSSValue

​(

String

propertyName)

Used to retrieve the object representation of the value of a CSS
property if it has been explicitly set within this declaration block.

String

getPropertyPriority

​(

String

propertyName)

Used to retrieve the priority of a CSS property (e.g. the

"important"

qualifier) if the priority has been
explicitly set in this declaration block.

String

getPropertyValue

​(

String

propertyName)

Used to retrieve the value of a CSS property if it has been explicitly
set within this declaration block.

String

item

​(int index)

Used to retrieve the properties that have been explicitly set in this
declaration block.

String

removeProperty

​(

String

propertyName)

Used to remove a CSS property if it has been explicitly set within
this declaration block.

void

setCssText

​(

String

cssText)

The parsable textual representation of the declaration block
(excluding the surrounding curly braces).

void

setProperty

​(

String

propertyName,

String

value,

String

priority)

Used to set a property value and priority within this declaration
block.

---

#### Method Summary

The parsable textual representation of the declaration block
(excluding the surrounding curly braces).

The number of properties that have been explicitly set in this
declaration block.

The CSS rule that contains this declaration block or

null

if this

CSSStyleDeclaration

is not attached to a

CSSRule

.

Used to retrieve the object representation of the value of a CSS
property if it has been explicitly set within this declaration block.

Used to retrieve the priority of a CSS property (e.g. the

"important"

qualifier) if the priority has been
explicitly set in this declaration block.

Used to retrieve the value of a CSS property if it has been explicitly
set within this declaration block.

Used to retrieve the properties that have been explicitly set in this
declaration block.

Used to remove a CSS property if it has been explicitly set within
this declaration block.

Used to set a property value and priority within this declaration
block.

============ METHOD DETAIL ==========

- Method Detail

- getCssText

```java
String
getCssText()
```

The parsable textual representation of the declaration block
(excluding the surrounding curly braces). Setting this attribute will
result in the parsing of the new value and resetting of all the
properties in the declaration block including the removal or addition
of properties.

- setCssText

```java
void setCssText​(
String
cssText)
throws
DOMException
```

The parsable textual representation of the declaration block
(excluding the surrounding curly braces). Setting this attribute will
result in the parsing of the new value and resetting of all the
properties in the declaration block including the removal or addition
of properties.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this declaration is
readonly or a property is readonly.

- getPropertyValue

```java
String
getPropertyValue​(
String
propertyName)
```

Used to retrieve the value of a CSS property if it has been explicitly
set within this declaration block.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Returns:** Returns the value of the property if it has been explicitly
set for this declaration block. Returns the empty string if the
property has not been set.

- getPropertyCSSValue

```java
CSSValue
getPropertyCSSValue​(
String
propertyName)
```

Used to retrieve the object representation of the value of a CSS
property if it has been explicitly set within this declaration block.
This method returns

null

if the property is a shorthand
property. Shorthand property values can only be accessed and modified
as strings, using the

getPropertyValue

and

setProperty

methods.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Returns:** Returns the value of the property if it has been explicitly
set for this declaration block. Returns

null

if the
property has not been set.

- removeProperty

```java
String
removeProperty​(
String
propertyName)
throws
DOMException
```

Used to remove a CSS property if it has been explicitly set within
this declaration block.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Returns:** Returns the value of the property if it has been explicitly
set for this declaration block. Returns the empty string if the
property has not been set or the property name does not correspond
to a known CSS property.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if this declaration is readonly
or the property is readonly.

- getPropertyPriority

```java
String
getPropertyPriority​(
String
propertyName)
```

Used to retrieve the priority of a CSS property (e.g. the

"important"

qualifier) if the priority has been
explicitly set in this declaration block.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Returns:** A string representing the priority (e.g.

"important"

) if the property has been explicitly set
in this declaration block and has a priority specified. The empty
string otherwise.

- setProperty

```java
void setProperty​(
String
propertyName,

String
value,

String
priority)
throws
DOMException
```

Used to set a property value and priority within this declaration
block.

setProperty

permits to modify a property or add a
new one in the declaration block. Any call to this method may modify
the order of properties in the

item

method.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Parameters:** value

- The new value of the property.
**Parameters:** priority

- The new priority of the property (e.g.

"important"

) or the empty string if none.
**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this declaration is
readonly or the property is readonly.

- getLength

```java
int getLength()
```

The number of properties that have been explicitly set in this
declaration block. The range of valid indices is 0 to length-1
inclusive.

- item

```java
String
item​(int index)
```

Used to retrieve the properties that have been explicitly set in this
declaration block. The order of the properties retrieved using this
method does not have to be the order in which they were set. This
method can be used to iterate over all properties in this declaration
block.

**Parameters:** index

- Index of the property name to retrieve.
**Returns:** The name of the property at this ordinal position. The empty
string if no property exists at this position.

- getParentRule

```java
CSSRule
getParentRule()
```

The CSS rule that contains this declaration block or

null

if this

CSSStyleDeclaration

is not attached to a

CSSRule

.

Method Detail

- getCssText

```java
String
getCssText()
```

The parsable textual representation of the declaration block
(excluding the surrounding curly braces). Setting this attribute will
result in the parsing of the new value and resetting of all the
properties in the declaration block including the removal or addition
of properties.

- setCssText

```java
void setCssText​(
String
cssText)
throws
DOMException
```

The parsable textual representation of the declaration block
(excluding the surrounding curly braces). Setting this attribute will
result in the parsing of the new value and resetting of all the
properties in the declaration block including the removal or addition
of properties.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this declaration is
readonly or a property is readonly.

- getPropertyValue

```java
String
getPropertyValue​(
String
propertyName)
```

Used to retrieve the value of a CSS property if it has been explicitly
set within this declaration block.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Returns:** Returns the value of the property if it has been explicitly
set for this declaration block. Returns the empty string if the
property has not been set.

- getPropertyCSSValue

```java
CSSValue
getPropertyCSSValue​(
String
propertyName)
```

Used to retrieve the object representation of the value of a CSS
property if it has been explicitly set within this declaration block.
This method returns

null

if the property is a shorthand
property. Shorthand property values can only be accessed and modified
as strings, using the

getPropertyValue

and

setProperty

methods.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Returns:** Returns the value of the property if it has been explicitly
set for this declaration block. Returns

null

if the
property has not been set.

- removeProperty

```java
String
removeProperty​(
String
propertyName)
throws
DOMException
```

Used to remove a CSS property if it has been explicitly set within
this declaration block.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Returns:** Returns the value of the property if it has been explicitly
set for this declaration block. Returns the empty string if the
property has not been set or the property name does not correspond
to a known CSS property.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if this declaration is readonly
or the property is readonly.

- getPropertyPriority

```java
String
getPropertyPriority​(
String
propertyName)
```

Used to retrieve the priority of a CSS property (e.g. the

"important"

qualifier) if the priority has been
explicitly set in this declaration block.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Returns:** A string representing the priority (e.g.

"important"

) if the property has been explicitly set
in this declaration block and has a priority specified. The empty
string otherwise.

- setProperty

```java
void setProperty​(
String
propertyName,

String
value,

String
priority)
throws
DOMException
```

Used to set a property value and priority within this declaration
block.

setProperty

permits to modify a property or add a
new one in the declaration block. Any call to this method may modify
the order of properties in the

item

method.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Parameters:** value

- The new value of the property.
**Parameters:** priority

- The new priority of the property (e.g.

"important"

) or the empty string if none.
**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this declaration is
readonly or the property is readonly.

- getLength

```java
int getLength()
```

The number of properties that have been explicitly set in this
declaration block. The range of valid indices is 0 to length-1
inclusive.

- item

```java
String
item​(int index)
```

Used to retrieve the properties that have been explicitly set in this
declaration block. The order of the properties retrieved using this
method does not have to be the order in which they were set. This
method can be used to iterate over all properties in this declaration
block.

**Parameters:** index

- Index of the property name to retrieve.
**Returns:** The name of the property at this ordinal position. The empty
string if no property exists at this position.

- getParentRule

```java
CSSRule
getParentRule()
```

The CSS rule that contains this declaration block or

null

if this

CSSStyleDeclaration

is not attached to a

CSSRule

.

---

#### Method Detail

getCssText

```java
String
getCssText()
```

The parsable textual representation of the declaration block
(excluding the surrounding curly braces). Setting this attribute will
result in the parsing of the new value and resetting of all the
properties in the declaration block including the removal or addition
of properties.

---

#### getCssText

String

getCssText()

The parsable textual representation of the declaration block
(excluding the surrounding curly braces). Setting this attribute will
result in the parsing of the new value and resetting of all the
properties in the declaration block including the removal or addition
of properties.

setCssText

```java
void setCssText​(
String
cssText)
throws
DOMException
```

The parsable textual representation of the declaration block
(excluding the surrounding curly braces). Setting this attribute will
result in the parsing of the new value and resetting of all the
properties in the declaration block including the removal or addition
of properties.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this declaration is
readonly or a property is readonly.

---

#### setCssText

void setCssText​(

String

cssText)
throws

DOMException

The parsable textual representation of the declaration block
(excluding the surrounding curly braces). Setting this attribute will
result in the parsing of the new value and resetting of all the
properties in the declaration block including the removal or addition
of properties.

getPropertyValue

```java
String
getPropertyValue​(
String
propertyName)
```

Used to retrieve the value of a CSS property if it has been explicitly
set within this declaration block.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Returns:** Returns the value of the property if it has been explicitly
set for this declaration block. Returns the empty string if the
property has not been set.

---

#### getPropertyValue

String

getPropertyValue​(

String

propertyName)

Used to retrieve the value of a CSS property if it has been explicitly
set within this declaration block.

getPropertyCSSValue

```java
CSSValue
getPropertyCSSValue​(
String
propertyName)
```

Used to retrieve the object representation of the value of a CSS
property if it has been explicitly set within this declaration block.
This method returns

null

if the property is a shorthand
property. Shorthand property values can only be accessed and modified
as strings, using the

getPropertyValue

and

setProperty

methods.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Returns:** Returns the value of the property if it has been explicitly
set for this declaration block. Returns

null

if the
property has not been set.

---

#### getPropertyCSSValue

CSSValue

getPropertyCSSValue​(

String

propertyName)

Used to retrieve the object representation of the value of a CSS
property if it has been explicitly set within this declaration block.
This method returns

null

if the property is a shorthand
property. Shorthand property values can only be accessed and modified
as strings, using the

getPropertyValue

and

setProperty

methods.

removeProperty

```java
String
removeProperty​(
String
propertyName)
throws
DOMException
```

Used to remove a CSS property if it has been explicitly set within
this declaration block.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Returns:** Returns the value of the property if it has been explicitly
set for this declaration block. Returns the empty string if the
property has not been set or the property name does not correspond
to a known CSS property.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if this declaration is readonly
or the property is readonly.

---

#### removeProperty

String

removeProperty​(

String

propertyName)
throws

DOMException

Used to remove a CSS property if it has been explicitly set within
this declaration block.

getPropertyPriority

```java
String
getPropertyPriority​(
String
propertyName)
```

Used to retrieve the priority of a CSS property (e.g. the

"important"

qualifier) if the priority has been
explicitly set in this declaration block.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Returns:** A string representing the priority (e.g.

"important"

) if the property has been explicitly set
in this declaration block and has a priority specified. The empty
string otherwise.

---

#### getPropertyPriority

String

getPropertyPriority​(

String

propertyName)

Used to retrieve the priority of a CSS property (e.g. the

"important"

qualifier) if the priority has been
explicitly set in this declaration block.

setProperty

```java
void setProperty​(
String
propertyName,

String
value,

String
priority)
throws
DOMException
```

Used to set a property value and priority within this declaration
block.

setProperty

permits to modify a property or add a
new one in the declaration block. Any call to this method may modify
the order of properties in the

item

method.

**Parameters:** propertyName

- The name of the CSS property. See the CSS
property index.
**Parameters:** value

- The new value of the property.
**Parameters:** priority

- The new priority of the property (e.g.

"important"

) or the empty string if none.
**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified value has a syntax error and is
unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this declaration is
readonly or the property is readonly.

---

#### setProperty

void setProperty​(

String

propertyName,

String

value,

String

priority)
throws

DOMException

Used to set a property value and priority within this declaration
block.

setProperty

permits to modify a property or add a
new one in the declaration block. Any call to this method may modify
the order of properties in the

item

method.

getLength

```java
int getLength()
```

The number of properties that have been explicitly set in this
declaration block. The range of valid indices is 0 to length-1
inclusive.

---

#### getLength

int getLength()

The number of properties that have been explicitly set in this
declaration block. The range of valid indices is 0 to length-1
inclusive.

item

```java
String
item​(int index)
```

Used to retrieve the properties that have been explicitly set in this
declaration block. The order of the properties retrieved using this
method does not have to be the order in which they were set. This
method can be used to iterate over all properties in this declaration
block.

**Parameters:** index

- Index of the property name to retrieve.
**Returns:** The name of the property at this ordinal position. The empty
string if no property exists at this position.

---

#### item

String

item​(int index)

Used to retrieve the properties that have been explicitly set in this
declaration block. The order of the properties retrieved using this
method does not have to be the order in which they were set. This
method can be used to iterate over all properties in this declaration
block.

getParentRule

```java
CSSRule
getParentRule()
```

The CSS rule that contains this declaration block or

null

if this

CSSStyleDeclaration

is not attached to a

CSSRule

.

---

#### getParentRule

CSSRule

getParentRule()

The CSS rule that contains this declaration block or

null

if this

CSSStyleDeclaration

is not attached to a

CSSRule

.

---

