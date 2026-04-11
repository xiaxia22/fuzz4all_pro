# Class ComponentOrientation

**Source:** `java.desktop\java\awt\ComponentOrientation.html`

### Class Description

```java
public final class
ComponentOrientation

extends
Object

implements
Serializable
```

The ComponentOrientation class encapsulates the language-sensitive
orientation that is to be used to order the elements of a component
or of text. It is used to reflect the differences in this ordering
between Western alphabets, Middle Eastern (such as Hebrew), and Far
Eastern (such as Japanese).

Fundamentally, this governs items (such as characters) which are laid out
in lines, with the lines then laid out in a block. This also applies
to items in a widget: for example, in a check box where the box is
positioned relative to the text.

There are four different orientations used in modern languages
as in the following table.

```java
LT RT TL TR
A B C C B A A D G G D A
D E F F E D B E H H E B
G H I I H G C F I I F C
```

(In the header, the two-letter abbreviation represents the item direction
in the first letter, and the line direction in the second. For example,
LT means "items left-to-right, lines top-to-bottom",
TL means "items top-to-bottom, lines left-to-right", and so on.)

The orientations are:

- LT - Western Europe (optional for Japanese, Chinese, Korean)

RT - Middle East (Arabic, Hebrew)

TR - Japanese, Chinese, Korean

TL - Mongolian

Components whose view and controller code depends on orientation
should use the

isLeftToRight()

and

isHorizontal()

methods to
determine their behavior. They should not include switch-like
code that keys off of the constants, such as:

```java
if (orientation == LEFT_TO_RIGHT) {
...
} else if (orientation == RIGHT_TO_LEFT) {
...
} else {
// Oops
}
```

This is unsafe, since more constants may be added in the future and
since it is not guaranteed that orientation objects will be unique.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final
ComponentOrientation
LEFT_TO_RIGHT

Items run left to right and lines flow top to bottom
Examples: English, French.

---

#### public static final
ComponentOrientation
RIGHT_TO_LEFT

Items run right to left and lines flow top to bottom
Examples: Arabic, Hebrew.

---

#### public static final
ComponentOrientation
UNKNOWN

Indicates that a component's orientation has not been set.
To preserve the behavior of existing applications,
isLeftToRight will return true for this value.

---

### Constructor Details

*No entries found.*

### Method Details

#### public boolean isHorizontal()

Are lines horizontal?
This will return true for horizontal, left-to-right writing
systems such as Roman.

**Returns:**
- true

if this orientation has horizontal lines

---

#### public boolean isLeftToRight()

HorizontalLines: Do items run left-to-right?

Vertical Lines: Do lines run left-to-right?

This will return true for horizontal, left-to-right writing
systems such as Roman.

**Returns:**
- true

if this orientation is left-to-right

---

#### public static
ComponentOrientation
getOrientation​(
Locale
locale)

Returns the orientation that is appropriate for the given locale.

**Parameters:**
- locale

- the specified locale

**Returns:**
- the orientation for the locale

---

#### @Deprecated

public static
ComponentOrientation
getOrientation​(
ResourceBundle
bdl)

Returns the orientation appropriate for the given ResourceBundle's
localization. Three approaches are tried, in the following order:

- Retrieve a ComponentOrientation object from the ResourceBundle
using the string "Orientation" as the key.

Use the ResourceBundle.getLocale to determine the bundle's
locale, then return the orientation for that locale.

Return the default locale's orientation.

**Parameters:**
- bdl

- the bundle to use

**Returns:**
- the orientation

---

### Additional Sections

#### Class ComponentOrientation

java.lang.Object

- java.awt.ComponentOrientation

java.awt.ComponentOrientation

**All Implemented Interfaces:** Serializable

```java
public final class
ComponentOrientation

extends
Object

implements
Serializable
```

The ComponentOrientation class encapsulates the language-sensitive
orientation that is to be used to order the elements of a component
or of text. It is used to reflect the differences in this ordering
between Western alphabets, Middle Eastern (such as Hebrew), and Far
Eastern (such as Japanese).

