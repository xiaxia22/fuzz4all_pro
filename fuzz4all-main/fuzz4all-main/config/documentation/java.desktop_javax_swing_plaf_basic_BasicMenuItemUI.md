# Class BasicMenuItemUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicMenuItemUI.html`

### Class Description

```java
public class
BasicMenuItemUI

extends
MenuItemUI
```

BasicMenuItem implementation

**Direct Known Subclasses:** BasicCheckBoxMenuItemUI

,

BasicMenuUI

,

BasicRadioButtonMenuItemUI

,

SynthMenuItemUI

---

### Field Details

#### protected
JMenuItem
menuItem

The instance of

JMenuItem

.

---

#### protected
Color
selectionBackground

The color of the selection background.

---

#### protected
Color
selectionForeground

The color of the selection foreground.

---

#### protected
Color
disabledForeground

The color of the disabled foreground.

---

#### protected
Color
acceleratorForeground

The color of the accelerator foreground.

---

#### protected
Color
acceleratorSelectionForeground

The color of the accelerator selection.

---

#### protected
String
acceleratorDelimiter

Accelerator delimiter string, such as

'+'

in

'Ctrl+C'

.

**Since:**
- 1.7

---

#### protected int defaultTextIconGap

The gap between the text and the icon.

---

#### protected
Font
acceleratorFont

The accelerator font.

---

#### protected
MouseInputListener
mouseInputListener

The instance of

MouseInputListener

.

---

#### protected
MenuDragMouseListener
menuDragMouseListener

The instance of

MenuDragMouseListener

.

---

#### protected
MenuKeyListener
menuKeyListener

The instance of

MenuKeyListener

.

---

#### protected
PropertyChangeListener
propertyChangeListener

PropertyChangeListener

returned from

createPropertyChangeListener

. You should not
need to access this field, rather if you want to customize the

PropertyChangeListener

override

createPropertyChangeListener

.

**See Also:**
- createPropertyChangeListener(javax.swing.JComponent)

**Since:**
- 1.6

---

#### protected
Icon
arrowIcon

The arrow icon.

---

#### protected
Icon
checkIcon

The check icon.

---

#### protected boolean oldBorderPainted

The value represents if the old border is painted.

---

### Constructor Details

#### public BasicMenuItemUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Returns a new instance of

BasicMenuItemUI

.

**Parameters:**
- c

- a component

**Returns:**
- a new instance of

BasicMenuItemUI

---

#### protected void installDefaults()

Installs default properties.

---

#### protected void installComponents​(
JMenuItem
menuItem)

**Parameters:**
- menuItem

- a menu item

**Since:**
- 1.3

---

#### protected
String
getPropertyPrefix()

Returns a property prefix.

**Returns:**
- a property prefix

---

#### protected void installListeners()

Registers listeners.

---

#### protected void installKeyboardActions()

Registers keyboard action.

---

#### protected void uninstallDefaults()

Uninstalls default properties.

---

#### protected void uninstallComponents​(
JMenuItem
menuItem)

Unregisters components.

**Parameters:**
- menuItem

- a menu item

**Since:**
- 1.3

---

#### protected void uninstallListeners()

Unregisters listeners.

---

#### protected void uninstallKeyboardActions()

Unregisters keyboard actions.

---

#### protected
MouseInputListener
createMouseInputListener​(
JComponent
c)

Returns an instance of

MouseInputListener

.

**Parameters:**
- c

- a component

**Returns:**
- an instance of

MouseInputListener

---

#### protected
MenuDragMouseListener
createMenuDragMouseListener​(
JComponent
c)

Returns an instance of

MenuDragMouseListener

.

**Parameters:**
- c

- a component

**Returns:**
- an instance of

MenuDragMouseListener

---

#### protected
MenuKeyListener
createMenuKeyListener​(
JComponent
c)

Returns an instance of

MenuKeyListener

.

**Parameters:**
- c

- a component

**Returns:**
- an instance of

MenuKeyListener

---

#### protected
PropertyChangeListener
createPropertyChangeListener​(
JComponent
c)

Creates a

PropertyChangeListener

which will be added to
the menu item.
If this method returns null then it will not be added to the menu item.

**Parameters:**
- c

- a component

**Returns:**
- an instance of a

PropertyChangeListener

or null

**Since:**
- 1.6

---

#### protected
Dimension
getPreferredMenuItemSize​(
JComponent
c,

Icon
checkIcon,

Icon
arrowIcon,
int defaultTextIconGap)

Returns the preferred size of a menu item.

**Parameters:**
- c

- a component
- checkIcon

- a check icon
- arrowIcon

- an arrow icon
- defaultTextIconGap

- a gap between a text and an icon

**Returns:**
- the preferred size of a menu item

---

#### public void update​(
Graphics
g,

JComponent
c)

We draw the background in paintMenuItem()
so override update (which fills the background of opaque
components by default) to just call paint().

**Overrides:**
- update

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

