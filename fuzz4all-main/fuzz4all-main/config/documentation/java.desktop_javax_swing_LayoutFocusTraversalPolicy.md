# Class LayoutFocusTraversalPolicy

**Source:** `java.desktop\javax\swing\LayoutFocusTraversalPolicy.html`

### Class Description

```java
public class
LayoutFocusTraversalPolicy

extends
SortingFocusTraversalPolicy

implements
Serializable
```

A SortingFocusTraversalPolicy which sorts Components based on their size,
position, and orientation. Based on their size and position, Components are
roughly categorized into rows and columns. For a Container with horizontal
orientation, columns run left-to-right or right-to-left, and rows run top-
to-bottom. For a Container with vertical orientation, columns run top-to-
bottom and rows run left-to-right or right-to-left. See

ComponentOrientation

for more information. All columns in a
row are fully traversed before proceeding to the next row.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public LayoutFocusTraversalPolicy()

Constructs a LayoutFocusTraversalPolicy.

---

### Method Details

#### public
Component
getComponentAfter​(
Container
aContainer,

Component
aComponent)

Returns the Component that should receive the focus after aComponent.
aContainer must be a focus cycle root of aComponent.

By default, LayoutFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Overrides:**
- getComponentAfter

in class

SortingFocusTraversalPolicy

**Parameters:**
- aContainer

- a focus cycle root of aComponent or a focus traversal policy provider
- aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself

**Returns:**
- the Component that should receive the focus after aComponent, or
null if no suitable Component can be found

**Throws:**
- IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if either aContainer or
aComponent is null

---

#### public
Component
getComponentBefore​(
Container
aContainer,

Component
aComponent)

Returns the Component that should receive the focus before aComponent.
aContainer must be a focus cycle root of aComponent.

By default, LayoutFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Overrides:**
- getComponentBefore

in class

SortingFocusTraversalPolicy

**Parameters:**
- aContainer

- a focus cycle root of aComponent or a focus traversal policy provider
- aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself

**Returns:**
- the Component that should receive the focus before aComponent,
or null if no suitable Component can be found

**Throws:**
- IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if either aContainer or
aComponent is null

---

#### public
Component
getFirstComponent​(
Container
aContainer)

Returns the first Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
forward direction.

**Overrides:**
- getFirstComponent

in class

SortingFocusTraversalPolicy

**Parameters:**
- aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
first Component is to be returned

**Returns:**
- the first Component in the traversal cycle of aContainer,
or null if no suitable Component can be found

**Throws:**
- IllegalArgumentException

- if aContainer is null

---

#### public
Component
getLastComponent​(
Container
aContainer)

Returns the last Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
reverse direction.

**Overrides:**
- getLastComponent

in class

SortingFocusTraversalPolicy

**Parameters:**
- aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
last Component is to be returned

**Returns:**
- the last Component in the traversal cycle of aContainer,
or null if no suitable Component can be found

**Throws:**
- IllegalArgumentException

- if aContainer is null

---

#### protected boolean accept​(
Component
aComponent)

Determines whether the specified

Component

is an acceptable choice as the new focus owner.
This method performs the following sequence of operations:

- Checks whether

aComponent

is visible, displayable,
enabled, and focusable. If any of these properties is

false

, this method returns

false

.

If

aComponent

is an instance of

JTable

,
returns

true

.

If

aComponent

is an instance of

JComboBox

,
then returns the value of

aComponent.getUI().isFocusTraversable(aComponent)

.

If

aComponent

is a

JComponent

with a

JComponent.WHEN_FOCUSED

InputMap

that is neither

null

nor empty, returns

true

.

Returns the value of

DefaultFocusTraversalPolicy.accept(aComponent)

.

**Overrides:**
- accept

in class

SortingFocusTraversalPolicy

**Parameters:**
- aComponent

- the

Component

whose fitness
as a focus owner is to be tested

**Returns:**
- true

if

aComponent

is a valid choice
for a focus owner;
otherwise

false

