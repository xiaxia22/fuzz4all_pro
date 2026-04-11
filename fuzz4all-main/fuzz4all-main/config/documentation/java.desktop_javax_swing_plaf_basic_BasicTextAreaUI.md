# Class BasicTextAreaUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicTextAreaUI.html`

### Class Description

```java
public class
BasicTextAreaUI

extends
BasicTextUI
```

Provides the look and feel for a plain text editor. In this
implementation the default UI is extended to act as a simple
view factory.

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

**All Implemented Interfaces:** ViewFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public BasicTextAreaUI()

Constructs a new BasicTextAreaUI object.

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
ta)

Creates a UI for a JTextArea.

**Parameters:**
- ta

- a text area

**Returns:**
- the UI

---

#### protected
String
getPropertyPrefix()

Fetches the name used as a key to look up properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Specified by:**
- getPropertyPrefix

in class

BasicTextUI

**Returns:**
- the name ("TextArea")

---

#### protected void propertyChange​(
PropertyChangeEvent
evt)

This method gets called when a bound property is changed
on the associated JTextComponent. This is a hook
which UI implementations may change to reflect how the
UI displays bound properties of JTextComponent subclasses.
This is implemented to rebuild the View when the

WrapLine

or the

WrapStyleWord

property changes.

**Overrides:**
- propertyChange

in class

BasicTextUI

**Parameters:**
- evt

- the property change event

---

#### public
Dimension
getPreferredSize​(
JComponent
c)

The method is overridden to take into account caret width.

**Overrides:**
- getPreferredSize

in class

BasicTextUI

**Parameters:**
- c

- the editor component

**Returns:**
- the preferred size

**Throws:**
- IllegalArgumentException

- if invalid value is passed

**See Also:**
- JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

**Since:**
- 1.5

---

#### public
Dimension
getMinimumSize​(
JComponent
c)

The method is overridden to take into account caret width.

**Overrides:**
- getMinimumSize

in class

BasicTextUI

**Parameters:**
- c

- the editor component

**Returns:**
- the minimum size

**Throws:**
- IllegalArgumentException

- if invalid value is passed

**See Also:**
- JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

**Since:**
- 1.5

---

#### public
View
create​(
Element
elem)

Creates the view for an element. Returns a WrappedPlainView or
PlainView.

**Specified by:**
- create

in interface

ViewFactory

**Overrides:**
- create

in class

BasicTextUI

**Parameters:**
- elem

- the element

**Returns:**
- the view

**See Also:**
- View

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

ComponentUI

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

#### public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:**
- getBaselineResizeBehavior

in class

ComponentUI

**Parameters:**
- c

-

JComponent

to return baseline resize behavior for

**Returns:**
- an enum indicating how the baseline changes as the component
size changes

**Throws:**
- NullPointerException

- if

c

is

null

**See Also:**
- JComponent.getBaseline(int, int)

**Since:**
- 1.6

---

### Additional Sections

#### Class BasicTextAreaUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextAreaUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextAreaUI

javax.swing.plaf.TextUI

- javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextAreaUI

javax.swing.plaf.basic.BasicTextUI

- javax.swing.plaf.basic.BasicTextAreaUI

javax.swing.plaf.basic.BasicTextAreaUI

**All Implemented Interfaces:** ViewFactory

**Direct Known Subclasses:** SynthTextAreaUI

```java
public class
BasicTextAreaUI

extends
BasicTextUI
```

Provides the look and feel for a plain text editor. In this
implementation the default UI is extended to act as a simple
view factory.

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

public class

BasicTextAreaUI

extends

BasicTextUI

Provides the look and feel for a plain text editor. In this
implementation the default UI is extended to act as a simple
view factory.

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

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTextUI

BasicTextUI.BasicCaret

,

BasicTextUI.BasicHighlighter

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicTextAreaUI

()

Constructs a new BasicTextAreaUI object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

View

create

​(

Element

elem)

Creates the view for an element.

static

ComponentUI

createUI

​(

JComponent

ta)

Creates a UI for a JTextArea.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

Dimension

getMinimumSize

​(

JComponent

c)

The method is overridden to take into account caret width.

Dimension

getPreferredSize

​(

JComponent

c)

The method is overridden to take into account caret width.

protected

String

getPropertyPrefix

()

Fetches the name used as a key to look up properties through the
UIManager.

protected void

propertyChange

​(

PropertyChangeEvent

evt)

This method gets called when a bound property is changed
on the associated JTextComponent.

- Methods declared in class javax.swing.plaf.basic.

BasicTextUI

create

,

createCaret

,

createHighlighter

,

createKeymap

,

damageRange

,

damageRange

,

getComponent

,

getEditorKit

,

getKeymapName

,

getMaximumSize

,

getRootView

,

getToolTipText

,