context in which to paint
- c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**See Also:**
- ComponentUI.paint(java.awt.Graphics, javax.swing.JComponent)

,

JComponent.paintComponent(java.awt.Graphics)

---

#### protected void paintMenuItem​(
Graphics
g,

JComponent
c,

Icon
checkIcon,

Icon
arrowIcon,

Color
background,

Color
foreground,
int defaultTextIconGap)

Paints a menu item.

**Parameters:**
- g

- an instance of

Graphics
- c

- a component
- checkIcon

- a check icon
- arrowIcon

- an arrow icon
- background

- a background color
- foreground

- a foreground color
- defaultTextIconGap

- a gap between a text and an icon

---

#### protected void paintBackground​(
Graphics
g,

JMenuItem
menuItem,

Color
bgColor)

Draws the background of the menu item.

**Parameters:**
- g

- the paint graphics
- menuItem

- menu item to be painted
- bgColor

- selection background color

**Since:**
- 1.4

---

#### protected void paintText​(
Graphics
g,

JMenuItem
menuItem,

Rectangle
textRect,

String
text)

Renders the text of the current menu item.

**Parameters:**
- g

- graphics context
- menuItem

- menu item to render
- textRect

- bounding rectangle for rendering the text
- text

- string to render

**Since:**
- 1.4

---

#### public
MenuElement
[] getPath()

Returns a menu element path.

**Returns:**
- a menu element path

---

#### protected void doClick​(
MenuSelectionManager
msm)

Call this method when a menu item is to be activated.
This method handles some of the details of menu item activation
such as clearing the selected path and messaging the
JMenuItem's doClick() method.

**Parameters:**
- msm

- A MenuSelectionManager. The visual feedback and
internal bookkeeping tasks are delegated to
this MenuSelectionManager. If

null

is
passed as this argument, the

MenuSelectionManager.defaultManager

is
used.

**See Also:**
- MenuSelectionManager

,

AbstractButton.doClick(int)

**Since:**
- 1.4

---

### Additional Sections

#### Class BasicMenuItemUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ButtonUI
- - javax.swing.plaf.MenuItemUI
- - javax.swing.plaf.basic.BasicMenuItemUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ButtonUI
- - javax.swing.plaf.MenuItemUI
- - javax.swing.plaf.basic.BasicMenuItemUI

javax.swing.plaf.ButtonUI

- javax.swing.plaf.MenuItemUI
- - javax.swing.plaf.basic.BasicMenuItemUI

javax.swing.plaf.MenuItemUI

- javax.swing.plaf.basic.BasicMenuItemUI

javax.swing.plaf.basic.BasicMenuItemUI

**Direct Known Subclasses:** BasicCheckBoxMenuItemUI

,

BasicMenuUI

,

BasicRadioButtonMenuItemUI

,

SynthMenuItemUI

```java
public class
BasicMenuItemUI

extends
MenuItemUI
```

BasicMenuItem implementation

public class

BasicMenuItemUI

extends

MenuItemUI

BasicMenuItem implementation

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

BasicMenuItemUI.MouseInputHandler

Mouse input handler

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

String

acceleratorDelimiter

Accelerator delimiter string, such as

'+'

in

'Ctrl+C'

.

protected

Font

acceleratorFont

The accelerator font.

protected

Color

acceleratorForeground

The color of the accelerator foreground.

protected

Color

acceleratorSelectionForeground

The color of the accelerator selection.

protected

Icon

arrowIcon

The arrow icon.

protected

Icon

checkIcon

The check icon.

protected int

defaultTextIconGap

The gap between the text and the icon.

protected

Color

disabledForeground

The color of the disabled foreground.

protected

MenuDragMouseListener

menuDragMouseListener

The instance of

MenuDragMouseListener

.

protected

JMenuItem

menuItem

The instance of

JMenuItem

.

protected

MenuKeyListener

menuKeyListener

The instance of

MenuKeyListener

.

protected

MouseInputListener

mouseInputListener

The instance of

MouseInputListener

.

protected boolean

oldBorderPainted

The value represents if the old border is painted.

protected

PropertyChangeListener

propertyChangeListener

PropertyChangeListener

returned from

createPropertyChangeListener

.

protected

Color

selectionBackground

The color of the selection background.

protected

Color

selectionForeground

The color of the selection foreground.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicMenuItemUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

MenuDragMouseListener

createMenuDragMouseListener

​(

JComponent

c)

Returns an instance of

MenuDragMouseListener

.

protected

MenuKeyListener

createMenuKeyListener

​(

JComponent

c)

Returns an instance of

MenuKeyListener

.

protected

MouseInputListener

createMouseInputListener

​(

JComponent

c)

Returns an instance of

MouseInputListener

.

protected

PropertyChangeListener

createPropertyChangeListener

​(

JComponent

c)

Creates a

PropertyChangeListener

which will be added to
the menu item.

static

ComponentUI

createUI

​(

JComponent

c)

Returns a new instance of

BasicMenuItemUI