**See Also:**
- Component.isVisible()

,

Component.isDisplayable()

,

Component.isEnabled()

,

Component.isFocusable()

,

ComboBoxUI.isFocusTraversable(javax.swing.JComboBox<?>)

,

JComponent.getInputMap(int)

,

DefaultFocusTraversalPolicy.accept(java.awt.Component)

---

### Additional Sections

#### Class LayoutFocusTraversalPolicy

java.lang.Object

- java.awt.FocusTraversalPolicy
- - javax.swing.InternalFrameFocusTraversalPolicy
- - javax.swing.SortingFocusTraversalPolicy
- - javax.swing.LayoutFocusTraversalPolicy

java.awt.FocusTraversalPolicy

- javax.swing.InternalFrameFocusTraversalPolicy
- - javax.swing.SortingFocusTraversalPolicy
- - javax.swing.LayoutFocusTraversalPolicy

javax.swing.InternalFrameFocusTraversalPolicy

- javax.swing.SortingFocusTraversalPolicy
- - javax.swing.LayoutFocusTraversalPolicy

javax.swing.SortingFocusTraversalPolicy

- javax.swing.LayoutFocusTraversalPolicy

javax.swing.LayoutFocusTraversalPolicy

**All Implemented Interfaces:** Serializable

```java
public class
LayoutFocusTraversalPolicy

extends
SortingFocusTraversalPolicy

implements
Serializable
```

A SortingFocusTraversalPolicy which sorts Components based on their size,
position, and orientation. Based on their size and position, Components are
roughly categorized into rows and columns. For a Container with horizontal
orientation, columns run left-to-right or right-to-left, and rows run top-
to-bottom. For a Container with vertical orientation, columns run top-to-
bottom and rows run left-to-right or right-to-left. See

ComponentOrientation

for more information. All columns in a
row are fully traversed before proceeding to the next row.

**Since:** 1.4
**See Also:** ComponentOrientation

,

Serialized Form

public class

LayoutFocusTraversalPolicy

extends

SortingFocusTraversalPolicy

implements

Serializable

A SortingFocusTraversalPolicy which sorts Components based on their size,
position, and orientation. Based on their size and position, Components are
roughly categorized into rows and columns. For a Container with horizontal
orientation, columns run left-to-right or right-to-left, and rows run top-
to-bottom. For a Container with vertical orientation, columns run top-to-
bottom and rows run left-to-right or right-to-left. See

ComponentOrientation

for more information. All columns in a
row are fully traversed before proceeding to the next row.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LayoutFocusTraversalPolicy

()

Constructs a LayoutFocusTraversalPolicy.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected boolean

accept

​(

Component

aComponent)

Determines whether the specified

Component

is an acceptable choice as the new focus owner.

Component

getComponentAfter

​(

Container

aContainer,

Component

aComponent)

Returns the Component that should receive the focus after aComponent.

Component

getComponentBefore

​(

Container

aContainer,

Component

aComponent)

Returns the Component that should receive the focus before aComponent.

Component

getFirstComponent

​(

Container

aContainer)

Returns the first Component in the traversal cycle.

Component

getLastComponent

​(

Container

aContainer)

Returns the last Component in the traversal cycle.

- Methods declared in class javax.swing.

SortingFocusTraversalPolicy

getComparator

,

getDefaultComponent

,

getImplicitDownCycleTraversal

,

setComparator

,

setImplicitDownCycleTraversal

- Methods declared in class javax.swing.

InternalFrameFocusTraversalPolicy

getInitialComponent

- Methods declared in class java.awt.

FocusTraversalPolicy

getInitialComponent

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

Constructor Summary

Constructors

Constructor

Description

LayoutFocusTraversalPolicy

()

Constructs a LayoutFocusTraversalPolicy.

---

#### Constructor Summary

Constructs a LayoutFocusTraversalPolicy.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected boolean

accept

​(

Component

aComponent)

Determines whether the specified

Component

is an acceptable choice as the new focus owner.

