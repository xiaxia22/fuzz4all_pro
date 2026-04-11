# Class DefaultTreeCellRenderer

**Source:** `java.desktop\javax\swing\tree\DefaultTreeCellRenderer.html`

### Class Description

```java
public class
DefaultTreeCellRenderer

extends
JLabel

implements
TreeCellRenderer
```

Displays an entry in a tree.

DefaultTreeCellRenderer

is not opaque and
unless you subclass paint you should not change this.
See

How to Use Trees

in

The Java Tutorial

for examples of customizing node display using this class.

The set of icons and colors used by

DefaultTreeCellRenderer

can be configured using the various setter methods. The value for
each property is initialized from the defaults table. When the
look and feel changes (

updateUI

is invoked), any properties
that have a value of type

UIResource

are refreshed from the
defaults table. The following table lists the mapping between

DefaultTreeCellRenderer

property and defaults table key:

Properties

Property

Key

"leafIcon"

"Tree.leafIcon"

"closedIcon"

"Tree.closedIcon"

"openIcon"

"Tree.openIcon"

"textSelectionColor"

"Tree.selectionForeground"

"textNonSelectionColor"

"Tree.textForeground"

"backgroundSelectionColor"

"Tree.selectionBackground"

"backgroundNonSelectionColor"

"Tree.textBackground"

"borderSelectionColor"

"Tree.selectionBorderColor"

Implementation Note:

This class overrides

invalidate

,

validate

,

revalidate

,

repaint

,
and

firePropertyChange

solely to improve performance.
If not overridden, these frequently called methods would execute code paths
that are unnecessary for the default tree cell renderer.
If you write your own renderer,
take care to weigh the benefits and
drawbacks of overriding these methods.

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

,

SwingConstants

,

TreeCellRenderer

---

### Field Details

#### protected boolean selected

Is the value currently selected.

---

#### protected boolean hasFocus

True if has focus.

---

#### protected transient
Icon
closedIcon

Icon used to show non-leaf nodes that aren't expanded.

---

#### protected transient
Icon
leafIcon

Icon used to show leaf nodes.

---

#### protected transient
Icon
openIcon

Icon used to show non-leaf nodes that are expanded.

---

#### protected
Color
textSelectionColor

Color to use for the foreground for selected nodes.

---

#### protected
Color
textNonSelectionColor

Color to use for the foreground for non-selected nodes.

---

#### protected
Color
backgroundSelectionColor

Color to use for the background when a node is selected.

---

#### protected
Color
backgroundNonSelectionColor

Color to use for the background when the node isn't selected.

---

#### protected
Color
borderSelectionColor

Color to use for the focus indicator when the node has focus.

---

### Constructor Details

#### public DefaultTreeCellRenderer()

Creates a

DefaultTreeCellRenderer

. Icons and text color are
determined from the

UIManager

.

---

### Method Details

#### public void updateUI()

Resets the UI property to a value from the current look and feel.

**Overrides:**
- updateUI

in class

JLabel

**See Also:**
- JComponent.updateUI()

**Since:**
- 1.7

---

#### public
Icon
getDefaultOpenIcon()

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are expanded.

**Returns:**
- the default icon, for the current laf, that is used to
represent non-leaf nodes that are expanded.

---

#### public
Icon
getDefaultClosedIcon()

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are not expanded.

**Returns:**
- the default icon, for the current laf, that is used to
represent non-leaf nodes that are not expanded.

---

#### public
Icon
getDefaultLeafIcon()

Returns the default icon, for the current laf, that is used to
represent leaf nodes.

**Returns:**
- the default icon, for the current laf, that is used to
represent leaf nodes.

---

#### public void setOpenIcon​(
Icon
newIcon)

Sets the icon used to represent non-leaf nodes that are expanded.

**Parameters:**
- newIcon

- the icon to be used for expanded non-leaf nodes

---

#### public
Icon
getOpenIcon()

Returns the icon used to represent non-leaf nodes that are expanded.

**Returns:**
- the icon used to represent non-leaf nodes that are expanded

---

#### public void setClosedIcon​(
Icon
newIcon)

Sets the icon used to represent non-leaf nodes that are not expanded.

**Parameters:**
- newIcon

- the icon to be used for not expanded non-leaf nodes

---

#### public
Icon
getClosedIcon()

Returns the icon used to represent non-leaf nodes that are not
expanded.

**Returns:**
- the icon used to represent non-leaf nodes that are not
expanded

---

#### public void setLeafIcon​(
Icon
newIcon)

Sets the icon used to represent leaf nodes.

**Parameters:**
- newIcon

- icon to be used for leaf nodes

---

#### public
Icon
getLeafIcon()

Returns the icon used to represent leaf nodes.

**Returns:**
- the icon used to represent leaf nodes

---

#### public void setTextSelectionColor​(
Color
newColor)

Sets the color the text is drawn with when the node is selected.

**Parameters:**
- newColor

- color to be used for text when the node is selected

---

#### public
Color
getTextSelectionColor()

Returns the color the text is drawn with when the node is selected.

**Returns:**
- the color the text is drawn with when the node is selected

---

#### public void setTextNonSelectionColor​(
Color
newColor)

Sets the color the text is drawn with when the node isn't selected.

**Parameters:**
- newColor

- color to be used for text when the node isn't selected

---

#### public
Color
getTextNonSelectionColor()

Returns the color the text is drawn with when the node isn't selected.

**Returns:**
- the color the text is drawn with when the node isn't selected.

---

#### public void setBackgroundSelectionColor​(
Color
newColor)

Sets the color to use for the background if node is selected.

**Parameters:**
- newColor

- to be used for the background if the node is selected

---

#### public
Color
getBackgroundSelectionColor()

Returns the color to use for the background if node is selected.

**Returns:**
- the color to use for the background if node is selected

---

#### public void setBackgroundNonSelectionColor​(
Color
newColor)

Sets the background color to be used for non selected nodes.

**Parameters:**
- newColor

- color to be used for the background for non selected nodes

---

#### public
Color
getBackgroundNonSelectionColor()

Returns the background color to be used for non selected nodes.

**Returns:**
- the background color to be used for non selected nodes.

---

#### public void setBorderSelectionColor​(
Color
newColor)

Sets the color to use for the border.

**Parameters:**
- newColor

- color to be used for the border

---

#### public
Color
getBorderSelectionColor()

Returns the color the border is drawn.

**Returns:**
- the color the border is drawn

---

#### public void setFont​(
Font
font)

Subclassed to map

FontUIResource

s to null. If

font

is null, or a

FontUIResource

, this
has the effect of letting the font of the JTree show
through. On the other hand, if

font

is non-null, and not
a

FontUIResource

, the font becomes

font

.

**Overrides:**
- setFont

in class

JComponent

**Parameters:**
- font

- the desired

Font

for this component

**See Also:**
- Component.getFont()

---

#### public
Font
getFont()

Gets the font of this component.

**Specified by:**
- getFont

in interface

MenuContainer

**Overrides:**
- getFont

in class

Component

**Returns:**
- this component's font; if a font has not been set
for this component, the font of its parent is returned

**See Also:**
- Component.setFont(java.awt.Font)

---

#### public void setBackground​(
Color
color)

Subclassed to map

ColorUIResource

s to null. If

color

is null, or a

ColorUIResource

, this
has the effect of letting the background color of the JTree show
through. On the other hand, if

color

is non-null, and not
a

ColorUIResource

, the background becomes

color

.

**Overrides:**
- setBackground

in class

JComponent

**Parameters:**
- color

- the desired background

Color

**See Also:**
- Component.getBackground()

,

JComponent.setOpaque(boolean)

---

#### public
Component
getTreeCellRendererComponent​(
JTree
tree,

Object
value,
boolean sel,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)

Configures the renderer based on the passed in components.
The value is set from messaging the tree with

convertValueToText

, which ultimately invokes

toString

on

value

.
The foreground color is set based on the selection and the icon
is set based on the

leaf

and

expanded

parameters.