Fundamentally, this governs items (such as characters) which are laid out
in lines, with the lines then laid out in a block. This also applies
to items in a widget: for example, in a check box where the box is
positioned relative to the text.

There are four different orientations used in modern languages
as in the following table.

```java
LT RT TL TR
A B C C B A A D G G D A
D E F F E D B E H H E B
G H I I H G C F I I F C
```

(In the header, the two-letter abbreviation represents the item direction
in the first letter, and the line direction in the second. For example,
LT means "items left-to-right, lines top-to-bottom",
TL means "items top-to-bottom, lines left-to-right", and so on.)

The orientations are:

- LT - Western Europe (optional for Japanese, Chinese, Korean)

RT - Middle East (Arabic, Hebrew)

TR - Japanese, Chinese, Korean

TL - Mongolian

Components whose view and controller code depends on orientation
should use the

isLeftToRight()

and

isHorizontal()

methods to
determine their behavior. They should not include switch-like
code that keys off of the constants, such as:

```java
if (orientation == LEFT_TO_RIGHT) {
...
} else if (orientation == RIGHT_TO_LEFT) {
...
} else {
// Oops
}
```

This is unsafe, since more constants may be added in the future and
since it is not guaranteed that orientation objects will be unique.

**See Also:** Serialized Form

public final class

ComponentOrientation

extends

Object

implements

Serializable

The ComponentOrientation class encapsulates the language-sensitive
orientation that is to be used to order the elements of a component
or of text. It is used to reflect the differences in this ordering
between Western alphabets, Middle Eastern (such as Hebrew), and Far
Eastern (such as Japanese).

Fundamentally, this governs items (such as characters) which are laid out
in lines, with the lines then laid out in a block. This also applies
to items in a widget: for example, in a check box where the box is
positioned relative to the text.

There are four different orientations used in modern languages
as in the following table.

```java
LT RT TL TR
A B C C B A A D G G D A
D E F F E D B E H H E B
G H I I H G C F I I F C
```

(In the header, the two-letter abbreviation represents the item direction
in the first letter, and the line direction in the second. For example,
LT means "items left-to-right, lines top-to-bottom",
TL means "items top-to-bottom, lines left-to-right", and so on.)

The orientations are:

- LT - Western Europe (optional for Japanese, Chinese, Korean)

RT - Middle East (Arabic, Hebrew)

TR - Japanese, Chinese, Korean

TL - Mongolian

Components whose view and controller code depends on orientation
should use the

isLeftToRight()

and

isHorizontal()

methods to
determine their behavior. They should not include switch-like
code that keys off of the constants, such as:

```java
if (orientation == LEFT_TO_RIGHT) {
...
} else if (orientation == RIGHT_TO_LEFT) {
...
} else {
// Oops
}
```

This is unsafe, since more constants may be added in the future and
since it is not guaranteed that orientation objects will be unique.

Fundamentally, this governs items (such as characters) which are laid out
in lines, with the lines then laid out in a block. This also applies
to items in a widget: for example, in a check box where the box is
positioned relative to the text.

There are four different orientations used in modern languages
as in the following table.

```java
LT RT TL TR
A B C C B A A D G G D A
D E F F E D B E H H E B
G H I I H G C F I I F C
```

(In the header, the two-letter abbreviation represents the item direction
in the first letter, and the line direction in the second. For example,
LT means "items left-to-right, lines top-to-bottom",
TL means "items top-to-bottom, lines left-to-right", and so on.)

The orientations are:

- LT - Western Europe (optional for Japanese, Chinese, Korean)

RT - Middle East (Arabic, Hebrew)

TR - Japanese, Chinese, Korean

TL - Mongolian

Components whose view and controller code depends on orientation
should use the

isLeftToRight()

and

isHorizontal()

methods to
determine their behavior. They should not include switch-like
code that keys off of the constants, such as:

```java
if (orientation == LEFT_TO_RIGHT) {
...
} else if (orientation == RIGHT_TO_LEFT) {
...
} else {
// Oops
}
```

