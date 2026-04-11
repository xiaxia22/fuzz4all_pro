# Enum Taskbar.State

**Source:** `java.desktop\java\awt\Taskbar.State.html`

### Class Description

```java
public static enum
Taskbar.State

extends
Enum
<
Taskbar.State
>
```

Kinds of available window progress states.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Taskbar.State

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Taskbar.State
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Taskbar.State c : Taskbar.State.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Taskbar.State
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

#### Enum Taskbar.State

java.lang.Object

- java.lang.Enum

<

Taskbar.State

>
- - java.awt.Taskbar.State

java.lang.Enum

<

Taskbar.State

>

- java.awt.Taskbar.State

java.awt.Taskbar.State

**All Implemented Interfaces:** Serializable

,

Comparable

<

Taskbar.State

>

**Enclosing class:** Taskbar

```java
public static enum
Taskbar.State

extends
Enum
<
Taskbar.State
>
```

Kinds of available window progress states.

**See Also:** Taskbar.setWindowProgressState(java.awt.Window, java.awt.Taskbar.State)

public static enum

Taskbar.State

extends

Enum

<

Taskbar.State

>

Kinds of available window progress states.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ERROR

Shows that an error has occurred.

INDETERMINATE

The progress indicator displays activity without specifying what
proportion of the progress is complete.

NORMAL

The progress indicator displays with normal color and determinate
mode.

OFF

Stops displaying the progress.

PAUSED

Shows progress as paused, progress can be resumed by the user.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Taskbar.State

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Taskbar.State

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

ERROR

Shows that an error has occurred.

INDETERMINATE

The progress indicator displays activity without specifying what
proportion of the progress is complete.

NORMAL

The progress indicator displays with normal color and determinate
mode.

OFF

Stops displaying the progress.

PAUSED

Shows progress as paused, progress can be resumed by the user.

---

#### Enum Constant Summary

Shows that an error has occurred.

The progress indicator displays activity without specifying what
proportion of the progress is complete.

The progress indicator displays with normal color and determinate
mode.

Stops displaying the progress.

Shows progress as paused, progress can be resumed by the user.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Taskbar.State

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Taskbar.State

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

- OFF

```java
public static final
Taskbar.State
OFF
```

Stops displaying the progress.

- NORMAL

```java
public static final
Taskbar.State
NORMAL
```

The progress indicator displays with normal color and determinate
mode.

- PAUSED

```java
public static final
Taskbar.State
PAUSED
```

Shows progress as paused, progress can be resumed by the user.
Switches to the determinate display.

- INDETERMINATE

```java
public static final
Taskbar.State
INDETERMINATE
```

The progress indicator displays activity without specifying what
proportion of the progress is complete.

- ERROR

```java
public static final
Taskbar.State
ERROR
```

Shows that an error has occurred. Switches to the determinate
display.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Taskbar.State
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Taskbar.State c : Taskbar.State.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Taskbar.State
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

- OFF

```java
public static final
Taskbar.State
OFF
```

Stops displaying the progress.

- NORMAL

```java
public static final
Taskbar.State
NORMAL
```

The progress indicator displays with normal color and determinate
mode.

- PAUSED

```java
public static final
Taskbar.State
PAUSED
```

Shows progress as paused, progress can be resumed by the user.
Switches to the determinate display.

- INDETERMINATE

```java
public static final
Taskbar.State
INDETERMINATE
```

The progress indicator displays activity without specifying what
proportion of the progress is complete.

- ERROR

```java
public static final
Taskbar.State
ERROR
```

Shows that an error has occurred. Switches to the determinate
display.

---

#### Enum Constant Detail

OFF

```java
public static final
Taskbar.State
OFF
```

Stops displaying the progress.

---

#### OFF

public static final

Taskbar.State

OFF

Stops displaying the progress.

NORMAL

```java
public static final
Taskbar.State
NORMAL
```

The progress indicator displays with normal color and determinate
mode.

---

#### NORMAL

public static final

Taskbar.State

NORMAL

The progress indicator displays with normal color and determinate
mode.

PAUSED

```java
public static final
Taskbar.State
PAUSED
```

Shows progress as paused, progress can be resumed by the user.
Switches to the determinate display.

---

#### PAUSED

public static final

Taskbar.State

PAUSED

Shows progress as paused, progress can be resumed by the user.
Switches to the determinate display.

INDETERMINATE

```java
public static final
Taskbar.State
INDETERMINATE
```

The progress indicator displays activity without specifying what
proportion of the progress is complete.

---

#### INDETERMINATE

public static final

Taskbar.State

INDETERMINATE

The progress indicator displays activity without specifying what
proportion of the progress is complete.

ERROR

```java
public static final
Taskbar.State
ERROR
```

Shows that an error has occurred. Switches to the determinate
display.

---

#### ERROR

public static final

Taskbar.State

ERROR

Shows that an error has occurred. Switches to the determinate
display.

Method Detail

- values

```java
public static
Taskbar.State
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Taskbar.State c : Taskbar.State.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Taskbar.State
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
Taskbar.State
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Taskbar.State c : Taskbar.State.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Taskbar.State

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Taskbar.State c : Taskbar.State.values())
System.out.println(c);
```

for (Taskbar.State c : Taskbar.State.values())
System.out.println(c);

valueOf

```java
public static
Taskbar.State
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

Taskbar.State

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

