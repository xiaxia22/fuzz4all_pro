# Class MenuShortcut

**Source:** `java.desktop\java\awt\MenuShortcut.html`

### Class Description

```java
public class
MenuShortcut

extends
Object

implements
Serializable
```

The

MenuShortcut

class represents a keyboard accelerator
for a MenuItem.

Menu shortcuts are created using virtual keycodes, not characters.
For example, a menu shortcut for Ctrl-a (assuming that Control is
the accelerator key) would be created with code like the following:

MenuShortcut ms = new MenuShortcut(KeyEvent.VK_A, false);

or alternatively

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('A'), false);

Menu shortcuts may also be constructed for a wider set of keycodes
using the

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

call.
For example, a menu shortcut for "Ctrl+cyrillic ef" is created by

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('ф'), false);

Note that shortcuts created with a keycode or an extended keycode defined as a constant in

KeyEvent

work regardless of the current keyboard layout. However, a shortcut made of
an extended keycode not listed in

KeyEvent

only work if the current keyboard layout produces a corresponding letter.

The accelerator key is platform-dependent and may be obtained
via

Toolkit.getMenuShortcutKeyMaskEx()

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public MenuShortcut​(int key)

Constructs a new MenuShortcut for the specified virtual keycode.

**Parameters:**
- key

- the raw keycode for this MenuShortcut, as would be returned
in the keyCode field of a

KeyEvent

if
this key were pressed.

**See Also:**
- KeyEvent

---

#### public MenuShortcut​(int key,
boolean useShiftModifier)

Constructs a new MenuShortcut for the specified virtual keycode.

**Parameters:**
- key

- the raw keycode for this MenuShortcut, as would be returned
in the keyCode field of a

KeyEvent

if
this key were pressed.
- useShiftModifier

- indicates whether this MenuShortcut is invoked
with the SHIFT key down.

**See Also:**
- KeyEvent

---

### Method Details

#### public int getKey()

Returns the raw keycode of this MenuShortcut.

**Returns:**
- the raw keycode of this MenuShortcut.

**See Also:**
- KeyEvent

**Since:**
- 1.1

---

#### public boolean usesShiftModifier()

Returns whether this MenuShortcut must be invoked using the SHIFT key.

**Returns:**
- true

if this MenuShortcut must be invoked using the
SHIFT key,

false

otherwise.

**Since:**
- 1.1

---

#### public boolean equals​(
MenuShortcut
s)

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

**Parameters:**
- s

- the MenuShortcut to compare with this.

**Returns:**
- true

if this MenuShortcut is the same as another,

false

otherwise.

**Since:**
- 1.1

---

#### public boolean equals​(
Object
obj)

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the Object to compare with this.

**Returns:**
- true

if this MenuShortcut is the same as another,

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

**Since:**
- 1.2

---

#### public int hashCode()

Returns the hashcode for this MenuShortcut.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hashcode for this MenuShortcut.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

**Since:**
- 1.2

---

#### public
String
toString()

Returns an internationalized description of the MenuShortcut.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this MenuShortcut.

**Since:**
- 1.1

---

#### protected
String
paramString()

Returns the parameter string representing the state of this
MenuShortcut. This string is useful for debugging.

**Returns:**
- the parameter string of this MenuShortcut.

**Since:**
- 1.1

---

### Additional Sections

#### Class MenuShortcut

java.lang.Object

- java.awt.MenuShortcut

java.awt.MenuShortcut

**All Implemented Interfaces:** Serializable

```java
public class
MenuShortcut

extends
Object

implements
Serializable
```

The

MenuShortcut

class represents a keyboard accelerator
for a MenuItem.

Menu shortcuts are created using virtual keycodes, not characters.
For example, a menu shortcut for Ctrl-a (assuming that Control is
the accelerator key) would be created with code like the following:

MenuShortcut ms = new MenuShortcut(KeyEvent.VK_A, false);

