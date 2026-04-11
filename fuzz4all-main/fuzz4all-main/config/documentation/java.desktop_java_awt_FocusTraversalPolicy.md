# Class FocusTraversalPolicy

**Source:** `java.desktop\java\awt\FocusTraversalPolicy.html`

### Class Description

```java
public abstract class
FocusTraversalPolicy

extends
Object
```

A FocusTraversalPolicy defines the order in which Components with a
particular focus cycle root are traversed. Instances can apply the policy to
arbitrary focus cycle roots, allowing themselves to be shared across
Containers. They do not need to be reinitialized when the focus cycle roots
of a Component hierarchy change.

The core responsibility of a FocusTraversalPolicy is to provide algorithms
determining the next and previous Components to focus when traversing
forward or backward in a UI. Each FocusTraversalPolicy must also provide
algorithms for determining the first, last, and default Components in a
traversal cycle. First and last Components are used when normal forward and
backward traversal, respectively, wraps. The default Component is the first
to receive focus when traversing down into a new focus traversal cycle.
A FocusTraversalPolicy can optionally provide an algorithm for determining
a Window's initial Component. The initial Component is the first to receive
focus when a Window is first made visible.

FocusTraversalPolicy takes into account

focus traversal
policy providers

. When searching for first/last/next/previous Component,
if a focus traversal policy provider is encountered, its focus traversal
policy is used to perform the search operation.

Please see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

**Direct Known Subclasses:** ContainerOrderFocusTraversalPolicy

,

InternalFrameFocusTraversalPolicy

---

### Field Details

*No entries found.*

### Constructor Details

#### public FocusTraversalPolicy()

*No description found.*

---

### Method Details

#### public abstract
Component
getComponentAfter​(
Container
aContainer,

Component
aComponent)

Returns the Component that should receive the focus after aComponent.
aContainer must be a focus cycle root of aComponent or a focus traversal
policy provider.

**Parameters:**
- aContainer

- a focus cycle root of aComponent or focus traversal
policy provider
- aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself

**Returns:**
- the Component that should receive the focus after aComponent, or
null if no suitable Component can be found

**Throws:**
- IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if
either aContainer or aComponent is null

---

#### public abstract
Component
getComponentBefore​(
Container
aContainer,

Component
aComponent)

Returns the Component that should receive the focus before aComponent.
aContainer must be a focus cycle root of aComponent or a focus traversal
policy provider.

**Parameters:**
- aContainer

- a focus cycle root of aComponent or focus traversal
policy provider
- aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself

**Returns:**
- the Component that should receive the focus before aComponent,
or null if no suitable Component can be found

**Throws:**
- IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if
either aContainer or aComponent is null

---

#### public abstract
Component
getFirstComponent​(
Container
aContainer)

Returns the first Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
forward direction.

**Parameters:**
- aContainer

- the focus cycle root or focus traversal policy provider
whose first Component is to be returned

**Returns:**
- the first Component in the traversal cycle of aContainer,
or null if no suitable Component can be found

**Throws:**
- IllegalArgumentException

- if aContainer is null

---

#### public abstract
Component
getLastComponent​(
Container
aContainer)

Returns the last Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
reverse direction.

**Parameters:**
- aContainer

- the focus cycle root or focus traversal policy
provider whose last Component is to be returned

**Returns:**
- the last Component in the traversal cycle of aContainer,
or null if no suitable Component can be found

**Throws:**
- IllegalArgumentException

- if aContainer is null

---

#### public abstract
Component
getDefaultComponent​(
Container
aContainer)

Returns the default Component to focus. This Component will be the first
to receive focus when traversing down into a new focus traversal cycle
rooted at aContainer.

**Parameters:**
- aContainer

- the focus cycle root or focus traversal policy
provider whose default Component is to be returned

**Returns:**
- the default Component in the traversal cycle of aContainer,
or null if no suitable Component can be found

**Throws:**
- IllegalArgumentException

- if aContainer is null

---

#### public
Component
getInitialComponent​(
Window
window)

Returns the Component that should receive the focus when a Window is
made visible for the first time. Once the Window has been made visible
by a call to

show()

or

