# Interface AccessibleComponent

**Source:** `java.desktop\javax\accessibility\AccessibleComponent.html`

### Class Description

```java
public interface
AccessibleComponent
```

The

AccessibleComponent

interface should be supported by any object
that is rendered on the screen. This interface provides the standard
mechanism for an assistive technology to determine and set the graphical
representation of an object. Applications can determine if an object supports
the

AccessibleComponent

interface by first obtaining its

AccessibleContext

and then calling the

AccessibleContext.getAccessibleComponent()

method. If the return value
is not

null

, the object supports this interface.

**All Known Subinterfaces:** AccessibleExtendedComponent

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Color
getBackground()

Gets the background color of this object.

**Returns:**
- the background color, if supported, of the object; otherwise,

null

**See Also:**
- setBackground(java.awt.Color)

---

#### void setBackground​(
Color
c)

Sets the background color of this object.

**Parameters:**
- c

- the new color for the background

**See Also:**
- setBackground(java.awt.Color)

---

#### Color
getForeground()

Gets the foreground color of this object.

**Returns:**
- the foreground color, if supported, of the object; otherwise,

null

**See Also:**
- setForeground(java.awt.Color)

---

#### void setForeground​(
Color
c)

Sets the foreground color of this object.

**Parameters:**
- c

- the new color for the foreground

**See Also:**
- getForeground()

---

#### Cursor
getCursor()

Gets the cursor of this object.

**Returns:**
- the cursor, if supported, of the object; otherwise,

null

**See Also:**
- setCursor(java.awt.Cursor)

---

#### void setCursor​(
Cursor
cursor)

Sets the cursor of this object.

**Parameters:**
- cursor

- the new cursor for the object

**See Also:**
- getCursor()

---

#### Font
getFont()

Gets the font of this object.

**Returns:**
- the font, if supported, for the object; otherwise,

null

**See Also:**
- setFont(java.awt.Font)

---

#### void setFont​(
Font
f)

Sets the font of this object.

**Parameters:**
- f

- the new font for the object

**See Also:**
- getFont()

---

#### FontMetrics
getFontMetrics​(
Font
f)

Gets the

FontMetrics

of this object.

**Parameters:**
- f

- the font for which font metrics is to be obtained

**Returns:**
- the

FontMetrics

, if supported, the object; otherwise,

null

**See Also:**
- getFont()

---

#### boolean isEnabled()

Determines if the object is enabled. Objects that are enabled will also
have the

AccessibleState.ENABLED

state set in their

AccessibleStateSets

.

**Returns:**
- true

if object is enabled; otherwise,

false

**See Also:**
- setEnabled(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.ENABLED

,

AccessibleStateSet

---

#### void setEnabled​(boolean b)

Sets the enabled state of the object.

**Parameters:**
- b

- if

true

, enables this object; otherwise, disables it

**See Also:**
- isEnabled()

---

#### boolean isVisible()

Determines if the object is visible. Note: this means that the object
intends to be visible; however, it may not be showing on the screen
because one of the objects that this object is contained by is currently
not visible. To determine if an object is showing on the screen, use

isShowing()

Objects that are visible will also have the

AccessibleState.VISIBLE

state set in their

AccessibleStateSets

.

**Returns:**
- true

if object is visible; otherwise,

false

**See Also:**
- setVisible(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.VISIBLE

,

AccessibleStateSet

---

#### void setVisible​(boolean b)

Sets the visible state of the object.

**Parameters:**
- b

- if

true

, shows this object; otherwise, hides it

**See Also:**
- isVisible()

---

#### boolean isShowing()

Determines if the object is showing. This is determined by checking the
visibility of the object and its ancestors. Note: this will return

true

even if the object is obscured by another (for example, it
is underneath a menu that was pulled down).

**Returns:**
- true

if object is showing; otherwise,

false

---

#### boolean contains​(
Point
p)

Checks whether the specified point is within this object's bounds, where
the point's x and y coordinates are defined to be relative to the
coordinate system of the object.

**Parameters:**
- p

- the point relative to the coordinate system of the object

**Returns:**
- true

if object contains point; otherwise

false

**See Also:**
- getBounds()

---

#### Point
getLocationOnScreen()

Returns the location of the object on the screen.

**Returns:**
- the location of the object on screen;

null

if this object
is not on the screen

**See Also:**
- getBounds()

,

getLocation()

---

#### Point
getLocation()

Gets the location of the object relative to the parent in the form of a
point specifying the object's top-left corner in the screen's coordinate
space.

**Returns:**
- An instance of

Point

representing the top-left corner of
the object's bounds in the coordinate space of the screen;

null

if this object or its parent are not on the screen

**See Also:**
- getBounds()

,

getLocationOnScreen()

---

#### void setLocation​(
Point
p)

Sets the location of the object relative to the parent.

**Parameters:**
- p

- the new position for the top-left corner

**See Also:**
- getLocation()

---

#### Rectangle
getBounds()

Gets the bounds of this object in the form of a

Rectangle

object.
The bounds specify this object's width, height, and location relative to
its parent.

**Returns:**
- A rectangle indicating this component's bounds;

null

if
this object is not on the screen.

**See Also:**
- contains(java.awt.Point)

---

#### void setBounds​(
Rectangle
r)

Sets the bounds of this object in the form of a

Rectangle

object.
The bounds specify this object's width, height, and location relative to
its parent.

**Parameters:**
- r

- rectangle indicating this component's bounds

**See Also:**
- getBounds()

