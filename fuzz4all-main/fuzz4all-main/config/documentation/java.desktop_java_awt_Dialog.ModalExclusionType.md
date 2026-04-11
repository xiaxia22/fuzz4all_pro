# Enum Dialog.ModalExclusionType

**Source:** `java.desktop\java\awt\Dialog.ModalExclusionType.html`

### Class Description

```java
public static enum
Dialog.ModalExclusionType

extends
Enum
<
Dialog.ModalExclusionType
>
```

Any top-level window can be marked not to be blocked by modal
dialogs. This is called "modal exclusion". This enum specifies
the possible modal exclusion types.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Dialog.ModalExclusionType

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Dialog.ModalExclusionType
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Dialog.ModalExclusionType c : Dialog.ModalExclusionType.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Dialog.ModalExclusionType
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

#### Enum Dialog.ModalExclusionType

java.lang.Object

- java.lang.Enum

<

Dialog.ModalExclusionType

>
- - java.awt.Dialog.ModalExclusionType

java.lang.Enum

<

Dialog.ModalExclusionType

>

- java.awt.Dialog.ModalExclusionType

java.awt.Dialog.ModalExclusionType

**All Implemented Interfaces:** Serializable

,

Comparable

<

Dialog.ModalExclusionType

>

**Enclosing class:** Dialog

```java
public static enum
Dialog.ModalExclusionType

extends
Enum
<
Dialog.ModalExclusionType
>
```

Any top-level window can be marked not to be blocked by modal
dialogs. This is called "modal exclusion". This enum specifies
the possible modal exclusion types.

**Since:** 1.6
**See Also:** Window.getModalExclusionType()

,

Window.setModalExclusionType(java.awt.Dialog.ModalExclusionType)

,

Toolkit.isModalExclusionTypeSupported(java.awt.Dialog.ModalExclusionType)

public static enum

Dialog.ModalExclusionType

extends

Enum

<

Dialog.ModalExclusionType

>

Any top-level window can be marked not to be blocked by modal
dialogs. This is called "modal exclusion". This enum specifies
the possible modal exclusion types.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

APPLICATION_EXCLUDE

APPLICATION_EXCLUDE

indicates that a top-level window
won't be blocked by any application-modal dialogs.

NO_EXCLUDE

No modal exclusion.

TOOLKIT_EXCLUDE

TOOLKIT_EXCLUDE

indicates that a top-level window
won't be blocked by application-modal or toolkit-modal dialogs.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Dialog.ModalExclusionType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Dialog.ModalExclusionType

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

APPLICATION_EXCLUDE

APPLICATION_EXCLUDE

indicates that a top-level window
won't be blocked by any application-modal dialogs.

NO_EXCLUDE

No modal exclusion.

TOOLKIT_EXCLUDE

TOOLKIT_EXCLUDE

indicates that a top-level window
won't be blocked by application-modal or toolkit-modal dialogs.

---

#### Enum Constant Summary

APPLICATION_EXCLUDE

indicates that a top-level window
won't be blocked by any application-modal dialogs.

No modal exclusion.

TOOLKIT_EXCLUDE

indicates that a top-level window
won't be blocked by application-modal or toolkit-modal dialogs.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Dialog.ModalExclusionType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Dialog.ModalExclusionType

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

- NO_EXCLUDE

```java
public static final
Dialog.ModalExclusionType
NO_EXCLUDE
```

No modal exclusion.

- APPLICATION_EXCLUDE

```java
public static final
Dialog.ModalExclusionType
APPLICATION_EXCLUDE
```

APPLICATION_EXCLUDE

indicates that a top-level window
won't be blocked by any application-modal dialogs. Also, it isn't
blocked by document-modal dialogs from outside of its child hierarchy.

- TOOLKIT_EXCLUDE

```java
public static final
Dialog.ModalExclusionType
TOOLKIT_EXCLUDE
```

TOOLKIT_EXCLUDE

indicates that a top-level window
won't be blocked by application-modal or toolkit-modal dialogs. Also,
it isn't blocked by document-modal dialogs from outside of its
child hierarchy.
The "toolkitModality"

AWTPermission

must be granted
for this exclusion. If an exclusion property is being changed to

