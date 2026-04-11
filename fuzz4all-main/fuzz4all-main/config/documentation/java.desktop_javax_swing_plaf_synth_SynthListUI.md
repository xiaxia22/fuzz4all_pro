# Class SynthListUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthListUI.html`

### Class Description

```java
public class
SynthListUI

extends
BasicListUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JList

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

#### public SynthListUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
list)

Creates a new UI object for the given component.

**Parameters:**
- list

- component to create UI object for

**Returns:**
- the UI object

---

#### public void update​(
Graphics
g,

JComponent
c)

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

BasicListUI.paint(java.awt.Graphics, javax.swing.JComponent)

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
- BasicListUI.paint(java.awt.Graphics, javax.swing.JComponent)

---

### Additional Sections

#### Class SynthListUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ListUI
- - javax.swing.plaf.basic.BasicListUI
- - javax.swing.plaf.synth.SynthListUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ListUI
- - javax.swing.plaf.basic.BasicListUI
- - javax.swing.plaf.synth.SynthListUI

javax.swing.plaf.ListUI

- javax.swing.plaf.basic.BasicListUI
- - javax.swing.plaf.synth.SynthListUI

javax.swing.plaf.basic.BasicListUI

- javax.swing.plaf.synth.SynthListUI

javax.swing.plaf.synth.SynthListUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

```java
public class
SynthListUI

extends
BasicListUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JList

.

**Since:** 1.7

public class

SynthListUI

extends

BasicListUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JList

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicListUI

BasicListUI.FocusHandler

,

BasicListUI.ListDataHandler

,

BasicListUI.ListSelectionHandler

,

BasicListUI.MouseInputHandler

,

BasicListUI.PropertyChangeHandler

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicListUI

cellHeight

,

cellHeights

,

cellRendererChanged

,

cellWidth

,

fixedCellHeightChanged

,

fixedCellWidthChanged

,

focusListener

,

fontChanged

,

list

,

listDataListener

,

listSelectionListener

,

modelChanged

,

mouseInputListener

,

propertyChangeListener

,

prototypeCellValueChanged

,

rendererPane

,

selectionModelChanged

,

updateLayoutStateNeeded

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

SynthListUI

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

list)

Creates a new UI object for the given component.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicListUI

convertRowToY

,

convertYToRow

,

createFocusListener

,

createListDataListener

,

createListSelectionListener

,

createMouseInputListener

,

createPropertyChangeListener

,

getBaseline

,

getBaselineResizeBehavior

,

getPreferredSize

,

getRowHeight

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

locationToIndex

,

maybeUpdateLayoutState

,

paint

,

paintCell

,

selectNextIndex

,

selectPreviousIndex

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

,

updateLayoutState

- Methods declared in class javax.swing.plaf.

ListUI

getCellBounds

,

indexToLocation

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

getMinimumSize

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

BasicListUI

BasicListUI.FocusHandler

,

BasicListUI.ListDataHandler

,

BasicListUI.ListSelectionHandler

,

BasicListUI.MouseInputHandler

,

BasicListUI.PropertyChangeHandler

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicListUI

BasicListUI.FocusHandler

,

BasicListUI.ListDataHandler

,

BasicListUI.ListSelectionHandler

,

BasicListUI.MouseInputHandler

,

BasicListUI.PropertyChangeHandler

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicListUI

Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicListUI

cellHeight

,

cellHeights

,

cellRendererChanged

,

cellWidth

,

fixedCellHeightChanged

,

fixedCellWidthChanged

,

focusListener

,

fontChanged

,

list

,

listDataListener

,

listSelectionListener

,

modelChanged

,

mouseInputListener

,

propertyChangeListener

,

prototypeCellValueChanged

,

rendererPane

,

selectionModelChanged

,

updateLayoutStateNeeded

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

BasicListUI

cellHeight

,

cellHeights

,

cellRendererChanged

,

cellWidth

,

fixedCellHeightChanged

,

fixedCellWidthChanged

,

focusListener

,

fontChanged

,

list

,

listDataListener

,

listSelectionListener

,

modelChanged

,

mouseInputListener

,

propertyChangeListener

,

prototypeCellValueChanged

,

rendererPane

,

selectionModelChanged

,

updateLayoutStateNeeded

---

#### Fields declared in class javax.swing.plaf.basic. BasicListUI

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

SynthListUI

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

list)

Creates a new UI object for the given component.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicListUI

convertRowToY

,

convertYToRow

,

createFocusListener

,

createListDataListener

,

createListSelectionListener

,

createMouseInputListener

,

createPropertyChangeListener

,

getBaseline

,

getBaselineResizeBehavior

,

getPreferredSize

,

getRowHeight

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

locationToIndex

,

maybeUpdateLayoutState

,

paint

,

paintCell

,

selectNextIndex

,

selectPreviousIndex

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

,

updateLayoutState

- Methods declared in class javax.swing.plaf.

ListUI

getCellBounds

,

indexToLocation

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

getMinimumSize

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

Notifies this UI delegate to repaint the specified component.

Methods declared in class javax.swing.plaf.basic.

BasicListUI

convertRowToY

,

convertYToRow

,

createFocusListener

,

createListDataListener

,

createListSelectionListener

,

createMouseInputListener

,

createPropertyChangeListener

,

getBaseline

,

getBaselineResizeBehavior

,

getPreferredSize

,

getRowHeight

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

locationToIndex

,

maybeUpdateLayoutState

,

paint

,

paintCell

,

selectNextIndex

,

selectPreviousIndex

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

,

updateLayoutState

---

#### Methods declared in class javax.swing.plaf.basic. BasicListUI

Methods declared in class javax.swing.plaf.

ListUI

getCellBounds

,

indexToLocation

---

#### Methods declared in class javax.swing.plaf. ListUI

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

getMinimumSize

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

- SynthListUI

```java
public SynthListUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
list)
```

Creates a new UI object for the given component.

**Parameters:** list

- component to create UI object for
**Returns:** the UI object

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

BasicListUI.paint(java.awt.Graphics, javax.swing.JComponent)

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
**See Also:** BasicListUI.paint(java.awt.Graphics, javax.swing.JComponent)

Constructor Detail

- SynthListUI

```java
public SynthListUI()
```

---

#### Constructor Detail

SynthListUI

```java
public SynthListUI()
```

---

#### SynthListUI

public SynthListUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
list)
```

Creates a new UI object for the given component.

**Parameters:** list

- component to create UI object for
**Returns:** the UI object

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

BasicListUI.paint(java.awt.Graphics, javax.swing.JComponent)

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
**See Also:** BasicListUI.paint(java.awt.Graphics, javax.swing.JComponent)

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
list)
```

Creates a new UI object for the given component.

**Parameters:** list

- component to create UI object for
**Returns:** the UI object

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

list)

Creates a new UI object for the given component.

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

BasicListUI.paint(java.awt.Graphics, javax.swing.JComponent)

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
**See Also:** BasicListUI.paint(java.awt.Graphics, javax.swing.JComponent)

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

BasicListUI.paint(java.awt.Graphics, javax.swing.JComponent)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

---

