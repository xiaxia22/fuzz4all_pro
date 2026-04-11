# Class FocusManager

**Source:** `java.desktop\javax\swing\FocusManager.html`

### Class Description

```java
public abstract class
FocusManager

extends
DefaultKeyboardFocusManager
```

This class has been obsoleted by the 1.4 focus APIs. While client code may
still use this class, developers are strongly encouraged to use

java.awt.KeyboardFocusManager

and

java.awt.DefaultKeyboardFocusManager

instead.

Please see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

**All Implemented Interfaces:** KeyEventDispatcher

,

KeyEventPostProcessor

---

### Field Details

#### public static final
String
FOCUS_MANAGER_CLASS_PROPERTY

This field is obsolete, and its use is discouraged since its
specification is incompatible with the 1.4 focus APIs.
The current FocusManager is no longer a property of the UI.
Client code must query for the current FocusManager using

KeyboardFocusManager.getCurrentKeyboardFocusManager()

.
See the Focus Specification for more information.

**See Also:**
- KeyboardFocusManager.getCurrentKeyboardFocusManager()

,

Focus Specification

,

Constant Field Values

---

### Constructor Details

#### public FocusManager()

*No description found.*

---

### Method Details

#### public static
FocusManager
getCurrentManager()

Returns the current

KeyboardFocusManager

instance
for the calling thread's context.

**Returns:**
- this thread's context's

KeyboardFocusManager

**See Also:**
- setCurrentManager(javax.swing.FocusManager)

---

#### public static void setCurrentManager​(
FocusManager
aFocusManager)
throws
SecurityException

Sets the current

KeyboardFocusManager

instance
for the calling thread's context. If

null

is
specified, then the current

KeyboardFocusManager

is replaced with a new instance of

DefaultKeyboardFocusManager

.

If a

SecurityManager

is installed,
the calling thread must be granted the

AWTPermission

"replaceKeyboardFocusManager" in order to replace the
the current

KeyboardFocusManager

.
If this permission is not granted,
this method will throw a

SecurityException

,
and the current

KeyboardFocusManager

will be unchanged.

**Parameters:**
- aFocusManager

- the new

KeyboardFocusManager

for this thread's context

**Throws:**
- SecurityException

- if the calling thread does not have permission
to replace the current

KeyboardFocusManager

**See Also:**
- getCurrentManager()

,

DefaultKeyboardFocusManager

---

#### @Deprecated

public static void disableSwingFocusManager()

Changes the current

KeyboardFocusManager

's default

FocusTraversalPolicy

to

DefaultFocusTraversalPolicy

.

**See Also:**
- DefaultFocusTraversalPolicy

,

KeyboardFocusManager.setDefaultFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

---

#### @Deprecated

public static boolean isFocusManagerEnabled()

Returns whether the application has invoked

disableSwingFocusManager()

.

**Returns:**
- true

if focus manager is enabled.

**See Also:**
- disableSwingFocusManager()

---

### Additional Sections

#### Class FocusManager

java.lang.Object

- java.awt.KeyboardFocusManager
- - java.awt.DefaultKeyboardFocusManager
- - javax.swing.FocusManager

java.awt.KeyboardFocusManager

- java.awt.DefaultKeyboardFocusManager
- - javax.swing.FocusManager

java.awt.DefaultKeyboardFocusManager

- javax.swing.FocusManager

javax.swing.FocusManager

**All Implemented Interfaces:** KeyEventDispatcher

,

KeyEventPostProcessor

**Direct Known Subclasses:** DefaultFocusManager

```java
public abstract class
FocusManager

extends
DefaultKeyboardFocusManager
```

This class has been obsoleted by the 1.4 focus APIs. While client code may
still use this class, developers are strongly encouraged to use

java.awt.KeyboardFocusManager

and

java.awt.DefaultKeyboardFocusManager

instead.

Please see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

**Since:** 1.2
**See Also:** Focus Specification

public abstract class

FocusManager

extends

DefaultKeyboardFocusManager

