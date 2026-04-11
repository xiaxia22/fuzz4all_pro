# Enum TextStyle

**Source:** `java.base\java\time\format\TextStyle.html`

### Class Description

```java
public enum
TextStyle

extends
Enum
<
TextStyle
>
```

Enumeration of the style of text formatting and parsing.

Text styles define three sizes for the formatted text - 'full', 'short' and 'narrow'.
Each of these three sizes is available in both 'standard' and 'stand-alone' variations.

The difference between the three sizes is obvious in most languages.
For example, in English the 'full' month is 'January', the 'short' month is 'Jan'
and the 'narrow' month is 'J'. Note that the narrow size is often not unique.
For example, 'January', 'June' and 'July' all have the 'narrow' text 'J'.

The difference between the 'standard' and 'stand-alone' forms is trickier to describe
as there is no difference in English. However, in other languages there is a difference
in the word used when the text is used alone, as opposed to in a complete date.
For example, the word used for a month when used alone in a date picker is different
to the word used for month in association with a day and year in a date.

**All Implemented Interfaces:** Serializable

,

Comparable

<

TextStyle

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
TextStyle
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TextStyle c : TextStyle.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
TextStyle
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

#### public boolean isStandalone()

Returns true if the Style is a stand-alone style.

**Returns:**
- true if the style is a stand-alone style.

---

#### public
TextStyle
asStandalone()

Returns the stand-alone style with the same size.

**Returns:**
- the stand-alone style with the same size

---

#### public
TextStyle
asNormal()

Returns the normal style with the same size.

**Returns:**
- the normal style with the same size

---

### Additional Sections

#### Enum TextStyle

java.lang.Object

- java.lang.Enum

<

TextStyle

>
- - java.time.format.TextStyle

java.lang.Enum

<

TextStyle

>

- java.time.format.TextStyle

java.time.format.TextStyle

**All Implemented Interfaces:** Serializable

,

Comparable

<

TextStyle

>

```java
public enum
TextStyle

extends
Enum
<
TextStyle
>
```

Enumeration of the style of text formatting and parsing.

Text styles define three sizes for the formatted text - 'full', 'short' and 'narrow'.
Each of these three sizes is available in both 'standard' and 'stand-alone' variations.

The difference between the three sizes is obvious in most languages.
For example, in English the 'full' month is 'January', the 'short' month is 'Jan'
and the 'narrow' month is 'J'. Note that the narrow size is often not unique.
For example, 'January', 'June' and 'July' all have the 'narrow' text 'J'.

The difference between the 'standard' and 'stand-alone' forms is trickier to describe
as there is no difference in English. However, in other languages there is a difference
in the word used when the text is used alone, as opposed to in a complete date.
For example, the word used for a month when used alone in a date picker is different
to the word used for month in association with a day and year in a date.

**Implementation Requirements:** This is immutable and thread-safe enum.
**Since:** 1.8

public enum

TextStyle

extends

Enum

<

TextStyle

>

Enumeration of the style of text formatting and parsing.

Text styles define three sizes for the formatted text - 'full', 'short' and 'narrow'.
Each of these three sizes is available in both 'standard' and 'stand-alone' variations.

The difference between the three sizes is obvious in most languages.
For example, in English the 'full' month is 'January', the 'short' month is 'Jan'
and the 'narrow' month is 'J'. Note that the narrow size is often not unique.
For example, 'January', 'June' and 'July' all have the 'narrow' text 'J'.

The difference between the 'standard' and 'stand-alone' forms is trickier to describe
as there is no difference in English. However, in other languages there is a difference
in the word used when the text is used alone, as opposed to in a complete date.
For example, the word used for a month when used alone in a date picker is different
to the word used for month in association with a day and year in a date.

Text styles define three sizes for the formatted text - 'full', 'short' and 'narrow'.
Each of these three sizes is available in both 'standard' and 'stand-alone' variations.

The difference between the three sizes is obvious in most languages.
For example, in English the 'full' month is 'January', the 'short' month is 'Jan'
and the 'narrow' month is 'J'. Note that the narrow size is often not unique.
For example, 'January', 'June' and 'July' all have the 'narrow' text 'J'.

The difference between the 'standard' and 'stand-alone' forms is trickier to describe
as there is no difference in English. However, in other languages there is a difference
in the word used when the text is used alone, as opposed to in a complete date.
For example, the word used for a month when used alone in a date picker is different
to the word used for month in association with a day and year in a date.

