# Enum Component.BaselineResizeBehavior

**Source:** `java.desktop\java\awt\Component.BaselineResizeBehavior.html`

### Class Description

```java
public static enum
Component.BaselineResizeBehavior

extends
Enum
<
Component.BaselineResizeBehavior
>
```

Enumeration of the common ways the baseline of a component can
change as the size changes. The baseline resize behavior is
primarily for layout managers that need to know how the
position of the baseline changes as the component size changes.
In general the baseline resize behavior will be valid for sizes
greater than or equal to the minimum size (the actual minimum
size; not a developer specified minimum size). For sizes
smaller than the minimum size the baseline may change in a way
other than the baseline resize behavior indicates. Similarly,
as the size approaches

Integer.MAX_VALUE

and/or

Short.MAX_VALUE

the baseline may change in a way
other than the baseline resize behavior indicates.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Component.BaselineResizeBehavior

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Component.BaselineResizeBehavior
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Component.BaselineResizeBehavior c : Component.BaselineResizeBehavior.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Component.BaselineResizeBehavior
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

### Additional Sections

#### Enum Component.BaselineResizeBehavior

java.lang.Object

- java.lang.Enum

<

Component.BaselineResizeBehavior

>
- - java.awt.Component.BaselineResizeBehavior

java.lang.Enum

<

Component.BaselineResizeBehavior

>

- java.awt.Component.BaselineResizeBehavior

java.awt.Component.BaselineResizeBehavior

**All Implemented Interfaces:** Serializable

,

Comparable

<

Component.BaselineResizeBehavior

>

**Enclosing class:** Component

```java
public static enum
Component.BaselineResizeBehavior

extends
Enum
<
Component.BaselineResizeBehavior
>
```

Enumeration of the common ways the baseline of a component can
change as the size changes. The baseline resize behavior is
primarily for layout managers that need to know how the
position of the baseline changes as the component size changes.
In general the baseline resize behavior will be valid for sizes
greater than or equal to the minimum size (the actual minimum
size; not a developer specified minimum size). For sizes
smaller than the minimum size the baseline may change in a way
other than the baseline resize behavior indicates. Similarly,
as the size approaches

Integer.MAX_VALUE

and/or

Short.MAX_VALUE

the baseline may change in a way
other than the baseline resize behavior indicates.

**Since:** 1.6
**See Also:** Component.getBaselineResizeBehavior()

,

Component.getBaseline(int,int)

public static enum

Component.BaselineResizeBehavior

extends

Enum

<

Component.BaselineResizeBehavior

>

Enumeration of the common ways the baseline of a component can
change as the size changes. The baseline resize behavior is
primarily for layout managers that need to know how the
position of the baseline changes as the component size changes.
In general the baseline resize behavior will be valid for sizes
greater than or equal to the minimum size (the actual minimum
size; not a developer specified minimum size). For sizes
smaller than the minimum size the baseline may change in a way
other than the baseline resize behavior indicates. Similarly,
as the size approaches

Integer.MAX_VALUE

and/or

Short.MAX_VALUE

the baseline may change in a way
other than the baseline resize behavior indicates.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

CENTER_OFFSET

Indicates the baseline remains a fixed distance from
the center of the component.

CONSTANT_ASCENT

Indicates the baseline remains fixed relative to the
y-origin.

CONSTANT_DESCENT

Indicates the baseline remains fixed relative to the height
and does not change as the width is varied.

OTHER

Indicates the baseline resize behavior can not be expressed using
any of the other constants.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Component.BaselineResizeBehavior

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Component.BaselineResizeBehavior

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

CENTER_OFFSET

Indicates the baseline remains a fixed distance from
the center of the component.

CONSTANT_ASCENT

Indicates the baseline remains fixed relative to the
y-origin.

CONSTANT_DESCENT

Indicates the baseline remains fixed relative to the height
and does not change as the width is varied.

OTHER

Indicates the baseline resize behavior can not be expressed using
any of the other constants.

---

#### Enum Constant Summary

Indicates the baseline remains a fixed distance from
the center of the component.

Indicates the baseline remains fixed relative to the
y-origin.