**Specified by:**
- getTreeCellRendererComponent

in interface

TreeCellRenderer

**Parameters:**
- tree

- the receiver is being configured for
- value

- the value to render
- sel

- whether node is selected
- expanded

- whether node is expanded
- leaf

- whether node is a lead node
- row

- row index
- hasFocus

- whether node has focus

**Returns:**
- the

Component

that the renderer uses to draw the value

---

#### public void paint​(
Graphics
g)

Paints the value. The background is filled based on selected.

**Overrides:**
- paint

in class

JComponent

**Parameters:**
- g

- the

Graphics

context in which to paint

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

#### public
Dimension
getPreferredSize()

Overrides

JComponent.getPreferredSize

to
return slightly wider preferred size value.

**Overrides:**
- getPreferredSize

in class

JComponent

**Returns:**
- the value of the

preferredSize

property

**See Also:**
- JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

---

#### public void validate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- validate

in class

Container

**See Also:**
- Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.isValidateRoot()

,

JComponent.revalidate()

,

Container.validateTree()

---

#### public void invalidate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- invalidate

in class

Container

**See Also:**
- Container.validate()

,

Container.layout()

,

LayoutManager2

**Since:**
- 1.5

---

#### public void revalidate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- revalidate

in class

JComponent

**See Also:**
- Component.invalidate()

,

Container.validate()

,

JComponent.isValidateRoot()

,

RepaintManager.addInvalidComponent(javax.swing.JComponent)

---

#### public void repaint​(long tm,
int x,
int y,
int width,
int height)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- repaint

in class

JComponent

**Parameters:**
- tm

- this parameter is not used
- x

- the x value of the dirty region
- y

- the y value of the dirty region
- width

- the width of the dirty region
- height

- the height of the dirty region

**See Also:**
- JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### public void repaint​(
Rectangle
r)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- repaint

in class

JComponent

**Parameters:**
- r

- a

Rectangle

containing the dirty region

**See Also:**
- JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### public void repaint()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- repaint

in class

Component

**See Also:**
- Component.update(Graphics)

**Since:**
- 1.5

---

#### protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the property whose value has changed
- oldValue

- the property's previous value
- newValue

- the property's new value

---

#### public void firePropertyChange​(
String
propertyName,
byte oldValue,
byte newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a byte)
- newValue

- the new value of the property (as a byte)

**See Also:**
- Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### public void firePropertyChange​(
String
propertyName,
char oldValue,
char newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a char)
- newValue

- the new value of the property (as a char)

**See Also:**
- Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### public void firePropertyChange​(
String
propertyName,
short oldValue,
short newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a short)
- newValue

- the new value of the property (as a short)

**See Also:**
- Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### public void firePropertyChange​(
String
propertyName,
int oldValue,
int newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

JComponent

**Parameters:**
- propertyName

- the property whose value has changed
- oldValue

- the property's previous value
- newValue

- the property's new value

---

#### public void firePropertyChange​(
String
propertyName,
long oldValue,
long newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a long)
- newValue

- the new value of the property (as a long)

**See Also:**
- Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### public void firePropertyChange​(
String
propertyName,
float oldValue,
float newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a float)
- newValue

- the new value of the property (as a float)

**See Also:**
- Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### public void firePropertyChange​(
String
propertyName,
double oldValue,
double newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the programmatic name of the property
that was changed
- oldValue

- the old value of the property (as a double)
- newValue

- the new value of the property (as a double)

**See Also:**
- Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### public void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

JComponent

**Parameters:**
- propertyName

- the property whose value has changed
- oldValue

- the property's previous value
- newValue

- the property's new value

---

### Additional Sections

#### Class DefaultTreeCellRenderer

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JLabel
- - javax.swing.tree.DefaultTreeCellRenderer

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JLabel
- - javax.swing.tree.DefaultTreeCellRenderer

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JLabel
- - javax.swing.tree.DefaultTreeCellRenderer

javax.swing.JComponent

- javax.swing.JLabel
- - javax.swing.tree.DefaultTreeCellRenderer

javax.swing.JLabel

- javax.swing.tree.DefaultTreeCellRenderer

javax.swing.tree.DefaultTreeCellRenderer

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

SwingConstants

,

TreeCellRenderer

```java
public class
DefaultTreeCellRenderer

extends
JLabel

implements
TreeCellRenderer
```

Displays an entry in a tree.

DefaultTreeCellRenderer

is not opaque and
unless you subclass paint you should not change this.
See

How to Use Trees

in

The Java Tutorial

for examples of customizing node display using this class.

The set of icons and colors used by

DefaultTreeCellRenderer

can be configured using the various setter methods. The value for
each property is initialized from the defaults table. When the
look and feel changes (

updateUI

is invoked), any properties
that have a value of type

UIResource

are refreshed from the
defaults table. The following table lists the mapping between

DefaultTreeCellRenderer

property and defaults table key:

Properties

Property

Key

"leafIcon"

"Tree.leafIcon"

"closedIcon"

"Tree.closedIcon"

"openIcon"

"Tree.openIcon"

"textSelectionColor"

"Tree.selectionForeground"

"textNonSelectionColor"

"Tree.textForeground"

"backgroundSelectionColor"

"Tree.selectionBackground"

"backgroundNonSelectionColor"

"Tree.textBackground"

"borderSelectionColor"

"Tree.selectionBorderColor"

Implementation Note:

This class overrides

invalidate

,

validate

,

revalidate

,

repaint

,
and

firePropertyChange

solely to improve performance.
If not overridden, these frequently called methods would execute code paths
that are unnecessary for the default tree cell renderer.
If you write your own renderer,
take care to weigh the benefits and
drawbacks of overriding these methods.

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

**See Also:** Serialized Form

public class

DefaultTreeCellRenderer

extends

JLabel

implements

TreeCellRenderer

Displays an entry in a tree.

DefaultTreeCellRenderer

is not opaque and
unless you subclass paint you should not change this.
See

How to Use Trees

in

The Java Tutorial

for examples of customizing node display using this class.

The set of icons and colors used by

DefaultTreeCellRenderer

can be configured using the various setter methods. The value for
each property is initialized from the defaults table. When the
look and feel changes (

updateUI

is invoked), any properties
that have a value of type

UIResource

are refreshed from the
defaults table. The following table lists the mapping between

DefaultTreeCellRenderer

property and defaults table key:

Properties

Property

Key

"leafIcon"

"Tree.leafIcon"

"closedIcon"

"Tree.closedIcon"

"openIcon"

"Tree.openIcon"

"textSelectionColor"

"Tree.selectionForeground"

"textNonSelectionColor"

"Tree.textForeground"

"backgroundSelectionColor"

"Tree.selectionBackground"

"backgroundNonSelectionColor"

"Tree.textBackground"

"borderSelectionColor"

"Tree.selectionBorderColor"

Implementation Note:

This class overrides

invalidate

,

validate

,

revalidate

,

repaint

,
and

firePropertyChange

solely to improve performance.
If not overridden, these frequently called methods would execute code paths
that are unnecessary for the default tree cell renderer.
If you write your own renderer,
take care to weigh the benefits and
drawbacks of overriding these methods.

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

The set of icons and colors used by

DefaultTreeCellRenderer

can be configured using the various setter methods. The value for
each property is initialized from the defaults table. When the
look and feel changes (

updateUI

is invoked), any properties
that have a value of type

UIResource

are refreshed from the
defaults table. The following table lists the mapping between

DefaultTreeCellRenderer

property and defaults table key:

Properties

Property

Key

"leafIcon"

"Tree.leafIcon"

"closedIcon"

"Tree.closedIcon"

"openIcon"

"Tree.openIcon"

"textSelectionColor"

"Tree.selectionForeground"

"textNonSelectionColor"

"Tree.textForeground"

"backgroundSelectionColor"

"Tree.selectionBackground"

"backgroundNonSelectionColor"

"Tree.textBackground"

"borderSelectionColor"

"Tree.selectionBorderColor"

Implementation Note:

This class overrides

invalidate