The difference between the three sizes is obvious in most languages.
For example, in English the 'full' month is 'January', the 'short' month is 'Jan'
and the 'narrow' month is 'J'. Note that the narrow size is often not unique.
For example, 'January', 'June' and 'July' all have the 'narrow' text 'J'.

The difference between the 'standard' and 'stand-alone' forms is trickier to describe
as there is no difference in English. However, in other languages there is a difference
in the word used when the text is used alone, as opposed to in a complete date.
For example, the word used for a month when used alone in a date picker is different
to the word used for month in association with a day and year in a date.

The difference between the 'standard' and 'stand-alone' forms is trickier to describe
as there is no difference in English. However, in other languages there is a difference
in the word used when the text is used alone, as opposed to in a complete date.
For example, the word used for a month when used alone in a date picker is different
to the word used for month in association with a day and year in a date.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

FULL

Full text, typically the full description.

FULL_STANDALONE

Full text for stand-alone use, typically the full description.

NARROW

Narrow text, typically a single letter.

NARROW_STANDALONE

Narrow text for stand-alone use, typically a single letter.

SHORT

Short text, typically an abbreviation.

SHORT_STANDALONE

Short text for stand-alone use, typically an abbreviation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

TextStyle

asNormal

()

Returns the normal style with the same size.

TextStyle

asStandalone

()

Returns the stand-alone style with the same size.

boolean

isStandalone

()

Returns true if the Style is a stand-alone style.

static

TextStyle

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

TextStyle

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

FULL

Full text, typically the full description.

FULL_STANDALONE

Full text for stand-alone use, typically the full description.

NARROW

Narrow text, typically a single letter.

NARROW_STANDALONE

Narrow text for stand-alone use, typically a single letter.

SHORT

Short text, typically an abbreviation.

SHORT_STANDALONE

Short text for stand-alone use, typically an abbreviation.

---

#### Enum Constant Summary

Full text, typically the full description.

Full text for stand-alone use, typically the full description.

Narrow text, typically a single letter.

Narrow text for stand-alone use, typically a single letter.

Short text, typically an abbreviation.

Short text for stand-alone use, typically an abbreviation.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

TextStyle

asNormal

()

Returns the normal style with the same size.

TextStyle

asStandalone

()

Returns the stand-alone style with the same size.

boolean

isStandalone

()

Returns true if the Style is a stand-alone style.

static

TextStyle

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

TextStyle

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

Returns the normal style with the same size.

Returns the stand-alone style with the same size.

Returns true if the Style is a stand-alone style.

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

- FULL

```java
public static final
TextStyle
FULL
```

Full text, typically the full description.
For example, day-of-week Monday might output "Monday".

- FULL_STANDALONE

```java
public static final
TextStyle
FULL_STANDALONE
```

Full text for stand-alone use, typically the full description.
For example, day-of-week Monday might output "Monday".

- SHORT

```java
public static final
TextStyle
SHORT
```

Short text, typically an abbreviation.
For example, day-of-week Monday might output "Mon".

- SHORT_STANDALONE

```java
public static final
TextStyle
SHORT_STANDALONE
```

Short text for stand-alone use, typically an abbreviation.
For example, day-of-week Monday might output "Mon".

- NARROW

```java
public static final
TextStyle
NARROW
```

Narrow text, typically a single letter.
For example, day-of-week Monday might output "M".

- NARROW_STANDALONE

```java
public static final
TextStyle
NARROW_STANDALONE
```

Narrow text for stand-alone use, typically a single letter.
For example, day-of-week Monday might output "M".

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
TextStyle
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TextStyle c : TextStyle.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
TextStyle
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

- isStandalone

```java
public boolean isStandalone()
```

Returns true if the Style is a stand-alone style.

**Returns:** true if the style is a stand-alone style.

- asStandalone

```java
public
TextStyle
asStandalone()
```

Returns the stand-alone style with the same size.

**Returns:** the stand-alone style with the same size

- asNormal

```java
public
TextStyle
asNormal()
```

Returns the normal style with the same size.

**Returns:** the normal style with the same size

Enum Constant Detail

- FULL

```java
public static final
TextStyle
FULL
```

Full text, typically the full description.
For example, day-of-week Monday might output "Monday".

- FULL_STANDALONE

```java
public static final
TextStyle
FULL_STANDALONE
```

