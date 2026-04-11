# Class BasicPasswordFieldUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicPasswordFieldUI.html`

### Class Description

```java
public class
BasicPasswordFieldUI

extends
BasicTextFieldUI
```

Provides the Windows look and feel for a password field.
The only difference from the standard text field is that
the view of the text is simply a string of the echo
character as specified in JPasswordField, rather than the
real text contained in the field.

**All Implemented Interfaces:** ViewFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public BasicPasswordFieldUI()

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

#### protected void installDefaults()

Installs the necessary properties on the JPasswordField.

**Overrides:**
- installDefaults

in class

BasicTextUI

**See Also:**
- BasicTextUI.uninstallDefaults()

,

BasicTextUI.installUI(javax.swing.JComponent)

**Since:**
- 1.6

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

#### Class BasicPasswordFieldUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.basic.BasicPasswordFieldUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TextUI
- - javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.basic.BasicPasswordFieldUI

javax.swing.plaf.TextUI

- javax.swing.plaf.basic.BasicTextUI
- - javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.basic.BasicPasswordFieldUI

javax.swing.plaf.basic.BasicTextUI

- javax.swing.plaf.basic.BasicTextFieldUI
- - javax.swing.plaf.basic.BasicPasswordFieldUI

javax.swing.plaf.basic.BasicTextFieldUI

- javax.swing.plaf.basic.BasicPasswordFieldUI

javax.swing.plaf.basic.BasicPasswordFieldUI

**All Implemented Interfaces:** ViewFactory

```java
public class
BasicPasswordFieldUI

extends
BasicTextFieldUI
```

Provides the Windows look and feel for a password field.
The only difference from the standard text field is that
the view of the text is simply a string of the echo
character as specified in JPasswordField, rather than the
real text contained in the field.

public class

BasicPasswordFieldUI

extends

BasicTextFieldUI

Provides the Windows look and feel for a password field.
The only difference from the standard text field is that
the view of the text is simply a string of the echo
character as specified in JPasswordField, rather than the
real text contained in the field.

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

BasicPasswordFieldUI

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

protected void

installDefaults

()

Installs the necessary properties on the JPasswordField.

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

BasicPasswordFieldUI

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

protected void

installDefaults

()

Installs the necessary properties on the JPasswordField.

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

Creates a view (PasswordView) for an element.

Creates a UI for a JPasswordField.

Fetches the name used as a key to look up properties through the
UIManager.

Installs the necessary properties on the JPasswordField.

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

- BasicPasswordFieldUI

```java
public BasicPasswordFieldUI()
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

- installDefaults

```java
protected void installDefaults()
```

Installs the necessary properties on the JPasswordField.

**Overrides:** installDefaults

in class

BasicTextUI
**Since:** 1.6
**See Also:** BasicTextUI.uninstallDefaults()

,

BasicTextUI.installUI(javax.swing.JComponent)

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

- BasicPasswordFieldUI

```java
public BasicPasswordFieldUI()
```

---

#### Constructor Detail

BasicPasswordFieldUI

```java
public BasicPasswordFieldUI()
```

---

#### BasicPasswordFieldUI

public BasicPasswordFieldUI()

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

- installDefaults

```java
protected void installDefaults()
```

Installs the necessary properties on the JPasswordField.

**Overrides:** installDefaults

in class

BasicTextUI
**Since:** 1.6
**See Also:** BasicTextUI.uninstallDefaults()

,

BasicTextUI.installUI(javax.swing.JComponent)

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

installDefaults

```java
protected void installDefaults()
```

Installs the necessary properties on the JPasswordField.

**Overrides:** installDefaults

in class

BasicTextUI
**Since:** 1.6
**See Also:** BasicTextUI.uninstallDefaults()

,

BasicTextUI.installUI(javax.swing.JComponent)

---

#### installDefaults

protected void installDefaults()

Installs the necessary properties on the JPasswordField.

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

