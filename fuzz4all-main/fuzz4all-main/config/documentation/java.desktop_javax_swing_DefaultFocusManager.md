# Class DefaultFocusManager

**Source:** `java.desktop\javax\swing\DefaultFocusManager.html`

### Class Description

```java
public class
DefaultFocusManager

extends
FocusManager
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

*No entries found.*

### Constructor Details

#### public DefaultFocusManager()

Constructs a

DefaultFocusManager

.

---

### Method Details

#### public
Component
getComponentAfter​(
Container
aContainer,

Component
aComponent)

Returns the component after.

**Parameters:**
- aContainer

- a container
- aComponent

- a component

**Returns:**
- the component after

---

#### public
Component
getComponentBefore​(
Container
aContainer,

Component
aComponent)

Returns the component before.

**Parameters:**
- aContainer

- a container
- aComponent

- a component

**Returns:**
- the component before

---

#### public
Component
getFirstComponent​(
Container
aContainer)

Returns the first component.

**Parameters:**
- aContainer

- a container

**Returns:**
- the first component

---

#### public
Component
getLastComponent​(
Container
aContainer)

Returns the last component.

**Parameters:**
- aContainer

- a container

**Returns:**
- the last component

---

#### public boolean compareTabOrder​(
Component
a,

Component
b)

Compares the components by their focus traversal cycle order.

**Parameters:**
- a

- the first component
- b

- the second component

**Returns:**
- a comparison of the components by their focus traversal cycle order

---

### Additional Sections

#### Class DefaultFocusManager

java.lang.Object

- java.awt.KeyboardFocusManager
- - java.awt.DefaultKeyboardFocusManager
- - javax.swing.FocusManager
- - javax.swing.DefaultFocusManager

java.awt.KeyboardFocusManager

- java.awt.DefaultKeyboardFocusManager
- - javax.swing.FocusManager
- - javax.swing.DefaultFocusManager

java.awt.DefaultKeyboardFocusManager

- javax.swing.FocusManager
- - javax.swing.DefaultFocusManager

javax.swing.FocusManager

- javax.swing.DefaultFocusManager

javax.swing.DefaultFocusManager

**All Implemented Interfaces:** KeyEventDispatcher

,

KeyEventPostProcessor

```java
public class
DefaultFocusManager

extends
FocusManager
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

public class

DefaultFocusManager

extends

FocusManager

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

- Fields declared in class javax.swing.

FocusManager

FOCUS_MANAGER_CLASS_PROPERTY

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

DefaultFocusManager

()

Constructs a

DefaultFocusManager

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

compareTabOrder

​(

Component

a,

Component

b)

Compares the components by their focus traversal cycle order.

Component

getComponentAfter

​(

Container

aContainer,

Component

aComponent)

Returns the component after.

Component

getComponentBefore

​(

Container

aContainer,

Component

aComponent)

Returns the component before.

Component

getFirstComponent

​(

Container

aContainer)

Returns the first component.

Component

getLastComponent

​(

Container

aContainer)

Returns the last component.

- Methods declared in class javax.swing.

FocusManager

disableSwingFocusManager

,

getCurrentManager

,

isFocusManagerEnabled

,

setCurrentManager

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

- Fields declared in class javax.swing.

FocusManager

FOCUS_MANAGER_CLASS_PROPERTY

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

Fields declared in class javax.swing.

FocusManager

FOCUS_MANAGER_CLASS_PROPERTY

---

#### Fields declared in class javax.swing. FocusManager

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

DefaultFocusManager

()

Constructs a

DefaultFocusManager

.

---

#### Constructor Summary

Constructs a

DefaultFocusManager

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

compareTabOrder

​(

Component

a,

Component

b)

Compares the components by their focus traversal cycle order.

Component

getComponentAfter

​(

Container

aContainer,

Component

aComponent)

Returns the component after.

Component

getComponentBefore

​(

Container

aContainer,

Component

aComponent)

Returns the component before.

Component

getFirstComponent

​(

Container

aContainer)

Returns the first component.

Component

getLastComponent

​(

Container

aContainer)

Returns the last component.

- Methods declared in class javax.swing.

FocusManager

disableSwingFocusManager

,

getCurrentManager

,

isFocusManagerEnabled

,

setCurrentManager

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

Compares the components by their focus traversal cycle order.

Returns the component after.

Returns the component before.

Returns the first component.

Returns the last component.

Methods declared in class javax.swing.

FocusManager

disableSwingFocusManager

,

getCurrentManager

,

isFocusManagerEnabled

,

setCurrentManager

---

#### Methods declared in class javax.swing. FocusManager

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultFocusManager

