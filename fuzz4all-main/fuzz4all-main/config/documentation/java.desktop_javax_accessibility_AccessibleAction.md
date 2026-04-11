# Interface AccessibleAction

**Source:** `java.desktop\javax\accessibility\AccessibleAction.html`

### Class Description

```java
public interface
AccessibleAction
```

The

AccessibleAction

interface should be supported by any object that
can perform one or more actions. This interface provides the standard
mechanism for an assistive technology to determine what those actions are as
well as tell the object to perform them. Any object that can be manipulated
should support this interface. Applications can determine if an object
supports the

AccessibleAction

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleAction()

method. If the return value is
not

null

, the object supports this interface.

**All Known Implementing Classes:** AbstractButton.AccessibleAbstractButton

,

AccessibleHyperlink

,

Button.AccessibleAWTButton

,

Checkbox.AccessibleAWTCheckbox

,

CheckboxMenuItem.AccessibleAWTCheckboxMenuItem

,

Choice.AccessibleAWTChoice

,

JButton.AccessibleJButton

,

JCheckBox.AccessibleJCheckBox

,

JCheckBoxMenuItem.AccessibleJCheckBoxMenuItem

,

JComboBox.AccessibleJComboBox

,

JEditorPane.AccessibleJEditorPane

,

JEditorPane.AccessibleJEditorPaneHTML

,

JEditorPane.JEditorPaneAccessibleHypertextSupport

,

JEditorPane.JEditorPaneAccessibleHypertextSupport.HTMLLink

,

JList.AccessibleJList.AccessibleJListChild

,

JMenu.AccessibleJMenu

,

JMenuItem.AccessibleJMenuItem

,

JPasswordField.AccessibleJPasswordField

,

JRadioButton.AccessibleJRadioButton

,

JRadioButtonMenuItem.AccessibleJRadioButtonMenuItem

,

JSpinner.AccessibleJSpinner

,

JTextArea.AccessibleJTextArea

,

JTextComponent.AccessibleJTextComponent

,

JTextField.AccessibleJTextField

,

JToggleButton.AccessibleJToggleButton

,

JTree.AccessibleJTree.AccessibleJTreeNode

,

Menu.AccessibleAWTMenu

,

MenuItem.AccessibleAWTMenuItem

,

PopupMenu.AccessibleAWTPopupMenu

---

### Field Details

#### static final
String
TOGGLE_EXPAND

An action which causes a tree node to collapse if expanded and expand if
collapsed.

**Since:**
- 1.5

---

#### static final
String
INCREMENT

An action which increments a value.

**Since:**
- 1.5

---

#### static final
String
DECREMENT

An action which decrements a value.

**Since:**
- 1.5

---

#### static final
String
CLICK

An action which causes a component to execute its default action.

**Since:**
- 1.6

---

#### static final
String
TOGGLE_POPUP

An action which causes a popup to become visible if it is hidden and
hidden if it is visible.

**Since:**
- 1.6

---

### Constructor Details

*No entries found.*

### Method Details

#### int getAccessibleActionCount()

Returns the number of accessible actions available in this object If
there are more than one, the first one is considered the "default" action
of the object.

**Returns:**
- the zero-based number of actions in this object

---

#### String
getAccessibleActionDescription​(int i)

Returns a description of the specified action of the object.

**Parameters:**
- i

- zero-based index of the actions

**Returns:**
- a

String

description of the action

**See Also:**
- getAccessibleActionCount()

---

#### boolean doAccessibleAction​(int i)

Performs the specified action on the object.

**Parameters:**
- i

- zero-based index of actions

**Returns:**
- true

if the action was performed; otherwise

false

**See Also:**
- getAccessibleActionCount()

---

### Additional Sections

#### Interface AccessibleAction

**All Known Implementing Classes:** AbstractButton.AccessibleAbstractButton

,

AccessibleHyperlink

,

Button.AccessibleAWTButton

,

Checkbox.AccessibleAWTCheckbox

,

CheckboxMenuItem.AccessibleAWTCheckboxMenuItem

,

Choice.AccessibleAWTChoice

,

JButton.AccessibleJButton

,

JCheckBox.AccessibleJCheckBox

,

JCheckBoxMenuItem.AccessibleJCheckBoxMenuItem

,

JComboBox.AccessibleJComboBox

,

JEditorPane.AccessibleJEditorPane

,

JEditorPane.AccessibleJEditorPaneHTML

,

JEditorPane.JEditorPaneAccessibleHypertextSupport

,

JEditorPane.JEditorPaneAccessibleHypertextSupport.HTMLLink