,

validate

,

revalidate

,

repaint

,
and

firePropertyChange

solely to improve performance.
If not overridden, these frequently called methods would execute code paths
that are unnecessary for the default tree cell renderer.
If you write your own renderer,
take care to weigh the benefits and
drawbacks of overriding these methods.

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

Implementation Note:

This class overrides

invalidate

,

validate

,

revalidate

,

repaint

,
and

firePropertyChange

solely to improve performance.
If not overridden, these frequently called methods would execute code paths
that are unnecessary for the default tree cell renderer.
If you write your own renderer,
take care to weigh the benefits and
drawbacks of overriding these methods.

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

- Nested classes/interfaces declared in class javax.swing.

JLabel

JLabel.AccessibleJLabel

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

protected

Color

backgroundNonSelectionColor

Color to use for the background when the node isn't selected.

protected

Color

backgroundSelectionColor

Color to use for the background when a node is selected.

protected

Color

borderSelectionColor

Color to use for the focus indicator when the node has focus.

protected

Icon

closedIcon

Icon used to show non-leaf nodes that aren't expanded.

protected boolean

hasFocus

True if has focus.

protected

Icon

leafIcon

Icon used to show leaf nodes.

protected

Icon

openIcon

Icon used to show non-leaf nodes that are expanded.

protected boolean

selected

Is the value currently selected.

protected

Color

textNonSelectionColor

Color to use for the foreground for non-selected nodes.

protected

Color

textSelectionColor

Color to use for the foreground for selected nodes.

- Fields declared in class javax.swing.

JLabel

labelFor

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

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultTreeCellRenderer

()

Creates a

DefaultTreeCellRenderer

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

firePropertyChange

​(

String

propertyName,
boolean oldValue,
boolean newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
byte oldValue,
byte newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
char oldValue,
char newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
double oldValue,
double newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
float oldValue,
float newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
int oldValue,
int newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
long oldValue,
long newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
short oldValue,
short newValue)

Overridden for performance reasons.

protected void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Overridden for performance reasons.

Color

getBackgroundNonSelectionColor

()

Returns the background color to be used for non selected nodes.

Color

getBackgroundSelectionColor

()

Returns the color to use for the background if node is selected.

Color

getBorderSelectionColor

()

Returns the color the border is drawn.

Icon

getClosedIcon

()

Returns the icon used to represent non-leaf nodes that are not
expanded.

Icon

getDefaultClosedIcon

()

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are not expanded.

Icon

getDefaultLeafIcon

()

Returns the default icon, for the current laf, that is used to
represent leaf nodes.

Icon

getDefaultOpenIcon

()

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are expanded.

Font

getFont

()

Gets the font of this component.

Icon

getLeafIcon

()

Returns the icon used to represent leaf nodes.

Icon

getOpenIcon

()

Returns the icon used to represent non-leaf nodes that are expanded.

Dimension

getPreferredSize

()

Overrides

JComponent.getPreferredSize

to
return slightly wider preferred size value.

Color

getTextNonSelectionColor

()

Returns the color the text is drawn with when the node isn't selected.

Color

getTextSelectionColor

()

Returns the color the text is drawn with when the node is selected.

Component

getTreeCellRendererComponent

​(

JTree

tree,

Object

value,
boolean sel,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)

Configures the renderer based on the passed in components.

void

invalidate

()

Overridden for performance reasons.

void

paint

​(

Graphics

g)

Paints the value.

void

repaint

()

Overridden for performance reasons.

void

repaint

​(long tm,
int x,
int y,
int width,
int height)

Overridden for performance reasons.

void

repaint

​(

Rectangle

r)

Overridden for performance reasons.

void

revalidate

()

Overridden for performance reasons.

void

setBackground

​(

Color

color)

Subclassed to map

ColorUIResource

s to null.

void

setBackgroundNonSelectionColor

​(

Color

newColor)

Sets the background color to be used for non selected nodes.

void

setBackgroundSelectionColor

​(

Color

newColor)

Sets the color to use for the background if node is selected.

void

setBorderSelectionColor

​(

Color

newColor)

Sets the color to use for the border.

void

setClosedIcon

​(

Icon

newIcon)

Sets the icon used to represent non-leaf nodes that are not expanded.

void

setFont

​(

Font

font)

Subclassed to map

FontUIResource

s to null.

void

setLeafIcon

​(

Icon

newIcon)

Sets the icon used to represent leaf nodes.

void

setOpenIcon

​(

Icon

newIcon)

Sets the icon used to represent non-leaf nodes that are expanded.

void

setTextNonSelectionColor

​(

Color

newColor)

Sets the color the text is drawn with when the node isn't selected.

void

setTextSelectionColor

​(

Color

newColor)

Sets the color the text is drawn with when the node is selected.

void

updateUI

()

Resets the UI property to a value from the current look and feel.

void

validate

()

Overridden for performance reasons.

- Methods declared in class javax.swing.

JLabel

checkHorizontalKey

,

checkVerticalKey

,

getAccessibleContext

,

getDisabledIcon

,

getDisplayedMnemonic

,

getDisplayedMnemonicIndex

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getLabelFor

,

getText

,

getUI

,

getUIClassID

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

paramString

,

setDisabledIcon

,

setDisplayedMnemonic

,

setDisplayedMnemonic

,

setDisplayedMnemonicIndex

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabelFor

,

setText

,

setUI

,

setVerticalAlignment

,

setVerticalTextPosition

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

isOptimizedDrawingEnabled

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

remove

,

removeAll

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

- Nested classes/interfaces declared in class javax.swing.

JLabel

JLabel.AccessibleJLabel

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

Nested classes/interfaces declared in class javax.swing.

JLabel

JLabel.AccessibleJLabel

---

#### Nested classes/interfaces declared in class javax.swing. JLabel

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

protected

Color

backgroundNonSelectionColor

Color to use for the background when the node isn't selected.

protected

Color

backgroundSelectionColor

Color to use for the background when a node is selected.

protected

Color

borderSelectionColor

Color to use for the focus indicator when the node has focus.

protected

Icon

closedIcon

Icon used to show non-leaf nodes that aren't expanded.

protected boolean

hasFocus

True if has focus.

protected

Icon

leafIcon

Icon used to show leaf nodes.

protected

Icon

openIcon

Icon used to show non-leaf nodes that are expanded.

protected boolean

selected

Is the value currently selected.

protected

Color

textNonSelectionColor

Color to use for the foreground for non-selected nodes.

protected

Color

textSelectionColor

Color to use for the foreground for selected nodes.

- Fields declared in class javax.swing.

JLabel

labelFor

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

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Field Summary

Color to use for the background when the node isn't selected.

Color to use for the background when a node is selected.

Color to use for the focus indicator when the node has focus.

Icon used to show non-leaf nodes that aren't expanded.

True if has focus.

Icon used to show leaf nodes.

Icon used to show non-leaf nodes that are expanded.

Is the value currently selected.

Color to use for the foreground for non-selected nodes.

Color to use for the foreground for selected nodes.

Fields declared in class javax.swing.

JLabel

labelFor

---

#### Fields declared in class javax.swing. JLabel

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

Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Fields declared in interface javax.swing. SwingConstants

Constructor Summary

Constructors

Constructor

Description

DefaultTreeCellRenderer

()

Creates a

DefaultTreeCellRenderer

.

---

#### Constructor Summary

Creates a

DefaultTreeCellRenderer

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

firePropertyChange

​(

String

propertyName,
boolean oldValue,
boolean newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
byte oldValue,
byte newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
char oldValue,
char newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
double oldValue,
double newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
float oldValue,
float newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
int oldValue,
int newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
long oldValue,
long newValue)

Overridden for performance reasons.

void

firePropertyChange

​(

String

propertyName,
short oldValue,
short newValue)

Overridden for performance reasons.

protected void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Overridden for performance reasons.

Color

getBackgroundNonSelectionColor

()

Returns the background color to be used for non selected nodes.

Color

getBackgroundSelectionColor

