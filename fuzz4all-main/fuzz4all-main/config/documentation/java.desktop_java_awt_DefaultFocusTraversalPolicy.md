# Class DefaultFocusTraversalPolicy

**Source:** `java.desktop\java\awt\DefaultFocusTraversalPolicy.html`

### Class Description

```java
public class
DefaultFocusTraversalPolicy

extends
ContainerOrderFocusTraversalPolicy
```

A FocusTraversalPolicy that determines traversal order based on the order
of child Components in a Container. From a particular focus cycle root, the
policy makes a pre-order traversal of the Component hierarchy, and traverses
a Container's children according to the ordering of the array returned by

Container.getComponents()

. Portions of the hierarchy that are
not visible and displayable will not be searched.

If client code has explicitly set the focusability of a Component by either
overriding

Component.isFocusTraversable()

or

Component.isFocusable()

, or by calling

Component.setFocusable()

, then a DefaultFocusTraversalPolicy
behaves exactly like a ContainerOrderFocusTraversalPolicy. If, however, the
Component is relying on default focusability, then a
DefaultFocusTraversalPolicy will reject all Components with non-focusable
peers. This is the default FocusTraversalPolicy for all AWT Containers.

The focusability of a peer is implementation-dependent. Sun recommends that
all implementations for a particular native platform construct peers with
the same focusability. The recommendations for Windows and Unix are that
Canvases, Labels, Panels, Scrollbars, ScrollPanes, Windows, and lightweight
Components have non-focusable peers, and all other Components have focusable
peers. These recommendations are used in the Sun AWT implementations. Note
that the focusability of a Component's peer is different from, and does not
impact, the focusability of the Component itself.

Please see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DefaultFocusTraversalPolicy()

*No description found.*

---

### Method Details

#### protected boolean accept​(
Component
aComponent)

Determines whether a Component is an acceptable choice as the new
focus owner. The Component must be visible, displayable, and enabled
to be accepted. If client code has explicitly set the focusability
of the Component by either overriding

Component.isFocusTraversable()

or

Component.isFocusable()

, or by calling

Component.setFocusable()

, then the Component will be
accepted if and only if it is focusable. If, however, the Component is
relying on default focusability, then all Canvases, Labels, Panels,
Scrollbars, ScrollPanes, Windows, and lightweight Components will be
rejected.

**Overrides:**
- accept

in class

ContainerOrderFocusTraversalPolicy

**Parameters:**
- aComponent

- the Component whose fitness as a focus owner is to
be tested

**Returns:**
- true

if aComponent meets the above requirements;

false

otherwise

---

### Additional Sections

#### Class DefaultFocusTraversalPolicy

java.lang.Object

- java.awt.FocusTraversalPolicy
- - java.awt.ContainerOrderFocusTraversalPolicy
- - java.awt.DefaultFocusTraversalPolicy

java.awt.FocusTraversalPolicy

- java.awt.ContainerOrderFocusTraversalPolicy
- - java.awt.DefaultFocusTraversalPolicy

java.awt.ContainerOrderFocusTraversalPolicy

- java.awt.DefaultFocusTraversalPolicy

java.awt.DefaultFocusTraversalPolicy

**All Implemented Interfaces:** Serializable

```java
public class
DefaultFocusTraversalPolicy

extends
ContainerOrderFocusTraversalPolicy
```

A FocusTraversalPolicy that determines traversal order based on the order
of child Components in a Container. From a particular focus cycle root, the
policy makes a pre-order traversal of the Component hierarchy, and traverses
a Container's children according to the ordering of the array returned by

Container.getComponents()

. Portions of the hierarchy that are
not visible and displayable will not be searched.

If client code has explicitly set the focusability of a Component by either
overriding

Component.isFocusTraversable()

or

Component.isFocusable()

, or by calling

Component.setFocusable()

, then a DefaultFocusTraversalPolicy
behaves exactly like a ContainerOrderFocusTraversalPolicy. If, however, the
Component is relying on default focusability, then a
DefaultFocusTraversalPolicy will reject all Components with non-focusable
peers. This is the default FocusTraversalPolicy for all AWT Containers.

