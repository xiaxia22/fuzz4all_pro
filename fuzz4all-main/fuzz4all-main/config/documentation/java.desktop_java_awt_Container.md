# Class Container

**Source:** `java.desktop\java\awt\Container.html`

### Class Description

```java
public class
Container

extends
Component
```

A generic Abstract Window Toolkit(AWT) container object is a component
that can contain other AWT components.

Components added to a container are tracked in a list. The order
of the list will define the components' front-to-back stacking order
within the container. If no index is specified when adding a
component to a container, it will be added to the end of the list
(and hence to the bottom of the stacking order).

Note

: For details on the focus subsystem, see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Container()

Constructs a new Container. Containers can be extended directly,
but are lightweight in this case and must be contained by a parent
somewhere higher up in the component tree that is native.
(such as Frame for example).

---

### Method Details

#### public int getComponentCount()

Gets the number of components in this panel.

Note: This method should be called under AWT tree lock.

**Returns:**
- the number of components in this panel.

**See Also:**
- getComponent(int)

,

Component.getTreeLock()

**Since:**
- 1.1

---

#### @Deprecated

public int countComponents()

Returns the number of components in this container.

**Returns:**
- the number of components in this container

---

#### public
Component
getComponent​(int n)

Gets the nth component in this container.

Note: This method should be called under AWT tree lock.

**Parameters:**
- n

- the index of the component to get.

**Returns:**
- the n

th

component in this container.

**Throws:**
- ArrayIndexOutOfBoundsException

- if the n

th

value does not exist.

**See Also:**
- Component.getTreeLock()

---

#### public
Component
[] getComponents()

Gets all the components in this container.

Note: This method should be called under AWT tree lock.

**Returns:**
- an array of all the components in this container.

**See Also:**
- Component.getTreeLock()

---

#### public
Insets
getInsets()

Determines the insets of this container, which indicate the size
of the container's border.

A

Frame

object, for example, has a top inset that
corresponds to the height of the frame's title bar.

**Returns:**
- the insets of this container.

**See Also:**
- Insets

,

LayoutManager

**Since:**
- 1.1

---

#### @Deprecated

public
Insets
insets()

Returns the insets for this container.

**Returns:**
- the insets for this container

---

#### public
Component
add​(
Component
comp)

Appends the specified component to the end of this container.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:**
- comp

- the component to be added

**Returns:**
- the component argument

**Throws:**
- NullPointerException

- if

comp

is

null

**See Also:**
- addImpl(java.awt.Component, java.lang.Object, int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

---

#### public
Component
add​(
String
name,

Component
comp)

Adds the specified component to this container.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method is obsolete as of 1.1. Please use the
method

add(Component, Object)

instead.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:**
- name

- the name of the component to be added
- comp

- the component to be added

**Returns:**
- the component added

**Throws:**
- NullPointerException

- if

comp

is

null

**See Also:**
- add(Component, Object)

,

invalidate()

---

#### public
Component
add​(
Component
comp,
int index)

Adds the specified component to this container at the given
position.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:**
- comp

- the component to be added
- index

- the position at which to insert the component,
or

-1

to append the component to the end

**Returns:**
- the component

comp

**Throws:**
- NullPointerException

- if

comp

is

null
- IllegalArgumentException

- if

index

is invalid (see

addImpl(java.awt.Component, java.lang.Object, int)

for details)

**See Also:**
- addImpl(java.awt.Component, java.lang.Object, int)

,

remove(int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

---

#### public void setComponentZOrder​(
Component
comp,
int index)

Moves the specified component to the specified z-order index in
the container. The z-order determines the order that components
are painted; the component with the highest z-order paints first
and the component with the lowest z-order paints last.
Where components overlap, the component with the lower
z-order paints over the component with the higher z-order.

If the component is a child of some other container, it is
removed from that container before being added to this container.
The important difference between this method and

java.awt.Container.add(Component, int)

is that this method
doesn't call

removeNotify

on the component while
removing it from its previous container unless necessary and when
allowed by the underlying native windowing system. This way, if the
component has the keyboard focus, it maintains the focus when
moved to the new position.

This property is guaranteed to apply only to lightweight
non-

Container

components.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

Note

: Not all platforms support changing the z-order of
heavyweight components from one container into another without
the call to

removeNotify

. There is no way to detect
whether a platform supports this, so developers shouldn't make
any assumptions.

**Parameters:**
- comp

- the component to be moved
- index

- the position in the container's list to
insert the component, where

getComponentCount()

appends to the end

**Throws:**
- NullPointerException

- if

comp

is

null
- IllegalArgumentException

- if

comp

is one of the
container's parents
- IllegalArgumentException

- if

index

is not in
the range

[0, getComponentCount()]

for moving
between containers, or not in the range

[0, getComponentCount()-1]

for moving inside
a container
- IllegalArgumentException

- if adding a container to itself
- IllegalArgumentException

- if adding a

Window

to a container

**See Also:**
- getComponentZOrder(java.awt.Component)

,

invalidate()

**Since:**
- 1.5

---

#### public int getComponentZOrder​(
Component
comp)

Returns the z-order index of the component inside the container.
The higher a component is in the z-order hierarchy, the lower
its index. The component with the lowest z-order index is
painted last, above all other child components.

**Parameters:**
- comp

- the component being queried

**Returns:**
- the z-order index of the component; otherwise
returns -1 if the component is

null

or doesn't belong to the container

**See Also:**
- setComponentZOrder(java.awt.Component, int)

**Since:**
- 1.5

---

#### public void add​(
Component
comp,

Object
constraints)

Adds the specified component to the end of this container.
Also notifies the layout manager to add the component to
this container's layout using the specified constraints object.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:**
- comp

- the component to be added
- constraints

- an object expressing
layout constraints for this component

**Throws:**
- NullPointerException

- if

comp

is

null

**See Also:**
- addImpl(java.awt.Component, java.lang.Object, int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

,

LayoutManager

**Since:**
- 1.1

---

#### public void add​(
Component
comp,

Object
constraints,
int index)

Adds the specified component to this container with the specified
constraints at the specified index. Also notifies the layout
manager to add the component to the this container's layout using
the specified constraints object.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:**
- comp

- the component to be added
- constraints

- an object expressing layout constraints for this
- index

- the position in the container's list at which to insert
the component;

-1

means insert at the end
component

**Throws:**
- NullPointerException

- if

comp

is

null
- IllegalArgumentException

- if

index

is invalid (see

addImpl(java.awt.Component, java.lang.Object, int)

for details)

**See Also:**
- addImpl(java.awt.Component, java.lang.Object, int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

,

remove(int)

,

LayoutManager

---

#### protected void addImpl​(
Component
comp,

Object
constraints,
int index)

Adds the specified component to this container at the specified
index. This method also notifies the layout manager to add
the component to this container's layout using the specified
constraints object via the

addLayoutComponent

method.

The constraints are
defined by the particular layout manager being used. For
example, the

BorderLayout

class defines five
constraints:

BorderLayout.NORTH

,

BorderLayout.SOUTH

,

BorderLayout.EAST

,

BorderLayout.WEST

, and

BorderLayout.CENTER

.

The

GridBagLayout

class requires a

GridBagConstraints

object. Failure to pass
the correct type of constraints object results in an

IllegalArgumentException

.

If the current layout manager implements

LayoutManager2

, then

LayoutManager2.addLayoutComponent(Component,Object)

is invoked on
it. If the current layout manager does not implement

LayoutManager2

, and constraints is a

String

, then

LayoutManager.addLayoutComponent(String,Component)

is invoked on it.

If the component is not an ancestor of this container and has a non-null
parent, it is removed from its current parent before it is added to this
container.

This is the method to override if a program needs to track
every add request to a container as all other add methods defer
to this one. An overriding method should
usually include a call to the superclass's version of the method:

super.addImpl(comp, constraints, index)

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:**
- comp

- the component to be added
- constraints

- an object expressing layout constraints
for this component
- index

- the position in the container's list at which to
insert the component, where

-1

means append to the end

**Throws:**
- IllegalArgumentException

- if

index

is invalid;
if

comp

is a child of this container, the valid
range is

[-1, getComponentCount()-1]

; if component is
not a child of this container, the valid range is

[-1, getComponentCount()]
- IllegalArgumentException

- if

comp

is an ancestor of
this container
- IllegalArgumentException

- if adding a window to a container
- NullPointerException

- if

comp

is

null

**See Also:**
- add(Component)

,

add(Component, int)

,

add(Component, java.lang.Object)

,

invalidate()

,

LayoutManager

,

LayoutManager2

**Since:**
- 1.1

---

#### public void remove​(int index)

Removes the component, specified by

index

,
from this container.
This method also notifies the layout manager to remove the
component from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

**Parameters:**
- index

- the index of the component to be removed

**Throws:**
- ArrayIndexOutOfBoundsException

- if

index

is not in
range

[0, getComponentCount()-1]

**See Also:**
- add(java.awt.Component)

,

invalidate()

,

validate()

,

getComponentCount()

**Since:**
- 1.1

---

#### public void remove​(
Component
comp)

Removes the specified component from this container.
This method also notifies the layout manager to remove the
component from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

**Parameters:**
- comp

- the component to be removed

**Throws:**
- NullPointerException

- if

comp

is

null

**See Also:**
- add(java.awt.Component)

,

invalidate()

,

validate()

,

remove(int)

---

#### public void removeAll()

Removes all the components from this container.
This method also notifies the layout manager to remove the
components from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

**See Also:**
- add(java.awt.Component)

,

remove(int)

,

invalidate()

---

#### public
LayoutManager
getLayout()

Gets the layout manager for this container.

**Returns:**
- the current layout manager for this container

**See Also:**
- doLayout()

,

setLayout(java.awt.LayoutManager)

---

#### public void setLayout​(
LayoutManager
mgr)

Sets the layout manager for this container.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:**
- mgr

- the specified layout manager

**See Also:**
- doLayout()

,

getLayout()

,

invalidate()

---

#### public void doLayout()

Causes this container to lay out its components. Most programs
should not call this method directly, but should invoke
the

validate

method instead.

**Overrides:**
- doLayout

in class

Component

**See Also:**
- LayoutManager.layoutContainer(java.awt.Container)

,

setLayout(java.awt.LayoutManager)

,

validate()

**Since:**
- 1.1

---

#### @Deprecated

public void layout()

**Overrides:**
- layout

in class

Component

---

#### public boolean isValidateRoot()

Indicates if this container is a

validate root

.

Layout-related changes, such as bounds of the validate root descendants,
do not affect the layout of the validate root parent. This peculiarity
enables the

invalidate()

method to stop invalidating the
component hierarchy when the method encounters a validate root. However,
to preserve backward compatibility this new optimized behavior is
enabled only when the

java.awt.smartInvalidate

system property
value is set to

true

.

If a component hierarchy contains validate roots and the new optimized

invalidate()

behavior is enabled, the

validate()

method
must be invoked on the validate root of a previously invalidated
component to restore the validity of the hierarchy later. Otherwise,
calling the

validate()

method on the top-level container (such
as a

Frame

object) should be used to restore the validity of the
component hierarchy.

The

Window

class and the

Applet

class are the validate
roots in AWT. Swing introduces more validate roots.

**Returns:**
- whether this container is a validate root

**See Also:**
- invalidate()

,

Component.invalidate()

,

JComponent.isValidateRoot()

,

JComponent.revalidate()

**Since:**
- 1.7

---

#### public void invalidate()

Invalidates the container.

If the

LayoutManager

installed on this container is an instance
of the

LayoutManager2

interface, then
the

LayoutManager2.invalidateLayout(Container)

method is invoked
on it supplying this

Container

as the argument.

Afterwards this method marks this container invalid, and invalidates its
ancestors. See the

Component.invalidate()

method for more details.

**Overrides:**
- invalidate

in class

Component

**See Also:**
- validate()

,

layout()

,

LayoutManager2

---

#### public void validate()

Validates this container and all of its subcomponents.

Validating a container means laying out its subcomponents.
Layout-related changes, such as setting the bounds of a component, or
adding a component to the container, invalidate the container
automatically. Note that the ancestors of the container may be
invalidated also (see

Component.invalidate()

for details.)
Therefore, to restore the validity of the hierarchy, the

validate()

method should be invoked on the top-most invalid
container of the hierarchy.

Validating the container may be a quite time-consuming operation. For
performance reasons a developer may postpone the validation of the
hierarchy till a set of layout-related operations completes, e.g. after
adding all the children to the container.

If this

Container

is not valid, this method invokes
the

validateTree

method and marks this

Container

as valid. Otherwise, no action is performed.

**Overrides:**
- validate

in class

Component

**See Also:**
- add(java.awt.Component)

,

invalidate()

,

isValidateRoot()

,

JComponent.revalidate()

,

validateTree()

---

#### protected void validateTree()

Recursively descends the container tree and recomputes the
layout for any subtrees marked as needing it (those marked as
invalid). Synchronization should be provided by the method
that calls this one:

validate

.

**See Also:**
- doLayout()

,

validate()

---

#### public void setFont​(
Font
f)

Sets the font of this container.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Overrides:**
- setFont

in class

Component

**Parameters:**
- f

- The font to become this container's font.

**See Also:**
- Component.getFont()

,

invalidate()

**Since:**
- 1.0

---

#### public
Dimension
getPreferredSize()

Returns the preferred size of this container. If the preferred size has
not been set explicitly by

Component.setPreferredSize(Dimension)

and this

Container

has a

non-null

LayoutManager

,
then

LayoutManager.preferredLayoutSize(Container)

is used to calculate the preferred size.

Note: some implementations may cache the value returned from the

LayoutManager

. Implementations that cache need not invoke

preferredLayoutSize

on the

LayoutManager

every time
this method is invoked, rather the

LayoutManager

will only
be queried after the

Container

becomes invalid.

**Overrides:**
- getPreferredSize

in class

Component

**Returns:**
- an instance of

Dimension

that represents
the preferred size of this container.

**See Also:**
- getMinimumSize()

,

getMaximumSize()

,

getLayout()

,

LayoutManager.preferredLayoutSize(Container)

,

Component.getPreferredSize()

---

#### @Deprecated

public
Dimension
preferredSize()

Description copied from class:

Component

**Overrides:**
- preferredSize

in class

Component

**Returns:**
- the component's preferred size

---

#### public
Dimension
getMinimumSize()

Returns the minimum size of this container. If the minimum size has
not been set explicitly by

Component.setMinimumSize(Dimension)

and this

Container

has a

non-null

LayoutManager

,
then

LayoutManager.minimumLayoutSize(Container)

is used to calculate the minimum size.

Note: some implementations may cache the value returned from the

LayoutManager

. Implementations that cache need not invoke

minimumLayoutSize

on the

LayoutManager

every time
this method is invoked, rather the

LayoutManager

will only
be queried after the

Container

becomes invalid.

**Overrides:**
- getMinimumSize

in class

Component

**Returns:**
- an instance of

Dimension

that represents
the minimum size of this container.

**See Also:**
- getPreferredSize()

,

getMaximumSize()

,

getLayout()

,

LayoutManager.minimumLayoutSize(Container)

,

Component.getMinimumSize()

**Since:**
- 1.1

---

#### @Deprecated

public
Dimension
minimumSize()

Description copied from class:

Component

**Overrides:**
- minimumSize

in class

Component

**Returns:**
- the minimum size of this component

---

#### public
Dimension
getMaximumSize()

Returns the maximum size of this container. If the maximum size has
not been set explicitly by

Component.setMaximumSize(Dimension)

and the

LayoutManager

installed on this

Container

is an instance of

LayoutManager2

, then

LayoutManager2.maximumLayoutSize(Container)

is used to calculate the maximum size.

Note: some implementations may cache the value returned from the

LayoutManager2

. Implementations that cache need not invoke

maximumLayoutSize

on the

LayoutManager2

every time
this method is invoked, rather the

LayoutManager2

will only
be queried after the

Container

becomes invalid.

**Overrides:**
- getMaximumSize

in class

Component

**Returns:**
- an instance of

Dimension

that represents
the maximum size of this container.

**See Also:**
- getPreferredSize()

,

getMinimumSize()

,

getLayout()

,

LayoutManager2.maximumLayoutSize(Container)

,

Component.getMaximumSize()

---

#### public float getAlignmentX()

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Overrides:**
- getAlignmentX

in class

Component

**Returns:**
- the horizontal alignment of this component

---

#### public float getAlignmentY()

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Overrides:**
- getAlignmentY

in class

Component

**Returns:**
- the vertical alignment of this component

---

#### public void paint​(
Graphics
g)

Paints the container. This forwards the paint to any lightweight
components that are children of this container. If this method is
reimplemented, super.paint(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, paint() will not be
forwarded to that child.

**Overrides:**
- paint

in class

Component

**Parameters:**
- g

- the specified Graphics window

**See Also:**
- Component.update(Graphics)

---

#### public void update​(
Graphics
g)

Updates the container. This forwards the update to any lightweight
components that are children of this container. If this method is
reimplemented, super.update(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, update() will not be
forwarded to that child.

**Overrides:**
- update

in class

Component

**Parameters:**
- g

- the specified Graphics window

**See Also:**
- Component.update(Graphics)

---

#### public void print​(
Graphics
g)

Prints the container. This forwards the print to any lightweight
components that are children of this container. If this method is
reimplemented, super.print(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, print() will not be
forwarded to that child.

**Overrides:**
- print

in class

Component

**Parameters:**
- g

- the specified Graphics window

**See Also:**
- Component.update(Graphics)

---

#### public void paintComponents​(
Graphics
g)

Paints each of the components in this container.

**Parameters:**
- g

- the graphics context.

**See Also:**
- Component.paint(java.awt.Graphics)

,

Component.paintAll(java.awt.Graphics)

---

#### public void printComponents​(
Graphics
g)

Prints each of the components in this container.

**Parameters:**
- g

- the graphics context.

**See Also:**
- Component.print(java.awt.Graphics)

,

Component.printAll(java.awt.Graphics)

---

#### public void addContainerListener​(
ContainerListener
l)

Adds the specified container listener to receive container events
from this container.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the container listener

**See Also:**
- removeContainerListener(java.awt.event.ContainerListener)

,

getContainerListeners()

---

#### public void removeContainerListener​(
ContainerListener
l)

Removes the specified container listener so it no longer receives
container events from this container.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the container listener

**See Also:**
- addContainerListener(java.awt.event.ContainerListener)

,

getContainerListeners()

---

#### public
ContainerListener
[] getContainerListeners()

Returns an array of all the container listeners
registered on this container.

**Returns:**
- all of this container's

ContainerListener

s
or an empty array if no container
listeners are currently registered

**See Also:**
- addContainerListener(java.awt.event.ContainerListener)

,

removeContainerListener(java.awt.event.ContainerListener)

**Since:**
- 1.4

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Container

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Container c

for its container listeners with the following code:

