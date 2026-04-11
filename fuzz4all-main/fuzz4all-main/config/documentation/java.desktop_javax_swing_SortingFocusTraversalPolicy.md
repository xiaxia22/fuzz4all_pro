# Class SortingFocusTraversalPolicy

**Source:** `java.desktop\javax\swing\SortingFocusTraversalPolicy.html`

### Class Description

```java
public class
SortingFocusTraversalPolicy

extends
InternalFrameFocusTraversalPolicy
```

A FocusTraversalPolicy that determines traversal order by sorting the
Components of a focus traversal cycle based on a given Comparator. Portions
of the Component hierarchy that are not visible and displayable will not be
included.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's default
Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

By default, methods of this class with return a Component only if it is
visible, displayable, enabled, and focusable. Subclasses can modify this
behavior by overriding the

accept

method.

This policy takes into account

focus traversal
policy providers

. When searching for first/last/next/previous Component,
if a focus traversal policy provider is encountered, its focus traversal
policy is used to perform the search operation.

**Direct Known Subclasses:** LayoutFocusTraversalPolicy

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SortingFocusTraversalPolicy()

Constructs a SortingFocusTraversalPolicy without a Comparator.
Subclasses must set the Comparator using

setComparator

before installing this FocusTraversalPolicy on a focus cycle root or
KeyboardFocusManager.

---

#### public SortingFocusTraversalPolicy​(
Comparator
<? super
Component
> comparator)

Constructs a SortingFocusTraversalPolicy with the specified Comparator.

**Parameters:**
- comparator

- the

Comparator

to sort by

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
aContainer must be a focus cycle root of aComponent or a focus traversal policy provider.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Specified by:**
- getComponentAfter

in class

FocusTraversalPolicy

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
aContainer must be a focus cycle root of aComponent or a focus traversal policy provider.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Specified by:**
- getComponentBefore

in class

FocusTraversalPolicy

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

**Specified by:**
- getFirstComponent

in class

FocusTraversalPolicy

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

**Specified by:**
- getLastComponent

in class

FocusTraversalPolicy

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

#### public
Component
getDefaultComponent​(
Container
aContainer)

Returns the default Component to focus. This Component will be the first
to receive focus when traversing down into a new focus traversal cycle
rooted at aContainer. The default implementation of this method
returns the same Component as

getFirstComponent

.

**Specified by:**
- getDefaultComponent

in class

FocusTraversalPolicy

**Parameters:**
- aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
default Component is to be returned

**Returns:**
- the default Component in the traversal cycle of aContainer,
or null if no suitable Component can be found

**Throws:**
- IllegalArgumentException

- if aContainer is null

**See Also:**
- getFirstComponent(java.awt.Container)

---

#### public void setImplicitDownCycleTraversal​(boolean implicitDownCycleTraversal)

Sets whether this SortingFocusTraversalPolicy transfers focus down-cycle
implicitly. If

true

, during normal focus traversal,
the Component traversed after a focus cycle root will be the focus-
cycle-root's default Component to focus. If

false

, the
next Component in the focus traversal cycle rooted at the specified
focus cycle root will be traversed instead. The default value for this
property is

true

.

**Parameters:**
- implicitDownCycleTraversal

- whether this
SortingFocusTraversalPolicy transfers focus down-cycle implicitly

**See Also:**
- getImplicitDownCycleTraversal()

,

getFirstComponent(java.awt.Container)

---

#### public boolean getImplicitDownCycleTraversal()

Returns whether this SortingFocusTraversalPolicy transfers focus down-
cycle implicitly. If

true

, during normal focus
traversal, the Component traversed after a focus cycle root will be the
focus-cycle-root's default Component to focus. If

false

,
the next Component in the focus traversal cycle rooted at the specified
focus cycle root will be traversed instead.

**Returns:**
- whether this SortingFocusTraversalPolicy transfers focus down-
cycle implicitly

**See Also:**
- setImplicitDownCycleTraversal(boolean)

,

getFirstComponent(java.awt.Container)

---

#### protected void setComparator​(
Comparator
<? super
Component
> comparator)

Sets the Comparator which will be used to sort the Components in a
focus traversal cycle.

**Parameters:**
- comparator

- the Comparator which will be used for sorting

