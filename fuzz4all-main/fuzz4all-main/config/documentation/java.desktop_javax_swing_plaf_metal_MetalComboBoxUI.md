# Class MetalComboBoxUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalComboBoxUI.html`

### Class Description

```java
public class
MetalComboBoxUI

extends
BasicComboBoxUI
```

Metal UI for JComboBox

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

**See Also:** MetalComboBoxEditor

,

MetalComboBoxButton

---

### Field Details

*No entries found.*

### Constructor Details

#### public MetalComboBoxUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Constructs an instance of

MetalComboBoxUI

.

**Parameters:**
- c

- a component

**Returns:**
- an instance of

MetalComboBoxUI

---

#### public void paintCurrentValue​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)

If necessary paints the currently selected item.

**Overrides:**
- paintCurrentValue

in class

BasicComboBoxUI

**Parameters:**
- g

- Graphics to paint to
- bounds

- Region to paint current value to
- hasFocus

- whether or not the JComboBox has focus

**Throws:**
- NullPointerException

- if any of the arguments are null.

**Since:**
- 1.5

---

#### public void paintCurrentValueBackground​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)

If necessary paints the background of the currently selected item.

**Overrides:**
- paintCurrentValueBackground

in class

BasicComboBoxUI

**Parameters:**
- g

- Graphics to paint to
- bounds

- Region to paint background to
- hasFocus

- whether or not the JComboBox has focus

**Throws:**
- NullPointerException

- if any of the arguments are null.

**Since:**
- 1.5

---

#### public int getBaseline​(
JComponent
c,
int width,
int height)

Returns the baseline.

**Overrides:**
- getBaseline

in class

BasicComboBoxUI

**Parameters:**
- c

-

JComponent

baseline is being requested for
- width

- the width to get the baseline for
- height

- the height to get the baseline for

**Returns:**
- baseline or a value < 0 indicating there is no reasonable
baseline

**Throws:**
- NullPointerException

- if

c

is

null
- IllegalArgumentException

- if width or height is < 0

**See Also:**
- JComponent.getBaseline(int, int)

**Since:**
- 1.6

---

#### @Deprecated

protected void editablePropertyChanged​(
PropertyChangeEvent
e)

As of Java 2 platform v1.4 this method is no longer used. Do not call or
override. All the functionality of this method is in the
MetalPropertyChangeListener.

**Parameters:**
- e

- an instance of

PropertyChangeEvent

---

#### public void layoutComboBox​(
Container
parent,

MetalComboBoxUI.MetalComboBoxLayoutManager
manager)

Lays out the

JComboBox

in the

parent

container.

**Parameters:**
- parent

- a container
- manager

- an instance of

MetalComboBoxLayoutManager

---

#### @Deprecated

protected void removeListeners()

As of Java 2 platform v1.4 this method is no
longer used.

---

### Additional Sections

#### Class MetalComboBoxUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ComboBoxUI
- - javax.swing.plaf.basic.BasicComboBoxUI
- - javax.swing.plaf.metal.MetalComboBoxUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ComboBoxUI
- - javax.swing.plaf.basic.BasicComboBoxUI
- - javax.swing.plaf.metal.MetalComboBoxUI

javax.swing.plaf.ComboBoxUI

- javax.swing.plaf.basic.BasicComboBoxUI
- - javax.swing.plaf.metal.MetalComboBoxUI

javax.swing.plaf.basic.BasicComboBoxUI

- javax.swing.plaf.metal.MetalComboBoxUI

javax.swing.plaf.metal.MetalComboBoxUI

```java
public class
MetalComboBoxUI

extends
BasicComboBoxUI
```

Metal UI for JComboBox

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

**See Also:** MetalComboBoxEditor

,

MetalComboBoxButton

public class

MetalComboBoxUI

extends

BasicComboBoxUI

Metal UI for JComboBox

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

class

MetalComboBoxUI.MetalComboBoxLayoutManager

This class should be treated as a "protected" inner class.

class

MetalComboBoxUI.MetalComboPopup

Deprecated.

As of Java 2 platform v1.4.

class

MetalComboBoxUI.MetalPropertyChangeListener

This class should be treated as a "protected" inner class.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MetalComboBoxUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

ComponentUI

createUI

​(

JComponent

c)

Constructs an instance of

MetalComboBoxUI

.

protected void

editablePropertyChanged

​(

PropertyChangeEvent

e)

Deprecated.

As of Java 2 platform v1.4.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

void

layoutComboBox

​(

Container

parent,

MetalComboBoxUI.MetalComboBoxLayoutManager

manager)

Lays out the

JComboBox

in the

parent

container.

void

paintCurrentValue

