# Class ViewportLayout

**Source:** `java.desktop\javax\swing\ViewportLayout.html`

### Class Description

```java
public class
ViewportLayout

extends
Object

implements
LayoutManager
,
Serializable
```

The default layout manager for

JViewport

.

ViewportLayout

defines
a policy for layout that should be useful for most applications.
The viewport makes its view the same size as the viewport,
however it will not make the view smaller than its minimum size.
As the viewport grows the view is kept bottom justified until
the entire view is visible, subsequently the view is kept top
justified.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** LayoutManager

,

Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ViewportLayout()

*No description found.*

---

### Method Details

#### public void addLayoutComponent​(
String
name,

Component
c)

Adds the specified component to the layout. Not used by this class.

**Specified by:**
- addLayoutComponent

in interface

LayoutManager

**Parameters:**
- name

- the name of the component
- c

- the component to be added

---

#### public void removeLayoutComponent​(
Component
c)

Removes the specified component from the layout. Not used by
this class.

**Specified by:**
- removeLayoutComponent

in interface

LayoutManager

**Parameters:**
- c

- the component to remove

---

#### public
Dimension
preferredLayoutSize​(
Container
parent)

Returns the preferred dimensions for this layout given the components
in the specified target container.

**Specified by:**
- preferredLayoutSize

in interface

LayoutManager

**Parameters:**
- parent

- the component which needs to be laid out

**Returns:**
- a

Dimension

object containing the
preferred dimensions

**See Also:**
- minimumLayoutSize(java.awt.Container)

---

#### public
Dimension
minimumLayoutSize​(
Container
parent)

Returns the minimum dimensions needed to layout the components
contained in the specified target container.

**Specified by:**
- minimumLayoutSize

in interface

LayoutManager

**Parameters:**
- parent

- the component which needs to be laid out

**Returns:**
- a

Dimension

object containing the minimum
dimensions

**See Also:**
- preferredLayoutSize(java.awt.Container)

---

#### public void layoutContainer​(
Container
parent)

Called by the AWT when the specified container needs to be laid out.

**Specified by:**
- layoutContainer

in interface

LayoutManager

**Parameters:**
- parent

- the container to lay out

**Throws:**
- AWTError

- if the target isn't the container specified to the

BoxLayout

constructor

---

### Additional Sections

#### Class ViewportLayout

java.lang.Object

- javax.swing.ViewportLayout

javax.swing.ViewportLayout

**All Implemented Interfaces:** LayoutManager

,

Serializable

```java
public class
ViewportLayout

extends
Object

implements
LayoutManager
,
Serializable
```

The default layout manager for

JViewport

.

ViewportLayout

defines
a policy for layout that should be useful for most applications.
The viewport makes its view the same size as the viewport,
however it will not make the view smaller than its minimum size.
As the viewport grows the view is kept bottom justified until
the entire view is visible, subsequently the view is kept top
justified.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**Since:** 1.2
**See Also:** Serialized Form

public class

ViewportLayout

extends

Object

implements

LayoutManager

,

Serializable

The default layout manager for

JViewport

.

ViewportLayout

defines
a policy for layout that should be useful for most applications.
The viewport makes its view the same size as the viewport,
however it will not make the view smaller than its minimum size.
As the viewport grows the view is kept bottom justified until
the entire view is visible, subsequently the view is kept top
justified.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ViewportLayout

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addLayoutComponent

​(

String

name,

Component

c)

Adds the specified component to the layout.

void

layoutContainer

​(

Container

parent)

Called by the AWT when the specified container needs to be laid out.

Dimension

minimumLayoutSize

​(

Container

parent)

Returns the minimum dimensions needed to layout the components
contained in the specified target container.

Dimension

preferredLayoutSize

​(

Container

parent)

Returns the preferred dimensions for this layout given the components
in the specified target container.

void

removeLayoutComponent

​(

Component

c)

Removes the specified component from the layout.

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

ViewportLayout

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

void

addLayoutComponent

​(

String

name,

Component

c)

Adds the specified component to the layout.

void

layoutContainer

​(

Container

parent)

Called by the AWT when the specified container needs to be laid out.

Dimension

minimumLayoutSize

​(

Container

parent)

Returns the minimum dimensions needed to layout the components
contained in the specified target container.

Dimension

preferredLayoutSize

​(

Container

parent)

Returns the preferred dimensions for this layout given the components
in the specified target container.