---

#### protected
Comparator
<? super
Component
> getComparator()

Returns the Comparator which will be used to sort the Components in a
focus traversal cycle.

**Returns:**
- the Comparator which will be used for sorting

---

#### protected boolean accept​(
Component
aComponent)

Determines whether a Component is an acceptable choice as the new
focus owner. By default, this method will accept a Component if and
only if it is visible, displayable, enabled, and focusable.

**Parameters:**
- aComponent

- the Component whose fitness as a focus owner is to
be tested

**Returns:**
- true

if aComponent is visible, displayable,
enabled, and focusable;

false

otherwise

---

### Additional Sections

#### Class SortingFocusTraversalPolicy

java.lang.Object

- java.awt.FocusTraversalPolicy
- - javax.swing.InternalFrameFocusTraversalPolicy
- - javax.swing.SortingFocusTraversalPolicy

java.awt.FocusTraversalPolicy

- javax.swing.InternalFrameFocusTraversalPolicy
- - javax.swing.SortingFocusTraversalPolicy

javax.swing.InternalFrameFocusTraversalPolicy

- javax.swing.SortingFocusTraversalPolicy

javax.swing.SortingFocusTraversalPolicy

**Direct Known Subclasses:** LayoutFocusTraversalPolicy

```java
public class
SortingFocusTraversalPolicy

extends
InternalFrameFocusTraversalPolicy
```

A FocusTraversalPolicy that determines traversal order by sorting the
Components of a focus traversal cycle based on a given Comparator. Portions
of the Component hierarchy that are not visible and displayable will not be
included.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's default
Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

By default, methods of this class with return a Component only if it is
visible, displayable, enabled, and focusable. Subclasses can modify this
behavior by overriding the

accept

method.

This policy takes into account

focus traversal
policy providers

. When searching for first/last/next/previous Component,
if a focus traversal policy provider is encountered, its focus traversal
policy is used to perform the search operation.

**Since:** 1.4
**See Also:** Comparator

public class

SortingFocusTraversalPolicy

extends

InternalFrameFocusTraversalPolicy

A FocusTraversalPolicy that determines traversal order by sorting the
Components of a focus traversal cycle based on a given Comparator. Portions
of the Component hierarchy that are not visible and displayable will not be
included.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's default
Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

By default, methods of this class with return a Component only if it is
visible, displayable, enabled, and focusable. Subclasses can modify this
behavior by overriding the

accept

method.

This policy takes into account

focus traversal
policy providers

. When searching for first/last/next/previous Component,
if a focus traversal policy provider is encountered, its focus traversal
policy is used to perform the search operation.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's default
Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

By default, methods of this class with return a Component only if it is
visible, displayable, enabled, and focusable. Subclasses can modify this
behavior by overriding the

accept

method.

This policy takes into account

focus traversal
policy providers

. When searching for first/last/next/previous Component,
if a focus traversal policy provider is encountered, its focus traversal
policy is used to perform the search operation.

By default, methods of this class with return a Component only if it is
visible, displayable, enabled, and focusable. Subclasses can modify this
behavior by overriding the

accept

method.

This policy takes into account

focus traversal
policy providers

. When searching for first/last/next/previous Component,
if a focus traversal policy provider is encountered, its focus traversal
policy is used to perform the search operation.

This policy takes into account

focus traversal
policy providers

. When searching for first/last/next/previous Component,
if a focus traversal policy provider is encountered, its focus traversal
policy is used to perform the search operation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SortingFocusTraversalPolicy

()

Constructs a SortingFocusTraversalPolicy without a Comparator.

SortingFocusTraversalPolicy

​(

Comparator

<? super

Component

> comparator)

Constructs a SortingFocusTraversalPolicy with the specified Comparator.

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

protected

Comparator

<? super

Component

>

getComparator

()

Returns the Comparator which will be used to sort the Components in a
focus traversal cycle.

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

getDefaultComponent

​(

Container

aContainer)

Returns the default Component to focus.

Component

getFirstComponent

​(

Container

aContainer)

Returns the first Component in the traversal cycle.

boolean

getImplicitDownCycleTraversal

()

Returns whether this SortingFocusTraversalPolicy transfers focus down-
cycle implicitly.