setVisible(true)

, the
initial Component will not be used again. Instead, if the Window loses
and subsequently regains focus, or is made invisible or undisplayable
and subsequently made visible and displayable, the Window's most
recently focused Component will become the focus owner. The default
implementation of this method returns the default Component.

**Parameters:**
- window

- the Window whose initial Component is to be returned

**Returns:**
- the Component that should receive the focus when window is made
visible for the first time, or null if no suitable Component can
be found

**Throws:**
- IllegalArgumentException

- if window is null

**See Also:**
- getDefaultComponent(java.awt.Container)

,

Window.getMostRecentFocusOwner()

---

### Additional Sections

#### Class FocusTraversalPolicy

java.lang.Object

- java.awt.FocusTraversalPolicy

java.awt.FocusTraversalPolicy

**Direct Known Subclasses:** ContainerOrderFocusTraversalPolicy

,

InternalFrameFocusTraversalPolicy

```java
public abstract class
FocusTraversalPolicy

extends
Object
```

A FocusTraversalPolicy defines the order in which Components with a
particular focus cycle root are traversed. Instances can apply the policy to
arbitrary focus cycle roots, allowing themselves to be shared across
Containers. They do not need to be reinitialized when the focus cycle roots
of a Component hierarchy change.

The core responsibility of a FocusTraversalPolicy is to provide algorithms
determining the next and previous Components to focus when traversing
forward or backward in a UI. Each FocusTraversalPolicy must also provide
algorithms for determining the first, last, and default Components in a
traversal cycle. First and last Components are used when normal forward and
backward traversal, respectively, wraps. The default Component is the first
to receive focus when traversing down into a new focus traversal cycle.
A FocusTraversalPolicy can optionally provide an algorithm for determining
a Window's initial Component. The initial Component is the first to receive
focus when a Window is first made visible.

FocusTraversalPolicy takes into account

focus traversal
policy providers

. When searching for first/last/next/previous Component,
if a focus traversal policy provider is encountered, its focus traversal
policy is used to perform the search operation.

Please see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

**Since:** 1.4
**See Also:** Container.setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

Container.getFocusTraversalPolicy()

,

Container.setFocusCycleRoot(boolean)

,

Container.isFocusCycleRoot(java.awt.Container)

,

Container.setFocusTraversalPolicyProvider(boolean)

,

Container.isFocusTraversalPolicyProvider()

,

KeyboardFocusManager.setDefaultFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

KeyboardFocusManager.getDefaultFocusTraversalPolicy()

public abstract class

FocusTraversalPolicy

extends

Object

A FocusTraversalPolicy defines the order in which Components with a
particular focus cycle root are traversed. Instances can apply the policy to
arbitrary focus cycle roots, allowing themselves to be shared across
Containers. They do not need to be reinitialized when the focus cycle roots
of a Component hierarchy change.

The core responsibility of a FocusTraversalPolicy is to provide algorithms
determining the next and previous Components to focus when traversing
forward or backward in a UI. Each FocusTraversalPolicy must also provide
algorithms for determining the first, last, and default Components in a
traversal cycle. First and last Components are used when normal forward and
backward traversal, respectively, wraps. The default Component is the first
to receive focus when traversing down into a new focus traversal cycle.
A FocusTraversalPolicy can optionally provide an algorithm for determining
a Window's initial Component. The initial Component is the first to receive
focus when a Window is first made visible.

FocusTraversalPolicy takes into account

focus traversal
policy providers

. When searching for first/last/next/previous Component,
if a focus traversal policy provider is encountered, its focus traversal
policy is used to perform the search operation.

Please see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

The core responsibility of a FocusTraversalPolicy is to provide algorithms
determining the next and previous Components to focus when traversing
forward or backward in a UI. Each FocusTraversalPolicy must also provide
algorithms for determining the first, last, and default Components in a
traversal cycle. First and last Components are used when normal forward and
backward traversal, respectively, wraps. The default Component is the first
to receive focus when traversing down into a new focus traversal cycle.
A FocusTraversalPolicy can optionally provide an algorithm for determining
a Window's initial Component. The initial Component is the first to receive
focus when a Window is first made visible.