```java
ContainerListener[] cls = (ContainerListener[])(c.getListeners(ContainerListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:**
- getListeners

in class

Component

**Parameters:**
- listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener

**Returns:**
- an array of all objects registered as

Foo

Listener

s on this container,
or an empty array if no such listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
- NullPointerException

- if

listenerType

is

null

**See Also:**
- getContainerListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the type of the listeners

---

#### protected void processEvent​(
AWTEvent
e)

Processes events on this container. If the event is a

ContainerEvent

, it invokes the

processContainerEvent

method, else it invokes
its superclass's

processEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:**
- processEvent

in class

Component

**Parameters:**
- e

- the event

**See Also:**
- Component.processComponentEvent(java.awt.event.ComponentEvent)

,

Component.processFocusEvent(java.awt.event.FocusEvent)

,

Component.processKeyEvent(java.awt.event.KeyEvent)

,

Component.processMouseEvent(java.awt.event.MouseEvent)

,

Component.processMouseMotionEvent(java.awt.event.MouseEvent)

,

Component.processInputMethodEvent(java.awt.event.InputMethodEvent)

,

Component.processHierarchyEvent(java.awt.event.HierarchyEvent)

,

Component.processMouseWheelEvent(java.awt.event.MouseWheelEvent)

---

#### protected void processContainerEvent​(
ContainerEvent
e)

Processes container events occurring on this container by
dispatching them to any registered ContainerListener objects.
NOTE: This method will not be called unless container events
are enabled for this component; this happens when one of the
following occurs:

- A ContainerListener object is registered via

addContainerListener

Container events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the container event

**See Also:**
- Component.enableEvents(long)

---

#### @Deprecated

public void deliverEvent​(
Event
e)

**Overrides:**
- deliverEvent

in class

Component

**Parameters:**
- e

- the event to deliver

---

#### public
Component
getComponentAt​(int x,
int y)

Locates the component that contains the x,y position. The
top-most child component is returned in the case where there
is overlap in the components. This is determined by finding
the component closest to the index 0 that claims to contain
the given point via Component.contains(), except that Components
which have native peers take precedence over those which do not
(i.e., lightweight Components).

**Overrides:**
- getComponentAt

in class

Component

**Parameters:**
- x

- the

x

coordinate
- y

- the

y

coordinate

**Returns:**
- null if the component does not contain the position.
If there is no child component at the requested point and the
point is within the bounds of the container the container itself
is returned; otherwise the top-most child is returned.

**See Also:**
- Component.contains(int, int)

**Since:**
- 1.1

---

#### @Deprecated

public
Component
locate​(int x,
int y)

Description copied from class:

Component

**Overrides:**
- locate

in class

Component

**Parameters:**
- x

- the

x

coordinate to search for components at
- y

- the

y

coordinate to search for components at

**Returns:**
- the component at the specified location or

null

---

#### public
Component
getComponentAt​(
Point
p)

Gets the component that contains the specified point.

**Overrides:**
- getComponentAt

in class

Component

**Parameters:**
- p

- the point.

**Returns:**
- returns the component that contains the point,
or

null

if the component does
not contain the point.

**See Also:**
- Component.contains(int, int)

**Since:**
- 1.1

---

#### public
Point
getMousePosition​(boolean allowChildren)
throws
HeadlessException

Returns the position of the mouse pointer in this

Container

's
coordinate space if the

Container

is under the mouse pointer,
otherwise returns

null

.
This method is similar to

Component.getMousePosition()

with the exception
that it can take the

Container

's children into account.
If

allowChildren

is

false

, this method will return
a non-null value only if the mouse pointer is above the

Container

directly, not above the part obscured by children.
If

allowChildren

is

true

, this method returns
a non-null value if the mouse pointer is above

Container

or any
of its descendants.

**Parameters:**
- allowChildren

- true if children should be taken into account

**Returns:**
- mouse coordinates relative to this

Component

, or null

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless() returns true

**See Also:**
- Component.getMousePosition()

**Since:**
- 1.5

---

#### public
Component
findComponentAt​(int x,
int y)

Locates the visible child component that contains the specified
position. The top-most child component is returned in the case
where there is overlap in the components. If the containing child
component is a Container, this method will continue searching for
the deepest nested child component. Components which are not
visible are ignored during the search.

The findComponentAt method is different from getComponentAt in
that getComponentAt only searches the Container's immediate
children; if the containing component is a Container,
findComponentAt will search that child to find a nested component.

**Parameters:**
- x

- the

x

coordinate
- y

- the

y

coordinate

**Returns:**
- null if the component does not contain the position.
If there is no child component at the requested point and the
point is within the bounds of the container the container itself
is returned.

**See Also:**
- Component.contains(int, int)

,

getComponentAt(int, int)

**Since:**
- 1.2

---

#### public
Component
findComponentAt​(
Point
p)

Locates the visible child component that contains the specified
point. The top-most child component is returned in the case
where there is overlap in the components. If the containing child
component is a Container, this method will continue searching for
the deepest nested child component. Components which are not
visible are ignored during the search.

The findComponentAt method is different from getComponentAt in
that getComponentAt only searches the Container's immediate
children; if the containing component is a Container,
findComponentAt will search that child to find a nested component.

**Parameters:**
- p

- the point.

**Returns:**
- null if the component does not contain the position.
If there is no child component at the requested point and the
point is within the bounds of the container the container itself
is returned.

**Throws:**
- NullPointerException

- if

p

is

null

**See Also:**
- Component.contains(int, int)

,

getComponentAt(int, int)

**Since:**
- 1.2

---

#### public void addNotify()

Makes this Container displayable by connecting it to
a native screen resource. Making a container displayable will
cause all of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:**
- addNotify

in class

Component

**See Also:**
- Component.isDisplayable()

,

removeNotify()

---

#### public void removeNotify()

Makes this Container undisplayable by removing its connection
to its native screen resource. Making a container undisplayable
will cause all of its children to be made undisplayable.
This method is called by the toolkit internally and should
not be called directly by programs.

**Overrides:**
- removeNotify

in class

Component

**See Also:**
- Component.isDisplayable()

,

addNotify()

---

#### public boolean isAncestorOf​(
Component
c)

Checks if the component is contained in the component hierarchy of
this container.

**Parameters:**
- c

- the component

**Returns:**
- true

if it is an ancestor;

false

otherwise.

**Since:**
- 1.1

---

#### protected
String
paramString()

Returns a string representing the state of this

Container

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:**
- paramString

in class

Component

**Returns:**
- the parameter string of this container

---

#### public void list​(
PrintStream
out,
int indent)

Prints a listing of this container to the specified output
stream. The listing starts at the specified indentation.

The immediate children of the container are printed with
an indentation of

indent+1

. The children
of those children are printed at

indent+2

and so on.

**Overrides:**
- list

in class

Component

**Parameters:**
- out

- a print stream
- indent

- the number of spaces to indent

**Throws:**
- NullPointerException

- if

out

is

null

**See Also:**
- Component.list(java.io.PrintStream, int)

**Since:**
- 1.0

---

#### public void list​(
PrintWriter
out,
int indent)

Prints out a list, starting at the specified indentation,
to the specified print writer.

The immediate children of the container are printed with
an indentation of

indent+1

. The children
of those children are printed at

indent+2

and so on.

**Overrides:**
- list

in class

Component

**Parameters:**
- out

- a print writer
- indent

- the number of spaces to indent

**Throws:**
- NullPointerException

- if

out

is

null

**See Also:**
- Component.list(java.io.PrintWriter, int)

**Since:**
- 1.1

---

#### public void setFocusTraversalKeys​(int id,

Set
<? extends
AWTKeyStroke
> keystrokes)

Sets the focus traversal keys for a given traversal operation for this
Container.

The default values for a Container's focus traversal keys are
implementation-dependent. Sun recommends that all implementations for a
particular native platform use the same default values. The
recommendations for Windows and Unix are listed below. These
recommendations are used in the Sun AWT implementations.

Recommended default values for a Container's focus traversal
keys

Identifier

Meaning

Default

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

Normal forward keyboard traversal

TAB on KEY_PRESSED, CTRL-TAB on KEY_PRESSED

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

Normal reverse keyboard traversal

SHIFT-TAB on KEY_PRESSED, CTRL-SHIFT-TAB on KEY_PRESSED

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

Go up one focus traversal cycle

none

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

Go down one focus traversal cycle

none

To disable a traversal key, use an empty Set; Collections.EMPTY_SET is
recommended.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Container. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Container inherits the
Set from its parent. If all ancestors of this Container have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

**Overrides:**
- setFocusTraversalKeys

in class

Component

**Parameters:**
- id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
- keystrokes

- the Set of AWTKeyStroke for the specified operation

**Throws:**
- IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS, or if keystrokes
contains null, or if any keystroke represents a KEY_TYPED event,
or if any keystroke already maps to another focus traversal
operation for this Container

**See Also:**
- getFocusTraversalKeys(int)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

,

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

**Since:**
- 1.4

---

#### public
Set
<
AWTKeyStroke
> getFocusTraversalKeys​(int id)

Returns the Set of focus traversal keys for a given traversal operation
for this Container. (See

setFocusTraversalKeys

for a full description of each key.)

If a Set of traversal keys has not been explicitly defined for this
Container, then this Container's parent's Set is returned. If no Set
has been explicitly defined for any of this Container's ancestors, then
the current KeyboardFocusManager's default Set is returned.

**Overrides:**
- getFocusTraversalKeys

in class

Component

**Parameters:**
- id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

**Returns:**
- the Set of AWTKeyStrokes for the specified operation. The Set
will be unmodifiable, and may be empty. null will never be
returned.

**Throws:**
- IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

**See Also:**
- setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

,

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

**Since:**
- 1.4

---

#### public boolean areFocusTraversalKeysSet​(int id)

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Container. If
this method returns

false

, this Container is inheriting the
Set from an ancestor, or from the current KeyboardFocusManager.

**Overrides:**
- areFocusTraversalKeysSet

in class

Component

**Parameters:**
- id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

**Returns:**
- true

if the Set of focus traversal keys for the
given focus traversal operation has been explicitly defined for
this Component;

false

otherwise.

**Throws:**
- IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

**Since:**
- 1.4

---

#### public boolean isFocusCycleRoot​(
Container
container)

Returns whether the specified Container is the focus cycle root of this
Container's focus traversal cycle. Each focus traversal cycle has only
a single focus cycle root and each Container which is not a focus cycle
root belongs to only a single focus traversal cycle. Containers which
are focus cycle roots belong to two cycles: one rooted at the Container
itself, and one rooted at the Container's nearest focus-cycle-root
ancestor. This method will return

true

for both such
Containers in this case.

**Overrides:**
- isFocusCycleRoot

in class

Component

**Parameters:**
- container

- the Container to be tested

**Returns:**
- true

if the specified Container is a focus-cycle-
root of this Container;

false

otherwise

**See Also:**
- isFocusCycleRoot()

**Since:**
- 1.4

---

#### public void setFocusTraversalPolicy​(
FocusTraversalPolicy
policy)

Sets the focus traversal policy that will manage keyboard traversal of
this Container's children, if this Container is a focus cycle root. If
the argument is null, this Container inherits its policy from its focus-
cycle-root ancestor. If the argument is non-null, this policy will be
inherited by all focus-cycle-root children that have no keyboard-
traversal policy of their own (as will, recursively, their focus-cycle-
root children).

If this Container is not a focus cycle root, the policy will be
remembered, but will not be used or inherited by this or any other
Containers until this Container is made a focus cycle root.

**Parameters:**
- policy

- the new focus traversal policy for this Container

**See Also:**
- getFocusTraversalPolicy()

,

setFocusCycleRoot(boolean)

,

isFocusCycleRoot(java.awt.Container)

**Since:**
- 1.4

---

#### public
FocusTraversalPolicy
getFocusTraversalPolicy()

Returns the focus traversal policy that will manage keyboard traversal
of this Container's children, or null if this Container is not a focus
cycle root. If no traversal policy has been explicitly set for this
Container, then this Container's focus-cycle-root ancestor's policy is
returned.

**Returns:**
- this Container's focus traversal policy, or null if this
Container is not a focus cycle root.

**See Also:**
- setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

setFocusCycleRoot(boolean)

,

isFocusCycleRoot(java.awt.Container)

**Since:**
- 1.4

---

#### public boolean isFocusTraversalPolicySet()

Returns whether the focus traversal policy has been explicitly set for
this Container. If this method returns

false

, this
Container will inherit its focus traversal policy from an ancestor.

**Returns:**
- true

if the focus traversal policy has been
explicitly set for this Container;

false

otherwise.

**Since:**
- 1.4

---

#### public void setFocusCycleRoot​(boolean focusCycleRoot)

Sets whether this Container is the root of a focus traversal cycle. Once
focus enters a traversal cycle, typically it cannot leave it via focus
traversal unless one of the up- or down-cycle keys is pressed. Normal
traversal is limited to this Container, and all of this Container's
descendants that are not descendants of inferior focus cycle roots. Note
that a FocusTraversalPolicy may bend these restrictions, however. For
example, ContainerOrderFocusTraversalPolicy supports implicit down-cycle
traversal.

The alternative way to specify the traversal order of this Container's
children is to make this Container a

focus traversal policy provider

.

**Parameters:**
- focusCycleRoot

- indicates whether this Container is the root of a
focus traversal cycle

**See Also:**
- isFocusCycleRoot()

,

setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

ContainerOrderFocusTraversalPolicy

,

setFocusTraversalPolicyProvider(boolean)

**Since:**
- 1.4

---

#### public boolean isFocusCycleRoot()

Returns whether this Container is the root of a focus traversal cycle.
Once focus enters a traversal cycle, typically it cannot leave it via
focus traversal unless one of the up- or down-cycle keys is pressed.
Normal traversal is limited to this Container, and all of this
Container's descendants that are not descendants of inferior focus
cycle roots. Note that a FocusTraversalPolicy may bend these
restrictions, however. For example, ContainerOrderFocusTraversalPolicy
supports implicit down-cycle traversal.

**Returns:**
- whether this Container is the root of a focus traversal cycle

**See Also:**
- setFocusCycleRoot(boolean)

,

setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

ContainerOrderFocusTraversalPolicy

**Since:**
- 1.4

---

#### public final void setFocusTraversalPolicyProvider​(boolean provider)

Sets whether this container will be used to provide focus
traversal policy. Container with this property as

true

will be used to acquire focus traversal policy
instead of closest focus cycle root ancestor.

**Parameters:**
- provider

- indicates whether this container will be used to
provide focus traversal policy

**See Also:**
- setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

isFocusTraversalPolicyProvider()

**Since:**
- 1.5

---

#### public final boolean isFocusTraversalPolicyProvider()

Returns whether this container provides focus traversal
policy. If this property is set to

true

then when
keyboard focus manager searches container hierarchy for focus
traversal policy and encounters this container before any other
container with this property as true or focus cycle roots then
its focus traversal policy will be used instead of focus cycle
root's policy.

**Returns:**
- true

if this container provides focus traversal
policy,

false

otherwise

**See Also:**
- setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

setFocusCycleRoot(boolean)

,

setFocusTraversalPolicyProvider(boolean)

**Since:**
- 1.5

---

#### public void transferFocusDownCycle()

Transfers the focus down one focus traversal cycle. If this Container is
a focus cycle root, then the focus owner is set to this Container's
default Component to focus, and the current focus cycle root is set to
this Container. If this Container is not a focus cycle root, then no
focus traversal operation occurs.

**See Also:**
- Component.requestFocus()

,

isFocusCycleRoot(java.awt.Container)

,

setFocusCycleRoot(boolean)

**Since:**
- 1.4

---

#### public void applyComponentOrientation​(
ComponentOrientation
o)

Sets the

ComponentOrientation

property of this container
and all components contained within it.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Overrides:**
- applyComponentOrientation

in class

Component

**Parameters:**
- o

- the new component orientation of this container and
the components contained within it.

**Throws:**
- NullPointerException

- if

orientation

is null.

**See Also:**
- Component.setComponentOrientation(java.awt.ComponentOrientation)

,

Component.getComponentOrientation()

,

invalidate()

**Since:**
- 1.4

---

#### public void addPropertyChangeListener​(
PropertyChangeListener
listener)

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Container's font ("font")
- this Container's background color ("background")
- this Container's foreground color ("foreground")
- this Container's focusability ("focusable")
- this Container's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Container's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Container's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Container's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Container's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Container's focus traversal policy ("focusTraversalPolicy")
- this Container's focus-cycle-root state ("focusCycleRoot")

Note that if this Container is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:**
- addPropertyChangeListener

in class

Component

**Parameters:**
- listener

- the PropertyChangeListener to be added

**See Also:**
- Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

,

addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)

---

#### public void addPropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following defaults:

- this Container's font ("font")
- this Container's background color ("background")
- this Container's foreground color ("foreground")
- this Container's focusability ("focusable")
- this Container's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Container's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Container's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Container's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Container's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Container's focus traversal policy ("focusTraversalPolicy")
- this Container's focus-cycle-root state ("focusCycleRoot")
- this Container's focus-traversal-policy-provider state("focusTraversalPolicyProvider")
- this Container's focus-traversal-policy-provider state("focusTraversalPolicyProvider")

Note that if this Container is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:**
- addPropertyChangeListener

in class

Component

**Parameters:**
- propertyName

- one of the property names listed above
- listener

- the PropertyChangeListener to be added

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

---

### Additional Sections

#### Class Container

java.lang.Object

- java.awt.Component
- - java.awt.Container

java.awt.Component

- java.awt.Container

java.awt.Container

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

**Direct Known Subclasses:** BasicSplitPaneDivider

,

CellRendererPane

,

DefaultTreeCellEditor.EditorContainer

,

JComponent

,

Panel

,

ScrollPane

,

Window

```java
public class
Container

extends
Component
```

A generic Abstract Window Toolkit(AWT) container object is a component
that can contain other AWT components.

Components added to a container are tracked in a list. The order
of the list will define the components' front-to-back stacking order
within the container. If no index is specified when adding a
component to a container, it will be added to the end of the list
(and hence to the bottom of the stacking order).

Note

: For details on the focus subsystem, see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

**Since:** 1.0
**See Also:** add(java.awt.Component, int)

,

getComponent(int)

,

LayoutManager

,

Serialized Form

public class

Container

extends

Component

A generic Abstract Window Toolkit(AWT) container object is a component
that can contain other AWT components.

Components added to a container are tracked in a list. The order
of the list will define the components' front-to-back stacking order
within the container. If no index is specified when adding a
component to a container, it will be added to the end of the list
(and hence to the bottom of the stacking order).

Note

: For details on the focus subsystem, see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

Components added to a container are tracked in a list. The order
of the list will define the components' front-to-back stacking order
within the container. If no index is specified when adding a
component to a container, it will be added to the end of the list
(and hence to the bottom of the stacking order).

Note

: For details on the focus subsystem, see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

Note

: For details on the focus subsystem, see

How to Use the Focus Subsystem

,
a section in

The Java Tutorial

, and the

Focus Specification

for more information.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Container.AccessibleAWTContainer

Inner class of Container used to provide default support for
accessibility.

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Container

()

Constructs a new Container.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Component

add

​(

Component

comp)

Appends the specified component to the end of this container.

Component

add

​(

Component

comp,
int index)

Adds the specified component to this container at the given
position.

void

add

​(

Component

comp,

Object

constraints)

Adds the specified component to the end of this container.

void

add

​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this container with the specified
constraints at the specified index.

Component

add

​(

String

name,

Component

comp)

Adds the specified component to this container.

void

addContainerListener

​(

ContainerListener

l)

Adds the specified container listener to receive container events
from this container.

protected void

addImpl

​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this container at the specified
index.

void

addNotify

()

Makes this Container displayable by connecting it to
a native screen resource.

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list.

void

addPropertyChangeListener

​(

String

propertyName,

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list for a specific
property.

void

applyComponentOrientation

​(

ComponentOrientation

o)

Sets the

ComponentOrientation

property of this container
and all components contained within it.

boolean

areFocusTraversalKeysSet

​(int id)

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Container.

int

countComponents

()

Deprecated.

As of JDK version 1.1,
replaced by getComponentCount().

void

deliverEvent

​(

Event

e)

Deprecated.

As of JDK version 1.1,
replaced by

dispatchEvent(AWTEvent e)

void

doLayout

()

Causes this container to lay out its components.

Component

findComponentAt

​(int x,
int y)

Locates the visible child component that contains the specified
position.

Component

findComponentAt

​(

Point

p)

Locates the visible child component that contains the specified
point.

float

getAlignmentX

()

Returns the alignment along the x axis.

float

getAlignmentY

()

Returns the alignment along the y axis.

Component

getComponent

​(int n)

Gets the nth component in this container.

Component

getComponentAt

​(int x,
int y)

Locates the component that contains the x,y position.

Component

getComponentAt

​(

Point

p)

Gets the component that contains the specified point.

int

getComponentCount

()

Gets the number of components in this panel.

Component

[]

getComponents

()

Gets all the components in this container.

int

getComponentZOrder

​(

Component

comp)

Returns the z-order index of the component inside the container.

ContainerListener

[]

getContainerListeners

()

Returns an array of all the container listeners
registered on this container.

Set

<

AWTKeyStroke

>

getFocusTraversalKeys

​(int id)

Returns the Set of focus traversal keys for a given traversal operation
for this Container.

FocusTraversalPolicy

getFocusTraversalPolicy

()

Returns the focus traversal policy that will manage keyboard traversal
of this Container's children, or null if this Container is not a focus
cycle root.

Insets

getInsets

()

Determines the insets of this container, which indicate the size
of the container's border.

LayoutManager

getLayout

()

Gets the layout manager for this container.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Container

.

Dimension

getMaximumSize

()

Returns the maximum size of this container.

Dimension

getMinimumSize

()

Returns the minimum size of this container.

Point

getMousePosition

​(boolean allowChildren)

Returns the position of the mouse pointer in this

Container

's
coordinate space if the

Container

is under the mouse pointer,
otherwise returns

null

.

Dimension

getPreferredSize

()

Returns the preferred size of this container.

Insets

insets

()

Deprecated.

As of JDK version 1.1,
replaced by

getInsets()

.

void

invalidate

()

Invalidates the container.

boolean

isAncestorOf

​(

Component

c)

Checks if the component is contained in the component hierarchy of
this container.

boolean

isFocusCycleRoot

()

Returns whether this Container is the root of a focus traversal cycle.

boolean

isFocusCycleRoot

​(

Container

container)

Returns whether the specified Container is the focus cycle root of this
Container's focus traversal cycle.

boolean

isFocusTraversalPolicyProvider

()

Returns whether this container provides focus traversal
policy.

boolean

isFocusTraversalPolicySet

()

Returns whether the focus traversal policy has been explicitly set for
this Container.

boolean

isValidateRoot

()

Indicates if this container is a

validate root

.

void

layout

()

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

void

list

​(

PrintStream

out,
int indent)

Prints a listing of this container to the specified output
stream.

void

list

​(

PrintWriter

out,
int indent)

Prints out a list, starting at the specified indentation,
to the specified print writer.

Component

locate

​(int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by

getComponentAt(int, int)

.

Dimension

minimumSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

void

paint

​(

Graphics

g)

Paints the container.

void

paintComponents

​(

Graphics

g)

Paints each of the components in this container.

protected

String

paramString

()

Returns a string representing the state of this

Container

.

Dimension

preferredSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

void

print

​(

Graphics

g)

Prints the container.

void

printComponents

​(

Graphics

g)

Prints each of the components in this container.

protected void

processContainerEvent

​(

ContainerEvent

e)

Processes container events occurring on this container by
dispatching them to any registered ContainerListener objects.

protected void

processEvent

​(

AWTEvent

e)

Processes events on this container.

void

remove

​(int index)

Removes the component, specified by

index

,
from this container.

void

remove

​(

Component

comp)

Removes the specified component from this container.

void

removeAll

()

Removes all the components from this container.

void

removeContainerListener

​(

ContainerListener

l)

Removes the specified container listener so it no longer receives
container events from this container.

void

removeNotify

()

Makes this Container undisplayable by removing its connection
to its native screen resource.

void

setComponentZOrder

​(

Component

comp,
int index)

Moves the specified component to the specified z-order index in
the container.

void

setFocusCycleRoot

​(boolean focusCycleRoot)

Sets whether this Container is the root of a focus traversal cycle.

void

setFocusTraversalKeys

​(int id,

Set

<? extends

AWTKeyStroke

> keystrokes)

Sets the focus traversal keys for a given traversal operation for this
Container.

void

setFocusTraversalPolicy

​(

FocusTraversalPolicy

policy)

Sets the focus traversal policy that will manage keyboard traversal of
this Container's children, if this Container is a focus cycle root.

void

setFocusTraversalPolicyProvider

​(boolean provider)

Sets whether this container will be used to provide focus
traversal policy.

void

setFont

​(

Font

f)

Sets the font of this container.

void

setLayout

​(

LayoutManager

mgr)

Sets the layout manager for this container.

void

transferFocusDownCycle

()

Transfers the focus down one focus traversal cycle.

void

update

​(

Graphics

g)

Updates the container.

void

validate

()

Validates this container and all of its subcomponents.

protected void

validateTree

()

Recursively descends the container tree and recomputes the
layout for any subtrees marked as needing it (those marked as
invalid).

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disable

,

disableEvents

,

dispatchEvent

,

enable

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getAccessibleContext

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isOpaque

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

printAll

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

Container.AccessibleAWTContainer

Inner class of Container used to provide default support for
accessibility.

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested Class Summary

Inner class of Container used to provide default support for
accessibility.

Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested classes/interfaces declared in class java.awt. Component

Field Summary

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Field Summary

Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

---

#### Fields declared in class java.awt. Component

Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Fields declared in interface java.awt.image. ImageObserver

Constructor Summary

Constructors

Constructor

Description

Container

()

Constructs a new Container.

---

#### Constructor Summary

Constructs a new Container.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Component

add

​(

Component

comp)

Appends the specified component to the end of this container.

Component

add

​(

Component

comp,
int index)

Adds the specified component to this container at the given
position.

void

add

​(

Component

comp,

Object

constraints)

Adds the specified component to the end of this container.

void

add

​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this container with the specified
constraints at the specified index.

Component

add

​(

String

name,

Component

comp)

Adds the specified component to this container.

void

addContainerListener

​(

ContainerListener

l)

Adds the specified container listener to receive container events
from this container.

protected void

addImpl

​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this container at the specified
index.

void

addNotify

()

Makes this Container displayable by connecting it to
a native screen resource.

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list.

void

addPropertyChangeListener

​(

String

propertyName,

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list for a specific
property.

void

applyComponentOrientation

​(

ComponentOrientation

o)

Sets the

ComponentOrientation

property of this container
and all components contained within it.

boolean

areFocusTraversalKeysSet

​(int id)

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Container.

int

countComponents

()

Deprecated.

As of JDK version 1.1,
replaced by getComponentCount().

void

deliverEvent

​(

Event

e)

Deprecated.

As of JDK version 1.1,
replaced by

dispatchEvent(AWTEvent e)

void

doLayout

()

Causes this container to lay out its components.

Component

findComponentAt

​(int x,
int y)

Locates the visible child component that contains the specified
position.

Component

findComponentAt

​(

Point

p)

Locates the visible child component that contains the specified
point.

float

getAlignmentX

()

Returns the alignment along the x axis.

float

getAlignmentY

()

Returns the alignment along the y axis.

Component

getComponent

​(int n)

Gets the nth component in this container.

Component

getComponentAt

​(int x,
int y)

Locates the component that contains the x,y position.

Component

getComponentAt

​(

Point

p)

Gets the component that contains the specified point.

int

getComponentCount

()

Gets the number of components in this panel.

Component

[]

getComponents

()

Gets all the components in this container.

int

getComponentZOrder

​(

Component

comp)

Returns the z-order index of the component inside the container.

ContainerListener

[]

getContainerListeners

()

Returns an array of all the container listeners
registered on this container.

Set

<

AWTKeyStroke

>

getFocusTraversalKeys

​(int id)

Returns the Set of focus traversal keys for a given traversal operation
for this Container.

FocusTraversalPolicy

getFocusTraversalPolicy

()

Returns the focus traversal policy that will manage keyboard traversal
of this Container's children, or null if this Container is not a focus
cycle root.

Insets

getInsets

()

Determines the insets of this container, which indicate the size
of the container's border.

LayoutManager

getLayout

()

Gets the layout manager for this container.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Container

.

Dimension

getMaximumSize

()

Returns the maximum size of this container.

Dimension

getMinimumSize

()

Returns the minimum size of this container.

Point

getMousePosition

​(boolean allowChildren)

Returns the position of the mouse pointer in this

Container

's
coordinate space if the

Container

is under the mouse pointer,
otherwise returns

null

.

Dimension

getPreferredSize

()

Returns the preferred size of this container.

Insets

insets

()

Deprecated.

As of JDK version 1.1,
replaced by

getInsets()

.

void

invalidate

()

Invalidates the container.

boolean

isAncestorOf

​(

Component

c)

Checks if the component is contained in the component hierarchy of
this container.

boolean

isFocusCycleRoot

()

Returns whether this Container is the root of a focus traversal cycle.

boolean

isFocusCycleRoot

​(

Container

container)

Returns whether the specified Container is the focus cycle root of this
Container's focus traversal cycle.

boolean

isFocusTraversalPolicyProvider

()

Returns whether this container provides focus traversal
policy.

boolean

isFocusTraversalPolicySet

()

Returns whether the focus traversal policy has been explicitly set for
this Container.

boolean

isValidateRoot

()

Indicates if this container is a

validate root

.

void

layout

()

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

void

list

​(

PrintStream

out,
int indent)

Prints a listing of this container to the specified output
stream.

void

list

​(

PrintWriter

out,
int indent)

Prints out a list, starting at the specified indentation,
to the specified print writer.

Component

locate

​(int x,
int y)

Deprecated.

As of JDK version 1.1,
replaced by

getComponentAt(int, int)

.

Dimension

minimumSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

void

paint

​(

Graphics

g)

Paints the container.

void

paintComponents

​(

Graphics

g)

Paints each of the components in this container.

protected

String

paramString

()

Returns a string representing the state of this

Container

.

Dimension

preferredSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

void

print

​(

Graphics

g)

Prints the container.

void

printComponents

​(

Graphics

g)

Prints each of the components in this container.

protected void

processContainerEvent

​(

ContainerEvent

e)

Processes container events occurring on this container by
dispatching them to any registered ContainerListener objects.

protected void

processEvent

​(

AWTEvent

e)

Processes events on this container.

void

remove

​(int index)

Removes the component, specified by

index

,
from this container.

void

remove

​(

Component

comp)

Removes the specified component from this container.

void

removeAll

()

Removes all the components from this container.

void

removeContainerListener

​(

ContainerListener

l)

Removes the specified container listener so it no longer receives
container events from this container.

void

removeNotify

()

Makes this Container undisplayable by removing its connection
to its native screen resource.

void

setComponentZOrder

​(

Component

comp,
int index)

Moves the specified component to the specified z-order index in
the container.

void

setFocusCycleRoot

​(boolean focusCycleRoot)

Sets whether this Container is the root of a focus traversal cycle.

void

setFocusTraversalKeys

​(int id,

Set

<? extends

AWTKeyStroke

> keystrokes)

Sets the focus traversal keys for a given traversal operation for this
Container.

void

setFocusTraversalPolicy

​(

FocusTraversalPolicy

policy)

Sets the focus traversal policy that will manage keyboard traversal of
this Container's children, if this Container is a focus cycle root.

void

setFocusTraversalPolicyProvider

​(boolean provider)

Sets whether this container will be used to provide focus
traversal policy.

void

setFont

​(

Font

f)

Sets the font of this container.

void

setLayout

​(

LayoutManager

mgr)

Sets the layout manager for this container.

void

transferFocusDownCycle

()

Transfers the focus down one focus traversal cycle.

void

update

​(

Graphics

g)

Updates the container.

void

validate

()

Validates this container and all of its subcomponents.

protected void

validateTree

()

Recursively descends the container tree and recomputes the
layout for any subtrees marked as needing it (those marked as
invalid).

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disable

,

disableEvents

,

dispatchEvent

,

enable

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getAccessibleContext

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isOpaque

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

printAll

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

wait

,

wait

,

wait

---

#### Method Summary

Appends the specified component to the end of this container.

Adds the specified component to this container at the given
position.

Adds the specified component to the end of this container.

Adds the specified component to this container with the specified
constraints at the specified index.

Adds the specified component to this container.

Adds the specified container listener to receive container events
from this container.

Adds the specified component to this container at the specified
index.

Makes this Container displayable by connecting it to
a native screen resource.

Adds a PropertyChangeListener to the listener list.

Adds a PropertyChangeListener to the listener list for a specific
property.

Sets the

ComponentOrientation

property of this container
and all components contained within it.

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Container.

Deprecated.

As of JDK version 1.1,
replaced by getComponentCount().

Deprecated.

As of JDK version 1.1,
replaced by

dispatchEvent(AWTEvent e)

Causes this container to lay out its components.

Locates the visible child component that contains the specified
position.

Locates the visible child component that contains the specified
point.

Returns the alignment along the x axis.

Returns the alignment along the y axis.

Gets the nth component in this container.

Locates the component that contains the x,y position.

Gets the component that contains the specified point.

Gets the number of components in this panel.

Gets all the components in this container.

Returns the z-order index of the component inside the container.

Returns an array of all the container listeners
registered on this container.

Returns the Set of focus traversal keys for a given traversal operation
for this Container.

Returns the focus traversal policy that will manage keyboard traversal
of this Container's children, or null if this Container is not a focus
cycle root.

Determines the insets of this container, which indicate the size
of the container's border.

Gets the layout manager for this container.

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Container

.

Returns the maximum size of this container.

Returns the minimum size of this container.

Returns the position of the mouse pointer in this

Container

's
coordinate space if the

Container

is under the mouse pointer,
otherwise returns

null

.

Returns the preferred size of this container.

Deprecated.

As of JDK version 1.1,
replaced by

getInsets()

.

Invalidates the container.

Checks if the component is contained in the component hierarchy of
this container.

Returns whether this Container is the root of a focus traversal cycle.

Returns whether the specified Container is the focus cycle root of this
Container's focus traversal cycle.

Returns whether this container provides focus traversal
policy.

Returns whether the focus traversal policy has been explicitly set for
this Container.

Indicates if this container is a

validate root

.

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

Prints a listing of this container to the specified output
stream.

Prints out a list, starting at the specified indentation,
to the specified print writer.

Deprecated.

As of JDK version 1.1,
replaced by

getComponentAt(int, int)

.

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Paints the container.

Paints each of the components in this container.

Returns a string representing the state of this

Container

.

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Prints the container.

Prints each of the components in this container.

Processes container events occurring on this container by
dispatching them to any registered ContainerListener objects.

Processes events on this container.

Removes the component, specified by

index

,
from this container.

Removes the specified component from this container.

Removes all the components from this container.

Removes the specified container listener so it no longer receives
container events from this container.

Makes this Container undisplayable by removing its connection
to its native screen resource.

Moves the specified component to the specified z-order index in
the container.

Sets whether this Container is the root of a focus traversal cycle.

Sets the focus traversal keys for a given traversal operation for this
Container.

Sets the focus traversal policy that will manage keyboard traversal of
this Container's children, if this Container is a focus cycle root.

Sets whether this container will be used to provide focus
traversal policy.

Sets the font of this container.

Sets the layout manager for this container.

Transfers the focus down one focus traversal cycle.

Updates the container.

Validates this container and all of its subcomponents.

Recursively descends the container tree and recomputes the
layout for any subtrees marked as needing it (those marked as
invalid).

Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disable

,

disableEvents

,

dispatchEvent

,

enable

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getAccessibleContext

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isOpaque

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

printAll

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

---

#### Methods declared in class java.awt. Component

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Container

```java
public Container()
```

Constructs a new Container. Containers can be extended directly,
but are lightweight in this case and must be contained by a parent
somewhere higher up in the component tree that is native.
(such as Frame for example).

============ METHOD DETAIL ==========

- Method Detail

- getComponentCount

```java
public int getComponentCount()
```

Gets the number of components in this panel.

Note: This method should be called under AWT tree lock.

**Returns:** the number of components in this panel.
**Since:** 1.1
**See Also:** getComponent(int)

,

Component.getTreeLock()

- countComponents

```java
@Deprecated