This class has been obsoleted by the 1.4 focus APIs. While client code may
still use this class, developers are strongly encouraged to use

java.awt.KeyboardFocusManager

and

java.awt.DefaultKeyboardFocusManager

instead.

Please see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

Please see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

FOCUS_MANAGER_CLASS_PROPERTY

This field is obsolete, and its use is discouraged since its
specification is incompatible with the 1.4 focus APIs.

- Fields declared in class java.awt.

KeyboardFocusManager

BACKWARD_TRAVERSAL_KEYS

,

DOWN_CYCLE_TRAVERSAL_KEYS

,

FORWARD_TRAVERSAL_KEYS

,

UP_CYCLE_TRAVERSAL_KEYS

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FocusManager

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static void

disableSwingFocusManager

()

Deprecated.

as of 1.4, replaced by

KeyboardFocusManager.setDefaultFocusTraversalPolicy(FocusTraversalPolicy)

static

FocusManager

getCurrentManager

()

Returns the current

KeyboardFocusManager

instance
for the calling thread's context.

static boolean

isFocusManagerEnabled

()

Deprecated.

As of 1.4, replaced by

KeyboardFocusManager.getDefaultFocusTraversalPolicy()

static void

setCurrentManager

​(

FocusManager

aFocusManager)

Sets the current

KeyboardFocusManager

instance
for the calling thread's context.

- Methods declared in class java.awt.

DefaultKeyboardFocusManager

dequeueKeyEvents

,

discardKeyEvents

,

dispatchEvent

,

dispatchKeyEvent

,

downFocusCycle

,

enqueueKeyEvents

,

focusNextComponent

,

focusPreviousComponent

,

postProcessKeyEvent

,

processKeyEvent

,

upFocusCycle

- Methods declared in class java.awt.

KeyboardFocusManager

addKeyEventDispatcher

,

addKeyEventPostProcessor

,

addPropertyChangeListener

,

addPropertyChangeListener

,

addVetoableChangeListener

,

addVetoableChangeListener

,

clearFocusOwner

,

clearGlobalFocusOwner

,

downFocusCycle

,

firePropertyChange

,

fireVetoableChange

,

focusNextComponent

,

focusPreviousComponent

,

getActiveWindow

,

getCurrentFocusCycleRoot

,

getCurrentKeyboardFocusManager

,

getDefaultFocusTraversalKeys

,

getDefaultFocusTraversalPolicy

,

getFocusedWindow

,

getFocusOwner

,

getGlobalActiveWindow

,

getGlobalCurrentFocusCycleRoot

,

getGlobalFocusedWindow

,

getGlobalFocusOwner

,

getGlobalPermanentFocusOwner

,

getKeyEventDispatchers

,

getKeyEventPostProcessors

,

getPermanentFocusOwner

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getVetoableChangeListeners

,

getVetoableChangeListeners

,

redispatchEvent

,

removeKeyEventDispatcher

,

removeKeyEventPostProcessor

,

removePropertyChangeListener

,

removePropertyChangeListener

,

removeVetoableChangeListener

,

removeVetoableChangeListener

,

setCurrentKeyboardFocusManager

,

setDefaultFocusTraversalKeys

,

setDefaultFocusTraversalPolicy

,

setGlobalActiveWindow

,

setGlobalCurrentFocusCycleRoot

,

setGlobalFocusedWindow

,

setGlobalFocusOwner

,

setGlobalPermanentFocusOwner

,

upFocusCycle

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

static

String

FOCUS_MANAGER_CLASS_PROPERTY

This field is obsolete, and its use is discouraged since its
specification is incompatible with the 1.4 focus APIs.

- Fields declared in class java.awt.

KeyboardFocusManager

BACKWARD_TRAVERSAL_KEYS

,

DOWN_CYCLE_TRAVERSAL_KEYS

,

FORWARD_TRAVERSAL_KEYS

,

UP_CYCLE_TRAVERSAL_KEYS

---

#### Field Summary

This field is obsolete, and its use is discouraged since its
specification is incompatible with the 1.4 focus APIs.