---

#### Dimension
getSize()

Returns the size of this object in the form of a

Dimension

object. The

height

field of the

Dimension

object contains
this object's height, and the

width

field of the

Dimension

object contains this object's width.

**Returns:**
- A

Dimension

object that indicates the size of this
component;

null

if this object is not on the screen

**See Also:**
- setSize(java.awt.Dimension)

---

#### void setSize​(
Dimension
d)

Resizes this object so that it has width and height.

**Parameters:**
- d

- The dimension specifying the new size of the object

**See Also:**
- getSize()

---

#### Accessible
getAccessibleAt​(
Point
p)

Returns the

Accessible

child, if one exists, contained at the
local coordinate

Point

.

**Parameters:**
- p

- The point relative to the coordinate system of this object

**Returns:**
- the

Accessible

, if it exists, at the specified location;
otherwise

null

---

#### boolean isFocusTraversable()

Returns whether this object can accept focus or not. Objects that can
accept focus will also have the

AccessibleState.FOCUSABLE

state
set in their

AccessibleStateSets

.

**Returns:**
- true

if object can accept focus; otherwise

false

**See Also:**
- AccessibleContext.getAccessibleStateSet()

,

AccessibleState.FOCUSABLE

,

AccessibleState.FOCUSED

,

AccessibleStateSet

---

#### void requestFocus()

Requests focus for this object. If this object cannot accept focus,
nothing will happen. Otherwise, the object will attempt to take focus.

**See Also:**
- isFocusTraversable()

---

#### void addFocusListener​(
FocusListener
l)

Adds the specified focus listener to receive focus events from this
component.

**Parameters:**
- l

- the focus listener

**See Also:**
- removeFocusListener(java.awt.event.FocusListener)

---

#### void removeFocusListener​(
FocusListener
l)

Removes the specified focus listener so it no longer receives focus
events from this component.

**Parameters:**
- l

- the focus listener

**See Also:**
- addFocusListener(java.awt.event.FocusListener)

---

### Additional Sections

#### Interface AccessibleComponent

**All Known Subinterfaces:** AccessibleExtendedComponent

**All Known Implementing Classes:** AbstractButton.AccessibleAbstractButton

,

Applet.AccessibleApplet

,

Box.AccessibleBox

,

Box.Filler.AccessibleBoxFiller

,

Button.AccessibleAWTButton

,

Canvas.AccessibleAWTCanvas

,

CellRendererPane.AccessibleCellRendererPane

,

Checkbox.AccessibleAWTCheckbox

,

CheckboxMenuItem.AccessibleAWTCheckboxMenuItem

,

Choice.AccessibleAWTChoice

,

Component.AccessibleAWTComponent

,

Container.AccessibleAWTContainer

,

Dialog.AccessibleAWTDialog

,

Frame.AccessibleAWTFrame

,

JApplet.AccessibleJApplet

,

JButton.AccessibleJButton

,

JCheckBox.AccessibleJCheckBox

,

JCheckBoxMenuItem.AccessibleJCheckBoxMenuItem

,

JColorChooser.AccessibleJColorChooser

,

JComboBox.AccessibleJComboBox

,

JComponent.AccessibleJComponent

,

JDesktopPane.AccessibleJDesktopPane

,

JDialog.AccessibleJDialog

,

JEditorPane.AccessibleJEditorPane

,

JEditorPane.AccessibleJEditorPaneHTML

,

JEditorPane.JEditorPaneAccessibleHypertextSupport

,

JFileChooser.AccessibleJFileChooser

,

JFrame.AccessibleJFrame

,

JInternalFrame.AccessibleJInternalFrame

,

JInternalFrame.JDesktopIcon.AccessibleJDesktopIcon

,

JLabel.AccessibleJLabel

,

JLayeredPane.AccessibleJLayeredPane

,

JList.AccessibleJList

,

JList.AccessibleJList.AccessibleJListChild

,

JMenu.AccessibleJMenu

,

JMenuBar.AccessibleJMenuBar

,

JMenuItem.AccessibleJMenuItem

,

JOptionPane.AccessibleJOptionPane

,

JPanel.AccessibleJPanel

,

JPasswordField.AccessibleJPasswordField

,

JPopupMenu.AccessibleJPopupMenu

,

JProgressBar.AccessibleJProgressBar

,

JRadioButton.AccessibleJRadioButton

,

JRadioButtonMenuItem.AccessibleJRadioButtonMenuItem

,

JRootPane.AccessibleJRootPane

,

JScrollBar.AccessibleJScrollBar

,

JScrollPane.AccessibleJScrollPane

,

JSeparator.AccessibleJSeparator

,

JSlider.AccessibleJSlider

,

JSpinner.AccessibleJSpinner

,

JSplitPane.AccessibleJSplitPane

,

JTabbedPane.AccessibleJTabbedPane

,

JTable.AccessibleJTable

,

JTable.AccessibleJTable.AccessibleJTableCell

,

JTableHeader.AccessibleJTableHeader

,

JTableHeader.AccessibleJTableHeader.AccessibleJTableHeaderEntry

,

JTextArea.AccessibleJTextArea

,

JTextComponent.AccessibleJTextComponent

,

JTextField.AccessibleJTextField

,

JToggleButton.AccessibleJToggleButton

,

JToolBar.AccessibleJToolBar

,

JToolTip.AccessibleJToolTip

,

JTree.AccessibleJTree

,

JTree.AccessibleJTree.AccessibleJTreeNode

