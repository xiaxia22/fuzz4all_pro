# Enum GraphicsDevice.WindowTranslucency

**Source:** `java.desktop\java\awt\GraphicsDevice.WindowTranslucency.html`

### Class Description

```java
public static enum
GraphicsDevice.WindowTranslucency

extends
Enum
<
GraphicsDevice.WindowTranslucency
>
```

Kinds of translucency supported by the underlying system.

**All Implemented Interfaces:** Serializable

,

Comparable

<

GraphicsDevice.WindowTranslucency

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
GraphicsDevice.WindowTranslucency
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (GraphicsDevice.WindowTranslucency c : GraphicsDevice.WindowTranslucency.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
GraphicsDevice.WindowTranslucency
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

#### Enum GraphicsDevice.WindowTranslucency

java.lang.Object

- java.lang.Enum

<

GraphicsDevice.WindowTranslucency

>
- - java.awt.GraphicsDevice.WindowTranslucency

java.lang.Enum

<

GraphicsDevice.WindowTranslucency

>

- java.awt.GraphicsDevice.WindowTranslucency

java.awt.GraphicsDevice.WindowTranslucency

**All Implemented Interfaces:** Serializable

,

Comparable

<

GraphicsDevice.WindowTranslucency

>

**Enclosing class:** GraphicsDevice

```java
public static enum
GraphicsDevice.WindowTranslucency

extends
Enum
<
GraphicsDevice.WindowTranslucency
>
```

Kinds of translucency supported by the underlying system.

**Since:** 1.7
**See Also:** GraphicsDevice.isWindowTranslucencySupported(java.awt.GraphicsDevice.WindowTranslucency)

public static enum

GraphicsDevice.WindowTranslucency

extends

Enum

<

GraphicsDevice.WindowTranslucency

>

Kinds of translucency supported by the underlying system.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

PERPIXEL_TRANSLUCENT

Represents support in the underlying system for windows that
contain or might contain pixels with arbitrary alpha values
between and including 0.0 and 1.0.

PERPIXEL_TRANSPARENT

Represents support in the underlying system for windows each pixel
of which is guaranteed to be either completely opaque, with
an alpha value of 1.0, or completely transparent, with an alpha
value of 0.0.

TRANSLUCENT

Represents support in the underlying system for windows all of
the pixels of which have the same alpha value between or including
0.0 and 1.0.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

GraphicsDevice.WindowTranslucency

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

GraphicsDevice.WindowTranslucency

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

PERPIXEL_TRANSLUCENT

Represents support in the underlying system for windows that
contain or might contain pixels with arbitrary alpha values
between and including 0.0 and 1.0.

PERPIXEL_TRANSPARENT

Represents support in the underlying system for windows each pixel
of which is guaranteed to be either completely opaque, with
an alpha value of 1.0, or completely transparent, with an alpha
value of 0.0.

TRANSLUCENT

Represents support in the underlying system for windows all of
the pixels of which have the same alpha value between or including
0.0 and 1.0.

---

#### Enum Constant Summary

Represents support in the underlying system for windows that
contain or might contain pixels with arbitrary alpha values
between and including 0.0 and 1.0.

Represents support in the underlying system for windows each pixel
of which is guaranteed to be either completely opaque, with
an alpha value of 1.0, or completely transparent, with an alpha
value of 0.0.

Represents support in the underlying system for windows all of
the pixels of which have the same alpha value between or including
0.0 and 1.0.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

GraphicsDevice.WindowTranslucency

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

GraphicsDevice.WindowTranslucency

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

- PERPIXEL_TRANSPARENT

```java
public static final
GraphicsDevice.WindowTranslucency
PERPIXEL_TRANSPARENT
```

Represents support in the underlying system for windows each pixel
of which is guaranteed to be either completely opaque, with
an alpha value of 1.0, or completely transparent, with an alpha
value of 0.0.

- TRANSLUCENT

```java
public static final
GraphicsDevice.WindowTranslucency
TRANSLUCENT
```

Represents support in the underlying system for windows all of
the pixels of which have the same alpha value between or including
0.0 and 1.0.

- PERPIXEL_TRANSLUCENT

```java
public static final
GraphicsDevice.WindowTranslucency
PERPIXEL_TRANSLUCENT
```

Represents support in the underlying system for windows that
contain or might contain pixels with arbitrary alpha values
between and including 0.0 and 1.0.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
GraphicsDevice.WindowTranslucency
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (GraphicsDevice.WindowTranslucency c : GraphicsDevice.WindowTranslucency.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
GraphicsDevice.WindowTranslucency
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

- PERPIXEL_TRANSPARENT

```java
public static final
GraphicsDevice.WindowTranslucency
PERPIXEL_TRANSPARENT
```

Represents support in the underlying system for windows each pixel
of which is guaranteed to be either completely opaque, with
an alpha value of 1.0, or completely transparent, with an alpha
value of 0.0.

- TRANSLUCENT

```java
public static final
GraphicsDevice.WindowTranslucency
TRANSLUCENT
```

Represents support in the underlying system for windows all of
the pixels of which have the same alpha value between or including
0.0 and 1.0.

- PERPIXEL_TRANSLUCENT

```java
public static final
GraphicsDevice.WindowTranslucency
PERPIXEL_TRANSLUCENT
```

Represents support in the underlying system for windows that
contain or might contain pixels with arbitrary alpha values
between and including 0.0 and 1.0.

---

#### Enum Constant Detail

PERPIXEL_TRANSPARENT

```java
public static final
GraphicsDevice.WindowTranslucency
PERPIXEL_TRANSPARENT
```

Represents support in the underlying system for windows each pixel
of which is guaranteed to be either completely opaque, with
an alpha value of 1.0, or completely transparent, with an alpha
value of 0.0.

---

#### PERPIXEL_TRANSPARENT

public static final

GraphicsDevice.WindowTranslucency

PERPIXEL_TRANSPARENT

Represents support in the underlying system for windows each pixel
of which is guaranteed to be either completely opaque, with
an alpha value of 1.0, or completely transparent, with an alpha
value of 0.0.

TRANSLUCENT

```java
public static final
GraphicsDevice.WindowTranslucency
TRANSLUCENT
```

Represents support in the underlying system for windows all of
the pixels of which have the same alpha value between or including
0.0 and 1.0.

---

#### TRANSLUCENT

public static final

GraphicsDevice.WindowTranslucency

TRANSLUCENT

Represents support in the underlying system for windows all of
the pixels of which have the same alpha value between or including
0.0 and 1.0.

PERPIXEL_TRANSLUCENT

```java
public static final
GraphicsDevice.WindowTranslucency
PERPIXEL_TRANSLUCENT
```

Represents support in the underlying system for windows that
contain or might contain pixels with arbitrary alpha values
between and including 0.0 and 1.0.

---

#### PERPIXEL_TRANSLUCENT

public static final

GraphicsDevice.WindowTranslucency

PERPIXEL_TRANSLUCENT

Represents support in the underlying system for windows that
contain or might contain pixels with arbitrary alpha values
between and including 0.0 and 1.0.

Method Detail

- values

```java
public static
GraphicsDevice.WindowTranslucency
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (GraphicsDevice.WindowTranslucency c : GraphicsDevice.WindowTranslucency.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
GraphicsDevice.WindowTranslucency
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
GraphicsDevice.WindowTranslucency
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (GraphicsDevice.WindowTranslucency c : GraphicsDevice.WindowTranslucency.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

GraphicsDevice.WindowTranslucency

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (GraphicsDevice.WindowTranslucency c : GraphicsDevice.WindowTranslucency.values())
System.out.println(c);
```

for (GraphicsDevice.WindowTranslucency c : GraphicsDevice.WindowTranslucency.values())
System.out.println(c);

valueOf

```java
public static
GraphicsDevice.WindowTranslucency
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

GraphicsDevice.WindowTranslucency

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

