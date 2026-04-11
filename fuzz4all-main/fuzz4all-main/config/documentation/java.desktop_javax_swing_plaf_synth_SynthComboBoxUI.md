# Class SynthComboBoxUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthComboBoxUI.html`

### Class Description

```java
public class
SynthComboBoxUI

extends
BasicComboBoxUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JComboBox

.

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthComboBoxUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Creates a new UI object for the given component.

**Parameters:**
- c

- component to create UI object for

**Returns:**
- the UI object

---

#### public void installUI​(
JComponent
c)

Configures the specified component appropriately for the look and feel.
This method is invoked when the

ComponentUI

instance is being installed
as the UI delegate on the specified component. This method should
completely configure the component for the look and feel,
including the following:

- Install default property values for color, fonts, borders,
icons, opacity, etc. on the component. Whenever possible,
property values initialized by the client program should

not

be overridden.

Install a

LayoutManager

on the component if necessary.

Create/add any required sub-components to the component.

Create/install event listeners on the component.

Create/install a

PropertyChangeListener

on the component in order
to detect and respond to component property changes appropriately.

Install keyboard UI (mnemonics, traversal, etc.) on the component.

Initialize any appropriate instance data.

Overridden to ensure that ButtonHandler is created prior to any of
the other installXXX methods, since several of them reference
buttonHandler.

**Overrides:**
- installUI

in class

ComponentUI

**Parameters:**
- c

- the component where this UI delegate is being installed

**See Also:**
- ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

---

#### public void update​(
Graphics
g,

JComponent
c)

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:**
- update

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

object used for painting
- c

- the component being painted

**See Also:**
- paint(SynthContext,Graphics)

---

#### public void paint​(
Graphics
g,

JComponent
c)

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:**
- paint

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

object used for painting
- c

- the component being painted

**See Also:**
- paint(SynthContext,Graphics)

---

#### protected void paint​(
SynthContext
context,

Graphics
g)

Paints the specified component.

**Parameters:**
- context

- context for the component being painted
- g

- the

Graphics

object used for painting

**See Also:**
- update(Graphics,JComponent)

---

#### public void paintCurrentValue​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)

Paints the currently selected item.

**Overrides:**
- paintCurrentValue

in class

BasicComboBoxUI

**Parameters:**
- g

- an instance of

Graphics
- bounds

- a bounding rectangle to render to
- hasFocus

- is focused

---

#### protected
Dimension
getDefaultSize()

Returns the default size of an empty display area of the combo box using
the current renderer and font.

This method was overridden to use SynthComboBoxRenderer instead of
DefaultListCellRenderer as the default renderer when calculating the
size of the combo box. This is used in the case of the combo not having
any data.

**Overrides:**
- getDefaultSize

in class

BasicComboBoxUI

**Returns:**
- the size of an empty display area

**See Also:**
- BasicComboBoxUI.getDisplaySize()

---

### Additional Sections

#### Class SynthComboBoxUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ComboBoxUI
- - javax.swing.plaf.basic.BasicComboBoxUI
- - javax.swing.plaf.synth.SynthComboBoxUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ComboBoxUI
- - javax.swing.plaf.basic.BasicComboBoxUI
- - javax.swing.plaf.synth.SynthComboBoxUI

javax.swing.plaf.ComboBoxUI

- javax.swing.plaf.basic.BasicComboBoxUI
- - javax.swing.plaf.synth.SynthComboBoxUI

javax.swing.plaf.basic.BasicComboBoxUI

- javax.swing.plaf.synth.SynthComboBoxUI

javax.swing.plaf.synth.SynthComboBoxUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

```java
public class
SynthComboBoxUI

extends
BasicComboBoxUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JComboBox

.

**Since:** 1.7

public class

SynthComboBoxUI

extends

BasicComboBoxUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JComboBox

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicComboBoxUI

BasicComboBoxUI.ComboBoxLayoutManager

,

BasicComboBoxUI.FocusHandler

,

BasicComboBoxUI.ItemHandler

,

BasicComboBoxUI.KeyHandler

,

BasicComboBoxUI.ListDataHandler

,

BasicComboBoxUI.PropertyChangeHandler

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicComboBoxUI

arrowButton

,

cachedMinimumSize

,

comboBox

,

currentValuePane

,

editor

,

focusListener

,

hasFocus

,

isMinimumSizeDirty

,

itemListener

,

keyListener

,

listBox

,

listDataListener

,

padding

,

popup

,

popupKeyListener

,

popupMouseListener

,

popupMouseMotionListener

,