Indicates the baseline remains fixed relative to the height
and does not change as the width is varied.

Indicates the baseline resize behavior can not be expressed using
any of the other constants.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Component.BaselineResizeBehavior

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Component.BaselineResizeBehavior

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

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

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

getClass

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- CONSTANT_ASCENT

```java
public static final
Component.BaselineResizeBehavior
CONSTANT_ASCENT
```

Indicates the baseline remains fixed relative to the
y-origin. That is,

getBaseline

returns
the same value regardless of the height or width. For example, a

JLabel

containing non-empty text with a
vertical alignment of

TOP

should have a
baseline type of

CONSTANT_ASCENT

.

- CONSTANT_DESCENT

```java
public static final
Component.BaselineResizeBehavior
CONSTANT_DESCENT
```

Indicates the baseline remains fixed relative to the height
and does not change as the width is varied. That is, for
any height H the difference between H and

getBaseline(w, H)

is the same. For example, a

JLabel

containing non-empty text with a
vertical alignment of

BOTTOM

should have a
baseline type of

CONSTANT_DESCENT

.

- CENTER_OFFSET

```java
public static final
Component.BaselineResizeBehavior
CENTER_OFFSET
```

Indicates the baseline remains a fixed distance from
the center of the component. That is, for any height H the
difference between

getBaseline(w, H)

and

H / 2

is the same (plus or minus one depending upon
rounding error).

Because of possible rounding errors it is recommended
you ask for the baseline with two consecutive heights and use
the return value to determine if you need to pad calculations
by 1. The following shows how to calculate the baseline for
any height:

```java
Dimension preferredSize = component.getPreferredSize();
int baseline = getBaseline(preferredSize.width,
preferredSize.height);
int nextBaseline = getBaseline(preferredSize.width,
preferredSize.height + 1);
// Amount to add to height when calculating where baseline
// lands for a particular height:
int padding = 0;
// Where the baseline is relative to the mid point
int baselineOffset = baseline - height / 2;
if (preferredSize.height % 2 == 0 &&
baseline != nextBaseline) {
padding = 1;
}
else if (preferredSize.height % 2 == 1 &&
baseline == nextBaseline) {
baselineOffset--;
padding = 1;
}
// The following calculates where the baseline lands for
// the height z:
int calculatedBaseline = (z + padding) / 2 + baselineOffset;
```

- OTHER

```java
public static final
Component.BaselineResizeBehavior
OTHER
```

Indicates the baseline resize behavior can not be expressed using
any of the other constants. This may also indicate the baseline
varies with the width of the component. This is also returned
by components that do not have a baseline.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Component.BaselineResizeBehavior
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Component.BaselineResizeBehavior c : Component.BaselineResizeBehavior.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Component.BaselineResizeBehavior
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

Enum Constant Detail

- CONSTANT_ASCENT

```java
public static final
Component.BaselineResizeBehavior
CONSTANT_ASCENT
```

Indicates the baseline remains fixed relative to the
y-origin. That is,

getBaseline

returns
the same value regardless of the height or width. For example, a

JLabel

containing non-empty text with a
vertical alignment of

TOP

should have a
baseline type of

CONSTANT_ASCENT

.

- CONSTANT_DESCENT

```java
public static final
Component.BaselineResizeBehavior
CONSTANT_DESCENT
```

Indicates the baseline remains fixed relative to the height
and does not change as the width is varied. That is, for
any height H the difference between H and

getBaseline(w, H)

is the same. For example, a

JLabel

containing non-empty text with a
vertical alignment of

BOTTOM

should have a
baseline type of

CONSTANT_DESCENT

.

- CENTER_OFFSET

```java
public static final
Component.BaselineResizeBehavior
CENTER_OFFSET
```

Indicates the baseline remains a fixed distance from
the center of the component. That is, for any height H the
difference between

getBaseline(w, H)

and

H / 2

is the same (plus or minus one depending upon
rounding error).

Because of possible rounding errors it is recommended
you ask for the baseline with two consecutive heights and use
the return value to determine if you need to pad calculations
by 1. The following shows how to calculate the baseline for
any height:

```java
Dimension preferredSize = component.getPreferredSize();
int baseline = getBaseline(preferredSize.width,
preferredSize.height);
int nextBaseline = getBaseline(preferredSize.width,
preferredSize.height + 1);
// Amount to add to height when calculating where baseline
// lands for a particular height:
int padding = 0;
// Where the baseline is relative to the mid point
int baselineOffset = baseline - height / 2;
if (preferredSize.height % 2 == 0 &&
baseline != nextBaseline) {
padding = 1;
}
else if (preferredSize.height % 2 == 1 &&
baseline == nextBaseline) {
baselineOffset--;
padding = 1;
}
// The following calculates where the baseline lands for
// the height z:
int calculatedBaseline = (z + padding) / 2 + baselineOffset;
```

- OTHER

```java
public static final
Component.BaselineResizeBehavior
OTHER
```

Indicates the baseline resize behavior can not be expressed using
any of the other constants. This may also indicate the baseline
varies with the width of the component. This is also returned
by components that do not have a baseline.

---

#### Enum Constant Detail

CONSTANT_ASCENT

```java
public static final
Component.BaselineResizeBehavior
CONSTANT_ASCENT
```

Indicates the baseline remains fixed relative to the
y-origin. That is,

getBaseline

returns
the same value regardless of the height or width. For example, a

JLabel

containing non-empty text with a
vertical alignment of

TOP

should have a
baseline type of

CONSTANT_ASCENT

.

---

#### CONSTANT_ASCENT

public static final

Component.BaselineResizeBehavior

CONSTANT_ASCENT

Indicates the baseline remains fixed relative to the
y-origin. That is,

getBaseline

returns
the same value regardless of the height or width. For example, a

JLabel

containing non-empty text with a
vertical alignment of

TOP

should have a
baseline type of

CONSTANT_ASCENT

.

CONSTANT_DESCENT

```java
public static final
Component.BaselineResizeBehavior
CONSTANT_DESCENT
```

Indicates the baseline remains fixed relative to the height
and does not change as the width is varied. That is, for
any height H the difference between H and

getBaseline(w, H)

is the same. For example, a

JLabel

containing non-empty text with a
vertical alignment of

BOTTOM

should have a
baseline type of

CONSTANT_DESCENT

.

---

#### CONSTANT_DESCENT

public static final

Component.BaselineResizeBehavior

CONSTANT_DESCENT

Indicates the baseline remains fixed relative to the height
and does not change as the width is varied. That is, for
any height H the difference between H and

getBaseline(w, H)

is the same. For example, a

JLabel

containing non-empty text with a
vertical alignment of

BOTTOM

should have a
baseline type of

CONSTANT_DESCENT

.

CENTER_OFFSET

```java
public static final
Component.BaselineResizeBehavior
CENTER_OFFSET
```

Indicates the baseline remains a fixed distance from
the center of the component. That is, for any height H the
difference between

getBaseline(w, H)

and

H / 2

is the same (plus or minus one depending upon
rounding error).

Because of possible rounding errors it is recommended
you ask for the baseline with two consecutive heights and use
the return value to determine if you need to pad calculations
by 1. The following shows how to calculate the baseline for
any height:

```java
Dimension preferredSize = component.getPreferredSize();
int baseline = getBaseline(preferredSize.width,
preferredSize.height);
int nextBaseline = getBaseline(preferredSize.width,
preferredSize.height + 1);
// Amount to add to height when calculating where baseline
// lands for a particular height:
int padding = 0;
// Where the baseline is relative to the mid point
int baselineOffset = baseline - height / 2;
if (preferredSize.height % 2 == 0 &&
baseline != nextBaseline) {
padding = 1;
}
else if (preferredSize.height % 2 == 1 &&
baseline == nextBaseline) {
baselineOffset--;
padding = 1;
}
// The following calculates where the baseline lands for
// the height z:
int calculatedBaseline = (z + padding) / 2 + baselineOffset;
```

---

#### CENTER_OFFSET

public static final

Component.BaselineResizeBehavior

CENTER_OFFSET