()

Returns the color to use for the background if node is selected.

Color

getBorderSelectionColor

()

Returns the color the border is drawn.

Icon

getClosedIcon

()

Returns the icon used to represent non-leaf nodes that are not
expanded.

Icon

getDefaultClosedIcon

()

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are not expanded.

Icon

getDefaultLeafIcon

()

Returns the default icon, for the current laf, that is used to
represent leaf nodes.

Icon

getDefaultOpenIcon

()

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are expanded.

Font

getFont

()

Gets the font of this component.

Icon

getLeafIcon

()

Returns the icon used to represent leaf nodes.

Icon

getOpenIcon

()

Returns the icon used to represent non-leaf nodes that are expanded.

Dimension

getPreferredSize

()

Overrides

JComponent.getPreferredSize

to
return slightly wider preferred size value.

Color

getTextNonSelectionColor

()

Returns the color the text is drawn with when the node isn't selected.

Color

getTextSelectionColor

()

Returns the color the text is drawn with when the node is selected.

Component

getTreeCellRendererComponent

​(

JTree

tree,

Object

value,
boolean sel,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)

Configures the renderer based on the passed in components.

void

invalidate

()

Overridden for performance reasons.

void

paint

​(

Graphics

g)

Paints the value.

void

repaint

()

Overridden for performance reasons.

void

repaint

​(long tm,
int x,
int y,
int width,
int height)

Overridden for performance reasons.

void

repaint

​(

Rectangle

r)

Overridden for performance reasons.

void

revalidate

()

Overridden for performance reasons.

void

setBackground

​(

Color

color)

Subclassed to map

ColorUIResource

s to null.

void

setBackgroundNonSelectionColor

​(

Color

newColor)

Sets the background color to be used for non selected nodes.

void

setBackgroundSelectionColor

​(

Color

newColor)

Sets the color to use for the background if node is selected.

void

setBorderSelectionColor

​(

Color

newColor)

Sets the color to use for the border.

void

setClosedIcon

​(

Icon

newIcon)

Sets the icon used to represent non-leaf nodes that are not expanded.

void

setFont

​(

Font

font)

Subclassed to map

FontUIResource

s to null.

void

setLeafIcon

​(

Icon

newIcon)

Sets the icon used to represent leaf nodes.

void

setOpenIcon

​(

Icon

newIcon)

Sets the icon used to represent non-leaf nodes that are expanded.

void

setTextNonSelectionColor

​(

Color

newColor)

Sets the color the text is drawn with when the node isn't selected.

void

setTextSelectionColor

​(

Color

newColor)

Sets the color the text is drawn with when the node is selected.

void

updateUI

()

Resets the UI property to a value from the current look and feel.

void

validate

()

Overridden for performance reasons.

- Methods declared in class javax.swing.

JLabel

checkHorizontalKey

,

checkVerticalKey

,

getAccessibleContext

,

getDisabledIcon

,

getDisplayedMnemonic

,

getDisplayedMnemonicIndex

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getLabelFor

,

getText

,

getUI

,

getUIClassID

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

paramString

,

setDisabledIcon

,

setDisplayedMnemonic

,

setDisplayedMnemonic

,

setDisplayedMnemonicIndex

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabelFor

,

setText

,

setUI

,

setVerticalAlignment

,

setVerticalTextPosition

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

isOptimizedDrawingEnabled

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

remove

,

removeAll

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

Overridden for performance reasons.

Returns the background color to be used for non selected nodes.

Returns the color to use for the background if node is selected.

Returns the color the border is drawn.

Returns the icon used to represent non-leaf nodes that are not
expanded.

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are not expanded.

Returns the default icon, for the current laf, that is used to
represent leaf nodes.

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are expanded.

Gets the font of this component.

Returns the icon used to represent leaf nodes.

Returns the icon used to represent non-leaf nodes that are expanded.

Overrides

JComponent.getPreferredSize

to
return slightly wider preferred size value.

Returns the color the text is drawn with when the node isn't selected.

Returns the color the text is drawn with when the node is selected.

Configures the renderer based on the passed in components.

Paints the value.

Subclassed to map

ColorUIResource

s to null.

Sets the background color to be used for non selected nodes.

Sets the color to use for the background if node is selected.

Sets the color to use for the border.

Sets the icon used to represent non-leaf nodes that are not expanded.

Subclassed to map

FontUIResource

s to null.

Sets the icon used to represent leaf nodes.

Sets the icon used to represent non-leaf nodes that are expanded.

Sets the color the text is drawn with when the node isn't selected.

Sets the color the text is drawn with when the node is selected.

Resets the UI property to a value from the current look and feel.

Methods declared in class javax.swing.

JLabel

checkHorizontalKey

,

checkVerticalKey

,

getAccessibleContext

,

getDisabledIcon

,

getDisplayedMnemonic

,

getDisplayedMnemonicIndex

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getLabelFor

,

getText

,

getUI

,

getUIClassID

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

paramString

,

setDisabledIcon

,

setDisplayedMnemonic

,

setDisplayedMnemonic

,

setDisplayedMnemonicIndex

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabelFor

,

setText

,

setUI

,

setVerticalAlignment

,

setVerticalTextPosition

---

#### Methods declared in class javax.swing. JLabel

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

isOptimizedDrawingEnabled

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

remove

,

removeAll

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

- selected

```java
protected boolean selected
```

Is the value currently selected.

- hasFocus

```java
protected boolean hasFocus
```

True if has focus.

- closedIcon

```java
protected transient
Icon
closedIcon
```

Icon used to show non-leaf nodes that aren't expanded.

- leafIcon

```java
protected transient
Icon
leafIcon
```

Icon used to show leaf nodes.

- openIcon

```java
protected transient
Icon
openIcon
```

Icon used to show non-leaf nodes that are expanded.

- textSelectionColor

```java
protected
Color
textSelectionColor
```

Color to use for the foreground for selected nodes.

- textNonSelectionColor

```java
protected
Color
textNonSelectionColor
```

Color to use for the foreground for non-selected nodes.

- backgroundSelectionColor

```java
protected
Color
backgroundSelectionColor
```

Color to use for the background when a node is selected.

- backgroundNonSelectionColor

```java
protected
Color
backgroundNonSelectionColor
```

Color to use for the background when the node isn't selected.

- borderSelectionColor

```java
protected
Color
borderSelectionColor
```

Color to use for the focus indicator when the node has focus.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultTreeCellRenderer

```java
public DefaultTreeCellRenderer()
```

Creates a

DefaultTreeCellRenderer

. Icons and text color are
determined from the

UIManager

.

============ METHOD DETAIL ==========

- Method Detail

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JLabel
**Since:** 1.7
**See Also:** JComponent.updateUI()

- getDefaultOpenIcon

```java
public
Icon
getDefaultOpenIcon()
```

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are expanded.

**Returns:** the default icon, for the current laf, that is used to
represent non-leaf nodes that are expanded.

- getDefaultClosedIcon

```java
public
Icon
getDefaultClosedIcon()
```

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are not expanded.

**Returns:** the default icon, for the current laf, that is used to
represent non-leaf nodes that are not expanded.

- getDefaultLeafIcon

```java
public
Icon
getDefaultLeafIcon()
```

Returns the default icon, for the current laf, that is used to
represent leaf nodes.

**Returns:** the default icon, for the current laf, that is used to
represent leaf nodes.

- setOpenIcon

```java
public void setOpenIcon​(
Icon
newIcon)
```

Sets the icon used to represent non-leaf nodes that are expanded.

**Parameters:** newIcon

- the icon to be used for expanded non-leaf nodes

- getOpenIcon

```java
public
Icon
getOpenIcon()
```

Returns the icon used to represent non-leaf nodes that are expanded.

**Returns:** the icon used to represent non-leaf nodes that are expanded

- setClosedIcon

```java
public void setClosedIcon​(
Icon
newIcon)
```

Sets the icon used to represent non-leaf nodes that are not expanded.

**Parameters:** newIcon