,

JList.AccessibleJList.AccessibleJListChild

,

JMenu.AccessibleJMenu

,

JMenuItem.AccessibleJMenuItem

,

JPasswordField.AccessibleJPasswordField

,

JRadioButton.AccessibleJRadioButton

,

JRadioButtonMenuItem.AccessibleJRadioButtonMenuItem

,

JSpinner.AccessibleJSpinner

,

JTextArea.AccessibleJTextArea

,

JTextComponent.AccessibleJTextComponent

,

JTextField.AccessibleJTextField

,

JToggleButton.AccessibleJToggleButton

,

JTree.AccessibleJTree.AccessibleJTreeNode

,

Menu.AccessibleAWTMenu

,

MenuItem.AccessibleAWTMenuItem

,

PopupMenu.AccessibleAWTPopupMenu

```java
public interface
AccessibleAction
```

The

AccessibleAction

interface should be supported by any object that
can perform one or more actions. This interface provides the standard
mechanism for an assistive technology to determine what those actions are as
well as tell the object to perform them. Any object that can be manipulated
should support this interface. Applications can determine if an object
supports the

AccessibleAction

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleAction()

method. If the return value is
not

null

, the object supports this interface.

**See Also:** Accessible

,

Accessible.getAccessibleContext()

,

AccessibleContext

,

AccessibleContext.getAccessibleAction()

public interface

AccessibleAction

The

AccessibleAction

interface should be supported by any object that
can perform one or more actions. This interface provides the standard
mechanism for an assistive technology to determine what those actions are as
well as tell the object to perform them. Any object that can be manipulated
should support this interface. Applications can determine if an object
supports the

AccessibleAction

interface by first obtaining its

AccessibleContext

(see

Accessible

) and then calling the

AccessibleContext.getAccessibleAction()

method. If the return value is
not

null

, the object supports this interface.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

CLICK

An action which causes a component to execute its default action.

static

String

DECREMENT

An action which decrements a value.

static

String

INCREMENT

An action which increments a value.

static

String

TOGGLE_EXPAND

An action which causes a tree node to collapse if expanded and expand if
collapsed.

static

String

TOGGLE_POPUP

An action which causes a popup to become visible if it is hidden and
hidden if it is visible.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

doAccessibleAction

​(int i)

Performs the specified action on the object.

int

getAccessibleActionCount

()

Returns the number of accessible actions available in this object If
there are more than one, the first one is considered the "default" action
of the object.

String

getAccessibleActionDescription

​(int i)

Returns a description of the specified action of the object.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

CLICK

An action which causes a component to execute its default action.

static

String

DECREMENT

An action which decrements a value.

static

String

INCREMENT

An action which increments a value.

static

String

TOGGLE_EXPAND

An action which causes a tree node to collapse if expanded and expand if
collapsed.

static

String

TOGGLE_POPUP

An action which causes a popup to become visible if it is hidden and
hidden if it is visible.

---

#### Field Summary

An action which causes a component to execute its default action.

An action which decrements a value.

An action which increments a value.

An action which causes a tree node to collapse if expanded and expand if
collapsed.

An action which causes a popup to become visible if it is hidden and
hidden if it is visible.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

doAccessibleAction

​(int i)

Performs the specified action on the object.

int

getAccessibleActionCount

()

Returns the number of accessible actions available in this object If
there are more than one, the first one is considered the "default" action
of the object.

String

getAccessibleActionDescription

​(int i)

Returns a description of the specified action of the object.

---

#### Method Summary

Performs the specified action on the object.

Returns the number of accessible actions available in this object If
there are more than one, the first one is considered the "default" action
of the object.

Returns a description of the specified action of the object.

============ FIELD DETAIL ===========

- Field Detail

- TOGGLE_EXPAND

```java
static final
String
TOGGLE_EXPAND
```

An action which causes a tree node to collapse if expanded and expand if
collapsed.

**Since:** 1.5

- INCREMENT

```java
static final
String
INCREMENT
```

An action which increments a value.

**Since:** 1.5

- DECREMENT

```java
static final
String
DECREMENT
```

An action which decrements a value.

**Since:** 1.5

- CLICK

```java
static final
String
CLICK
```

An action which causes a component to execute its default action.

**Since:** 1.6

- TOGGLE_POPUP

```java
static final
String
TOGGLE_POPUP
```

An action which causes a popup to become visible if it is hidden and
hidden if it is visible.

**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- getAccessibleActionCount

```java
int getAccessibleActionCount()
```

Returns the number of accessible actions available in this object If
there are more than one, the first one is considered the "default" action
of the object.

