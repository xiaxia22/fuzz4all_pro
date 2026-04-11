# Enum Dialog.ModalityType

**Source:** `java.desktop\java\awt\Dialog.ModalityType.html`

### Class Description

```java
public static enum
Dialog.ModalityType

extends
Enum
<
Dialog.ModalityType
>
```

Modal dialogs block all input to some top-level windows.
Whether a particular window is blocked depends on dialog's type
of modality; this is called the "scope of blocking". The

ModalityType

enum specifies modal types and their
associated scopes.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Dialog.ModalityType

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Dialog.ModalityType
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Dialog.ModalityType c : Dialog.ModalityType.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Dialog.ModalityType
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

#### Enum Dialog.ModalityType

java.lang.Object

- java.lang.Enum

<

Dialog.ModalityType

>
- - java.awt.Dialog.ModalityType

java.lang.Enum

<

Dialog.ModalityType

>

- java.awt.Dialog.ModalityType

java.awt.Dialog.ModalityType

**All Implemented Interfaces:** Serializable

,

Comparable

<

Dialog.ModalityType

>

**Enclosing class:** Dialog

```java
public static enum
Dialog.ModalityType

extends
Enum
<
Dialog.ModalityType
>
```

Modal dialogs block all input to some top-level windows.
Whether a particular window is blocked depends on dialog's type
of modality; this is called the "scope of blocking". The

ModalityType

enum specifies modal types and their
associated scopes.

**Since:** 1.6
**See Also:** Dialog.getModalityType()

,

Dialog.setModalityType(java.awt.Dialog.ModalityType)

,

Toolkit.isModalityTypeSupported(java.awt.Dialog.ModalityType)

public static enum

Dialog.ModalityType

extends

Enum

<

Dialog.ModalityType

>

Modal dialogs block all input to some top-level windows.
Whether a particular window is blocked depends on dialog's type
of modality; this is called the "scope of blocking". The

ModalityType

enum specifies modal types and their
associated scopes.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

APPLICATION_MODAL

An

APPLICATION_MODAL

dialog blocks all top-level windows
from the same Java application except those from its own child hierarchy.

DOCUMENT_MODAL

A

DOCUMENT_MODAL

dialog blocks input to all top-level windows
from the same document except those from its own child hierarchy.

MODELESS

MODELESS

dialog doesn't block any top-level windows.

TOOLKIT_MODAL

A

TOOLKIT_MODAL

dialog blocks all top-level windows run
from the same toolkit except those from its own child hierarchy.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Dialog.ModalityType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Dialog.ModalityType

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

APPLICATION_MODAL

An

APPLICATION_MODAL

dialog blocks all top-level windows
from the same Java application except those from its own child hierarchy.

DOCUMENT_MODAL

A

DOCUMENT_MODAL

dialog blocks input to all top-level windows
from the same document except those from its own child hierarchy.

MODELESS

MODELESS

dialog doesn't block any top-level windows.

TOOLKIT_MODAL

A

TOOLKIT_MODAL

dialog blocks all top-level windows run
from the same toolkit except those from its own child hierarchy.

---

#### Enum Constant Summary

An

APPLICATION_MODAL

dialog blocks all top-level windows
from the same Java application except those from its own child hierarchy.

A

DOCUMENT_MODAL

dialog blocks input to all top-level windows
from the same document except those from its own child hierarchy.

MODELESS

dialog doesn't block any top-level windows.

A

TOOLKIT_MODAL

dialog blocks all top-level windows run
from the same toolkit except those from its own child hierarchy.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Dialog.ModalityType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Dialog.ModalityType

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

- MODELESS

```java
public static final
Dialog.ModalityType
MODELESS
```

MODELESS

dialog doesn't block any top-level windows.

- DOCUMENT_MODAL

```java
public static final
Dialog.ModalityType
DOCUMENT_MODAL
```

A

DOCUMENT_MODAL

dialog blocks input to all top-level windows
from the same document except those from its own child hierarchy.
A document is a top-level window without an owner. It may contain child
windows that, together with the top-level window are treated as a single
solid document. Since every top-level window must belong to some
document, its root can be found as the top-nearest window without an owner.

- APPLICATION_MODAL

```java
public static final
Dialog.ModalityType
APPLICATION_MODAL
```

An

APPLICATION_MODAL

dialog blocks all top-level windows
from the same Java application except those from its own child hierarchy.
If there are several applets launched in a browser, they can be
treated either as separate applications or a single one. This behavior
is implementation-dependent.

- TOOLKIT_MODAL

```java
public static final
Dialog.ModalityType
TOOLKIT_MODAL
```

A

TOOLKIT_MODAL

dialog blocks all top-level windows run
from the same toolkit except those from its own child hierarchy. If there
are several applets launched in a browser, all of them run with the same
toolkit; thus, a toolkit-modal dialog displayed by an applet may affect
other applets and all windows of the browser instance which embeds the
Java runtime environment for this toolkit.
Special

AWTPermission

"toolkitModality" must be granted to use
toolkit-modal dialogs. If a

TOOLKIT_MODAL

dialog is being created
and this permission is not granted, a

SecurityException

will be
thrown, and no dialog will be created. If a modality type is being changed
to

TOOLKIT_MODAL

and this permission is not granted, a

SecurityException

will be thrown, and the modality type will
be left unchanged.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Dialog.ModalityType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Dialog.ModalityType c : Dialog.ModalityType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Dialog.ModalityType
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

- MODELESS

```java
public static final
Dialog.ModalityType
MODELESS
```

MODELESS

dialog doesn't block any top-level windows.

- DOCUMENT_MODAL

