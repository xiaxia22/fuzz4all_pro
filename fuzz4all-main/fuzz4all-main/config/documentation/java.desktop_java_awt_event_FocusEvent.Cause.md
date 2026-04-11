# Enum FocusEvent.Cause

**Source:** `java.desktop\java\awt\event\FocusEvent.Cause.html`

### Class Description

```java
public static enum
FocusEvent.Cause

extends
Enum
<
FocusEvent.Cause
>
```

This enum represents the cause of a

FocusEvent

- the reason why it
occurred. Possible reasons include mouse events, keyboard focus
traversal, window activation.
If no cause is provided then the reason is

UNKNOWN

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

FocusEvent.Cause

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
FocusEvent.Cause
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FocusEvent.Cause c : FocusEvent.Cause.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
FocusEvent.Cause
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

#### Enum FocusEvent.Cause

java.lang.Object

- java.lang.Enum

<

FocusEvent.Cause

>
- - java.awt.event.FocusEvent.Cause

java.lang.Enum

<

FocusEvent.Cause

>

- java.awt.event.FocusEvent.Cause

java.awt.event.FocusEvent.Cause

**All Implemented Interfaces:** Serializable

,

Comparable

<

FocusEvent.Cause

>

**Enclosing class:** FocusEvent

```java
public static enum
FocusEvent.Cause

extends
Enum
<
FocusEvent.Cause
>
```

This enum represents the cause of a

FocusEvent

- the reason why it
occurred. Possible reasons include mouse events, keyboard focus
traversal, window activation.
If no cause is provided then the reason is

UNKNOWN

.

**Since:** 9

public static enum

FocusEvent.Cause

extends

Enum

<

FocusEvent.Cause

>

This enum represents the cause of a

FocusEvent

- the reason why it
occurred. Possible reasons include mouse events, keyboard focus
traversal, window activation.
If no cause is provided then the reason is

UNKNOWN

.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ACTIVATION

An activation of a toplevel window.

CLEAR_GLOBAL_FOCUS_OWNER

Clearing global focus owner.

MOUSE_EVENT

An activating mouse event.

ROLLBACK

Restoring focus after a focus request has been rejected.

TRAVERSAL

A focus traversal action with unspecified direction.

TRAVERSAL_BACKWARD

A backward focus traversal action.

TRAVERSAL_DOWN

A down-cycle focus traversal action.

TRAVERSAL_FORWARD

A forward focus traversal action.

TRAVERSAL_UP

An up-cycle focus traversal action.

UNEXPECTED

A system action causing an unexpected focus change.

UNKNOWN

The default value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

FocusEvent.Cause

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

FocusEvent.Cause

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

ACTIVATION

An activation of a toplevel window.

CLEAR_GLOBAL_FOCUS_OWNER

Clearing global focus owner.

MOUSE_EVENT

An activating mouse event.

ROLLBACK

Restoring focus after a focus request has been rejected.

TRAVERSAL

A focus traversal action with unspecified direction.

TRAVERSAL_BACKWARD

A backward focus traversal action.

TRAVERSAL_DOWN

A down-cycle focus traversal action.

TRAVERSAL_FORWARD

A forward focus traversal action.

TRAVERSAL_UP

An up-cycle focus traversal action.

UNEXPECTED

A system action causing an unexpected focus change.

UNKNOWN

The default value.

---

#### Enum Constant Summary

An activation of a toplevel window.

Clearing global focus owner.

An activating mouse event.

Restoring focus after a focus request has been rejected.

A focus traversal action with unspecified direction.

A backward focus traversal action.

A down-cycle focus traversal action.

A forward focus traversal action.

An up-cycle focus traversal action.

A system action causing an unexpected focus change.

The default value.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

FocusEvent.Cause

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

FocusEvent.Cause

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

- UNKNOWN

```java
public static final
FocusEvent.Cause
UNKNOWN
```

The default value.

- MOUSE_EVENT

```java
public static final
FocusEvent.Cause
MOUSE_EVENT
```

An activating mouse event.

- TRAVERSAL

```java
public static final
FocusEvent.Cause
TRAVERSAL
```

A focus traversal action with unspecified direction.

- TRAVERSAL_UP

```java
public static final
FocusEvent.Cause
TRAVERSAL_UP
```

An up-cycle focus traversal action.

- TRAVERSAL_DOWN

```java
public static final
FocusEvent.Cause
TRAVERSAL_DOWN
```

A down-cycle focus traversal action.

- TRAVERSAL_FORWARD

```java
public static final
FocusEvent.Cause
TRAVERSAL_FORWARD
```

A forward focus traversal action.

- TRAVERSAL_BACKWARD

```java
public static final
FocusEvent.Cause
TRAVERSAL_BACKWARD
```

A backward focus traversal action.

- ROLLBACK

```java
public static final
FocusEvent.Cause
ROLLBACK
```

Restoring focus after a focus request has been rejected.

- UNEXPECTED

```java
public static final
FocusEvent.Cause
UNEXPECTED
```

A system action causing an unexpected focus change.

- ACTIVATION

```java
public static final
FocusEvent.Cause
ACTIVATION
```

An activation of a toplevel window.

- CLEAR_GLOBAL_FOCUS_OWNER

```java
public static final
FocusEvent.Cause
CLEAR_GLOBAL_FOCUS_OWNER
```