.

protected void

doClick

​(

MenuSelectionManager

msm)

Call this method when a menu item is to be activated.

MenuElement

[]

getPath

()

Returns a menu element path.

protected

Dimension

getPreferredMenuItemSize

​(

JComponent

c,

Icon

checkIcon,

Icon

arrowIcon,
int defaultTextIconGap)

Returns the preferred size of a menu item.

protected

String

getPropertyPrefix

()

Returns a property prefix.

protected void

installComponents

​(

JMenuItem

menuItem)

protected void

installDefaults

()

Installs default properties.

protected void

installKeyboardActions

()

Registers keyboard action.

protected void

installListeners

()

Registers listeners.

protected void

paintBackground

​(

Graphics

g,

JMenuItem

menuItem,

Color

bgColor)

Draws the background of the menu item.

protected void

paintMenuItem

​(

Graphics

g,

JComponent

c,

Icon

checkIcon,

Icon

arrowIcon,

Color

background,

Color

foreground,
int defaultTextIconGap)

Paints a menu item.

protected void

paintText

​(

Graphics

g,

JMenuItem

menuItem,

Rectangle

textRect,

String

text)

Renders the text of the current menu item.

protected void

uninstallComponents

​(

JMenuItem

menuItem)

Unregisters components.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Unregisters listeners.

void

update

​(

Graphics

g,

JComponent

c)

We draw the background in paintMenuItem()
so override update (which fills the background of opaque
components by default) to just call paint().

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

BasicMenuItemUI.MouseInputHandler

Mouse input handler

---

#### Nested Class Summary

Mouse input handler

Field Summary

Fields

Modifier and Type

Field

Description

protected

String

acceleratorDelimiter

Accelerator delimiter string, such as

'+'

in

'Ctrl+C'

.

protected

Font

acceleratorFont

The accelerator font.

protected

Color

acceleratorForeground

The color of the accelerator foreground.

protected

Color

acceleratorSelectionForeground

The color of the accelerator selection.

protected

Icon

arrowIcon

The arrow icon.

protected

Icon

checkIcon

The check icon.

protected int

defaultTextIconGap

The gap between the text and the icon.

protected

Color

disabledForeground

The color of the disabled foreground.

protected

MenuDragMouseListener

menuDragMouseListener

The instance of

MenuDragMouseListener

.

protected

JMenuItem

menuItem

The instance of

JMenuItem

.

protected

MenuKeyListener

menuKeyListener

The instance of

MenuKeyListener

.

protected

MouseInputListener

mouseInputListener

The instance of

MouseInputListener

.

protected boolean

oldBorderPainted

The value represents if the old border is painted.

protected

PropertyChangeListener

propertyChangeListener

PropertyChangeListener

returned from

createPropertyChangeListener

.

protected

Color

selectionBackground

The color of the selection background.

protected

Color

selectionForeground

The color of the selection foreground.

---

#### Field Summary

Accelerator delimiter string, such as

'+'

in

'Ctrl+C'

.

The accelerator font.

The color of the accelerator foreground.

The color of the accelerator selection.

The arrow icon.

The check icon.

The gap between the text and the icon.

The color of the disabled foreground.

The instance of

MenuDragMouseListener

.

The instance of

JMenuItem

.

The instance of

MenuKeyListener

.

The instance of

MouseInputListener

.

The value represents if the old border is painted.

PropertyChangeListener

returned from

createPropertyChangeListener

.

The color of the selection background.

The color of the selection foreground.

Constructor Summary

Constructors

Constructor

Description

BasicMenuItemUI

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

MenuDragMouseListener

createMenuDragMouseListener

​(

JComponent

c)

Returns an instance of

MenuDragMouseListener

.

protected

MenuKeyListener

createMenuKeyListener

​(

JComponent

c)

Returns an instance of

MenuKeyListener

.

protected

MouseInputListener

createMouseInputListener

​(

JComponent

c)

Returns an instance of

MouseInputListener

.

protected

PropertyChangeListener

createPropertyChangeListener

​(

JComponent

c)

Creates a

PropertyChangeListener

which will be added to
the menu item.

static

ComponentUI

createUI

​(

JComponent

c)

Returns a new instance of

BasicMenuItemUI

.

protected void

doClick

​(

MenuSelectionManager

msm)

Call this method when a menu item is to be activated.

MenuElement

[]

getPath

()

Returns a menu element path.

protected

Dimension

getPreferredMenuItemSize

​(

JComponent

c,

Icon

checkIcon,

Icon

arrowIcon,
int defaultTextIconGap)

Returns the preferred size of a menu item.

protected

String

getPropertyPrefix

()

Returns a property prefix.

protected void

installComponents

​(

JMenuItem

menuItem)

protected void

installDefaults

()

Installs default properties.

protected void

installKeyboardActions

()

Registers keyboard action.

protected void

installListeners

()

Registers listeners.

protected void

paintBackground

​(

Graphics

g,

JMenuItem

menuItem,

Color

bgColor)