propertyChangeListener

,

squareButton

- Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SynthComboBoxUI

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

static

ComponentUI

createUI

​(

JComponent

c)

Creates a new UI object for the given component.

protected

Dimension

getDefaultSize

()

Returns the default size of an empty display area of the combo box using
the current renderer and font.

void

installUI

​(

JComponent

c)

Configures the specified component appropriately for the look and feel.

void

paint

​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the specified component.

void

paintCurrentValue

​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

Paints the currently selected item.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicComboBoxUI

addEditor

,

configureArrowButton

,

configureEditor

,

createArrowButton

,

createEditor

,

createFocusListener

,

createItemListener

,

createKeyListener

,

createLayoutManager

,

createListDataListener

,

createPopup

,

createPropertyChangeListener

,

createRenderer

,

getBaseline

,

getBaselineResizeBehavior

,

getDisplaySize

,

getInsets

,

getMinimumSize

,

getSizeForComponent

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

isFocusTraversable

,

isNavigationKey

,

isPopupVisible

,

paintCurrentValueBackground

,

rectangleForCurrentValue

,

removeEditor

,

selectNextPossibleValue

,

selectPreviousPossibleValue

,

setPopupVisible

,

toggleOpenClose

,

unconfigureArrowButton

,

unconfigureEditor

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMaximumSize

,

getPreferredSize

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

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicComboBoxUI

BasicComboBoxUI.ComboBoxLayoutManager

,

BasicComboBoxUI.FocusHandler

,

BasicComboBoxUI.ItemHandler

,

BasicComboBoxUI.KeyHandler

,

BasicComboBoxUI.ListDataHandler

,

BasicComboBoxUI.PropertyChangeHandler

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicComboBoxUI

BasicComboBoxUI.ComboBoxLayoutManager

,

BasicComboBoxUI.FocusHandler

,

BasicComboBoxUI.ItemHandler

,

BasicComboBoxUI.KeyHandler

,

BasicComboBoxUI.ListDataHandler

,

BasicComboBoxUI.PropertyChangeHandler

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicComboBoxUI

Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicComboBoxUI

arrowButton

,

cachedMinimumSize

,

comboBox

,

currentValuePane

,

editor

,

focusListener

,

hasFocus

,

isMinimumSizeDirty

,

itemListener

,

keyListener

,

listBox

,

listDataListener

,

padding

,

popup

,

popupKeyListener

,

popupMouseListener

,

popupMouseMotionListener

,

propertyChangeListener

,

squareButton

- Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

---

#### Field Summary

Fields declared in class javax.swing.plaf.basic.

BasicComboBoxUI

arrowButton

,

cachedMinimumSize

,

comboBox

,

currentValuePane

,

editor

,

focusListener

,

hasFocus

,

isMinimumSizeDirty

,

itemListener

,

keyListener

,

listBox

,

listDataListener

,

padding

,

popup

,

popupKeyListener

,

popupMouseListener

,

popupMouseMotionListener

,

propertyChangeListener

,

squareButton

---

#### Fields declared in class javax.swing.plaf.basic. BasicComboBoxUI

Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

---

#### Fields declared in interface javax.swing.plaf.synth. SynthConstants

Constructor Summary

Constructors

Constructor

Description

SynthComboBoxUI

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

static

ComponentUI

createUI

​(

JComponent

c)

Creates a new UI object for the given component.

protected

Dimension

getDefaultSize

()

Returns the default size of an empty display area of the combo box using
the current renderer and font.

void

installUI

​(

JComponent

c)

Configures the specified component appropriately for the look and feel.

void

paint

​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the specified component.

void

paintCurrentValue

​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

Paints the currently selected item.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicComboBoxUI

addEditor

,

configureArrowButton

,

configureEditor

,

createArrowButton

,

createEditor

,

createFocusListener

,

createItemListener

,

createKeyListener

,

createLayoutManager

,

createListDataListener

,

createPopup

,

createPropertyChangeListener

,

createRenderer

,

getBaseline

,

getBaselineResizeBehavior

,

getDisplaySize

,

getInsets

,

getMinimumSize

,

getSizeForComponent

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

isFocusTraversable

,

isNavigationKey

,

isPopupVisible

,

paintCurrentValueBackground

,

rectangleForCurrentValue

,

removeEditor

,

selectNextPossibleValue

,

selectPreviousPossibleValue

,

setPopupVisible

,

toggleOpenClose

,

unconfigureArrowButton

,

unconfigureEditor

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMaximumSize

,

getPreferredSize

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

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Method Summary

Creates a new UI object for the given component.