getVisibleEditorRect

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

modelChanged

,

modelToView

,

modelToView

,

paint

,

paintBackground

,

paintSafely

,

setView

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

,

update

,

viewToModel

,

viewToModel

- Methods declared in class javax.swing.plaf.

TextUI

getNextVisualPositionFrom

,

getToolTipText2D

,

modelToView2D

,

viewToModel2D

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTextUI

BasicTextUI.BasicCaret

,

BasicTextUI.BasicHighlighter

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTextUI

BasicTextUI.BasicCaret

,

BasicTextUI.BasicHighlighter

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicTextUI

Constructor Summary

Constructors

Constructor

Description

BasicTextAreaUI

()

Constructs a new BasicTextAreaUI object.

---

#### Constructor Summary

Constructs a new BasicTextAreaUI object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

View

create

​(

Element

elem)

Creates the view for an element.

static

ComponentUI

createUI

​(

JComponent

ta)

Creates a UI for a JTextArea.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

Dimension

getMinimumSize

​(

JComponent

c)

The method is overridden to take into account caret width.

Dimension

getPreferredSize

​(

JComponent

c)

The method is overridden to take into account caret width.

protected

String

getPropertyPrefix

()

Fetches the name used as a key to look up properties through the
UIManager.

protected void

propertyChange

​(

PropertyChangeEvent

evt)

This method gets called when a bound property is changed
on the associated JTextComponent.

- Methods declared in class javax.swing.plaf.basic.

BasicTextUI

create

,

createCaret

,

createHighlighter

,

createKeymap

,

damageRange

,

damageRange

,

getComponent

,

getEditorKit

,

getKeymapName

,

getMaximumSize

,

getRootView

,

getToolTipText

,

getVisibleEditorRect

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

modelChanged

,

modelToView

,

modelToView

,

paint

,

paintBackground

,

paintSafely

,

setView

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

,

update

,

viewToModel

,

viewToModel

- Methods declared in class javax.swing.plaf.

TextUI

getNextVisualPositionFrom

,

getToolTipText2D

,

modelToView2D

,

viewToModel2D

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

Creates the view for an element.

Creates a UI for a JTextArea.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

The method is overridden to take into account caret width.

Fetches the name used as a key to look up properties through the
UIManager.

This method gets called when a bound property is changed
on the associated JTextComponent.

Methods declared in class javax.swing.plaf.basic.

BasicTextUI

create

,

createCaret

,

createHighlighter

,

createKeymap

,

damageRange

,

damageRange

,

getComponent

,

getEditorKit

,

getKeymapName

,

getMaximumSize

,

getRootView

,

getToolTipText

,

getVisibleEditorRect

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

modelChanged

,

modelToView

,

modelToView

,

paint

,

paintBackground

,

paintSafely

,

setView

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

,

update

,

viewToModel

,

viewToModel

---

#### Methods declared in class javax.swing.plaf.basic. BasicTextUI

Methods declared in class javax.swing.plaf.

TextUI

getNextVisualPositionFrom

,

getToolTipText2D

,

modelToView2D

,

viewToModel2D

---

#### Methods declared in class javax.swing.plaf. TextUI

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

- BasicTextAreaUI

```java
public BasicTextAreaUI()
```

Constructs a new BasicTextAreaUI object.

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
ta)
```

Creates a UI for a JTextArea.

**Parameters:** ta

- a text area
**Returns:** the UI

- getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Fetches the name used as a key to look up properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Specified by:** getPropertyPrefix

in class

BasicTextUI
**Returns:** the name ("TextArea")

- propertyChange

```java
protected void propertyChange​(
PropertyChangeEvent
evt)
```

This method gets called when a bound property is changed
on the associated JTextComponent. This is a hook
which UI implementations may change to reflect how the
UI displays bound properties of JTextComponent subclasses.
This is implemented to rebuild the View when the

WrapLine

or the

WrapStyleWord

property changes.

**Overrides:** propertyChange

in class

BasicTextUI
**Parameters:** evt

- the property change event

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

The method is overridden to take into account caret width.

**Overrides:** getPreferredSize

in class

BasicTextUI
**Parameters:** c

- the editor component
**Returns:** the preferred size
**Throws:** IllegalArgumentException

- if invalid value is passed
**Since:** 1.5
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

The method is overridden to take into account caret width.

**Overrides:** getMinimumSize

in class

BasicTextUI
**Parameters:** c

- the editor component
**Returns:** the minimum size
**Throws:** IllegalArgumentException

- if invalid value is passed
**Since:** 1.5
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- create

```java
public
View
create​(
Element
elem)
```

Creates the view for an element. Returns a WrappedPlainView or
PlainView.

**Specified by:** create

in interface

ViewFactory
**Overrides:** create

in class

BasicTextUI
**Parameters:** elem

- the element
**Returns:** the view
**See Also:** View

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

ComponentUI
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

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

Constructor Detail

- BasicTextAreaUI

```java
public BasicTextAreaUI()
```

Constructs a new BasicTextAreaUI object.

---

#### Constructor Detail

BasicTextAreaUI

```java
public BasicTextAreaUI()
```

Constructs a new BasicTextAreaUI object.

---

#### BasicTextAreaUI

public BasicTextAreaUI()

Constructs a new BasicTextAreaUI object.

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
ta)
```