Draws the background of the menu item.

protected void

paintMenuItem

​(

Graphics

g,

JComponent

c,

Icon

checkIcon,

Icon

arrowIcon,

Color

background,

Color

foreground,
int defaultTextIconGap)

Paints a menu item.

protected void

paintText

​(

Graphics

g,

JMenuItem

menuItem,

Rectangle

textRect,

String

text)

Renders the text of the current menu item.

protected void

uninstallComponents

​(

JMenuItem

menuItem)

Unregisters components.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Unregisters listeners.

void

update

​(

Graphics

g,

JComponent

c)

We draw the background in paintMenuItem()
so override update (which fills the background of opaque
components by default) to just call paint().

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

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

Returns an instance of

MenuDragMouseListener

.

Returns an instance of

MenuKeyListener

.

Returns an instance of

MouseInputListener

.

Creates a

PropertyChangeListener

which will be added to
the menu item.

Returns a new instance of

BasicMenuItemUI

.

Call this method when a menu item is to be activated.

Returns a menu element path.

Returns the preferred size of a menu item.

Returns a property prefix.

Installs default properties.

Registers keyboard action.

Registers listeners.

Draws the background of the menu item.

Paints a menu item.

Renders the text of the current menu item.

Unregisters components.

Uninstalls default properties.

Unregisters keyboard actions.

Unregisters listeners.

We draw the background in paintMenuItem()
so override update (which fills the background of opaque
components by default) to just call paint().

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

---

#### Methods declared in class javax.swing.plaf. ComponentUI

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

============ FIELD DETAIL ===========

- Field Detail

- menuItem

```java
protected
JMenuItem
menuItem
```

The instance of

JMenuItem

.

- selectionBackground

```java
protected
Color
selectionBackground
```

The color of the selection background.

- selectionForeground

```java
protected
Color
selectionForeground
```

The color of the selection foreground.

- disabledForeground

```java
protected
Color
disabledForeground
```

The color of the disabled foreground.

- acceleratorForeground

```java
protected
Color
acceleratorForeground
```

The color of the accelerator foreground.

- acceleratorSelectionForeground

```java
protected
Color
acceleratorSelectionForeground
```

The color of the accelerator selection.

- acceleratorDelimiter

```java
protected
String
acceleratorDelimiter
```

Accelerator delimiter string, such as

'+'

in

'Ctrl+C'

.

**Since:** 1.7

- defaultTextIconGap

```java
protected int defaultTextIconGap
```

The gap between the text and the icon.

- acceleratorFont

```java
protected
Font
acceleratorFont
```

The accelerator font.

- mouseInputListener

```java
protected
MouseInputListener
mouseInputListener
```

The instance of

MouseInputListener

.

- menuDragMouseListener

```java
protected
MenuDragMouseListener
menuDragMouseListener
```

The instance of

MenuDragMouseListener

.

- menuKeyListener

```java
protected
MenuKeyListener
menuKeyListener
```

The instance of

MenuKeyListener

.

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

PropertyChangeListener

returned from

createPropertyChangeListener

. You should not
need to access this field, rather if you want to customize the

PropertyChangeListener

override

createPropertyChangeListener

.

**Since:** 1.6
**See Also:** createPropertyChangeListener(javax.swing.JComponent)

- arrowIcon

```java
protected
Icon
arrowIcon
```

The arrow icon.

- checkIcon

```java
protected
Icon
checkIcon
```

The check icon.

- oldBorderPainted

```java
protected boolean oldBorderPainted
```

The value represents if the old border is painted.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicMenuItemUI

```java
public BasicMenuItemUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of

BasicMenuItemUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicMenuItemUI

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- installComponents

```java
protected void installComponents​(
JMenuItem
menuItem)
```

**Parameters:** menuItem

- a menu item
**Since:** 1.3

- getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Returns a property prefix.

**Returns:** a property prefix

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard action.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- uninstallComponents

```java
protected void uninstallComponents​(
JMenuItem
menuItem)
```

Unregisters components.

**Parameters:** menuItem

- a menu item
**Since:** 1.3

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

- createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener​(
JComponent
c)
```

Returns an instance of

MouseInputListener

.

**Parameters:** c

- a component
**Returns:** an instance of

MouseInputListener

- createMenuDragMouseListener

```java
protected
MenuDragMouseListener
createMenuDragMouseListener​(
JComponent
c)
```

Returns an instance of

MenuDragMouseListener

.

**Parameters:** c

- a component
**Returns:** an instance of

MenuDragMouseListener

- createMenuKeyListener

```java
protected
MenuKeyListener
createMenuKeyListener​(
JComponent
c)
```

Returns an instance of

MenuKeyListener

.

**Parameters:** c

- a component
**Returns:** an instance of