FocusTraversalPolicy takes into account

focus traversal
policy providers

. When searching for first/last/next/previous Component,
if a focus traversal policy provider is encountered, its focus traversal
policy is used to perform the search operation.

Please see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

FocusTraversalPolicy takes into account

focus traversal
policy providers

. When searching for first/last/next/previous Component,
if a focus traversal policy provider is encountered, its focus traversal
policy is used to perform the search operation.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FocusTraversalPolicy

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Component

getComponentAfter

​(

Container

aContainer,

Component

aComponent)

Returns the Component that should receive the focus after aComponent.

abstract

Component

getComponentBefore

​(

Container

aContainer,

Component

aComponent)

Returns the Component that should receive the focus before aComponent.

abstract

Component

getDefaultComponent

​(

Container

aContainer)

Returns the default Component to focus.

abstract

Component

getFirstComponent

​(

Container

aContainer)

Returns the first Component in the traversal cycle.

Component

getInitialComponent

​(

Window

window)

Returns the Component that should receive the focus when a Window is
made visible for the first time.

abstract

Component

getLastComponent

​(

Container

aContainer)

Returns the last Component in the traversal cycle.

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

FocusTraversalPolicy

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Component

getComponentAfter

​(

Container

aContainer,

Component

aComponent)

Returns the Component that should receive the focus after aComponent.

abstract

Component

getComponentBefore

​(

Container

aContainer,

Component

aComponent)

Returns the Component that should receive the focus before aComponent.

abstract

Component

getDefaultComponent

​(

Container

aContainer)

Returns the default Component to focus.

abstract

Component

getFirstComponent

​(

Container

aContainer)

Returns the first Component in the traversal cycle.

Component

getInitialComponent

​(

Window

window)

Returns the Component that should receive the focus when a Window is
made visible for the first time.

abstract

Component

getLastComponent

​(

Container

aContainer)

Returns the last Component in the traversal cycle.

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

Returns the Component that should receive the focus after aComponent.

Returns the Component that should receive the focus before aComponent.

Returns the default Component to focus.

Returns the first Component in the traversal cycle.

Returns the Component that should receive the focus when a Window is
made visible for the first time.

Returns the last Component in the traversal cycle.

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

- FocusTraversalPolicy

```java
public FocusTraversalPolicy()
```

============ METHOD DETAIL ==========

- Method Detail

- getComponentAfter

```java
public abstract
Component
getComponentAfter​(
Container
aContainer,

Component
aComponent)
```

Returns the Component that should receive the focus after aComponent.
aContainer must be a focus cycle root of aComponent or a focus traversal
policy provider.

**Parameters:** aContainer

- a focus cycle root of aComponent or focus traversal
policy provider
**Parameters:** aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself
**Returns:** the Component that should receive the focus after aComponent, or
null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if
either aContainer or aComponent is null

- getComponentBefore

```java
public abstract
Component
getComponentBefore​(
Container
aContainer,

Component
aComponent)
```

Returns the Component that should receive the focus before aComponent.
aContainer must be a focus cycle root of aComponent or a focus traversal
policy provider.

**Parameters:** aContainer

- a focus cycle root of aComponent or focus traversal
policy provider
**Parameters:** aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself
**Returns:** the Component that should receive the focus before aComponent,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if
either aContainer or aComponent is null

- getFirstComponent

```java
public abstract
Component
getFirstComponent​(
Container
aContainer)
```

Returns the first Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
forward direction.

**Parameters:** aContainer

- the focus cycle root or focus traversal policy provider
whose first Component is to be returned
**Returns:** the first Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

- getLastComponent

```java
public abstract
Component
getLastComponent​(
Container
aContainer)
```

Returns the last Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
reverse direction.

**Parameters:** aContainer

- the focus cycle root or focus traversal policy
provider whose last Component is to be returned
**Returns:** the last Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

- getDefaultComponent

```java
public abstract
Component
getDefaultComponent​(
Container
aContainer)
```

Returns the default Component to focus. This Component will be the first
to receive focus when traversing down into a new focus traversal cycle
rooted at aContainer.

**Parameters:** aContainer

