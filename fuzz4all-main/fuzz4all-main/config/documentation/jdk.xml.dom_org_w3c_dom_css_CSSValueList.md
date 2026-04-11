# Interface CSSValueList

**Source:** `jdk.xml.dom\org\w3c\dom\css\CSSValueList.html`

### Class Description

```java
public interface
CSSValueList

extends
CSSValue
```

The

CSSValueList

interface provides the abstraction of an
ordered collection of CSS values.

Some properties allow an empty list into their syntax. In that case,
these properties take the

none

identifier. So, an empty list
means that the property has the value

none

.

The items in the

CSSValueList

are accessible via an
integral index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**All Superinterfaces:** CSSValue

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getLength()

The number of

CSSValues

in the list. The range of valid
values of the indices is

0

to

length-1

inclusive.

---

#### CSSValue
item​(int index)

Used to retrieve a

CSSValue

by ordinal index. The order in
this collection represents the order of the values in the CSS style
property. If index is greater than or equal to the number of values
in the list, this returns

null

.

**Parameters:**
- index

- Index into the collection.

**Returns:**
- The

CSSValue

at the

index

position
in the

CSSValueList

, or

null

if that is
not a valid index.

---

### Additional Sections

#### Interface CSSValueList

**All Superinterfaces:** CSSValue

```java
public interface
CSSValueList

extends
CSSValue
```

The

CSSValueList

interface provides the abstraction of an
ordered collection of CSS values.

Some properties allow an empty list into their syntax. In that case,
these properties take the

none

identifier. So, an empty list
means that the property has the value

none

.

The items in the

CSSValueList

are accessible via an
integral index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

CSSValueList

extends

CSSValue

The

CSSValueList

interface provides the abstraction of an
ordered collection of CSS values.

Some properties allow an empty list into their syntax. In that case,
these properties take the

none

identifier. So, an empty list
means that the property has the value

none

.

The items in the

CSSValueList

are accessible via an
integral index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

Some properties allow an empty list into their syntax. In that case,
these properties take the

none

identifier. So, an empty list
means that the property has the value

none

.

The items in the

CSSValueList

are accessible via an
integral index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

The items in the

CSSValueList

are accessible via an
integral index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface org.w3c.dom.css.

CSSValue

CSS_CUSTOM

,

CSS_INHERIT

,

CSS_PRIMITIVE_VALUE

,

CSS_VALUE_LIST

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getLength

()

The number of

CSSValues

in the list.

CSSValue

item

​(int index)

Used to retrieve a

CSSValue

by ordinal index.

- Methods declared in interface org.w3c.dom.css.

CSSValue

getCssText

,

getCssValueType

,

setCssText

Field Summary

- Fields declared in interface org.w3c.dom.css.

CSSValue

CSS_CUSTOM

,

CSS_INHERIT

,

CSS_PRIMITIVE_VALUE

,

CSS_VALUE_LIST

---

#### Field Summary

Fields declared in interface org.w3c.dom.css.

CSSValue

CSS_CUSTOM

,

CSS_INHERIT

,

CSS_PRIMITIVE_VALUE

,

CSS_VALUE_LIST

---

#### Fields declared in interface org.w3c.dom.css. CSSValue

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getLength

()

The number of

CSSValues

in the list.

CSSValue

item

​(int index)

Used to retrieve a

CSSValue

by ordinal index.

- Methods declared in interface org.w3c.dom.css.

CSSValue

getCssText

,

getCssValueType

,

setCssText

---

#### Method Summary

The number of

CSSValues

in the list.

Used to retrieve a

CSSValue

by ordinal index.

Methods declared in interface org.w3c.dom.css.

CSSValue

getCssText

,

getCssValueType

,

setCssText

---

#### Methods declared in interface org.w3c.dom.css. CSSValue

============ METHOD DETAIL ==========

- Method Detail

- getLength

```java
int getLength()
```

The number of

CSSValues

in the list. The range of valid
values of the indices is

0

to

length-1

inclusive.

- item

```java
CSSValue
item​(int index)
```

Used to retrieve a

CSSValue

by ordinal index. The order in
this collection represents the order of the values in the CSS style
property. If index is greater than or equal to the number of values
in the list, this returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The

CSSValue

at the

index

position
in the

CSSValueList

, or

null

if that is
not a valid index.

Method Detail

- getLength

```java
int getLength()
```

The number of

CSSValues

in the list. The range of valid
values of the indices is

0

to

length-1

inclusive.

- item

```java
CSSValue
item​(int index)
```

Used to retrieve a

CSSValue

by ordinal index. The order in
this collection represents the order of the values in the CSS style
property. If index is greater than or equal to the number of values
in the list, this returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The

CSSValue

at the

index

position
in the

CSSValueList

, or

null

if that is
not a valid index.

---

#### Method Detail

getLength

```java
int getLength()
```

The number of

CSSValues

in the list. The range of valid
values of the indices is

0

to

length-1

inclusive.

---

#### getLength

int getLength()

The number of

CSSValues

in the list. The range of valid
values of the indices is

0

to

length-1

inclusive.

item

```java
CSSValue
item​(int index)
```

Used to retrieve a

CSSValue

by ordinal index. The order in
this collection represents the order of the values in the CSS style
property. If index is greater than or equal to the number of values
in the list, this returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The

CSSValue

at the

index

position
in the

CSSValueList

, or

null

if that is
not a valid index.

---

#### item

CSSValue

item​(int index)

Used to retrieve a

CSSValue

by ordinal index. The order in
this collection represents the order of the values in the CSS style
property. If index is greater than or equal to the number of values
in the list, this returns

null

.

---