​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

If necessary paints the currently selected item.

void

paintCurrentValueBackground

​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

If necessary paints the background of the currently selected item.

protected void

removeListeners

()

Deprecated.

As of Java 2 platform v1.4.

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

getBaselineResizeBehavior

,

getDefaultSize

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

installUI

,

paint

,

uninstallUI

,

update

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

class

MetalComboBoxUI.MetalComboBoxLayoutManager

This class should be treated as a "protected" inner class.

class

MetalComboBoxUI.MetalComboPopup

Deprecated.

As of Java 2 platform v1.4.

class

MetalComboBoxUI.MetalPropertyChangeListener

This class should be treated as a "protected" inner class.

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

This class should be treated as a "protected" inner class.

Deprecated.

As of Java 2 platform v1.4.

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

Constructor Summary

Constructors

Constructor

Description

MetalComboBoxUI

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

ComponentUI

createUI

​(

JComponent

c)

Constructs an instance of

MetalComboBoxUI

.

protected void

editablePropertyChanged

​(

PropertyChangeEvent

e)

Deprecated.

As of Java 2 platform v1.4.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

void

layoutComboBox

​(

Container

parent,

MetalComboBoxUI.MetalComboBoxLayoutManager

manager)

Lays out the

JComboBox

in the

parent

container.

void

paintCurrentValue

​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

If necessary paints the currently selected item.

void

paintCurrentValueBackground

​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

If necessary paints the background of the currently selected item.

protected void

removeListeners

()

Deprecated.

As of Java 2 platform v1.4.

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

getBaselineResizeBehavior

,

getDefaultSize

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

installUI

,

paint

,

uninstallUI

,

update

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

Constructs an instance of

MetalComboBoxUI

.

Deprecated.

As of Java 2 platform v1.4.

Returns the baseline.

Lays out the

JComboBox

in the

parent

container.

If necessary paints the currently selected item.

If necessary paints the background of the currently selected item.

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

getBaselineResizeBehavior

,

getDefaultSize

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

installUI

,

paint

,

uninstallUI

,

update

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalComboBoxUI

```java
public MetalComboBoxUI()
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

Constructs an instance of

MetalComboBoxUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalComboBoxUI

- paintCurrentValue

```java
public void paintCurrentValue​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

If necessary paints the currently selected item.

**Overrides:** paintCurrentValue

in class

BasicComboBoxUI
**Parameters:** g

- Graphics to paint to
**Parameters:** bounds

- Region to paint current value to
**Parameters:** hasFocus

- whether or not the JComboBox has focus
**Throws:** NullPointerException

- if any of the arguments are null.
**Since:** 1.5

- paintCurrentValueBackground

```java
public void paintCurrentValueBackground​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

If necessary paints the background of the currently selected item.

**Overrides:** paintCurrentValueBackground

in class

BasicComboBoxUI
**Parameters:** g

- Graphics to paint to
**Parameters:** bounds

- Region to paint background to
**Parameters:** hasFocus

- whether or not the JComboBox has focus
**Throws:** NullPointerException

- if any of the arguments are null.
**Since:** 1.5

- getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

BasicComboBoxUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- editablePropertyChanged

```java
@Deprecated

protected void editablePropertyChanged​(
PropertyChangeEvent
e)
```

Deprecated.

As of Java 2 platform v1.4.

As of Java 2 platform v1.4 this method is no longer used. Do not call or
override. All the functionality of this method is in the
MetalPropertyChangeListener.

**Parameters:** e

- an instance of

PropertyChangeEvent

- layoutComboBox

```java
public void layoutComboBox​(
Container
parent,

MetalComboBoxUI.MetalComboBoxLayoutManager
manager)
```

Lays out the

JComboBox

in the

parent

container.

**Parameters:** parent

- a container
**Parameters:** manager

- an instance of

MetalComboBoxLayoutManager

- removeListeners

```java
@Deprecated

protected void removeListeners()
```

Deprecated.

As of Java 2 platform v1.4.

As of Java 2 platform v1.4 this method is no
longer used.

Constructor Detail

- MetalComboBoxUI

```java
public MetalComboBoxUI()
```

---

#### Constructor Detail

MetalComboBoxUI

```java
public MetalComboBoxUI()
```

---

#### MetalComboBoxUI

public MetalComboBoxUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs an instance of

MetalComboBoxUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalComboBoxUI

- paintCurrentValue

```java
public void paintCurrentValue​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

If necessary paints the currently selected item.

**Overrides:** paintCurrentValue

in class

BasicComboBoxUI
**Parameters:** g

- Graphics to paint to
**Parameters:** bounds

- Region to paint current value to
**Parameters:** hasFocus