Fields declared in class java.awt.

KeyboardFocusManager

BACKWARD_TRAVERSAL_KEYS

,

DOWN_CYCLE_TRAVERSAL_KEYS

,

FORWARD_TRAVERSAL_KEYS

,

UP_CYCLE_TRAVERSAL_KEYS

---

#### Fields declared in class java.awt. KeyboardFocusManager

Constructor Summary

Constructors

Constructor

Description

FocusManager

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static void

disableSwingFocusManager

()

Deprecated.

as of 1.4, replaced by

KeyboardFocusManager.setDefaultFocusTraversalPolicy(FocusTraversalPolicy)

static

FocusManager

getCurrentManager

()

Returns the current

KeyboardFocusManager

instance
for the calling thread's context.

static boolean

isFocusManagerEnabled

()

Deprecated.

As of 1.4, replaced by

KeyboardFocusManager.getDefaultFocusTraversalPolicy()

static void

setCurrentManager

​(

FocusManager

aFocusManager)

Sets the current

KeyboardFocusManager

instance
for the calling thread's context.

- Methods declared in class java.awt.

DefaultKeyboardFocusManager

dequeueKeyEvents

,

discardKeyEvents

,

dispatchEvent

,

dispatchKeyEvent

,

downFocusCycle

,

enqueueKeyEvents

,

focusNextComponent

,

focusPreviousComponent

,

postProcessKeyEvent

,

processKeyEvent

,

upFocusCycle

- Methods declared in class java.awt.

KeyboardFocusManager

addKeyEventDispatcher

,

addKeyEventPostProcessor

,

addPropertyChangeListener

,

addPropertyChangeListener

,

addVetoableChangeListener

,

addVetoableChangeListener

,

clearFocusOwner

,

clearGlobalFocusOwner

,

downFocusCycle

,

firePropertyChange

,

fireVetoableChange

,

focusNextComponent

,

focusPreviousComponent

,

getActiveWindow

,

getCurrentFocusCycleRoot

,

getCurrentKeyboardFocusManager

,

getDefaultFocusTraversalKeys

,

getDefaultFocusTraversalPolicy

,

getFocusedWindow

,

getFocusOwner

,

getGlobalActiveWindow

,

getGlobalCurrentFocusCycleRoot

,

getGlobalFocusedWindow

,

getGlobalFocusOwner

,

getGlobalPermanentFocusOwner

,

getKeyEventDispatchers

,

getKeyEventPostProcessors

,

getPermanentFocusOwner

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getVetoableChangeListeners

,

getVetoableChangeListeners

,

redispatchEvent

,

removeKeyEventDispatcher

,

removeKeyEventPostProcessor

,

removePropertyChangeListener

,

removePropertyChangeListener

,

removeVetoableChangeListener

,

removeVetoableChangeListener

,

setCurrentKeyboardFocusManager

,

setDefaultFocusTraversalKeys

,

setDefaultFocusTraversalPolicy

,

setGlobalActiveWindow

,

setGlobalCurrentFocusCycleRoot

,

setGlobalFocusedWindow

,

setGlobalFocusOwner

,

setGlobalPermanentFocusOwner

,

upFocusCycle

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Deprecated.

as of 1.4, replaced by

KeyboardFocusManager.setDefaultFocusTraversalPolicy(FocusTraversalPolicy)

Returns the current

KeyboardFocusManager

instance
for the calling thread's context.

Deprecated.

As of 1.4, replaced by

KeyboardFocusManager.getDefaultFocusTraversalPolicy()

Sets the current

KeyboardFocusManager

instance
for the calling thread's context.

Methods declared in class java.awt.

DefaultKeyboardFocusManager

dequeueKeyEvents

,

discardKeyEvents

,

dispatchEvent

,

dispatchKeyEvent

,

downFocusCycle

,

enqueueKeyEvents

,

focusNextComponent

,

focusPreviousComponent

,

postProcessKeyEvent

,

processKeyEvent

,

upFocusCycle

---

