# Enum Taskbar.Feature

**Source:** `java.desktop\java\awt\Taskbar.Feature.html`

### Class Description

```java
public static enum
Taskbar.Feature

extends
Enum
<
Taskbar.Feature
>
```

List of provided features. Each platform supports a different
set of features. You may use the

Taskbar.isSupported(java.awt.Taskbar.Feature)

method to determine if the given feature is supported by the
current platform.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Taskbar.Feature

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Taskbar.Feature
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Taskbar.Feature c : Taskbar.Feature.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Taskbar.Feature
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

#### Enum Taskbar.Feature

java.lang.Object

- java.lang.Enum

<

Taskbar.Feature

>
- - java.awt.Taskbar.Feature

java.lang.Enum

<

Taskbar.Feature

>

- java.awt.Taskbar.Feature

java.awt.Taskbar.Feature

**All Implemented Interfaces:** Serializable

,

Comparable

<

Taskbar.Feature

>

**Enclosing class:** Taskbar

```java
public static enum
Taskbar.Feature

extends
Enum
<
Taskbar.Feature
>
```

List of provided features. Each platform supports a different
set of features. You may use the

Taskbar.isSupported(java.awt.Taskbar.Feature)

method to determine if the given feature is supported by the
current platform.

public static enum

Taskbar.Feature

extends

Enum

<

Taskbar.Feature

>

List of provided features. Each platform supports a different
set of features. You may use the

Taskbar.isSupported(java.awt.Taskbar.Feature)

method to determine if the given feature is supported by the
current platform.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ICON_BADGE_IMAGE_WINDOW

Represents a graphical icon badge feature for a window.

ICON_BADGE_NUMBER

Represents a numerical icon badge feature.

ICON_BADGE_TEXT

Represents a textual icon badge feature.

ICON_IMAGE

Represents an icon feature.

MENU

Represents a menu feature.

PROGRESS_STATE_WINDOW

Represents a progress state feature for a specified window.

PROGRESS_VALUE

Represents a progress value feature.

PROGRESS_VALUE_WINDOW

Represents a progress value feature for a specified window.

USER_ATTENTION

Represents a user attention request feature.

USER_ATTENTION_WINDOW

Represents a user attention request feature for a specified window.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Taskbar.Feature

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Taskbar.Feature

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

ICON_BADGE_IMAGE_WINDOW

Represents a graphical icon badge feature for a window.

ICON_BADGE_NUMBER

Represents a numerical icon badge feature.

ICON_BADGE_TEXT

Represents a textual icon badge feature.

ICON_IMAGE

Represents an icon feature.

MENU

Represents a menu feature.

PROGRESS_STATE_WINDOW

Represents a progress state feature for a specified window.

PROGRESS_VALUE

Represents a progress value feature.

PROGRESS_VALUE_WINDOW

Represents a progress value feature for a specified window.

USER_ATTENTION

Represents a user attention request feature.

USER_ATTENTION_WINDOW

Represents a user attention request feature for a specified window.

---

#### Enum Constant Summary

Represents a graphical icon badge feature for a window.

Represents a numerical icon badge feature.

Represents a textual icon badge feature.

Represents an icon feature.

Represents a menu feature.

Represents a progress state feature for a specified window.

Represents a progress value feature.

Represents a progress value feature for a specified window.

Represents a user attention request feature.

Represents a user attention request feature for a specified window.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Taskbar.Feature

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Taskbar.Feature

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

- ICON_BADGE_TEXT

```java
public static final
Taskbar.Feature
ICON_BADGE_TEXT
```

Represents a textual icon badge feature.

**See Also:** Taskbar.setIconBadge(java.lang.String)

- ICON_BADGE_NUMBER

```java
public static final
Taskbar.Feature
ICON_BADGE_NUMBER
```

Represents a numerical icon badge feature.

**See Also:** Taskbar.setIconBadge(java.lang.String)

- ICON_BADGE_IMAGE_WINDOW

```java
public static final
Taskbar.Feature
ICON_BADGE_IMAGE_WINDOW
```

Represents a graphical icon badge feature for a window.

**See Also:** Taskbar.setWindowIconBadge(java.awt.Window, java.awt.Image)

