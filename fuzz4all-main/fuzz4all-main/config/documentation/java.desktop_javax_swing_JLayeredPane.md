# Class JLayeredPane

**Source:** `java.desktop\javax\swing\JLayeredPane.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="accessibleContext")
public class
JLayeredPane

extends
JComponent

implements
Accessible
```

JLayeredPane

adds depth to a JFC/Swing container,
allowing components to overlap each other when needed.
An

Integer

object specifies each component's depth in the
container, where higher-numbered components sit "on top" of other
components.
For task-oriented documentation and examples of using layered panes see

How to Use a Layered Pane

,
a section in

The Java Tutorial

.

Example

For convenience,

JLayeredPane

divides the depth-range
into several different layers. Putting a component into one of those
layers makes it easy to ensure that components overlap properly,
without having to worry about specifying numbers for specific depths:

**DEFAULT_LAYER:** The standard layer, where most components go. This the bottommost
layer.

PALETTE_LAYER

The palette layer sits over the default layer. Useful for floating
toolbars and palettes, so they can be positioned above other components.

MODAL_LAYER

The layer used for modal dialogs. They will appear on top of any
toolbars, palettes, or standard components in the container.

POPUP_LAYER

The popup layer displays above dialogs. That way, the popup windows
associated with combo boxes, tooltips, and other help text will appear
above the component, palette, or dialog that generated them.

DRAG_LAYER

When dragging a component, reassigning it to the drag layer ensures
that it is positioned over every other component in the container. When
finished dragging, it can be reassigned to its normal layer.

The

JLayeredPane

methods

moveToFront(Component)

,

moveToBack(Component)

and

setPosition

can be used
to reposition a component within its layer. The

setLayer

method
can also be used to change the component's current layer.

Details

JLayeredPane

manages its list of children like

Container

, but allows for the definition of a several
layers within itself. Children in the same layer are managed exactly
like the normal

Container

object,
with the added feature that when children components overlap, children
in higher layers display above the children in lower layers.

Each layer is a distinct integer number. The layer attribute can be set
on a

Component

by passing an

Integer

object during the add call.

For example:

```java
layeredPane.add(child, JLayeredPane.DEFAULT_LAYER);
or
layeredPane.add(child, Integer.valueOf.valueOf(10));
```

The layer attribute can also be set on a Component by calling

```java
layeredPaneParent.setLayer(child, 10)
```

on the

JLayeredPane

that is the parent of component. The layer
should be set

before

adding the child to the parent.

Higher number layers display above lower number layers. So, using
numbers for the layers and letters for individual components, a
representative list order would look like this:

```java
5a, 5b, 5c, 2a, 2b, 2c, 1a
```

where the leftmost components are closest to the top of the display.

A component can be moved to the top or bottom position within its
layer by calling

moveToFront

or

moveToBack

.

The position of a component within a layer can also be specified directly.
Valid positions range from 0 up to one less than the number of
components in that layer. A value of -1 indicates the bottommost
position. A value of 0 indicates the topmost position. Unlike layer
numbers, higher position values are

lower

in the display.

Note:

This sequence (defined by java.awt.Container) is the reverse
of the layer numbering sequence. Usually though, you will use

moveToFront

,

moveToBack

, and

setLayer

.

Here are some examples using the method add(Component, layer, position):
Calling add(5x, 5, -1) results in:

```java
5a, 5b, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(5z, 5, 2) results in:

```java
5a, 5b, 5z, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(3a, 3, 7) results in:

```java
5a, 5b, 5z, 5c, 5x, 3a, 2a, 2b, 2c, 1a
```

Using normal paint/event mechanics results in 1a appearing at the bottom
and 5a being above all other components.

Note:

that these layers are simply a logical construct and LayoutManagers
will affect all child components of this container without regard for
layer settings.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

---

### Field Details

#### public static final
Integer
DEFAULT_LAYER

Convenience object defining the Default layer. Equivalent to Integer.valueOf(0).

---

#### public static final
Integer
PALETTE_LAYER

Convenience object defining the Palette layer. Equivalent to Integer.valueOf(100).

---

#### public static final
Integer
MODAL_LAYER

Convenience object defining the Modal layer. Equivalent to Integer.valueOf(200).

---

#### public static final
Integer
POPUP_LAYER

Convenience object defining the Popup layer. Equivalent to Integer.valueOf(300).

---

#### public static final
Integer
DRAG_LAYER

Convenience object defining the Drag layer. Equivalent to Integer.valueOf(400).

---

#### public static final
Integer
FRAME_CONTENT_LAYER

Convenience object defining the Frame Content layer.
This layer is normally only use to position the contentPane and menuBar
components of JFrame.
Equivalent to Integer.valueOf(-30000).

**See Also:**
- JFrame

---

#### public static final
String
LAYER_PROPERTY

Bound property

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public JLayeredPane()

Create a new JLayeredPane

---

### Method Details

#### public void remove​(int index)

Remove the indexed component from this pane.
This is the absolute index, ignoring layers.

**Overrides:**
- remove

in class

Container

**Parameters:**
- index

- an int specifying the component to remove

**See Also:**
- getIndexOf(java.awt.Component)

---

#### public void removeAll()

Removes all the components from this container.

**Overrides:**
- removeAll

in class

Container

**See Also:**
- Container.add(java.awt.Component)

,

Container.remove(int)

,

Container.invalidate()

**Since:**
- 1.5

---

#### @BeanProperty
(
bound
=false)
public boolean isOptimizedDrawingEnabled()

Returns false if components in the pane can overlap, which makes
optimized drawing impossible. Otherwise, returns true.

**Overrides:**
- isOptimizedDrawingEnabled

in class

JComponent

**Returns:**
- false if components can overlap, else true

**See Also:**
- JComponent.isOptimizedDrawingEnabled()

---

#### public static void putLayer​(
JComponent
c,
int layer)

Sets the layer property on a JComponent. This method does not cause
any side effects like setLayer() (painting, add/remove, etc).
Normally you should use the instance method setLayer(), in order to
get the desired side-effects (like repainting).

**Parameters:**
- c

- the JComponent to move
- layer

- an int specifying the layer to move it to

**See Also:**
- setLayer(java.awt.Component, int)

---

#### public static int getLayer​(
JComponent
c)

Gets the layer property for a JComponent, it
does not cause any side effects like setLayer(). (painting, add/remove, etc)
Normally you should use the instance method getLayer().

**Parameters:**
- c

- the JComponent to check

**Returns:**
- an int specifying the component's layer

---

#### public static
JLayeredPane
getLayeredPaneAbove​(
Component
c)

Convenience method that returns the first JLayeredPane which
contains the specified component. Note that all JFrames have a
JLayeredPane at their root, so any component in a JFrame will
have a JLayeredPane parent.

**Parameters:**
- c

- the Component to check

**Returns:**
- the JLayeredPane that contains the component, or
null if no JLayeredPane is found in the component
hierarchy

**See Also:**
- JFrame

,

JRootPane

---

#### public void setLayer​(
Component
c,
int layer)

Sets the layer attribute on the specified component,
making it the bottommost component in that layer.
Should be called before adding to parent.

**Parameters:**
- c

- the Component to set the layer for
- layer

- an int specifying the layer to set, where
lower numbers are closer to the bottom

---

#### public void setLayer​(
Component
c,
int layer,
int position)

Sets the layer attribute for the specified component and
also sets its position within that layer.

**Parameters:**
- c

- the Component to set the layer for
- layer

- an int specifying the layer to set, where
lower numbers are closer to the bottom
- position

- an int specifying the position within the
layer, where 0 is the topmost position and -1
is the bottommost position

---

#### public int getLayer​(
Component
c)

Returns the layer attribute for the specified Component.

**Parameters:**
- c

- the Component to check

**Returns:**
- an int specifying the component's current layer

---

#### public int getIndexOf​(
Component
c)

Returns the index of the specified Component.
This is the absolute index, ignoring layers.
Index numbers, like position numbers, have the topmost component
at index zero. Larger numbers are closer to the bottom.