- the icon to be used for not expanded non-leaf nodes

- getClosedIcon

```java
public
Icon
getClosedIcon()
```

Returns the icon used to represent non-leaf nodes that are not
expanded.

**Returns:** the icon used to represent non-leaf nodes that are not
expanded

- setLeafIcon

```java
public void setLeafIcon​(
Icon
newIcon)
```

Sets the icon used to represent leaf nodes.

**Parameters:** newIcon

- icon to be used for leaf nodes

- getLeafIcon

```java
public
Icon
getLeafIcon()
```

Returns the icon used to represent leaf nodes.

**Returns:** the icon used to represent leaf nodes

- setTextSelectionColor

```java
public void setTextSelectionColor​(
Color
newColor)
```

Sets the color the text is drawn with when the node is selected.

**Parameters:** newColor

- color to be used for text when the node is selected

- getTextSelectionColor

```java
public
Color
getTextSelectionColor()
```

Returns the color the text is drawn with when the node is selected.

**Returns:** the color the text is drawn with when the node is selected

- setTextNonSelectionColor

```java
public void setTextNonSelectionColor​(
Color
newColor)
```

Sets the color the text is drawn with when the node isn't selected.

**Parameters:** newColor

- color to be used for text when the node isn't selected

- getTextNonSelectionColor

```java
public
Color
getTextNonSelectionColor()
```

Returns the color the text is drawn with when the node isn't selected.

**Returns:** the color the text is drawn with when the node isn't selected.

- setBackgroundSelectionColor

```java
public void setBackgroundSelectionColor​(
Color
newColor)
```

Sets the color to use for the background if node is selected.

**Parameters:** newColor

- to be used for the background if the node is selected

- getBackgroundSelectionColor

```java
public
Color
getBackgroundSelectionColor()
```

Returns the color to use for the background if node is selected.

**Returns:** the color to use for the background if node is selected

- setBackgroundNonSelectionColor

```java
public void setBackgroundNonSelectionColor​(
Color
newColor)
```

Sets the background color to be used for non selected nodes.

**Parameters:** newColor

- color to be used for the background for non selected nodes

- getBackgroundNonSelectionColor

```java
public
Color
getBackgroundNonSelectionColor()
```

Returns the background color to be used for non selected nodes.

**Returns:** the background color to be used for non selected nodes.

- setBorderSelectionColor

```java
public void setBorderSelectionColor​(
Color
newColor)
```

Sets the color to use for the border.

**Parameters:** newColor

- color to be used for the border

- getBorderSelectionColor

```java
public
Color
getBorderSelectionColor()
```

Returns the color the border is drawn.

**Returns:** the color the border is drawn

- setFont

```java
public void setFont​(
Font
font)
```

Subclassed to map

FontUIResource

s to null. If

font

is null, or a

FontUIResource

, this
has the effect of letting the font of the JTree show
through. On the other hand, if

font

is non-null, and not
a

FontUIResource

, the font becomes

font

.

**Overrides:** setFont

in class

JComponent
**Parameters:** font

- the desired

Font

for this component
**See Also:** Component.getFont()

- getFont

```java
public
Font
getFont()
```

Gets the font of this component.

**Specified by:** getFont

in interface

MenuContainer
**Overrides:** getFont

in class

Component
**Returns:** this component's font; if a font has not been set
for this component, the font of its parent is returned
**See Also:** Component.setFont(java.awt.Font)

- setBackground

```java
public void setBackground​(
Color
color)
```

Subclassed to map

ColorUIResource

s to null. If

color

is null, or a

ColorUIResource

, this
has the effect of letting the background color of the JTree show
through. On the other hand, if

color

is non-null, and not
a

ColorUIResource

, the background becomes

color

.

**Overrides:** setBackground

in class

JComponent
**Parameters:** color

- the desired background

Color
**See Also:** Component.getBackground()

,

JComponent.setOpaque(boolean)

- getTreeCellRendererComponent

```java
public
Component
getTreeCellRendererComponent​(
JTree
tree,

Object
value,
boolean sel,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)
```

Configures the renderer based on the passed in components.
The value is set from messaging the tree with

convertValueToText

, which ultimately invokes

toString

on

value

.
The foreground color is set based on the selection and the icon
is set based on the

leaf

and

expanded

parameters.

**Specified by:** getTreeCellRendererComponent

in interface

TreeCellRenderer
**Parameters:** tree

- the receiver is being configured for
**Parameters:** value

- the value to render
**Parameters:** sel

- whether node is selected
**Parameters:** expanded

- whether node is expanded
**Parameters:** leaf

- whether node is a lead node
**Parameters:** row

- row index
**Parameters:** hasFocus

- whether node has focus
**Returns:** the

Component

that the renderer uses to draw the value

- paint

```java
public void paint​(
Graphics
g)
```

Paints the value. The background is filled based on selected.

**Overrides:** paint

in class

JComponent
**Parameters:** g

- the

Graphics

context in which to paint
**See Also:** JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Overrides

JComponent.getPreferredSize

to
return slightly wider preferred size value.

**Overrides:** getPreferredSize

in class

JComponent
**Returns:** the value of the

preferredSize

property
**See Also:** JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

- validate

```java
public void validate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** validate

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.isValidateRoot()

,

JComponent.revalidate()

,

Container.validateTree()

- invalidate

```java
public void invalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** invalidate

in class

Container
**Since:** 1.5
**See Also:** Container.validate()

,

Container.layout()

,

LayoutManager2

- revalidate

```java
public void revalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** revalidate

in class

JComponent
**See Also:** Component.invalidate()

,

Container.validate()

,

JComponent.isValidateRoot()

,

RepaintManager.addInvalidComponent(javax.swing.JComponent)

- repaint

```java
public void repaint​(long tm,
int x,
int y,
int width,
int height)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** tm

- this parameter is not used
**Parameters:** x

- the x value of the dirty region
**Parameters:** y

- the y value of the dirty region
**Parameters:** width

- the width of the dirty region
**Parameters:** height

- the height of the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- repaint

```java
public void repaint​(
Rectangle
r)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** r

- a

Rectangle

containing the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- repaint

```java
public void repaint()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

Component
**Since:** 1.5
**See Also:** Component.update(Graphics)

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
byte oldValue,
byte newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a byte)
**Parameters:** newValue

- the new value of the property (as a byte)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
char oldValue,
char newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a char)
**Parameters:** newValue

- the new value of the property (as a char)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
short oldValue,
short newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a short)
**Parameters:** newValue

- the new value of the property (as a short)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
int oldValue,
int newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
long oldValue,
long newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a long)
**Parameters:** newValue

- the new value of the property (as a long)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
float oldValue,
float newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a float)
**Parameters:** newValue

- the new value of the property (as a float)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
double oldValue,
double newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a double)
**Parameters:** newValue

- the new value of the property (as a double)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

Field Detail

- selected

```java
protected boolean selected
```

Is the value currently selected.

- hasFocus

```java
protected boolean hasFocus
```

True if has focus.

- closedIcon

```java
protected transient
Icon
closedIcon
```

Icon used to show non-leaf nodes that aren't expanded.

- leafIcon

```java
protected transient
Icon
leafIcon
```

Icon used to show leaf nodes.

- openIcon

```java
protected transient
Icon
openIcon
```

Icon used to show non-leaf nodes that are expanded.

- textSelectionColor

```java
protected
Color
textSelectionColor
```

Color to use for the foreground for selected nodes.

- textNonSelectionColor

```java
protected
Color
textNonSelectionColor
```

Color to use for the foreground for non-selected nodes.

- backgroundSelectionColor

```java
protected
Color
backgroundSelectionColor
```

Color to use for the background when a node is selected.

- backgroundNonSelectionColor

```java
protected
Color
backgroundNonSelectionColor
```

Color to use for the background when the node isn't selected.

- borderSelectionColor

```java
protected
Color
borderSelectionColor
```

Color to use for the focus indicator when the node has focus.

---

#### Field Detail

selected

```java
protected boolean selected
```

