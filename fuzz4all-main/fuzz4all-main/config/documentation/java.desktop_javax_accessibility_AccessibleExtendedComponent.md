# Interface AccessibleExtendedComponent

**Source:** `java.desktop\javax\accessibility\AccessibleExtendedComponent.html`

### Class Description

```java
public interface
AccessibleExtendedComponent

extends
AccessibleComponent
```

The

AccessibleExtendedComponent

interface should be supported by any
object that is rendered on the screen. This interface provides the standard
mechanism for an assistive technology to determine the extended graphical
representation of an object. Applications can determine if an object supports
the

AccessibleExtendedComponent

interface by first obtaining its

AccessibleContext

and then calling the

AccessibleContext.getAccessibleComponent()

method. If the return value
is not

null

and the type of the return value is

AccessibleExtendedComponent

, the object supports this interface.

**All Superinterfaces:** AccessibleComponent

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getToolTipText()

Returns the tool tip text.

**Returns:**
- the tool tip text, if supported, of the object; otherwise,

null

---

#### String
getTitledBorderText()

Returns the titled border text.

**Returns:**
- the titled border text, if supported, of the object; otherwise,

null

---

#### AccessibleKeyBinding
getAccessibleKeyBinding()

Returns key bindings associated with this object.

**Returns:**
- the key bindings, if supported, of the object; otherwise,

null

**See Also:**
- AccessibleKeyBinding

---

### Additional Sections

#### Interface AccessibleExtendedComponent

**All Superinterfaces:** AccessibleComponent

**All Known Implementing Classes:** AbstractButton.AccessibleAbstractButton

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

JEditorPane.AccessibleJEditorPane

,

JEditorPane.AccessibleJEditorPaneHTML

,

JEditorPane.JEditorPaneAccessibleHypertextSupport

,

JFileChooser.AccessibleJFileChooser

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

JTableHeader.AccessibleJTableHeader

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

JViewport.AccessibleJViewport

```java
public interface
AccessibleExtendedComponent

extends
AccessibleComponent
```

The

AccessibleExtendedComponent

interface should be supported by any
object that is rendered on the screen. This interface provides the standard
mechanism for an assistive technology to determine the extended graphical
representation of an object. Applications can determine if an object supports
the

AccessibleExtendedComponent

interface by first obtaining its

AccessibleContext

and then calling the

AccessibleContext.getAccessibleComponent()

method. If the return value
is not

null

and the type of the return value is

AccessibleExtendedComponent

, the object supports this interface.

**Since:** 1.4
**See Also:** Accessible

,

Accessible.getAccessibleContext()

,

AccessibleContext

,

AccessibleContext.getAccessibleComponent()

public interface

AccessibleExtendedComponent

extends

AccessibleComponent

The

AccessibleExtendedComponent

interface should be supported by any
object that is rendered on the screen. This interface provides the standard
mechanism for an assistive technology to determine the extended graphical
representation of an object. Applications can determine if an object supports
the

AccessibleExtendedComponent

interface by first obtaining its

AccessibleContext

and then calling the

AccessibleContext.getAccessibleComponent()

method. If the return value
is not

null

and the type of the return value is

AccessibleExtendedComponent

, the object supports this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AccessibleKeyBinding

getAccessibleKeyBinding

()

Returns key bindings associated with this object.

String

getTitledBorderText

()

Returns the titled border text.

String

getToolTipText

()

Returns the tool tip text.

- Methods declared in interface javax.accessibility.

AccessibleComponent

addFocusListener

,

contains

,

getAccessibleAt

,

getBackground

,

getBounds

,

getCursor

,

getFont

,

getFontMetrics

,

getForeground

,

getLocation

,

getLocationOnScreen

,

getSize

,

isEnabled

,

isFocusTraversable

,

isShowing

,

isVisible

,

removeFocusListener

,

requestFocus

,

setBackground

,

setBounds

,

setCursor

,

setEnabled

,

setFont

,

setForeground

,

setLocation

,

setSize

,

setVisible

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AccessibleKeyBinding

getAccessibleKeyBinding

()

Returns key bindings associated with this object.

String

getTitledBorderText

()

Returns the titled border text.

String

getToolTipText

()

Returns the tool tip text.

- Methods declared in interface javax.accessibility.

AccessibleComponent

addFocusListener

,

contains

,

getAccessibleAt

,

getBackground

,

getBounds

,

getCursor

,

getFont

,

getFontMetrics

,

getForeground

,

getLocation

,

getLocationOnScreen

,

getSize

,

isEnabled

,

isFocusTraversable

,

isShowing

,

isVisible

,

removeFocusListener

,

requestFocus

,

setBackground

,

setBounds

,

setCursor

,

setEnabled

,

setFont

,

setForeground

,

setLocation

,

setSize

,

setVisible

---

#### Method Summary

Returns key bindings associated with this object.

Returns the titled border text.

Returns the tool tip text.

Methods declared in interface javax.accessibility.

AccessibleComponent

addFocusListener

,

contains

,

getAccessibleAt

,

getBackground

,

getBounds

,

getCursor

,

getFont

,

getFontMetrics

,

getForeground

,

getLocation

,

getLocationOnScreen

,

getSize

,

isEnabled

,

isFocusTraversable

,

isShowing

,

isVisible

,

removeFocusListener

,

requestFocus

,

setBackground

,

setBounds

,

setCursor

,

setEnabled

,

setFont

,

setForeground

,

setLocation

,

setSize

,

setVisible

---

#### Methods declared in interface javax.accessibility. AccessibleComponent

============ METHOD DETAIL ==========

- Method Detail

- getToolTipText

```java
String
getToolTipText()
```

Returns the tool tip text.

**Returns:** the tool tip text, if supported, of the object; otherwise,

null

- getTitledBorderText

```java
String
getTitledBorderText()
```

Returns the titled border text.

**Returns:** the titled border text, if supported, of the object; otherwise,

null

- getAccessibleKeyBinding

```java
AccessibleKeyBinding
getAccessibleKeyBinding()
```

Returns key bindings associated with this object.

**Returns:** the key bindings, if supported, of the object; otherwise,

null
**See Also:** AccessibleKeyBinding

Method Detail

- getToolTipText

```java
String
getToolTipText()
```

Returns the tool tip text.

**Returns:** the tool tip text, if supported, of the object; otherwise,

null

- getTitledBorderText

```java
String
getTitledBorderText()
```

Returns the titled border text.

**Returns:** the titled border text, if supported, of the object; otherwise,

null

- getAccessibleKeyBinding

```java
AccessibleKeyBinding
getAccessibleKeyBinding()
```

Returns key bindings associated with this object.

**Returns:** the key bindings, if supported, of the object; otherwise,

null
**See Also:** AccessibleKeyBinding

---

#### Method Detail

getToolTipText

```java
String
getToolTipText()
```

Returns the tool tip text.

**Returns:** the tool tip text, if supported, of the object; otherwise,

null

---

#### getToolTipText

String

getToolTipText()

Returns the tool tip text.

getTitledBorderText

```java
String
getTitledBorderText()
```

Returns the titled border text.

**Returns:** the titled border text, if supported, of the object; otherwise,

null

---

#### getTitledBorderText

String

getTitledBorderText()

Returns the titled border text.

getAccessibleKeyBinding

```java
AccessibleKeyBinding
getAccessibleKeyBinding()
```

Returns key bindings associated with this object.

**Returns:** the key bindings, if supported, of the object; otherwise,

null
**See Also:** AccessibleKeyBinding

---

#### getAccessibleKeyBinding

AccessibleKeyBinding

getAccessibleKeyBinding()

Returns key bindings associated with this object.

---