```java
public static final
Dialog.ModalityType
DOCUMENT_MODAL
```

A

DOCUMENT_MODAL

dialog blocks input to all top-level windows
from the same document except those from its own child hierarchy.
A document is a top-level window without an owner. It may contain child
windows that, together with the top-level window are treated as a single
solid document. Since every top-level window must belong to some
document, its root can be found as the top-nearest window without an owner.

- APPLICATION_MODAL

```java
public static final
Dialog.ModalityType
APPLICATION_MODAL
```

An

APPLICATION_MODAL

dialog blocks all top-level windows
from the same Java application except those from its own child hierarchy.
If there are several applets launched in a browser, they can be
treated either as separate applications or a single one. This behavior
is implementation-dependent.

- TOOLKIT_MODAL

```java
public static final
Dialog.ModalityType
TOOLKIT_MODAL
```

A

TOOLKIT_MODAL

dialog blocks all top-level windows run
from the same toolkit except those from its own child hierarchy. If there
are several applets launched in a browser, all of them run with the same
toolkit; thus, a toolkit-modal dialog displayed by an applet may affect
other applets and all windows of the browser instance which embeds the
Java runtime environment for this toolkit.
Special

AWTPermission

"toolkitModality" must be granted to use
toolkit-modal dialogs. If a

TOOLKIT_MODAL

dialog is being created
and this permission is not granted, a

SecurityException

will be
thrown, and no dialog will be created. If a modality type is being changed
to

TOOLKIT_MODAL

and this permission is not granted, a

SecurityException

will be thrown, and the modality type will
be left unchanged.

---

#### Enum Constant Detail

MODELESS

```java
public static final
Dialog.ModalityType
MODELESS
```

MODELESS

dialog doesn't block any top-level windows.

---

#### MODELESS

public static final

Dialog.ModalityType

MODELESS

MODELESS

dialog doesn't block any top-level windows.

DOCUMENT_MODAL

```java
public static final
Dialog.ModalityType
DOCUMENT_MODAL
```

A

DOCUMENT_MODAL

dialog blocks input to all top-level windows
from the same document except those from its own child hierarchy.
A document is a top-level window without an owner. It may contain child
windows that, together with the top-level window are treated as a single
solid document. Since every top-level window must belong to some
document, its root can be found as the top-nearest window without an owner.

---

#### DOCUMENT_MODAL

public static final

Dialog.ModalityType

DOCUMENT_MODAL

A

DOCUMENT_MODAL

dialog blocks input to all top-level windows
from the same document except those from its own child hierarchy.
A document is a top-level window without an owner. It may contain child
windows that, together with the top-level window are treated as a single
solid document. Since every top-level window must belong to some
document, its root can be found as the top-nearest window without an owner.

APPLICATION_MODAL

```java
public static final
Dialog.ModalityType
APPLICATION_MODAL
```

An

APPLICATION_MODAL

dialog blocks all top-level windows
from the same Java application except those from its own child hierarchy.
If there are several applets launched in a browser, they can be
treated either as separate applications or a single one. This behavior
is implementation-dependent.

---

#### APPLICATION_MODAL

public static final

Dialog.ModalityType

APPLICATION_MODAL

An

APPLICATION_MODAL

dialog blocks all top-level windows
from the same Java application except those from its own child hierarchy.
If there are several applets launched in a browser, they can be
treated either as separate applications or a single one. This behavior
is implementation-dependent.

TOOLKIT_MODAL

```java
public static final
Dialog.ModalityType
TOOLKIT_MODAL
```

A

TOOLKIT_MODAL

dialog blocks all top-level windows run
from the same toolkit except those from its own child hierarchy. If there
are several applets launched in a browser, all of them run with the same
toolkit; thus, a toolkit-modal dialog displayed by an applet may affect
other applets and all windows of the browser instance which embeds the
Java runtime environment for this toolkit.
Special

AWTPermission

"toolkitModality" must be granted to use
toolkit-modal dialogs. If a

TOOLKIT_MODAL

dialog is being created
and this permission is not granted, a

SecurityException

will be
thrown, and no dialog will be created. If a modality type is being changed
to

TOOLKIT_MODAL

and this permission is not granted, a

SecurityException

will be thrown, and the modality type will
be left unchanged.

---

#### TOOLKIT_MODAL

public static final

Dialog.ModalityType

TOOLKIT_MODAL

A

TOOLKIT_MODAL

dialog blocks all top-level windows run
from the same toolkit except those from its own child hierarchy. If there
are several applets launched in a browser, all of them run with the same
toolkit; thus, a toolkit-modal dialog displayed by an applet may affect
other applets and all windows of the browser instance which embeds the
Java runtime environment for this toolkit.
Special

AWTPermission

"toolkitModality" must be granted to use
toolkit-modal dialogs. If a

TOOLKIT_MODAL

dialog is being created
and this permission is not granted, a

SecurityException

will be
thrown, and no dialog will be created. If a modality type is being changed
to

TOOLKIT_MODAL

and this permission is not granted, a

SecurityException

will be thrown, and the modality type will
be left unchanged.

Method Detail

- values

```java
public static
Dialog.ModalityType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Dialog.ModalityType c : Dialog.ModalityType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Dialog.ModalityType
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
Dialog.ModalityType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Dialog.ModalityType c : Dialog.ModalityType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Dialog.ModalityType

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Dialog.ModalityType c : Dialog.ModalityType.values())
System.out.println(c);
```

for (Dialog.ModalityType c : Dialog.ModalityType.values())
System.out.println(c);

valueOf

```java
public static
Dialog.ModalityType
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

Dialog.ModalityType

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