#### Methods declared in class java.awt. DefaultKeyboardFocusManager

Methods declared in class java.awt.

KeyboardFocusManager

addKeyEventDispatcher

,

addKeyEventPostProcessor

,

addPropertyChangeListener

,

addPropertyChangeListener

,

addVetoableChangeListener

,

addVetoableChangeListener

,

clearFocusOwner

,

clearGlobalFocusOwner

,

downFocusCycle

,

firePropertyChange

,

fireVetoableChange

,

focusNextComponent

,

focusPreviousComponent

,

getActiveWindow

,

getCurrentFocusCycleRoot

,

getCurrentKeyboardFocusManager

,

getDefaultFocusTraversalKeys

,

getDefaultFocusTraversalPolicy

,

getFocusedWindow

,

getFocusOwner

,

getGlobalActiveWindow

,

getGlobalCurrentFocusCycleRoot

,

getGlobalFocusedWindow

,

getGlobalFocusOwner

,

getGlobalPermanentFocusOwner

,

getKeyEventDispatchers

,

getKeyEventPostProcessors

,

getPermanentFocusOwner

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getVetoableChangeListeners

,

getVetoableChangeListeners

,

redispatchEvent

,

removeKeyEventDispatcher

,

removeKeyEventPostProcessor

,

removePropertyChangeListener

,

removePropertyChangeListener

,

removeVetoableChangeListener

,

removeVetoableChangeListener

,

setCurrentKeyboardFocusManager

,

setDefaultFocusTraversalKeys

,

setDefaultFocusTraversalPolicy

,

setGlobalActiveWindow

,

setGlobalCurrentFocusCycleRoot

,

setGlobalFocusedWindow

,

setGlobalFocusOwner

,

setGlobalPermanentFocusOwner

,

upFocusCycle

---

#### Methods declared in class java.awt. KeyboardFocusManager

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- FOCUS_MANAGER_CLASS_PROPERTY

```java
public static final
String
FOCUS_MANAGER_CLASS_PROPERTY
```

This field is obsolete, and its use is discouraged since its
specification is incompatible with the 1.4 focus APIs.
The current FocusManager is no longer a property of the UI.
Client code must query for the current FocusManager using

KeyboardFocusManager.getCurrentKeyboardFocusManager()

.
See the Focus Specification for more information.

**See Also:** KeyboardFocusManager.getCurrentKeyboardFocusManager()

,

Focus Specification

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FocusManager

```java
public FocusManager()
```

============ METHOD DETAIL ==========

- Method Detail

- getCurrentManager

```java
public static
FocusManager
getCurrentManager()
```

Returns the current

KeyboardFocusManager

instance
for the calling thread's context.

**Returns:** this thread's context's

KeyboardFocusManager
**See Also:** setCurrentManager(javax.swing.FocusManager)

- setCurrentManager

```java
public static void setCurrentManager​(
FocusManager
aFocusManager)
throws
SecurityException
```

Sets the current

KeyboardFocusManager

instance
for the calling thread's context. If

null

is
specified, then the current

KeyboardFocusManager

is replaced with a new instance of

DefaultKeyboardFocusManager

.

If a

SecurityManager

is installed,
the calling thread must be granted the

AWTPermission

"replaceKeyboardFocusManager" in order to replace the
the current

KeyboardFocusManager

.
If this permission is not granted,
this method will throw a

SecurityException

,
and the current

KeyboardFocusManager

will be unchanged.

**Parameters:** aFocusManager

- the new

KeyboardFocusManager

for this thread's context
**Throws:** SecurityException

- if the calling thread does not have permission
to replace the current

KeyboardFocusManager
**See Also:** getCurrentManager()

,

DefaultKeyboardFocusManager

- disableSwingFocusManager

```java
@Deprecated

public static void disableSwingFocusManager()
```

Deprecated.

as of 1.4, replaced by

KeyboardFocusManager.setDefaultFocusTraversalPolicy(FocusTraversalPolicy)

Changes the current

KeyboardFocusManager

's default

FocusTraversalPolicy