**Parameters:**
- c

- the Component to check

**Returns:**
- an int specifying the component's index

---

#### public void moveToFront​(
Component
c)

Moves the component to the top of the components in its current layer
(position 0).

**Parameters:**
- c

- the Component to move

**See Also:**
- setPosition(Component, int)

---

#### public void moveToBack​(
Component
c)

Moves the component to the bottom of the components in its current layer
(position -1).

**Parameters:**
- c

- the Component to move

**See Also:**
- setPosition(Component, int)

---

#### public void setPosition​(
Component
c,
int position)

Moves the component to

position

within its current layer,
where 0 is the topmost position within the layer and -1 is the bottommost
position.

Note:

Position numbering is defined by java.awt.Container, and
is the opposite of layer numbering. Lower position numbers are closer
to the top (0 is topmost), and higher position numbers are closer to
the bottom.

**Parameters:**
- c

- the Component to move
- position

- an int in the range -1..N-1, where N is the number of
components in the component's current layer

---

#### public int getPosition​(
Component
c)

Get the relative position of the component within its layer.

**Parameters:**
- c

- the Component to check

**Returns:**
- an int giving the component's position, where 0 is the
topmost position and the highest index value = the count
count of components at that layer, minus 1

**See Also:**
- getComponentCountInLayer(int)

---

#### public int highestLayer()

Returns the highest layer value from all current children.
Returns 0 if there are no children.

**Returns:**
- an int indicating the layer of the topmost component in the
pane, or zero if there are no children

---

#### public int lowestLayer()

Returns the lowest layer value from all current children.
Returns 0 if there are no children.

**Returns:**
- an int indicating the layer of the bottommost component in the
pane, or zero if there are no children

---

#### public int getComponentCountInLayer​(int layer)

Returns the number of children currently in the specified layer.

**Parameters:**
- layer

- an int specifying the layer to check

**Returns:**
- an int specifying the number of components in that layer

---

#### public
Component
[] getComponentsInLayer​(int layer)

Returns an array of the components in the specified layer.

**Parameters:**
- layer

- an int specifying the layer to check

**Returns:**
- an array of Components contained in that layer

---

#### public void paint​(
Graphics
g)

Paints this JLayeredPane within the specified graphics context.

**Overrides:**
- paint

in class

JComponent

**Parameters:**
- g

- the Graphics context within which to paint

**See Also:**
- JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

---

#### protected
Hashtable
<
Component
,​
Integer
> getComponentToLayer()

Returns the hashtable that maps components to layers.

**Returns:**
- the Hashtable used to map components to their layers

---

#### protected
Integer
getObjectForLayer​(int layer)

Returns the Integer object associated with a specified layer.

**Parameters:**
- layer

- an int specifying the layer

**Returns:**
- an Integer object for that layer

---

#### protected int insertIndexForLayer​(int layer,
int position)

Primitive method that determines the proper location to
insert a new child based on layer and position requests.

**Parameters:**
- layer

- an int specifying the layer
- position

- an int specifying the position within the layer

**Returns:**
- an int giving the (absolute) insertion-index

**See Also:**
- getIndexOf(java.awt.Component)

---

#### protected
String
paramString()

Returns a string representation of this JLayeredPane. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

JComponent

**Returns:**
- a string representation of this JLayeredPane.

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JLayeredPane.
For layered panes, the AccessibleContext takes the form of an
AccessibleJLayeredPane.
A new AccessibleJLayeredPane instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleJLayeredPane that serves as the
AccessibleContext of this JLayeredPane

---

### Additional Sections

#### Class JLayeredPane

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JLayeredPane

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JLayeredPane

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JLayeredPane

javax.swing.JComponent

- javax.swing.JLayeredPane

javax.swing.JLayeredPane

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

**Direct Known Subclasses:** JDesktopPane

```java
@JavaBean
(
defaultProperty
="accessibleContext")
public class
JLayeredPane

extends
JComponent

implements
Accessible
```

JLayeredPane

adds depth to a JFC/Swing container,
allowing components to overlap each other when needed.
An

Integer

object specifies each component's depth in the
container, where higher-numbered components sit "on top" of other
components.
For task-oriented documentation and examples of using layered panes see

How to Use a Layered Pane

,
a section in

The Java Tutorial

.

Example

For convenience,

JLayeredPane

divides the depth-range
into several different layers. Putting a component into one of those
layers makes it easy to ensure that components overlap properly,
without having to worry about specifying numbers for specific depths:

**DEFAULT_LAYER:** The standard layer, where most components go. This the bottommost
layer.

PALETTE_LAYER

The palette layer sits over the default layer. Useful for floating
toolbars and palettes, so they can be positioned above other components.

MODAL_LAYER

The layer used for modal dialogs. They will appear on top of any
toolbars, palettes, or standard components in the container.

POPUP_LAYER

The popup layer displays above dialogs. That way, the popup windows
associated with combo boxes, tooltips, and other help text will appear
above the component, palette, or dialog that generated them.

DRAG_LAYER

When dragging a component, reassigning it to the drag layer ensures
that it is positioned over every other component in the container. When
finished dragging, it can be reassigned to its normal layer.

The

JLayeredPane

methods

moveToFront(Component)

,

moveToBack(Component)

and

setPosition

can be used
to reposition a component within its layer. The

setLayer

method
can also be used to change the component's current layer.

Details

JLayeredPane

manages its list of children like

Container

, but allows for the definition of a several
layers within itself. Children in the same layer are managed exactly
like the normal

Container

object,
with the added feature that when children components overlap, children
in higher layers display above the children in lower layers.

Each layer is a distinct integer number. The layer attribute can be set
on a

Component

by passing an

Integer

object during the add call.

For example:

```java
layeredPane.add(child, JLayeredPane.DEFAULT_LAYER);
or
layeredPane.add(child, Integer.valueOf.valueOf(10));
```

The layer attribute can also be set on a Component by calling

```java
layeredPaneParent.setLayer(child, 10)
```

on the

JLayeredPane

that is the parent of component. The layer
should be set

before

adding the child to the parent.

Higher number layers display above lower number layers. So, using
numbers for the layers and letters for individual components, a
representative list order would look like this:

```java
5a, 5b, 5c, 2a, 2b, 2c, 1a
```

where the leftmost components are closest to the top of the display.

A component can be moved to the top or bottom position within its
layer by calling

moveToFront

or

moveToBack

.

The position of a component within a layer can also be specified directly.
Valid positions range from 0 up to one less than the number of
components in that layer. A value of -1 indicates the bottommost
position. A value of 0 indicates the topmost position. Unlike layer
numbers, higher position values are

lower

in the display.

Note:

This sequence (defined by java.awt.Container) is the reverse
of the layer numbering sequence. Usually though, you will use

moveToFront

,

moveToBack

, and

setLayer

.

Here are some examples using the method add(Component, layer, position):
Calling add(5x, 5, -1) results in:

```java
5a, 5b, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(5z, 5, 2) results in:

```java
5a, 5b, 5z, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(3a, 3, 7) results in:

```java
5a, 5b, 5z, 5c, 5x, 3a, 2a, 2b, 2c, 1a
```

Using normal paint/event mechanics results in 1a appearing at the bottom
and 5a being above all other components.

Note:

that these layers are simply a logical construct and LayoutManagers
will affect all child components of this container without regard for
layer settings.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**Since:** 1.2
**See Also:** Serialized Form

@JavaBean

(

defaultProperty

="accessibleContext")
public class

JLayeredPane

extends

JComponent

implements

Accessible

JLayeredPane

adds depth to a JFC/Swing container,
allowing components to overlap each other when needed.
An

Integer

object specifies each component's depth in the
container, where higher-numbered components sit "on top" of other
components.
For task-oriented documentation and examples of using layered panes see

How to Use a Layered Pane

,
a section in

The Java Tutorial

.

Example

For convenience,

JLayeredPane