Component

getLastComponent

​(

Container

aContainer)

Returns the last Component in the traversal cycle.

protected void

setComparator

​(

Comparator

<? super

Component

> comparator)

Sets the Comparator which will be used to sort the Components in a
focus traversal cycle.

void

setImplicitDownCycleTraversal

​(boolean implicitDownCycleTraversal)

Sets whether this SortingFocusTraversalPolicy transfers focus down-cycle
implicitly.

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

Modifier

Constructor

Description

protected

SortingFocusTraversalPolicy

()

Constructs a SortingFocusTraversalPolicy without a Comparator.

SortingFocusTraversalPolicy

​(

Comparator

<? super

Component

> comparator)

Constructs a SortingFocusTraversalPolicy with the specified Comparator.

---

#### Constructor Summary

Constructs a SortingFocusTraversalPolicy without a Comparator.

Constructs a SortingFocusTraversalPolicy with the specified Comparator.

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

protected

Comparator

<? super

Component

>

getComparator

()

Returns the Comparator which will be used to sort the Components in a
focus traversal cycle.

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

getDefaultComponent

​(

Container

aContainer)

Returns the default Component to focus.

Component

getFirstComponent

​(

Container

aContainer)

Returns the first Component in the traversal cycle.

boolean

getImplicitDownCycleTraversal

()

Returns whether this SortingFocusTraversalPolicy transfers focus down-
cycle implicitly.

Component

getLastComponent

​(

Container

aContainer)

Returns the last Component in the traversal cycle.

protected void

setComparator

​(

Comparator

<? super

Component

> comparator)

Sets the Comparator which will be used to sort the Components in a
focus traversal cycle.

void

setImplicitDownCycleTraversal

​(boolean implicitDownCycleTraversal)

Sets whether this SortingFocusTraversalPolicy transfers focus down-cycle
implicitly.

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

Determines whether a Component is an acceptable choice as the new
focus owner.

Returns the Comparator which will be used to sort the Components in a
focus traversal cycle.

Returns the Component that should receive the focus after aComponent.

Returns the Component that should receive the focus before aComponent.

Returns the default Component to focus.

Returns the first Component in the traversal cycle.

Returns whether this SortingFocusTraversalPolicy transfers focus down-
cycle implicitly.

Returns the last Component in the traversal cycle.

Sets the Comparator which will be used to sort the Components in a
focus traversal cycle.

Sets whether this SortingFocusTraversalPolicy transfers focus down-cycle
implicitly.

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

- SortingFocusTraversalPolicy

```java
protected SortingFocusTraversalPolicy()
```

Constructs a SortingFocusTraversalPolicy without a Comparator.
Subclasses must set the Comparator using

setComparator

before installing this FocusTraversalPolicy on a focus cycle root or
KeyboardFocusManager.

- SortingFocusTraversalPolicy

```java
public SortingFocusTraversalPolicy​(
Comparator
<? super
Component
> comparator)
```

Constructs a SortingFocusTraversalPolicy with the specified Comparator.

**Parameters:** comparator

- the

Comparator

to sort by

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
aContainer must be a focus cycle root of aComponent or a focus traversal policy provider.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Specified by:** getComponentAfter

in class

FocusTraversalPolicy
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
aContainer must be a focus cycle root of aComponent or a focus traversal policy provider.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Specified by:** getComponentBefore

in class

FocusTraversalPolicy
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

**Specified by:** getFirstComponent

in class

FocusTraversalPolicy
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

**Specified by:** getLastComponent

in class

FocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
last Component is to be returned
**Returns:** the last Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

- getDefaultComponent

```java
public
Component
getDefaultComponent​(
Container
aContainer)
```

Returns the default Component to focus. This Component will be the first
to receive focus when traversing down into a new focus traversal cycle
rooted at aContainer. The default implementation of this method
returns the same Component as

getFirstComponent

.

**Specified by:** getDefaultComponent

in class

FocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
default Component is to be returned
**Returns:** the default Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null
**See Also:** getFirstComponent(java.awt.Container)

- setImplicitDownCycleTraversal

```java
public void setImplicitDownCycleTraversal​(boolean implicitDownCycleTraversal)
```

Sets whether this SortingFocusTraversalPolicy transfers focus down-cycle
implicitly. If