**Returns:** the zero-based number of actions in this object

- getAccessibleActionDescription

```java
String
getAccessibleActionDescription​(int i)
```

Returns a description of the specified action of the object.

**Parameters:** i

- zero-based index of the actions
**Returns:** a

String

description of the action
**See Also:** getAccessibleActionCount()

- doAccessibleAction

```java
boolean doAccessibleAction​(int i)
```

Performs the specified action on the object.

**Parameters:** i

- zero-based index of actions
**Returns:** true

if the action was performed; otherwise

false
**See Also:** getAccessibleActionCount()

Field Detail

- TOGGLE_EXPAND

```java
static final
String
TOGGLE_EXPAND
```

An action which causes a tree node to collapse if expanded and expand if
collapsed.

**Since:** 1.5

- INCREMENT

```java
static final
String
INCREMENT
```

An action which increments a value.

**Since:** 1.5

- DECREMENT

```java
static final
String
DECREMENT
```

An action which decrements a value.

**Since:** 1.5

- CLICK

```java
static final
String
CLICK
```

An action which causes a component to execute its default action.

**Since:** 1.6

- TOGGLE_POPUP

```java
static final
String
TOGGLE_POPUP
```

An action which causes a popup to become visible if it is hidden and
hidden if it is visible.

**Since:** 1.6

---

#### Field Detail

TOGGLE_EXPAND

```java
static final
String
TOGGLE_EXPAND
```

An action which causes a tree node to collapse if expanded and expand if
collapsed.

**Since:** 1.5

---

#### TOGGLE_EXPAND

static final

String

TOGGLE_EXPAND

An action which causes a tree node to collapse if expanded and expand if
collapsed.

INCREMENT

```java
static final
String
INCREMENT
```

An action which increments a value.

**Since:** 1.5

---

#### INCREMENT

static final

String

INCREMENT

An action which increments a value.

DECREMENT

```java
static final
String
DECREMENT
```

An action which decrements a value.

**Since:** 1.5

---

#### DECREMENT

static final

String

DECREMENT

An action which decrements a value.

CLICK

```java
static final
String
CLICK
```

An action which causes a component to execute its default action.

**Since:** 1.6

---

#### CLICK

static final

String

CLICK

An action which causes a component to execute its default action.

TOGGLE_POPUP

```java
static final
String
TOGGLE_POPUP
```

An action which causes a popup to become visible if it is hidden and
hidden if it is visible.

**Since:** 1.6

---

#### TOGGLE_POPUP

static final

String

TOGGLE_POPUP

An action which causes a popup to become visible if it is hidden and
hidden if it is visible.

Method Detail

- getAccessibleActionCount

```java
int getAccessibleActionCount()
```

Returns the number of accessible actions available in this object If
there are more than one, the first one is considered the "default" action
of the object.

**Returns:** the zero-based number of actions in this object

- getAccessibleActionDescription

```java
String
getAccessibleActionDescription​(int i)
```

Returns a description of the specified action of the object.

**Parameters:** i

- zero-based index of the actions
**Returns:** a

String

description of the action
**See Also:** getAccessibleActionCount()

- doAccessibleAction

```java
boolean doAccessibleAction​(int i)
```

Performs the specified action on the object.

**Parameters:** i

- zero-based index of actions
**Returns:** true

if the action was performed; otherwise

false
**See Also:** getAccessibleActionCount()

---

#### Method Detail

getAccessibleActionCount

```java
int getAccessibleActionCount()
```

Returns the number of accessible actions available in this object If
there are more than one, the first one is considered the "default" action
of the object.

**Returns:** the zero-based number of actions in this object

---

#### getAccessibleActionCount

int getAccessibleActionCount()

Returns the number of accessible actions available in this object If
there are more than one, the first one is considered the "default" action
of the object.

getAccessibleActionDescription

```java
String
getAccessibleActionDescription​(int i)
```

Returns a description of the specified action of the object.

**Parameters:** i

- zero-based index of the actions
**Returns:** a

String

description of the action
**See Also:** getAccessibleActionCount()

---

#### getAccessibleActionDescription

String

getAccessibleActionDescription​(int i)

Returns a description of the specified action of the object.

doAccessibleAction

```java
boolean doAccessibleAction​(int i)
```

Performs the specified action on the object.

**Parameters:** i

- zero-based index of actions
**Returns:** true

if the action was performed; otherwise

false
**See Also:** getAccessibleActionCount()

---

#### doAccessibleAction

boolean doAccessibleAction​(int i)

Performs the specified action on the object.

---