,

JViewport.AccessibleJViewport

,

JWindow.AccessibleJWindow

,

Label.AccessibleAWTLabel

,

List.AccessibleAWTList

,

List.AccessibleAWTList.AccessibleAWTListChild

,

Menu.AccessibleAWTMenu

,

MenuBar.AccessibleAWTMenuBar

,

MenuComponent.AccessibleAWTMenuComponent

,

MenuItem.AccessibleAWTMenuItem

,

Panel.AccessibleAWTPanel

,

PopupMenu.AccessibleAWTPopupMenu

,

Scrollbar.AccessibleAWTScrollBar

,

ScrollPane.AccessibleAWTScrollPane

,

TextArea.AccessibleAWTTextArea

,

TextComponent.AccessibleAWTTextComponent

,

TextField.AccessibleAWTTextField

,

Translator

,

Window.AccessibleAWTWindow

```java
public interface
AccessibleComponent
```

The

AccessibleComponent

interface should be supported by any object
that is rendered on the screen. This interface provides the standard
mechanism for an assistive technology to determine and set the graphical
representation of an object. Applications can determine if an object supports
the

AccessibleComponent

interface by first obtaining its

AccessibleContext

and then calling the

AccessibleContext.getAccessibleComponent()

method. If the return value
is not

null

, the object supports this interface.

**See Also:** Accessible

,

Accessible.getAccessibleContext()

,

AccessibleContext

,

AccessibleContext.getAccessibleComponent()

public interface

AccessibleComponent

The

AccessibleComponent

interface should be supported by any object
that is rendered on the screen. This interface provides the standard
mechanism for an assistive technology to determine and set the graphical
representation of an object. Applications can determine if an object supports
the

AccessibleComponent

interface by first obtaining its

AccessibleContext

and then calling the

AccessibleContext.getAccessibleComponent()

method. If the return value
is not

null

, the object supports this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addFocusListener

​(

FocusListener

l)

Adds the specified focus listener to receive focus events from this
component.

boolean

contains

​(

Point

p)

Checks whether the specified point is within this object's bounds, where
the point's x and y coordinates are defined to be relative to the
coordinate system of the object.

Accessible

getAccessibleAt

​(

Point

p)

Returns the

Accessible

child, if one exists, contained at the
local coordinate

Point

.

Color

getBackground

()

Gets the background color of this object.

Rectangle

getBounds

()

Gets the bounds of this object in the form of a

Rectangle

object.

Cursor

getCursor

()

Gets the cursor of this object.

Font

getFont

()

Gets the font of this object.

FontMetrics

getFontMetrics

​(

Font

f)

Gets the

FontMetrics

of this object.

Color

getForeground

()

Gets the foreground color of this object.

Point

getLocation

()

Gets the location of the object relative to the parent in the form of a
point specifying the object's top-left corner in the screen's coordinate
space.

Point

getLocationOnScreen

()

Returns the location of the object on the screen.

Dimension

getSize

()

Returns the size of this object in the form of a

Dimension

object.

boolean

isEnabled

()

Determines if the object is enabled.

boolean

isFocusTraversable

()

Returns whether this object can accept focus or not.

boolean

isShowing

()

Determines if the object is showing.

boolean

isVisible

()

Determines if the object is visible.

void

removeFocusListener

​(

FocusListener

l)

Removes the specified focus listener so it no longer receives focus
events from this component.

void

requestFocus

()

Requests focus for this object.

void

setBackground

​(

Color

c)

Sets the background color of this object.

void

setBounds

​(

Rectangle

r)

Sets the bounds of this object in the form of a

Rectangle

object.

void

setCursor

​(

Cursor

cursor)

Sets the cursor of this object.

void

setEnabled

​(boolean b)

Sets the enabled state of the object.

void

setFont

​(

Font

f)

Sets the font of this object.

void

setForeground

​(

Color

c)

Sets the foreground color of this object.

void

setLocation

​(

Point

p)

Sets the location of the object relative to the parent.

void

setSize

​(

Dimension

d)

Resizes this object so that it has width and height.

void

setVisible

​(boolean b)

Sets the visible state of the object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addFocusListener

​(

FocusListener

l)

Adds the specified focus listener to receive focus events from this
component.

boolean

contains

​(

Point

p)

Checks whether the specified point is within this object's bounds, where
the point's x and y coordinates are defined to be relative to the
coordinate system of the object.

Accessible

getAccessibleAt

​(

Point

p)

Returns the

Accessible

child, if one exists, contained at the
local coordinate

Point

.

Color

getBackground

()

Gets the background color of this object.

Rectangle

getBounds

()

Gets the bounds of this object in the form of a

Rectangle

object.

Cursor

getCursor

()

Gets the cursor of this object.

Font

getFont

()

Gets the font of this object.

FontMetrics

getFontMetrics

​(

Font

f)

Gets the

FontMetrics

of this object.

Color

getForeground

()

Gets the foreground color of this object.

Point

getLocation

()

Gets the location of the object relative to the parent in the form of a
point specifying the object's top-left corner in the screen's coordinate
space.

Point

getLocationOnScreen

()

Returns the location of the object on the screen.

Dimension

getSize

()

Returns the size of this object in the form of a

Dimension

object.

boolean

isEnabled

()

Determines if the object is enabled.

boolean

isFocusTraversable

()

Returns whether this object can accept focus or not.

boolean

isShowing

()

Determines if the object is showing.

boolean

isVisible

()

Determines if the object is visible.