This is unsafe, since more constants may be added in the future and
since it is not guaranteed that orientation objects will be unique.

There are four different orientations used in modern languages
as in the following table.

```java
LT RT TL TR
A B C C B A A D G G D A
D E F F E D B E H H E B
G H I I H G C F I I F C
```

(In the header, the two-letter abbreviation represents the item direction
in the first letter, and the line direction in the second. For example,
LT means "items left-to-right, lines top-to-bottom",
TL means "items top-to-bottom, lines left-to-right", and so on.)

The orientations are:

- LT - Western Europe (optional for Japanese, Chinese, Korean)

RT - Middle East (Arabic, Hebrew)

TR - Japanese, Chinese, Korean

TL - Mongolian

Components whose view and controller code depends on orientation
should use the

isLeftToRight()

and

isHorizontal()

methods to
determine their behavior. They should not include switch-like
code that keys off of the constants, such as:

```java
if (orientation == LEFT_TO_RIGHT) {
...
} else if (orientation == RIGHT_TO_LEFT) {
...
} else {
// Oops
}
```

This is unsafe, since more constants may be added in the future and
since it is not guaranteed that orientation objects will be unique.

LT RT TL TR
A B C C B A A D G G D A
D E F F E D B E H H E B
G H I I H G C F I I F C

The orientations are:

- LT - Western Europe (optional for Japanese, Chinese, Korean)

RT - Middle East (Arabic, Hebrew)

TR - Japanese, Chinese, Korean

TL - Mongolian

Components whose view and controller code depends on orientation
should use the

isLeftToRight()

and

isHorizontal()

methods to
determine their behavior. They should not include switch-like
code that keys off of the constants, such as:

```java
if (orientation == LEFT_TO_RIGHT) {
...
} else if (orientation == RIGHT_TO_LEFT) {
...
} else {
// Oops
}
```

This is unsafe, since more constants may be added in the future and
since it is not guaranteed that orientation objects will be unique.

LT - Western Europe (optional for Japanese, Chinese, Korean)

RT - Middle East (Arabic, Hebrew)

TR - Japanese, Chinese, Korean

TL - Mongolian

if (orientation == LEFT_TO_RIGHT) {
...
} else if (orientation == RIGHT_TO_LEFT) {
...
} else {
// Oops
}

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

ComponentOrientation

LEFT_TO_RIGHT

Items run left to right and lines flow top to bottom
Examples: English, French.

static

ComponentOrientation

RIGHT_TO_LEFT

Items run right to left and lines flow top to bottom
Examples: Arabic, Hebrew.

static

ComponentOrientation

UNKNOWN

Indicates that a component's orientation has not been set.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

ComponentOrientation

getOrientation

​(

Locale

locale)

Returns the orientation that is appropriate for the given locale.

static

ComponentOrientation

getOrientation

​(

ResourceBundle

bdl)

Deprecated.

As of J2SE 1.4, use

getOrientation(java.util.Locale)

.

boolean

isHorizontal

()

Are lines horizontal?

boolean

isLeftToRight

()

HorizontalLines: Do items run left-to-right?

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

ComponentOrientation

LEFT_TO_RIGHT

Items run left to right and lines flow top to bottom
Examples: English, French.

static

ComponentOrientation

RIGHT_TO_LEFT

Items run right to left and lines flow top to bottom
Examples: Arabic, Hebrew.

static

ComponentOrientation

UNKNOWN

Indicates that a component's orientation has not been set.

---

#### Field Summary

Items run left to right and lines flow top to bottom
Examples: English, French.

Items run right to left and lines flow top to bottom
Examples: Arabic, Hebrew.

Indicates that a component's orientation has not been set.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

ComponentOrientation

getOrientation

​(

Locale

locale)

Returns the orientation that is appropriate for the given locale.

static

ComponentOrientation

getOrientation

​(

ResourceBundle

bdl)

Deprecated.

As of J2SE 1.4, use

getOrientation(java.util.Locale)

.

boolean

isHorizontal

()

Are lines horizontal?

boolean

