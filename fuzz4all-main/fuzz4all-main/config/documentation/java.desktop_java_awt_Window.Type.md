# Enum Window.Type

**Source:** `java.desktop\java\awt\Window.Type.html`

### Class Description

```java
public static enum
Window.Type

extends
Enum
<
Window.Type
>
```

Enumeration of available

window types

.

A window type defines the generic visual appearance and behavior of a
top-level window. For example, the type may affect the kind of
decorations of a decorated

Frame

or

Dialog

instance.

Some platforms may not fully support a certain window type. Depending on
the level of support, some properties of the window type may be
disobeyed.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Window.Type

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Window.Type
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Window.Type c : Window.Type.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Window.Type
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

#### Enum Window.Type

java.lang.Object

- java.lang.Enum

<

Window.Type

>
- - java.awt.Window.Type

java.lang.Enum

<

Window.Type

>

- java.awt.Window.Type

java.awt.Window.Type

**All Implemented Interfaces:** Serializable

,

Comparable

<

Window.Type

>

**Enclosing class:** Window

```java
public static enum
Window.Type

extends
Enum
<
Window.Type
>
```

Enumeration of available

window types

.

A window type defines the generic visual appearance and behavior of a
top-level window. For example, the type may affect the kind of
decorations of a decorated

Frame

or

Dialog

instance.

Some platforms may not fully support a certain window type. Depending on
the level of support, some properties of the window type may be
disobeyed.

**Since:** 1.7
**See Also:** Window.getType()

,

Window.setType(java.awt.Window.Type)

public static enum

Window.Type

extends

Enum

<

Window.Type

>

Enumeration of available

window types

.

A window type defines the generic visual appearance and behavior of a
top-level window. For example, the type may affect the kind of
decorations of a decorated

Frame

or

Dialog

instance.

Some platforms may not fully support a certain window type. Depending on
the level of support, some properties of the window type may be
disobeyed.

Some platforms may not fully support a certain window type. Depending on
the level of support, some properties of the window type may be
disobeyed.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

NORMAL

Represents a

normal

window.

POPUP

Represents a

popup

window.

UTILITY

Represents a

utility

window.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Window.Type

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Window.Type

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

NORMAL

Represents a

normal

window.

POPUP

Represents a

popup

window.

UTILITY

Represents a

utility

window.

---

#### Enum Constant Summary

Represents a

normal

window.

Represents a

popup

window.

Represents a

utility

window.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Window.Type

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Window.Type

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

- NORMAL

```java
public static final
Window.Type
NORMAL
```

Represents a

normal

window.

This is the default type for objects of the

Window

class or
its descendants. Use this type for regular top-level windows.

- UTILITY

```java
public static final
Window.Type
UTILITY
```

Represents a

utility

window.

A utility window is usually a small window such as a toolbar or a
palette. The native system may render the window with smaller
title-bar if the window is either a

Frame

or a

Dialog

object, and if it has its decorations enabled.

- POPUP

```java
public static final
Window.Type
POPUP
```

Represents a

popup

window.

A popup window is a temporary window such as a drop-down menu or a
tooltip. On some platforms, windows of that type may be forcibly
made undecorated even if they are instances of the

Frame

or

Dialog

class, and have decorations enabled.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Window.Type
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Window.Type c : Window.Type.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Window.Type
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

- NORMAL

```java
public static final
Window.Type
NORMAL
```

Represents a

normal

window.

This is the default type for objects of the

Window

class or
its descendants. Use this type for regular top-level windows.

- UTILITY

```java
public static final
Window.Type
UTILITY
```

Represents a

utility

window.

A utility window is usually a small window such as a toolbar or a
palette. The native system may render the window with smaller
title-bar if the window is either a

Frame

or a

Dialog

object, and if it has its decorations enabled.

- POPUP

```java
public static final
Window.Type
POPUP
```

Represents a

popup

window.

A popup window is a temporary window such as a drop-down menu or a
tooltip. On some platforms, windows of that type may be forcibly
made undecorated even if they are instances of the

Frame

or

Dialog

class, and have decorations enabled.

---

#### Enum Constant Detail

NORMAL

```java
public static final
Window.Type
NORMAL
```

Represents a

normal

window.

This is the default type for objects of the

Window

class or
its descendants. Use this type for regular top-level windows.

---

#### NORMAL

public static final

Window.Type

NORMAL

Represents a

normal

window.

This is the default type for objects of the

Window

class or
its descendants. Use this type for regular top-level windows.

UTILITY

```java
public static final
Window.Type
UTILITY
```

Represents a

utility

window.

A utility window is usually a small window such as a toolbar or a
palette. The native system may render the window with smaller
title-bar if the window is either a

Frame

or a

Dialog

object, and if it has its decorations enabled.

---

#### UTILITY

public static final

Window.Type

UTILITY

Represents a

utility

window.

A utility window is usually a small window such as a toolbar or a
palette. The native system may render the window with smaller
title-bar if the window is either a

Frame

or a

Dialog

object, and if it has its decorations enabled.

POPUP

```java
public static final
Window.Type
POPUP
```

Represents a

popup

window.

A popup window is a temporary window such as a drop-down menu or a
tooltip. On some platforms, windows of that type may be forcibly
made undecorated even if they are instances of the

Frame

or

Dialog

class, and have decorations enabled.

---

#### POPUP

public static final

Window.Type

POPUP

Represents a

popup

window.

A popup window is a temporary window such as a drop-down menu or a
tooltip. On some platforms, windows of that type may be forcibly
made undecorated even if they are instances of the

Frame

or

Dialog

class, and have decorations enabled.

Method Detail

- values

```java
public static
Window.Type
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Window.Type c : Window.Type.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Window.Type
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
Window.Type
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Window.Type c : Window.Type.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Window.Type

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Window.Type c : Window.Type.values())
System.out.println(c);
```

for (Window.Type c : Window.Type.values())
System.out.println(c);

valueOf

```java
public static
Window.Type
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

Window.Type

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