- ICON_IMAGE

```java
public static final
Taskbar.Feature
ICON_IMAGE
```

Represents an icon feature.

**See Also:** Taskbar.setIconImage(java.awt.Image)

- MENU

```java
public static final
Taskbar.Feature
MENU
```

Represents a menu feature.

**See Also:** Taskbar.setMenu(java.awt.PopupMenu)

,

Taskbar.getMenu()

- PROGRESS_STATE_WINDOW

```java
public static final
Taskbar.Feature
PROGRESS_STATE_WINDOW
```

Represents a progress state feature for a specified window.

**See Also:** Taskbar.setWindowProgressState(java.awt.Window, State)

- PROGRESS_VALUE

```java
public static final
Taskbar.Feature
PROGRESS_VALUE
```

Represents a progress value feature.

**See Also:** Taskbar.setProgressValue(int)

- PROGRESS_VALUE_WINDOW

```java
public static final
Taskbar.Feature
PROGRESS_VALUE_WINDOW
```

Represents a progress value feature for a specified window.

**See Also:** Taskbar.setWindowProgressValue(java.awt.Window, int)

- USER_ATTENTION

```java
public static final
Taskbar.Feature
USER_ATTENTION
```

Represents a user attention request feature.

**See Also:** Taskbar.requestUserAttention(boolean, boolean)

- USER_ATTENTION_WINDOW

```java
public static final
Taskbar.Feature
USER_ATTENTION_WINDOW
```

Represents a user attention request feature for a specified window.

**See Also:** Taskbar.requestWindowUserAttention(java.awt.Window)

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Taskbar.Feature
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Taskbar.Feature c : Taskbar.Feature.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Taskbar.Feature
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

- ICON_BADGE_TEXT

```java
public static final
Taskbar.Feature
ICON_BADGE_TEXT
```

Represents a textual icon badge feature.

**See Also:** Taskbar.setIconBadge(java.lang.String)

- ICON_BADGE_NUMBER

```java
public static final
Taskbar.Feature
ICON_BADGE_NUMBER
```

Represents a numerical icon badge feature.

**See Also:** Taskbar.setIconBadge(java.lang.String)

- ICON_BADGE_IMAGE_WINDOW

```java
public static final
Taskbar.Feature
ICON_BADGE_IMAGE_WINDOW
```

Represents a graphical icon badge feature for a window.

**See Also:** Taskbar.setWindowIconBadge(java.awt.Window, java.awt.Image)

- ICON_IMAGE

```java
public static final
Taskbar.Feature
ICON_IMAGE
```

Represents an icon feature.

**See Also:** Taskbar.setIconImage(java.awt.Image)

- MENU

```java
public static final
Taskbar.Feature
MENU
```

Represents a menu feature.

**See Also:** Taskbar.setMenu(java.awt.PopupMenu)

,

Taskbar.getMenu()

- PROGRESS_STATE_WINDOW

```java
public static final
Taskbar.Feature
PROGRESS_STATE_WINDOW
```

Represents a progress state feature for a specified window.

**See Also:** Taskbar.setWindowProgressState(java.awt.Window, State)

- PROGRESS_VALUE

```java
public static final
Taskbar.Feature
PROGRESS_VALUE
```

Represents a progress value feature.

**See Also:** Taskbar.setProgressValue(int)

- PROGRESS_VALUE_WINDOW

```java
public static final
Taskbar.Feature
PROGRESS_VALUE_WINDOW
```

Represents a progress value feature for a specified window.

**See Also:** Taskbar.setWindowProgressValue(java.awt.Window, int)

- USER_ATTENTION

```java
public static final
Taskbar.Feature
USER_ATTENTION
```

Represents a user attention request feature.

**See Also:** Taskbar.requestUserAttention(boolean, boolean)

- USER_ATTENTION_WINDOW

```java
public static final
Taskbar.Feature
USER_ATTENTION_WINDOW
```

Represents a user attention request feature for a specified window.

**See Also:** Taskbar.requestWindowUserAttention(java.awt.Window)

---

#### Enum Constant Detail

ICON_BADGE_TEXT

```java
public static final
Taskbar.Feature
ICON_BADGE_TEXT
```

Represents a textual icon badge feature.

