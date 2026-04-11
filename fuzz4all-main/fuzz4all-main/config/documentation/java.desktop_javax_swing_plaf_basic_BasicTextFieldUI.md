# Class BasicTextFieldUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicTextFieldUI.html`

### Class Description

```java
public class
BasicTextFieldUI

extends
BasicTextUI
```

Basis of a look and feel for a JTextField.

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

#### public BasicTextFieldUI()

Creates a new BasicTextFieldUI.

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Creates a UI for a JTextField.

**Parameters:**
- c

- the text field

**Returns:**
- the UI

---

#### protected
String
getPropertyPrefix()

Fetches the name used as a key to lookup properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Specified by:**
- getPropertyPrefix

in class

BasicTextUI

**Returns:**
- the name ("TextField")

---

#### public
View
create​(
Element
elem)

Creates a view (FieldView) based on an element.

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

#### Class BasicTextFieldUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI

javax.swing.plaf.TextUI

- javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI

javax.swing.plaf.basic.BasicTextUI

- javax.swing.plaf.basic.BasicTextFieldUI

javax.swing.plaf.basic.BasicTextFieldUI

**All Implemented Interfaces:** ViewFactory

**Direct Known Subclasses:** BasicFormattedTextFieldUI

,

BasicPasswordFieldUI

,

MetalTextFieldUI

,

SynthTextFieldUI

```java
public class
BasicTextFieldUI

extends
BasicTextUI
```

Basis of a look and feel for a JTextField.

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

BasicTextFieldUI

extends

BasicTextUI

Basis of a look and feel for a JTextField.

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

BasicTextFieldUI

()

Creates a new BasicTextFieldUI.

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

Creates a view (FieldView) based on an element.

static

ComponentUI

createUI

​(

JComponent

c)

Creates a UI for a JTextField.

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

protected

String

getPropertyPrefix

()

Fetches the name used as a key to lookup properties through the
UIManager.

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

getMinimumSize

,

getPreferredSize

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

propertyChange

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

BasicTextFieldUI

()

Creates a new BasicTextFieldUI.

---

#### Constructor Summary

Creates a new BasicTextFieldUI.

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

Creates a view (FieldView) based on an element.

static

ComponentUI

createUI

​(

JComponent

c)

Creates a UI for a JTextField.

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

protected

String

getPropertyPrefix

()

Fetches the name used as a key to lookup properties through the
UIManager.

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

getMinimumSize

,

getPreferredSize

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

propertyChange

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

Creates a view (FieldView) based on an element.

Creates a UI for a JTextField.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Fetches the name used as a key to lookup properties through the
UIManager.

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

getMinimumSize

,

getPreferredSize

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

propertyChange

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

- BasicTextFieldUI

```java
public BasicTextFieldUI()
```

Creates a new BasicTextFieldUI.

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

Creates a UI for a JTextField.

**Parameters:** c

- the text field
**Returns:** the UI

- getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Fetches the name used as a key to lookup properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Specified by:** getPropertyPrefix

in class

BasicTextUI
**Returns:** the name ("TextField")

- create

```java
public
View
create​(
Element
elem)
```

Creates a view (FieldView) based on an element.

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

- BasicTextFieldUI

```java
public BasicTextFieldUI()
```

Creates a new BasicTextFieldUI.

---

#### Constructor Detail

BasicTextFieldUI

```java
public BasicTextFieldUI()
```

Creates a new BasicTextFieldUI.

---

#### BasicTextFieldUI

public BasicTextFieldUI()

Creates a new BasicTextFieldUI.

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates a UI for a JTextField.

**Parameters:** c

- the text field
**Returns:** the UI

- getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Fetches the name used as a key to lookup properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Specified by:** getPropertyPrefix

in class

BasicTextUI
**Returns:** the name ("TextField")

- create

```java
public
View
create​(
Element
elem)
```

Creates a view (FieldView) based on an element.

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
c)
```

Creates a UI for a JTextField.

**Parameters:** c

- the text field
**Returns:** the UI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Creates a UI for a JTextField.

getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Fetches the name used as a key to lookup properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Specified by:** getPropertyPrefix

in class

BasicTextUI
**Returns:** the name ("TextField")

---

#### getPropertyPrefix

protected

String

getPropertyPrefix()

Fetches the name used as a key to lookup properties through the
UIManager. This is used as a prefix to all the standard
text properties.

create

```java
public
View
create​(
Element
elem)
```

Creates a view (FieldView) based on an element.

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

Creates a view (FieldView) based on an element.

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