isLeftToRight

()

HorizontalLines: Do items run left-to-right?

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

Returns the orientation that is appropriate for the given locale.

Deprecated.

As of J2SE 1.4, use

getOrientation(java.util.Locale)

.

Are lines horizontal?

HorizontalLines: Do items run left-to-right?

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

- LEFT_TO_RIGHT

```java
public static final
ComponentOrientation
LEFT_TO_RIGHT
```

Items run left to right and lines flow top to bottom
Examples: English, French.

- RIGHT_TO_LEFT

```java
public static final
ComponentOrientation
RIGHT_TO_LEFT
```

Items run right to left and lines flow top to bottom
Examples: Arabic, Hebrew.

- UNKNOWN

```java
public static final
ComponentOrientation
UNKNOWN
```

Indicates that a component's orientation has not been set.
To preserve the behavior of existing applications,
isLeftToRight will return true for this value.

============ METHOD DETAIL ==========

- Method Detail

- isHorizontal

```java
public boolean isHorizontal()
```

Are lines horizontal?
This will return true for horizontal, left-to-right writing
systems such as Roman.

**Returns:** true

if this orientation has horizontal lines

- isLeftToRight

```java
public boolean isLeftToRight()
```

HorizontalLines: Do items run left-to-right?

Vertical Lines: Do lines run left-to-right?

This will return true for horizontal, left-to-right writing
systems such as Roman.

**Returns:** true

if this orientation is left-to-right

- getOrientation

```java
public static
ComponentOrientation
getOrientation​(
Locale
locale)
```

Returns the orientation that is appropriate for the given locale.

**Parameters:** locale

- the specified locale
**Returns:** the orientation for the locale

- getOrientation

```java
@Deprecated

public static
ComponentOrientation
getOrientation​(
ResourceBundle
bdl)
```

Deprecated.

As of J2SE 1.4, use

getOrientation(java.util.Locale)

.

Returns the orientation appropriate for the given ResourceBundle's
localization. Three approaches are tried, in the following order:

- Retrieve a ComponentOrientation object from the ResourceBundle
using the string "Orientation" as the key.

Use the ResourceBundle.getLocale to determine the bundle's
locale, then return the orientation for that locale.

Return the default locale's orientation.

**Parameters:** bdl

- the bundle to use
**Returns:** the orientation

Field Detail

- LEFT_TO_RIGHT

```java
public static final
ComponentOrientation
LEFT_TO_RIGHT
```

Items run left to right and lines flow top to bottom
Examples: English, French.

- RIGHT_TO_LEFT

```java
public static final
ComponentOrientation
RIGHT_TO_LEFT
```

Items run right to left and lines flow top to bottom
Examples: Arabic, Hebrew.

- UNKNOWN

```java
public static final
ComponentOrientation
UNKNOWN
```

Indicates that a component's orientation has not been set.
To preserve the behavior of existing applications,
isLeftToRight will return true for this value.

---

#### Field Detail

LEFT_TO_RIGHT

```java
public static final
ComponentOrientation
LEFT_TO_RIGHT
```

Items run left to right and lines flow top to bottom
Examples: English, French.

---

#### LEFT_TO_RIGHT

public static final

ComponentOrientation

LEFT_TO_RIGHT

Items run left to right and lines flow top to bottom
Examples: English, French.

RIGHT_TO_LEFT

```java
public static final
ComponentOrientation
RIGHT_TO_LEFT
```

Items run right to left and lines flow top to bottom
Examples: Arabic, Hebrew.

---

#### RIGHT_TO_LEFT

public static final

ComponentOrientation

RIGHT_TO_LEFT

Items run right to left and lines flow top to bottom
Examples: Arabic, Hebrew.

UNKNOWN

```java
public static final
ComponentOrientation
UNKNOWN
```

Indicates that a component's orientation has not been set.
To preserve the behavior of existing applications,
isLeftToRight will return true for this value.

---

#### UNKNOWN

public static final

ComponentOrientation

UNKNOWN