- the focus cycle root or focus traversal policy
provider whose default Component is to be returned
**Returns:** the default Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

- getInitialComponent

```java
public
Component
getInitialComponent​(
Window
window)
```

Returns the Component that should receive the focus when a Window is
made visible for the first time. Once the Window has been made visible
by a call to

show()

or

setVisible(true)

, the
initial Component will not be used again. Instead, if the Window loses
and subsequently regains focus, or is made invisible or undisplayable
and subsequently made visible and displayable, the Window's most
recently focused Component will become the focus owner. The default
implementation of this method returns the default Component.

**Parameters:** window

- the Window whose initial Component is to be returned
**Returns:** the Component that should receive the focus when window is made
visible for the first time, or null if no suitable Component can
be found
**Throws:** IllegalArgumentException

- if window is null
**See Also:** getDefaultComponent(java.awt.Container)

,

Window.getMostRecentFocusOwner()

Constructor Detail

- FocusTraversalPolicy

```java
public FocusTraversalPolicy()
```

---

#### Constructor Detail

FocusTraversalPolicy

```java
public FocusTraversalPolicy()
```

---

#### FocusTraversalPolicy

public FocusTraversalPolicy()

Method Detail

- getComponentAfter

```java
public abstract
Component
getComponentAfter​(
Container
aContainer,

Component
aComponent)
```

Returns the Component that should receive the focus after aComponent.
aContainer must be a focus cycle root of aComponent or a focus traversal
policy provider.

**Parameters:** aContainer

- a focus cycle root of aComponent or focus traversal
policy provider
**Parameters:** aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself
**Returns:** the Component that should receive the focus after aComponent, or
null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if
either aContainer or aComponent is null

- getComponentBefore

```java
public abstract
Component
getComponentBefore​(
Container
aContainer,

Component
aComponent)
```

Returns the Component that should receive the focus before aComponent.
aContainer must be a focus cycle root of aComponent or a focus traversal
policy provider.

**Parameters:** aContainer

- a focus cycle root of aComponent or focus traversal
policy provider
**Parameters:** aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself
**Returns:** the Component that should receive the focus before aComponent,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if
either aContainer or aComponent is null

- getFirstComponent

```java
public abstract
Component
getFirstComponent​(
Container
aContainer)
```

Returns the first Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
forward direction.

**Parameters:** aContainer

- the focus cycle root or focus traversal policy provider
whose first Component is to be returned
**Returns:** the first Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

- getLastComponent

```java
public abstract
Component
getLastComponent​(
Container
aContainer)
```

Returns the last Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
reverse direction.

**Parameters:** aContainer

- the focus cycle root or focus traversal policy
provider whose last Component is to be returned
**Returns:** the last Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

- getDefaultComponent

```java
public abstract
Component
getDefaultComponent​(
Container
aContainer)
```

Returns the default Component to focus. This Component will be the first
to receive focus when traversing down into a new focus traversal cycle
rooted at aContainer.

**Parameters:** aContainer

- the focus cycle root or focus traversal policy
provider whose default Component is to be returned
**Returns:** the default Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

- getInitialComponent

```java
public
Component
getInitialComponent​(
Window
window)
```

Returns the Component that should receive the focus when a Window is
made visible for the first time. Once the Window has been made visible
by a call to

show()

or

setVisible(true)

, the
initial Component will not be used again. Instead, if the Window loses
and subsequently regains focus, or is made invisible or undisplayable
and subsequently made visible and displayable, the Window's most
recently focused Component will become the focus owner. The default
implementation of this method returns the default Component.

**Parameters:** window

- the Window whose initial Component is to be returned
**Returns:** the Component that should receive the focus when window is made
visible for the first time, or null if no suitable Component can
be found
**Throws:** IllegalArgumentException

- if window is null
**See Also:** getDefaultComponent(java.awt.Container)

,

Window.getMostRecentFocusOwner()

---

#### Method Detail

getComponentAfter

```java
public abstract
Component
getComponentAfter​(
Container
aContainer,

Component
aComponent)
```

Returns the Component that should receive the focus after aComponent.
aContainer must be a focus cycle root of aComponent or a focus traversal
policy provider.