void

removeFocusListener

​(

FocusListener

l)

Removes the specified focus listener so it no longer receives focus
events from this component.

void

requestFocus

()

Requests focus for this object.

void

setBackground

​(

Color

c)

Sets the background color of this object.

void

setBounds

​(

Rectangle

r)

Sets the bounds of this object in the form of a

Rectangle

object.

void

setCursor

​(

Cursor

cursor)

Sets the cursor of this object.

void

setEnabled

​(boolean b)

Sets the enabled state of the object.

void

setFont

​(

Font

f)

Sets the font of this object.

void

setForeground

​(

Color

c)

Sets the foreground color of this object.

void

setLocation

​(

Point

p)

Sets the location of the object relative to the parent.

void

setSize

​(

Dimension

d)

Resizes this object so that it has width and height.

void

setVisible

​(boolean b)

Sets the visible state of the object.

---

#### Method Summary

Adds the specified focus listener to receive focus events from this
component.

Checks whether the specified point is within this object's bounds, where
the point's x and y coordinates are defined to be relative to the
coordinate system of the object.

Returns the

Accessible

child, if one exists, contained at the
local coordinate

Point

.

Gets the background color of this object.

Gets the bounds of this object in the form of a

Rectangle

object.

Gets the cursor of this object.

Gets the font of this object.

Gets the

FontMetrics

of this object.

Gets the foreground color of this object.

Gets the location of the object relative to the parent in the form of a
point specifying the object's top-left corner in the screen's coordinate
space.

Returns the location of the object on the screen.

Returns the size of this object in the form of a

Dimension

object.

Determines if the object is enabled.

Returns whether this object can accept focus or not.

Determines if the object is showing.

Determines if the object is visible.

Removes the specified focus listener so it no longer receives focus
events from this component.

Requests focus for this object.

Sets the background color of this object.

Sets the bounds of this object in the form of a

Rectangle

object.

Sets the cursor of this object.

Sets the enabled state of the object.

Sets the font of this object.

Sets the foreground color of this object.

Sets the location of the object relative to the parent.

Resizes this object so that it has width and height.

Sets the visible state of the object.

============ METHOD DETAIL ==========

- Method Detail

- getBackground

```java
Color
getBackground()
```

Gets the background color of this object.

**Returns:** the background color, if supported, of the object; otherwise,

null
**See Also:** setBackground(java.awt.Color)

- setBackground

```java
void setBackground​(
Color
c)
```

Sets the background color of this object.

**Parameters:** c

- the new color for the background
**See Also:** setBackground(java.awt.Color)

- getForeground

```java
Color
getForeground()
```

Gets the foreground color of this object.

**Returns:** the foreground color, if supported, of the object; otherwise,

null
**See Also:** setForeground(java.awt.Color)

- setForeground

```java
void setForeground​(
Color
c)
```

Sets the foreground color of this object.

**Parameters:** c

- the new color for the foreground
**See Also:** getForeground()

- getCursor

```java
Cursor
getCursor()
```

Gets the cursor of this object.

**Returns:** the cursor, if supported, of the object; otherwise,

null
**See Also:** setCursor(java.awt.Cursor)

- setCursor

```java
void setCursor​(
Cursor
cursor)
```

Sets the cursor of this object.

**Parameters:** cursor

- the new cursor for the object
**See Also:** getCursor()

- getFont

```java
Font
getFont()
```

Gets the font of this object.

**Returns:** the font, if supported, for the object; otherwise,

null
**See Also:** setFont(java.awt.Font)

- setFont

```java
void setFont​(
Font
f)
```

Sets the font of this object.

**Parameters:** f

- the new font for the object
**See Also:** getFont()

- getFontMetrics

```java
FontMetrics
getFontMetrics​(
Font
f)
```

Gets the

FontMetrics

of this object.

**Parameters:** f

- the font for which font metrics is to be obtained
**Returns:** the

FontMetrics

, if supported, the object; otherwise,

null
**See Also:** getFont()

- isEnabled

```java
boolean isEnabled()
```

Determines if the object is enabled. Objects that are enabled will also
have the

AccessibleState.ENABLED

state set in their

AccessibleStateSets

.

**Returns:** true

if object is enabled; otherwise,