Component

getComponentAfter

​(

Container

aContainer,

Component

aComponent)

Returns the Component that should receive the focus after aComponent.

Component

getComponentBefore

​(

Container

aContainer,

Component

aComponent)

Returns the Component that should receive the focus before aComponent.

Component

getFirstComponent

​(

Container

aContainer)

Returns the first Component in the traversal cycle.

Component

getLastComponent

​(

Container

aContainer)

Returns the last Component in the traversal cycle.

- Methods declared in class javax.swing.

SortingFocusTraversalPolicy

getComparator

,

getDefaultComponent

,

getImplicitDownCycleTraversal

,

setComparator

,

setImplicitDownCycleTraversal

- Methods declared in class javax.swing.

InternalFrameFocusTraversalPolicy

getInitialComponent

- Methods declared in class java.awt.

FocusTraversalPolicy

getInitialComponent

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

Determines whether the specified

Component

is an acceptable choice as the new focus owner.

Returns the Component that should receive the focus after aComponent.

Returns the Component that should receive the focus before aComponent.

Returns the first Component in the traversal cycle.

Returns the last Component in the traversal cycle.

Methods declared in class javax.swing.

SortingFocusTraversalPolicy

getComparator

,

getDefaultComponent

,

getImplicitDownCycleTraversal

,

setComparator

,

setImplicitDownCycleTraversal

---

#### Methods declared in class javax.swing. SortingFocusTraversalPolicy

Methods declared in class javax.swing.

InternalFrameFocusTraversalPolicy

getInitialComponent

---

#### Methods declared in class javax.swing. InternalFrameFocusTraversalPolicy

Methods declared in class java.awt.

FocusTraversalPolicy

getInitialComponent

---

#### Methods declared in class java.awt. FocusTraversalPolicy

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

- LayoutFocusTraversalPolicy

```java
public LayoutFocusTraversalPolicy()
```

Constructs a LayoutFocusTraversalPolicy.

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

Returns the Component that should receive the focus after aComponent.
aContainer must be a focus cycle root of aComponent.

By default, LayoutFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Overrides:** getComponentAfter

in class

SortingFocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider
**Parameters:** aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself
**Returns:** the Component that should receive the focus after aComponent, or
null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if either aContainer or
aComponent is null

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

Returns the Component that should receive the focus before aComponent.
aContainer must be a focus cycle root of aComponent.

By default, LayoutFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Overrides:** getComponentBefore

in class

SortingFocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider
**Parameters:** aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself
**Returns:** the Component that should receive the focus before aComponent,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if either aContainer or
aComponent is null

- getFirstComponent

```java
public
Component
getFirstComponent​(
Container
aContainer)
```

Returns the first Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
forward direction.

**Overrides:** getFirstComponent

in class

SortingFocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
first Component is to be returned
**Returns:** the first Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

- getLastComponent

```java
public
Component
getLastComponent​(
Container
aContainer)
```

Returns the last Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
reverse direction.

**Overrides:** getLastComponent

in class

SortingFocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
last Component is to be returned
**Returns:** the last Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

- accept

```java
protected boolean accept​(
Component
aComponent)
```

Determines whether the specified

Component

is an acceptable choice as the new focus owner.
This method performs the following sequence of operations:

- Checks whether

aComponent

is visible, displayable,
enabled, and focusable. If any of these properties is

false

, this method returns

false

.

If

aComponent

is an instance of

JTable

,
returns

true

.

If

aComponent

is an instance of

JComboBox

,
then returns the value of

aComponent.getUI().isFocusTraversable(aComponent)

.

If

aComponent

is a

JComponent

with a

JComponent.WHEN_FOCUSED

InputMap

that is neither

null

nor empty, returns

true

.

Returns the value of

DefaultFocusTraversalPolicy.accept(aComponent)

.

**Overrides:** accept

in class

SortingFocusTraversalPolicy
**Parameters:** aComponent

- the

Component

whose fitness
as a focus owner is to be tested
**Returns:** true