Indicates that a component's orientation has not been set.
To preserve the behavior of existing applications,
isLeftToRight will return true for this value.

Method Detail

- isHorizontal

```java
public boolean isHorizontal()
```

Are lines horizontal?
This will return true for horizontal, left-to-right writing
systems such as Roman.

**Returns:** true

if this orientation has horizontal lines

- isLeftToRight

```java
public boolean isLeftToRight()
```

HorizontalLines: Do items run left-to-right?

Vertical Lines: Do lines run left-to-right?

This will return true for horizontal, left-to-right writing
systems such as Roman.

**Returns:** true

if this orientation is left-to-right

- getOrientation

```java
public static
ComponentOrientation
getOrientation​(
Locale
locale)
```

Returns the orientation that is appropriate for the given locale.

**Parameters:** locale

- the specified locale
**Returns:** the orientation for the locale

- getOrientation

```java
@Deprecated

public static
ComponentOrientation
getOrientation​(
ResourceBundle
bdl)
```

Deprecated.

As of J2SE 1.4, use

getOrientation(java.util.Locale)

.

Returns the orientation appropriate for the given ResourceBundle's
localization. Three approaches are tried, in the following order:

- Retrieve a ComponentOrientation object from the ResourceBundle
using the string "Orientation" as the key.

Use the ResourceBundle.getLocale to determine the bundle's
locale, then return the orientation for that locale.

Return the default locale's orientation.

**Parameters:** bdl

- the bundle to use
**Returns:** the orientation

---

#### Method Detail

isHorizontal

```java
public boolean isHorizontal()
```

Are lines horizontal?
This will return true for horizontal, left-to-right writing
systems such as Roman.

**Returns:** true

if this orientation has horizontal lines

---

#### isHorizontal

public boolean isHorizontal()

Are lines horizontal?
This will return true for horizontal, left-to-right writing
systems such as Roman.

isLeftToRight

```java
public boolean isLeftToRight()
```

HorizontalLines: Do items run left-to-right?

Vertical Lines: Do lines run left-to-right?

This will return true for horizontal, left-to-right writing
systems such as Roman.

**Returns:** true

if this orientation is left-to-right

---

#### isLeftToRight

public boolean isLeftToRight()

HorizontalLines: Do items run left-to-right?

Vertical Lines: Do lines run left-to-right?

This will return true for horizontal, left-to-right writing
systems such as Roman.

getOrientation

```java
public static
ComponentOrientation
getOrientation​(
Locale
locale)
```

Returns the orientation that is appropriate for the given locale.

**Parameters:** locale

- the specified locale
**Returns:** the orientation for the locale

---

#### getOrientation

public static

ComponentOrientation

getOrientation​(

Locale

locale)

Returns the orientation that is appropriate for the given locale.

getOrientation

```java
@Deprecated

public static
ComponentOrientation
getOrientation​(
ResourceBundle
bdl)
```

Deprecated.

As of J2SE 1.4, use

getOrientation(java.util.Locale)

.

Returns the orientation appropriate for the given ResourceBundle's
localization. Three approaches are tried, in the following order:

- Retrieve a ComponentOrientation object from the ResourceBundle
using the string "Orientation" as the key.

Use the ResourceBundle.getLocale to determine the bundle's
locale, then return the orientation for that locale.

Return the default locale's orientation.

**Parameters:** bdl

- the bundle to use
**Returns:** the orientation

---

#### getOrientation

@Deprecated

public static

ComponentOrientation

getOrientation​(

ResourceBundle

bdl)

Returns the orientation appropriate for the given ResourceBundle's
localization. Three approaches are tried, in the following order:

- Retrieve a ComponentOrientation object from the ResourceBundle
using the string "Orientation" as the key.

Use the ResourceBundle.getLocale to determine the bundle's
locale, then return the orientation for that locale.

Return the default locale's orientation.

Retrieve a ComponentOrientation object from the ResourceBundle
using the string "Orientation" as the key.

Use the ResourceBundle.getLocale to determine the bundle's
locale, then return the orientation for that locale.

Return the default locale's orientation.

---