or alternatively

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('A'), false);

Menu shortcuts may also be constructed for a wider set of keycodes
using the

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

call.
For example, a menu shortcut for "Ctrl+cyrillic ef" is created by

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('ф'), false);

Note that shortcuts created with a keycode or an extended keycode defined as a constant in

KeyEvent

work regardless of the current keyboard layout. However, a shortcut made of
an extended keycode not listed in

KeyEvent

only work if the current keyboard layout produces a corresponding letter.

The accelerator key is platform-dependent and may be obtained
via

Toolkit.getMenuShortcutKeyMaskEx()

.

**Since:** 1.1
**See Also:** Serialized Form

public class

MenuShortcut

extends

Object

implements

Serializable

The

MenuShortcut

class represents a keyboard accelerator
for a MenuItem.

Menu shortcuts are created using virtual keycodes, not characters.
For example, a menu shortcut for Ctrl-a (assuming that Control is
the accelerator key) would be created with code like the following:

MenuShortcut ms = new MenuShortcut(KeyEvent.VK_A, false);

or alternatively

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('A'), false);

Menu shortcuts may also be constructed for a wider set of keycodes
using the

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

call.
For example, a menu shortcut for "Ctrl+cyrillic ef" is created by

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('ф'), false);

Note that shortcuts created with a keycode or an extended keycode defined as a constant in

KeyEvent

work regardless of the current keyboard layout. However, a shortcut made of
an extended keycode not listed in

KeyEvent

only work if the current keyboard layout produces a corresponding letter.

The accelerator key is platform-dependent and may be obtained
via

Toolkit.getMenuShortcutKeyMaskEx()

.

Menu shortcuts are created using virtual keycodes, not characters.
For example, a menu shortcut for Ctrl-a (assuming that Control is
the accelerator key) would be created with code like the following:

MenuShortcut ms = new MenuShortcut(KeyEvent.VK_A, false);

or alternatively

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('A'), false);

Menu shortcuts may also be constructed for a wider set of keycodes
using the

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

call.
For example, a menu shortcut for "Ctrl+cyrillic ef" is created by

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('ф'), false);

Note that shortcuts created with a keycode or an extended keycode defined as a constant in

KeyEvent

work regardless of the current keyboard layout. However, a shortcut made of
an extended keycode not listed in

KeyEvent

only work if the current keyboard layout produces a corresponding letter.

The accelerator key is platform-dependent and may be obtained
via

Toolkit.getMenuShortcutKeyMaskEx()

.

MenuShortcut ms = new MenuShortcut(KeyEvent.VK_A, false);

or alternatively

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('A'), false);

Menu shortcuts may also be constructed for a wider set of keycodes
using the

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

call.
For example, a menu shortcut for "Ctrl+cyrillic ef" is created by

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('ф'), false);

Note that shortcuts created with a keycode or an extended keycode defined as a constant in

KeyEvent

work regardless of the current keyboard layout. However, a shortcut made of
an extended keycode not listed in

KeyEvent

only work if the current keyboard layout produces a corresponding letter.

The accelerator key is platform-dependent and may be obtained
via

Toolkit.getMenuShortcutKeyMaskEx()

.

or alternatively

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('A'), false);

Menu shortcuts may also be constructed for a wider set of keycodes
using the

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

call.
For example, a menu shortcut for "Ctrl+cyrillic ef" is created by

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('ф'), false);

Note that shortcuts created with a keycode or an extended keycode defined as a constant in

KeyEvent

work regardless of the current keyboard layout. However, a shortcut made of
an extended keycode not listed in

KeyEvent

only work if the current keyboard layout produces a corresponding letter.

The accelerator key is platform-dependent and may be obtained
via

Toolkit.getMenuShortcutKeyMaskEx()

.

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('A'), false);

Menu shortcuts may also be constructed for a wider set of keycodes
using the

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