Creates a UI for a JTextArea.

**Parameters:** ta

- a text area
**Returns:** the UI

- getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Fetches the name used as a key to look up properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Specified by:** getPropertyPrefix

in class

BasicTextUI
**Returns:** the name ("TextArea")

- propertyChange

```java
protected void propertyChange​(
PropertyChangeEvent
evt)
```

This method gets called when a bound property is changed
on the associated JTextComponent. This is a hook
which UI implementations may change to reflect how the
UI displays bound properties of JTextComponent subclasses.
This is implemented to rebuild the View when the

WrapLine

or the

WrapStyleWord

property changes.

**Overrides:** propertyChange

in class

BasicTextUI
**Parameters:** evt

- the property change event

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

The method is overridden to take into account caret width.

**Overrides:** getPreferredSize

in class

BasicTextUI
**Parameters:** c

- the editor component
**Returns:** the preferred size
**Throws:** IllegalArgumentException

- if invalid value is passed
**Since:** 1.5
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

The method is overridden to take into account caret width.

**Overrides:** getMinimumSize

in class

BasicTextUI
**Parameters:** c

- the editor component
**Returns:** the minimum size
**Throws:** IllegalArgumentException

- if invalid value is passed
**Since:** 1.5
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- create

```java
public
View
create​(
Element
elem)
```

Creates the view for an element. Returns a WrappedPlainView or
PlainView.

**Specified by:** create

in interface

ViewFactory
**Overrides:** create

in class

BasicTextUI
**Parameters:** elem

- the element
**Returns:** the view
**See Also:** View

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

ComponentUI
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

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
ta)
```

Creates a UI for a JTextArea.

**Parameters:** ta

- a text area
**Returns:** the UI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

ta)

Creates a UI for a JTextArea.

getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Fetches the name used as a key to look up properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Specified by:** getPropertyPrefix

in class

BasicTextUI
**Returns:** the name ("TextArea")

---

#### getPropertyPrefix

protected

String

getPropertyPrefix()

Fetches the name used as a key to look up properties through the
UIManager. This is used as a prefix to all the standard
text properties.

propertyChange

```java
protected void propertyChange​(
PropertyChangeEvent
evt)
```

This method gets called when a bound property is changed
on the associated JTextComponent. This is a hook
which UI implementations may change to reflect how the
UI displays bound properties of JTextComponent subclasses.
This is implemented to rebuild the View when the

WrapLine

or the

WrapStyleWord

property changes.

**Overrides:** propertyChange

in class

BasicTextUI
**Parameters:** evt

- the property change event

---

#### propertyChange

protected void propertyChange​(

PropertyChangeEvent

evt)

This method gets called when a bound property is changed
on the associated JTextComponent. This is a hook
which UI implementations may change to reflect how the
UI displays bound properties of JTextComponent subclasses.
This is implemented to rebuild the View when the

WrapLine

or the

WrapStyleWord

property changes.

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

The method is overridden to take into account caret width.

**Overrides:** getPreferredSize

in class

BasicTextUI
**Parameters:** c

- the editor component
**Returns:** the preferred size
**Throws:** IllegalArgumentException

- if invalid value is passed
**Since:** 1.5
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### getPreferredSize

public

Dimension

getPreferredSize​(

JComponent

c)

The method is overridden to take into account caret width.

getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

The method is overridden to take into account caret width.

**Overrides:** getMinimumSize

in class

BasicTextUI
**Parameters:** c

- the editor component
**Returns:** the minimum size
**Throws:** IllegalArgumentException

- if invalid value is passed
**Since:** 1.5
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

---

#### getMinimumSize

public

Dimension

getMinimumSize​(

JComponent

c)

The method is overridden to take into account caret width.

create

```java
public
View
create​(
Element
elem)
```

Creates the view for an element. Returns a WrappedPlainView or
PlainView.

**Specified by:** create

in interface

ViewFactory
**Overrides:** create

in class

BasicTextUI
**Parameters:** elem

- the element
**Returns:** the view
**See Also:** View

---

#### create

public

View

create​(

Element

elem)

Creates the view for an element. Returns a WrappedPlainView or
PlainView.

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

ComponentUI
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

getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### getBaselineResizeBehavior

public

Component.BaselineResizeBehavior

getBaselineResizeBehavior​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

---