true

, during normal focus traversal,
the Component traversed after a focus cycle root will be the focus-
cycle-root's default Component to focus. If

false

, the
next Component in the focus traversal cycle rooted at the specified
focus cycle root will be traversed instead. The default value for this
property is

true

.

**Parameters:** implicitDownCycleTraversal

- whether this
SortingFocusTraversalPolicy transfers focus down-cycle implicitly
**See Also:** getImplicitDownCycleTraversal()

,

getFirstComponent(java.awt.Container)

- getImplicitDownCycleTraversal

```java
public boolean getImplicitDownCycleTraversal()
```

Returns whether this SortingFocusTraversalPolicy transfers focus down-
cycle implicitly. If

true

, during normal focus
traversal, the Component traversed after a focus cycle root will be the
focus-cycle-root's default Component to focus. If

false

,
the next Component in the focus traversal cycle rooted at the specified
focus cycle root will be traversed instead.

**Returns:** whether this SortingFocusTraversalPolicy transfers focus down-
cycle implicitly
**See Also:** setImplicitDownCycleTraversal(boolean)

,

getFirstComponent(java.awt.Container)

- setComparator

```java
protected void setComparator​(
Comparator
<? super
Component
> comparator)
```

Sets the Comparator which will be used to sort the Components in a
focus traversal cycle.

**Parameters:** comparator

- the Comparator which will be used for sorting

- getComparator

```java
protected
Comparator
<? super
Component
> getComparator()
```

Returns the Comparator which will be used to sort the Components in a
focus traversal cycle.

**Returns:** the Comparator which will be used for sorting

- accept

```java
protected boolean accept​(
Component
aComponent)
```

Determines whether a Component is an acceptable choice as the new
focus owner. By default, this method will accept a Component if and
only if it is visible, displayable, enabled, and focusable.

**Parameters:** aComponent

- the Component whose fitness as a focus owner is to
be tested
**Returns:** true

if aComponent is visible, displayable,
enabled, and focusable;

false

otherwise

Constructor Detail

- SortingFocusTraversalPolicy

```java
protected SortingFocusTraversalPolicy()
```

Constructs a SortingFocusTraversalPolicy without a Comparator.
Subclasses must set the Comparator using

setComparator

before installing this FocusTraversalPolicy on a focus cycle root or
KeyboardFocusManager.

- SortingFocusTraversalPolicy

```java
public SortingFocusTraversalPolicy​(
Comparator
<? super
Component
> comparator)
```

Constructs a SortingFocusTraversalPolicy with the specified Comparator.

**Parameters:** comparator

- the

Comparator

to sort by

---

#### Constructor Detail

SortingFocusTraversalPolicy

```java
protected SortingFocusTraversalPolicy()
```

Constructs a SortingFocusTraversalPolicy without a Comparator.
Subclasses must set the Comparator using

setComparator

before installing this FocusTraversalPolicy on a focus cycle root or
KeyboardFocusManager.

---

#### SortingFocusTraversalPolicy

protected SortingFocusTraversalPolicy()

Constructs a SortingFocusTraversalPolicy without a Comparator.
Subclasses must set the Comparator using

setComparator

before installing this FocusTraversalPolicy on a focus cycle root or
KeyboardFocusManager.

SortingFocusTraversalPolicy

```java
public SortingFocusTraversalPolicy​(
Comparator
<? super
Component
> comparator)
```

Constructs a SortingFocusTraversalPolicy with the specified Comparator.

**Parameters:** comparator

- the

Comparator

to sort by

---

#### SortingFocusTraversalPolicy

public SortingFocusTraversalPolicy​(

Comparator

<? super

Component

> comparator)

Constructs a SortingFocusTraversalPolicy with the specified Comparator.

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
aContainer must be a focus cycle root of aComponent or a focus traversal policy provider.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Specified by:** getComponentAfter

in class

FocusTraversalPolicy
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
aContainer must be a focus cycle root of aComponent or a focus traversal policy provider.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Specified by:** getComponentBefore

in class

FocusTraversalPolicy
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

**Specified by:** getFirstComponent

in class

FocusTraversalPolicy
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

**Specified by:** getLastComponent

in class

FocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
last Component is to be returned
**Returns:** the last Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null

- getDefaultComponent

```java
public
Component
getDefaultComponent​(
Container
aContainer)
```

Returns the default Component to focus. This Component will be the first
to receive focus when traversing down into a new focus traversal cycle
rooted at aContainer. The default implementation of this method
returns the same Component as

getFirstComponent

.

**Specified by:** getDefaultComponent

in class

FocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
default Component is to be returned
**Returns:** the default Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null
**See Also:** getFirstComponent(java.awt.Container)

- setImplicitDownCycleTraversal

```java
public void setImplicitDownCycleTraversal​(boolean implicitDownCycleTraversal)
```

Sets whether this SortingFocusTraversalPolicy transfers focus down-cycle
implicitly. If

true

, during normal focus traversal,
the Component traversed after a focus cycle root will be the focus-
cycle-root's default Component to focus. If

false

, the
next Component in the focus traversal cycle rooted at the specified
focus cycle root will be traversed instead. The default value for this
property is

true

.

**Parameters:** implicitDownCycleTraversal

- whether this
SortingFocusTraversalPolicy transfers focus down-cycle implicitly
**See Also:** getImplicitDownCycleTraversal()

,

getFirstComponent(java.awt.Container)

- getImplicitDownCycleTraversal

```java
public boolean getImplicitDownCycleTraversal()
```

Returns whether this SortingFocusTraversalPolicy transfers focus down-
cycle implicitly. If

true

, during normal focus
traversal, the Component traversed after a focus cycle root will be the
focus-cycle-root's default Component to focus. If

false

,
the next Component in the focus traversal cycle rooted at the specified
focus cycle root will be traversed instead.

**Returns:** whether this SortingFocusTraversalPolicy transfers focus down-
cycle implicitly
**See Also:** setImplicitDownCycleTraversal(boolean)

,

getFirstComponent(java.awt.Container)

- setComparator

```java
protected void setComparator​(
Comparator
<? super
Component
> comparator)
```

Sets the Comparator which will be used to sort the Components in a
focus traversal cycle.

**Parameters:** comparator

- the Comparator which will be used for sorting

- getComparator

```java
protected
Comparator
<? super
Component
> getComparator()
```

Returns the Comparator which will be used to sort the Components in a
focus traversal cycle.

**Returns:** the Comparator which will be used for sorting

- accept

```java
protected boolean accept​(
Component
aComponent)
```

Determines whether a Component is an acceptable choice as the new
focus owner. By default, this method will accept a Component if and
only if it is visible, displayable, enabled, and focusable.

**Parameters:** aComponent

- the Component whose fitness as a focus owner is to
be tested
**Returns:** true

if aComponent is visible, displayable,
enabled, and focusable;

false

otherwise

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
aContainer must be a focus cycle root of aComponent or a focus traversal policy provider.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Specified by:** getComponentAfter

in class

FocusTraversalPolicy
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
aContainer must be a focus cycle root of aComponent or a focus traversal policy provider.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
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
aContainer must be a focus cycle root of aComponent or a focus traversal policy provider.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

**Specified by:** getComponentBefore

in class

FocusTraversalPolicy
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
aContainer must be a focus cycle root of aComponent or a focus traversal policy provider.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
cycle. That is, during normal focus traversal, the Component
traversed after a focus cycle root will be the focus-cycle-root's
default Component to focus. This behavior can be disabled using the

setImplicitDownCycleTraversal

method.

If aContainer is

focus
traversal policy provider

, the focus is always transferred down-cycle.

By default, SortingFocusTraversalPolicy implicitly transfers focus down-
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

**Specified by:** getFirstComponent

in class

FocusTraversalPolicy
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

**Specified by:** getLastComponent

in class

FocusTraversalPolicy
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

getDefaultComponent

```java
public
Component
getDefaultComponent​(
Container
aContainer)
```

Returns the default Component to focus. This Component will be the first
to receive focus when traversing down into a new focus traversal cycle
rooted at aContainer. The default implementation of this method
returns the same Component as

getFirstComponent

.

**Specified by:** getDefaultComponent

in class

FocusTraversalPolicy
**Parameters:** aContainer