Returns the default size of an empty display area of the combo box using
the current renderer and font.

Configures the specified component appropriately for the look and feel.

Paints the specified component according to the Look and Feel.

Paints the specified component.

Paints the currently selected item.

Notifies this UI delegate to repaint the specified component.

Methods declared in class javax.swing.plaf.basic.

BasicComboBoxUI

addEditor

,

configureArrowButton

,

configureEditor

,

createArrowButton

,

createEditor

,

createFocusListener

,

createItemListener

,

createKeyListener

,

createLayoutManager

,

createListDataListener

,

createPopup

,

createPropertyChangeListener

,

createRenderer

,

getBaseline

,

getBaselineResizeBehavior

,

getDisplaySize

,

getInsets

,

getMinimumSize

,

getSizeForComponent

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

isFocusTraversable

,

isNavigationKey

,

isPopupVisible

,

paintCurrentValueBackground

,

rectangleForCurrentValue

,

removeEditor

,

selectNextPossibleValue

,

selectPreviousPossibleValue

,

setPopupVisible

,

toggleOpenClose

,

unconfigureArrowButton

,

unconfigureEditor

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

---

#### Methods declared in class javax.swing.plaf.basic. BasicComboBoxUI

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMaximumSize

,

getPreferredSize

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

Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Methods declared in interface java.beans. PropertyChangeListener

Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Methods declared in interface javax.swing.plaf.synth. SynthUI

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SynthComboBoxUI

```java
public SynthComboBoxUI()
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

Creates a new UI object for the given component.

**Parameters:** c

- component to create UI object for
**Returns:** the UI object

- installUI

```java
public void installUI​(
JComponent
c)
```

Configures the specified component appropriately for the look and feel.
This method is invoked when the

ComponentUI

instance is being installed
as the UI delegate on the specified component. This method should
completely configure the component for the look and feel,
including the following:

- Install default property values for color, fonts, borders,
icons, opacity, etc. on the component. Whenever possible,
property values initialized by the client program should

not

be overridden.

Install a

LayoutManager

on the component if necessary.

Create/add any required sub-components to the component.

Create/install event listeners on the component.

Create/install a

PropertyChangeListener

on the component in order
to detect and respond to component property changes appropriately.

Install keyboard UI (mnemonics, traversal, etc.) on the component.

Initialize any appropriate instance data.

Overridden to ensure that ButtonHandler is created prior to any of
the other installXXX methods, since several of them reference
buttonHandler.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

- paintCurrentValue

```java
public void paintCurrentValue​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

Paints the currently selected item.

**Overrides:** paintCurrentValue

in class

BasicComboBoxUI
**Parameters:** g

- an instance of

Graphics
**Parameters:** bounds

- a bounding rectangle to render to
**Parameters:** hasFocus

- is focused

- getDefaultSize

```java
protected
Dimension
getDefaultSize()
```

Returns the default size of an empty display area of the combo box using
the current renderer and font.

This method was overridden to use SynthComboBoxRenderer instead of
DefaultListCellRenderer as the default renderer when calculating the
size of the combo box. This is used in the case of the combo not having
any data.

**Overrides:** getDefaultSize

in class

BasicComboBoxUI
**Returns:** the size of an empty display area
**See Also:** BasicComboBoxUI.getDisplaySize()

Constructor Detail

- SynthComboBoxUI

```java
public SynthComboBoxUI()
```

---

#### Constructor Detail

SynthComboBoxUI

```java
public SynthComboBoxUI()
```

---

#### SynthComboBoxUI

public SynthComboBoxUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates a new UI object for the given component.

**Parameters:** c

- component to create UI object for
**Returns:** the UI object

- installUI

```java
public void installUI​(
JComponent
c)
```

Configures the specified component appropriately for the look and feel.
This method is invoked when the

ComponentUI

instance is being installed
as the UI delegate on the specified component. This method should
completely configure the component for the look and feel,
including the following:

- Install default property values for color, fonts, borders,
icons, opacity, etc. on the component. Whenever possible,
property values initialized by the client program should

not

be overridden.

Install a

LayoutManager

on the component if necessary.

Create/add any required sub-components to the component.

Create/install event listeners on the component.

Create/install a

PropertyChangeListener

on the component in order
to detect and respond to component property changes appropriately.

Install keyboard UI (mnemonics, traversal, etc.) on the component.

Initialize any appropriate instance data.

Overridden to ensure that ButtonHandler is created prior to any of
the other installXXX methods, since several of them reference
buttonHandler.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

- paintCurrentValue