Is the value currently selected.

---

#### selected

protected boolean selected

Is the value currently selected.

hasFocus

```java
protected boolean hasFocus
```

True if has focus.

---

#### hasFocus

protected boolean hasFocus

True if has focus.

closedIcon

```java
protected transient
Icon
closedIcon
```

Icon used to show non-leaf nodes that aren't expanded.

---

#### closedIcon

protected transient

Icon

closedIcon

Icon used to show non-leaf nodes that aren't expanded.

leafIcon

```java
protected transient
Icon
leafIcon
```

Icon used to show leaf nodes.

---

#### leafIcon

protected transient

Icon

leafIcon

Icon used to show leaf nodes.

openIcon

```java
protected transient
Icon
openIcon
```

Icon used to show non-leaf nodes that are expanded.

---

#### openIcon

protected transient

Icon

openIcon

Icon used to show non-leaf nodes that are expanded.

textSelectionColor

```java
protected
Color
textSelectionColor
```

Color to use for the foreground for selected nodes.

---

#### textSelectionColor

protected

Color

textSelectionColor

Color to use for the foreground for selected nodes.

textNonSelectionColor

```java
protected
Color
textNonSelectionColor
```

Color to use for the foreground for non-selected nodes.

---

#### textNonSelectionColor

protected

Color

textNonSelectionColor

Color to use for the foreground for non-selected nodes.

backgroundSelectionColor

```java
protected
Color
backgroundSelectionColor
```

Color to use for the background when a node is selected.

---

#### backgroundSelectionColor

protected

Color

backgroundSelectionColor

Color to use for the background when a node is selected.

backgroundNonSelectionColor

```java
protected
Color
backgroundNonSelectionColor
```

Color to use for the background when the node isn't selected.

---

#### backgroundNonSelectionColor

protected

Color

backgroundNonSelectionColor

Color to use for the background when the node isn't selected.

borderSelectionColor

```java
protected
Color
borderSelectionColor
```

Color to use for the focus indicator when the node has focus.

---

#### borderSelectionColor

protected

Color

borderSelectionColor

Color to use for the focus indicator when the node has focus.

Constructor Detail

- DefaultTreeCellRenderer

```java
public DefaultTreeCellRenderer()
```

Creates a

DefaultTreeCellRenderer

. Icons and text color are
determined from the

UIManager

.

---

#### Constructor Detail

DefaultTreeCellRenderer

```java
public DefaultTreeCellRenderer()
```

Creates a

DefaultTreeCellRenderer

. Icons and text color are
determined from the

UIManager

.

---

#### DefaultTreeCellRenderer

public DefaultTreeCellRenderer()

Creates a

DefaultTreeCellRenderer

. Icons and text color are
determined from the

UIManager

.

Method Detail

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JLabel
**Since:** 1.7
**See Also:** JComponent.updateUI()

- getDefaultOpenIcon

```java
public
Icon
getDefaultOpenIcon()
```

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are expanded.

**Returns:** the default icon, for the current laf, that is used to
represent non-leaf nodes that are expanded.

- getDefaultClosedIcon

```java
public
Icon
getDefaultClosedIcon()
```

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are not expanded.

**Returns:** the default icon, for the current laf, that is used to
represent non-leaf nodes that are not expanded.

- getDefaultLeafIcon

```java
public
Icon
getDefaultLeafIcon()
```

Returns the default icon, for the current laf, that is used to
represent leaf nodes.

**Returns:** the default icon, for the current laf, that is used to
represent leaf nodes.

- setOpenIcon

```java
public void setOpenIcon​(
Icon
newIcon)
```

Sets the icon used to represent non-leaf nodes that are expanded.

**Parameters:** newIcon

- the icon to be used for expanded non-leaf nodes

- getOpenIcon

```java
public
Icon
getOpenIcon()
```

Returns the icon used to represent non-leaf nodes that are expanded.

**Returns:** the icon used to represent non-leaf nodes that are expanded

- setClosedIcon

```java
public void setClosedIcon​(
Icon
newIcon)
```

Sets the icon used to represent non-leaf nodes that are not expanded.

**Parameters:** newIcon

- the icon to be used for not expanded non-leaf nodes

- getClosedIcon

```java
public
Icon
getClosedIcon()
```

Returns the icon used to represent non-leaf nodes that are not
expanded.

**Returns:** the icon used to represent non-leaf nodes that are not
expanded

- setLeafIcon

```java
public void setLeafIcon​(
Icon
newIcon)
```

Sets the icon used to represent leaf nodes.

**Parameters:** newIcon

- icon to be used for leaf nodes

- getLeafIcon

```java
public
Icon
getLeafIcon()
```

Returns the icon used to represent leaf nodes.

**Returns:** the icon used to represent leaf nodes

- setTextSelectionColor

```java
public void setTextSelectionColor​(
Color
newColor)
```

Sets the color the text is drawn with when the node is selected.

**Parameters:** newColor

- color to be used for text when the node is selected

- getTextSelectionColor

```java
public
Color
getTextSelectionColor()
```

Returns the color the text is drawn with when the node is selected.

**Returns:** the color the text is drawn with when the node is selected

- setTextNonSelectionColor

```java
public void setTextNonSelectionColor​(
Color
newColor)
```

Sets the color the text is drawn with when the node isn't selected.

**Parameters:** newColor

- color to be used for text when the node isn't selected

- getTextNonSelectionColor

```java
public
Color
getTextNonSelectionColor()
```

Returns the color the text is drawn with when the node isn't selected.

**Returns:** the color the text is drawn with when the node isn't selected.

- setBackgroundSelectionColor

```java
public void setBackgroundSelectionColor​(
Color
newColor)
```

Sets the color to use for the background if node is selected.

**Parameters:** newColor

- to be used for the background if the node is selected

- getBackgroundSelectionColor

```java
public
Color
getBackgroundSelectionColor()
```

Returns the color to use for the background if node is selected.

**Returns:** the color to use for the background if node is selected

- setBackgroundNonSelectionColor

```java
public void setBackgroundNonSelectionColor​(
Color
newColor)
```

Sets the background color to be used for non selected nodes.

**Parameters:** newColor

- color to be used for the background for non selected nodes

- getBackgroundNonSelectionColor

```java
public
Color
getBackgroundNonSelectionColor()
```

Returns the background color to be used for non selected nodes.

**Returns:** the background color to be used for non selected nodes.

- setBorderSelectionColor

```java
public void setBorderSelectionColor​(
Color
newColor)
```

Sets the color to use for the border.

**Parameters:** newColor

- color to be used for the border

- getBorderSelectionColor

```java
public
Color
getBorderSelectionColor()
```

Returns the color the border is drawn.

**Returns:** the color the border is drawn

- setFont

```java
public void setFont​(
Font
font)
```

Subclassed to map

FontUIResource

s to null. If

font

is null, or a

FontUIResource

, this
has the effect of letting the font of the JTree show
through. On the other hand, if

font

is non-null, and not
a

FontUIResource

, the font becomes

font

.

**Overrides:** setFont

in class

JComponent
**Parameters:** font

- the desired

Font

for this component
**See Also:** Component.getFont()

- getFont

```java
public
Font
getFont()
```

Gets the font of this component.

**Specified by:** getFont

in interface

MenuContainer
**Overrides:** getFont

in class

Component
**Returns:** this component's font; if a font has not been set
for this component, the font of its parent is returned
**See Also:** Component.setFont(java.awt.Font)

- setBackground

```java
public void setBackground​(
Color
color)
```

Subclassed to map

ColorUIResource

s to null. If

color

is null, or a

ColorUIResource

, this
has the effect of letting the background color of the JTree show
through. On the other hand, if

color

is non-null, and not
a

ColorUIResource

, the background becomes

color

.

**Overrides:** setBackground

in class

JComponent
**Parameters:** color

- the desired background

Color
**See Also:** Component.getBackground()

,

JComponent.setOpaque(boolean)

- getTreeCellRendererComponent