Full text for stand-alone use, typically the full description.
For example, day-of-week Monday might output "Monday".

- SHORT

```java
public static final
TextStyle
SHORT
```

Short text, typically an abbreviation.
For example, day-of-week Monday might output "Mon".

- SHORT_STANDALONE

```java
public static final
TextStyle
SHORT_STANDALONE
```

Short text for stand-alone use, typically an abbreviation.
For example, day-of-week Monday might output "Mon".

- NARROW

```java
public static final
TextStyle
NARROW
```

Narrow text, typically a single letter.
For example, day-of-week Monday might output "M".

- NARROW_STANDALONE

```java
public static final
TextStyle
NARROW_STANDALONE
```

Narrow text for stand-alone use, typically a single letter.
For example, day-of-week Monday might output "M".

---

#### Enum Constant Detail

FULL

```java
public static final
TextStyle
FULL
```

Full text, typically the full description.
For example, day-of-week Monday might output "Monday".

---

#### FULL

public static final

TextStyle

FULL

Full text, typically the full description.
For example, day-of-week Monday might output "Monday".

FULL_STANDALONE

```java
public static final
TextStyle
FULL_STANDALONE
```

Full text for stand-alone use, typically the full description.
For example, day-of-week Monday might output "Monday".

---

#### FULL_STANDALONE

public static final

TextStyle

FULL_STANDALONE

Full text for stand-alone use, typically the full description.
For example, day-of-week Monday might output "Monday".

SHORT

```java
public static final
TextStyle
SHORT
```

Short text, typically an abbreviation.
For example, day-of-week Monday might output "Mon".

---

#### SHORT

public static final

TextStyle

SHORT

Short text, typically an abbreviation.
For example, day-of-week Monday might output "Mon".

SHORT_STANDALONE

```java
public static final
TextStyle
SHORT_STANDALONE
```

Short text for stand-alone use, typically an abbreviation.
For example, day-of-week Monday might output "Mon".

---

#### SHORT_STANDALONE

public static final

TextStyle

SHORT_STANDALONE

Short text for stand-alone use, typically an abbreviation.
For example, day-of-week Monday might output "Mon".

NARROW

```java
public static final
TextStyle
NARROW
```

Narrow text, typically a single letter.
For example, day-of-week Monday might output "M".

---

#### NARROW

public static final

TextStyle

NARROW

Narrow text, typically a single letter.
For example, day-of-week Monday might output "M".

NARROW_STANDALONE

```java
public static final
TextStyle
NARROW_STANDALONE
```

Narrow text for stand-alone use, typically a single letter.
For example, day-of-week Monday might output "M".

---

#### NARROW_STANDALONE

public static final

TextStyle

NARROW_STANDALONE

Narrow text for stand-alone use, typically a single letter.
For example, day-of-week Monday might output "M".

Method Detail

- values

```java
public static
TextStyle
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TextStyle c : TextStyle.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
TextStyle
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

- isStandalone

```java
public boolean isStandalone()
```

Returns true if the Style is a stand-alone style.

**Returns:** true if the style is a stand-alone style.

- asStandalone

```java
public
TextStyle
asStandalone()
```

Returns the stand-alone style with the same size.

**Returns:** the stand-alone style with the same size

- asNormal

```java
public
TextStyle
asNormal()
```

Returns the normal style with the same size.

**Returns:** the normal style with the same size

---

#### Method Detail

values

```java
public static
TextStyle
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TextStyle c : TextStyle.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

TextStyle

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TextStyle c : TextStyle.values())
System.out.println(c);
```

for (TextStyle c : TextStyle.values())
System.out.println(c);

valueOf

```java
public static
TextStyle
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

TextStyle

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

isStandalone

```java
public boolean isStandalone()
```

Returns true if the Style is a stand-alone style.

**Returns:** true if the style is a stand-alone style.

---

#### isStandalone

public boolean isStandalone()

Returns true if the Style is a stand-alone style.

asStandalone

```java
public
TextStyle
asStandalone()
```

Returns the stand-alone style with the same size.

**Returns:** the stand-alone style with the same size

---

#### asStandalone

public

TextStyle

asStandalone()

Returns the stand-alone style with the same size.

asNormal

```java
public
TextStyle
asNormal()
```

Returns the normal style with the same size.

**Returns:** the normal style with the same size

---

#### asNormal

public

TextStyle

asNormal()

Returns the normal style with the same size.

---

