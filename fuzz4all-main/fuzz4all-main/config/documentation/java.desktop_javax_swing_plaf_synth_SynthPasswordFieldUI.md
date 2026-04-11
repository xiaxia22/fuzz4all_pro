# Class SynthPasswordFieldUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthPasswordFieldUI.html`

### Class Description

```java
public class
SynthPasswordFieldUI

extends
SynthTextFieldUI
```

Provides the Synth L&F UI delegate for

JPasswordField

.

**All Implemented Interfaces:** SynthConstants

,

SynthUI

,

ViewFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthPasswordFieldUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Creates a UI for a JPasswordField.

**Parameters:**
- c

- the JPasswordField

**Returns:**
- the UI

---

#### protected
String
getPropertyPrefix()

Fetches the name used as a key to look up properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Overrides:**
- getPropertyPrefix

in class

BasicTextFieldUI

**Returns:**
- the name ("PasswordField")

---

#### public
View
create​(
Element
elem)

Creates a view (PasswordView) for an element.

**Specified by:**
- create

in interface

ViewFactory

**Overrides:**
- create

in class

BasicTextFieldUI

**Parameters:**
- elem

- the element

**Returns:**
- the view

**See Also:**
- View

---

### Additional Sections

#### Class SynthPasswordFieldUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.synth.SynthTextFieldUI
- - javax.swing.plaf.synth.SynthPasswordFieldUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.synth.SynthTextFieldUI
- - javax.swing.plaf.synth.SynthPasswordFieldUI

javax.swing.plaf.TextUI

- javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.synth.SynthTextFieldUI
- - javax.swing.plaf.synth.SynthPasswordFieldUI

javax.swing.plaf.basic.BasicTextUI

- javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.synth.SynthTextFieldUI
- - javax.swing.plaf.synth.SynthPasswordFieldUI

javax.swing.plaf.basic.BasicTextFieldUI

- javax.swing.plaf.synth.SynthTextFieldUI
- - javax.swing.plaf.synth.SynthPasswordFieldUI

javax.swing.plaf.synth.SynthTextFieldUI

- javax.swing.plaf.synth.SynthPasswordFieldUI

javax.swing.plaf.synth.SynthPasswordFieldUI

**All Implemented Interfaces:** SynthConstants

,

SynthUI

,

ViewFactory

```java
public class
SynthPasswordFieldUI

extends
SynthTextFieldUI
```

Provides the Synth L&F UI delegate for

JPasswordField

.

**Since:** 1.7

public class

SynthPasswordFieldUI

extends

SynthTextFieldUI

Provides the Synth L&F UI delegate for

JPasswordField

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTextUI

BasicTextUI.BasicCaret

,

BasicTextUI.BasicHighlighter

=========== FIELD SUMMARY ===========

- Field Summary

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

SynthPasswordFieldUI

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

View

create

​(

Element

elem)

Creates a view (PasswordView) for an element.

static

ComponentUI

createUI

​(

JComponent

c)

Creates a UI for a JPasswordField.

protected

String

getPropertyPrefix

()

Fetches the name used as a key to look up properties through the
UIManager.

- Methods declared in class javax.swing.plaf.synth.

SynthTextFieldUI

paint

,

paintBackground

,

propertyChange

,

update

- Methods declared in class javax.swing.plaf.basic.

BasicTextFieldUI

getBaseline

,

getBaselineResizeBehavior

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

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

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

Field Summary

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

SynthPasswordFieldUI

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

View

create

​(

Element

elem)

Creates a view (PasswordView) for an element.

static

ComponentUI

createUI

​(

JComponent

c)

Creates a UI for a JPasswordField.

protected

String

getPropertyPrefix

()

Fetches the name used as a key to look up properties through the
UIManager.

- Methods declared in class javax.swing.plaf.synth.

SynthTextFieldUI

paint

,

paintBackground

,

propertyChange

,

update

- Methods declared in class javax.swing.plaf.basic.

BasicTextFieldUI

getBaseline

,

getBaselineResizeBehavior

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

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Method Summary

Creates a view (PasswordView) for an element.

Creates a UI for a JPasswordField.

Fetches the name used as a key to look up properties through the
UIManager.

Methods declared in class javax.swing.plaf.synth.

SynthTextFieldUI

paint

,

paintBackground

,

propertyChange

,

update

---

#### Methods declared in class javax.swing.plaf.synth. SynthTextFieldUI

Methods declared in class javax.swing.plaf.basic.

BasicTextFieldUI

getBaseline

,

getBaselineResizeBehavior

---

#### Methods declared in class javax.swing.plaf.basic. BasicTextFieldUI

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

Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Methods declared in interface javax.swing.plaf.synth. SynthUI

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SynthPasswordFieldUI

```java
public SynthPasswordFieldUI()
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

Creates a UI for a JPasswordField.

**Parameters:** c

- the JPasswordField
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

**Overrides:** getPropertyPrefix

in class

BasicTextFieldUI
**Returns:** the name ("PasswordField")

- create

```java
public
View
create​(
Element
elem)
```

Creates a view (PasswordView) for an element.

**Specified by:** create

in interface

ViewFactory
**Overrides:** create

in class

BasicTextFieldUI
**Parameters:** elem

- the element
**Returns:** the view
**See Also:** View

Constructor Detail

- SynthPasswordFieldUI

```java
public SynthPasswordFieldUI()
```

---

#### Constructor Detail

SynthPasswordFieldUI

```java
public SynthPasswordFieldUI()
```

---

#### SynthPasswordFieldUI

public SynthPasswordFieldUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates a UI for a JPasswordField.

**Parameters:** c

- the JPasswordField
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

**Overrides:** getPropertyPrefix

in class

BasicTextFieldUI
**Returns:** the name ("PasswordField")

- create

```java
public
View
create​(
Element
elem)
```

Creates a view (PasswordView) for an element.

**Specified by:** create

in interface

ViewFactory
**Overrides:** create

in class

BasicTextFieldUI
**Parameters:** elem

- the element
**Returns:** the view
**See Also:** View

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

Creates a UI for a JPasswordField.

**Parameters:** c

- the JPasswordField
**Returns:** the UI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Creates a UI for a JPasswordField.

getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Fetches the name used as a key to look up properties through the
UIManager. This is used as a prefix to all the standard
text properties.

**Overrides:** getPropertyPrefix

in class

BasicTextFieldUI
**Returns:** the name ("PasswordField")

---

#### getPropertyPrefix

protected

String

getPropertyPrefix()

Fetches the name used as a key to look up properties through the
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

Creates a view (PasswordView) for an element.

**Specified by:** create

in interface

ViewFactory
**Overrides:** create

in class

BasicTextFieldUI
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

Creates a view (PasswordView) for an element.

---