```java
public DefaultFocusManager()
```

Constructs a

DefaultFocusManager

.

============ METHOD DETAIL ==========

- Method Detail

- getComponentAfter

```java
public
Component
getComponentAfter​(
Container
aContainer,

Component
aComponent)
```

Returns the component after.

**Parameters:** aContainer

- a container
**Parameters:** aComponent

- a component
**Returns:** the component after

- getComponentBefore

```java
public
Component
getComponentBefore​(
Container
aContainer,

Component
aComponent)
```

Returns the component before.

**Parameters:** aContainer

- a container
**Parameters:** aComponent

- a component
**Returns:** the component before

- getFirstComponent

```java
public
Component
getFirstComponent​(
Container
aContainer)
```

Returns the first component.

**Parameters:** aContainer

- a container
**Returns:** the first component

- getLastComponent

```java
public
Component
getLastComponent​(
Container
aContainer)
```

Returns the last component.

**Parameters:** aContainer

- a container
**Returns:** the last component

- compareTabOrder

```java
public boolean compareTabOrder​(
Component
a,

Component
b)
```

Compares the components by their focus traversal cycle order.

**Parameters:** a

- the first component
**Parameters:** b

- the second component
**Returns:** a comparison of the components by their focus traversal cycle order

Constructor Detail

- DefaultFocusManager

```java
public DefaultFocusManager()
```

Constructs a

DefaultFocusManager

.

---

#### Constructor Detail

DefaultFocusManager

```java
public DefaultFocusManager()
```

Constructs a

DefaultFocusManager

.

---

#### DefaultFocusManager

public DefaultFocusManager()

Constructs a

DefaultFocusManager

.

Method Detail

- getComponentAfter

```java
public
Component
getComponentAfter​(
Container
aContainer,

Component
aComponent)
```

Returns the component after.

**Parameters:** aContainer

- a container
**Parameters:** aComponent

- a component
**Returns:** the component after

- getComponentBefore

```java
public
Component
getComponentBefore​(
Container
aContainer,

Component
aComponent)
```

Returns the component before.

**Parameters:** aContainer

- a container
**Parameters:** aComponent

- a component
**Returns:** the component before

- getFirstComponent

```java
public
Component
getFirstComponent​(
Container
aContainer)
```

Returns the first component.

**Parameters:** aContainer

- a container
**Returns:** the first component

- getLastComponent

```java
public
Component
getLastComponent​(
Container
aContainer)
```

Returns the last component.

**Parameters:** aContainer

- a container
**Returns:** the last component

- compareTabOrder

```java
public boolean compareTabOrder​(
Component
a,

Component
b)
```

Compares the components by their focus traversal cycle order.

**Parameters:** a

- the first component
**Parameters:** b

- the second component
**Returns:** a comparison of the components by their focus traversal cycle order

---

#### Method Detail

getComponentAfter

```java
public
Component
getComponentAfter​(
Container
aContainer,

Component
aComponent)
```

Returns the component after.

**Parameters:** aContainer

- a container
**Parameters:** aComponent

- a component
**Returns:** the component after

---

#### getComponentAfter

public

Component

getComponentAfter​(

Container

aContainer,

Component

aComponent)

Returns the component after.

getComponentBefore

```java
public
Component
getComponentBefore​(
Container
aContainer,

Component
aComponent)
```

Returns the component before.

**Parameters:** aContainer

- a container
**Parameters:** aComponent

- a component
**Returns:** the component before

---

#### getComponentBefore

public

Component

getComponentBefore​(

Container

aContainer,

Component

aComponent)

Returns the component before.

getFirstComponent

```java
public
Component
getFirstComponent​(
Container
aContainer)
```

Returns the first component.

**Parameters:** aContainer

- a container
**Returns:** the first component

---

#### getFirstComponent

public

Component

getFirstComponent​(

Container

aContainer)

Returns the first component.

getLastComponent

```java
public
Component
getLastComponent​(
Container
aContainer)
```

Returns the last component.

**Parameters:** aContainer

- a container
**Returns:** the last component

---

#### getLastComponent

public

Component

getLastComponent​(

Container

aContainer)

Returns the last component.

compareTabOrder

```java
public boolean compareTabOrder​(
Component
a,

Component
b)
```

Compares the components by their focus traversal cycle order.

**Parameters:** a

- the first component
**Parameters:** b

- the second component
**Returns:** a comparison of the components by their focus traversal cycle order

---

#### compareTabOrder

public boolean compareTabOrder​(

Component

a,

Component

b)

Compares the components by their focus traversal cycle order.

---