MenuKeyListener

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener​(
JComponent
c)
```

Creates a

PropertyChangeListener

which will be added to
the menu item.
If this method returns null then it will not be added to the menu item.

**Parameters:** c

- a component
**Returns:** an instance of a

PropertyChangeListener

or null
**Since:** 1.6

- getPreferredMenuItemSize

```java
protected
Dimension
getPreferredMenuItemSize​(
JComponent
c,

Icon
checkIcon,

Icon
arrowIcon,
int defaultTextIconGap)
```

Returns the preferred size of a menu item.

**Parameters:** c

- a component
**Parameters:** checkIcon

- a check icon
**Parameters:** arrowIcon

- an arrow icon
**Parameters:** defaultTextIconGap

- a gap between a text and an icon
**Returns:** the preferred size of a menu item

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

We draw the background in paintMenuItem()
so override update (which fills the background of opaque
components by default) to just call paint().

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.paint(java.awt.Graphics, javax.swing.JComponent)

,

JComponent.paintComponent(java.awt.Graphics)

- paintMenuItem

```java
protected void paintMenuItem​(
Graphics
g,

JComponent
c,

Icon
checkIcon,

Icon
arrowIcon,

Color
background,

Color
foreground,
int defaultTextIconGap)
```

Paints a menu item.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Parameters:** checkIcon

- a check icon
**Parameters:** arrowIcon

- an arrow icon
**Parameters:** background

- a background color
**Parameters:** foreground

- a foreground color
**Parameters:** defaultTextIconGap

- a gap between a text and an icon

- paintBackground

```java
protected void paintBackground​(
Graphics
g,

JMenuItem
menuItem,

Color
bgColor)
```

Draws the background of the menu item.

**Parameters:** g

- the paint graphics
**Parameters:** menuItem

- menu item to be painted
**Parameters:** bgColor

- selection background color
**Since:** 1.4

- paintText

```java
protected void paintText​(
Graphics
g,

JMenuItem
menuItem,

Rectangle
textRect,

String
text)
```

Renders the text of the current menu item.

**Parameters:** g

- graphics context
**Parameters:** menuItem

- menu item to render
**Parameters:** textRect

- bounding rectangle for rendering the text
**Parameters:** text

- string to render
**Since:** 1.4

- getPath

```java
public
MenuElement
[] getPath()
```

Returns a menu element path.

**Returns:** a menu element path

- doClick

```java
protected void doClick​(
MenuSelectionManager
msm)
```

Call this method when a menu item is to be activated.
This method handles some of the details of menu item activation
such as clearing the selected path and messaging the
JMenuItem's doClick() method.

**Parameters:** msm

- A MenuSelectionManager. The visual feedback and
internal bookkeeping tasks are delegated to
this MenuSelectionManager. If

null

is
passed as this argument, the

MenuSelectionManager.defaultManager

is
used.
**Since:** 1.4
**See Also:** MenuSelectionManager

,

AbstractButton.doClick(int)

Field Detail

- menuItem

```java
protected
JMenuItem
menuItem
```

The instance of

JMenuItem

.

- selectionBackground

```java
protected
Color
selectionBackground
```

The color of the selection background.

- selectionForeground

```java
protected
Color
selectionForeground
```

The color of the selection foreground.

- disabledForeground

```java
protected
Color
disabledForeground
```

The color of the disabled foreground.

- acceleratorForeground

```java
protected
Color
acceleratorForeground
```

The color of the accelerator foreground.

- acceleratorSelectionForeground

```java
protected
Color
acceleratorSelectionForeground
```

The color of the accelerator selection.

- acceleratorDelimiter

```java
protected
String
acceleratorDelimiter
```

Accelerator delimiter string, such as

'+'

in

'Ctrl+C'

.

**Since:** 1.7

- defaultTextIconGap

```java
protected int defaultTextIconGap
```

The gap between the text and the icon.

- acceleratorFont

```java
protected
Font
acceleratorFont
```

The accelerator font.

- mouseInputListener

```java
protected
MouseInputListener
mouseInputListener
```

The instance of

MouseInputListener

.

- menuDragMouseListener

```java
protected
MenuDragMouseListener
menuDragMouseListener
```

The instance of

MenuDragMouseListener

.

- menuKeyListener

```java
protected
MenuKeyListener
menuKeyListener
```

The instance of

MenuKeyListener

.

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

PropertyChangeListener

returned from

createPropertyChangeListener

. You should not
need to access this field, rather if you want to customize the

PropertyChangeListener

override

createPropertyChangeListener

.

**Since:** 1.6
**See Also:** createPropertyChangeListener(javax.swing.JComponent)

- arrowIcon

```java
protected
Icon
arrowIcon
```

The arrow icon.

- checkIcon

```java
protected
Icon
checkIcon
```

The check icon.

- oldBorderPainted

```java
protected boolean oldBorderPainted
```

The value represents if the old border is painted.

---

#### Field Detail

menuItem

```java
protected
JMenuItem
menuItem
```

The instance of

JMenuItem

.

---

#### menuItem

protected

JMenuItem

menuItem

The instance of

JMenuItem

.

selectionBackground

```java
protected
Color
selectionBackground
```

The color of the selection background.

---

#### selectionBackground

protected

Color

selectionBackground

The color of the selection background.

selectionForeground

```java
protected
Color
selectionForeground
```

The color of the selection foreground.

---

#### selectionForeground

protected

Color

selectionForeground

The color of the selection foreground.

disabledForeground

```java
protected
Color
disabledForeground
```

The color of the disabled foreground.

---

#### disabledForeground

protected

Color

disabledForeground

The color of the disabled foreground.

acceleratorForeground

```java
protected
Color
acceleratorForeground
```

The color of the accelerator foreground.

---

#### acceleratorForeground

protected

Color

acceleratorForeground

The color of the accelerator foreground.

acceleratorSelectionForeground

```java
protected
Color
acceleratorSelectionForeground
```

The color of the accelerator selection.

---

#### acceleratorSelectionForeground

protected

Color

acceleratorSelectionForeground

The color of the accelerator selection.

acceleratorDelimiter

```java
protected
String
acceleratorDelimiter
```

Accelerator delimiter string, such as

'+'

in

'Ctrl+C'

.

**Since:** 1.7

---

#### acceleratorDelimiter

protected

String

acceleratorDelimiter

Accelerator delimiter string, such as

'+'

in

'Ctrl+C'

.

defaultTextIconGap

```java
protected int defaultTextIconGap
```

The gap between the text and the icon.

---

#### defaultTextIconGap

protected int defaultTextIconGap

The gap between the text and the icon.

acceleratorFont

```java
protected
Font
acceleratorFont
```

The accelerator font.

---

#### acceleratorFont

protected

Font

acceleratorFont

The accelerator font.

mouseInputListener

```java
protected
MouseInputListener
mouseInputListener
```

The instance of

MouseInputListener

.

---

#### mouseInputListener

protected

MouseInputListener

mouseInputListener

The instance of

MouseInputListener

.

menuDragMouseListener

```java
protected
MenuDragMouseListener
menuDragMouseListener
```

The instance of

MenuDragMouseListener

.

---

#### menuDragMouseListener

protected

MenuDragMouseListener

menuDragMouseListener

The instance of

MenuDragMouseListener

.

menuKeyListener

```java
protected
MenuKeyListener
menuKeyListener
```

The instance of

MenuKeyListener

.

---

#### menuKeyListener

protected

MenuKeyListener

menuKeyListener

The instance of

MenuKeyListener

.

propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

PropertyChangeListener

returned from

createPropertyChangeListener

. You should not
need to access this field, rather if you want to customize the

PropertyChangeListener

override

createPropertyChangeListener

.

**Since:** 1.6
**See Also:** createPropertyChangeListener(javax.swing.JComponent)

---

#### propertyChangeListener

protected

PropertyChangeListener

propertyChangeListener

PropertyChangeListener

returned from

createPropertyChangeListener

. You should not
need to access this field, rather if you want to customize the

PropertyChangeListener

override

createPropertyChangeListener

.

arrowIcon

```java
protected
Icon
arrowIcon
```

The arrow icon.

---

#### arrowIcon

protected

Icon

arrowIcon

The arrow icon.

checkIcon

```java
protected
Icon
checkIcon
```

The check icon.

---

#### checkIcon

protected

Icon

checkIcon

The check icon.

oldBorderPainted

```java
protected boolean oldBorderPainted
```

The value represents if the old border is painted.

---

#### oldBorderPainted

protected boolean oldBorderPainted

The value represents if the old border is painted.

Constructor Detail

- BasicMenuItemUI

```java
public BasicMenuItemUI()
```

---

#### Constructor Detail

BasicMenuItemUI

```java
public BasicMenuItemUI()
```

---

#### BasicMenuItemUI

public BasicMenuItemUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of

BasicMenuItemUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicMenuItemUI

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- installComponents

```java
protected void installComponents​(
JMenuItem
menuItem)
```

**Parameters:** menuItem

- a menu item
**Since:** 1.3

- getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Returns a property prefix.

**Returns:** a property prefix

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard action.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- uninstallComponents

```java
protected void uninstallComponents​(
JMenuItem
menuItem)
```

Unregisters components.

**Parameters:** menuItem

- a menu item
**Since:** 1.3

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

- createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener​(
JComponent
c)
```