Clearing global focus owner.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
FocusEvent.Cause
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FocusEvent.Cause c : FocusEvent.Cause.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
FocusEvent.Cause
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

- UNKNOWN

```java
public static final
FocusEvent.Cause
UNKNOWN
```

The default value.

- MOUSE_EVENT

```java
public static final
FocusEvent.Cause
MOUSE_EVENT
```

An activating mouse event.

- TRAVERSAL

```java
public static final
FocusEvent.Cause
TRAVERSAL
```

A focus traversal action with unspecified direction.

- TRAVERSAL_UP

```java
public static final
FocusEvent.Cause
TRAVERSAL_UP
```

An up-cycle focus traversal action.

- TRAVERSAL_DOWN

```java
public static final
FocusEvent.Cause
TRAVERSAL_DOWN
```

A down-cycle focus traversal action.

- TRAVERSAL_FORWARD

```java
public static final
FocusEvent.Cause
TRAVERSAL_FORWARD
```

A forward focus traversal action.

- TRAVERSAL_BACKWARD

```java
public static final
FocusEvent.Cause
TRAVERSAL_BACKWARD
```

A backward focus traversal action.

- ROLLBACK

```java
public static final
FocusEvent.Cause
ROLLBACK
```

Restoring focus after a focus request has been rejected.

- UNEXPECTED

```java
public static final
FocusEvent.Cause
UNEXPECTED
```

A system action causing an unexpected focus change.

- ACTIVATION

```java
public static final
FocusEvent.Cause
ACTIVATION
```

An activation of a toplevel window.

- CLEAR_GLOBAL_FOCUS_OWNER

```java
public static final
FocusEvent.Cause
CLEAR_GLOBAL_FOCUS_OWNER
```

Clearing global focus owner.

---

#### Enum Constant Detail

UNKNOWN

```java
public static final
FocusEvent.Cause
UNKNOWN
```

The default value.

---

#### UNKNOWN

public static final

FocusEvent.Cause

UNKNOWN

The default value.

MOUSE_EVENT

```java
public static final
FocusEvent.Cause
MOUSE_EVENT
```

An activating mouse event.

---

#### MOUSE_EVENT

public static final

FocusEvent.Cause

MOUSE_EVENT

An activating mouse event.

TRAVERSAL

```java
public static final
FocusEvent.Cause
TRAVERSAL
```

A focus traversal action with unspecified direction.

---

#### TRAVERSAL

public static final

FocusEvent.Cause

TRAVERSAL

A focus traversal action with unspecified direction.

TRAVERSAL_UP

```java
public static final
FocusEvent.Cause
TRAVERSAL_UP
```

An up-cycle focus traversal action.

---

#### TRAVERSAL_UP

public static final

FocusEvent.Cause

TRAVERSAL_UP

An up-cycle focus traversal action.

TRAVERSAL_DOWN

```java
public static final
FocusEvent.Cause
TRAVERSAL_DOWN
```

A down-cycle focus traversal action.

---

#### TRAVERSAL_DOWN

public static final

FocusEvent.Cause

TRAVERSAL_DOWN

A down-cycle focus traversal action.

TRAVERSAL_FORWARD

```java
public static final
FocusEvent.Cause
TRAVERSAL_FORWARD
```

A forward focus traversal action.

---

#### TRAVERSAL_FORWARD

public static final

FocusEvent.Cause

TRAVERSAL_FORWARD

A forward focus traversal action.

TRAVERSAL_BACKWARD

```java
public static final
FocusEvent.Cause
TRAVERSAL_BACKWARD
```

A backward focus traversal action.

---

#### TRAVERSAL_BACKWARD

public static final

FocusEvent.Cause

TRAVERSAL_BACKWARD

A backward focus traversal action.

ROLLBACK

```java
public static final
FocusEvent.Cause
ROLLBACK
```

Restoring focus after a focus request has been rejected.

---

#### ROLLBACK

public static final

FocusEvent.Cause

ROLLBACK

Restoring focus after a focus request has been rejected.

UNEXPECTED

```java
public static final
FocusEvent.Cause
UNEXPECTED
```

A system action causing an unexpected focus change.

---

#### UNEXPECTED

public static final

FocusEvent.Cause

UNEXPECTED

A system action causing an unexpected focus change.

ACTIVATION

```java
public static final
FocusEvent.Cause
ACTIVATION
```

An activation of a toplevel window.

---

#### ACTIVATION

public static final

FocusEvent.Cause

ACTIVATION

An activation of a toplevel window.

CLEAR_GLOBAL_FOCUS_OWNER

```java
public static final
FocusEvent.Cause
CLEAR_GLOBAL_FOCUS_OWNER
```

Clearing global focus owner.

---

#### CLEAR_GLOBAL_FOCUS_OWNER

public static final

FocusEvent.Cause

CLEAR_GLOBAL_FOCUS_OWNER

Clearing global focus owner.

Method Detail

- values

```java
public static
FocusEvent.Cause
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FocusEvent.Cause c : FocusEvent.Cause.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
FocusEvent.Cause
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
FocusEvent.Cause
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FocusEvent.Cause c : FocusEvent.Cause.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

FocusEvent.Cause

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (FocusEvent.Cause c : FocusEvent.Cause.values())
System.out.println(c);
```

for (FocusEvent.Cause c : FocusEvent.Cause.values())
System.out.println(c);

valueOf

```java
public static
FocusEvent.Cause
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

FocusEvent.Cause

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