Indicates the baseline remains a fixed distance from
the center of the component. That is, for any height H the
difference between

getBaseline(w, H)

and

H / 2

is the same (plus or minus one depending upon
rounding error).

Because of possible rounding errors it is recommended
you ask for the baseline with two consecutive heights and use
the return value to determine if you need to pad calculations
by 1. The following shows how to calculate the baseline for
any height:

```java
Dimension preferredSize = component.getPreferredSize();
int baseline = getBaseline(preferredSize.width,
preferredSize.height);
int nextBaseline = getBaseline(preferredSize.width,
preferredSize.height + 1);
// Amount to add to height when calculating where baseline
// lands for a particular height:
int padding = 0;
// Where the baseline is relative to the mid point
int baselineOffset = baseline - height / 2;
if (preferredSize.height % 2 == 0 &&
baseline != nextBaseline) {
padding = 1;
}
else if (preferredSize.height % 2 == 1 &&
baseline == nextBaseline) {
baselineOffset--;
padding = 1;
}
// The following calculates where the baseline lands for
// the height z:
int calculatedBaseline = (z + padding) / 2 + baselineOffset;
```

Because of possible rounding errors it is recommended
you ask for the baseline with two consecutive heights and use
the return value to determine if you need to pad calculations
by 1. The following shows how to calculate the baseline for
any height:

```java
Dimension preferredSize = component.getPreferredSize();
int baseline = getBaseline(preferredSize.width,
preferredSize.height);
int nextBaseline = getBaseline(preferredSize.width,
preferredSize.height + 1);
// Amount to add to height when calculating where baseline
// lands for a particular height:
int padding = 0;
// Where the baseline is relative to the mid point
int baselineOffset = baseline - height / 2;
if (preferredSize.height % 2 == 0 &&
baseline != nextBaseline) {
padding = 1;
}
else if (preferredSize.height % 2 == 1 &&
baseline == nextBaseline) {
baselineOffset--;
padding = 1;
}
// The following calculates where the baseline lands for
// the height z:
int calculatedBaseline = (z + padding) / 2 + baselineOffset;
```

Dimension preferredSize = component.getPreferredSize();
int baseline = getBaseline(preferredSize.width,
preferredSize.height);
int nextBaseline = getBaseline(preferredSize.width,
preferredSize.height + 1);
// Amount to add to height when calculating where baseline
// lands for a particular height:
int padding = 0;
// Where the baseline is relative to the mid point
int baselineOffset = baseline - height / 2;
if (preferredSize.height % 2 == 0 &&
baseline != nextBaseline) {
padding = 1;
}
else if (preferredSize.height % 2 == 1 &&
baseline == nextBaseline) {
baselineOffset--;
padding = 1;
}
// The following calculates where the baseline lands for
// the height z:
int calculatedBaseline = (z + padding) / 2 + baselineOffset;

OTHER

```java
public static final
Component.BaselineResizeBehavior
OTHER
```

Indicates the baseline resize behavior can not be expressed using
any of the other constants. This may also indicate the baseline
varies with the width of the component. This is also returned
by components that do not have a baseline.

---

#### OTHER

public static final

Component.BaselineResizeBehavior

OTHER

Indicates the baseline resize behavior can not be expressed using
any of the other constants. This may also indicate the baseline
varies with the width of the component. This is also returned
by components that do not have a baseline.

Method Detail

- values

```java
public static
Component.BaselineResizeBehavior
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Component.BaselineResizeBehavior c : Component.BaselineResizeBehavior.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Component.BaselineResizeBehavior
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### Method Detail

values

```java
public static
Component.BaselineResizeBehavior
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Component.BaselineResizeBehavior c : Component.BaselineResizeBehavior.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Component.BaselineResizeBehavior

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Component.BaselineResizeBehavior c : Component.BaselineResizeBehavior.values())
System.out.println(c);
```

for (Component.BaselineResizeBehavior c : Component.BaselineResizeBehavior.values())
System.out.println(c);

valueOf

```java
public static
Component.BaselineResizeBehavior
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

Component.BaselineResizeBehavior

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