if

aComponent

is a valid choice
for a focus owner;
otherwise

false
**See Also:** Component.isVisible()

,

Component.isDisplayable()

,

Component.isEnabled()

,

Component.isFocusable()

,

ComboBoxUI.isFocusTraversable(javax.swing.JComboBox<?>)

,

JComponent.getInputMap(int)

,

DefaultFocusTraversalPolicy.accept(java.awt.Component)

Constructor Detail

- LayoutFocusTraversalPolicy

```java
public LayoutFocusTraversalPolicy()
```

Constructs a LayoutFocusTraversalPolicy.

---

#### Constructor Detail

LayoutFocusTraversalPolicy

```java
public LayoutFocusTraversalPolicy()
```

Constructs a LayoutFocusTraversalPolicy.

---

#### LayoutFocusTraversalPolicy

public LayoutFocusTraversalPolicy()

Constructs a LayoutFocusTraversalPolicy.

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

Returns the Component that should receive the focus after aComponent.
aContainer must be a focus cycle root of aComponent.

By default, LayoutFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Overrides:** getComponentAfter

in class

SortingFocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider
**Parameters:** aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself
**Returns:** the Component that should receive the focus after aComponent, or
null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if either aContainer or
aComponent is null

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

Returns the Component that should receive the focus before aComponent.
aContainer must be a focus cycle root of aComponent.

By default, LayoutFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Overrides:** getComponentBefore

in class

SortingFocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider
**Parameters:** aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself
**Returns:** the Component that should receive the focus before aComponent,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if either aContainer or
aComponent is null

- getFirstComponent

```java
public
Component
getFirstComponent​(
Container
aContainer)
```

Returns the first Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
forward direction.

**Overrides:** getFirstComponent

in class

SortingFocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
first Component is to be returned
**Returns:** the first Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

- getLastComponent

```java
public
Component
getLastComponent​(
Container
aContainer)
```

Returns the last Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
reverse direction.

**Overrides:** getLastComponent

in class

SortingFocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
last Component is to be returned
**Returns:** the last Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

- accept

```java
protected boolean accept​(
Component
aComponent)
```

Determines whether the specified

Component

is an acceptable choice as the new focus owner.
This method performs the following sequence of operations:

- Checks whether

aComponent

is visible, displayable,
enabled, and focusable. If any of these properties is

false

, this method returns

false

.

If

aComponent

is an instance of

JTable

,
returns

true

.

If

aComponent

is an instance of

JComboBox

,
then returns the value of

aComponent.getUI().isFocusTraversable(aComponent)

.

If

aComponent

is a

JComponent

with a

JComponent.WHEN_FOCUSED

InputMap

that is neither

null

nor empty, returns

true

.

Returns the value of

DefaultFocusTraversalPolicy.accept(aComponent)

.

**Overrides:** accept

in class

SortingFocusTraversalPolicy
**Parameters:** aComponent

- the

Component

whose fitness
as a focus owner is to be tested
**Returns:** true

if

aComponent

is a valid choice
for a focus owner;
otherwise

false
**See Also:** Component.isVisible()

,

Component.isDisplayable()

,

Component.isEnabled()

,

Component.isFocusable()

,

ComboBoxUI.isFocusTraversable(javax.swing.JComboBox<?>)

,

JComponent.getInputMap(int)

,

DefaultFocusTraversalPolicy.accept(java.awt.Component)

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

Returns the Component that should receive the focus after aComponent.
aContainer must be a focus cycle root of aComponent.

By default, LayoutFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Overrides:** getComponentAfter

in class

SortingFocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider
**Parameters:** aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself
**Returns:** the Component that should receive the focus after aComponent, or
null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if either aContainer or
aComponent is null

---

#### getComponentAfter

public

Component

getComponentAfter​(

Container

aContainer,

Component

aComponent)

Returns the Component that should receive the focus after aComponent.
aContainer must be a focus cycle root of aComponent.

By default, LayoutFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