Returns an instance of

MouseInputListener

.

**Parameters:** c

- a component
**Returns:** an instance of

MouseInputListener

- createMenuDragMouseListener

```java
protected
MenuDragMouseListener
createMenuDragMouseListener​(
JComponent
c)
```

Returns an instance of

MenuDragMouseListener

.

**Parameters:** c

- a component
**Returns:** an instance of

MenuDragMouseListener

- createMenuKeyListener

```java
protected
MenuKeyListener
createMenuKeyListener​(
JComponent
c)
```

Returns an instance of

MenuKeyListener

.

**Parameters:** c

- a component
**Returns:** an instance of

MenuKeyListener

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener​(
JComponent
c)
```

Creates a

PropertyChangeListener

which will be added to
the menu item.
If this method returns null then it will not be added to the menu item.

**Parameters:** c

- a component
**Returns:** an instance of a

PropertyChangeListener

or null
**Since:** 1.6

- getPreferredMenuItemSize

```java
protected
Dimension
getPreferredMenuItemSize​(
JComponent
c,

Icon
checkIcon,

Icon
arrowIcon,
int defaultTextIconGap)
```

Returns the preferred size of a menu item.

**Parameters:** c

- a component
**Parameters:** checkIcon

- a check icon
**Parameters:** arrowIcon

- an arrow icon
**Parameters:** defaultTextIconGap

- a gap between a text and an icon
**Returns:** the preferred size of a menu item

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

We draw the background in paintMenuItem()
so override update (which fills the background of opaque
components by default) to just call paint().

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.paint(java.awt.Graphics, javax.swing.JComponent)

,

JComponent.paintComponent(java.awt.Graphics)

- paintMenuItem

```java
protected void paintMenuItem​(
Graphics
g,

JComponent
c,

Icon
checkIcon,

Icon
arrowIcon,

Color
background,

Color
foreground,
int defaultTextIconGap)
```

Paints a menu item.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Parameters:** checkIcon

- a check icon
**Parameters:** arrowIcon

- an arrow icon
**Parameters:** background

- a background color
**Parameters:** foreground

- a foreground color
**Parameters:** defaultTextIconGap

- a gap between a text and an icon

- paintBackground

```java
protected void paintBackground​(
Graphics
g,

JMenuItem
menuItem,

Color
bgColor)
```

Draws the background of the menu item.

**Parameters:** g

- the paint graphics
**Parameters:** menuItem

- menu item to be painted
**Parameters:** bgColor

- selection background color
**Since:** 1.4

- paintText

```java
protected void paintText​(
Graphics
g,

JMenuItem
menuItem,

Rectangle
textRect,

String
text)
```

Renders the text of the current menu item.

**Parameters:** g

- graphics context
**Parameters:** menuItem

- menu item to render
**Parameters:** textRect

- bounding rectangle for rendering the text
**Parameters:** text

- string to render
**Since:** 1.4

- getPath

```java
public
MenuElement
[] getPath()
```

Returns a menu element path.

**Returns:** a menu element path

- doClick

```java
protected void doClick​(
MenuSelectionManager
msm)
```

Call this method when a menu item is to be activated.
This method handles some of the details of menu item activation
such as clearing the selected path and messaging the
JMenuItem's doClick() method.

**Parameters:** msm

- A MenuSelectionManager. The visual feedback and
internal bookkeeping tasks are delegated to
this MenuSelectionManager. If

null

is
passed as this argument, the

MenuSelectionManager.defaultManager

is
used.
**Since:** 1.4
**See Also:** MenuSelectionManager

,

AbstractButton.doClick(int)

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of

BasicMenuItemUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicMenuItemUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Returns a new instance of

BasicMenuItemUI

.

installDefaults

```java
protected void installDefaults()
```

Installs default properties.

---

#### installDefaults

protected void installDefaults()

Installs default properties.

installComponents

```java
protected void installComponents​(
JMenuItem
menuItem)
```

**Parameters:** menuItem

- a menu item
**Since:** 1.3

---

#### installComponents

protected void installComponents​(

JMenuItem

menuItem)

getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Returns a property prefix.

**Returns:** a property prefix

---

#### getPropertyPrefix

protected

String

getPropertyPrefix()

Returns a property prefix.

installListeners

```java
protected void installListeners()
```

Registers listeners.

---

#### installListeners

protected void installListeners()

Registers listeners.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard action.

---

#### installKeyboardActions

protected void installKeyboardActions()

Registers keyboard action.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls default properties.

uninstallComponents

```java
protected void uninstallComponents​(
JMenuItem
menuItem)
```

Unregisters components.

**Parameters:** menuItem

- a menu item
**Since:** 1.3

---

#### uninstallComponents

protected void uninstallComponents​(

JMenuItem

menuItem)

Unregisters components.

uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

---

#### uninstallListeners

protected void uninstallListeners()

Unregisters listeners.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Unregisters keyboard actions.

createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener​(
JComponent
c)
```

