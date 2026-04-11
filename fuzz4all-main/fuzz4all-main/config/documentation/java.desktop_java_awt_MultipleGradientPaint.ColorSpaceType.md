# Enum MultipleGradientPaint.ColorSpaceType

**Source:** `java.desktop\java\awt\MultipleGradientPaint.ColorSpaceType.html`

### Class Description

```java
public static enum
MultipleGradientPaint.ColorSpaceType

extends
Enum
<
MultipleGradientPaint.ColorSpaceType
>
```

The color space in which to perform the gradient interpolation.

**All Implemented Interfaces:** Serializable

,

Comparable

<

MultipleGradientPaint.ColorSpaceType

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
MultipleGradientPaint.ColorSpaceType
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MultipleGradientPaint.ColorSpaceType c : MultipleGradientPaint.ColorSpaceType.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
MultipleGradientPaint.ColorSpaceType
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

#### Enum MultipleGradientPaint.ColorSpaceType

java.lang.Object

- java.lang.Enum

<

MultipleGradientPaint.ColorSpaceType

>
- - java.awt.MultipleGradientPaint.ColorSpaceType

java.lang.Enum

<

MultipleGradientPaint.ColorSpaceType

>

- java.awt.MultipleGradientPaint.ColorSpaceType

java.awt.MultipleGradientPaint.ColorSpaceType

**All Implemented Interfaces:** Serializable

,

Comparable

<

MultipleGradientPaint.ColorSpaceType

>

**Enclosing class:** MultipleGradientPaint

```java
public static enum
MultipleGradientPaint.ColorSpaceType

extends
Enum
<
MultipleGradientPaint.ColorSpaceType
>
```

The color space in which to perform the gradient interpolation.

**Since:** 1.6

public static enum

MultipleGradientPaint.ColorSpaceType

extends

Enum

<

MultipleGradientPaint.ColorSpaceType

>

The color space in which to perform the gradient interpolation.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

LINEAR_RGB

Indicates that the color interpolation should occur in linearized
RGB space.

SRGB

Indicates that the color interpolation should occur in sRGB space.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

MultipleGradientPaint.ColorSpaceType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

MultipleGradientPaint.ColorSpaceType

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

LINEAR_RGB

Indicates that the color interpolation should occur in linearized
RGB space.

SRGB

Indicates that the color interpolation should occur in sRGB space.

---

#### Enum Constant Summary

Indicates that the color interpolation should occur in linearized
RGB space.

Indicates that the color interpolation should occur in sRGB space.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

MultipleGradientPaint.ColorSpaceType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

MultipleGradientPaint.ColorSpaceType

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

- SRGB

```java
public static final
MultipleGradientPaint.ColorSpaceType
SRGB
```

Indicates that the color interpolation should occur in sRGB space.

- LINEAR_RGB

```java
public static final
MultipleGradientPaint.ColorSpaceType
LINEAR_RGB
```

Indicates that the color interpolation should occur in linearized
RGB space.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
MultipleGradientPaint.ColorSpaceType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MultipleGradientPaint.ColorSpaceType c : MultipleGradientPaint.ColorSpaceType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
MultipleGradientPaint.ColorSpaceType
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

- SRGB

```java
public static final
MultipleGradientPaint.ColorSpaceType
SRGB
```

Indicates that the color interpolation should occur in sRGB space.

- LINEAR_RGB

```java
public static final
MultipleGradientPaint.ColorSpaceType
LINEAR_RGB
```

Indicates that the color interpolation should occur in linearized
RGB space.

---

#### Enum Constant Detail

SRGB

```java
public static final
MultipleGradientPaint.ColorSpaceType
SRGB
```

Indicates that the color interpolation should occur in sRGB space.

---

#### SRGB

public static final

MultipleGradientPaint.ColorSpaceType

SRGB

Indicates that the color interpolation should occur in sRGB space.

LINEAR_RGB

```java
public static final
MultipleGradientPaint.ColorSpaceType
LINEAR_RGB
```

Indicates that the color interpolation should occur in linearized
RGB space.

---

#### LINEAR_RGB

public static final

MultipleGradientPaint.ColorSpaceType

LINEAR_RGB

Indicates that the color interpolation should occur in linearized
RGB space.

Method Detail

- values

```java
public static
MultipleGradientPaint.ColorSpaceType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MultipleGradientPaint.ColorSpaceType c : MultipleGradientPaint.ColorSpaceType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
MultipleGradientPaint.ColorSpaceType
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
MultipleGradientPaint.ColorSpaceType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MultipleGradientPaint.ColorSpaceType c : MultipleGradientPaint.ColorSpaceType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

MultipleGradientPaint.ColorSpaceType

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (MultipleGradientPaint.ColorSpaceType c : MultipleGradientPaint.ColorSpaceType.values())
System.out.println(c);
```

for (MultipleGradientPaint.ColorSpaceType c : MultipleGradientPaint.ColorSpaceType.values())
System.out.println(c);

valueOf

```java
public static
MultipleGradientPaint.ColorSpaceType
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

MultipleGradientPaint.ColorSpaceType

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