to

DefaultFocusTraversalPolicy

.

**See Also:** DefaultFocusTraversalPolicy

,

KeyboardFocusManager.setDefaultFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

- isFocusManagerEnabled

```java
@Deprecated

public static boolean isFocusManagerEnabled()
```

Deprecated.

As of 1.4, replaced by

KeyboardFocusManager.getDefaultFocusTraversalPolicy()

Returns whether the application has invoked

disableSwingFocusManager()

.

**Returns:** true

if focus manager is enabled.
**See Also:** disableSwingFocusManager()

Field Detail

- FOCUS_MANAGER_CLASS_PROPERTY

```java
public static final
String
FOCUS_MANAGER_CLASS_PROPERTY
```

This field is obsolete, and its use is discouraged since its
specification is incompatible with the 1.4 focus APIs.
The current FocusManager is no longer a property of the UI.
Client code must query for the current FocusManager using

KeyboardFocusManager.getCurrentKeyboardFocusManager()

.
See the Focus Specification for more information.

**See Also:** KeyboardFocusManager.getCurrentKeyboardFocusManager()

,

Focus Specification

,

Constant Field Values

---

#### Field Detail

FOCUS_MANAGER_CLASS_PROPERTY

```java
public static final
String
FOCUS_MANAGER_CLASS_PROPERTY
```

This field is obsolete, and its use is discouraged since its
specification is incompatible with the 1.4 focus APIs.
The current FocusManager is no longer a property of the UI.
Client code must query for the current FocusManager using

KeyboardFocusManager.getCurrentKeyboardFocusManager()

.
See the Focus Specification for more information.

**See Also:** KeyboardFocusManager.getCurrentKeyboardFocusManager()

,

Focus Specification

,

Constant Field Values

---

#### FOCUS_MANAGER_CLASS_PROPERTY

public static final

String

FOCUS_MANAGER_CLASS_PROPERTY

This field is obsolete, and its use is discouraged since its
specification is incompatible with the 1.4 focus APIs.
The current FocusManager is no longer a property of the UI.
Client code must query for the current FocusManager using

KeyboardFocusManager.getCurrentKeyboardFocusManager()

.
See the Focus Specification for more information.

Constructor Detail

- FocusManager

```java
public FocusManager()
```

---

#### Constructor Detail

FocusManager

```java
public FocusManager()
```

---

#### FocusManager

public FocusManager()

Method Detail

- getCurrentManager

```java
public static
FocusManager
getCurrentManager()
```

Returns the current

KeyboardFocusManager

instance
for the calling thread's context.

**Returns:** this thread's context's

KeyboardFocusManager
**See Also:** setCurrentManager(javax.swing.FocusManager)

- setCurrentManager

```java
public static void setCurrentManager​(
FocusManager
aFocusManager)
throws
SecurityException
```

Sets the current

KeyboardFocusManager

instance
for the calling thread's context. If

null

is
specified, then the current

KeyboardFocusManager

is replaced with a new instance of

DefaultKeyboardFocusManager

.

If a

SecurityManager

is installed,
the calling thread must be granted the

AWTPermission

"replaceKeyboardFocusManager" in order to replace the
the current

KeyboardFocusManager

.
If this permission is not granted,
this method will throw a

SecurityException

,
and the current

KeyboardFocusManager

will be unchanged.

**Parameters:** aFocusManager

- the new

KeyboardFocusManager

for this thread's context
**Throws:** SecurityException

- if the calling thread does not have permission
to replace the current

KeyboardFocusManager
**See Also:** getCurrentManager()

,

DefaultKeyboardFocusManager

- disableSwingFocusManager

```java
@Deprecated

public static void disableSwingFocusManager()
```

Deprecated.

as of 1.4, replaced by

KeyboardFocusManager.setDefaultFocusTraversalPolicy(FocusTraversalPolicy)

Changes the current

KeyboardFocusManager

's default

FocusTraversalPolicy

to

DefaultFocusTraversalPolicy

.

**See Also:** DefaultFocusTraversalPolicy