public int countComponents()
```

Deprecated.

As of JDK version 1.1,
replaced by getComponentCount().

Returns the number of components in this container.

**Returns:** the number of components in this container

- getComponent

```java
public
Component
getComponent​(int n)
```

Gets the nth component in this container.

Note: This method should be called under AWT tree lock.

**Parameters:** n

- the index of the component to get.
**Returns:** the n

th

component in this container.
**Throws:** ArrayIndexOutOfBoundsException

- if the n

th

value does not exist.
**See Also:** Component.getTreeLock()

- getComponents

```java
public
Component
[] getComponents()
```

Gets all the components in this container.

Note: This method should be called under AWT tree lock.

**Returns:** an array of all the components in this container.
**See Also:** Component.getTreeLock()

- getInsets

```java
public
Insets
getInsets()
```

Determines the insets of this container, which indicate the size
of the container's border.

A

Frame

object, for example, has a top inset that
corresponds to the height of the frame's title bar.

**Returns:** the insets of this container.
**Since:** 1.1
**See Also:** Insets

,

LayoutManager

- insets

```java
@Deprecated

public
Insets
insets()
```

Deprecated.

As of JDK version 1.1,
replaced by

getInsets()

.

Returns the insets for this container.

**Returns:** the insets for this container

- add

```java
public
Component
add​(
Component
comp)
```

Appends the specified component to the end of this container.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Returns:** the component argument
**Throws:** NullPointerException

- if

comp

is

null
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

- add

```java
public
Component
add​(
String
name,

Component
comp)
```

Adds the specified component to this container.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method is obsolete as of 1.1. Please use the
method

add(Component, Object)

instead.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** name

- the name of the component to be added
**Parameters:** comp

- the component to be added
**Returns:** the component added
**Throws:** NullPointerException

- if

comp

is

null
**See Also:** add(Component, Object)

,

invalidate()

- add

```java
public
Component
add​(
Component
comp,
int index)
```

Adds the specified component to this container at the given
position.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Parameters:** index

- the position at which to insert the component,
or

-1

to append the component to the end
**Returns:** the component

comp
**Throws:** NullPointerException

- if

comp

is

null
**Throws:** IllegalArgumentException

- if

index

is invalid (see

addImpl(java.awt.Component, java.lang.Object, int)

for details)
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

remove(int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

- setComponentZOrder

```java
public void setComponentZOrder​(
Component
comp,
int index)
```

Moves the specified component to the specified z-order index in
the container. The z-order determines the order that components
are painted; the component with the highest z-order paints first
and the component with the lowest z-order paints last.
Where components overlap, the component with the lower
z-order paints over the component with the higher z-order.

If the component is a child of some other container, it is
removed from that container before being added to this container.
The important difference between this method and

java.awt.Container.add(Component, int)

is that this method
doesn't call

removeNotify

on the component while
removing it from its previous container unless necessary and when
allowed by the underlying native windowing system. This way, if the
component has the keyboard focus, it maintains the focus when
moved to the new position.

This property is guaranteed to apply only to lightweight
non-

Container

components.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

Note

: Not all platforms support changing the z-order of
heavyweight components from one container into another without
the call to

removeNotify

. There is no way to detect
whether a platform supports this, so developers shouldn't make
any assumptions.

**Parameters:** comp

- the component to be moved
**Parameters:** index

- the position in the container's list to
insert the component, where

getComponentCount()

appends to the end
**Throws:** NullPointerException

- if

comp

is

null
**Throws:** IllegalArgumentException

- if

comp

is one of the
container's parents
**Throws:** IllegalArgumentException

- if

index

is not in
the range

[0, getComponentCount()]

for moving
between containers, or not in the range

[0, getComponentCount()-1]

for moving inside
a container
**Throws:** IllegalArgumentException

- if adding a container to itself
**Throws:** IllegalArgumentException

- if adding a

Window

to a container
**Since:** 1.5
**See Also:** getComponentZOrder(java.awt.Component)

,

invalidate()

- getComponentZOrder

```java
public int getComponentZOrder​(
Component
comp)
```

Returns the z-order index of the component inside the container.
The higher a component is in the z-order hierarchy, the lower
its index. The component with the lowest z-order index is
painted last, above all other child components.

**Parameters:** comp

- the component being queried
**Returns:** the z-order index of the component; otherwise
returns -1 if the component is

null

or doesn't belong to the container
**Since:** 1.5
**See Also:** setComponentZOrder(java.awt.Component, int)

- add

```java
public void add​(
Component
comp,

Object
constraints)
```

Adds the specified component to the end of this container.
Also notifies the layout manager to add the component to
this container's layout using the specified constraints object.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing
layout constraints for this component
**Throws:** NullPointerException

- if

comp

is

null
**Since:** 1.1
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

,

LayoutManager

- add

```java
public void add​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this container with the specified
constraints at the specified index. Also notifies the layout
manager to add the component to the this container's layout using
the specified constraints object.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing layout constraints for this
**Parameters:** index

- the position in the container's list at which to insert
the component;

-1

means insert at the end
component
**Throws:** NullPointerException

- if

comp

is

null
**Throws:** IllegalArgumentException

- if

index

is invalid (see

addImpl(java.awt.Component, java.lang.Object, int)

for details)
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

,

remove(int)

,

LayoutManager

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this container at the specified
index. This method also notifies the layout manager to add
the component to this container's layout using the specified
constraints object via the

addLayoutComponent

method.

The constraints are
defined by the particular layout manager being used. For
example, the

BorderLayout

class defines five
constraints:

BorderLayout.NORTH

,

BorderLayout.SOUTH

,

BorderLayout.EAST

,

BorderLayout.WEST

, and

BorderLayout.CENTER

.

The

GridBagLayout

class requires a

GridBagConstraints

object. Failure to pass
the correct type of constraints object results in an

IllegalArgumentException

.

If the current layout manager implements

LayoutManager2

, then

LayoutManager2.addLayoutComponent(Component,Object)

is invoked on
it. If the current layout manager does not implement

LayoutManager2

, and constraints is a

String

, then

LayoutManager.addLayoutComponent(String,Component)

is invoked on it.

If the component is not an ancestor of this container and has a non-null
parent, it is removed from its current parent before it is added to this
container.

This is the method to override if a program needs to track
every add request to a container as all other add methods defer
to this one. An overriding method should
usually include a call to the superclass's version of the method:

super.addImpl(comp, constraints, index)

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing layout constraints
for this component
**Parameters:** index

- the position in the container's list at which to
insert the component, where

-1

means append to the end
**Throws:** IllegalArgumentException

- if

index

is invalid;
if

comp

is a child of this container, the valid
range is

[-1, getComponentCount()-1]

; if component is
not a child of this container, the valid range is

[-1, getComponentCount()]
**Throws:** IllegalArgumentException

- if

comp

is an ancestor of
this container
**Throws:** IllegalArgumentException

- if adding a window to a container
**Throws:** NullPointerException

- if

comp

is

null
**Since:** 1.1
**See Also:** add(Component)

,

add(Component, int)

,

add(Component, java.lang.Object)

,

invalidate()

,

LayoutManager

,

LayoutManager2

- remove

```java
public void remove​(int index)
```

Removes the component, specified by

index

,
from this container.
This method also notifies the layout manager to remove the
component from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

**Parameters:** index

- the index of the component to be removed
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is not in
range

[0, getComponentCount()-1]
**Since:** 1.1
**See Also:** add(java.awt.Component)

,

invalidate()

,

validate()

,

getComponentCount()

- remove

```java
public void remove​(
Component
comp)
```

Removes the specified component from this container.
This method also notifies the layout manager to remove the
component from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

**Parameters:** comp

- the component to be removed
**Throws:** NullPointerException

- if

comp

is

null
**See Also:** add(java.awt.Component)

,

invalidate()

,

validate()

,

remove(int)

- removeAll

```java
public void removeAll()
```

Removes all the components from this container.
This method also notifies the layout manager to remove the
components from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

**See Also:** add(java.awt.Component)

,

remove(int)

,

invalidate()

- getLayout

```java
public
LayoutManager
getLayout()
```

Gets the layout manager for this container.

**Returns:** the current layout manager for this container
**See Also:** doLayout()

,

setLayout(java.awt.LayoutManager)

- setLayout

```java
public void setLayout​(
LayoutManager
mgr)
```

Sets the layout manager for this container.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** mgr

- the specified layout manager
**See Also:** doLayout()

,

getLayout()

,

invalidate()

- doLayout

```java
public void doLayout()
```

Causes this container to lay out its components. Most programs
should not call this method directly, but should invoke
the

validate

method instead.

**Overrides:** doLayout

in class

Component
**Since:** 1.1
**See Also:** LayoutManager.layoutContainer(java.awt.Container)

,

setLayout(java.awt.LayoutManager)

,

validate()

- layout

```java
@Deprecated

public void layout()
```

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

**Overrides:** layout

in class

Component

- isValidateRoot

```java
public boolean isValidateRoot()
```

Indicates if this container is a

validate root

.

Layout-related changes, such as bounds of the validate root descendants,
do not affect the layout of the validate root parent. This peculiarity
enables the

invalidate()

method to stop invalidating the
component hierarchy when the method encounters a validate root. However,
to preserve backward compatibility this new optimized behavior is
enabled only when the

java.awt.smartInvalidate

system property
value is set to

true

.

If a component hierarchy contains validate roots and the new optimized

invalidate()

behavior is enabled, the

validate()

method
must be invoked on the validate root of a previously invalidated
component to restore the validity of the hierarchy later. Otherwise,
calling the

validate()

method on the top-level container (such
as a

Frame

object) should be used to restore the validity of the
component hierarchy.

The

Window

class and the

Applet

class are the validate
roots in AWT. Swing introduces more validate roots.

**Returns:** whether this container is a validate root
**Since:** 1.7
**See Also:** invalidate()

,

Component.invalidate()

,

JComponent.isValidateRoot()

,

JComponent.revalidate()

- invalidate

```java
public void invalidate()
```

Invalidates the container.

If the

LayoutManager

installed on this container is an instance
of the

LayoutManager2

interface, then
the

LayoutManager2.invalidateLayout(Container)

method is invoked
on it supplying this

Container

as the argument.

Afterwards this method marks this container invalid, and invalidates its
ancestors. See the

Component.invalidate()

method for more details.

**Overrides:** invalidate

in class

Component
**See Also:** validate()

,

layout()

,

LayoutManager2

- validate

```java
public void validate()
```

Validates this container and all of its subcomponents.

Validating a container means laying out its subcomponents.
Layout-related changes, such as setting the bounds of a component, or
adding a component to the container, invalidate the container
automatically. Note that the ancestors of the container may be
invalidated also (see

Component.invalidate()

for details.)
Therefore, to restore the validity of the hierarchy, the

validate()

method should be invoked on the top-most invalid
container of the hierarchy.

Validating the container may be a quite time-consuming operation. For
performance reasons a developer may postpone the validation of the
hierarchy till a set of layout-related operations completes, e.g. after
adding all the children to the container.

If this

Container

is not valid, this method invokes
the

validateTree

method and marks this

Container

as valid. Otherwise, no action is performed.

**Overrides:** validate

in class

Component
**See Also:** add(java.awt.Component)

,

invalidate()

,

isValidateRoot()

,

JComponent.revalidate()

,

validateTree()

- validateTree

```java
protected void validateTree()
```

Recursively descends the container tree and recomputes the
layout for any subtrees marked as needing it (those marked as
invalid). Synchronization should be provided by the method
that calls this one:

validate

.

**See Also:** doLayout()

,

validate()

- setFont

```java
public void setFont​(
Font
f)
```

Sets the font of this container.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Overrides:** setFont

in class

Component
**Parameters:** f

- The font to become this container's font.
**Since:** 1.0
**See Also:** Component.getFont()

,

invalidate()

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns the preferred size of this container. If the preferred size has
not been set explicitly by

Component.setPreferredSize(Dimension)

and this

Container

has a

non-null

LayoutManager

,
then

LayoutManager.preferredLayoutSize(Container)

is used to calculate the preferred size.

Note: some implementations may cache the value returned from the

LayoutManager

. Implementations that cache need not invoke

preferredLayoutSize

on the

LayoutManager

every time
this method is invoked, rather the

LayoutManager

will only
be queried after the

Container

becomes invalid.

**Overrides:** getPreferredSize

in class

Component
**Returns:** an instance of

Dimension

that represents
the preferred size of this container.
**See Also:** getMinimumSize()

,

getMaximumSize()

,

getLayout()

,

LayoutManager.preferredLayoutSize(Container)

,

Component.getPreferredSize()

- preferredSize

```java
@Deprecated

public
Dimension
preferredSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Description copied from class:

Component

Returns the component's preferred size.

**Overrides:** preferredSize

in class

Component
**Returns:** the component's preferred size

- getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Returns the minimum size of this container. If the minimum size has
not been set explicitly by

Component.setMinimumSize(Dimension)

and this

Container

has a

non-null

LayoutManager

,
then

LayoutManager.minimumLayoutSize(Container)

is used to calculate the minimum size.

Note: some implementations may cache the value returned from the

LayoutManager

. Implementations that cache need not invoke

minimumLayoutSize

on the

LayoutManager

every time
this method is invoked, rather the

LayoutManager

will only
be queried after the

Container

becomes invalid.

**Overrides:** getMinimumSize

in class

Component
**Returns:** an instance of

Dimension

that represents
the minimum size of this container.
**Since:** 1.1
**See Also:** getPreferredSize()

,

getMaximumSize()

,

getLayout()

,

LayoutManager.minimumLayoutSize(Container)

,

Component.getMinimumSize()

- minimumSize

```java
@Deprecated

public
Dimension
minimumSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Description copied from class:

Component

Returns the minimum size of this component.

**Overrides:** minimumSize

in class

Component
**Returns:** the minimum size of this component

- getMaximumSize

```java
public
Dimension
getMaximumSize()
```

Returns the maximum size of this container. If the maximum size has
not been set explicitly by

Component.setMaximumSize(Dimension)

and the

LayoutManager

installed on this

Container

is an instance of

LayoutManager2

, then

LayoutManager2.maximumLayoutSize(Container)

is used to calculate the maximum size.

Note: some implementations may cache the value returned from the

LayoutManager2

. Implementations that cache need not invoke

maximumLayoutSize

on the

LayoutManager2

every time
this method is invoked, rather the

LayoutManager2

will only
be queried after the

Container

becomes invalid.

**Overrides:** getMaximumSize

in class

Component
**Returns:** an instance of

Dimension

that represents
the maximum size of this container.
**See Also:** getPreferredSize()

,

getMinimumSize()

,

getLayout()

,

LayoutManager2.maximumLayoutSize(Container)

,

Component.getMaximumSize()

- getAlignmentX

```java
public float getAlignmentX()
```

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Overrides:** getAlignmentX

in class

Component
**Returns:** the horizontal alignment of this component

- getAlignmentY

```java
public float getAlignmentY()
```

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Overrides:** getAlignmentY

in class

Component
**Returns:** the vertical alignment of this component

- paint

```java
public void paint​(
Graphics
g)
```