call.
For example, a menu shortcut for "Ctrl+cyrillic ef" is created by

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('ф'), false);

Note that shortcuts created with a keycode or an extended keycode defined as a constant in

KeyEvent

work regardless of the current keyboard layout. However, a shortcut made of
an extended keycode not listed in

KeyEvent

only work if the current keyboard layout produces a corresponding letter.

The accelerator key is platform-dependent and may be obtained
via

Toolkit.getMenuShortcutKeyMaskEx()

.

Menu shortcuts may also be constructed for a wider set of keycodes
using the

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

call.
For example, a menu shortcut for "Ctrl+cyrillic ef" is created by

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('ф'), false);

Note that shortcuts created with a keycode or an extended keycode defined as a constant in

KeyEvent

work regardless of the current keyboard layout. However, a shortcut made of
an extended keycode not listed in

KeyEvent

only work if the current keyboard layout produces a corresponding letter.

The accelerator key is platform-dependent and may be obtained
via

Toolkit.getMenuShortcutKeyMaskEx()

.

MenuShortcut ms = new MenuShortcut(KeyEvent.getExtendedKeyCodeForChar('ф'), false);

Note that shortcuts created with a keycode or an extended keycode defined as a constant in

KeyEvent

work regardless of the current keyboard layout. However, a shortcut made of
an extended keycode not listed in

KeyEvent

only work if the current keyboard layout produces a corresponding letter.

The accelerator key is platform-dependent and may be obtained
via

Toolkit.getMenuShortcutKeyMaskEx()

.

Note that shortcuts created with a keycode or an extended keycode defined as a constant in

KeyEvent

work regardless of the current keyboard layout. However, a shortcut made of
an extended keycode not listed in

KeyEvent

only work if the current keyboard layout produces a corresponding letter.

The accelerator key is platform-dependent and may be obtained
via

Toolkit.getMenuShortcutKeyMaskEx()

.

The accelerator key is platform-dependent and may be obtained
via

Toolkit.getMenuShortcutKeyMaskEx()

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MenuShortcut

​(int key)

Constructs a new MenuShortcut for the specified virtual keycode.

MenuShortcut

​(int key,
boolean useShiftModifier)

Constructs a new MenuShortcut for the specified virtual keycode.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

MenuShortcut

s)

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

boolean

equals

​(

Object

obj)

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

int

getKey

()

Returns the raw keycode of this MenuShortcut.

int

hashCode

()

Returns the hashcode for this MenuShortcut.

protected

String

paramString

()

Returns the parameter string representing the state of this
MenuShortcut.

String

toString

()

Returns an internationalized description of the MenuShortcut.

boolean

usesShiftModifier

()

Returns whether this MenuShortcut must be invoked using the SHIFT key.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Constructor Summary

Constructors

Constructor

Description

MenuShortcut

​(int key)

Constructs a new MenuShortcut for the specified virtual keycode.

MenuShortcut

​(int key,
boolean useShiftModifier)

Constructs a new MenuShortcut for the specified virtual keycode.

---

#### Constructor Summary

Constructs a new MenuShortcut for the specified virtual keycode.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

MenuShortcut

s)

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

boolean

equals

​(

Object

obj)

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

int

getKey

()

Returns the raw keycode of this MenuShortcut.

int

hashCode

()

Returns the hashcode for this MenuShortcut.

protected

String

paramString

()

Returns the parameter string representing the state of this
MenuShortcut.

String

toString

()

Returns an internationalized description of the MenuShortcut.

boolean

usesShiftModifier

()

Returns whether this MenuShortcut must be invoked using the SHIFT key.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

Returns the raw keycode of this MenuShortcut.

Returns the hashcode for this MenuShortcut.

Returns the parameter string representing the state of this
MenuShortcut.

Returns an internationalized description of the MenuShortcut.

Returns whether this MenuShortcut must be invoked using the SHIFT key.

Methods declared in class java.lang.