TOOLKIT_EXCLUDE

and this permission is not granted, a

SecurityException

will be thrown, and the exclusion
property will be left unchanged.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Dialog.ModalExclusionType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Dialog.ModalExclusionType c : Dialog.ModalExclusionType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Dialog.ModalExclusionType
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

- NO_EXCLUDE

```java
public static final
Dialog.ModalExclusionType
NO_EXCLUDE
```

No modal exclusion.

- APPLICATION_EXCLUDE

```java
public static final
Dialog.ModalExclusionType
APPLICATION_EXCLUDE
```

APPLICATION_EXCLUDE

indicates that a top-level window
won't be blocked by any application-modal dialogs. Also, it isn't
blocked by document-modal dialogs from outside of its child hierarchy.

- TOOLKIT_EXCLUDE

```java
public static final
Dialog.ModalExclusionType
TOOLKIT_EXCLUDE
```

TOOLKIT_EXCLUDE

indicates that a top-level window
won't be blocked by application-modal or toolkit-modal dialogs. Also,
it isn't blocked by document-modal dialogs from outside of its
child hierarchy.
The "toolkitModality"

AWTPermission

must be granted
for this exclusion. If an exclusion property is being changed to

TOOLKIT_EXCLUDE

and this permission is not granted, a

SecurityException

will be thrown, and the exclusion
property will be left unchanged.

---

#### Enum Constant Detail

NO_EXCLUDE

```java
public static final
Dialog.ModalExclusionType
NO_EXCLUDE
```

No modal exclusion.

---

#### NO_EXCLUDE

public static final

Dialog.ModalExclusionType

NO_EXCLUDE

No modal exclusion.

APPLICATION_EXCLUDE

```java
public static final
Dialog.ModalExclusionType
APPLICATION_EXCLUDE
```

APPLICATION_EXCLUDE

indicates that a top-level window
won't be blocked by any application-modal dialogs. Also, it isn't
blocked by document-modal dialogs from outside of its child hierarchy.

---

#### APPLICATION_EXCLUDE

public static final

Dialog.ModalExclusionType

APPLICATION_EXCLUDE

APPLICATION_EXCLUDE

indicates that a top-level window
won't be blocked by any application-modal dialogs. Also, it isn't
blocked by document-modal dialogs from outside of its child hierarchy.

TOOLKIT_EXCLUDE

```java
public static final
Dialog.ModalExclusionType
TOOLKIT_EXCLUDE
```

TOOLKIT_EXCLUDE

indicates that a top-level window
won't be blocked by application-modal or toolkit-modal dialogs. Also,
it isn't blocked by document-modal dialogs from outside of its
child hierarchy.
The "toolkitModality"

AWTPermission

must be granted
for this exclusion. If an exclusion property is being changed to

TOOLKIT_EXCLUDE

and this permission is not granted, a

SecurityException

will be thrown, and the exclusion
property will be left unchanged.

---

#### TOOLKIT_EXCLUDE

public static final

Dialog.ModalExclusionType

TOOLKIT_EXCLUDE

TOOLKIT_EXCLUDE

indicates that a top-level window
won't be blocked by application-modal or toolkit-modal dialogs. Also,
it isn't blocked by document-modal dialogs from outside of its
child hierarchy.
The "toolkitModality"

AWTPermission

must be granted
for this exclusion. If an exclusion property is being changed to

TOOLKIT_EXCLUDE

and this permission is not granted, a

SecurityException

will be thrown, and the exclusion
property will be left unchanged.

Method Detail

- values

```java
public static
Dialog.ModalExclusionType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Dialog.ModalExclusionType c : Dialog.ModalExclusionType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Dialog.ModalExclusionType
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
Dialog.ModalExclusionType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Dialog.ModalExclusionType c : Dialog.ModalExclusionType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Dialog.ModalExclusionType

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Dialog.ModalExclusionType c : Dialog.ModalExclusionType.values())
System.out.println(c);
```

for (Dialog.ModalExclusionType c : Dialog.ModalExclusionType.values())
System.out.println(c);

valueOf

```java
public static
Dialog.ModalExclusionType
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

Dialog.ModalExclusionType

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