```java
public
Component
getTreeCellRendererComponent​(
JTree
tree,

Object
value,
boolean sel,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)
```

Configures the renderer based on the passed in components.
The value is set from messaging the tree with

convertValueToText

, which ultimately invokes

toString

on

value

.
The foreground color is set based on the selection and the icon
is set based on the

leaf

and

expanded

parameters.

**Specified by:** getTreeCellRendererComponent

in interface

TreeCellRenderer
**Parameters:** tree

- the receiver is being configured for
**Parameters:** value

- the value to render
**Parameters:** sel

- whether node is selected
**Parameters:** expanded

- whether node is expanded
**Parameters:** leaf

- whether node is a lead node
**Parameters:** row

- row index
**Parameters:** hasFocus

- whether node has focus
**Returns:** the

Component

that the renderer uses to draw the value

- paint

```java
public void paint​(
Graphics
g)
```

Paints the value. The background is filled based on selected.

**Overrides:** paint

in class

JComponent
**Parameters:** g

- the

Graphics

context in which to paint
**See Also:** JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Overrides

JComponent.getPreferredSize

to
return slightly wider preferred size value.

**Overrides:** getPreferredSize

in class

JComponent
**Returns:** the value of the

preferredSize

property
**See Also:** JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

- validate

```java
public void validate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** validate

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.isValidateRoot()

,

JComponent.revalidate()

,

Container.validateTree()

- invalidate

```java
public void invalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** invalidate

in class

Container
**Since:** 1.5
**See Also:** Container.validate()

,

Container.layout()

,

LayoutManager2

- revalidate

```java
public void revalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** revalidate

in class

JComponent
**See Also:** Component.invalidate()

,

Container.validate()

,

JComponent.isValidateRoot()

,

RepaintManager.addInvalidComponent(javax.swing.JComponent)

- repaint

```java
public void repaint​(long tm,
int x,
int y,
int width,
int height)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** tm

- this parameter is not used
**Parameters:** x

- the x value of the dirty region
**Parameters:** y

- the y value of the dirty region
**Parameters:** width

- the width of the dirty region
**Parameters:** height

- the height of the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- repaint

```java
public void repaint​(
Rectangle
r)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** r

- a

Rectangle

containing the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- repaint

```java
public void repaint()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

Component
**Since:** 1.5
**See Also:** Component.update(Graphics)

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
byte oldValue,
byte newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a byte)
**Parameters:** newValue

- the new value of the property (as a byte)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
char oldValue,
char newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a char)
**Parameters:** newValue

- the new value of the property (as a char)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
short oldValue,
short newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a short)
**Parameters:** newValue

- the new value of the property (as a short)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
int oldValue,
int newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
long oldValue,
long newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a long)
**Parameters:** newValue

- the new value of the property (as a long)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
float oldValue,
float newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a float)
**Parameters:** newValue

- the new value of the property (as a float)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
double oldValue,
double newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a double)
**Parameters:** newValue

- the new value of the property (as a double)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

---

#### Method Detail

updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JLabel
**Since:** 1.7
**See Also:** JComponent.updateUI()

---

#### updateUI

public void updateUI()

Resets the UI property to a value from the current look and feel.

getDefaultOpenIcon

```java
public
Icon
getDefaultOpenIcon()
```

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are expanded.

**Returns:** the default icon, for the current laf, that is used to
represent non-leaf nodes that are expanded.

---

#### getDefaultOpenIcon

public

Icon

getDefaultOpenIcon()

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are expanded.

getDefaultClosedIcon

```java
public
Icon
getDefaultClosedIcon()
```

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are not expanded.

**Returns:** the default icon, for the current laf, that is used to
represent non-leaf nodes that are not expanded.

---

#### getDefaultClosedIcon

public

Icon

getDefaultClosedIcon()

Returns the default icon, for the current laf, that is used to
represent non-leaf nodes that are not expanded.

getDefaultLeafIcon

```java
public
Icon
getDefaultLeafIcon()
```

Returns the default icon, for the current laf, that is used to
represent leaf nodes.

**Returns:** the default icon, for the current laf, that is used to
represent leaf nodes.

---

#### getDefaultLeafIcon

public

Icon

getDefaultLeafIcon()

Returns the default icon, for the current laf, that is used to
represent leaf nodes.

setOpenIcon

```java
public void setOpenIcon​(
Icon
newIcon)
```

Sets the icon used to represent non-leaf nodes that are expanded.

**Parameters:** newIcon

- the icon to be used for expanded non-leaf nodes

---

#### setOpenIcon

public void setOpenIcon​(

Icon

newIcon)

Sets the icon used to represent non-leaf nodes that are expanded.

getOpenIcon

```java
public
Icon
getOpenIcon()
```

Returns the icon used to represent non-leaf nodes that are expanded.

**Returns:** the icon used to represent non-leaf nodes that are expanded

---

#### getOpenIcon

public

Icon

getOpenIcon()

Returns the icon used to represent non-leaf nodes that are expanded.

setClosedIcon

```java
public void setClosedIcon​(
Icon
newIcon)
```

Sets the icon used to represent non-leaf nodes that are not expanded.

**Parameters:** newIcon

- the icon to be used for not expanded non-leaf nodes

---

#### setClosedIcon

public void setClosedIcon​(

Icon

newIcon)

Sets the icon used to represent non-leaf nodes that are not expanded.

getClosedIcon

```java
public
Icon
getClosedIcon()
```

Returns the icon used to represent non-leaf nodes that are not
expanded.

**Returns:** the icon used to represent non-leaf nodes that are not
expanded

---

#### getClosedIcon

public

Icon

getClosedIcon()

Returns the icon used to represent non-leaf nodes that are not
expanded.

setLeafIcon

```java
public void setLeafIcon​(
Icon
newIcon)
```

Sets the icon used to represent leaf nodes.

**Parameters:** newIcon

- icon to be used for leaf nodes

---

#### setLeafIcon

public void setLeafIcon​(

Icon

newIcon)

Sets the icon used to represent leaf nodes.

getLeafIcon

```java
public
Icon
getLeafIcon()
```

Returns the icon used to represent leaf nodes.

**Returns:** the icon used to represent leaf nodes

---

#### getLeafIcon

public

Icon

getLeafIcon()

Returns the icon used to represent leaf nodes.

setTextSelectionColor

```java
public void setTextSelectionColor​(
Color
newColor)
```

Sets the color the text is drawn with when the node is selected.

**Parameters:** newColor

- color to be used for text when the node is selected

---

#### setTextSelectionColor

public void setTextSelectionColor​(

Color

newColor)

Sets the color the text is drawn with when the node is selected.

getTextSelectionColor

```java
public
Color
getTextSelectionColor()
```

Returns the color the text is drawn with when the node is selected.

**Returns:** the color the text is drawn with when the node is selected

---

#### getTextSelectionColor

public

Color

getTextSelectionColor()

Returns the color the text is drawn with when the node is selected.

setTextNonSelectionColor

```java
public void setTextNonSelectionColor​(
Color
newColor)
```

Sets the color the text is drawn with when the node isn't selected.

**Parameters:** newColor

- color to be used for text when the node isn't selected

---

#### setTextNonSelectionColor

public void setTextNonSelectionColor​(

Color

newColor)

Sets the color the text is drawn with when the node isn't selected.

getTextNonSelectionColor

```java
public
Color
getTextNonSelectionColor()
```

Returns the color the text is drawn with when the node isn't selected.

**Returns:** the color the text is drawn with when the node isn't selected.

---

#### getTextNonSelectionColor

public

Color

getTextNonSelectionColor()

Returns the color the text is drawn with when the node isn't selected.

setBackgroundSelectionColor

```java
public void setBackgroundSelectionColor​(
Color
newColor)
```

Sets the color to use for the background if node is selected.

**Parameters:** newColor

- to be used for the background if the node is selected

---

#### setBackgroundSelectionColor

public void setBackgroundSelectionColor​(

Color

newColor)

Sets the color to use for the background if node is selected.