Object

clone

,

finalize

,

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MenuShortcut

```java
public MenuShortcut​(int key)
```

Constructs a new MenuShortcut for the specified virtual keycode.

**Parameters:** key

- the raw keycode for this MenuShortcut, as would be returned
in the keyCode field of a

KeyEvent

if
this key were pressed.
**See Also:** KeyEvent

- MenuShortcut

```java
public MenuShortcut​(int key,
boolean useShiftModifier)
```

Constructs a new MenuShortcut for the specified virtual keycode.

**Parameters:** key

- the raw keycode for this MenuShortcut, as would be returned
in the keyCode field of a

KeyEvent

if
this key were pressed.
**Parameters:** useShiftModifier

- indicates whether this MenuShortcut is invoked
with the SHIFT key down.
**See Also:** KeyEvent

============ METHOD DETAIL ==========

- Method Detail

- getKey

```java
public int getKey()
```

Returns the raw keycode of this MenuShortcut.

**Returns:** the raw keycode of this MenuShortcut.
**Since:** 1.1
**See Also:** KeyEvent

- usesShiftModifier

```java
public boolean usesShiftModifier()
```

Returns whether this MenuShortcut must be invoked using the SHIFT key.

**Returns:** true

if this MenuShortcut must be invoked using the
SHIFT key,

false

otherwise.
**Since:** 1.1

- equals

```java
public boolean equals​(
MenuShortcut
s)
```

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

**Parameters:** s

- the MenuShortcut to compare with this.
**Returns:** true

if this MenuShortcut is the same as another,

false

otherwise.
**Since:** 1.1

- equals

```java
public boolean equals​(
Object
obj)
```

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with this.
**Returns:** true

if this MenuShortcut is the same as another,

false

otherwise.
**Since:** 1.2
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this MenuShortcut.

**Overrides:** hashCode

in class

Object
**Returns:** the hashcode for this MenuShortcut.
**Since:** 1.2
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns an internationalized description of the MenuShortcut.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this MenuShortcut.
**Since:** 1.1

- paramString

```java
protected
String
paramString()
```

Returns the parameter string representing the state of this
MenuShortcut. This string is useful for debugging.

**Returns:** the parameter string of this MenuShortcut.
**Since:** 1.1

Constructor Detail

- MenuShortcut

```java
public MenuShortcut​(int key)
```

Constructs a new MenuShortcut for the specified virtual keycode.

**Parameters:** key

- the raw keycode for this MenuShortcut, as would be returned
in the keyCode field of a

KeyEvent

if
this key were pressed.
**See Also:** KeyEvent

- MenuShortcut

```java
public MenuShortcut​(int key,
boolean useShiftModifier)
```

Constructs a new MenuShortcut for the specified virtual keycode.

**Parameters:** key

- the raw keycode for this MenuShortcut, as would be returned
in the keyCode field of a

KeyEvent

if
this key were pressed.
**Parameters:** useShiftModifier

- indicates whether this MenuShortcut is invoked
with the SHIFT key down.
**See Also:** KeyEvent

---

#### Constructor Detail

MenuShortcut

```java
public MenuShortcut​(int key)
```

Constructs a new MenuShortcut for the specified virtual keycode.

**Parameters:** key

- the raw keycode for this MenuShortcut, as would be returned
in the keyCode field of a

KeyEvent

if
this key were pressed.
**See Also:** KeyEvent

---

#### MenuShortcut

public MenuShortcut​(int key)

Constructs a new MenuShortcut for the specified virtual keycode.

MenuShortcut

```java
public MenuShortcut​(int key,
boolean useShiftModifier)
```

Constructs a new MenuShortcut for the specified virtual keycode.

**Parameters:** key

- the raw keycode for this MenuShortcut, as would be returned
in the keyCode field of a

KeyEvent

if
this key were pressed.
**Parameters:** useShiftModifier