- whether or not the JComboBox has focus
**Throws:** NullPointerException

- if any of the arguments are null.
**Since:** 1.5

- paintCurrentValueBackground

```java
public void paintCurrentValueBackground​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

If necessary paints the background of the currently selected item.

**Overrides:** paintCurrentValueBackground

in class

BasicComboBoxUI
**Parameters:** g

- Graphics to paint to
**Parameters:** bounds

- Region to paint background to
**Parameters:** hasFocus

- whether or not the JComboBox has focus
**Throws:** NullPointerException

- if any of the arguments are null.
**Since:** 1.5

- getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

BasicComboBoxUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- editablePropertyChanged

```java
@Deprecated

protected void editablePropertyChanged​(
PropertyChangeEvent
e)
```

Deprecated.

As of Java 2 platform v1.4.

As of Java 2 platform v1.4 this method is no longer used. Do not call or
override. All the functionality of this method is in the
MetalPropertyChangeListener.

**Parameters:** e

- an instance of

PropertyChangeEvent

- layoutComboBox

```java
public void layoutComboBox​(
Container
parent,

MetalComboBoxUI.MetalComboBoxLayoutManager
manager)
```

Lays out the

JComboBox

in the

parent

container.

**Parameters:** parent

- a container
**Parameters:** manager

- an instance of

MetalComboBoxLayoutManager

- removeListeners

```java
@Deprecated

protected void removeListeners()
```

Deprecated.

As of Java 2 platform v1.4.

As of Java 2 platform v1.4 this method is no
longer used.

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

Constructs an instance of

MetalComboBoxUI

.

**Parameters:** c

- a component
**Returns:** an instance of

MetalComboBoxUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Constructs an instance of

MetalComboBoxUI

.

paintCurrentValue

```java
public void paintCurrentValue​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

If necessary paints the currently selected item.

**Overrides:** paintCurrentValue

in class

BasicComboBoxUI
**Parameters:** g

- Graphics to paint to
**Parameters:** bounds

- Region to paint current value to
**Parameters:** hasFocus

- whether or not the JComboBox has focus
**Throws:** NullPointerException

- if any of the arguments are null.
**Since:** 1.5

---

#### paintCurrentValue

public void paintCurrentValue​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

If necessary paints the currently selected item.

paintCurrentValueBackground

```java
public void paintCurrentValueBackground​(
Graphics
g,

Rectangle
bounds,
boolean hasFocus)
```

If necessary paints the background of the currently selected item.

**Overrides:** paintCurrentValueBackground

in class

BasicComboBoxUI
**Parameters:** g

- Graphics to paint to
**Parameters:** bounds

- Region to paint background to
**Parameters:** hasFocus

- whether or not the JComboBox has focus
**Throws:** NullPointerException

- if any of the arguments are null.
**Since:** 1.5

---

#### paintCurrentValueBackground

public void paintCurrentValueBackground​(

Graphics

g,

Rectangle

bounds,
boolean hasFocus)

If necessary paints the background of the currently selected item.

getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

BasicComboBoxUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### getBaseline

public int getBaseline​(

JComponent

c,
int width,
int height)

Returns the baseline.

editablePropertyChanged

```java
@Deprecated

protected void editablePropertyChanged​(
PropertyChangeEvent
e)
```

Deprecated.

As of Java 2 platform v1.4.

As of Java 2 platform v1.4 this method is no longer used. Do not call or
override. All the functionality of this method is in the
MetalPropertyChangeListener.

**Parameters:** e

- an instance of

PropertyChangeEvent

---

#### editablePropertyChanged

@Deprecated

protected void editablePropertyChanged​(

PropertyChangeEvent

e)

As of Java 2 platform v1.4 this method is no longer used. Do not call or
override. All the functionality of this method is in the
MetalPropertyChangeListener.

layoutComboBox

```java
public void layoutComboBox​(
Container
parent,

MetalComboBoxUI.MetalComboBoxLayoutManager
manager)
```

Lays out the

JComboBox

in the

parent

container.

**Parameters:** parent

- a container
**Parameters:** manager

- an instance of

MetalComboBoxLayoutManager

---

#### layoutComboBox

public void layoutComboBox​(

Container

parent,

MetalComboBoxUI.MetalComboBoxLayoutManager

manager)

Lays out the

JComboBox

in the

parent

container.

removeListeners

```java
@Deprecated

protected void removeListeners()
```

Deprecated.

As of Java 2 platform v1.4.

As of Java 2 platform v1.4 this method is no
longer used.

---

#### removeListeners

@Deprecated

protected void removeListeners()

As of Java 2 platform v1.4 this method is no
longer used.

---