```java
public void paintCurrentValue​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

Paints the currently selected item.

**Overrides:** paintCurrentValue

in class

BasicComboBoxUI
**Parameters:** g

- an instance of

Graphics
**Parameters:** bounds

- a bounding rectangle to render to
**Parameters:** hasFocus

- is focused

- getDefaultSize

```java
protected
Dimension
getDefaultSize()
```

Returns the default size of an empty display area of the combo box using
the current renderer and font.

This method was overridden to use SynthComboBoxRenderer instead of
DefaultListCellRenderer as the default renderer when calculating the
size of the combo box. This is used in the case of the combo not having
any data.

**Overrides:** getDefaultSize

in class

BasicComboBoxUI
**Returns:** the size of an empty display area
**See Also:** BasicComboBoxUI.getDisplaySize()

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

Creates a new UI object for the given component.

**Parameters:** c

- component to create UI object for
**Returns:** the UI object

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Creates a new UI object for the given component.

installUI

```java
public void installUI​(
JComponent
c)
```

Configures the specified component appropriately for the look and feel.
This method is invoked when the

ComponentUI

instance is being installed
as the UI delegate on the specified component. This method should
completely configure the component for the look and feel,
including the following:

- Install default property values for color, fonts, borders,
icons, opacity, etc. on the component. Whenever possible,
property values initialized by the client program should

not

be overridden.

Install a

LayoutManager

on the component if necessary.

Create/add any required sub-components to the component.

Create/install event listeners on the component.

Create/install a

PropertyChangeListener

on the component in order
to detect and respond to component property changes appropriately.

Install keyboard UI (mnemonics, traversal, etc.) on the component.

Initialize any appropriate instance data.

Overridden to ensure that ButtonHandler is created prior to any of
the other installXXX methods, since several of them reference
buttonHandler.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

---

#### installUI

public void installUI​(

JComponent

c)

Configures the specified component appropriately for the look and feel.
This method is invoked when the

ComponentUI

instance is being installed
as the UI delegate on the specified component. This method should
completely configure the component for the look and feel,
including the following:

- Install default property values for color, fonts, borders,
icons, opacity, etc. on the component. Whenever possible,
property values initialized by the client program should

not

be overridden.

Install a

LayoutManager

on the component if necessary.

Create/add any required sub-components to the component.

Create/install event listeners on the component.

Create/install a

PropertyChangeListener

on the component in order
to detect and respond to component property changes appropriately.

Install keyboard UI (mnemonics, traversal, etc.) on the component.

Initialize any appropriate instance data.

Overridden to ensure that ButtonHandler is created prior to any of
the other installXXX methods, since several of them reference
buttonHandler.

Install default property values for color, fonts, borders,
icons, opacity, etc. on the component. Whenever possible,
property values initialized by the client program should

not

be overridden.

Install a

LayoutManager

on the component if necessary.

Create/add any required sub-components to the component.

Create/install event listeners on the component.

Create/install a

PropertyChangeListener

on the component in order
to detect and respond to component property changes appropriately.

Install keyboard UI (mnemonics, traversal, etc.) on the component.

Initialize any appropriate instance data.

update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

---

#### update

public void update​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

---

#### paint

public void paint​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

---

#### paint

protected void paint​(

SynthContext

context,

Graphics

g)

Paints the specified component.

paintCurrentValue

```java
public void paintCurrentValue​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

Paints the currently selected item.

**Overrides:** paintCurrentValue

in class

BasicComboBoxUI
**Parameters:** g

- an instance of

Graphics
**Parameters:** bounds

- a bounding rectangle to render to
**Parameters:** hasFocus

- is focused

---

#### paintCurrentValue

public void paintCurrentValue​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

Paints the currently selected item.

getDefaultSize

```java
protected
Dimension
getDefaultSize()
```

Returns the default size of an empty display area of the combo box using
the current renderer and font.

This method was overridden to use SynthComboBoxRenderer instead of
DefaultListCellRenderer as the default renderer when calculating the
size of the combo box. This is used in the case of the combo not having
any data.

**Overrides:** getDefaultSize

in class

BasicComboBoxUI
**Returns:** the size of an empty display area
**See Also:** BasicComboBoxUI.getDisplaySize()

---

#### getDefaultSize

protected

Dimension

getDefaultSize()

Returns the default size of an empty display area of the combo box using
the current renderer and font.

This method was overridden to use SynthComboBoxRenderer instead of
DefaultListCellRenderer as the default renderer when calculating the
size of the combo box. This is used in the case of the combo not having
any data.

---