- indicates whether this MenuShortcut is invoked
with the SHIFT key down.
**See Also:** KeyEvent

---

#### MenuShortcut

public MenuShortcut​(int key,
boolean useShiftModifier)

Constructs a new MenuShortcut for the specified virtual keycode.

Method Detail

- getKey

```java
public int getKey()
```

Returns the raw keycode of this MenuShortcut.

**Returns:** the raw keycode of this MenuShortcut.
**Since:** 1.1
**See Also:** KeyEvent

- usesShiftModifier

```java
public boolean usesShiftModifier()
```

Returns whether this MenuShortcut must be invoked using the SHIFT key.

**Returns:** true

if this MenuShortcut must be invoked using the
SHIFT key,

false

otherwise.
**Since:** 1.1

- equals

```java
public boolean equals​(
MenuShortcut
s)
```

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

**Parameters:** s

- the MenuShortcut to compare with this.
**Returns:** true

if this MenuShortcut is the same as another,

false

otherwise.
**Since:** 1.1

- equals

```java
public boolean equals​(
Object
obj)
```

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with this.
**Returns:** true

if this MenuShortcut is the same as another,

false

otherwise.
**Since:** 1.2
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hashcode for this MenuShortcut.

**Overrides:** hashCode

in class

Object
**Returns:** the hashcode for this MenuShortcut.
**Since:** 1.2
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns an internationalized description of the MenuShortcut.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this MenuShortcut.
**Since:** 1.1

- paramString

```java
protected
String
paramString()
```

Returns the parameter string representing the state of this
MenuShortcut. This string is useful for debugging.

**Returns:** the parameter string of this MenuShortcut.
**Since:** 1.1

---

#### Method Detail

getKey

```java
public int getKey()
```

Returns the raw keycode of this MenuShortcut.

**Returns:** the raw keycode of this MenuShortcut.
**Since:** 1.1
**See Also:** KeyEvent

---

#### getKey

public int getKey()

Returns the raw keycode of this MenuShortcut.

usesShiftModifier

```java
public boolean usesShiftModifier()
```

Returns whether this MenuShortcut must be invoked using the SHIFT key.

**Returns:** true

if this MenuShortcut must be invoked using the
SHIFT key,

false

otherwise.
**Since:** 1.1

---

#### usesShiftModifier

public boolean usesShiftModifier()

Returns whether this MenuShortcut must be invoked using the SHIFT key.

equals

```java
public boolean equals​(
MenuShortcut
s)
```

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

**Parameters:** s

- the MenuShortcut to compare with this.
**Returns:** true

if this MenuShortcut is the same as another,

false

otherwise.
**Since:** 1.1

---

#### equals

public boolean equals​(

MenuShortcut

s)

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

equals

```java
public boolean equals​(
Object
obj)
```

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with this.
**Returns:** true

if this MenuShortcut is the same as another,

false

otherwise.
**Since:** 1.2
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Returns whether this MenuShortcut is the same as another:
equality is defined to mean that both MenuShortcuts use the same key
and both either use or don't use the SHIFT key.

hashCode

```java
public int hashCode()
```

Returns the hashcode for this MenuShortcut.

**Overrides:** hashCode

in class

Object
**Returns:** the hashcode for this MenuShortcut.
**Since:** 1.2
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hashcode for this MenuShortcut.

toString

```java
public
String
toString()
```

Returns an internationalized description of the MenuShortcut.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this MenuShortcut.
**Since:** 1.1

---

#### toString

public

String

toString()

Returns an internationalized description of the MenuShortcut.

paramString

```java
protected
String
paramString()
```

Returns the parameter string representing the state of this
MenuShortcut. This string is useful for debugging.

**Returns:** the parameter string of this MenuShortcut.
**Since:** 1.1

---

#### paramString

protected

String

paramString()

Returns the parameter string representing the state of this
MenuShortcut. This string is useful for debugging.

---