The focusability of a peer is implementation-dependent. Sun recommends that
all implementations for a particular native platform construct peers with
the same focusability. The recommendations for Windows and Unix are that
Canvases, Labels, Panels, Scrollbars, ScrollPanes, Windows, and lightweight
Components have non-focusable peers, and all other Components have focusable
peers. These recommendations are used in the Sun AWT implementations. Note
that the focusability of a Component's peer is different from, and does not
impact, the focusability of the Component itself.

Please see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

**Since:** 1.4
**See Also:** Container.getComponents()

,

Component.isFocusable()

,

Component.setFocusable(boolean)

,

Serialized Form

public class

DefaultFocusTraversalPolicy

extends

ContainerOrderFocusTraversalPolicy

A FocusTraversalPolicy that determines traversal order based on the order
of child Components in a Container. From a particular focus cycle root, the
policy makes a pre-order traversal of the Component hierarchy, and traverses
a Container's children according to the ordering of the array returned by

Container.getComponents()

. Portions of the hierarchy that are
not visible and displayable will not be searched.

If client code has explicitly set the focusability of a Component by either
overriding

Component.isFocusTraversable()

or

Component.isFocusable()

, or by calling

Component.setFocusable()

, then a DefaultFocusTraversalPolicy
behaves exactly like a ContainerOrderFocusTraversalPolicy. If, however, the
Component is relying on default focusability, then a
DefaultFocusTraversalPolicy will reject all Components with non-focusable
peers. This is the default FocusTraversalPolicy for all AWT Containers.

The focusability of a peer is implementation-dependent. Sun recommends that
all implementations for a particular native platform construct peers with
the same focusability. The recommendations for Windows and Unix are that
Canvases, Labels, Panels, Scrollbars, ScrollPanes, Windows, and lightweight
Components have non-focusable peers, and all other Components have focusable
peers. These recommendations are used in the Sun AWT implementations. Note
that the focusability of a Component's peer is different from, and does not
impact, the focusability of the Component itself.

Please see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

If client code has explicitly set the focusability of a Component by either
overriding

Component.isFocusTraversable()

or

Component.isFocusable()

, or by calling

Component.setFocusable()

, then a DefaultFocusTraversalPolicy
behaves exactly like a ContainerOrderFocusTraversalPolicy. If, however, the
Component is relying on default focusability, then a
DefaultFocusTraversalPolicy will reject all Components with non-focusable
peers. This is the default FocusTraversalPolicy for all AWT Containers.

The focusability of a peer is implementation-dependent. Sun recommends that
all implementations for a particular native platform construct peers with
the same focusability. The recommendations for Windows and Unix are that
Canvases, Labels, Panels, Scrollbars, ScrollPanes, Windows, and lightweight
Components have non-focusable peers, and all other Components have focusable
peers. These recommendations are used in the Sun AWT implementations. Note
that the focusability of a Component's peer is different from, and does not
impact, the focusability of the Component itself.

Please see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

The focusability of a peer is implementation-dependent. Sun recommends that
all implementations for a particular native platform construct peers with
the same focusability. The recommendations for Windows and Unix are that
Canvases, Labels, Panels, Scrollbars, ScrollPanes, Windows, and lightweight
Components have non-focusable peers, and all other Components have focusable
peers. These recommendations are used in the Sun AWT implementations. Note
that the focusability of a Component's peer is different from, and does not
impact, the focusability of the Component itself.

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

DefaultFocusTraversalPolicy

()

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

Determines whether a Component is an acceptable choice as the new
focus owner.

- Methods declared in class java.awt.

ContainerOrderFocusTraversalPolicy

getComponentAfter

,

getComponentBefore

,

getDefaultComponent

,

getFirstComponent

,

getImplicitDownCycleTraversal

,

getLastComponent

,

setImplicitDownCycleTraversal

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

DefaultFocusTraversalPolicy

()

---

#### Constructor Summary

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

Determines whether a Component is an acceptable choice as the new
focus owner.

- Methods declared in class java.awt.

ContainerOrderFocusTraversalPolicy

getComponentAfter

,

getComponentBefore