false
**See Also:** setEnabled(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.ENABLED

,

AccessibleStateSet

- setEnabled

```java
void setEnabled​(boolean b)
```

Sets the enabled state of the object.

**Parameters:** b

- if

true

, enables this object; otherwise, disables it
**See Also:** isEnabled()

- isVisible

```java
boolean isVisible()
```

Determines if the object is visible. Note: this means that the object
intends to be visible; however, it may not be showing on the screen
because one of the objects that this object is contained by is currently
not visible. To determine if an object is showing on the screen, use

isShowing()

Objects that are visible will also have the

AccessibleState.VISIBLE

state set in their

AccessibleStateSets

.

**Returns:** true

if object is visible; otherwise,

false
**See Also:** setVisible(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.VISIBLE

,

AccessibleStateSet

- setVisible

```java
void setVisible​(boolean b)
```

Sets the visible state of the object.

**Parameters:** b

- if

true

, shows this object; otherwise, hides it
**See Also:** isVisible()

- isShowing

```java
boolean isShowing()
```

Determines if the object is showing. This is determined by checking the
visibility of the object and its ancestors. Note: this will return

true

even if the object is obscured by another (for example, it
is underneath a menu that was pulled down).

**Returns:** true

if object is showing; otherwise,

false

- contains

```java
boolean contains​(
Point
p)
```

Checks whether the specified point is within this object's bounds, where
the point's x and y coordinates are defined to be relative to the
coordinate system of the object.

**Parameters:** p

- the point relative to the coordinate system of the object
**Returns:** true

if object contains point; otherwise

false
**See Also:** getBounds()

- getLocationOnScreen

```java
Point
getLocationOnScreen()
```

Returns the location of the object on the screen.

**Returns:** the location of the object on screen;

null

if this object
is not on the screen
**See Also:** getBounds()

,

getLocation()

- getLocation

```java
Point
getLocation()
```

Gets the location of the object relative to the parent in the form of a
point specifying the object's top-left corner in the screen's coordinate
space.

**Returns:** An instance of

Point

representing the top-left corner of
the object's bounds in the coordinate space of the screen;

null

if this object or its parent are not on the screen
**See Also:** getBounds()

,

getLocationOnScreen()

- setLocation

```java
void setLocation​(
Point
p)
```

Sets the location of the object relative to the parent.

**Parameters:** p

- the new position for the top-left corner
**See Also:** getLocation()

- getBounds

```java
Rectangle
getBounds()
```

Gets the bounds of this object in the form of a

Rectangle

object.
The bounds specify this object's width, height, and location relative to
its parent.

**Returns:** A rectangle indicating this component's bounds;

null

if
this object is not on the screen.
**See Also:** contains(java.awt.Point)

- setBounds

```java
void setBounds​(
Rectangle
r)
```

Sets the bounds of this object in the form of a

Rectangle

object.
The bounds specify this object's width, height, and location relative to
its parent.

**Parameters:** r

- rectangle indicating this component's bounds
**See Also:** getBounds()

- getSize

```java
Dimension
getSize()
```

Returns the size of this object in the form of a

Dimension

object. The

height

field of the

Dimension

object contains
this object's height, and the

width

field of the

Dimension

object contains this object's width.

**Returns:** A

Dimension

object that indicates the size of this
component;

null

if this object is not on the screen
**See Also:** setSize(java.awt.Dimension)

- setSize

```java
void setSize​(
Dimension
d)
```

Resizes this object so that it has width and height.

**Parameters:** d

- The dimension specifying the new size of the object
**See Also:** getSize()

- getAccessibleAt

```java
Accessible
getAccessibleAt​(
Point
p)
```

Returns the

Accessible

child, if one exists, contained at the
local coordinate

Point

.

**Parameters:** p

- The point relative to the coordinate system of this object
**Returns:** the

Accessible

, if it exists, at the specified location;
otherwise

null

- isFocusTraversable

```java
boolean isFocusTraversable()
```

Returns whether this object can accept focus or not. Objects that can
accept focus will also have the

AccessibleState.FOCUSABLE

state
set in their

AccessibleStateSets

.

**Returns:** true

if object can accept focus; otherwise

false
**See Also:** AccessibleContext.getAccessibleStateSet()

,

AccessibleState.FOCUSABLE

,

AccessibleState.FOCUSED

,

AccessibleStateSet

- requestFocus

```java
void requestFocus()
```

Requests focus for this object. If this object cannot accept focus,
nothing will happen. Otherwise, the object will attempt to take focus.

**See Also:** isFocusTraversable()

- addFocusListener

```java
void addFocusListener​(
FocusListener
l)
```

Adds the specified focus listener to receive focus events from this
component.

**Parameters:** l

- the focus listener
**See Also:** removeFocusListener(java.awt.event.FocusListener)

- removeFocusListener

```java
void removeFocusListener​(
FocusListener
l)
```

Removes the specified focus listener so it no longer receives focus
events from this component.

**Parameters:** l

- the focus listener
**See Also:** addFocusListener(java.awt.event.FocusListener)

Method Detail

- getBackground

```java
Color
getBackground()
```

Gets the background color of this object.

**Returns:** the background color, if supported, of the object; otherwise,

null
**See Also:** setBackground(java.awt.Color)

- setBackground

```java
void setBackground​(
Color
c)
```

Sets the background color of this object.

**Parameters:** c

- the new color for the background
**See Also:** setBackground(java.awt.Color)

- getForeground

```java
Color
getForeground()
```

Gets the foreground color of this object.

**Returns:** the foreground color, if supported, of the object; otherwise,

null
**See Also:** setForeground(java.awt.Color)

- setForeground

```java
void setForeground​(
Color
c)
```

Sets the foreground color of this object.

**Parameters:** c

- the new color for the foreground
**See Also:** getForeground()

- getCursor

```java
Cursor
getCursor()
```

Gets the cursor of this object.

**Returns:** the cursor, if supported, of the object; otherwise,

null
**See Also:** setCursor(java.awt.Cursor)

- setCursor

```java
void setCursor​(
Cursor
cursor)
```

Sets the cursor of this object.

**Parameters:** cursor

- the new cursor for the object
**See Also:** getCursor()

- getFont

```java
Font
getFont()
```

Gets the font of this object.

**Returns:** the font, if supported, for the object; otherwise,

null
**See Also:** setFont(java.awt.Font)

- setFont

```java
void setFont​(
Font
f)
```

Sets the font of this object.

**Parameters:** f

- the new font for the object
**See Also:** getFont()

- getFontMetrics

```java
FontMetrics
getFontMetrics​(
Font
f)
```

Gets the

FontMetrics

of this object.

**Parameters:** f

- the font for which font metrics is to be obtained
**Returns:** the

FontMetrics

, if supported, the object; otherwise,

null
**See Also:** getFont()

- isEnabled

```java
boolean isEnabled()
```

Determines if the object is enabled. Objects that are enabled will also
have the

AccessibleState.ENABLED

state set in their

AccessibleStateSets

.

**Returns:** true

if object is enabled; otherwise,

false
**See Also:** setEnabled(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.ENABLED

,

AccessibleStateSet

- setEnabled

```java
void setEnabled​(boolean b)
```

Sets the enabled state of the object.

**Parameters:** b

- if

true

, enables this object; otherwise, disables it
**See Also:** isEnabled()

- isVisible

```java
boolean isVisible()
```

Determines if the object is visible. Note: this means that the object
intends to be visible; however, it may not be showing on the screen
because one of the objects that this object is contained by is currently
not visible. To determine if an object is showing on the screen, use

isShowing()

Objects that are visible will also have the

AccessibleState.VISIBLE

state set in their

AccessibleStateSets

.

**Returns:** true

if object is visible; otherwise,

false
**See Also:** setVisible(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.VISIBLE

,

AccessibleStateSet

- setVisible

```java
void setVisible​(boolean b)
```

Sets the visible state of the object.

**Parameters:** b

- if

true

, shows this object; otherwise, hides it
**See Also:** isVisible()

- isShowing

```java
boolean isShowing()
```

Determines if the object is showing. This is determined by checking the
visibility of the object and its ancestors. Note: this will return

true

even if the object is obscured by another (for example, it
is underneath a menu that was pulled down).

**Returns:** true

if object is showing; otherwise,

false

- contains

```java
boolean contains​(
Point
p)
```

Checks whether the specified point is within this object's bounds, where
the point's x and y coordinates are defined to be relative to the
coordinate system of the object.

**Parameters:** p

- the point relative to the coordinate system of the object
**Returns:** true

if object contains point; otherwise

false
**See Also:** getBounds()

- getLocationOnScreen

```java
Point
getLocationOnScreen()
```

Returns the location of the object on the screen.

**Returns:** the location of the object on screen;

null

if this object
is not on the screen
**See Also:** getBounds()

,

getLocation()

- getLocation

```java
Point
getLocation()
```

Gets the location of the object relative to the parent in the form of a
point specifying the object's top-left corner in the screen's coordinate
space.

**Returns:** An instance of

Point

representing the top-left corner of
the object's bounds in the coordinate space of the screen;

null

if this object or its parent are not on the screen
**See Also:** getBounds()

,

getLocationOnScreen()

- setLocation

```java
void setLocation​(
Point
p)
```

Sets the location of the object relative to the parent.

**Parameters:** p

- the new position for the top-left corner
**See Also:** getLocation()

- getBounds

```java
Rectangle
getBounds()
```

Gets the bounds of this object in the form of a

Rectangle

object.
The bounds specify this object's width, height, and location relative to
its parent.

**Returns:** A rectangle indicating this component's bounds;

null

if
this object is not on the screen.
**See Also:** contains(java.awt.Point)

- setBounds

```java
void setBounds​(
Rectangle
r)
```

Sets the bounds of this object in the form of a

Rectangle

object.
The bounds specify this object's width, height, and location relative to
its parent.

**Parameters:** r

- rectangle indicating this component's bounds
**See Also:** getBounds()

- getSize

```java
Dimension
getSize()
```

Returns the size of this object in the form of a

Dimension

object. The

height

field of the

Dimension

object contains
this object's height, and the

width

field of the

Dimension

object contains this object's width.

**Returns:** A

Dimension

object that indicates the size of this
component;

null

if this object is not on the screen
**See Also:** setSize(java.awt.Dimension)

- setSize

```java
void setSize​(
Dimension
d)
```

Resizes this object so that it has width and height.

**Parameters:** d

- The dimension specifying the new size of the object
**See Also:** getSize()

- getAccessibleAt

```java
Accessible
getAccessibleAt​(
Point
p)
```

Returns the

Accessible

child, if one exists, contained at the
local coordinate

Point

.

**Parameters:** p

- The point relative to the coordinate system of this object
**Returns:** the

Accessible

, if it exists, at the specified location;
otherwise

null

- isFocusTraversable

```java
boolean isFocusTraversable()
```

Returns whether this object can accept focus or not. Objects that can
accept focus will also have the

AccessibleState.FOCUSABLE

state
set in their

AccessibleStateSets

.

**Returns:** true

if object can accept focus; otherwise

false
**See Also:** AccessibleContext.getAccessibleStateSet()

,

AccessibleState.FOCUSABLE

,

AccessibleState.FOCUSED

,

AccessibleStateSet

- requestFocus

```java
void requestFocus()
```

Requests focus for this object. If this object cannot accept focus,
nothing will happen. Otherwise, the object will attempt to take focus.

**See Also:** isFocusTraversable()

- addFocusListener

```java
void addFocusListener​(
FocusListener
l)
```

Adds the specified focus listener to receive focus events from this
component.

**Parameters:** l

- the focus listener
**See Also:** removeFocusListener(java.awt.event.FocusListener)

- removeFocusListener

```java
void removeFocusListener​(
FocusListener
l)
```

Removes the specified focus listener so it no longer receives focus
events from this component.

**Parameters:** l

- the focus listener
**See Also:** addFocusListener(java.awt.event.FocusListener)

---

#### Method Detail

getBackground

```java
Color
getBackground()
```

Gets the background color of this object.

**Returns:** the background color, if supported, of the object; otherwise,

null
**See Also:** setBackground(java.awt.Color)

---

#### getBackground

Color

getBackground()

Gets the background color of this object.

setBackground

```java
void setBackground​(
Color
c)
```

Sets the background color of this object.

**Parameters:** c

- the new color for the background
**See Also:** setBackground(java.awt.Color)

---

#### setBackground

void setBackground​(

Color

c)

Sets the background color of this object.

getForeground

```java
Color
getForeground()
```

Gets the foreground color of this object.

**Returns:** the foreground color, if supported, of the object; otherwise,

null
**See Also:** setForeground(java.awt.Color)

---

#### getForeground

Color

getForeground()

Gets the foreground color of this object.

setForeground

```java
void setForeground​(
Color
c)
```

Sets the foreground color of this object.

**Parameters:** c

- the new color for the foreground
**See Also:** getForeground()

---

#### setForeground

void setForeground​(

Color

c)

Sets the foreground color of this object.

getCursor

```java
Cursor
getCursor()
```

Gets the cursor of this object.

**Returns:** the cursor, if supported, of the object; otherwise,

null
**See Also:** setCursor(java.awt.Cursor)

---

#### getCursor

Cursor

getCursor()

Gets the cursor of this object.

setCursor

```java
void setCursor​(
Cursor
cursor)
```

Sets the cursor of this object.

**Parameters:** cursor

- the new cursor for the object
**See Also:** getCursor()

---

#### setCursor

void setCursor​(

Cursor

cursor)

Sets the cursor of this object.

getFont

```java
Font
getFont()
```

Gets the font of this object.

**Returns:** the font, if supported, for the object; otherwise,

null
**See Also:** setFont(java.awt.Font)

---

#### getFont

Font

getFont()

Gets the font of this object.

setFont

```java
void setFont​(
Font
f)
```

Sets the font of this object.

**Parameters:** f

- the new font for the object
**See Also:** getFont()

---

#### setFont

void setFont​(

Font

f)

Sets the font of this object.

getFontMetrics

```java
FontMetrics
getFontMetrics​(
Font
f)
```

Gets the

FontMetrics

of this object.

**Parameters:** f

- the font for which font metrics is to be obtained
**Returns:** the

FontMetrics

, if supported, the object; otherwise,

null
**See Also:** getFont()

---

#### getFontMetrics

FontMetrics

getFontMetrics​(

Font

f)

Gets the

FontMetrics

of this object.

isEnabled

```java
boolean isEnabled()
```

Determines if the object is enabled. Objects that are enabled will also
have the

AccessibleState.ENABLED

state set in their

AccessibleStateSets

.

**Returns:** true

if object is enabled; otherwise,

false
**See Also:** setEnabled(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.ENABLED

,

AccessibleStateSet

---

#### isEnabled

boolean isEnabled()

Determines if the object is enabled. Objects that are enabled will also
have the

AccessibleState.ENABLED

state set in their

AccessibleStateSets

.

setEnabled

```java
void setEnabled​(boolean b)
```

Sets the enabled state of the object.

**Parameters:** b

- if

true

, enables this object; otherwise, disables it
**See Also:** isEnabled()

---

#### setEnabled

void setEnabled​(boolean b)

Sets the enabled state of the object.

isVisible

```java
boolean isVisible()
```

Determines if the object is visible. Note: this means that the object
intends to be visible; however, it may not be showing on the screen
because one of the objects that this object is contained by is currently
not visible. To determine if an object is showing on the screen, use

isShowing()

Objects that are visible will also have the

AccessibleState.VISIBLE

state set in their

AccessibleStateSets

.

**Returns:** true

if object is visible; otherwise,

false
**See Also:** setVisible(boolean)

,

AccessibleContext.getAccessibleStateSet()

,

AccessibleState.VISIBLE

,

AccessibleStateSet

---

#### isVisible

boolean isVisible()

Determines if the object is visible. Note: this means that the object
intends to be visible; however, it may not be showing on the screen
because one of the objects that this object is contained by is currently
not visible. To determine if an object is showing on the screen, use

isShowing()

Objects that are visible will also have the

AccessibleState.VISIBLE

state set in their

AccessibleStateSets

.

Objects that are visible will also have the

AccessibleState.VISIBLE

state set in their

AccessibleStateSets

.

setVisible

```java
void setVisible​(boolean b)
```

Sets the visible state of the object.

**Parameters:** b

- if

true

, shows this object; otherwise, hides it
**See Also:** isVisible()

---

#### setVisible

void setVisible​(boolean b)

Sets the visible state of the object.

isShowing

```java
boolean isShowing()
```

Determines if the object is showing. This is determined by checking the
visibility of the object and its ancestors. Note: this will return

true

even if the object is obscured by another (for example, it
is underneath a menu that was pulled down).

**Returns:** true

if object is showing; otherwise,

false

---

#### isShowing

boolean isShowing()

Determines if the object is showing. This is determined by checking the
visibility of the object and its ancestors. Note: this will return

true

even if the object is obscured by another (for example, it
is underneath a menu that was pulled down).

contains

```java
boolean contains​(
Point
p)
```

Checks whether the specified point is within this object's bounds, where
the point's x and y coordinates are defined to be relative to the
coordinate system of the object.

**Parameters:** p

- the point relative to the coordinate system of the object
**Returns:** true

if object contains point; otherwise

false
**See Also:** getBounds()

---

#### contains

boolean contains​(

Point

p)

Checks whether the specified point is within this object's bounds, where
the point's x and y coordinates are defined to be relative to the
coordinate system of the object.

getLocationOnScreen

```java
Point
getLocationOnScreen()
```

Returns the location of the object on the screen.

**Returns:** the location of the object on screen;

null

if this object
is not on the screen
**See Also:** getBounds()

,

getLocation()

---

#### getLocationOnScreen

Point

getLocationOnScreen()

Returns the location of the object on the screen.

getLocation

```java
Point
getLocation()
```

Gets the location of the object relative to the parent in the form of a
point specifying the object's top-left corner in the screen's coordinate
space.

**Returns:** An instance of

Point

representing the top-left corner of
the object's bounds in the coordinate space of the screen;

null

if this object or its parent are not on the screen
**See Also:** getBounds()

,

getLocationOnScreen()

---

#### getLocation

Point

getLocation()

Gets the location of the object relative to the parent in the form of a
point specifying the object's top-left corner in the screen's coordinate
space.

setLocation

```java
void setLocation​(
Point
p)
```

Sets the location of the object relative to the parent.

**Parameters:** p

- the new position for the top-left corner
**See Also:** getLocation()

---

#### setLocation

void setLocation​(

Point

p)

Sets the location of the object relative to the parent.

getBounds

```java
Rectangle
getBounds()
```

Gets the bounds of this object in the form of a

Rectangle

object.
The bounds specify this object's width, height, and location relative to
its parent.

**Returns:** A rectangle indicating this component's bounds;

null

if
this object is not on the screen.
**See Also:** contains(java.awt.Point)

---

#### getBounds

Rectangle

getBounds()

Gets the bounds of this object in the form of a

Rectangle

object.
The bounds specify this object's width, height, and location relative to
its parent.

setBounds

```java
void setBounds​(
Rectangle
r)
```

Sets the bounds of this object in the form of a

Rectangle

object.
The bounds specify this object's width, height, and location relative to
its parent.

**Parameters:** r

- rectangle indicating this component's bounds
**See Also:** getBounds()

---

#### setBounds

void setBounds​(

Rectangle

r)

Sets the bounds of this object in the form of a

Rectangle

object.
The bounds specify this object's width, height, and location relative to
its parent.

getSize

```java
Dimension
getSize()
```

Returns the size of this object in the form of a

Dimension

object. The

height

field of the

Dimension

object contains
this object's height, and the

width

field of the

Dimension

object contains this object's width.

**Returns:** A

Dimension

object that indicates the size of this
component;

null

if this object is not on the screen
**See Also:** setSize(java.awt.Dimension)

---

#### getSize

Dimension

getSize()

Returns the size of this object in the form of a

Dimension

object. The

height

field of the

Dimension

object contains
this object's height, and the

width

field of the

Dimension

object contains this object's width.

setSize

```java
void setSize​(
Dimension
d)
```

Resizes this object so that it has width and height.

**Parameters:** d

- The dimension specifying the new size of the object
**See Also:** getSize()

---

#### setSize

void setSize​(

Dimension

d)

Resizes this object so that it has width and height.

getAccessibleAt

```java
Accessible
getAccessibleAt​(
Point
p)
```

Returns the

Accessible

child, if one exists, contained at the
local coordinate

Point

.

**Parameters:** p

- The point relative to the coordinate system of this object
**Returns:** the

Accessible

, if it exists, at the specified location;
otherwise

null

---

#### getAccessibleAt

Accessible

getAccessibleAt​(

Point

p)

Returns the

Accessible

child, if one exists, contained at the
local coordinate

Point

.

isFocusTraversable

```java
boolean isFocusTraversable()
```

Returns whether this object can accept focus or not. Objects that can
accept focus will also have the

AccessibleState.FOCUSABLE

state
set in their

AccessibleStateSets

.

**Returns:** true

if object can accept focus; otherwise

false
**See Also:** AccessibleContext.getAccessibleStateSet()

,

AccessibleState.FOCUSABLE

,

AccessibleState.FOCUSED

,

AccessibleStateSet

---

#### isFocusTraversable

boolean isFocusTraversable()

Returns whether this object can accept focus or not. Objects that can
accept focus will also have the

AccessibleState.FOCUSABLE

state
set in their

AccessibleStateSets

.

requestFocus

```java
void requestFocus()
```

Requests focus for this object. If this object cannot accept focus,
nothing will happen. Otherwise, the object will attempt to take focus.

**See Also:** isFocusTraversable()

---

#### requestFocus

void requestFocus()

Requests focus for this object. If this object cannot accept focus,
nothing will happen. Otherwise, the object will attempt to take focus.

addFocusListener

```java
void addFocusListener​(
FocusListener
l)
```

Adds the specified focus listener to receive focus events from this
component.

**Parameters:** l

- the focus listener
**See Also:** removeFocusListener(java.awt.event.FocusListener)

---

#### addFocusListener

void addFocusListener​(

FocusListener

l)

Adds the specified focus listener to receive focus events from this
component.

removeFocusListener

```java
void removeFocusListener​(
FocusListener
l)
```

Removes the specified focus listener so it no longer receives focus
events from this component.

**Parameters:** l

- the focus listener
**See Also:** addFocusListener(java.awt.event.FocusListener)

---

#### removeFocusListener

void removeFocusListener​(

FocusListener

l)

Removes the specified focus listener so it no longer receives focus
events from this component.

---