divides the depth-range
into several different layers. Putting a component into one of those
layers makes it easy to ensure that components overlap properly,
without having to worry about specifying numbers for specific depths:

**DEFAULT_LAYER:** The standard layer, where most components go. This the bottommost
layer.

PALETTE_LAYER

The palette layer sits over the default layer. Useful for floating
toolbars and palettes, so they can be positioned above other components.

MODAL_LAYER

The layer used for modal dialogs. They will appear on top of any
toolbars, palettes, or standard components in the container.

POPUP_LAYER

The popup layer displays above dialogs. That way, the popup windows
associated with combo boxes, tooltips, and other help text will appear
above the component, palette, or dialog that generated them.

DRAG_LAYER

When dragging a component, reassigning it to the drag layer ensures
that it is positioned over every other component in the container. When
finished dragging, it can be reassigned to its normal layer.

The

JLayeredPane

methods

moveToFront(Component)

,

moveToBack(Component)

and

setPosition

can be used
to reposition a component within its layer. The

setLayer

method
can also be used to change the component's current layer.

Details

JLayeredPane

manages its list of children like

Container

, but allows for the definition of a several
layers within itself. Children in the same layer are managed exactly
like the normal

Container

object,
with the added feature that when children components overlap, children
in higher layers display above the children in lower layers.

Each layer is a distinct integer number. The layer attribute can be set
on a

Component

by passing an

Integer

object during the add call.

For example:

```java
layeredPane.add(child, JLayeredPane.DEFAULT_LAYER);
or
layeredPane.add(child, Integer.valueOf.valueOf(10));
```

The layer attribute can also be set on a Component by calling

```java
layeredPaneParent.setLayer(child, 10)
```

on the

JLayeredPane

that is the parent of component. The layer
should be set

before

adding the child to the parent.

Higher number layers display above lower number layers. So, using
numbers for the layers and letters for individual components, a
representative list order would look like this:

```java
5a, 5b, 5c, 2a, 2b, 2c, 1a
```

where the leftmost components are closest to the top of the display.

A component can be moved to the top or bottom position within its
layer by calling

moveToFront

or

moveToBack

.

The position of a component within a layer can also be specified directly.
Valid positions range from 0 up to one less than the number of
components in that layer. A value of -1 indicates the bottommost
position. A value of 0 indicates the topmost position. Unlike layer
numbers, higher position values are

lower

in the display.

Note:

This sequence (defined by java.awt.Container) is the reverse
of the layer numbering sequence. Usually though, you will use

moveToFront

,

moveToBack

, and

setLayer

.

Here are some examples using the method add(Component, layer, position):
Calling add(5x, 5, -1) results in:

```java
5a, 5b, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(5z, 5, 2) results in:

```java
5a, 5b, 5z, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(3a, 3, 7) results in:

```java
5a, 5b, 5z, 5c, 5x, 3a, 2a, 2b, 2c, 1a
```

Using normal paint/event mechanics results in 1a appearing at the bottom
and 5a being above all other components.

Note:

that these layers are simply a logical construct and LayoutManagers
will affect all child components of this container without regard for
layer settings.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

---

#### Details

Each layer is a distinct integer number. The layer attribute can be set
on a

Component

by passing an

Integer

object during the add call.

For example:

```java
layeredPane.add(child, JLayeredPane.DEFAULT_LAYER);
or
layeredPane.add(child, Integer.valueOf.valueOf(10));
```

The layer attribute can also be set on a Component by calling

```java
layeredPaneParent.setLayer(child, 10)
```

on the

JLayeredPane

that is the parent of component. The layer
should be set

before

adding the child to the parent.

Higher number layers display above lower number layers. So, using
numbers for the layers and letters for individual components, a
representative list order would look like this:

```java
5a, 5b, 5c, 2a, 2b, 2c, 1a
```

where the leftmost components are closest to the top of the display.

A component can be moved to the top or bottom position within its
layer by calling

moveToFront

or

moveToBack

.

The position of a component within a layer can also be specified directly.
Valid positions range from 0 up to one less than the number of
components in that layer. A value of -1 indicates the bottommost
position. A value of 0 indicates the topmost position. Unlike layer
numbers, higher position values are

lower

in the display.

Note:

This sequence (defined by java.awt.Container) is the reverse
of the layer numbering sequence. Usually though, you will use

moveToFront

,

moveToBack

, and

setLayer

.

Here are some examples using the method add(Component, layer, position):
Calling add(5x, 5, -1) results in:

```java
5a, 5b, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(5z, 5, 2) results in:

```java
5a, 5b, 5z, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(3a, 3, 7) results in:

```java
5a, 5b, 5z, 5c, 5x, 3a, 2a, 2b, 2c, 1a
```

Using normal paint/event mechanics results in 1a appearing at the bottom
and 5a being above all other components.

Note:

that these layers are simply a logical construct and LayoutManagers
will affect all child components of this container without regard for
layer settings.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

layeredPane.add(child, JLayeredPane.DEFAULT_LAYER);
or
layeredPane.add(child, Integer.valueOf.valueOf(10));

layeredPaneParent.setLayer(child, 10)

Higher number layers display above lower number layers. So, using
numbers for the layers and letters for individual components, a
representative list order would look like this:

```java
5a, 5b, 5c, 2a, 2b, 2c, 1a
```

where the leftmost components are closest to the top of the display.

A component can be moved to the top or bottom position within its
layer by calling

moveToFront

or

moveToBack

.

The position of a component within a layer can also be specified directly.
Valid positions range from 0 up to one less than the number of
components in that layer. A value of -1 indicates the bottommost
position. A value of 0 indicates the topmost position. Unlike layer
numbers, higher position values are

lower

in the display.

Note:

This sequence (defined by java.awt.Container) is the reverse
of the layer numbering sequence. Usually though, you will use

moveToFront

,

moveToBack

, and

setLayer

.

Here are some examples using the method add(Component, layer, position):
Calling add(5x, 5, -1) results in:

```java
5a, 5b, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(5z, 5, 2) results in:

```java
5a, 5b, 5z, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(3a, 3, 7) results in:

```java
5a, 5b, 5z, 5c, 5x, 3a, 2a, 2b, 2c, 1a
```

Using normal paint/event mechanics results in 1a appearing at the bottom
and 5a being above all other components.

Note:

that these layers are simply a logical construct and LayoutManagers
will affect all child components of this container without regard for
layer settings.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

5a, 5b, 5c, 2a, 2b, 2c, 1a

A component can be moved to the top or bottom position within its
layer by calling

moveToFront

or

moveToBack

.

The position of a component within a layer can also be specified directly.
Valid positions range from 0 up to one less than the number of
components in that layer. A value of -1 indicates the bottommost
position. A value of 0 indicates the topmost position. Unlike layer
numbers, higher position values are

lower

in the display.

Note:

This sequence (defined by java.awt.Container) is the reverse
of the layer numbering sequence. Usually though, you will use

moveToFront

,

moveToBack

, and

setLayer

.

Here are some examples using the method add(Component, layer, position):
Calling add(5x, 5, -1) results in:

```java
5a, 5b, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(5z, 5, 2) results in:

```java
5a, 5b, 5z, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(3a, 3, 7) results in:

```java
5a, 5b, 5z, 5c, 5x, 3a, 2a, 2b, 2c, 1a
```

Using normal paint/event mechanics results in 1a appearing at the bottom
and 5a being above all other components.

Note:

that these layers are simply a logical construct and LayoutManagers
will affect all child components of this container without regard for
layer settings.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

The position of a component within a layer can also be specified directly.
Valid positions range from 0 up to one less than the number of
components in that layer. A value of -1 indicates the bottommost
position. A value of 0 indicates the topmost position. Unlike layer
numbers, higher position values are

lower

in the display.

Note:

This sequence (defined by java.awt.Container) is the reverse
of the layer numbering sequence. Usually though, you will use

moveToFront

,

moveToBack

, and

setLayer

.

Here are some examples using the method add(Component, layer, position):
Calling add(5x, 5, -1) results in:

```java
5a, 5b, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(5z, 5, 2) results in:

```java
5a, 5b, 5z, 5c, 5x, 2a, 2b, 2c, 1a
```

Calling add(3a, 3, 7) results in:

```java
5a, 5b, 5z, 5c, 5x, 3a, 2a, 2b, 2c, 1a
```

Using normal paint/event mechanics results in 1a appearing at the bottom
and 5a being above all other components.

Note:

that these layers are simply a logical construct and LayoutManagers
will affect all child components of this container without regard for
layer settings.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

5a, 5b, 5c, 5x, 2a, 2b, 2c, 1a

5a, 5b, 5z, 5c, 5x, 2a, 2b, 2c, 1a

5a, 5b, 5z, 5c, 5x, 3a, 2a, 2b, 2c, 1a

Note:

that these layers are simply a logical construct and LayoutManagers
will affect all child components of this container without regard for
layer settings.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

JLayeredPane.AccessibleJLayeredPane

This class implements accessibility support for the

JLayeredPane

class.

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

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

Fields

Modifier and Type

Field

Description

static

Integer

DEFAULT_LAYER

Convenience object defining the Default layer.

static

Integer

DRAG_LAYER

Convenience object defining the Drag layer.

static

Integer

FRAME_CONTENT_LAYER

Convenience object defining the Frame Content layer.

static

String

LAYER_PROPERTY

Bound property

static

Integer

MODAL_LAYER

Convenience object defining the Modal layer.

static

Integer

PALETTE_LAYER

Convenience object defining the Palette layer.

static

Integer

POPUP_LAYER

Convenience object defining the Popup layer.

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

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

JLayeredPane

()

Create a new JLayeredPane

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JLayeredPane.

int

getComponentCountInLayer

​(int layer)

Returns the number of children currently in the specified layer.

Component

[]

getComponentsInLayer

​(int layer)

Returns an array of the components in the specified layer.

protected

Hashtable

<

Component

,​

Integer

>

getComponentToLayer

()

Returns the hashtable that maps components to layers.

int

getIndexOf

​(

Component

c)

Returns the index of the specified Component.

int

getLayer

​(

Component

c)

Returns the layer attribute for the specified Component.

static int

getLayer

​(

JComponent

c)

Gets the layer property for a JComponent, it
does not cause any side effects like setLayer().

static

JLayeredPane

getLayeredPaneAbove

​(

Component

c)

Convenience method that returns the first JLayeredPane which
contains the specified component.

protected

Integer

getObjectForLayer

​(int layer)

Returns the Integer object associated with a specified layer.

int

getPosition

​(

Component

c)

Get the relative position of the component within its layer.

int

highestLayer

()

Returns the highest layer value from all current children.

protected int

insertIndexForLayer

​(int layer,
int position)

Primitive method that determines the proper location to
insert a new child based on layer and position requests.

boolean

isOptimizedDrawingEnabled

()

Returns false if components in the pane can overlap, which makes
optimized drawing impossible.

int

lowestLayer

()

Returns the lowest layer value from all current children.

void

moveToBack

​(

Component

c)

Moves the component to the bottom of the components in its current layer
(position -1).

void

moveToFront

​(

Component

c)

Moves the component to the top of the components in its current layer
(position 0).

void

paint

​(

Graphics

g)

Paints this JLayeredPane within the specified graphics context.

protected

String

paramString

()

Returns a string representation of this JLayeredPane.

static void

putLayer

​(

JComponent

c,
int layer)

Sets the layer property on a JComponent.

void

remove

​(int index)

Remove the indexed component from this pane.

void

removeAll

()

Removes all the components from this container.

void

setLayer

​(

Component

c,
int layer)

Sets the layer attribute on the specified component,
making it the bottommost component in that layer.

void

setLayer

​(

Component

c,
int layer,
int position)

Sets the layer attribute for the specified component and
also sets its position within that layer.

void

setPosition

​(

Component

c,
int position)

Moves the component to

position

within its current layer,
where 0 is the topmost position within the layer and -1 is the bottommost
position.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getUI

,

getUIClassID

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

,

updateUI

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

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

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

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

getBackground

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

getForeground

,

getGraphicsConfiguration

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

getToolkit

,

getTreeLock

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

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

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

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

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

JLayeredPane.AccessibleJLayeredPane

This class implements accessibility support for the

JLayeredPane

class.

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

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

This class implements accessibility support for the

JLayeredPane

class.

Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

---

#### Nested classes/interfaces declared in class javax.swing. JComponent

Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

---

#### Nested classes/interfaces declared in class java.awt. Container

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

Fields

Modifier and Type

Field

Description

static

Integer

DEFAULT_LAYER

Convenience object defining the Default layer.

static

Integer

DRAG_LAYER

Convenience object defining the Drag layer.

static

Integer

FRAME_CONTENT_LAYER

Convenience object defining the Frame Content layer.

static

String

LAYER_PROPERTY

Bound property

static

Integer

MODAL_LAYER

Convenience object defining the Modal layer.

static

Integer

PALETTE_LAYER

Convenience object defining the Palette layer.

static

Integer

POPUP_LAYER

Convenience object defining the Popup layer.

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

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

Convenience object defining the Default layer.

Convenience object defining the Drag layer.

Convenience object defining the Frame Content layer.

Bound property

Convenience object defining the Modal layer.

Convenience object defining the Palette layer.

Convenience object defining the Popup layer.

Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

---

#### Fields declared in class javax.swing. JComponent

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

JLayeredPane

()

Create a new JLayeredPane

---

#### Constructor Summary

Create a new JLayeredPane

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JLayeredPane.

int

getComponentCountInLayer

​(int layer)

Returns the number of children currently in the specified layer.

Component

[]

getComponentsInLayer

​(int layer)

Returns an array of the components in the specified layer.

protected

Hashtable

<

Component

,​

Integer

>

getComponentToLayer

()

Returns the hashtable that maps components to layers.

int

getIndexOf

​(

Component

c)

Returns the index of the specified Component.

int

getLayer

​(

Component

c)

Returns the layer attribute for the specified Component.

static int

getLayer

​(

JComponent

c)

Gets the layer property for a JComponent, it
does not cause any side effects like setLayer().

static

JLayeredPane

getLayeredPaneAbove

​(

Component

c)

Convenience method that returns the first JLayeredPane which
contains the specified component.

protected

Integer

getObjectForLayer

​(int layer)

Returns the Integer object associated with a specified layer.

int

getPosition

​(

Component

c)

Get the relative position of the component within its layer.

int

highestLayer

()

Returns the highest layer value from all current children.

protected int

insertIndexForLayer

​(int layer,
int position)

Primitive method that determines the proper location to
insert a new child based on layer and position requests.

boolean

isOptimizedDrawingEnabled

()

Returns false if components in the pane can overlap, which makes
optimized drawing impossible.

int

lowestLayer

()

Returns the lowest layer value from all current children.

void

moveToBack

​(

Component

c)

Moves the component to the bottom of the components in its current layer
(position -1).

void

moveToFront

​(

Component

c)

Moves the component to the top of the components in its current layer
(position 0).

void

paint

​(

Graphics

g)

Paints this JLayeredPane within the specified graphics context.

protected

String

paramString

()

Returns a string representation of this JLayeredPane.

static void

putLayer

​(

JComponent

c,
int layer)

Sets the layer property on a JComponent.

void

remove

​(int index)

Remove the indexed component from this pane.

void

removeAll

()

Removes all the components from this container.

void

setLayer

​(

Component

c,
int layer)

Sets the layer attribute on the specified component,
making it the bottommost component in that layer.

void

setLayer

​(

Component

c,
int layer,
int position)

Sets the layer attribute for the specified component and
also sets its position within that layer.

void

setPosition

​(

Component

c,
int position)

Moves the component to

position

within its current layer,
where 0 is the topmost position within the layer and -1 is the bottommost
position.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getUI

,

getUIClassID

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

,

updateUI

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

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

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

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

getBackground

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

getForeground

,

getGraphicsConfiguration

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

getToolkit

,

getTreeLock

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

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

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

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

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

Gets the AccessibleContext associated with this JLayeredPane.

Returns the number of children currently in the specified layer.

Returns an array of the components in the specified layer.

Returns the hashtable that maps components to layers.

Returns the index of the specified Component.

Returns the layer attribute for the specified Component.

Gets the layer property for a JComponent, it
does not cause any side effects like setLayer().

Convenience method that returns the first JLayeredPane which
contains the specified component.

Returns the Integer object associated with a specified layer.

Get the relative position of the component within its layer.

Returns the highest layer value from all current children.

Primitive method that determines the proper location to
insert a new child based on layer and position requests.

Returns false if components in the pane can overlap, which makes
optimized drawing impossible.

Returns the lowest layer value from all current children.

Moves the component to the bottom of the components in its current layer
(position -1).

Moves the component to the top of the components in its current layer
(position 0).

Paints this JLayeredPane within the specified graphics context.

Returns a string representation of this JLayeredPane.

Sets the layer property on a JComponent.

Remove the indexed component from this pane.

Removes all the components from this container.

Sets the layer attribute on the specified component,
making it the bottommost component in that layer.

Sets the layer attribute for the specified component and
also sets its position within that layer.

Moves the component to

position

within its current layer,
where 0 is the topmost position within the layer and -1 is the bottommost
position.

Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getUI

,

getUIClassID

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

,

updateUI

---

#### Methods declared in class javax.swing. JComponent

Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

---

#### Methods declared in class java.awt. Container

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

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

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

getBackground

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

getForeground

,

getGraphicsConfiguration

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

getToolkit

,

getTreeLock

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

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

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

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

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

============ FIELD DETAIL ===========

- Field Detail

- DEFAULT_LAYER

```java
public static final
Integer
DEFAULT_LAYER
```

Convenience object defining the Default layer. Equivalent to Integer.valueOf(0).

- PALETTE_LAYER

```java
public static final
Integer
PALETTE_LAYER
```

Convenience object defining the Palette layer. Equivalent to Integer.valueOf(100).

- MODAL_LAYER

```java
public static final
Integer
MODAL_LAYER
```

Convenience object defining the Modal layer. Equivalent to Integer.valueOf(200).

- POPUP_LAYER

```java
public static final
Integer
POPUP_LAYER
```

Convenience object defining the Popup layer. Equivalent to Integer.valueOf(300).

- DRAG_LAYER

```java
public static final
Integer
DRAG_LAYER
```

Convenience object defining the Drag layer. Equivalent to Integer.valueOf(400).

- FRAME_CONTENT_LAYER

```java
public static final
Integer
FRAME_CONTENT_LAYER
```

Convenience object defining the Frame Content layer.
This layer is normally only use to position the contentPane and menuBar
components of JFrame.
Equivalent to Integer.valueOf(-30000).

**See Also:** JFrame

- LAYER_PROPERTY

```java
public static final
String
LAYER_PROPERTY
```

Bound property

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JLayeredPane

```java
public JLayeredPane()
```

Create a new JLayeredPane

============ METHOD DETAIL ==========

- Method Detail

- remove

```java
public void remove​(int index)
```

Remove the indexed component from this pane.
This is the absolute index, ignoring layers.

**Overrides:** remove

in class

Container
**Parameters:** index

- an int specifying the component to remove
**See Also:** getIndexOf(java.awt.Component)

- removeAll

```java
public void removeAll()
```

Removes all the components from this container.

**Overrides:** removeAll

in class

Container
**Since:** 1.5
**See Also:** Container.add(java.awt.Component)

,

Container.remove(int)

,

Container.invalidate()

- isOptimizedDrawingEnabled

```java
@BeanProperty
(
bound
=false)
public boolean isOptimizedDrawingEnabled()
```

Returns false if components in the pane can overlap, which makes
optimized drawing impossible. Otherwise, returns true.

**Overrides:** isOptimizedDrawingEnabled

in class

JComponent
**Returns:** false if components can overlap, else true
**See Also:** JComponent.isOptimizedDrawingEnabled()

- putLayer

```java
public static void putLayer​(
JComponent
c,
int layer)
```

Sets the layer property on a JComponent. This method does not cause
any side effects like setLayer() (painting, add/remove, etc).
Normally you should use the instance method setLayer(), in order to
get the desired side-effects (like repainting).

**Parameters:** c

- the JComponent to move
**Parameters:** layer

- an int specifying the layer to move it to
**See Also:** setLayer(java.awt.Component, int)

- getLayer

```java
public static int getLayer​(
JComponent
c)
```

Gets the layer property for a JComponent, it
does not cause any side effects like setLayer(). (painting, add/remove, etc)
Normally you should use the instance method getLayer().

**Parameters:** c

- the JComponent to check
**Returns:** an int specifying the component's layer

- getLayeredPaneAbove

```java
public static
JLayeredPane
getLayeredPaneAbove​(
Component
c)
```

Convenience method that returns the first JLayeredPane which
contains the specified component. Note that all JFrames have a
JLayeredPane at their root, so any component in a JFrame will
have a JLayeredPane parent.

**Parameters:** c

- the Component to check
**Returns:** the JLayeredPane that contains the component, or
null if no JLayeredPane is found in the component
hierarchy
**See Also:** JFrame

,

JRootPane

- setLayer

```java
public void setLayer​(
Component
c,
int layer)
```

Sets the layer attribute on the specified component,
making it the bottommost component in that layer.
Should be called before adding to parent.

**Parameters:** c

- the Component to set the layer for
**Parameters:** layer

- an int specifying the layer to set, where
lower numbers are closer to the bottom

- setLayer

```java
public void setLayer​(
Component
c,
int layer,
int position)
```

Sets the layer attribute for the specified component and
also sets its position within that layer.

**Parameters:** c

- the Component to set the layer for
**Parameters:** layer

- an int specifying the layer to set, where
lower numbers are closer to the bottom
**Parameters:** position

- an int specifying the position within the
layer, where 0 is the topmost position and -1
is the bottommost position

- getLayer

```java
public int getLayer​(
Component
c)
```

Returns the layer attribute for the specified Component.

**Parameters:** c

- the Component to check
**Returns:** an int specifying the component's current layer

- getIndexOf

```java
public int getIndexOf​(
Component
c)
```

Returns the index of the specified Component.
This is the absolute index, ignoring layers.
Index numbers, like position numbers, have the topmost component
at index zero. Larger numbers are closer to the bottom.

**Parameters:** c

- the Component to check
**Returns:** an int specifying the component's index

- moveToFront

```java
public void moveToFront​(
Component
c)
```

Moves the component to the top of the components in its current layer
(position 0).

**Parameters:** c

- the Component to move
**See Also:** setPosition(Component, int)

- moveToBack

```java
public void moveToBack​(
Component
c)
```

Moves the component to the bottom of the components in its current layer
(position -1).

**Parameters:** c

- the Component to move
**See Also:** setPosition(Component, int)

- setPosition

```java
public void setPosition​(
Component
c,
int position)
```

Moves the component to

position

within its current layer,
where 0 is the topmost position within the layer and -1 is the bottommost
position.

Note:

Position numbering is defined by java.awt.Container, and
is the opposite of layer numbering. Lower position numbers are closer
to the top (0 is topmost), and higher position numbers are closer to
the bottom.

**Parameters:** c

- the Component to move
**Parameters:** position

- an int in the range -1..N-1, where N is the number of
components in the component's current layer

- getPosition

```java
public int getPosition​(
Component
c)
```

Get the relative position of the component within its layer.

**Parameters:** c

- the Component to check
**Returns:** an int giving the component's position, where 0 is the
topmost position and the highest index value = the count
count of components at that layer, minus 1
**See Also:** getComponentCountInLayer(int)

- highestLayer

```java
public int highestLayer()
```

Returns the highest layer value from all current children.
Returns 0 if there are no children.

**Returns:** an int indicating the layer of the topmost component in the
pane, or zero if there are no children

- lowestLayer

```java
public int lowestLayer()
```

Returns the lowest layer value from all current children.
Returns 0 if there are no children.

**Returns:** an int indicating the layer of the bottommost component in the
pane, or zero if there are no children

- getComponentCountInLayer

```java
public int getComponentCountInLayer​(int layer)
```

Returns the number of children currently in the specified layer.

**Parameters:** layer

- an int specifying the layer to check
**Returns:** an int specifying the number of components in that layer

- getComponentsInLayer

```java
public
Component
[] getComponentsInLayer​(int layer)
```

Returns an array of the components in the specified layer.

**Parameters:** layer

- an int specifying the layer to check
**Returns:** an array of Components contained in that layer

- paint

```java
public void paint​(
Graphics
g)
```

Paints this JLayeredPane within the specified graphics context.

**Overrides:** paint

in class

JComponent
**Parameters:** g

- the Graphics context within which to paint
**See Also:** JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

- getComponentToLayer

```java
protected
Hashtable
<
Component
,​
Integer
> getComponentToLayer()
```

Returns the hashtable that maps components to layers.

**Returns:** the Hashtable used to map components to their layers

- getObjectForLayer

```java
protected
Integer
getObjectForLayer​(int layer)
```

Returns the Integer object associated with a specified layer.

**Parameters:** layer

- an int specifying the layer
**Returns:** an Integer object for that layer

- insertIndexForLayer

```java
protected int insertIndexForLayer​(int layer,
int position)
```

Primitive method that determines the proper location to
insert a new child based on layer and position requests.

**Parameters:** layer

- an int specifying the layer
**Parameters:** position

- an int specifying the position within the layer
**Returns:** an int giving the (absolute) insertion-index
**See Also:** getIndexOf(java.awt.Component)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this JLayeredPane. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this JLayeredPane.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JLayeredPane.
For layered panes, the AccessibleContext takes the form of an
AccessibleJLayeredPane.
A new AccessibleJLayeredPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJLayeredPane that serves as the
AccessibleContext of this JLayeredPane

Field Detail

- DEFAULT_LAYER

```java
public static final
Integer
DEFAULT_LAYER
```

Convenience object defining the Default layer. Equivalent to Integer.valueOf(0).

- PALETTE_LAYER

```java
public static final
Integer
PALETTE_LAYER
```

Convenience object defining the Palette layer. Equivalent to Integer.valueOf(100).

- MODAL_LAYER

```java
public static final
Integer
MODAL_LAYER
```

Convenience object defining the Modal layer. Equivalent to Integer.valueOf(200).

- POPUP_LAYER

```java
public static final
Integer
POPUP_LAYER
```

Convenience object defining the Popup layer. Equivalent to Integer.valueOf(300).

- DRAG_LAYER

```java
public static final
Integer
DRAG_LAYER
```

Convenience object defining the Drag layer. Equivalent to Integer.valueOf(400).

- FRAME_CONTENT_LAYER

```java
public static final
Integer
FRAME_CONTENT_LAYER
```

Convenience object defining the Frame Content layer.
This layer is normally only use to position the contentPane and menuBar
components of JFrame.
Equivalent to Integer.valueOf(-30000).

**See Also:** JFrame

- LAYER_PROPERTY

```java
public static final
String
LAYER_PROPERTY
```

Bound property

**See Also:** Constant Field Values

---

#### Field Detail

DEFAULT_LAYER

```java
public static final
Integer
DEFAULT_LAYER
```

Convenience object defining the Default layer. Equivalent to Integer.valueOf(0).

---

#### DEFAULT_LAYER

public static final

Integer

DEFAULT_LAYER

Convenience object defining the Default layer. Equivalent to Integer.valueOf(0).

PALETTE_LAYER

```java
public static final
Integer
PALETTE_LAYER
```

Convenience object defining the Palette layer. Equivalent to Integer.valueOf(100).

---

#### PALETTE_LAYER

public static final

Integer

PALETTE_LAYER

Convenience object defining the Palette layer. Equivalent to Integer.valueOf(100).

MODAL_LAYER

```java
public static final
Integer
MODAL_LAYER
```

Convenience object defining the Modal layer. Equivalent to Integer.valueOf(200).

---

#### MODAL_LAYER

public static final

Integer

MODAL_LAYER

Convenience object defining the Modal layer. Equivalent to Integer.valueOf(200).

POPUP_LAYER

```java
public static final
Integer
POPUP_LAYER
```

Convenience object defining the Popup layer. Equivalent to Integer.valueOf(300).

---

#### POPUP_LAYER

public static final

Integer

POPUP_LAYER

Convenience object defining the Popup layer. Equivalent to Integer.valueOf(300).

DRAG_LAYER

```java
public static final
Integer
DRAG_LAYER
```

Convenience object defining the Drag layer. Equivalent to Integer.valueOf(400).

---

#### DRAG_LAYER

public static final

Integer

DRAG_LAYER

Convenience object defining the Drag layer. Equivalent to Integer.valueOf(400).

FRAME_CONTENT_LAYER

```java
public static final
Integer
FRAME_CONTENT_LAYER
```

Convenience object defining the Frame Content layer.
This layer is normally only use to position the contentPane and menuBar
components of JFrame.
Equivalent to Integer.valueOf(-30000).

**See Also:** JFrame

---

#### FRAME_CONTENT_LAYER

public static final

Integer

FRAME_CONTENT_LAYER

Convenience object defining the Frame Content layer.
This layer is normally only use to position the contentPane and menuBar
components of JFrame.
Equivalent to Integer.valueOf(-30000).

LAYER_PROPERTY

```java
public static final
String
LAYER_PROPERTY
```

Bound property

**See Also:** Constant Field Values

---

#### LAYER_PROPERTY

public static final

String

LAYER_PROPERTY

Bound property

Constructor Detail

- JLayeredPane

```java
public JLayeredPane()
```

Create a new JLayeredPane

---

#### Constructor Detail

JLayeredPane

```java
public JLayeredPane()
```

Create a new JLayeredPane

---

#### JLayeredPane

public JLayeredPane()

Create a new JLayeredPane

Method Detail

- remove

```java
public void remove​(int index)
```

Remove the indexed component from this pane.
This is the absolute index, ignoring layers.

**Overrides:** remove

in class

Container
**Parameters:** index

- an int specifying the component to remove
**See Also:** getIndexOf(java.awt.Component)

- removeAll

```java
public void removeAll()
```

Removes all the components from this container.

**Overrides:** removeAll

in class

Container
**Since:** 1.5
**See Also:** Container.add(java.awt.Component)

,

Container.remove(int)

,

Container.invalidate()

- isOptimizedDrawingEnabled

```java
@BeanProperty
(
bound
=false)
public boolean isOptimizedDrawingEnabled()
```

Returns false if components in the pane can overlap, which makes
optimized drawing impossible. Otherwise, returns true.

**Overrides:** isOptimizedDrawingEnabled

in class

JComponent
**Returns:** false if components can overlap, else true
**See Also:** JComponent.isOptimizedDrawingEnabled()

- putLayer

```java
public static void putLayer​(
JComponent
c,
int layer)
```

Sets the layer property on a JComponent. This method does not cause
any side effects like setLayer() (painting, add/remove, etc).
Normally you should use the instance method setLayer(), in order to
get the desired side-effects (like repainting).

**Parameters:** c

- the JComponent to move
**Parameters:** layer

- an int specifying the layer to move it to
**See Also:** setLayer(java.awt.Component, int)

- getLayer

```java
public static int getLayer​(
JComponent
c)
```

Gets the layer property for a JComponent, it
does not cause any side effects like setLayer(). (painting, add/remove, etc)
Normally you should use the instance method getLayer().

**Parameters:** c

- the JComponent to check
**Returns:** an int specifying the component's layer

- getLayeredPaneAbove

```java
public static
JLayeredPane
getLayeredPaneAbove​(
Component
c)
```

Convenience method that returns the first JLayeredPane which
contains the specified component. Note that all JFrames have a
JLayeredPane at their root, so any component in a JFrame will
have a JLayeredPane parent.

**Parameters:** c

- the Component to check
**Returns:** the JLayeredPane that contains the component, or
null if no JLayeredPane is found in the component
hierarchy
**See Also:** JFrame

,

JRootPane

- setLayer

```java
public void setLayer​(
Component
c,
int layer)
```

Sets the layer attribute on the specified component,
making it the bottommost component in that layer.
Should be called before adding to parent.

**Parameters:** c

- the Component to set the layer for
**Parameters:** layer

- an int specifying the layer to set, where
lower numbers are closer to the bottom

- setLayer

```java
public void setLayer​(
Component
c,
int layer,
int position)
```

Sets the layer attribute for the specified component and
also sets its position within that layer.

**Parameters:** c

- the Component to set the layer for
**Parameters:** layer

- an int specifying the layer to set, where
lower numbers are closer to the bottom
**Parameters:** position

- an int specifying the position within the
layer, where 0 is the topmost position and -1
is the bottommost position

- getLayer

```java
public int getLayer​(
Component
c)
```

Returns the layer attribute for the specified Component.

**Parameters:** c

- the Component to check
**Returns:** an int specifying the component's current layer

- getIndexOf

```java
public int getIndexOf​(
Component
c)
```

Returns the index of the specified Component.
This is the absolute index, ignoring layers.
Index numbers, like position numbers, have the topmost component
at index zero. Larger numbers are closer to the bottom.

**Parameters:** c

- the Component to check
**Returns:** an int specifying the component's index

- moveToFront

```java
public void moveToFront​(
Component
c)
```

Moves the component to the top of the components in its current layer
(position 0).

**Parameters:** c

- the Component to move
**See Also:** setPosition(Component, int)

- moveToBack

```java
public void moveToBack​(
Component
c)
```

Moves the component to the bottom of the components in its current layer
(position -1).

**Parameters:** c

- the Component to move
**See Also:** setPosition(Component, int)

- setPosition

```java
public void setPosition​(
Component
c,
int position)
```

Moves the component to

position

within its current layer,
where 0 is the topmost position within the layer and -1 is the bottommost
position.

Note:

Position numbering is defined by java.awt.Container, and
is the opposite of layer numbering. Lower position numbers are closer
to the top (0 is topmost), and higher position numbers are closer to
the bottom.

**Parameters:** c

- the Component to move
**Parameters:** position

- an int in the range -1..N-1, where N is the number of
components in the component's current layer

- getPosition

```java
public int getPosition​(
Component
c)
```

Get the relative position of the component within its layer.

**Parameters:** c

- the Component to check
**Returns:** an int giving the component's position, where 0 is the
topmost position and the highest index value = the count
count of components at that layer, minus 1
**See Also:** getComponentCountInLayer(int)

- highestLayer

```java
public int highestLayer()
```

Returns the highest layer value from all current children.
Returns 0 if there are no children.

**Returns:** an int indicating the layer of the topmost component in the
pane, or zero if there are no children

- lowestLayer

```java
public int lowestLayer()
```

Returns the lowest layer value from all current children.
Returns 0 if there are no children.

**Returns:** an int indicating the layer of the bottommost component in the
pane, or zero if there are no children

- getComponentCountInLayer

```java
public int getComponentCountInLayer​(int layer)
```

Returns the number of children currently in the specified layer.

**Parameters:** layer

- an int specifying the layer to check
**Returns:** an int specifying the number of components in that layer

- getComponentsInLayer

```java
public
Component
[] getComponentsInLayer​(int layer)
```

Returns an array of the components in the specified layer.

**Parameters:** layer

- an int specifying the layer to check
**Returns:** an array of Components contained in that layer

- paint

```java
public void paint​(
Graphics
g)
```

Paints this JLayeredPane within the specified graphics context.

**Overrides:** paint

in class

JComponent
**Parameters:** g

- the Graphics context within which to paint
**See Also:** JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

- getComponentToLayer

```java
protected
Hashtable
<
Component
,​
Integer
> getComponentToLayer()
```

Returns the hashtable that maps components to layers.

**Returns:** the Hashtable used to map components to their layers

- getObjectForLayer

```java
protected
Integer
getObjectForLayer​(int layer)
```

Returns the Integer object associated with a specified layer.

**Parameters:** layer

- an int specifying the layer
**Returns:** an Integer object for that layer

- insertIndexForLayer

```java
protected int insertIndexForLayer​(int layer,
int position)
```

Primitive method that determines the proper location to
insert a new child based on layer and position requests.

**Parameters:** layer

- an int specifying the layer
**Parameters:** position

- an int specifying the position within the layer
**Returns:** an int giving the (absolute) insertion-index
**See Also:** getIndexOf(java.awt.Component)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this JLayeredPane. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this JLayeredPane.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JLayeredPane.
For layered panes, the AccessibleContext takes the form of an
AccessibleJLayeredPane.
A new AccessibleJLayeredPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJLayeredPane that serves as the
AccessibleContext of this JLayeredPane

---

#### Method Detail

remove

```java
public void remove​(int index)
```

Remove the indexed component from this pane.
This is the absolute index, ignoring layers.

**Overrides:** remove

in class

Container
**Parameters:** index

- an int specifying the component to remove
**See Also:** getIndexOf(java.awt.Component)

---

#### remove

public void remove​(int index)

Remove the indexed component from this pane.
This is the absolute index, ignoring layers.

removeAll

```java
public void removeAll()
```

Removes all the components from this container.

**Overrides:** removeAll

in class

Container
**Since:** 1.5
**See Also:** Container.add(java.awt.Component)

,

Container.remove(int)

,

Container.invalidate()

---

#### removeAll

public void removeAll()

Removes all the components from this container.

isOptimizedDrawingEnabled

```java
@BeanProperty
(
bound
=false)
public boolean isOptimizedDrawingEnabled()
```

Returns false if components in the pane can overlap, which makes
optimized drawing impossible. Otherwise, returns true.

**Overrides:** isOptimizedDrawingEnabled

in class

JComponent
**Returns:** false if components can overlap, else true
**See Also:** JComponent.isOptimizedDrawingEnabled()

---

#### isOptimizedDrawingEnabled

@BeanProperty

(

bound

=false)
public boolean isOptimizedDrawingEnabled()

Returns false if components in the pane can overlap, which makes
optimized drawing impossible. Otherwise, returns true.

putLayer

```java
public static void putLayer​(
JComponent
c,
int layer)
```

Sets the layer property on a JComponent. This method does not cause
any side effects like setLayer() (painting, add/remove, etc).
Normally you should use the instance method setLayer(), in order to
get the desired side-effects (like repainting).

**Parameters:** c

- the JComponent to move
**Parameters:** layer

- an int specifying the layer to move it to
**See Also:** setLayer(java.awt.Component, int)

---

#### putLayer

public static void putLayer​(

JComponent

c,
int layer)

Sets the layer property on a JComponent. This method does not cause
any side effects like setLayer() (painting, add/remove, etc).
Normally you should use the instance method setLayer(), in order to
get the desired side-effects (like repainting).

getLayer

```java
public static int getLayer​(
JComponent
c)
```

Gets the layer property for a JComponent, it
does not cause any side effects like setLayer(). (painting, add/remove, etc)
Normally you should use the instance method getLayer().

**Parameters:** c

- the JComponent to check
**Returns:** an int specifying the component's layer

---

#### getLayer

public static int getLayer​(

JComponent

c)

Gets the layer property for a JComponent, it
does not cause any side effects like setLayer(). (painting, add/remove, etc)
Normally you should use the instance method getLayer().

getLayeredPaneAbove

```java
public static
JLayeredPane
getLayeredPaneAbove​(
Component
c)
```

Convenience method that returns the first JLayeredPane which
contains the specified component. Note that all JFrames have a
JLayeredPane at their root, so any component in a JFrame will
have a JLayeredPane parent.

**Parameters:** c

- the Component to check
**Returns:** the JLayeredPane that contains the component, or
null if no JLayeredPane is found in the component
hierarchy
**See Also:** JFrame

,

JRootPane

---

#### getLayeredPaneAbove

public static

JLayeredPane

getLayeredPaneAbove​(

Component

c)

Convenience method that returns the first JLayeredPane which
contains the specified component. Note that all JFrames have a
JLayeredPane at their root, so any component in a JFrame will
have a JLayeredPane parent.

setLayer

```java
public void setLayer​(
Component
c,
int layer)
```

Sets the layer attribute on the specified component,
making it the bottommost component in that layer.
Should be called before adding to parent.

**Parameters:** c

- the Component to set the layer for
**Parameters:** layer

- an int specifying the layer to set, where
lower numbers are closer to the bottom

---

#### setLayer

public void setLayer​(

Component

c,
int layer)

Sets the layer attribute on the specified component,
making it the bottommost component in that layer.
Should be called before adding to parent.

setLayer

```java
public void setLayer​(
Component
c,
int layer,
int position)
```

Sets the layer attribute for the specified component and
also sets its position within that layer.

**Parameters:** c

- the Component to set the layer for
**Parameters:** layer

- an int specifying the layer to set, where
lower numbers are closer to the bottom
**Parameters:** position

- an int specifying the position within the
layer, where 0 is the topmost position and -1
is the bottommost position

---

#### setLayer

public void setLayer​(

Component

c,
int layer,
int position)

Sets the layer attribute for the specified component and
also sets its position within that layer.

getLayer

```java
public int getLayer​(
Component
c)
```

Returns the layer attribute for the specified Component.

**Parameters:** c

- the Component to check
**Returns:** an int specifying the component's current layer

---

#### getLayer

public int getLayer​(

Component

c)

Returns the layer attribute for the specified Component.

getIndexOf

```java
public int getIndexOf​(
Component
c)
```

Returns the index of the specified Component.
This is the absolute index, ignoring layers.
Index numbers, like position numbers, have the topmost component
at index zero. Larger numbers are closer to the bottom.

**Parameters:** c

- the Component to check
**Returns:** an int specifying the component's index

---

#### getIndexOf

public int getIndexOf​(

Component

c)

Returns the index of the specified Component.
This is the absolute index, ignoring layers.
Index numbers, like position numbers, have the topmost component
at index zero. Larger numbers are closer to the bottom.

moveToFront

```java
public void moveToFront​(
Component
c)
```

Moves the component to the top of the components in its current layer
(position 0).

**Parameters:** c

- the Component to move
**See Also:** setPosition(Component, int)

---

#### moveToFront

public void moveToFront​(

Component

c)

Moves the component to the top of the components in its current layer
(position 0).

moveToBack

```java
public void moveToBack​(
Component
c)
```

Moves the component to the bottom of the components in its current layer
(position -1).

**Parameters:** c

- the Component to move
**See Also:** setPosition(Component, int)

---

#### moveToBack

public void moveToBack​(

Component

c)

Moves the component to the bottom of the components in its current layer
(position -1).

setPosition

```java
public void setPosition​(
Component
c,
int position)
```

Moves the component to

position

within its current layer,
where 0 is the topmost position within the layer and -1 is the bottommost
position.

Note:

Position numbering is defined by java.awt.Container, and
is the opposite of layer numbering. Lower position numbers are closer
to the top (0 is topmost), and higher position numbers are closer to
the bottom.

**Parameters:** c

- the Component to move
**Parameters:** position

- an int in the range -1..N-1, where N is the number of
components in the component's current layer

---

#### setPosition

public void setPosition​(

Component

c,
int position)

Moves the component to

position

within its current layer,
where 0 is the topmost position within the layer and -1 is the bottommost
position.

Note:

Position numbering is defined by java.awt.Container, and
is the opposite of layer numbering. Lower position numbers are closer
to the top (0 is topmost), and higher position numbers are closer to
the bottom.

Note:

Position numbering is defined by java.awt.Container, and
is the opposite of layer numbering. Lower position numbers are closer
to the top (0 is topmost), and higher position numbers are closer to
the bottom.

getPosition

```java
public int getPosition​(
Component
c)
```

Get the relative position of the component within its layer.

**Parameters:** c

- the Component to check
**Returns:** an int giving the component's position, where 0 is the
topmost position and the highest index value = the count
count of components at that layer, minus 1
**See Also:** getComponentCountInLayer(int)

---

#### getPosition

public int getPosition​(

Component

c)

Get the relative position of the component within its layer.

highestLayer

```java
public int highestLayer()
```

Returns the highest layer value from all current children.
Returns 0 if there are no children.

**Returns:** an int indicating the layer of the topmost component in the
pane, or zero if there are no children

---

#### highestLayer

public int highestLayer()

Returns the highest layer value from all current children.
Returns 0 if there are no children.

lowestLayer

```java
public int lowestLayer()
```

Returns the lowest layer value from all current children.
Returns 0 if there are no children.

**Returns:** an int indicating the layer of the bottommost component in the
pane, or zero if there are no children

---

#### lowestLayer

public int lowestLayer()

Returns the lowest layer value from all current children.
Returns 0 if there are no children.

getComponentCountInLayer

```java
public int getComponentCountInLayer​(int layer)
```

Returns the number of children currently in the specified layer.

**Parameters:** layer

- an int specifying the layer to check
**Returns:** an int specifying the number of components in that layer

---

#### getComponentCountInLayer

public int getComponentCountInLayer​(int layer)

Returns the number of children currently in the specified layer.

getComponentsInLayer

```java
public
Component
[] getComponentsInLayer​(int layer)
```

Returns an array of the components in the specified layer.

**Parameters:** layer

- an int specifying the layer to check
**Returns:** an array of Components contained in that layer

---

#### getComponentsInLayer

public

Component

[] getComponentsInLayer​(int layer)

Returns an array of the components in the specified layer.

paint

```java
public void paint​(
Graphics
g)
```

Paints this JLayeredPane within the specified graphics context.

**Overrides:** paint

in class

JComponent
**Parameters:** g

- the Graphics context within which to paint
**See Also:** JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

---

#### paint

public void paint​(

Graphics

g)

Paints this JLayeredPane within the specified graphics context.

getComponentToLayer

```java
protected
Hashtable
<
Component
,​
Integer
> getComponentToLayer()
```

Returns the hashtable that maps components to layers.

**Returns:** the Hashtable used to map components to their layers

---

#### getComponentToLayer

protected

Hashtable

<

Component

,​

Integer

> getComponentToLayer()

Returns the hashtable that maps components to layers.

getObjectForLayer

```java
protected
Integer
getObjectForLayer​(int layer)
```

Returns the Integer object associated with a specified layer.

**Parameters:** layer

- an int specifying the layer
**Returns:** an Integer object for that layer

---

#### getObjectForLayer

protected

Integer

getObjectForLayer​(int layer)

Returns the Integer object associated with a specified layer.

insertIndexForLayer

```java
protected int insertIndexForLayer​(int layer,
int position)
```

Primitive method that determines the proper location to
insert a new child based on layer and position requests.

**Parameters:** layer

- an int specifying the layer
**Parameters:** position

- an int specifying the position within the layer
**Returns:** an int giving the (absolute) insertion-index
**See Also:** getIndexOf(java.awt.Component)

---

#### insertIndexForLayer

protected int insertIndexForLayer​(int layer,
int position)

Primitive method that determines the proper location to
insert a new child based on layer and position requests.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this JLayeredPane. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this JLayeredPane.

---

#### paramString

protected

String

paramString()

Returns a string representation of this JLayeredPane. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JLayeredPane.
For layered panes, the AccessibleContext takes the form of an
AccessibleJLayeredPane.
A new AccessibleJLayeredPane instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJLayeredPane that serves as the
AccessibleContext of this JLayeredPane

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JLayeredPane.
For layered panes, the AccessibleContext takes the form of an
AccessibleJLayeredPane.
A new AccessibleJLayeredPane instance is created if necessary.

---