Paints the container. This forwards the paint to any lightweight
components that are children of this container. If this method is
reimplemented, super.paint(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, paint() will not be
forwarded to that child.

**Overrides:** paint

in class

Component
**Parameters:** g

- the specified Graphics window
**See Also:** Component.update(Graphics)

- update

```java
public void update​(
Graphics
g)
```

Updates the container. This forwards the update to any lightweight
components that are children of this container. If this method is
reimplemented, super.update(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, update() will not be
forwarded to that child.

**Overrides:** update

in class

Component
**Parameters:** g

- the specified Graphics window
**See Also:** Component.update(Graphics)

- print

```java
public void print​(
Graphics
g)
```

Prints the container. This forwards the print to any lightweight
components that are children of this container. If this method is
reimplemented, super.print(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, print() will not be
forwarded to that child.

**Overrides:** print

in class

Component
**Parameters:** g

- the specified Graphics window
**See Also:** Component.update(Graphics)

- paintComponents

```java
public void paintComponents​(
Graphics
g)
```

Paints each of the components in this container.

**Parameters:** g

- the graphics context.
**See Also:** Component.paint(java.awt.Graphics)

,

Component.paintAll(java.awt.Graphics)

- printComponents

```java
public void printComponents​(
Graphics
g)
```

Prints each of the components in this container.

**Parameters:** g

- the graphics context.
**See Also:** Component.print(java.awt.Graphics)

,

Component.printAll(java.awt.Graphics)

- addContainerListener

```java
public void addContainerListener​(
ContainerListener
l)
```

Adds the specified container listener to receive container events
from this container.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the container listener
**See Also:** removeContainerListener(java.awt.event.ContainerListener)

,

getContainerListeners()

- removeContainerListener

```java
public void removeContainerListener​(
ContainerListener
l)
```

Removes the specified container listener so it no longer receives
container events from this container.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the container listener
**See Also:** addContainerListener(java.awt.event.ContainerListener)

,

getContainerListeners()

- getContainerListeners

```java
public
ContainerListener
[] getContainerListeners()
```

Returns an array of all the container listeners
registered on this container.

**Returns:** all of this container's

ContainerListener

s
or an empty array if no container
listeners are currently registered
**Since:** 1.4
**See Also:** addContainerListener(java.awt.event.ContainerListener)

,

removeContainerListener(java.awt.event.ContainerListener)

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Container

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Container c

for its container listeners with the following code:

```java
ContainerListener[] cls = (ContainerListener[])(c.getListeners(ContainerListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Component
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this container,
or an empty array if no such listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Throws:** NullPointerException

- if

listenerType

is

null
**Since:** 1.3
**See Also:** getContainerListeners()

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this container. If the event is a

ContainerEvent

, it invokes the

processContainerEvent

method, else it invokes
its superclass's

processEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Component
**Parameters:** e

- the event
**See Also:** Component.processComponentEvent(java.awt.event.ComponentEvent)

,

Component.processFocusEvent(java.awt.event.FocusEvent)

,

Component.processKeyEvent(java.awt.event.KeyEvent)

,

Component.processMouseEvent(java.awt.event.MouseEvent)

,

Component.processMouseMotionEvent(java.awt.event.MouseEvent)

,

Component.processInputMethodEvent(java.awt.event.InputMethodEvent)

,

Component.processHierarchyEvent(java.awt.event.HierarchyEvent)

,

Component.processMouseWheelEvent(java.awt.event.MouseWheelEvent)

- processContainerEvent

```java
protected void processContainerEvent​(
ContainerEvent
e)
```

Processes container events occurring on this container by
dispatching them to any registered ContainerListener objects.
NOTE: This method will not be called unless container events
are enabled for this component; this happens when one of the
following occurs:

- A ContainerListener object is registered via

addContainerListener

Container events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the container event
**See Also:** Component.enableEvents(long)

- deliverEvent

```java
@Deprecated

public void deliverEvent​(
Event
e)
```

Deprecated.

As of JDK version 1.1,
replaced by

dispatchEvent(AWTEvent e)

**Overrides:** deliverEvent

in class

Component
**Parameters:** e

- the event to deliver

- getComponentAt

```java
public
Component
getComponentAt​(int x,
int y)
```

Locates the component that contains the x,y position. The
top-most child component is returned in the case where there
is overlap in the components. This is determined by finding
the component closest to the index 0 that claims to contain
the given point via Component.contains(), except that Components
which have native peers take precedence over those which do not
(i.e., lightweight Components).

**Overrides:** getComponentAt

in class

Component
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Returns:** null if the component does not contain the position.
If there is no child component at the requested point and the
point is within the bounds of the container the container itself
is returned; otherwise the top-most child is returned.
**Since:** 1.1
**See Also:** Component.contains(int, int)

- locate

```java
@Deprecated

public
Component
locate​(int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by

getComponentAt(int, int)

.

Description copied from class:

Component

Returns the component occupying the position specified (this component,
or immediate child component, or null if neither
of the first two occupies the location).

**Overrides:** locate

in class

Component
**Parameters:** x

- the

x

coordinate to search for components at
**Parameters:** y

- the

y

coordinate to search for components at
**Returns:** the component at the specified location or

null

- getComponentAt

```java
public
Component
getComponentAt​(
Point
p)
```

Gets the component that contains the specified point.

**Overrides:** getComponentAt

in class

Component
**Parameters:** p

- the point.
**Returns:** returns the component that contains the point,
or

null

if the component does
not contain the point.
**Since:** 1.1
**See Also:** Component.contains(int, int)

- getMousePosition

```java
public
Point
getMousePosition​(boolean allowChildren)
throws
HeadlessException
```

Returns the position of the mouse pointer in this

Container

's
coordinate space if the

Container

is under the mouse pointer,
otherwise returns

null

.
This method is similar to

Component.getMousePosition()

with the exception
that it can take the

Container

's children into account.
If

allowChildren

is

false

, this method will return
a non-null value only if the mouse pointer is above the

Container

directly, not above the part obscured by children.
If

allowChildren

is

true

, this method returns
a non-null value if the mouse pointer is above

Container

or any
of its descendants.

**Parameters:** allowChildren

- true if children should be taken into account
**Returns:** mouse coordinates relative to this

Component

, or null
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless() returns true
**Since:** 1.5
**See Also:** Component.getMousePosition()

- findComponentAt

```java
public
Component
findComponentAt​(int x,
int y)
```

Locates the visible child component that contains the specified
position. The top-most child component is returned in the case
where there is overlap in the components. If the containing child
component is a Container, this method will continue searching for
the deepest nested child component. Components which are not
visible are ignored during the search.

The findComponentAt method is different from getComponentAt in
that getComponentAt only searches the Container's immediate
children; if the containing component is a Container,
findComponentAt will search that child to find a nested component.

**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Returns:** null if the component does not contain the position.
If there is no child component at the requested point and the
point is within the bounds of the container the container itself
is returned.
**Since:** 1.2
**See Also:** Component.contains(int, int)

,

getComponentAt(int, int)

- findComponentAt

```java
public
Component
findComponentAt​(
Point
p)
```

Locates the visible child component that contains the specified
point. The top-most child component is returned in the case
where there is overlap in the components. If the containing child
component is a Container, this method will continue searching for
the deepest nested child component. Components which are not
visible are ignored during the search.

The findComponentAt method is different from getComponentAt in
that getComponentAt only searches the Container's immediate
children; if the containing component is a Container,
findComponentAt will search that child to find a nested component.

**Parameters:** p

- the point.
**Returns:** null if the component does not contain the position.
If there is no child component at the requested point and the
point is within the bounds of the container the container itself
is returned.
**Throws:** NullPointerException

- if

p

is

null
**Since:** 1.2
**See Also:** Component.contains(int, int)

,

getComponentAt(int, int)

- addNotify

```java
public void addNotify()
```

Makes this Container displayable by connecting it to
a native screen resource. Making a container displayable will
cause all of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:** addNotify

in class

Component
**See Also:** Component.isDisplayable()

,

removeNotify()

- removeNotify

```java
public void removeNotify()
```

Makes this Container undisplayable by removing its connection
to its native screen resource. Making a container undisplayable
will cause all of its children to be made undisplayable.
This method is called by the toolkit internally and should
not be called directly by programs.

**Overrides:** removeNotify

in class

Component
**See Also:** Component.isDisplayable()

,

addNotify()

- isAncestorOf

```java
public boolean isAncestorOf​(
Component
c)
```

Checks if the component is contained in the component hierarchy of
this container.

**Parameters:** c

- the component
**Returns:** true

if it is an ancestor;

false

otherwise.
**Since:** 1.1

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

Container

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Component
**Returns:** the parameter string of this container

- list

```java
public void list​(
PrintStream
out,
int indent)
```

Prints a listing of this container to the specified output
stream. The listing starts at the specified indentation.

The immediate children of the container are printed with
an indentation of

indent+1

. The children
of those children are printed at

indent+2

and so on.

**Overrides:** list

in class

Component
**Parameters:** out

- a print stream
**Parameters:** indent

- the number of spaces to indent
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.0
**See Also:** Component.list(java.io.PrintStream, int)

- list

```java
public void list​(
PrintWriter
out,
int indent)
```

Prints out a list, starting at the specified indentation,
to the specified print writer.

The immediate children of the container are printed with
an indentation of

indent+1

. The children
of those children are printed at

indent+2

and so on.

**Overrides:** list

in class

Component
**Parameters:** out

- a print writer
**Parameters:** indent

- the number of spaces to indent
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.1
**See Also:** Component.list(java.io.PrintWriter, int)

- setFocusTraversalKeys

```java
public void setFocusTraversalKeys​(int id,

Set
<? extends
AWTKeyStroke
> keystrokes)
```

Sets the focus traversal keys for a given traversal operation for this
Container.

The default values for a Container's focus traversal keys are
implementation-dependent. Sun recommends that all implementations for a
particular native platform use the same default values. The
recommendations for Windows and Unix are listed below. These
recommendations are used in the Sun AWT implementations.

Recommended default values for a Container's focus traversal
keys

Identifier

Meaning

Default

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

Normal forward keyboard traversal

TAB on KEY_PRESSED, CTRL-TAB on KEY_PRESSED

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

Normal reverse keyboard traversal

SHIFT-TAB on KEY_PRESSED, CTRL-SHIFT-TAB on KEY_PRESSED

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

Go up one focus traversal cycle

none

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

Go down one focus traversal cycle

none

To disable a traversal key, use an empty Set; Collections.EMPTY_SET is
recommended.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Container. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Container inherits the
Set from its parent. If all ancestors of this Container have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

**Overrides:** setFocusTraversalKeys

in class

Component
**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Parameters:** keystrokes

- the Set of AWTKeyStroke for the specified operation
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS, or if keystrokes
contains null, or if any keystroke represents a KEY_TYPED event,
or if any keystroke already maps to another focus traversal
operation for this Container
**Since:** 1.4
**See Also:** getFocusTraversalKeys(int)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

,

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

- getFocusTraversalKeys

```java
public
Set
<
AWTKeyStroke
> getFocusTraversalKeys​(int id)
```

Returns the Set of focus traversal keys for a given traversal operation
for this Container. (See

setFocusTraversalKeys

for a full description of each key.)

If a Set of traversal keys has not been explicitly defined for this
Container, then this Container's parent's Set is returned. If no Set
has been explicitly defined for any of this Container's ancestors, then
the current KeyboardFocusManager's default Set is returned.

**Overrides:** getFocusTraversalKeys

in class

Component
**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Returns:** the Set of AWTKeyStrokes for the specified operation. The Set
will be unmodifiable, and may be empty. null will never be
returned.
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4
**See Also:** setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

,

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

- areFocusTraversalKeysSet

```java
public boolean areFocusTraversalKeysSet​(int id)
```

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Container. If
this method returns

false

, this Container is inheriting the
Set from an ancestor, or from the current KeyboardFocusManager.

**Overrides:** areFocusTraversalKeysSet

in class

Component
**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Returns:** true

if the Set of focus traversal keys for the
given focus traversal operation has been explicitly defined for
this Component;

false

otherwise.
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4

- isFocusCycleRoot

```java
public boolean isFocusCycleRoot​(
Container
container)
```

Returns whether the specified Container is the focus cycle root of this
Container's focus traversal cycle. Each focus traversal cycle has only
a single focus cycle root and each Container which is not a focus cycle
root belongs to only a single focus traversal cycle. Containers which
are focus cycle roots belong to two cycles: one rooted at the Container
itself, and one rooted at the Container's nearest focus-cycle-root
ancestor. This method will return

true

for both such
Containers in this case.

**Overrides:** isFocusCycleRoot

in class

Component
**Parameters:** container

- the Container to be tested
**Returns:** true

if the specified Container is a focus-cycle-
root of this Container;

false

otherwise
**Since:** 1.4
**See Also:** isFocusCycleRoot()

- setFocusTraversalPolicy

```java
public void setFocusTraversalPolicy​(
FocusTraversalPolicy
policy)
```

Sets the focus traversal policy that will manage keyboard traversal of
this Container's children, if this Container is a focus cycle root. If
the argument is null, this Container inherits its policy from its focus-
cycle-root ancestor. If the argument is non-null, this policy will be
inherited by all focus-cycle-root children that have no keyboard-
traversal policy of their own (as will, recursively, their focus-cycle-
root children).

If this Container is not a focus cycle root, the policy will be
remembered, but will not be used or inherited by this or any other
Containers until this Container is made a focus cycle root.

**Parameters:** policy

- the new focus traversal policy for this Container
**Since:** 1.4
**See Also:** getFocusTraversalPolicy()

,

setFocusCycleRoot(boolean)

,

isFocusCycleRoot(java.awt.Container)

- getFocusTraversalPolicy

```java
public
FocusTraversalPolicy
getFocusTraversalPolicy()
```

Returns the focus traversal policy that will manage keyboard traversal
of this Container's children, or null if this Container is not a focus
cycle root. If no traversal policy has been explicitly set for this
Container, then this Container's focus-cycle-root ancestor's policy is
returned.

**Returns:** this Container's focus traversal policy, or null if this
Container is not a focus cycle root.
**Since:** 1.4
**See Also:** setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

setFocusCycleRoot(boolean)

,

isFocusCycleRoot(java.awt.Container)

- isFocusTraversalPolicySet

```java
public boolean isFocusTraversalPolicySet()
```

Returns whether the focus traversal policy has been explicitly set for
this Container. If this method returns

false

, this
Container will inherit its focus traversal policy from an ancestor.

**Returns:** true

if the focus traversal policy has been
explicitly set for this Container;

false

otherwise.
**Since:** 1.4

- setFocusCycleRoot

```java
public void setFocusCycleRoot​(boolean focusCycleRoot)
```

Sets whether this Container is the root of a focus traversal cycle. Once
focus enters a traversal cycle, typically it cannot leave it via focus
traversal unless one of the up- or down-cycle keys is pressed. Normal
traversal is limited to this Container, and all of this Container's
descendants that are not descendants of inferior focus cycle roots. Note
that a FocusTraversalPolicy may bend these restrictions, however. For
example, ContainerOrderFocusTraversalPolicy supports implicit down-cycle
traversal.

The alternative way to specify the traversal order of this Container's
children is to make this Container a

focus traversal policy provider

.

**Parameters:** focusCycleRoot

- indicates whether this Container is the root of a
focus traversal cycle
**Since:** 1.4
**See Also:** isFocusCycleRoot()

,

setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

ContainerOrderFocusTraversalPolicy

,

setFocusTraversalPolicyProvider(boolean)

- isFocusCycleRoot

```java
public boolean isFocusCycleRoot()
```

Returns whether this Container is the root of a focus traversal cycle.
Once focus enters a traversal cycle, typically it cannot leave it via
focus traversal unless one of the up- or down-cycle keys is pressed.
Normal traversal is limited to this Container, and all of this
Container's descendants that are not descendants of inferior focus
cycle roots. Note that a FocusTraversalPolicy may bend these
restrictions, however. For example, ContainerOrderFocusTraversalPolicy
supports implicit down-cycle traversal.

**Returns:** whether this Container is the root of a focus traversal cycle
**Since:** 1.4
**See Also:** setFocusCycleRoot(boolean)

,

setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

ContainerOrderFocusTraversalPolicy

- setFocusTraversalPolicyProvider

```java
public final void setFocusTraversalPolicyProvider​(boolean provider)
```

Sets whether this container will be used to provide focus
traversal policy. Container with this property as

true

will be used to acquire focus traversal policy
instead of closest focus cycle root ancestor.

**Parameters:** provider

- indicates whether this container will be used to
provide focus traversal policy
**Since:** 1.5
**See Also:** setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

isFocusTraversalPolicyProvider()

- isFocusTraversalPolicyProvider

```java
public final boolean isFocusTraversalPolicyProvider()
```

Returns whether this container provides focus traversal
policy. If this property is set to

true

then when
keyboard focus manager searches container hierarchy for focus
traversal policy and encounters this container before any other
container with this property as true or focus cycle roots then
its focus traversal policy will be used instead of focus cycle
root's policy.

**Returns:** true

if this container provides focus traversal
policy,

false

otherwise
**Since:** 1.5
**See Also:** setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

setFocusCycleRoot(boolean)

,

setFocusTraversalPolicyProvider(boolean)

- transferFocusDownCycle

```java
public void transferFocusDownCycle()
```

Transfers the focus down one focus traversal cycle. If this Container is
a focus cycle root, then the focus owner is set to this Container's
default Component to focus, and the current focus cycle root is set to
this Container. If this Container is not a focus cycle root, then no
focus traversal operation occurs.

**Since:** 1.4
**See Also:** Component.requestFocus()

,

isFocusCycleRoot(java.awt.Container)

,

setFocusCycleRoot(boolean)

- applyComponentOrientation

```java
public void applyComponentOrientation​(
ComponentOrientation
o)
```

Sets the

ComponentOrientation

property of this container
and all components contained within it.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Overrides:** applyComponentOrientation

in class

Component
**Parameters:** o

- the new component orientation of this container and
the components contained within it.
**Throws:** NullPointerException

- if

orientation

is null.
**Since:** 1.4
**See Also:** Component.setComponentOrientation(java.awt.ComponentOrientation)

,

Component.getComponentOrientation()

,

invalidate()

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Container's font ("font")
- this Container's background color ("background")
- this Container's foreground color ("foreground")
- this Container's focusability ("focusable")
- this Container's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Container's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Container's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Container's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Container's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Container's focus traversal policy ("focusTraversalPolicy")
- this Container's focus-cycle-root state ("focusCycleRoot")

Note that if this Container is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:** addPropertyChangeListener

in class

Component
**Parameters:** listener

- the PropertyChangeListener to be added
**See Also:** Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

,

addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following defaults:

- this Container's font ("font")
- this Container's background color ("background")
- this Container's foreground color ("foreground")
- this Container's focusability ("focusable")
- this Container's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Container's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Container's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Container's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Container's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Container's focus traversal policy ("focusTraversalPolicy")
- this Container's focus-cycle-root state ("focusCycleRoot")
- this Container's focus-traversal-policy-provider state("focusTraversalPolicyProvider")
- this Container's focus-traversal-policy-provider state("focusTraversalPolicyProvider")

Note that if this Container is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:** addPropertyChangeListener

in class

Component
**Parameters:** propertyName

- one of the property names listed above
**Parameters:** listener

- the PropertyChangeListener to be added
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

Constructor Detail

- Container

```java
public Container()
```

Constructs a new Container. Containers can be extended directly,
but are lightweight in this case and must be contained by a parent
somewhere higher up in the component tree that is native.
(such as Frame for example).

---

#### Constructor Detail

Container

```java
public Container()
```

Constructs a new Container. Containers can be extended directly,
but are lightweight in this case and must be contained by a parent
somewhere higher up in the component tree that is native.
(such as Frame for example).

---

#### Container

public Container()

Constructs a new Container. Containers can be extended directly,
but are lightweight in this case and must be contained by a parent
somewhere higher up in the component tree that is native.
(such as Frame for example).

Method Detail

- getComponentCount

```java
public int getComponentCount()
```

Gets the number of components in this panel.

Note: This method should be called under AWT tree lock.

**Returns:** the number of components in this panel.
**Since:** 1.1
**See Also:** getComponent(int)

,

Component.getTreeLock()

- countComponents

```java
@Deprecated

public int countComponents()
```

Deprecated.

As of JDK version 1.1,
replaced by getComponentCount().

Returns the number of components in this container.

**Returns:** the number of components in this container

- getComponent

```java
public
Component
getComponent​(int n)
```

Gets the nth component in this container.

Note: This method should be called under AWT tree lock.

**Parameters:** n

- the index of the component to get.
**Returns:** the n

th

component in this container.
**Throws:** ArrayIndexOutOfBoundsException

- if the n

th

value does not exist.
**See Also:** Component.getTreeLock()

- getComponents

```java
public
Component
[] getComponents()
```

Gets all the components in this container.

Note: This method should be called under AWT tree lock.

**Returns:** an array of all the components in this container.
**See Also:** Component.getTreeLock()

- getInsets

```java
public
Insets
getInsets()
```

Determines the insets of this container, which indicate the size
of the container's border.

A

Frame

object, for example, has a top inset that
corresponds to the height of the frame's title bar.

**Returns:** the insets of this container.
**Since:** 1.1
**See Also:** Insets

,

LayoutManager

- insets

```java
@Deprecated

public
Insets
insets()
```

Deprecated.

As of JDK version 1.1,
replaced by

getInsets()

.

Returns the insets for this container.

**Returns:** the insets for this container

- add

```java
public
Component
add​(
Component
comp)
```

Appends the specified component to the end of this container.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Returns:** the component argument
**Throws:** NullPointerException

- if

comp

is

null
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

- add

```java
public
Component
add​(
String
name,

Component
comp)
```

Adds the specified component to this container.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method is obsolete as of 1.1. Please use the
method

add(Component, Object)

instead.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** name

- the name of the component to be added
**Parameters:** comp

- the component to be added
**Returns:** the component added
**Throws:** NullPointerException

- if

comp

is

null
**See Also:** add(Component, Object)

,

invalidate()

- add

```java
public
Component
add​(
Component
comp,
int index)
```

Adds the specified component to this container at the given
position.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Parameters:** index

- the position at which to insert the component,
or

-1

to append the component to the end
**Returns:** the component

comp
**Throws:** NullPointerException

- if

comp

is

null
**Throws:** IllegalArgumentException

- if

index

is invalid (see

addImpl(java.awt.Component, java.lang.Object, int)

for details)
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

remove(int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

- setComponentZOrder

```java
public void setComponentZOrder​(
Component
comp,
int index)
```

Moves the specified component to the specified z-order index in
the container. The z-order determines the order that components
are painted; the component with the highest z-order paints first
and the component with the lowest z-order paints last.
Where components overlap, the component with the lower
z-order paints over the component with the higher z-order.

If the component is a child of some other container, it is
removed from that container before being added to this container.
The important difference between this method and

java.awt.Container.add(Component, int)

is that this method
doesn't call

removeNotify

on the component while
removing it from its previous container unless necessary and when
allowed by the underlying native windowing system. This way, if the
component has the keyboard focus, it maintains the focus when
moved to the new position.

This property is guaranteed to apply only to lightweight
non-

Container

components.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

Note

: Not all platforms support changing the z-order of
heavyweight components from one container into another without
the call to

removeNotify

. There is no way to detect
whether a platform supports this, so developers shouldn't make
any assumptions.

**Parameters:** comp

- the component to be moved
**Parameters:** index

- the position in the container's list to
insert the component, where

getComponentCount()

appends to the end
**Throws:** NullPointerException

- if

comp

is

null
**Throws:** IllegalArgumentException

- if

comp

is one of the
container's parents
**Throws:** IllegalArgumentException

- if

index

is not in
the range

[0, getComponentCount()]

for moving
between containers, or not in the range

[0, getComponentCount()-1]

for moving inside
a container
**Throws:** IllegalArgumentException

- if adding a container to itself
**Throws:** IllegalArgumentException

- if adding a

Window

to a container
**Since:** 1.5
**See Also:** getComponentZOrder(java.awt.Component)

,

invalidate()

- getComponentZOrder

```java
public int getComponentZOrder​(
Component
comp)
```

Returns the z-order index of the component inside the container.
The higher a component is in the z-order hierarchy, the lower
its index. The component with the lowest z-order index is
painted last, above all other child components.

**Parameters:** comp

- the component being queried
**Returns:** the z-order index of the component; otherwise
returns -1 if the component is

null

or doesn't belong to the container
**Since:** 1.5
**See Also:** setComponentZOrder(java.awt.Component, int)

- add

```java
public void add​(
Component
comp,

Object
constraints)
```

Adds the specified component to the end of this container.
Also notifies the layout manager to add the component to
this container's layout using the specified constraints object.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing
layout constraints for this component
**Throws:** NullPointerException

- if

comp

is

null
**Since:** 1.1
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

,

LayoutManager

- add

```java
public void add​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this container with the specified
constraints at the specified index. Also notifies the layout
manager to add the component to the this container's layout using
the specified constraints object.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing layout constraints for this
**Parameters:** index

- the position in the container's list at which to insert
the component;

-1

means insert at the end
component
**Throws:** NullPointerException

- if

comp

is

null
**Throws:** IllegalArgumentException

- if

index

is invalid (see

addImpl(java.awt.Component, java.lang.Object, int)

for details)
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

,

remove(int)

,

LayoutManager

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this container at the specified
index. This method also notifies the layout manager to add
the component to this container's layout using the specified
constraints object via the

addLayoutComponent

method.

The constraints are
defined by the particular layout manager being used. For
example, the

BorderLayout

class defines five
constraints:

BorderLayout.NORTH

,

BorderLayout.SOUTH

,

BorderLayout.EAST

,

BorderLayout.WEST

, and

BorderLayout.CENTER

.

The

GridBagLayout

class requires a

GridBagConstraints

object. Failure to pass
the correct type of constraints object results in an

IllegalArgumentException

.

If the current layout manager implements

LayoutManager2

, then

LayoutManager2.addLayoutComponent(Component,Object)

is invoked on
it. If the current layout manager does not implement

LayoutManager2

, and constraints is a

String

, then

LayoutManager.addLayoutComponent(String,Component)

is invoked on it.

If the component is not an ancestor of this container and has a non-null
parent, it is removed from its current parent before it is added to this
container.

This is the method to override if a program needs to track
every add request to a container as all other add methods defer
to this one. An overriding method should
usually include a call to the superclass's version of the method:

super.addImpl(comp, constraints, index)

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing layout constraints
for this component
**Parameters:** index

- the position in the container's list at which to
insert the component, where

-1

means append to the end
**Throws:** IllegalArgumentException

- if

index

is invalid;
if

comp

is a child of this container, the valid
range is

[-1, getComponentCount()-1]

; if component is
not a child of this container, the valid range is

[-1, getComponentCount()]
**Throws:** IllegalArgumentException

- if

comp

is an ancestor of
this container
**Throws:** IllegalArgumentException

- if adding a window to a container
**Throws:** NullPointerException

- if

comp

is

null
**Since:** 1.1
**See Also:** add(Component)

,

add(Component, int)

,

add(Component, java.lang.Object)

,

invalidate()

,

LayoutManager

,

LayoutManager2

- remove

```java
public void remove​(int index)
```

Removes the component, specified by

index

,
from this container.
This method also notifies the layout manager to remove the
component from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

**Parameters:** index

- the index of the component to be removed
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is not in
range

[0, getComponentCount()-1]
**Since:** 1.1
**See Also:** add(java.awt.Component)

,

invalidate()

,

validate()

,

getComponentCount()

- remove

```java
public void remove​(
Component
comp)
```

Removes the specified component from this container.
This method also notifies the layout manager to remove the
component from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

**Parameters:** comp

- the component to be removed
**Throws:** NullPointerException

- if

comp

is

null
**See Also:** add(java.awt.Component)

,

invalidate()

,

validate()

,

remove(int)

- removeAll

```java
public void removeAll()
```

Removes all the components from this container.
This method also notifies the layout manager to remove the
components from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

**See Also:** add(java.awt.Component)

,

remove(int)

,

invalidate()

- getLayout

```java
public
LayoutManager
getLayout()
```

Gets the layout manager for this container.

**Returns:** the current layout manager for this container
**See Also:** doLayout()

,

setLayout(java.awt.LayoutManager)

- setLayout

```java
public void setLayout​(
LayoutManager
mgr)
```

Sets the layout manager for this container.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** mgr

- the specified layout manager
**See Also:** doLayout()

,

getLayout()

,

invalidate()

- doLayout

```java
public void doLayout()
```

Causes this container to lay out its components. Most programs
should not call this method directly, but should invoke
the

validate

method instead.

**Overrides:** doLayout

in class

Component
**Since:** 1.1
**See Also:** LayoutManager.layoutContainer(java.awt.Container)

,

setLayout(java.awt.LayoutManager)

,

validate()

- layout

```java
@Deprecated

public void layout()
```

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

**Overrides:** layout

in class

Component

- isValidateRoot

```java
public boolean isValidateRoot()
```

Indicates if this container is a

validate root

.

Layout-related changes, such as bounds of the validate root descendants,
do not affect the layout of the validate root parent. This peculiarity
enables the

invalidate()

method to stop invalidating the
component hierarchy when the method encounters a validate root. However,
to preserve backward compatibility this new optimized behavior is
enabled only when the

java.awt.smartInvalidate

system property
value is set to

true

.

If a component hierarchy contains validate roots and the new optimized

invalidate()

behavior is enabled, the

validate()

method
must be invoked on the validate root of a previously invalidated
component to restore the validity of the hierarchy later. Otherwise,
calling the

validate()

method on the top-level container (such
as a

Frame

object) should be used to restore the validity of the
component hierarchy.

The

Window

class and the

Applet

class are the validate
roots in AWT. Swing introduces more validate roots.

**Returns:** whether this container is a validate root
**Since:** 1.7
**See Also:** invalidate()

,

Component.invalidate()

,

JComponent.isValidateRoot()

,

JComponent.revalidate()

- invalidate

```java
public void invalidate()
```

Invalidates the container.

If the

LayoutManager

installed on this container is an instance
of the

LayoutManager2

interface, then
the

LayoutManager2.invalidateLayout(Container)

method is invoked
on it supplying this

Container

as the argument.

Afterwards this method marks this container invalid, and invalidates its
ancestors. See the

Component.invalidate()

method for more details.

**Overrides:** invalidate

in class

Component
**See Also:** validate()

,

layout()

,

LayoutManager2

- validate

```java
public void validate()
```

Validates this container and all of its subcomponents.

Validating a container means laying out its subcomponents.
Layout-related changes, such as setting the bounds of a component, or
adding a component to the container, invalidate the container
automatically. Note that the ancestors of the container may be
invalidated also (see

Component.invalidate()

for details.)
Therefore, to restore the validity of the hierarchy, the

validate()

method should be invoked on the top-most invalid
container of the hierarchy.

Validating the container may be a quite time-consuming operation. For
performance reasons a developer may postpone the validation of the
hierarchy till a set of layout-related operations completes, e.g. after
adding all the children to the container.

If this

Container

is not valid, this method invokes
the

validateTree

method and marks this

Container

as valid. Otherwise, no action is performed.

**Overrides:** validate

in class

Component
**See Also:** add(java.awt.Component)

,

invalidate()

,

isValidateRoot()

,

JComponent.revalidate()

,

validateTree()

- validateTree

```java
protected void validateTree()
```

Recursively descends the container tree and recomputes the
layout for any subtrees marked as needing it (those marked as
invalid). Synchronization should be provided by the method
that calls this one:

validate

.

**See Also:** doLayout()

,

validate()

- setFont

```java
public void setFont​(
Font
f)
```

Sets the font of this container.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Overrides:** setFont

in class

Component
**Parameters:** f

- The font to become this container's font.
**Since:** 1.0
**See Also:** Component.getFont()

,

invalidate()

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns the preferred size of this container. If the preferred size has
not been set explicitly by

Component.setPreferredSize(Dimension)

and this

Container

has a

non-null

LayoutManager

,
then

LayoutManager.preferredLayoutSize(Container)

is used to calculate the preferred size.

Note: some implementations may cache the value returned from the

LayoutManager

. Implementations that cache need not invoke

preferredLayoutSize

on the

LayoutManager

every time
this method is invoked, rather the

LayoutManager

will only
be queried after the

Container

becomes invalid.

**Overrides:** getPreferredSize

in class

Component
**Returns:** an instance of

Dimension

that represents
the preferred size of this container.
**See Also:** getMinimumSize()

,

getMaximumSize()

,

getLayout()

,

LayoutManager.preferredLayoutSize(Container)

,

Component.getPreferredSize()

- preferredSize

```java
@Deprecated

public
Dimension
preferredSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Description copied from class:

Component

Returns the component's preferred size.

**Overrides:** preferredSize

in class

Component
**Returns:** the component's preferred size

- getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Returns the minimum size of this container. If the minimum size has
not been set explicitly by

Component.setMinimumSize(Dimension)

and this

Container

has a

non-null

LayoutManager

,
then

LayoutManager.minimumLayoutSize(Container)

is used to calculate the minimum size.

Note: some implementations may cache the value returned from the

LayoutManager

. Implementations that cache need not invoke

minimumLayoutSize

on the

LayoutManager

every time
this method is invoked, rather the

LayoutManager

will only
be queried after the

Container

becomes invalid.

**Overrides:** getMinimumSize

in class

Component
**Returns:** an instance of

Dimension

that represents
the minimum size of this container.
**Since:** 1.1
**See Also:** getPreferredSize()

,

getMaximumSize()

,

getLayout()

,

LayoutManager.minimumLayoutSize(Container)

,

Component.getMinimumSize()

- minimumSize

```java
@Deprecated

public
Dimension
minimumSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Description copied from class:

Component

Returns the minimum size of this component.

**Overrides:** minimumSize

in class

Component
**Returns:** the minimum size of this component

- getMaximumSize

```java
public
Dimension
getMaximumSize()
```

Returns the maximum size of this container. If the maximum size has
not been set explicitly by

Component.setMaximumSize(Dimension)

and the

LayoutManager

installed on this

Container

is an instance of

LayoutManager2

, then

LayoutManager2.maximumLayoutSize(Container)

is used to calculate the maximum size.

Note: some implementations may cache the value returned from the

LayoutManager2

. Implementations that cache need not invoke

maximumLayoutSize

on the

LayoutManager2

every time
this method is invoked, rather the

LayoutManager2

will only
be queried after the

Container

becomes invalid.

**Overrides:** getMaximumSize

in class

Component
**Returns:** an instance of

Dimension

that represents
the maximum size of this container.
**See Also:** getPreferredSize()

,

getMinimumSize()

,

getLayout()

,

LayoutManager2.maximumLayoutSize(Container)

,

Component.getMaximumSize()

- getAlignmentX

```java
public float getAlignmentX()
```

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Overrides:** getAlignmentX

in class

Component
**Returns:** the horizontal alignment of this component

- getAlignmentY

```java
public float getAlignmentY()
```

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Overrides:** getAlignmentY

in class

Component
**Returns:** the vertical alignment of this component

- paint

```java
public void paint​(
Graphics
g)
```

Paints the container. This forwards the paint to any lightweight
components that are children of this container. If this method is
reimplemented, super.paint(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, paint() will not be
forwarded to that child.

**Overrides:** paint

in class

Component
**Parameters:** g

- the specified Graphics window
**See Also:** Component.update(Graphics)

- update

```java
public void update​(
Graphics
g)
```

Updates the container. This forwards the update to any lightweight
components that are children of this container. If this method is
reimplemented, super.update(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, update() will not be
forwarded to that child.

**Overrides:** update

in class

Component
**Parameters:** g

- the specified Graphics window
**See Also:** Component.update(Graphics)

- print

```java
public void print​(
Graphics
g)
```

Prints the container. This forwards the print to any lightweight
components that are children of this container. If this method is
reimplemented, super.print(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, print() will not be
forwarded to that child.

**Overrides:** print

in class

Component
**Parameters:** g

- the specified Graphics window
**See Also:** Component.update(Graphics)

- paintComponents

```java
public void paintComponents​(
Graphics
g)
```

Paints each of the components in this container.

**Parameters:** g

- the graphics context.
**See Also:** Component.paint(java.awt.Graphics)

,

Component.paintAll(java.awt.Graphics)

- printComponents

```java
public void printComponents​(
Graphics
g)
```

Prints each of the components in this container.

**Parameters:** g

- the graphics context.
**See Also:** Component.print(java.awt.Graphics)

,

Component.printAll(java.awt.Graphics)

- addContainerListener

```java
public void addContainerListener​(
ContainerListener
l)
```

Adds the specified container listener to receive container events
from this container.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the container listener
**See Also:** removeContainerListener(java.awt.event.ContainerListener)

,

getContainerListeners()

- removeContainerListener

```java
public void removeContainerListener​(
ContainerListener
l)
```

Removes the specified container listener so it no longer receives
container events from this container.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the container listener
**See Also:** addContainerListener(java.awt.event.ContainerListener)

,

getContainerListeners()

- getContainerListeners

```java
public
ContainerListener
[] getContainerListeners()
```

Returns an array of all the container listeners
registered on this container.

**Returns:** all of this container's

ContainerListener

s
or an empty array if no container
listeners are currently registered
**Since:** 1.4
**See Also:** addContainerListener(java.awt.event.ContainerListener)

,

removeContainerListener(java.awt.event.ContainerListener)

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Container

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Container c

for its container listeners with the following code:

```java
ContainerListener[] cls = (ContainerListener[])(c.getListeners(ContainerListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Component
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this container,
or an empty array if no such listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Throws:** NullPointerException

- if

listenerType

is

null
**Since:** 1.3
**See Also:** getContainerListeners()

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this container. If the event is a

ContainerEvent

, it invokes the

processContainerEvent

method, else it invokes
its superclass's

processEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Component
**Parameters:** e

- the event
**See Also:** Component.processComponentEvent(java.awt.event.ComponentEvent)

,

Component.processFocusEvent(java.awt.event.FocusEvent)

,

Component.processKeyEvent(java.awt.event.KeyEvent)

,

Component.processMouseEvent(java.awt.event.MouseEvent)

,

Component.processMouseMotionEvent(java.awt.event.MouseEvent)

,

Component.processInputMethodEvent(java.awt.event.InputMethodEvent)

,

Component.processHierarchyEvent(java.awt.event.HierarchyEvent)

,

Component.processMouseWheelEvent(java.awt.event.MouseWheelEvent)

- processContainerEvent

```java
protected void processContainerEvent​(
ContainerEvent
e)
```

Processes container events occurring on this container by
dispatching them to any registered ContainerListener objects.
NOTE: This method will not be called unless container events
are enabled for this component; this happens when one of the
following occurs:

- A ContainerListener object is registered via

addContainerListener

Container events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the container event
**See Also:** Component.enableEvents(long)

- deliverEvent

```java
@Deprecated

public void deliverEvent​(
Event
e)
```

Deprecated.

As of JDK version 1.1,
replaced by

dispatchEvent(AWTEvent e)

**Overrides:** deliverEvent

in class

Component
**Parameters:** e

- the event to deliver

- getComponentAt

```java
public
Component
getComponentAt​(int x,
int y)
```

Locates the component that contains the x,y position. The
top-most child component is returned in the case where there
is overlap in the components. This is determined by finding
the component closest to the index 0 that claims to contain
the given point via Component.contains(), except that Components
which have native peers take precedence over those which do not
(i.e., lightweight Components).

**Overrides:** getComponentAt

in class

Component
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Returns:** null if the component does not contain the position.
If there is no child component at the requested point and the
point is within the bounds of the container the container itself
is returned; otherwise the top-most child is returned.
**Since:** 1.1
**See Also:** Component.contains(int, int)

- locate

```java
@Deprecated

public
Component
locate​(int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by

getComponentAt(int, int)

.

Description copied from class:

Component

Returns the component occupying the position specified (this component,
or immediate child component, or null if neither
of the first two occupies the location).

**Overrides:** locate

in class

Component
**Parameters:** x

- the

x

coordinate to search for components at
**Parameters:** y

- the

y

coordinate to search for components at
**Returns:** the component at the specified location or

null

- getComponentAt

```java
public
Component
getComponentAt​(
Point
p)
```

Gets the component that contains the specified point.

**Overrides:** getComponentAt

in class

Component
**Parameters:** p

- the point.
**Returns:** returns the component that contains the point,
or

null

if the component does
not contain the point.
**Since:** 1.1
**See Also:** Component.contains(int, int)

- getMousePosition

```java
public
Point
getMousePosition​(boolean allowChildren)
throws
HeadlessException
```

Returns the position of the mouse pointer in this

Container

's
coordinate space if the

Container

is under the mouse pointer,
otherwise returns

null

.
This method is similar to

Component.getMousePosition()

with the exception
that it can take the

Container

's children into account.
If

allowChildren

is

false

, this method will return
a non-null value only if the mouse pointer is above the

Container

directly, not above the part obscured by children.
If

allowChildren

is

true

, this method returns
a non-null value if the mouse pointer is above

Container

or any
of its descendants.

**Parameters:** allowChildren

- true if children should be taken into account
**Returns:** mouse coordinates relative to this

Component

, or null
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless() returns true
**Since:** 1.5
**See Also:** Component.getMousePosition()

- findComponentAt

```java
public
Component
findComponentAt​(int x,
int y)
```

Locates the visible child component that contains the specified
position. The top-most child component is returned in the case
where there is overlap in the components. If the containing child
component is a Container, this method will continue searching for
the deepest nested child component. Components which are not
visible are ignored during the search.

The findComponentAt method is different from getComponentAt in
that getComponentAt only searches the Container's immediate
children; if the containing component is a Container,
findComponentAt will search that child to find a nested component.

**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Returns:** null if the component does not contain the position.
If there is no child component at the requested point and the
point is within the bounds of the container the container itself
is returned.
**Since:** 1.2
**See Also:** Component.contains(int, int)

,

getComponentAt(int, int)

- findComponentAt

```java
public
Component
findComponentAt​(
Point
p)
```

Locates the visible child component that contains the specified
point. The top-most child component is returned in the case
where there is overlap in the components. If the containing child
component is a Container, this method will continue searching for
the deepest nested child component. Components which are not
visible are ignored during the search.

The findComponentAt method is different from getComponentAt in
that getComponentAt only searches the Container's immediate
children; if the containing component is a Container,
findComponentAt will search that child to find a nested component.

**Parameters:** p

- the point.
**Returns:** null if the component does not contain the position.
If there is no child component at the requested point and the
point is within the bounds of the container the container itself
is returned.
**Throws:** NullPointerException

- if

p

is

null
**Since:** 1.2
**See Also:** Component.contains(int, int)

,

getComponentAt(int, int)

- addNotify

```java
public void addNotify()
```

Makes this Container displayable by connecting it to
a native screen resource. Making a container displayable will
cause all of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:** addNotify

in class

Component
**See Also:** Component.isDisplayable()

,

removeNotify()

- removeNotify

```java
public void removeNotify()
```

Makes this Container undisplayable by removing its connection
to its native screen resource. Making a container undisplayable
will cause all of its children to be made undisplayable.
This method is called by the toolkit internally and should
not be called directly by programs.

**Overrides:** removeNotify

in class

Component
**See Also:** Component.isDisplayable()

,

addNotify()

- isAncestorOf

```java
public boolean isAncestorOf​(
Component
c)
```

Checks if the component is contained in the component hierarchy of
this container.

**Parameters:** c

- the component
**Returns:** true

if it is an ancestor;

false

otherwise.
**Since:** 1.1

- paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

Container

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Component
**Returns:** the parameter string of this container

- list

```java
public void list​(
PrintStream
out,
int indent)
```

Prints a listing of this container to the specified output
stream. The listing starts at the specified indentation.

The immediate children of the container are printed with
an indentation of

indent+1

. The children
of those children are printed at

indent+2

and so on.

**Overrides:** list

in class

Component
**Parameters:** out

- a print stream
**Parameters:** indent

- the number of spaces to indent
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.0
**See Also:** Component.list(java.io.PrintStream, int)

- list

```java
public void list​(
PrintWriter
out,
int indent)
```

Prints out a list, starting at the specified indentation,
to the specified print writer.

The immediate children of the container are printed with
an indentation of

indent+1

. The children
of those children are printed at

indent+2

and so on.

**Overrides:** list

in class

Component
**Parameters:** out

- a print writer
**Parameters:** indent

- the number of spaces to indent
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.1
**See Also:** Component.list(java.io.PrintWriter, int)

- setFocusTraversalKeys

```java
public void setFocusTraversalKeys​(int id,

Set
<? extends
AWTKeyStroke
> keystrokes)
```

Sets the focus traversal keys for a given traversal operation for this
Container.

The default values for a Container's focus traversal keys are
implementation-dependent. Sun recommends that all implementations for a
particular native platform use the same default values. The
recommendations for Windows and Unix are listed below. These
recommendations are used in the Sun AWT implementations.

Recommended default values for a Container's focus traversal
keys

Identifier

Meaning

Default

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

Normal forward keyboard traversal

TAB on KEY_PRESSED, CTRL-TAB on KEY_PRESSED

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

Normal reverse keyboard traversal

SHIFT-TAB on KEY_PRESSED, CTRL-SHIFT-TAB on KEY_PRESSED

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

Go up one focus traversal cycle

none

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

Go down one focus traversal cycle

none

To disable a traversal key, use an empty Set; Collections.EMPTY_SET is
recommended.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Container. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Container inherits the
Set from its parent. If all ancestors of this Container have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

**Overrides:** setFocusTraversalKeys

in class

Component
**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Parameters:** keystrokes

- the Set of AWTKeyStroke for the specified operation
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS, or if keystrokes
contains null, or if any keystroke represents a KEY_TYPED event,
or if any keystroke already maps to another focus traversal
operation for this Container
**Since:** 1.4
**See Also:** getFocusTraversalKeys(int)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

,

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

- getFocusTraversalKeys

```java
public
Set
<
AWTKeyStroke
> getFocusTraversalKeys​(int id)
```

Returns the Set of focus traversal keys for a given traversal operation
for this Container. (See

setFocusTraversalKeys

for a full description of each key.)

If a Set of traversal keys has not been explicitly defined for this
Container, then this Container's parent's Set is returned. If no Set
has been explicitly defined for any of this Container's ancestors, then
the current KeyboardFocusManager's default Set is returned.

**Overrides:** getFocusTraversalKeys

in class

Component
**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Returns:** the Set of AWTKeyStrokes for the specified operation. The Set
will be unmodifiable, and may be empty. null will never be
returned.
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4
**See Also:** setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

,

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

- areFocusTraversalKeysSet

```java
public boolean areFocusTraversalKeysSet​(int id)
```

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Container. If
this method returns

false

, this Container is inheriting the
Set from an ancestor, or from the current KeyboardFocusManager.

**Overrides:** areFocusTraversalKeysSet

in class

Component
**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Returns:** true

if the Set of focus traversal keys for the
given focus traversal operation has been explicitly defined for
this Component;

false

otherwise.
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4

- isFocusCycleRoot

```java
public boolean isFocusCycleRoot​(
Container
container)
```

Returns whether the specified Container is the focus cycle root of this
Container's focus traversal cycle. Each focus traversal cycle has only
a single focus cycle root and each Container which is not a focus cycle
root belongs to only a single focus traversal cycle. Containers which
are focus cycle roots belong to two cycles: one rooted at the Container
itself, and one rooted at the Container's nearest focus-cycle-root
ancestor. This method will return

true

for both such
Containers in this case.

**Overrides:** isFocusCycleRoot

in class

Component
**Parameters:** container

- the Container to be tested
**Returns:** true

if the specified Container is a focus-cycle-
root of this Container;

false

otherwise
**Since:** 1.4
**See Also:** isFocusCycleRoot()

- setFocusTraversalPolicy

```java
public void setFocusTraversalPolicy​(
FocusTraversalPolicy
policy)
```

Sets the focus traversal policy that will manage keyboard traversal of
this Container's children, if this Container is a focus cycle root. If
the argument is null, this Container inherits its policy from its focus-
cycle-root ancestor. If the argument is non-null, this policy will be
inherited by all focus-cycle-root children that have no keyboard-
traversal policy of their own (as will, recursively, their focus-cycle-
root children).

If this Container is not a focus cycle root, the policy will be
remembered, but will not be used or inherited by this or any other
Containers until this Container is made a focus cycle root.

**Parameters:** policy

- the new focus traversal policy for this Container
**Since:** 1.4
**See Also:** getFocusTraversalPolicy()

,

setFocusCycleRoot(boolean)

,

isFocusCycleRoot(java.awt.Container)

- getFocusTraversalPolicy

```java
public
FocusTraversalPolicy
getFocusTraversalPolicy()
```

Returns the focus traversal policy that will manage keyboard traversal
of this Container's children, or null if this Container is not a focus
cycle root. If no traversal policy has been explicitly set for this
Container, then this Container's focus-cycle-root ancestor's policy is
returned.

**Returns:** this Container's focus traversal policy, or null if this
Container is not a focus cycle root.
**Since:** 1.4
**See Also:** setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

setFocusCycleRoot(boolean)

,

isFocusCycleRoot(java.awt.Container)

- isFocusTraversalPolicySet

```java
public boolean isFocusTraversalPolicySet()
```

Returns whether the focus traversal policy has been explicitly set for
this Container. If this method returns

false

, this
Container will inherit its focus traversal policy from an ancestor.

**Returns:** true

if the focus traversal policy has been
explicitly set for this Container;

false

otherwise.
**Since:** 1.4

- setFocusCycleRoot

```java
public void setFocusCycleRoot​(boolean focusCycleRoot)
```

Sets whether this Container is the root of a focus traversal cycle. Once
focus enters a traversal cycle, typically it cannot leave it via focus
traversal unless one of the up- or down-cycle keys is pressed. Normal
traversal is limited to this Container, and all of this Container's
descendants that are not descendants of inferior focus cycle roots. Note
that a FocusTraversalPolicy may bend these restrictions, however. For
example, ContainerOrderFocusTraversalPolicy supports implicit down-cycle
traversal.

The alternative way to specify the traversal order of this Container's
children is to make this Container a

focus traversal policy provider

.

**Parameters:** focusCycleRoot

- indicates whether this Container is the root of a
focus traversal cycle
**Since:** 1.4
**See Also:** isFocusCycleRoot()

,

setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

ContainerOrderFocusTraversalPolicy

,

setFocusTraversalPolicyProvider(boolean)

- isFocusCycleRoot

```java
public boolean isFocusCycleRoot()
```

Returns whether this Container is the root of a focus traversal cycle.
Once focus enters a traversal cycle, typically it cannot leave it via
focus traversal unless one of the up- or down-cycle keys is pressed.
Normal traversal is limited to this Container, and all of this
Container's descendants that are not descendants of inferior focus
cycle roots. Note that a FocusTraversalPolicy may bend these
restrictions, however. For example, ContainerOrderFocusTraversalPolicy
supports implicit down-cycle traversal.

**Returns:** whether this Container is the root of a focus traversal cycle
**Since:** 1.4
**See Also:** setFocusCycleRoot(boolean)

,

setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

ContainerOrderFocusTraversalPolicy

- setFocusTraversalPolicyProvider

```java
public final void setFocusTraversalPolicyProvider​(boolean provider)
```

Sets whether this container will be used to provide focus
traversal policy. Container with this property as

true

will be used to acquire focus traversal policy
instead of closest focus cycle root ancestor.

**Parameters:** provider

- indicates whether this container will be used to
provide focus traversal policy
**Since:** 1.5
**See Also:** setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

isFocusTraversalPolicyProvider()

- isFocusTraversalPolicyProvider

```java
public final boolean isFocusTraversalPolicyProvider()
```

Returns whether this container provides focus traversal
policy. If this property is set to

true

then when
keyboard focus manager searches container hierarchy for focus
traversal policy and encounters this container before any other
container with this property as true or focus cycle roots then
its focus traversal policy will be used instead of focus cycle
root's policy.

**Returns:** true

if this container provides focus traversal
policy,

false

otherwise
**Since:** 1.5
**See Also:** setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

setFocusCycleRoot(boolean)

,

setFocusTraversalPolicyProvider(boolean)

- transferFocusDownCycle

```java
public void transferFocusDownCycle()
```

Transfers the focus down one focus traversal cycle. If this Container is
a focus cycle root, then the focus owner is set to this Container's
default Component to focus, and the current focus cycle root is set to
this Container. If this Container is not a focus cycle root, then no
focus traversal operation occurs.

**Since:** 1.4
**See Also:** Component.requestFocus()

,

isFocusCycleRoot(java.awt.Container)

,

setFocusCycleRoot(boolean)

- applyComponentOrientation

```java
public void applyComponentOrientation​(
ComponentOrientation
o)
```

Sets the

ComponentOrientation

property of this container
and all components contained within it.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Overrides:** applyComponentOrientation

in class

Component
**Parameters:** o

- the new component orientation of this container and
the components contained within it.
**Throws:** NullPointerException

- if

orientation

is null.
**Since:** 1.4
**See Also:** Component.setComponentOrientation(java.awt.ComponentOrientation)

,

Component.getComponentOrientation()

,

invalidate()

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Container's font ("font")
- this Container's background color ("background")
- this Container's foreground color ("foreground")
- this Container's focusability ("focusable")
- this Container's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Container's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Container's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Container's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Container's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Container's focus traversal policy ("focusTraversalPolicy")
- this Container's focus-cycle-root state ("focusCycleRoot")

Note that if this Container is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:** addPropertyChangeListener

in class

Component
**Parameters:** listener

- the PropertyChangeListener to be added
**See Also:** Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

,

addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following defaults:

- this Container's font ("font")
- this Container's background color ("background")
- this Container's foreground color ("foreground")
- this Container's focusability ("focusable")
- this Container's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Container's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Container's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Container's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Container's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Container's focus traversal policy ("focusTraversalPolicy")
- this Container's focus-cycle-root state ("focusCycleRoot")
- this Container's focus-traversal-policy-provider state("focusTraversalPolicyProvider")
- this Container's focus-traversal-policy-provider state("focusTraversalPolicyProvider")

Note that if this Container is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:** addPropertyChangeListener

in class

Component
**Parameters:** propertyName

- one of the property names listed above
**Parameters:** listener

- the PropertyChangeListener to be added
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

---

#### Method Detail

getComponentCount

```java
public int getComponentCount()
```

Gets the number of components in this panel.

Note: This method should be called under AWT tree lock.

**Returns:** the number of components in this panel.
**Since:** 1.1
**See Also:** getComponent(int)

,

Component.getTreeLock()

---

#### getComponentCount

public int getComponentCount()

Gets the number of components in this panel.

Note: This method should be called under AWT tree lock.

Note: This method should be called under AWT tree lock.

countComponents

```java
@Deprecated

public int countComponents()
```

Deprecated.

As of JDK version 1.1,
replaced by getComponentCount().

Returns the number of components in this container.

**Returns:** the number of components in this container

---

#### countComponents

@Deprecated

public int countComponents()

Returns the number of components in this container.

getComponent

```java
public
Component
getComponent​(int n)
```

Gets the nth component in this container.

Note: This method should be called under AWT tree lock.

**Parameters:** n

- the index of the component to get.
**Returns:** the n

th

component in this container.
**Throws:** ArrayIndexOutOfBoundsException

- if the n

th

value does not exist.
**See Also:** Component.getTreeLock()

---

#### getComponent

public

Component

getComponent​(int n)

Gets the nth component in this container.

Note: This method should be called under AWT tree lock.

Note: This method should be called under AWT tree lock.

getComponents

```java
public
Component
[] getComponents()
```

Gets all the components in this container.

Note: This method should be called under AWT tree lock.

**Returns:** an array of all the components in this container.
**See Also:** Component.getTreeLock()

---

#### getComponents

public

Component

[] getComponents()

Gets all the components in this container.

Note: This method should be called under AWT tree lock.

Note: This method should be called under AWT tree lock.

getInsets

```java
public
Insets
getInsets()
```

Determines the insets of this container, which indicate the size
of the container's border.

A

Frame

object, for example, has a top inset that
corresponds to the height of the frame's title bar.

**Returns:** the insets of this container.
**Since:** 1.1
**See Also:** Insets

,

LayoutManager

---

#### getInsets

public

Insets

getInsets()

Determines the insets of this container, which indicate the size
of the container's border.

A

Frame

object, for example, has a top inset that
corresponds to the height of the frame's title bar.

A

Frame

object, for example, has a top inset that
corresponds to the height of the frame's title bar.

insets

```java
@Deprecated

public
Insets
insets()
```

Deprecated.

As of JDK version 1.1,
replaced by

getInsets()

.

Returns the insets for this container.

**Returns:** the insets for this container

---

#### insets

@Deprecated

public

Insets

insets()

Returns the insets for this container.

add

```java
public
Component
add​(
Component
comp)
```

Appends the specified component to the end of this container.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Returns:** the component argument
**Throws:** NullPointerException

- if

comp

is

null
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

---

#### add

public

Component

add​(

Component

comp)

Appends the specified component to the end of this container.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

add

```java
public
Component
add​(
String
name,

Component
comp)
```

Adds the specified component to this container.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method is obsolete as of 1.1. Please use the
method

add(Component, Object)

instead.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** name

- the name of the component to be added
**Parameters:** comp

- the component to be added
**Returns:** the component added
**Throws:** NullPointerException

- if

comp

is

null
**See Also:** add(Component, Object)

,

invalidate()

---

#### add

public

Component

add​(

String

name,

Component

comp)

Adds the specified component to this container.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method is obsolete as of 1.1. Please use the
method

add(Component, Object)

instead.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

This method is obsolete as of 1.1. Please use the
method

add(Component, Object)

instead.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

add

```java
public
Component
add​(
Component
comp,
int index)
```

Adds the specified component to this container at the given
position.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Parameters:** index

- the position at which to insert the component,
or

-1

to append the component to the end
**Returns:** the component

comp
**Throws:** NullPointerException

- if

comp

is

null
**Throws:** IllegalArgumentException

- if

index

is invalid (see

addImpl(java.awt.Component, java.lang.Object, int)

for details)
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

remove(int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

---

#### add

public

Component

add​(

Component

comp,
int index)

Adds the specified component to this container at the given
position.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

setComponentZOrder

```java
public void setComponentZOrder​(
Component
comp,
int index)
```

Moves the specified component to the specified z-order index in
the container. The z-order determines the order that components
are painted; the component with the highest z-order paints first
and the component with the lowest z-order paints last.
Where components overlap, the component with the lower
z-order paints over the component with the higher z-order.

If the component is a child of some other container, it is
removed from that container before being added to this container.
The important difference between this method and

java.awt.Container.add(Component, int)

is that this method
doesn't call

removeNotify

on the component while
removing it from its previous container unless necessary and when
allowed by the underlying native windowing system. This way, if the
component has the keyboard focus, it maintains the focus when
moved to the new position.

This property is guaranteed to apply only to lightweight
non-

Container

components.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

Note

: Not all platforms support changing the z-order of
heavyweight components from one container into another without
the call to

removeNotify

. There is no way to detect
whether a platform supports this, so developers shouldn't make
any assumptions.

**Parameters:** comp

- the component to be moved
**Parameters:** index

- the position in the container's list to
insert the component, where

getComponentCount()

appends to the end
**Throws:** NullPointerException

- if

comp

is

null
**Throws:** IllegalArgumentException

- if

comp

is one of the
container's parents
**Throws:** IllegalArgumentException

- if

index

is not in
the range

[0, getComponentCount()]

for moving
between containers, or not in the range

[0, getComponentCount()-1]

for moving inside
a container
**Throws:** IllegalArgumentException

- if adding a container to itself
**Throws:** IllegalArgumentException

- if adding a

Window

to a container
**Since:** 1.5
**See Also:** getComponentZOrder(java.awt.Component)

,

invalidate()

---

#### setComponentZOrder

public void setComponentZOrder​(

Component

comp,
int index)

Moves the specified component to the specified z-order index in
the container. The z-order determines the order that components
are painted; the component with the highest z-order paints first
and the component with the lowest z-order paints last.
Where components overlap, the component with the lower
z-order paints over the component with the higher z-order.

If the component is a child of some other container, it is
removed from that container before being added to this container.
The important difference between this method and

java.awt.Container.add(Component, int)

is that this method
doesn't call

removeNotify

on the component while
removing it from its previous container unless necessary and when
allowed by the underlying native windowing system. This way, if the
component has the keyboard focus, it maintains the focus when
moved to the new position.

This property is guaranteed to apply only to lightweight
non-

Container

components.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

Note

: Not all platforms support changing the z-order of
heavyweight components from one container into another without
the call to

removeNotify

. There is no way to detect
whether a platform supports this, so developers shouldn't make
any assumptions.

If the component is a child of some other container, it is
removed from that container before being added to this container.
The important difference between this method and

java.awt.Container.add(Component, int)

is that this method
doesn't call

removeNotify

on the component while
removing it from its previous container unless necessary and when
allowed by the underlying native windowing system. This way, if the
component has the keyboard focus, it maintains the focus when
moved to the new position.

This property is guaranteed to apply only to lightweight
non-

Container

components.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

Note

: Not all platforms support changing the z-order of
heavyweight components from one container into another without
the call to

removeNotify

. There is no way to detect
whether a platform supports this, so developers shouldn't make
any assumptions.

This property is guaranteed to apply only to lightweight
non-

Container

components.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

Note

: Not all platforms support changing the z-order of
heavyweight components from one container into another without
the call to

removeNotify

. There is no way to detect
whether a platform supports this, so developers shouldn't make
any assumptions.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

Note

: Not all platforms support changing the z-order of
heavyweight components from one container into another without
the call to

removeNotify

. There is no way to detect
whether a platform supports this, so developers shouldn't make
any assumptions.

Note

: Not all platforms support changing the z-order of
heavyweight components from one container into another without
the call to

removeNotify

. There is no way to detect
whether a platform supports this, so developers shouldn't make
any assumptions.

getComponentZOrder

```java
public int getComponentZOrder​(
Component
comp)
```

Returns the z-order index of the component inside the container.
The higher a component is in the z-order hierarchy, the lower
its index. The component with the lowest z-order index is
painted last, above all other child components.

**Parameters:** comp

- the component being queried
**Returns:** the z-order index of the component; otherwise
returns -1 if the component is

null

or doesn't belong to the container
**Since:** 1.5
**See Also:** setComponentZOrder(java.awt.Component, int)

---

#### getComponentZOrder

public int getComponentZOrder​(

Component

comp)

Returns the z-order index of the component inside the container.
The higher a component is in the z-order hierarchy, the lower
its index. The component with the lowest z-order index is
painted last, above all other child components.

add

```java
public void add​(
Component
comp,

Object
constraints)
```

Adds the specified component to the end of this container.
Also notifies the layout manager to add the component to
this container's layout using the specified constraints object.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing
layout constraints for this component
**Throws:** NullPointerException

- if

comp

is

null
**Since:** 1.1
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

,

LayoutManager

---

#### add

public void add​(

Component

comp,

Object

constraints)

Adds the specified component to the end of this container.
Also notifies the layout manager to add the component to
this container's layout using the specified constraints object.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

add

```java
public void add​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this container with the specified
constraints at the specified index. Also notifies the layout
manager to add the component to the this container's layout using
the specified constraints object.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing layout constraints for this
**Parameters:** index

- the position in the container's list at which to insert
the component;

-1

means insert at the end
component
**Throws:** NullPointerException

- if

comp

is

null
**Throws:** IllegalArgumentException

- if

index

is invalid (see

addImpl(java.awt.Component, java.lang.Object, int)

for details)
**See Also:** addImpl(java.awt.Component, java.lang.Object, int)

,

invalidate()

,

validate()

,

JComponent.revalidate()

,

remove(int)

,

LayoutManager

---

#### add

public void add​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this container with the specified
constraints at the specified index. Also notifies the layout
manager to add the component to the this container's layout using
the specified constraints object.
This is a convenience method for

addImpl(java.awt.Component, java.lang.Object, int)

.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this container at the specified
index. This method also notifies the layout manager to add
the component to this container's layout using the specified
constraints object via the

addLayoutComponent

method.

The constraints are
defined by the particular layout manager being used. For
example, the

BorderLayout

class defines five
constraints:

BorderLayout.NORTH

,

BorderLayout.SOUTH

,

BorderLayout.EAST

,

BorderLayout.WEST

, and

BorderLayout.CENTER

.

The

GridBagLayout

class requires a

GridBagConstraints

object. Failure to pass
the correct type of constraints object results in an

IllegalArgumentException

.

If the current layout manager implements

LayoutManager2

, then

LayoutManager2.addLayoutComponent(Component,Object)

is invoked on
it. If the current layout manager does not implement

LayoutManager2

, and constraints is a

String

, then

LayoutManager.addLayoutComponent(String,Component)

is invoked on it.

If the component is not an ancestor of this container and has a non-null
parent, it is removed from its current parent before it is added to this
container.

This is the method to override if a program needs to track
every add request to a container as all other add methods defer
to this one. An overriding method should
usually include a call to the superclass's version of the method:

super.addImpl(comp, constraints, index)

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing layout constraints
for this component
**Parameters:** index

- the position in the container's list at which to
insert the component, where

-1

means append to the end
**Throws:** IllegalArgumentException

- if

index

is invalid;
if

comp

is a child of this container, the valid
range is

[-1, getComponentCount()-1]

; if component is
not a child of this container, the valid range is

[-1, getComponentCount()]
**Throws:** IllegalArgumentException

- if

comp

is an ancestor of
this container
**Throws:** IllegalArgumentException

- if adding a window to a container
**Throws:** NullPointerException

- if

comp

is

null
**Since:** 1.1
**See Also:** add(Component)

,

add(Component, int)

,

add(Component, java.lang.Object)

,

invalidate()

,

LayoutManager

,

LayoutManager2

---

#### addImpl

protected void addImpl​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this container at the specified
index. This method also notifies the layout manager to add
the component to this container's layout using the specified
constraints object via the

addLayoutComponent

method.

The constraints are
defined by the particular layout manager being used. For
example, the

BorderLayout

class defines five
constraints:

BorderLayout.NORTH

,

BorderLayout.SOUTH

,

BorderLayout.EAST

,

BorderLayout.WEST

, and

BorderLayout.CENTER

.

The

GridBagLayout

class requires a

GridBagConstraints

object. Failure to pass
the correct type of constraints object results in an

IllegalArgumentException

.

If the current layout manager implements

LayoutManager2

, then

LayoutManager2.addLayoutComponent(Component,Object)

is invoked on
it. If the current layout manager does not implement

LayoutManager2

, and constraints is a

String

, then

LayoutManager.addLayoutComponent(String,Component)

is invoked on it.

If the component is not an ancestor of this container and has a non-null
parent, it is removed from its current parent before it is added to this
container.

This is the method to override if a program needs to track
every add request to a container as all other add methods defer
to this one. An overriding method should
usually include a call to the superclass's version of the method:

super.addImpl(comp, constraints, index)

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

The constraints are
defined by the particular layout manager being used. For
example, the

BorderLayout

class defines five
constraints:

BorderLayout.NORTH

,

BorderLayout.SOUTH

,

BorderLayout.EAST

,

BorderLayout.WEST

, and

BorderLayout.CENTER

.

The

GridBagLayout

class requires a

GridBagConstraints

object. Failure to pass
the correct type of constraints object results in an

IllegalArgumentException

.

If the current layout manager implements

LayoutManager2

, then

LayoutManager2.addLayoutComponent(Component,Object)

is invoked on
it. If the current layout manager does not implement

LayoutManager2

, and constraints is a

String

, then

LayoutManager.addLayoutComponent(String,Component)

is invoked on it.

If the component is not an ancestor of this container and has a non-null
parent, it is removed from its current parent before it is added to this
container.

This is the method to override if a program needs to track
every add request to a container as all other add methods defer
to this one. An overriding method should
usually include a call to the superclass's version of the method:

super.addImpl(comp, constraints, index)

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

The

GridBagLayout

class requires a

GridBagConstraints

object. Failure to pass
the correct type of constraints object results in an

IllegalArgumentException

.

If the current layout manager implements

LayoutManager2

, then

LayoutManager2.addLayoutComponent(Component,Object)

is invoked on
it. If the current layout manager does not implement

LayoutManager2

, and constraints is a

String

, then

LayoutManager.addLayoutComponent(String,Component)

is invoked on it.

If the component is not an ancestor of this container and has a non-null
parent, it is removed from its current parent before it is added to this
container.

This is the method to override if a program needs to track
every add request to a container as all other add methods defer
to this one. An overriding method should
usually include a call to the superclass's version of the method:

super.addImpl(comp, constraints, index)

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

If the current layout manager implements

LayoutManager2

, then

LayoutManager2.addLayoutComponent(Component,Object)

is invoked on
it. If the current layout manager does not implement

LayoutManager2

, and constraints is a

String

, then

LayoutManager.addLayoutComponent(String,Component)

is invoked on it.

If the component is not an ancestor of this container and has a non-null
parent, it is removed from its current parent before it is added to this
container.

This is the method to override if a program needs to track
every add request to a container as all other add methods defer
to this one. An overriding method should
usually include a call to the superclass's version of the method:

super.addImpl(comp, constraints, index)

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

If the component is not an ancestor of this container and has a non-null
parent, it is removed from its current parent before it is added to this
container.

This is the method to override if a program needs to track
every add request to a container as all other add methods defer
to this one. An overriding method should
usually include a call to the superclass's version of the method:

super.addImpl(comp, constraints, index)

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

This is the method to override if a program needs to track
every add request to a container as all other add methods defer
to this one. An overriding method should
usually include a call to the superclass's version of the method:

super.addImpl(comp, constraints, index)

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
display the added component.

remove

```java
public void remove​(int index)
```

Removes the component, specified by

index

,
from this container.
This method also notifies the layout manager to remove the
component from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

**Parameters:** index

- the index of the component to be removed
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is not in
range

[0, getComponentCount()-1]
**Since:** 1.1
**See Also:** add(java.awt.Component)

,

invalidate()

,

validate()

,

getComponentCount()

---

#### remove

public void remove​(int index)

Removes the component, specified by

index

,
from this container.
This method also notifies the layout manager to remove the
component from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

remove

```java
public void remove​(
Component
comp)
```

Removes the specified component from this container.
This method also notifies the layout manager to remove the
component from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

**Parameters:** comp

- the component to be removed
**Throws:** NullPointerException

- if

comp

is

null
**See Also:** add(java.awt.Component)

,

invalidate()

,

validate()

,

remove(int)

---

#### remove

public void remove​(

Component

comp)

Removes the specified component from this container.
This method also notifies the layout manager to remove the
component from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

removeAll

```java
public void removeAll()
```

Removes all the components from this container.
This method also notifies the layout manager to remove the
components from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

**See Also:** add(java.awt.Component)

,

remove(int)

,

invalidate()

---

#### removeAll

public void removeAll()

Removes all the components from this container.
This method also notifies the layout manager to remove the
components from this container's layout via the

removeLayoutComponent

method.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

This method changes layout-related information, and therefore,
invalidates the component hierarchy. If the container has already been
displayed, the hierarchy must be validated thereafter in order to
reflect the changes.

getLayout

```java
public
LayoutManager
getLayout()
```

Gets the layout manager for this container.

**Returns:** the current layout manager for this container
**See Also:** doLayout()

,

setLayout(java.awt.LayoutManager)

---

#### getLayout

public

LayoutManager

getLayout()

Gets the layout manager for this container.

setLayout

```java
public void setLayout​(
LayoutManager
mgr)
```

Sets the layout manager for this container.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Parameters:** mgr

- the specified layout manager
**See Also:** doLayout()

,

getLayout()

,

invalidate()

---

#### setLayout

public void setLayout​(

LayoutManager

mgr)

Sets the layout manager for this container.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

doLayout

```java
public void doLayout()
```

Causes this container to lay out its components. Most programs
should not call this method directly, but should invoke
the

validate

method instead.

**Overrides:** doLayout

in class

Component
**Since:** 1.1
**See Also:** LayoutManager.layoutContainer(java.awt.Container)

,

setLayout(java.awt.LayoutManager)

,

validate()

---

#### doLayout

public void doLayout()

Causes this container to lay out its components. Most programs
should not call this method directly, but should invoke
the

validate

method instead.

layout

```java
@Deprecated

public void layout()
```

Deprecated.

As of JDK version 1.1,
replaced by

doLayout()

.

**Overrides:** layout

in class

Component

---

#### layout

@Deprecated

public void layout()

isValidateRoot

```java
public boolean isValidateRoot()
```

Indicates if this container is a

validate root

.

Layout-related changes, such as bounds of the validate root descendants,
do not affect the layout of the validate root parent. This peculiarity
enables the

invalidate()

method to stop invalidating the
component hierarchy when the method encounters a validate root. However,
to preserve backward compatibility this new optimized behavior is
enabled only when the

java.awt.smartInvalidate

system property
value is set to

true

.

If a component hierarchy contains validate roots and the new optimized

invalidate()

behavior is enabled, the

validate()

method
must be invoked on the validate root of a previously invalidated
component to restore the validity of the hierarchy later. Otherwise,
calling the

validate()

method on the top-level container (such
as a

Frame

object) should be used to restore the validity of the
component hierarchy.

The

Window

class and the

Applet

class are the validate
roots in AWT. Swing introduces more validate roots.

**Returns:** whether this container is a validate root
**Since:** 1.7
**See Also:** invalidate()

,

Component.invalidate()

,

JComponent.isValidateRoot()

,

JComponent.revalidate()

---

#### isValidateRoot

public boolean isValidateRoot()

Indicates if this container is a

validate root

.

Layout-related changes, such as bounds of the validate root descendants,
do not affect the layout of the validate root parent. This peculiarity
enables the

invalidate()

method to stop invalidating the
component hierarchy when the method encounters a validate root. However,
to preserve backward compatibility this new optimized behavior is
enabled only when the

java.awt.smartInvalidate

system property
value is set to

true

.

If a component hierarchy contains validate roots and the new optimized

invalidate()

behavior is enabled, the

validate()

method
must be invoked on the validate root of a previously invalidated
component to restore the validity of the hierarchy later. Otherwise,
calling the

validate()

method on the top-level container (such
as a

Frame

object) should be used to restore the validity of the
component hierarchy.

The

Window

class and the

Applet

class are the validate
roots in AWT. Swing introduces more validate roots.

Layout-related changes, such as bounds of the validate root descendants,
do not affect the layout of the validate root parent. This peculiarity
enables the

invalidate()

method to stop invalidating the
component hierarchy when the method encounters a validate root. However,
to preserve backward compatibility this new optimized behavior is
enabled only when the

java.awt.smartInvalidate

system property
value is set to

true

.

If a component hierarchy contains validate roots and the new optimized

invalidate()

behavior is enabled, the

validate()

method
must be invoked on the validate root of a previously invalidated
component to restore the validity of the hierarchy later. Otherwise,
calling the

validate()

method on the top-level container (such
as a

Frame

object) should be used to restore the validity of the
component hierarchy.

The

Window

class and the

Applet

class are the validate
roots in AWT. Swing introduces more validate roots.

If a component hierarchy contains validate roots and the new optimized

invalidate()

behavior is enabled, the

validate()

method
must be invoked on the validate root of a previously invalidated
component to restore the validity of the hierarchy later. Otherwise,
calling the

validate()

method on the top-level container (such
as a

Frame

object) should be used to restore the validity of the
component hierarchy.

The

Window

class and the

Applet

class are the validate
roots in AWT. Swing introduces more validate roots.

The

Window

class and the

Applet

class are the validate
roots in AWT. Swing introduces more validate roots.

invalidate

```java
public void invalidate()
```

Invalidates the container.

If the

LayoutManager

installed on this container is an instance
of the

LayoutManager2

interface, then
the

LayoutManager2.invalidateLayout(Container)

method is invoked
on it supplying this

Container

as the argument.

Afterwards this method marks this container invalid, and invalidates its
ancestors. See the

Component.invalidate()

method for more details.

**Overrides:** invalidate

in class

Component
**See Also:** validate()

,

layout()

,

LayoutManager2

---

#### invalidate

public void invalidate()

Invalidates the container.

If the

LayoutManager

installed on this container is an instance
of the

LayoutManager2

interface, then
the

LayoutManager2.invalidateLayout(Container)

method is invoked
on it supplying this

Container

as the argument.

Afterwards this method marks this container invalid, and invalidates its
ancestors. See the

Component.invalidate()

method for more details.

If the

LayoutManager

installed on this container is an instance
of the

LayoutManager2

interface, then
the

LayoutManager2.invalidateLayout(Container)

method is invoked
on it supplying this

Container

as the argument.

Afterwards this method marks this container invalid, and invalidates its
ancestors. See the

Component.invalidate()

method for more details.

Afterwards this method marks this container invalid, and invalidates its
ancestors. See the

Component.invalidate()

method for more details.

validate

```java
public void validate()
```

Validates this container and all of its subcomponents.

Validating a container means laying out its subcomponents.
Layout-related changes, such as setting the bounds of a component, or
adding a component to the container, invalidate the container
automatically. Note that the ancestors of the container may be
invalidated also (see

Component.invalidate()

for details.)
Therefore, to restore the validity of the hierarchy, the

validate()

method should be invoked on the top-most invalid
container of the hierarchy.

Validating the container may be a quite time-consuming operation. For
performance reasons a developer may postpone the validation of the
hierarchy till a set of layout-related operations completes, e.g. after
adding all the children to the container.

If this

Container

is not valid, this method invokes
the

validateTree

method and marks this

Container

as valid. Otherwise, no action is performed.

**Overrides:** validate

in class

Component
**See Also:** add(java.awt.Component)

,

invalidate()

,

isValidateRoot()

,

JComponent.revalidate()

,

validateTree()

---

#### validate

public void validate()

Validates this container and all of its subcomponents.

Validating a container means laying out its subcomponents.
Layout-related changes, such as setting the bounds of a component, or
adding a component to the container, invalidate the container
automatically. Note that the ancestors of the container may be
invalidated also (see

Component.invalidate()

for details.)
Therefore, to restore the validity of the hierarchy, the

validate()

method should be invoked on the top-most invalid
container of the hierarchy.

Validating the container may be a quite time-consuming operation. For
performance reasons a developer may postpone the validation of the
hierarchy till a set of layout-related operations completes, e.g. after
adding all the children to the container.

If this

Container

is not valid, this method invokes
the

validateTree

method and marks this

Container

as valid. Otherwise, no action is performed.

Validating a container means laying out its subcomponents.
Layout-related changes, such as setting the bounds of a component, or
adding a component to the container, invalidate the container
automatically. Note that the ancestors of the container may be
invalidated also (see

Component.invalidate()

for details.)
Therefore, to restore the validity of the hierarchy, the

validate()

method should be invoked on the top-most invalid
container of the hierarchy.

Validating the container may be a quite time-consuming operation. For
performance reasons a developer may postpone the validation of the
hierarchy till a set of layout-related operations completes, e.g. after
adding all the children to the container.

If this

Container

is not valid, this method invokes
the

validateTree

method and marks this

Container

as valid. Otherwise, no action is performed.

Validating the container may be a quite time-consuming operation. For
performance reasons a developer may postpone the validation of the
hierarchy till a set of layout-related operations completes, e.g. after
adding all the children to the container.

If this

Container

is not valid, this method invokes
the

validateTree

method and marks this

Container

as valid. Otherwise, no action is performed.

If this

Container

is not valid, this method invokes
the

validateTree

method and marks this

Container

as valid. Otherwise, no action is performed.

validateTree

```java
protected void validateTree()
```

Recursively descends the container tree and recomputes the
layout for any subtrees marked as needing it (those marked as
invalid). Synchronization should be provided by the method
that calls this one:

validate

.

**See Also:** doLayout()

,

validate()

---

#### validateTree

protected void validateTree()

Recursively descends the container tree and recomputes the
layout for any subtrees marked as needing it (those marked as
invalid). Synchronization should be provided by the method
that calls this one:

validate

.

setFont

```java
public void setFont​(
Font
f)
```

Sets the font of this container.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Overrides:** setFont

in class

Component
**Parameters:** f

- The font to become this container's font.
**Since:** 1.0
**See Also:** Component.getFont()

,

invalidate()

---

#### setFont

public void setFont​(

Font

f)

Sets the font of this container.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns the preferred size of this container. If the preferred size has
not been set explicitly by

Component.setPreferredSize(Dimension)

and this

Container

has a

non-null

LayoutManager

,
then

LayoutManager.preferredLayoutSize(Container)

is used to calculate the preferred size.

Note: some implementations may cache the value returned from the

LayoutManager

. Implementations that cache need not invoke

preferredLayoutSize

on the

LayoutManager

every time
this method is invoked, rather the

LayoutManager

will only
be queried after the

Container

becomes invalid.

**Overrides:** getPreferredSize

in class

Component
**Returns:** an instance of

Dimension

that represents
the preferred size of this container.
**See Also:** getMinimumSize()

,

getMaximumSize()

,

getLayout()

,

LayoutManager.preferredLayoutSize(Container)

,

Component.getPreferredSize()

---

#### getPreferredSize

public

Dimension

getPreferredSize()

Returns the preferred size of this container. If the preferred size has
not been set explicitly by

Component.setPreferredSize(Dimension)

and this

Container

has a

non-null

LayoutManager

,
then

LayoutManager.preferredLayoutSize(Container)

is used to calculate the preferred size.

Note: some implementations may cache the value returned from the

LayoutManager

. Implementations that cache need not invoke

preferredLayoutSize

on the

LayoutManager

every time
this method is invoked, rather the

LayoutManager

will only
be queried after the

Container

becomes invalid.

Note: some implementations may cache the value returned from the

LayoutManager

. Implementations that cache need not invoke

preferredLayoutSize

on the

LayoutManager

every time
this method is invoked, rather the

LayoutManager

will only
be queried after the

Container

becomes invalid.

preferredSize

```java
@Deprecated

public
Dimension
preferredSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Description copied from class:

Component

Returns the component's preferred size.

**Overrides:** preferredSize

in class

Component
**Returns:** the component's preferred size

---

#### preferredSize

@Deprecated

public

Dimension

preferredSize()

Description copied from class:

Component

Returns the component's preferred size.

getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Returns the minimum size of this container. If the minimum size has
not been set explicitly by

Component.setMinimumSize(Dimension)

and this

Container

has a

non-null

LayoutManager

,
then

LayoutManager.minimumLayoutSize(Container)

is used to calculate the minimum size.

Note: some implementations may cache the value returned from the

LayoutManager

. Implementations that cache need not invoke

minimumLayoutSize

on the

LayoutManager

every time
this method is invoked, rather the

LayoutManager

will only
be queried after the

Container

becomes invalid.

**Overrides:** getMinimumSize

in class

Component
**Returns:** an instance of

Dimension

that represents
the minimum size of this container.
**Since:** 1.1
**See Also:** getPreferredSize()

,

getMaximumSize()

,

getLayout()

,

LayoutManager.minimumLayoutSize(Container)

,

Component.getMinimumSize()

---

#### getMinimumSize

public

Dimension

getMinimumSize()

Returns the minimum size of this container. If the minimum size has
not been set explicitly by

Component.setMinimumSize(Dimension)

and this

Container

has a

non-null

LayoutManager

,
then

LayoutManager.minimumLayoutSize(Container)

is used to calculate the minimum size.

Note: some implementations may cache the value returned from the

LayoutManager

. Implementations that cache need not invoke

minimumLayoutSize

on the

LayoutManager

every time
this method is invoked, rather the

LayoutManager

will only
be queried after the

Container

becomes invalid.

Note: some implementations may cache the value returned from the

LayoutManager

. Implementations that cache need not invoke

minimumLayoutSize

on the

LayoutManager

every time
this method is invoked, rather the

LayoutManager

will only
be queried after the

Container

becomes invalid.

minimumSize

```java
@Deprecated

public
Dimension
minimumSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Description copied from class:

Component

Returns the minimum size of this component.

**Overrides:** minimumSize

in class

Component
**Returns:** the minimum size of this component

---

#### minimumSize

@Deprecated

public

Dimension

minimumSize()

Description copied from class:

Component

Returns the minimum size of this component.

getMaximumSize

```java
public
Dimension
getMaximumSize()
```

Returns the maximum size of this container. If the maximum size has
not been set explicitly by

Component.setMaximumSize(Dimension)

and the

LayoutManager

installed on this

Container

is an instance of

LayoutManager2

, then

LayoutManager2.maximumLayoutSize(Container)

is used to calculate the maximum size.

Note: some implementations may cache the value returned from the

LayoutManager2

. Implementations that cache need not invoke

maximumLayoutSize

on the

LayoutManager2

every time
this method is invoked, rather the

LayoutManager2

will only
be queried after the

Container

becomes invalid.

**Overrides:** getMaximumSize

in class

Component
**Returns:** an instance of

Dimension

that represents
the maximum size of this container.
**See Also:** getPreferredSize()

,

getMinimumSize()

,

getLayout()

,

LayoutManager2.maximumLayoutSize(Container)

,

Component.getMaximumSize()

---

#### getMaximumSize

public

Dimension

getMaximumSize()

Returns the maximum size of this container. If the maximum size has
not been set explicitly by

Component.setMaximumSize(Dimension)

and the

LayoutManager

installed on this

Container

is an instance of

LayoutManager2

, then

LayoutManager2.maximumLayoutSize(Container)

is used to calculate the maximum size.

Note: some implementations may cache the value returned from the

LayoutManager2

. Implementations that cache need not invoke

maximumLayoutSize

on the

LayoutManager2

every time
this method is invoked, rather the

LayoutManager2

will only
be queried after the

Container

becomes invalid.

Note: some implementations may cache the value returned from the

LayoutManager2

. Implementations that cache need not invoke

maximumLayoutSize

on the

LayoutManager2

every time
this method is invoked, rather the

LayoutManager2

will only
be queried after the

Container

becomes invalid.

getAlignmentX

```java
public float getAlignmentX()
```

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Overrides:** getAlignmentX

in class

Component
**Returns:** the horizontal alignment of this component

---

#### getAlignmentX

public float getAlignmentX()

Returns the alignment along the x axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

getAlignmentY

```java
public float getAlignmentY()
```

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

**Overrides:** getAlignmentY

in class

Component
**Returns:** the vertical alignment of this component

---

#### getAlignmentY

public float getAlignmentY()

Returns the alignment along the y axis. This specifies how
the component would like to be aligned relative to other
components. The value should be a number between 0 and 1
where 0 represents alignment along the origin, 1 is aligned
the furthest away from the origin, 0.5 is centered, etc.

paint

```java
public void paint​(
Graphics
g)
```

Paints the container. This forwards the paint to any lightweight
components that are children of this container. If this method is
reimplemented, super.paint(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, paint() will not be
forwarded to that child.

**Overrides:** paint

in class

Component
**Parameters:** g

- the specified Graphics window
**See Also:** Component.update(Graphics)

---

#### paint

public void paint​(

Graphics

g)

Paints the container. This forwards the paint to any lightweight
components that are children of this container. If this method is
reimplemented, super.paint(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, paint() will not be
forwarded to that child.

update

```java
public void update​(
Graphics
g)
```

Updates the container. This forwards the update to any lightweight
components that are children of this container. If this method is
reimplemented, super.update(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, update() will not be
forwarded to that child.

**Overrides:** update

in class

Component
**Parameters:** g

- the specified Graphics window
**See Also:** Component.update(Graphics)

---

#### update

public void update​(

Graphics

g)

Updates the container. This forwards the update to any lightweight
components that are children of this container. If this method is
reimplemented, super.update(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, update() will not be
forwarded to that child.

print

```java
public void print​(
Graphics
g)
```

Prints the container. This forwards the print to any lightweight
components that are children of this container. If this method is
reimplemented, super.print(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, print() will not be
forwarded to that child.

**Overrides:** print

in class

Component
**Parameters:** g

- the specified Graphics window
**See Also:** Component.update(Graphics)

---

#### print

public void print​(

Graphics

g)

Prints the container. This forwards the print to any lightweight
components that are children of this container. If this method is
reimplemented, super.print(g) should be called so that lightweight
components are properly rendered. If a child component is entirely
clipped by the current clipping setting in g, print() will not be
forwarded to that child.

paintComponents

```java
public void paintComponents​(
Graphics
g)
```

Paints each of the components in this container.

**Parameters:** g

- the graphics context.
**See Also:** Component.paint(java.awt.Graphics)

,

Component.paintAll(java.awt.Graphics)

---

#### paintComponents

public void paintComponents​(

Graphics

g)

Paints each of the components in this container.

printComponents

```java
public void printComponents​(
Graphics
g)
```

Prints each of the components in this container.

**Parameters:** g

- the graphics context.
**See Also:** Component.print(java.awt.Graphics)

,

Component.printAll(java.awt.Graphics)

---

#### printComponents

public void printComponents​(

Graphics

g)

Prints each of the components in this container.

addContainerListener

```java
public void addContainerListener​(
ContainerListener
l)
```

Adds the specified container listener to receive container events
from this container.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the container listener
**See Also:** removeContainerListener(java.awt.event.ContainerListener)

,

getContainerListeners()

---

#### addContainerListener

public void addContainerListener​(

ContainerListener

l)

Adds the specified container listener to receive container events
from this container.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeContainerListener

```java
public void removeContainerListener​(
ContainerListener
l)
```

Removes the specified container listener so it no longer receives
container events from this container.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the container listener
**See Also:** addContainerListener(java.awt.event.ContainerListener)

,

getContainerListeners()

---

#### removeContainerListener

public void removeContainerListener​(

ContainerListener

l)

Removes the specified container listener so it no longer receives
container events from this container.
If l is null, no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getContainerListeners

```java
public
ContainerListener
[] getContainerListeners()
```

Returns an array of all the container listeners
registered on this container.

**Returns:** all of this container's

ContainerListener

s
or an empty array if no container
listeners are currently registered
**Since:** 1.4
**See Also:** addContainerListener(java.awt.event.ContainerListener)

,

removeContainerListener(java.awt.event.ContainerListener)

---

#### getContainerListeners

public

ContainerListener

[] getContainerListeners()

Returns an array of all the container listeners
registered on this container.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Container

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Container c

for its container listeners with the following code:

```java
ContainerListener[] cls = (ContainerListener[])(c.getListeners(ContainerListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Component
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this container,
or an empty array if no such listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Throws:** NullPointerException

- if

listenerType

is

null
**Since:** 1.3
**See Also:** getContainerListeners()

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

Container

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Container c

for its container listeners with the following code:

```java
ContainerListener[] cls = (ContainerListener[])(c.getListeners(ContainerListener.class));
```

If no such listeners exist, this method returns an empty array.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

Container c

for its container listeners with the following code:

```java
ContainerListener[] cls = (ContainerListener[])(c.getListeners(ContainerListener.class));
```

If no such listeners exist, this method returns an empty array.

ContainerListener[] cls = (ContainerListener[])(c.getListeners(ContainerListener.class));

processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this container. If the event is a

ContainerEvent

, it invokes the

processContainerEvent

method, else it invokes
its superclass's

processEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Component
**Parameters:** e

- the event
**See Also:** Component.processComponentEvent(java.awt.event.ComponentEvent)

,

Component.processFocusEvent(java.awt.event.FocusEvent)

,

Component.processKeyEvent(java.awt.event.KeyEvent)

,

Component.processMouseEvent(java.awt.event.MouseEvent)

,

Component.processMouseMotionEvent(java.awt.event.MouseEvent)

,

Component.processInputMethodEvent(java.awt.event.InputMethodEvent)

,

Component.processHierarchyEvent(java.awt.event.HierarchyEvent)

,

Component.processMouseWheelEvent(java.awt.event.MouseWheelEvent)

---

#### processEvent

protected void processEvent​(

AWTEvent

e)

Processes events on this container. If the event is a

ContainerEvent

, it invokes the

processContainerEvent

method, else it invokes
its superclass's

processEvent

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processContainerEvent

```java
protected void processContainerEvent​(
ContainerEvent
e)
```

Processes container events occurring on this container by
dispatching them to any registered ContainerListener objects.
NOTE: This method will not be called unless container events
are enabled for this component; this happens when one of the
following occurs:

- A ContainerListener object is registered via

addContainerListener

Container events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the container event
**See Also:** Component.enableEvents(long)

---

#### processContainerEvent

protected void processContainerEvent​(

ContainerEvent

e)

Processes container events occurring on this container by
dispatching them to any registered ContainerListener objects.
NOTE: This method will not be called unless container events
are enabled for this component; this happens when one of the
following occurs:

- A ContainerListener object is registered via

addContainerListener

Container events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

A ContainerListener object is registered via

addContainerListener

Container events are enabled via

enableEvents

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

deliverEvent

```java
@Deprecated

public void deliverEvent​(
Event
e)
```

Deprecated.

As of JDK version 1.1,
replaced by

dispatchEvent(AWTEvent e)

**Overrides:** deliverEvent

in class

Component
**Parameters:** e

- the event to deliver

---

#### deliverEvent

@Deprecated

public void deliverEvent​(

Event

e)

getComponentAt

```java
public
Component
getComponentAt​(int x,
int y)
```

Locates the component that contains the x,y position. The
top-most child component is returned in the case where there
is overlap in the components. This is determined by finding
the component closest to the index 0 that claims to contain
the given point via Component.contains(), except that Components
which have native peers take precedence over those which do not
(i.e., lightweight Components).

**Overrides:** getComponentAt

in class

Component
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Returns:** null if the component does not contain the position.
If there is no child component at the requested point and the
point is within the bounds of the container the container itself
is returned; otherwise the top-most child is returned.
**Since:** 1.1
**See Also:** Component.contains(int, int)

---

#### getComponentAt

public

Component

getComponentAt​(int x,
int y)

Locates the component that contains the x,y position. The
top-most child component is returned in the case where there
is overlap in the components. This is determined by finding
the component closest to the index 0 that claims to contain
the given point via Component.contains(), except that Components
which have native peers take precedence over those which do not
(i.e., lightweight Components).

locate

```java
@Deprecated

public
Component
locate​(int x,
int y)
```

Deprecated.

As of JDK version 1.1,
replaced by

getComponentAt(int, int)

.

Description copied from class:

Component

Returns the component occupying the position specified (this component,
or immediate child component, or null if neither
of the first two occupies the location).

**Overrides:** locate

in class

Component
**Parameters:** x

- the

x

coordinate to search for components at
**Parameters:** y

- the

y

coordinate to search for components at
**Returns:** the component at the specified location or

null

---

#### locate

@Deprecated

public

Component

locate​(int x,
int y)

Description copied from class:

Component

Returns the component occupying the position specified (this component,
or immediate child component, or null if neither
of the first two occupies the location).

getComponentAt

```java
public
Component
getComponentAt​(
Point
p)
```

Gets the component that contains the specified point.

**Overrides:** getComponentAt

in class

Component
**Parameters:** p

- the point.
**Returns:** returns the component that contains the point,
or

null

if the component does
not contain the point.
**Since:** 1.1
**See Also:** Component.contains(int, int)

---

#### getComponentAt

public

Component

getComponentAt​(

Point

p)

Gets the component that contains the specified point.

getMousePosition

```java
public
Point
getMousePosition​(boolean allowChildren)
throws
HeadlessException
```

Returns the position of the mouse pointer in this

Container

's
coordinate space if the

Container

is under the mouse pointer,
otherwise returns

null

.
This method is similar to

Component.getMousePosition()

with the exception
that it can take the

Container

's children into account.
If

allowChildren

is

false

, this method will return
a non-null value only if the mouse pointer is above the

Container

directly, not above the part obscured by children.
If

allowChildren

is

true

, this method returns
a non-null value if the mouse pointer is above

Container

or any
of its descendants.

**Parameters:** allowChildren

- true if children should be taken into account
**Returns:** mouse coordinates relative to this

Component

, or null
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless() returns true
**Since:** 1.5
**See Also:** Component.getMousePosition()

---

#### getMousePosition

public

Point

getMousePosition​(boolean allowChildren)
throws

HeadlessException

Returns the position of the mouse pointer in this

Container

's
coordinate space if the

Container

is under the mouse pointer,
otherwise returns

null

.
This method is similar to

Component.getMousePosition()

with the exception
that it can take the

Container

's children into account.
If

allowChildren

is

false

, this method will return
a non-null value only if the mouse pointer is above the

Container

directly, not above the part obscured by children.
If

allowChildren

is

true

, this method returns
a non-null value if the mouse pointer is above

Container

or any
of its descendants.

findComponentAt

```java
public
Component
findComponentAt​(int x,
int y)
```

Locates the visible child component that contains the specified
position. The top-most child component is returned in the case
where there is overlap in the components. If the containing child
component is a Container, this method will continue searching for
the deepest nested child component. Components which are not
visible are ignored during the search.

The findComponentAt method is different from getComponentAt in
that getComponentAt only searches the Container's immediate
children; if the containing component is a Container,
findComponentAt will search that child to find a nested component.

**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Returns:** null if the component does not contain the position.
If there is no child component at the requested point and the
point is within the bounds of the container the container itself
is returned.
**Since:** 1.2
**See Also:** Component.contains(int, int)

,

getComponentAt(int, int)

---

#### findComponentAt

public

Component

findComponentAt​(int x,
int y)

Locates the visible child component that contains the specified
position. The top-most child component is returned in the case
where there is overlap in the components. If the containing child
component is a Container, this method will continue searching for
the deepest nested child component. Components which are not
visible are ignored during the search.

The findComponentAt method is different from getComponentAt in
that getComponentAt only searches the Container's immediate
children; if the containing component is a Container,
findComponentAt will search that child to find a nested component.

The findComponentAt method is different from getComponentAt in
that getComponentAt only searches the Container's immediate
children; if the containing component is a Container,
findComponentAt will search that child to find a nested component.

findComponentAt

```java
public
Component
findComponentAt​(
Point
p)
```

Locates the visible child component that contains the specified
point. The top-most child component is returned in the case
where there is overlap in the components. If the containing child
component is a Container, this method will continue searching for
the deepest nested child component. Components which are not
visible are ignored during the search.

The findComponentAt method is different from getComponentAt in
that getComponentAt only searches the Container's immediate
children; if the containing component is a Container,
findComponentAt will search that child to find a nested component.

**Parameters:** p

- the point.
**Returns:** null if the component does not contain the position.
If there is no child component at the requested point and the
point is within the bounds of the container the container itself
is returned.
**Throws:** NullPointerException

- if

p

is

null
**Since:** 1.2
**See Also:** Component.contains(int, int)

,

getComponentAt(int, int)

---

#### findComponentAt

public

Component

findComponentAt​(

Point

p)

Locates the visible child component that contains the specified
point. The top-most child component is returned in the case
where there is overlap in the components. If the containing child
component is a Container, this method will continue searching for
the deepest nested child component. Components which are not
visible are ignored during the search.

The findComponentAt method is different from getComponentAt in
that getComponentAt only searches the Container's immediate
children; if the containing component is a Container,
findComponentAt will search that child to find a nested component.

The findComponentAt method is different from getComponentAt in
that getComponentAt only searches the Container's immediate
children; if the containing component is a Container,
findComponentAt will search that child to find a nested component.

addNotify

```java
public void addNotify()
```

Makes this Container displayable by connecting it to
a native screen resource. Making a container displayable will
cause all of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

**Overrides:** addNotify

in class

Component
**See Also:** Component.isDisplayable()

,

removeNotify()

---

#### addNotify

public void addNotify()

Makes this Container displayable by connecting it to
a native screen resource. Making a container displayable will
cause all of its children to be made displayable.
This method is called internally by the toolkit and should
not be called directly by programs.

removeNotify

```java
public void removeNotify()
```

Makes this Container undisplayable by removing its connection
to its native screen resource. Making a container undisplayable
will cause all of its children to be made undisplayable.
This method is called by the toolkit internally and should
not be called directly by programs.

**Overrides:** removeNotify

in class

Component
**See Also:** Component.isDisplayable()

,

addNotify()

---

#### removeNotify

public void removeNotify()

Makes this Container undisplayable by removing its connection
to its native screen resource. Making a container undisplayable
will cause all of its children to be made undisplayable.
This method is called by the toolkit internally and should
not be called directly by programs.

isAncestorOf

```java
public boolean isAncestorOf​(
Component
c)
```

Checks if the component is contained in the component hierarchy of
this container.

**Parameters:** c

- the component
**Returns:** true

if it is an ancestor;

false

otherwise.
**Since:** 1.1

---

#### isAncestorOf

public boolean isAncestorOf​(

Component

c)

Checks if the component is contained in the component hierarchy of
this container.

paramString

```java
protected
String
paramString()
```

Returns a string representing the state of this

Container

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

**Overrides:** paramString

in class

Component
**Returns:** the parameter string of this container

---

#### paramString

protected

String

paramString()

Returns a string representing the state of this

Container

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not be

null

.

list

```java
public void list​(
PrintStream
out,
int indent)
```

Prints a listing of this container to the specified output
stream. The listing starts at the specified indentation.

The immediate children of the container are printed with
an indentation of

indent+1

. The children
of those children are printed at

indent+2

and so on.

**Overrides:** list

in class

Component
**Parameters:** out

- a print stream
**Parameters:** indent

- the number of spaces to indent
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.0
**See Also:** Component.list(java.io.PrintStream, int)

---

#### list

public void list​(

PrintStream

out,
int indent)

Prints a listing of this container to the specified output
stream. The listing starts at the specified indentation.

The immediate children of the container are printed with
an indentation of

indent+1

. The children
of those children are printed at

indent+2

and so on.

The immediate children of the container are printed with
an indentation of

indent+1

. The children
of those children are printed at

indent+2

and so on.

list

```java
public void list​(
PrintWriter
out,
int indent)
```

Prints out a list, starting at the specified indentation,
to the specified print writer.

The immediate children of the container are printed with
an indentation of

indent+1

. The children
of those children are printed at

indent+2

and so on.

**Overrides:** list

in class

Component
**Parameters:** out

- a print writer
**Parameters:** indent

- the number of spaces to indent
**Throws:** NullPointerException

- if

out

is

null
**Since:** 1.1
**See Also:** Component.list(java.io.PrintWriter, int)

---

#### list

public void list​(

PrintWriter

out,
int indent)

Prints out a list, starting at the specified indentation,
to the specified print writer.

The immediate children of the container are printed with
an indentation of

indent+1

. The children
of those children are printed at

indent+2

and so on.

The immediate children of the container are printed with
an indentation of

indent+1

. The children
of those children are printed at

indent+2

and so on.

setFocusTraversalKeys

```java
public void setFocusTraversalKeys​(int id,

Set
<? extends
AWTKeyStroke
> keystrokes)
```

Sets the focus traversal keys for a given traversal operation for this
Container.

The default values for a Container's focus traversal keys are
implementation-dependent. Sun recommends that all implementations for a
particular native platform use the same default values. The
recommendations for Windows and Unix are listed below. These
recommendations are used in the Sun AWT implementations.

Recommended default values for a Container's focus traversal
keys

Identifier

Meaning

Default

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

Normal forward keyboard traversal

TAB on KEY_PRESSED, CTRL-TAB on KEY_PRESSED

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

Normal reverse keyboard traversal

SHIFT-TAB on KEY_PRESSED, CTRL-SHIFT-TAB on KEY_PRESSED

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

Go up one focus traversal cycle

none

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

Go down one focus traversal cycle

none

To disable a traversal key, use an empty Set; Collections.EMPTY_SET is
recommended.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Container. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Container inherits the
Set from its parent. If all ancestors of this Container have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

**Overrides:** setFocusTraversalKeys

in class

Component
**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Parameters:** keystrokes

- the Set of AWTKeyStroke for the specified operation
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS, or if keystrokes
contains null, or if any keystroke represents a KEY_TYPED event,
or if any keystroke already maps to another focus traversal
operation for this Container
**Since:** 1.4
**See Also:** getFocusTraversalKeys(int)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

,

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

---

#### setFocusTraversalKeys

public void setFocusTraversalKeys​(int id,

Set

<? extends

AWTKeyStroke

> keystrokes)

Sets the focus traversal keys for a given traversal operation for this
Container.

The default values for a Container's focus traversal keys are
implementation-dependent. Sun recommends that all implementations for a
particular native platform use the same default values. The
recommendations for Windows and Unix are listed below. These
recommendations are used in the Sun AWT implementations.

Recommended default values for a Container's focus traversal
keys

Identifier

Meaning

Default

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

Normal forward keyboard traversal

TAB on KEY_PRESSED, CTRL-TAB on KEY_PRESSED

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

Normal reverse keyboard traversal

SHIFT-TAB on KEY_PRESSED, CTRL-SHIFT-TAB on KEY_PRESSED

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

Go up one focus traversal cycle

none

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

Go down one focus traversal cycle

none

To disable a traversal key, use an empty Set; Collections.EMPTY_SET is
recommended.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Container. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Container inherits the
Set from its parent. If all ancestors of this Container have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

The default values for a Container's focus traversal keys are
implementation-dependent. Sun recommends that all implementations for a
particular native platform use the same default values. The
recommendations for Windows and Unix are listed below. These
recommendations are used in the Sun AWT implementations.

Recommended default values for a Container's focus traversal
keys

Identifier

Meaning

Default

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

Normal forward keyboard traversal

TAB on KEY_PRESSED, CTRL-TAB on KEY_PRESSED

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

Normal reverse keyboard traversal

SHIFT-TAB on KEY_PRESSED, CTRL-SHIFT-TAB on KEY_PRESSED

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

Go up one focus traversal cycle

none

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

Go down one focus traversal cycle

none

To disable a traversal key, use an empty Set; Collections.EMPTY_SET is
recommended.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Container. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Container inherits the
Set from its parent. If all ancestors of this Container have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

Using the AWTKeyStroke API, client code can specify on which of two
specific KeyEvents, KEY_PRESSED or KEY_RELEASED, the focus traversal
operation will occur. Regardless of which KeyEvent is specified,
however, all KeyEvents related to the focus traversal key, including the
associated KEY_TYPED event, will be consumed, and will not be dispatched
to any Container. It is a runtime error to specify a KEY_TYPED event as
mapping to a focus traversal operation, or to map the same event to
multiple default focus traversal operations.

If a value of null is specified for the Set, this Container inherits the
Set from its parent. If all ancestors of this Container have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

If a value of null is specified for the Set, this Container inherits the
Set from its parent. If all ancestors of this Container have null
specified for the Set, then the current KeyboardFocusManager's default
Set is used.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

This method may throw a

ClassCastException

if any

Object

in

keystrokes

is not an

AWTKeyStroke

.

getFocusTraversalKeys

```java
public
Set
<
AWTKeyStroke
> getFocusTraversalKeys​(int id)
```

Returns the Set of focus traversal keys for a given traversal operation
for this Container. (See

setFocusTraversalKeys

for a full description of each key.)

If a Set of traversal keys has not been explicitly defined for this
Container, then this Container's parent's Set is returned. If no Set
has been explicitly defined for any of this Container's ancestors, then
the current KeyboardFocusManager's default Set is returned.

**Overrides:** getFocusTraversalKeys

in class

Component
**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Returns:** the Set of AWTKeyStrokes for the specified operation. The Set
will be unmodifiable, and may be empty. null will never be
returned.
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4
**See Also:** setFocusTraversalKeys(int, java.util.Set<? extends java.awt.AWTKeyStroke>)

,

KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS

,

KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS

,

KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS

---

#### getFocusTraversalKeys

public

Set

<

AWTKeyStroke

> getFocusTraversalKeys​(int id)

Returns the Set of focus traversal keys for a given traversal operation
for this Container. (See

setFocusTraversalKeys

for a full description of each key.)

If a Set of traversal keys has not been explicitly defined for this
Container, then this Container's parent's Set is returned. If no Set
has been explicitly defined for any of this Container's ancestors, then
the current KeyboardFocusManager's default Set is returned.

If a Set of traversal keys has not been explicitly defined for this
Container, then this Container's parent's Set is returned. If no Set
has been explicitly defined for any of this Container's ancestors, then
the current KeyboardFocusManager's default Set is returned.

areFocusTraversalKeysSet

```java
public boolean areFocusTraversalKeysSet​(int id)
```

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Container. If
this method returns

false

, this Container is inheriting the
Set from an ancestor, or from the current KeyboardFocusManager.

**Overrides:** areFocusTraversalKeysSet

in class

Component
**Parameters:** id

- one of KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Returns:** true

if the Set of focus traversal keys for the
given focus traversal operation has been explicitly defined for
this Component;

false

otherwise.
**Throws:** IllegalArgumentException

- if id is not one of
KeyboardFocusManager.FORWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.BACKWARD_TRAVERSAL_KEYS,
KeyboardFocusManager.UP_CYCLE_TRAVERSAL_KEYS, or
KeyboardFocusManager.DOWN_CYCLE_TRAVERSAL_KEYS
**Since:** 1.4

---

#### areFocusTraversalKeysSet

public boolean areFocusTraversalKeysSet​(int id)

Returns whether the Set of focus traversal keys for the given focus
traversal operation has been explicitly defined for this Container. If
this method returns

false

, this Container is inheriting the
Set from an ancestor, or from the current KeyboardFocusManager.

isFocusCycleRoot

```java
public boolean isFocusCycleRoot​(
Container
container)
```

Returns whether the specified Container is the focus cycle root of this
Container's focus traversal cycle. Each focus traversal cycle has only
a single focus cycle root and each Container which is not a focus cycle
root belongs to only a single focus traversal cycle. Containers which
are focus cycle roots belong to two cycles: one rooted at the Container
itself, and one rooted at the Container's nearest focus-cycle-root
ancestor. This method will return

true

for both such
Containers in this case.

**Overrides:** isFocusCycleRoot

in class

Component
**Parameters:** container

- the Container to be tested
**Returns:** true

if the specified Container is a focus-cycle-
root of this Container;

false

otherwise
**Since:** 1.4
**See Also:** isFocusCycleRoot()

---

#### isFocusCycleRoot

public boolean isFocusCycleRoot​(

Container

container)

Returns whether the specified Container is the focus cycle root of this
Container's focus traversal cycle. Each focus traversal cycle has only
a single focus cycle root and each Container which is not a focus cycle
root belongs to only a single focus traversal cycle. Containers which
are focus cycle roots belong to two cycles: one rooted at the Container
itself, and one rooted at the Container's nearest focus-cycle-root
ancestor. This method will return

true

for both such
Containers in this case.

setFocusTraversalPolicy

```java
public void setFocusTraversalPolicy​(
FocusTraversalPolicy
policy)
```

Sets the focus traversal policy that will manage keyboard traversal of
this Container's children, if this Container is a focus cycle root. If
the argument is null, this Container inherits its policy from its focus-
cycle-root ancestor. If the argument is non-null, this policy will be
inherited by all focus-cycle-root children that have no keyboard-
traversal policy of their own (as will, recursively, their focus-cycle-
root children).

If this Container is not a focus cycle root, the policy will be
remembered, but will not be used or inherited by this or any other
Containers until this Container is made a focus cycle root.

**Parameters:** policy

- the new focus traversal policy for this Container
**Since:** 1.4
**See Also:** getFocusTraversalPolicy()

,

setFocusCycleRoot(boolean)

,

isFocusCycleRoot(java.awt.Container)

---

#### setFocusTraversalPolicy

public void setFocusTraversalPolicy​(

FocusTraversalPolicy

policy)

Sets the focus traversal policy that will manage keyboard traversal of
this Container's children, if this Container is a focus cycle root. If
the argument is null, this Container inherits its policy from its focus-
cycle-root ancestor. If the argument is non-null, this policy will be
inherited by all focus-cycle-root children that have no keyboard-
traversal policy of their own (as will, recursively, their focus-cycle-
root children).

If this Container is not a focus cycle root, the policy will be
remembered, but will not be used or inherited by this or any other
Containers until this Container is made a focus cycle root.

If this Container is not a focus cycle root, the policy will be
remembered, but will not be used or inherited by this or any other
Containers until this Container is made a focus cycle root.

getFocusTraversalPolicy

```java
public
FocusTraversalPolicy
getFocusTraversalPolicy()
```

Returns the focus traversal policy that will manage keyboard traversal
of this Container's children, or null if this Container is not a focus
cycle root. If no traversal policy has been explicitly set for this
Container, then this Container's focus-cycle-root ancestor's policy is
returned.

**Returns:** this Container's focus traversal policy, or null if this
Container is not a focus cycle root.
**Since:** 1.4
**See Also:** setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

setFocusCycleRoot(boolean)

,

isFocusCycleRoot(java.awt.Container)

---

#### getFocusTraversalPolicy

public

FocusTraversalPolicy

getFocusTraversalPolicy()

Returns the focus traversal policy that will manage keyboard traversal
of this Container's children, or null if this Container is not a focus
cycle root. If no traversal policy has been explicitly set for this
Container, then this Container's focus-cycle-root ancestor's policy is
returned.

isFocusTraversalPolicySet

```java
public boolean isFocusTraversalPolicySet()
```

Returns whether the focus traversal policy has been explicitly set for
this Container. If this method returns

false

, this
Container will inherit its focus traversal policy from an ancestor.

**Returns:** true

if the focus traversal policy has been
explicitly set for this Container;

false

otherwise.
**Since:** 1.4

---

#### isFocusTraversalPolicySet

public boolean isFocusTraversalPolicySet()

Returns whether the focus traversal policy has been explicitly set for
this Container. If this method returns

false

, this
Container will inherit its focus traversal policy from an ancestor.

setFocusCycleRoot

```java
public void setFocusCycleRoot​(boolean focusCycleRoot)
```

Sets whether this Container is the root of a focus traversal cycle. Once
focus enters a traversal cycle, typically it cannot leave it via focus
traversal unless one of the up- or down-cycle keys is pressed. Normal
traversal is limited to this Container, and all of this Container's
descendants that are not descendants of inferior focus cycle roots. Note
that a FocusTraversalPolicy may bend these restrictions, however. For
example, ContainerOrderFocusTraversalPolicy supports implicit down-cycle
traversal.

The alternative way to specify the traversal order of this Container's
children is to make this Container a

focus traversal policy provider

.

**Parameters:** focusCycleRoot

- indicates whether this Container is the root of a
focus traversal cycle
**Since:** 1.4
**See Also:** isFocusCycleRoot()

,

setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

ContainerOrderFocusTraversalPolicy

,

setFocusTraversalPolicyProvider(boolean)

---

#### setFocusCycleRoot

public void setFocusCycleRoot​(boolean focusCycleRoot)

Sets whether this Container is the root of a focus traversal cycle. Once
focus enters a traversal cycle, typically it cannot leave it via focus
traversal unless one of the up- or down-cycle keys is pressed. Normal
traversal is limited to this Container, and all of this Container's
descendants that are not descendants of inferior focus cycle roots. Note
that a FocusTraversalPolicy may bend these restrictions, however. For
example, ContainerOrderFocusTraversalPolicy supports implicit down-cycle
traversal.

The alternative way to specify the traversal order of this Container's
children is to make this Container a

focus traversal policy provider

.

The alternative way to specify the traversal order of this Container's
children is to make this Container a

focus traversal policy provider

.

isFocusCycleRoot

```java
public boolean isFocusCycleRoot()
```

Returns whether this Container is the root of a focus traversal cycle.
Once focus enters a traversal cycle, typically it cannot leave it via
focus traversal unless one of the up- or down-cycle keys is pressed.
Normal traversal is limited to this Container, and all of this
Container's descendants that are not descendants of inferior focus
cycle roots. Note that a FocusTraversalPolicy may bend these
restrictions, however. For example, ContainerOrderFocusTraversalPolicy
supports implicit down-cycle traversal.

**Returns:** whether this Container is the root of a focus traversal cycle
**Since:** 1.4
**See Also:** setFocusCycleRoot(boolean)

,

setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

ContainerOrderFocusTraversalPolicy

---

#### isFocusCycleRoot

public boolean isFocusCycleRoot()

Returns whether this Container is the root of a focus traversal cycle.
Once focus enters a traversal cycle, typically it cannot leave it via
focus traversal unless one of the up- or down-cycle keys is pressed.
Normal traversal is limited to this Container, and all of this
Container's descendants that are not descendants of inferior focus
cycle roots. Note that a FocusTraversalPolicy may bend these
restrictions, however. For example, ContainerOrderFocusTraversalPolicy
supports implicit down-cycle traversal.

setFocusTraversalPolicyProvider

```java
public final void setFocusTraversalPolicyProvider​(boolean provider)
```

Sets whether this container will be used to provide focus
traversal policy. Container with this property as

true

will be used to acquire focus traversal policy
instead of closest focus cycle root ancestor.

**Parameters:** provider

- indicates whether this container will be used to
provide focus traversal policy
**Since:** 1.5
**See Also:** setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

isFocusTraversalPolicyProvider()

---

#### setFocusTraversalPolicyProvider

public final void setFocusTraversalPolicyProvider​(boolean provider)

Sets whether this container will be used to provide focus
traversal policy. Container with this property as

true

will be used to acquire focus traversal policy
instead of closest focus cycle root ancestor.

isFocusTraversalPolicyProvider

```java
public final boolean isFocusTraversalPolicyProvider()
```

Returns whether this container provides focus traversal
policy. If this property is set to

true

then when
keyboard focus manager searches container hierarchy for focus
traversal policy and encounters this container before any other
container with this property as true or focus cycle roots then
its focus traversal policy will be used instead of focus cycle
root's policy.

**Returns:** true

if this container provides focus traversal
policy,

false

otherwise
**Since:** 1.5
**See Also:** setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)

,

getFocusTraversalPolicy()

,

setFocusCycleRoot(boolean)

,

setFocusTraversalPolicyProvider(boolean)

---

#### isFocusTraversalPolicyProvider

public final boolean isFocusTraversalPolicyProvider()

Returns whether this container provides focus traversal
policy. If this property is set to

true

then when
keyboard focus manager searches container hierarchy for focus
traversal policy and encounters this container before any other
container with this property as true or focus cycle roots then
its focus traversal policy will be used instead of focus cycle
root's policy.

transferFocusDownCycle

```java
public void transferFocusDownCycle()
```

Transfers the focus down one focus traversal cycle. If this Container is
a focus cycle root, then the focus owner is set to this Container's
default Component to focus, and the current focus cycle root is set to
this Container. If this Container is not a focus cycle root, then no
focus traversal operation occurs.

**Since:** 1.4
**See Also:** Component.requestFocus()

,

isFocusCycleRoot(java.awt.Container)

,

setFocusCycleRoot(boolean)

---

#### transferFocusDownCycle

public void transferFocusDownCycle()

Transfers the focus down one focus traversal cycle. If this Container is
a focus cycle root, then the focus owner is set to this Container's
default Component to focus, and the current focus cycle root is set to
this Container. If this Container is not a focus cycle root, then no
focus traversal operation occurs.

applyComponentOrientation

```java
public void applyComponentOrientation​(
ComponentOrientation
o)
```

Sets the

ComponentOrientation

property of this container
and all components contained within it.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

**Overrides:** applyComponentOrientation

in class

Component
**Parameters:** o

- the new component orientation of this container and
the components contained within it.
**Throws:** NullPointerException

- if

orientation

is null.
**Since:** 1.4
**See Also:** Component.setComponentOrientation(java.awt.ComponentOrientation)

,

Component.getComponentOrientation()

,

invalidate()

---

#### applyComponentOrientation

public void applyComponentOrientation​(

ComponentOrientation

o)

Sets the

ComponentOrientation

property of this container
and all components contained within it.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

This method changes layout-related information, and therefore,
invalidates the component hierarchy.

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Container's font ("font")
- this Container's background color ("background")
- this Container's foreground color ("foreground")
- this Container's focusability ("focusable")
- this Container's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Container's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Container's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Container's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Container's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Container's focus traversal policy ("focusTraversalPolicy")
- this Container's focus-cycle-root state ("focusCycleRoot")

Note that if this Container is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:** addPropertyChangeListener

in class

Component
**Parameters:** listener

- the PropertyChangeListener to be added
**See Also:** Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

,

addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list. The listener is
registered for all bound properties of this class, including the
following:

- this Container's font ("font")
- this Container's background color ("background")
- this Container's foreground color ("foreground")
- this Container's focusability ("focusable")
- this Container's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Container's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Container's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Container's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Container's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Container's focus traversal policy ("focusTraversalPolicy")
- this Container's focus-cycle-root state ("focusCycleRoot")

Note that if this Container is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

this Container's font ("font")

this Container's background color ("background")

this Container's foreground color ("foreground")

this Container's focusability ("focusable")

this Container's focus traversal keys enabled state
("focusTraversalKeysEnabled")

this Container's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")

this Container's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")

this Container's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")

this Container's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")

this Container's focus traversal policy ("focusTraversalPolicy")

this Container's focus-cycle-root state ("focusCycleRoot")

If listener is null, no exception is thrown and no action is performed.

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
String
propertyName,

PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following defaults:

- this Container's font ("font")
- this Container's background color ("background")
- this Container's foreground color ("foreground")
- this Container's focusability ("focusable")
- this Container's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Container's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Container's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Container's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Container's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Container's focus traversal policy ("focusTraversalPolicy")
- this Container's focus-cycle-root state ("focusCycleRoot")
- this Container's focus-traversal-policy-provider state("focusTraversalPolicyProvider")
- this Container's focus-traversal-policy-provider state("focusTraversalPolicyProvider")

Note that if this Container is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

**Overrides:** addPropertyChangeListener

in class

Component
**Parameters:** propertyName

- one of the property names listed above
**Parameters:** listener

- the PropertyChangeListener to be added
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Component.removePropertyChangeListener(java.beans.PropertyChangeListener)

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

String

propertyName,

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list for a specific
property. The specified property may be user-defined, or one of the
following defaults:

- this Container's font ("font")
- this Container's background color ("background")
- this Container's foreground color ("foreground")
- this Container's focusability ("focusable")
- this Container's focus traversal keys enabled state
("focusTraversalKeysEnabled")
- this Container's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")
- this Container's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")
- this Container's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")
- this Container's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")
- this Container's focus traversal policy ("focusTraversalPolicy")
- this Container's focus-cycle-root state ("focusCycleRoot")
- this Container's focus-traversal-policy-provider state("focusTraversalPolicyProvider")
- this Container's focus-traversal-policy-provider state("focusTraversalPolicyProvider")

Note that if this Container is inheriting a bound property, then no
event will be fired in response to a change in the inherited property.

If listener is null, no exception is thrown and no action is performed.

this Container's font ("font")

this Container's background color ("background")

this Container's foreground color ("foreground")

this Container's focusability ("focusable")

this Container's focus traversal keys enabled state
("focusTraversalKeysEnabled")

this Container's Set of FORWARD_TRAVERSAL_KEYS
("forwardFocusTraversalKeys")

this Container's Set of BACKWARD_TRAVERSAL_KEYS
("backwardFocusTraversalKeys")

this Container's Set of UP_CYCLE_TRAVERSAL_KEYS
("upCycleFocusTraversalKeys")

this Container's Set of DOWN_CYCLE_TRAVERSAL_KEYS
("downCycleFocusTraversalKeys")

this Container's focus traversal policy ("focusTraversalPolicy")

this Container's focus-cycle-root state ("focusCycleRoot")

this Container's focus-traversal-policy-provider state("focusTraversalPolicyProvider")

this Container's focus-traversal-policy-provider state("focusTraversalPolicyProvider")

If listener is null, no exception is thrown and no action is performed.

---