void

removeLayoutComponent

​(

Component

c)

Removes the specified component from the layout.

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

Adds the specified component to the layout.

Called by the AWT when the specified container needs to be laid out.

Returns the minimum dimensions needed to layout the components
contained in the specified target container.

Returns the preferred dimensions for this layout given the components
in the specified target container.

Removes the specified component from the layout.

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

- ViewportLayout

```java
public ViewportLayout()
```

============ METHOD DETAIL ==========

- Method Detail

- addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
c)
```

Adds the specified component to the layout. Not used by this class.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the name of the component
**Parameters:** c

- the component to be added

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
c)
```

Removes the specified component from the layout. Not used by
this class.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** c

- the component to remove

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
parent)
```

Returns the preferred dimensions for this layout given the components
in the specified target container.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the component which needs to be laid out
**Returns:** a

Dimension

object containing the
preferred dimensions
**See Also:** minimumLayoutSize(java.awt.Container)

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

Returns the minimum dimensions needed to layout the components
contained in the specified target container.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the component which needs to be laid out
**Returns:** a

Dimension

object containing the minimum
dimensions
**See Also:** preferredLayoutSize(java.awt.Container)

- layoutContainer

```java
public void layoutContainer​(
Container
parent)
```

Called by the AWT when the specified container needs to be laid out.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** parent

- the container to lay out
**Throws:** AWTError

- if the target isn't the container specified to the

BoxLayout

constructor

Constructor Detail

- ViewportLayout

```java
public ViewportLayout()
```

---

#### Constructor Detail

ViewportLayout

```java
public ViewportLayout()
```

---

#### ViewportLayout

public ViewportLayout()

Method Detail

- addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
c)
```

Adds the specified component to the layout. Not used by this class.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the name of the component
**Parameters:** c

- the component to be added

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
c)
```

Removes the specified component from the layout. Not used by
this class.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** c

- the component to remove

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
parent)
```

Returns the preferred dimensions for this layout given the components
in the specified target container.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the component which needs to be laid out
**Returns:** a

Dimension

object containing the
preferred dimensions
**See Also:** minimumLayoutSize(java.awt.Container)

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

Returns the minimum dimensions needed to layout the components
contained in the specified target container.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the component which needs to be laid out
**Returns:** a

Dimension

object containing the minimum
dimensions
**See Also:** preferredLayoutSize(java.awt.Container)

- layoutContainer

```java
public void layoutContainer​(
Container
parent)
```

Called by the AWT when the specified container needs to be laid out.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** parent

- the container to lay out
**Throws:** AWTError

- if the target isn't the container specified to the

BoxLayout

constructor

---

#### Method Detail

addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
c)
```

Adds the specified component to the layout. Not used by this class.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the name of the component
**Parameters:** c

- the component to be added

---

#### addLayoutComponent

public void addLayoutComponent​(

String

name,

Component

c)

Adds the specified component to the layout. Not used by this class.

removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
c)
```

Removes the specified component from the layout. Not used by
this class.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** c

- the component to remove

---

#### removeLayoutComponent

public void removeLayoutComponent​(

Component

c)

Removes the specified component from the layout. Not used by
this class.

preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
parent)
```

Returns the preferred dimensions for this layout given the components
in the specified target container.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the component which needs to be laid out
**Returns:** a

Dimension

object containing the
preferred dimensions
**See Also:** minimumLayoutSize(java.awt.Container)

---

#### preferredLayoutSize

public

Dimension

preferredLayoutSize​(

Container

parent)

Returns the preferred dimensions for this layout given the components
in the specified target container.

minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
parent)
```

Returns the minimum dimensions needed to layout the components
contained in the specified target container.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** parent

- the component which needs to be laid out
**Returns:** a

Dimension

object containing the minimum
dimensions
**See Also:** preferredLayoutSize(java.awt.Container)

---

#### minimumLayoutSize

public

Dimension

minimumLayoutSize​(

Container

parent)

Returns the minimum dimensions needed to layout the components
contained in the specified target container.

layoutContainer

```java
public void layoutContainer​(
Container
parent)
```

Called by the AWT when the specified container needs to be laid out.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** parent

- the container to lay out
**Throws:** AWTError

- if the target isn't the container specified to the

BoxLayout

constructor

---

#### layoutContainer

public void layoutContainer​(

Container

parent)

Called by the AWT when the specified container needs to be laid out.

---