getBackgroundSelectionColor

```java
public
Color
getBackgroundSelectionColor()
```

Returns the color to use for the background if node is selected.

**Returns:** the color to use for the background if node is selected

---

#### getBackgroundSelectionColor

public

Color

getBackgroundSelectionColor()

Returns the color to use for the background if node is selected.

setBackgroundNonSelectionColor

```java
public void setBackgroundNonSelectionColor​(
Color
newColor)
```

Sets the background color to be used for non selected nodes.

**Parameters:** newColor

- color to be used for the background for non selected nodes

---

#### setBackgroundNonSelectionColor

public void setBackgroundNonSelectionColor​(

Color

newColor)

Sets the background color to be used for non selected nodes.

getBackgroundNonSelectionColor

```java
public
Color
getBackgroundNonSelectionColor()
```

Returns the background color to be used for non selected nodes.

**Returns:** the background color to be used for non selected nodes.

---

#### getBackgroundNonSelectionColor

public

Color

getBackgroundNonSelectionColor()

Returns the background color to be used for non selected nodes.

setBorderSelectionColor

```java
public void setBorderSelectionColor​(
Color
newColor)
```

Sets the color to use for the border.

**Parameters:** newColor

- color to be used for the border

---

#### setBorderSelectionColor

public void setBorderSelectionColor​(

Color

newColor)

Sets the color to use for the border.

getBorderSelectionColor

```java
public
Color
getBorderSelectionColor()
```

Returns the color the border is drawn.

**Returns:** the color the border is drawn

---

#### getBorderSelectionColor

public

Color

getBorderSelectionColor()

Returns the color the border is drawn.

setFont

```java
public void setFont​(
Font
font)
```

Subclassed to map

FontUIResource

s to null. If

font

is null, or a

FontUIResource

, this
has the effect of letting the font of the JTree show
through. On the other hand, if

font

is non-null, and not
a

FontUIResource

, the font becomes

font

.

**Overrides:** setFont

in class

JComponent
**Parameters:** font

- the desired

Font

for this component
**See Also:** Component.getFont()

---

#### setFont

public void setFont​(

Font

font)

Subclassed to map

FontUIResource

s to null. If

font

is null, or a

FontUIResource

, this
has the effect of letting the font of the JTree show
through. On the other hand, if

font

is non-null, and not
a

FontUIResource

, the font becomes

font

.

getFont

```java
public
Font
getFont()
```

Gets the font of this component.

**Specified by:** getFont

in interface

MenuContainer
**Overrides:** getFont

in class

Component
**Returns:** this component's font; if a font has not been set
for this component, the font of its parent is returned
**See Also:** Component.setFont(java.awt.Font)

---

#### getFont

public

Font

getFont()

Gets the font of this component.

setBackground

```java
public void setBackground​(
Color
color)
```

Subclassed to map

ColorUIResource

s to null. If

color

is null, or a

ColorUIResource

, this
has the effect of letting the background color of the JTree show
through. On the other hand, if

color

is non-null, and not
a

ColorUIResource

, the background becomes

color

.

**Overrides:** setBackground

in class

JComponent
**Parameters:** color

- the desired background

Color
**See Also:** Component.getBackground()

,

JComponent.setOpaque(boolean)

---

#### setBackground

public void setBackground​(

Color

color)

Subclassed to map

ColorUIResource

s to null. If

color

is null, or a

ColorUIResource

, this
has the effect of letting the background color of the JTree show
through. On the other hand, if

color

is non-null, and not
a

ColorUIResource

, the background becomes

color

.

getTreeCellRendererComponent

```java
public
Component
getTreeCellRendererComponent​(
JTree
tree,

Object
value,
boolean sel,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)
```

Configures the renderer based on the passed in components.
The value is set from messaging the tree with

convertValueToText

, which ultimately invokes

toString

on

value

.
The foreground color is set based on the selection and the icon
is set based on the

leaf

and

expanded

parameters.

**Specified by:** getTreeCellRendererComponent

in interface

TreeCellRenderer
**Parameters:** tree

- the receiver is being configured for
**Parameters:** value

- the value to render
**Parameters:** sel

- whether node is selected
**Parameters:** expanded

- whether node is expanded
**Parameters:** leaf

- whether node is a lead node
**Parameters:** row

- row index
**Parameters:** hasFocus

- whether node has focus
**Returns:** the

Component

that the renderer uses to draw the value

---

#### getTreeCellRendererComponent

public

Component

getTreeCellRendererComponent​(

JTree

tree,

Object

value,
boolean sel,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)

Configures the renderer based on the passed in components.
The value is set from messaging the tree with

convertValueToText

, which ultimately invokes

toString

on

value

.
The foreground color is set based on the selection and the icon
is set based on the

leaf

and

expanded

parameters.

paint

```java
public void paint​(
Graphics
g)
```

Paints the value. The background is filled based on selected.

**Overrides:** paint

in class

JComponent
**Parameters:** g

- the

Graphics

context in which to paint
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

Paints the value. The background is filled based on selected.

getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Overrides

JComponent.getPreferredSize

to
return slightly wider preferred size value.

**Overrides:** getPreferredSize

in class

JComponent
**Returns:** the value of the

preferredSize

property
**See Also:** JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

---

#### getPreferredSize

public

Dimension

getPreferredSize()

Overrides

JComponent.getPreferredSize

to
return slightly wider preferred size value.

validate

```java
public void validate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** validate

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.isValidateRoot()

,

JComponent.revalidate()

,

Container.validateTree()

---

#### validate

public void validate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

invalidate

```java
public void invalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** invalidate

in class

Container
**Since:** 1.5
**See Also:** Container.validate()

,

Container.layout()

,

LayoutManager2

---

#### invalidate

public void invalidate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

revalidate

```java
public void revalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** revalidate

in class

JComponent
**See Also:** Component.invalidate()

,

Container.validate()

,

JComponent.isValidateRoot()

,

RepaintManager.addInvalidComponent(javax.swing.JComponent)

---

#### revalidate

public void revalidate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

repaint

```java
public void repaint​(long tm,
int x,
int y,
int width,
int height)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** tm

- this parameter is not used
**Parameters:** x

- the x value of the dirty region
**Parameters:** y

- the y value of the dirty region
**Parameters:** width

- the width of the dirty region
**Parameters:** height

- the height of the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### repaint

public void repaint​(long tm,
int x,
int y,
int width,
int height)

Overridden for performance reasons.
See the

Implementation Note

for more information.

repaint

```java
public void repaint​(
Rectangle
r)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** r

- a

Rectangle

containing the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### repaint

public void repaint​(

Rectangle

r)

Overridden for performance reasons.
See the

Implementation Note

for more information.

repaint

```java
public void repaint()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

Component
**Since:** 1.5
**See Also:** Component.update(Graphics)

---

#### repaint

public void repaint()

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

---

#### firePropertyChange

protected void firePropertyChange​(

String

propertyName,

Object

oldValue,

Object

newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
byte oldValue,
byte newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a byte)
**Parameters:** newValue

- the new value of the property (as a byte)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
byte oldValue,
byte newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
char oldValue,
char newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a char)
**Parameters:** newValue

- the new value of the property (as a char)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
char oldValue,
char newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
short oldValue,
short newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a short)
**Parameters:** newValue

- the new value of the property (as a short)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
short oldValue,
short newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
int oldValue,
int newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
int oldValue,
int newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
long oldValue,
long newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a long)
**Parameters:** newValue

- the new value of the property (as a long)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
long oldValue,
long newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
float oldValue,
float newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a float)
**Parameters:** newValue

- the new value of the property (as a float)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
float oldValue,
float newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
double oldValue,
double newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the programmatic name of the property
that was changed
**Parameters:** oldValue

- the old value of the property (as a double)
**Parameters:** newValue

- the new value of the property (as a double)
**See Also:** Component.firePropertyChange(java.lang.String, java.lang.Object,
java.lang.Object)

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
double oldValue,
double newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
boolean oldValue,
boolean newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

---