,

KeyboardFocusManager.setDefaultFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

- isFocusManagerEnabled

```java
@Deprecated

public static boolean isFocusManagerEnabled()
```

Deprecated.

As of 1.4, replaced by

KeyboardFocusManager.getDefaultFocusTraversalPolicy()

Returns whether the application has invoked

disableSwingFocusManager()

.

**Returns:** true

if focus manager is enabled.
**See Also:** disableSwingFocusManager()

---

#### Method Detail

getCurrentManager

```java
public static
FocusManager
getCurrentManager()
```

Returns the current

KeyboardFocusManager

instance
for the calling thread's context.

**Returns:** this thread's context's

KeyboardFocusManager
**See Also:** setCurrentManager(javax.swing.FocusManager)

---

#### getCurrentManager

public static

FocusManager

getCurrentManager()

Returns the current

KeyboardFocusManager

instance
for the calling thread's context.

setCurrentManager

```java
public static void setCurrentManager​(
FocusManager
aFocusManager)
throws
SecurityException
```

Sets the current

KeyboardFocusManager

instance
for the calling thread's context. If

null

is
specified, then the current

KeyboardFocusManager

is replaced with a new instance of

DefaultKeyboardFocusManager

.

If a

SecurityManager

is installed,
the calling thread must be granted the

AWTPermission

"replaceKeyboardFocusManager" in order to replace the
the current

KeyboardFocusManager

.
If this permission is not granted,
this method will throw a

SecurityException

,
and the current

KeyboardFocusManager

will be unchanged.

**Parameters:** aFocusManager

- the new

KeyboardFocusManager

for this thread's context
**Throws:** SecurityException

- if the calling thread does not have permission
to replace the current

KeyboardFocusManager
**See Also:** getCurrentManager()

,

DefaultKeyboardFocusManager

---

#### setCurrentManager

public static void setCurrentManager​(

FocusManager

aFocusManager)
throws

SecurityException

Sets the current

KeyboardFocusManager

instance
for the calling thread's context. If

null

is
specified, then the current

KeyboardFocusManager

is replaced with a new instance of

DefaultKeyboardFocusManager

.

If a

SecurityManager

is installed,
the calling thread must be granted the

AWTPermission

"replaceKeyboardFocusManager" in order to replace the
the current

KeyboardFocusManager

.
If this permission is not granted,
this method will throw a

SecurityException

,
and the current

KeyboardFocusManager

will be unchanged.

If a

SecurityManager

is installed,
the calling thread must be granted the

AWTPermission

"replaceKeyboardFocusManager" in order to replace the
the current

KeyboardFocusManager

.
If this permission is not granted,
this method will throw a

SecurityException

,
and the current

KeyboardFocusManager

will be unchanged.

disableSwingFocusManager

```java
@Deprecated

public static void disableSwingFocusManager()
```

Deprecated.

as of 1.4, replaced by

KeyboardFocusManager.setDefaultFocusTraversalPolicy(FocusTraversalPolicy)

Changes the current

KeyboardFocusManager

's default

FocusTraversalPolicy

to

DefaultFocusTraversalPolicy

.

**See Also:** DefaultFocusTraversalPolicy

,

KeyboardFocusManager.setDefaultFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

---

#### disableSwingFocusManager

@Deprecated

public static void disableSwingFocusManager()

Changes the current

KeyboardFocusManager

's default

FocusTraversalPolicy

to

DefaultFocusTraversalPolicy

.

isFocusManagerEnabled

```java
@Deprecated

public static boolean isFocusManagerEnabled()
```

Deprecated.

As of 1.4, replaced by

KeyboardFocusManager.getDefaultFocusTraversalPolicy()

Returns whether the application has invoked

disableSwingFocusManager()

.

**Returns:** true

if focus manager is enabled.
**See Also:** disableSwingFocusManager()

---

#### isFocusManagerEnabled

@Deprecated

public static boolean isFocusManagerEnabled()

Returns whether the application has invoked

disableSwingFocusManager()

.

---