**See Also:** Taskbar.setIconBadge(java.lang.String)

---

#### ICON_BADGE_TEXT

public static final

Taskbar.Feature

ICON_BADGE_TEXT

Represents a textual icon badge feature.

ICON_BADGE_NUMBER

```java
public static final
Taskbar.Feature
ICON_BADGE_NUMBER
```

Represents a numerical icon badge feature.

**See Also:** Taskbar.setIconBadge(java.lang.String)

---

#### ICON_BADGE_NUMBER

public static final

Taskbar.Feature

ICON_BADGE_NUMBER

Represents a numerical icon badge feature.

ICON_BADGE_IMAGE_WINDOW

```java
public static final
Taskbar.Feature
ICON_BADGE_IMAGE_WINDOW
```

Represents a graphical icon badge feature for a window.

**See Also:** Taskbar.setWindowIconBadge(java.awt.Window, java.awt.Image)

---

#### ICON_BADGE_IMAGE_WINDOW

public static final

Taskbar.Feature

ICON_BADGE_IMAGE_WINDOW

Represents a graphical icon badge feature for a window.

ICON_IMAGE

```java
public static final
Taskbar.Feature
ICON_IMAGE
```

Represents an icon feature.

**See Also:** Taskbar.setIconImage(java.awt.Image)

---

#### ICON_IMAGE

public static final

Taskbar.Feature

ICON_IMAGE

Represents an icon feature.

MENU

```java
public static final
Taskbar.Feature
MENU
```

Represents a menu feature.

**See Also:** Taskbar.setMenu(java.awt.PopupMenu)

,

Taskbar.getMenu()

---

#### MENU

public static final

Taskbar.Feature

MENU

Represents a menu feature.

PROGRESS_STATE_WINDOW

```java
public static final
Taskbar.Feature
PROGRESS_STATE_WINDOW
```

Represents a progress state feature for a specified window.

**See Also:** Taskbar.setWindowProgressState(java.awt.Window, State)

---

#### PROGRESS_STATE_WINDOW

public static final

Taskbar.Feature

PROGRESS_STATE_WINDOW

Represents a progress state feature for a specified window.

PROGRESS_VALUE

```java
public static final
Taskbar.Feature
PROGRESS_VALUE
```

Represents a progress value feature.

**See Also:** Taskbar.setProgressValue(int)

---

#### PROGRESS_VALUE

public static final

Taskbar.Feature

PROGRESS_VALUE

Represents a progress value feature.

PROGRESS_VALUE_WINDOW

```java
public static final
Taskbar.Feature
PROGRESS_VALUE_WINDOW
```

Represents a progress value feature for a specified window.

**See Also:** Taskbar.setWindowProgressValue(java.awt.Window, int)

---

#### PROGRESS_VALUE_WINDOW

public static final

Taskbar.Feature

PROGRESS_VALUE_WINDOW

Represents a progress value feature for a specified window.

USER_ATTENTION

```java
public static final
Taskbar.Feature
USER_ATTENTION
```

Represents a user attention request feature.

**See Also:** Taskbar.requestUserAttention(boolean, boolean)

---

#### USER_ATTENTION

public static final

Taskbar.Feature

USER_ATTENTION

Represents a user attention request feature.

USER_ATTENTION_WINDOW

```java
public static final
Taskbar.Feature
USER_ATTENTION_WINDOW
```

Represents a user attention request feature for a specified window.

**See Also:** Taskbar.requestWindowUserAttention(java.awt.Window)

---

#### USER_ATTENTION_WINDOW

public static final

Taskbar.Feature

USER_ATTENTION_WINDOW

Represents a user attention request feature for a specified window.

Method Detail

- values

```java
public static
Taskbar.Feature
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Taskbar.Feature c : Taskbar.Feature.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Taskbar.Feature
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
Taskbar.Feature
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Taskbar.Feature c : Taskbar.Feature.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Taskbar.Feature

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Taskbar.Feature c : Taskbar.Feature.values())
System.out.println(c);
```

for (Taskbar.Feature c : Taskbar.Feature.values())
System.out.println(c);

valueOf

```java
public static
Taskbar.Feature
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

Taskbar.Feature

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