,

getDefaultComponent

,

getFirstComponent

,

getImplicitDownCycleTraversal

,

getLastComponent

,

setImplicitDownCycleTraversal

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

Determines whether a Component is an acceptable choice as the new
focus owner.

Methods declared in class java.awt.

ContainerOrderFocusTraversalPolicy

getComponentAfter

,

getComponentBefore

,

getDefaultComponent

,

getFirstComponent

,

getImplicitDownCycleTraversal

,

getLastComponent

,

setImplicitDownCycleTraversal

---

#### Methods declared in class java.awt. ContainerOrderFocusTraversalPolicy

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

- DefaultFocusTraversalPolicy

```java
public DefaultFocusTraversalPolicy()
```

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
protected boolean accept​(
Component
aComponent)
```

Determines whether a Component is an acceptable choice as the new
focus owner. The Component must be visible, displayable, and enabled
to be accepted. If client code has explicitly set the focusability
of the Component by either overriding

Component.isFocusTraversable()

or

Component.isFocusable()

, or by calling

Component.setFocusable()

, then the Component will be
accepted if and only if it is focusable. If, however, the Component is
relying on default focusability, then all Canvases, Labels, Panels,
Scrollbars, ScrollPanes, Windows, and lightweight Components will be
rejected.

**Overrides:** accept

in class

ContainerOrderFocusTraversalPolicy
**Parameters:** aComponent

- the Component whose fitness as a focus owner is to
be tested
**Returns:** true

if aComponent meets the above requirements;

false

otherwise

Constructor Detail

- DefaultFocusTraversalPolicy

```java
public DefaultFocusTraversalPolicy()
```

---

#### Constructor Detail

DefaultFocusTraversalPolicy

```java
public DefaultFocusTraversalPolicy()
```

---

#### DefaultFocusTraversalPolicy

public DefaultFocusTraversalPolicy()

Method Detail

- accept

```java
protected boolean accept​(
Component
aComponent)
```

Determines whether a Component is an acceptable choice as the new
focus owner. The Component must be visible, displayable, and enabled
to be accepted. If client code has explicitly set the focusability
of the Component by either overriding

Component.isFocusTraversable()

or

Component.isFocusable()

, or by calling

Component.setFocusable()

, then the Component will be
accepted if and only if it is focusable. If, however, the Component is
relying on default focusability, then all Canvases, Labels, Panels,
Scrollbars, ScrollPanes, Windows, and lightweight Components will be
rejected.

**Overrides:** accept

in class

ContainerOrderFocusTraversalPolicy
**Parameters:** aComponent

- the Component whose fitness as a focus owner is to
be tested
**Returns:** true

if aComponent meets the above requirements;

false

otherwise

---

#### Method Detail

accept

```java
protected boolean accept​(
Component
aComponent)
```

Determines whether a Component is an acceptable choice as the new
focus owner. The Component must be visible, displayable, and enabled
to be accepted. If client code has explicitly set the focusability
of the Component by either overriding

Component.isFocusTraversable()

or

Component.isFocusable()

, or by calling

Component.setFocusable()

, then the Component will be
accepted if and only if it is focusable. If, however, the Component is
relying on default focusability, then all Canvases, Labels, Panels,
Scrollbars, ScrollPanes, Windows, and lightweight Components will be
rejected.

**Overrides:** accept

in class

ContainerOrderFocusTraversalPolicy
**Parameters:** aComponent

- the Component whose fitness as a focus owner is to
be tested
**Returns:** true

if aComponent meets the above requirements;

false

otherwise

---

#### accept

protected boolean accept​(

Component

aComponent)

Determines whether a Component is an acceptable choice as the new
focus owner. The Component must be visible, displayable, and enabled
to be accepted. If client code has explicitly set the focusability
of the Component by either overriding

Component.isFocusTraversable()

or

Component.isFocusable()

, or by calling

Component.setFocusable()

, then the Component will be
accepted if and only if it is focusable. If, however, the Component is
relying on default focusability, then all Canvases, Labels, Panels,
Scrollbars, ScrollPanes, Windows, and lightweight Components will be
rejected.

---