- a focus cycle root of aComponent or a focus traversal policy provider whose
default Component is to be returned
**Returns:** the default Component in the traversal cycle of aContainer,
or null if no suitable Component can be found
**Throws:** IllegalArgumentException

- if aContainer is null
**See Also:** getFirstComponent(java.awt.Container)

---

#### getDefaultComponent

public

Component

getDefaultComponent​(

Container

aContainer)

Returns the default Component to focus. This Component will be the first
to receive focus when traversing down into a new focus traversal cycle
rooted at aContainer. The default implementation of this method
returns the same Component as

getFirstComponent

.

setImplicitDownCycleTraversal

```java
public void setImplicitDownCycleTraversal​(boolean implicitDownCycleTraversal)
```

Sets whether this SortingFocusTraversalPolicy transfers focus down-cycle
implicitly. If

true

, during normal focus traversal,
the Component traversed after a focus cycle root will be the focus-
cycle-root's default Component to focus. If

false

, the
next Component in the focus traversal cycle rooted at the specified
focus cycle root will be traversed instead. The default value for this
property is

true

.

**Parameters:** implicitDownCycleTraversal

- whether this
SortingFocusTraversalPolicy transfers focus down-cycle implicitly
**See Also:** getImplicitDownCycleTraversal()

,

getFirstComponent(java.awt.Container)

---

#### setImplicitDownCycleTraversal

public void setImplicitDownCycleTraversal​(boolean implicitDownCycleTraversal)

Sets whether this SortingFocusTraversalPolicy transfers focus down-cycle
implicitly. If

true

, during normal focus traversal,
the Component traversed after a focus cycle root will be the focus-
cycle-root's default Component to focus. If

false

, the
next Component in the focus traversal cycle rooted at the specified
focus cycle root will be traversed instead. The default value for this
property is

true

.

getImplicitDownCycleTraversal

```java
public boolean getImplicitDownCycleTraversal()
```

Returns whether this SortingFocusTraversalPolicy transfers focus down-
cycle implicitly. If

true

, during normal focus
traversal, the Component traversed after a focus cycle root will be the
focus-cycle-root's default Component to focus. If

false

,
the next Component in the focus traversal cycle rooted at the specified
focus cycle root will be traversed instead.

**Returns:** whether this SortingFocusTraversalPolicy transfers focus down-
cycle implicitly
**See Also:** setImplicitDownCycleTraversal(boolean)

,

getFirstComponent(java.awt.Container)

---

#### getImplicitDownCycleTraversal

public boolean getImplicitDownCycleTraversal()

Returns whether this SortingFocusTraversalPolicy transfers focus down-
cycle implicitly. If

true

, during normal focus
traversal, the Component traversed after a focus cycle root will be the
focus-cycle-root's default Component to focus. If

false

,
the next Component in the focus traversal cycle rooted at the specified
focus cycle root will be traversed instead.

setComparator

```java
protected void setComparator​(
Comparator
<? super
Component
> comparator)
```

Sets the Comparator which will be used to sort the Components in a
focus traversal cycle.

**Parameters:** comparator

- the Comparator which will be used for sorting

---

#### setComparator

protected void setComparator​(

Comparator

<? super

Component

> comparator)

Sets the Comparator which will be used to sort the Components in a
focus traversal cycle.

getComparator

```java
protected
Comparator
<? super
Component
> getComparator()
```

Returns the Comparator which will be used to sort the Components in a
focus traversal cycle.

**Returns:** the Comparator which will be used for sorting

---

#### getComparator

protected

Comparator

<? super

Component

> getComparator()

Returns the Comparator which will be used to sort the Components in a
focus traversal cycle.

accept

```java
protected boolean accept​(
Component
aComponent)
```

Determines whether a Component is an acceptable choice as the new
focus owner. By default, this method will accept a Component if and
only if it is visible, displayable, enabled, and focusable.

**Parameters:** aComponent

- the Component whose fitness as a focus owner is to
be tested
**Returns:** true

if aComponent is visible, displayable,
enabled, and focusable;

false

otherwise

---

#### accept

protected boolean accept​(

Component

aComponent)

Determines whether a Component is an acceptable choice as the new
focus owner. By default, this method will accept a Component if and
only if it is visible, displayable, enabled, and focusable.

---