By default, LayoutFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

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

Returns the Component that should receive the focus before aComponent.
aContainer must be a focus cycle root of aComponent.

By default, LayoutFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Overrides:** getComponentBefore

in class

SortingFocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider
**Parameters:** aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself
**Returns:** the Component that should receive the focus before aComponent,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if either aContainer or
aComponent is null

---

#### getComponentBefore

public

Component

getComponentBefore​(

Container

aContainer,

Component

aComponent)

Returns the Component that should receive the focus before aComponent.
aContainer must be a focus cycle root of aComponent.

By default, LayoutFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

By default, LayoutFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

getFirstComponent

```java
public
Component
getFirstComponent​(
Container
aContainer)
```

Returns the first Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
forward direction.

**Overrides:** getFirstComponent

in class

SortingFocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
first Component is to be returned
**Returns:** the first Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

---

#### getFirstComponent

public

Component

getFirstComponent​(

Container

aContainer)

Returns the first Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
forward direction.

getLastComponent

```java
public
Component
getLastComponent​(
Container
aContainer)
```

Returns the last Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
reverse direction.

**Overrides:** getLastComponent

in class

SortingFocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
last Component is to be returned
**Returns:** the last Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

---

#### getLastComponent

public

Component

getLastComponent​(

Container

aContainer)

Returns the last Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
reverse direction.

accept

```java
protected boolean accept​(
Component
aComponent)
```

Determines whether the specified

Component

is an acceptable choice as the new focus owner.
This method performs the following sequence of operations:

- Checks whether

aComponent

is visible, displayable,
enabled, and focusable. If any of these properties is

false

, this method returns

false

.

If

aComponent

is an instance of

JTable

,
returns

true

.

If

aComponent

is an instance of

JComboBox

,
then returns the value of

aComponent.getUI().isFocusTraversable(aComponent)

.

If

aComponent

is a

JComponent

with a

JComponent.WHEN_FOCUSED

InputMap

that is neither

null

nor empty, returns

true

.

Returns the value of

DefaultFocusTraversalPolicy.accept(aComponent)

.

**Overrides:** accept

in class

SortingFocusTraversalPolicy
**Parameters:** aComponent

- the

Component

whose fitness
as a focus owner is to be tested
**Returns:** true

if

aComponent

is a valid choice
for a focus owner;
otherwise

false
**See Also:** Component.isVisible()

,

Component.isDisplayable()

,

Component.isEnabled()

,

Component.isFocusable()

,

ComboBoxUI.isFocusTraversable(javax.swing.JComboBox<?>)

,

JComponent.getInputMap(int)

,

DefaultFocusTraversalPolicy.accept(java.awt.Component)

---

#### accept

protected boolean accept​(

Component

aComponent)

Determines whether the specified

Component

is an acceptable choice as the new focus owner.
This method performs the following sequence of operations:

- Checks whether

aComponent

is visible, displayable,
enabled, and focusable. If any of these properties is

false

, this method returns

false

.

If

aComponent

is an instance of

JTable

,
returns

true

.

If

aComponent

is an instance of

JComboBox

,
then returns the value of

aComponent.getUI().isFocusTraversable(aComponent)

.

If

aComponent

is a

JComponent

with a

JComponent.WHEN_FOCUSED

InputMap

that is neither

null

nor empty, returns

true

.

Returns the value of

DefaultFocusTraversalPolicy.accept(aComponent)

.

Checks whether

aComponent

is visible, displayable,
enabled, and focusable. If any of these properties is

false

, this method returns

false

.

If

aComponent

is an instance of

JTable

,
returns

true

.

If

aComponent

is an instance of

JComboBox

,
then returns the value of

aComponent.getUI().isFocusTraversable(aComponent)

.

If

aComponent

is a

JComponent

with a

JComponent.WHEN_FOCUSED

InputMap

that is neither

null

nor empty, returns

true

.

Returns the value of

DefaultFocusTraversalPolicy.accept(aComponent)

.

---