Returns an instance of

MouseInputListener

.

**Parameters:** c

- a component
**Returns:** an instance of

MouseInputListener

---

#### createMouseInputListener

protected

MouseInputListener

createMouseInputListener​(

JComponent

c)

Returns an instance of

MouseInputListener

.

createMenuDragMouseListener

```java
protected
MenuDragMouseListener
createMenuDragMouseListener​(
JComponent
c)
```

Returns an instance of

MenuDragMouseListener

.

**Parameters:** c

- a component
**Returns:** an instance of

MenuDragMouseListener

---

#### createMenuDragMouseListener

protected

MenuDragMouseListener

createMenuDragMouseListener​(

JComponent

c)

Returns an instance of

MenuDragMouseListener

.

createMenuKeyListener

```java
protected
MenuKeyListener
createMenuKeyListener​(
JComponent
c)
```

Returns an instance of

MenuKeyListener

.

**Parameters:** c

- a component
**Returns:** an instance of

MenuKeyListener

---

#### createMenuKeyListener

protected

MenuKeyListener

createMenuKeyListener​(

JComponent

c)

Returns an instance of

MenuKeyListener

.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener​(
JComponent
c)
```

Creates a

PropertyChangeListener

which will be added to
the menu item.
If this method returns null then it will not be added to the menu item.

**Parameters:** c

- a component
**Returns:** an instance of a

PropertyChangeListener

or null
**Since:** 1.6

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener​(

JComponent

c)

Creates a

PropertyChangeListener

which will be added to
the menu item.
If this method returns null then it will not be added to the menu item.

getPreferredMenuItemSize

```java
protected
Dimension
getPreferredMenuItemSize​(
JComponent
c,

Icon
checkIcon,

Icon
arrowIcon,
int defaultTextIconGap)
```

Returns the preferred size of a menu item.

**Parameters:** c

- a component
**Parameters:** checkIcon

- a check icon
**Parameters:** arrowIcon

- an arrow icon
**Parameters:** defaultTextIconGap

- a gap between a text and an icon
**Returns:** the preferred size of a menu item

---

#### getPreferredMenuItemSize

protected

Dimension

getPreferredMenuItemSize​(

JComponent

c,

Icon

checkIcon,

Icon

arrowIcon,
int defaultTextIconGap)

Returns the preferred size of a menu item.

update

```java
public void update​(
Graphics
g,

JComponent
c)
```

We draw the background in paintMenuItem()
so override update (which fills the background of opaque
components by default) to just call paint().

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.paint(java.awt.Graphics, javax.swing.JComponent)

,

JComponent.paintComponent(java.awt.Graphics)

---

#### update

public void update​(

Graphics

g,

JComponent

c)

We draw the background in paintMenuItem()
so override update (which fills the background of opaque
components by default) to just call paint().

paintMenuItem

```java
protected void paintMenuItem​(
Graphics
g,

JComponent
c,

Icon
checkIcon,

Icon
arrowIcon,

Color
background,

Color
foreground,
int defaultTextIconGap)
```

Paints a menu item.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Parameters:** checkIcon

- a check icon
**Parameters:** arrowIcon

- an arrow icon
**Parameters:** background

- a background color
**Parameters:** foreground

- a foreground color
**Parameters:** defaultTextIconGap

- a gap between a text and an icon

---

#### paintMenuItem

protected void paintMenuItem​(

Graphics

g,

JComponent

c,

Icon

checkIcon,

Icon

arrowIcon,

Color

background,

Color

foreground,
int defaultTextIconGap)

Paints a menu item.

paintBackground

```java
protected void paintBackground​(
Graphics
g,

JMenuItem
menuItem,

Color
bgColor)
```

Draws the background of the menu item.

**Parameters:** g

- the paint graphics
**Parameters:** menuItem

- menu item to be painted
**Parameters:** bgColor

- selection background color
**Since:** 1.4

---

#### paintBackground

protected void paintBackground​(

Graphics

g,

JMenuItem

menuItem,

Color

bgColor)

Draws the background of the menu item.

paintText

```java
protected void paintText​(
Graphics
g,

JMenuItem
menuItem,

Rectangle
textRect,

String
text)
```

Renders the text of the current menu item.

**Parameters:** g

- graphics context
**Parameters:** menuItem

- menu item to render
**Parameters:** textRect

- bounding rectangle for rendering the text
**Parameters:** text

- string to render
**Since:** 1.4

---

#### paintText

protected void paintText​(

Graphics

g,

JMenuItem

menuItem,

Rectangle

textRect,

String

text)

Renders the text of the current menu item.

getPath

```java
public
MenuElement
[] getPath()
```

Returns a menu element path.

**Returns:** a menu element path

---

#### getPath

public

MenuElement

[] getPath()

Returns a menu element path.

doClick

```java
protected void doClick​(
MenuSelectionManager
msm)
```

Call this method when a menu item is to be activated.
This method handles some of the details of menu item activation
such as clearing the selected path and messaging the
JMenuItem's doClick() method.

**Parameters:** msm

- A MenuSelectionManager. The visual feedback and
internal bookkeeping tasks are delegated to
this MenuSelectionManager. If

null

is
passed as this argument, the

MenuSelectionManager.defaultManager

is
used.
**Since:** 1.4
**See Also:** MenuSelectionManager

,

AbstractButton.doClick(int)

---

#### doClick

protected void doClick​(

MenuSelectionManager

msm)

Call this method when a menu item is to be activated.
This method handles some of the details of menu item activation
such as clearing the selected path and messaging the
JMenuItem's doClick() method.

---