**Parameters:** aContainer

- a focus cycle root of aComponent or focus traversal
policy provider
**Parameters:** aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself
**Returns:** the Component that should receive the focus after aComponent, or
null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if
either aContainer or aComponent is null

---

#### getComponentAfter

public abstract

Component

getComponentAfter​(

Container

aContainer,

Component

aComponent)

Returns the Component that should receive the focus after aComponent.
aContainer must be a focus cycle root of aComponent or a focus traversal
policy provider.

getComponentBefore

```java
public abstract
Component
getComponentBefore​(
Container
aContainer,

Component
aComponent)
```

Returns the Component that should receive the focus before aComponent.
aContainer must be a focus cycle root of aComponent or a focus traversal
policy provider.

**Parameters:** aContainer

- a focus cycle root of aComponent or focus traversal
policy provider
**Parameters:** aComponent

- a (possibly indirect) child of aContainer, or
aContainer itself
**Returns:** the Component that should receive the focus before aComponent,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is not a focus cycle
root of aComponent or a focus traversal policy provider, or if
either aContainer or aComponent is null

---

#### getComponentBefore

public abstract

Component

getComponentBefore​(

Container

aContainer,

Component

aComponent)

Returns the Component that should receive the focus before aComponent.
aContainer must be a focus cycle root of aComponent or a focus traversal
policy provider.

getFirstComponent

```java
public abstract
Component
getFirstComponent​(
Container
aContainer)
```

Returns the first Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
forward direction.

**Parameters:** aContainer

- the focus cycle root or focus traversal policy provider
whose first Component is to be returned
**Returns:** the first Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

---

#### getFirstComponent

public abstract

Component

getFirstComponent​(

Container

aContainer)

Returns the first Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
forward direction.

getLastComponent

```java
public abstract
Component
getLastComponent​(
Container
aContainer)
```

Returns the last Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
reverse direction.

**Parameters:** aContainer

- the focus cycle root or focus traversal policy
provider whose last Component is to be returned
**Returns:** the last Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

---

#### getLastComponent

public abstract

Component

getLastComponent​(

Container

aContainer)

Returns the last Component in the traversal cycle. This method is used
to determine the next Component to focus when traversal wraps in the
reverse direction.

getDefaultComponent

```java
public abstract
Component
getDefaultComponent​(
Container
aContainer)
```

Returns the default Component to focus. This Component will be the first
to receive focus when traversing down into a new focus traversal cycle
rooted at aContainer.

**Parameters:** aContainer

- the focus cycle root or focus traversal policy
provider whose default Component is to be returned
**Returns:** the default Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

---

#### getDefaultComponent

public abstract

Component

getDefaultComponent​(

Container

aContainer)

Returns the default Component to focus. This Component will be the first
to receive focus when traversing down into a new focus traversal cycle
rooted at aContainer.

getInitialComponent

```java
public
Component
getInitialComponent​(
Window
window)
```

Returns the Component that should receive the focus when a Window is
made visible for the first time. Once the Window has been made visible
by a call to

show()

or

setVisible(true)

, the
initial Component will not be used again. Instead, if the Window loses
and subsequently regains focus, or is made invisible or undisplayable
and subsequently made visible and displayable, the Window's most
recently focused Component will become the focus owner. The default
implementation of this method returns the default Component.

**Parameters:** window

- the Window whose initial Component is to be returned
**Returns:** the Component that should receive the focus when window is made
visible for the first time, or null if no suitable Component can
be found
**Throws:** IllegalArgumentException

- if window is null
**See Also:** getDefaultComponent(java.awt.Container)

,

Window.getMostRecentFocusOwner()

---

#### getInitialComponent

public

Component

getInitialComponent​(

Window

window)

Returns the Component that should receive the focus when a Window is
made visible for the first time. Once the Window has been made visible
by a call to

show()

or

setVisible(true)

, the
initial Component will not be used again. Instead, if the Window loses
and subsequently regains focus, or is made invisible or undisplayable
and subsequently made visible and displayable, the Window's most
recently focused Component will become the focus owner. The default
implementation of this method returns the default Component.

---

