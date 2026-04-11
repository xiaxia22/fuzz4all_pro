# Interface MenuContainer

**Source:** `java.desktop\java\awt\MenuContainer.html`

### Class Description

```java
public interface
MenuContainer
```

The super class of all menu related containers.

**All Known Implementing Classes:** AbstractButton

,

AbstractColorChooserPanel

,

Applet

,

BasicArrowButton

,

BasicComboBoxRenderer

,

BasicComboBoxRenderer.UIResource

,

BasicComboPopup

,

BasicInternalFrameTitlePane

,

BasicInternalFrameTitlePane.SystemMenuBar

,

BasicSplitPaneDivider

,

BasicToolBarUI.DragWindow

,

Box

,

Box.Filler

,

Button

,

Canvas

,

CellRendererPane

,

Checkbox

,

Choice

,

Component

,

Container

,

DefaultListCellRenderer

,

DefaultListCellRenderer.UIResource

,

DefaultTableCellRenderer

,

DefaultTableCellRenderer.UIResource

,

DefaultTreeCellEditor.DefaultTextField

,

DefaultTreeCellEditor.EditorContainer

,

DefaultTreeCellRenderer

,

Dialog

,

FileDialog

,

Frame

,

JApplet

,

JButton

,

JCheckBox

,

JCheckBoxMenuItem

,

JColorChooser

,

JComboBox

,

JComponent

,

JDesktopPane

,

JDialog

,

JEditorPane

,

JFileChooser

,

JFormattedTextField

,

JFrame

,

JInternalFrame

,

JInternalFrame.JDesktopIcon

,

JLabel

,

JLayer

,

JLayeredPane

,

JList

,

JMenu

,

JMenuBar

,

JMenuItem

,

JOptionPane

,

JPanel

,

JPasswordField

,

JPopupMenu

,

JPopupMenu.Separator

,

JProgressBar

,

JRadioButton

,

JRadioButtonMenuItem

,

JRootPane

,

JScrollBar

,

JScrollPane

,

JScrollPane.ScrollBar

,

JSeparator

,

JSlider

,

JSpinner

,

JSpinner.DateEditor

,

JSpinner.DefaultEditor

,

JSpinner.ListEditor

,

JSpinner.NumberEditor

,

JSplitPane

,

JTabbedPane

,

JTable

,

JTableHeader

,

JTextArea

,

JTextComponent

,

JTextField

,

JTextPane

,

JToggleButton

,

JToolBar

,

JToolBar.Separator

,

JToolTip

,

JTree

,

JViewport

,

JWindow

,

Label

,

List

,

Menu

,

MenuBar

,

MetalComboBoxButton

,

MetalComboBoxUI.MetalComboPopup

,

MetalFileChooserUI.FileRenderer

,

MetalFileChooserUI.FilterComboBoxRenderer

,

MetalInternalFrameTitlePane

,

MetalScrollButton

,

Panel

,

PopupMenu

,

Scrollbar

,

ScrollPane

,

TextArea

,

TextComponent

,

TextField

,

Window

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Font
getFont()

Returns the font in use by this container.

**Returns:**
- the menu font

---

#### void remove​(
MenuComponent
comp)

Removes the specified menu component from the menu.

**Parameters:**
- comp

- the menu component to remove

---

#### @Deprecated

boolean postEvent​(
Event
evt)

Posts an event to the listeners.

**Parameters:**
- evt

- the event to dispatch

**Returns:**
- the results of posting the event

---

### Additional Sections

#### Interface MenuContainer

**All Known Implementing Classes:** AbstractButton

,

AbstractColorChooserPanel

,

Applet

,

BasicArrowButton

,

BasicComboBoxRenderer

,

BasicComboBoxRenderer.UIResource

,

BasicComboPopup

,

BasicInternalFrameTitlePane

,

BasicInternalFrameTitlePane.SystemMenuBar

,

BasicSplitPaneDivider

,

BasicToolBarUI.DragWindow

,

Box

,

Box.Filler

,

Button

,

Canvas

,

CellRendererPane

,

Checkbox

,

Choice

,

Component

,

Container

,

DefaultListCellRenderer

,

DefaultListCellRenderer.UIResource

,

DefaultTableCellRenderer

,

DefaultTableCellRenderer.UIResource

,

DefaultTreeCellEditor.DefaultTextField

,

DefaultTreeCellEditor.EditorContainer

,

DefaultTreeCellRenderer

,

Dialog

,

FileDialog

,

Frame

,

JApplet

,

JButton

,

JCheckBox

,

JCheckBoxMenuItem

,

JColorChooser

,

JComboBox

,

JComponent

,

JDesktopPane

,

JDialog

,

JEditorPane

,

JFileChooser

,

JFormattedTextField

,

JFrame

,

JInternalFrame

,

JInternalFrame.JDesktopIcon

,

JLabel

,

JLayer

,

JLayeredPane

,

JList

,

JMenu

,

JMenuBar

,

JMenuItem

,

JOptionPane

,

JPanel

,

JPasswordField

,

JPopupMenu

,

JPopupMenu.Separator

,

JProgressBar

,

JRadioButton

,

JRadioButtonMenuItem

,

JRootPane

,

JScrollBar

,

JScrollPane

,

JScrollPane.ScrollBar

,

JSeparator

,

JSlider

,

JSpinner

,

JSpinner.DateEditor

,

JSpinner.DefaultEditor

,

JSpinner.ListEditor

,

JSpinner.NumberEditor

,

JSplitPane

,

JTabbedPane

,

JTable

,

JTableHeader

,

JTextArea

,

JTextComponent

,

JTextField

,

JTextPane

,

JToggleButton

,

JToolBar

,

JToolBar.Separator

,

JToolTip

,

JTree

,

JViewport

,

JWindow

,

Label

,

List

,

Menu

,

MenuBar

,

MetalComboBoxButton

,

MetalComboBoxUI.MetalComboPopup

,

MetalFileChooserUI.FileRenderer

,

MetalFileChooserUI.FilterComboBoxRenderer

,

MetalInternalFrameTitlePane

,

MetalScrollButton

,

Panel

,

PopupMenu

,

Scrollbar

,

ScrollPane

,

TextArea

,

TextComponent

,

TextField

,

Window

```java
public interface
MenuContainer
```

The super class of all menu related containers.

public interface

MenuContainer

The super class of all menu related containers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

Font

getFont

()

Returns the font in use by this container.

boolean

postEvent

​(

Event

evt)

Deprecated.

As of JDK version 1.1
replaced by dispatchEvent(AWTEvent).

void

remove

​(

MenuComponent

comp)

Removes the specified menu component from the menu.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

Font

getFont

()

Returns the font in use by this container.

boolean

postEvent

​(

Event

evt)

Deprecated.

As of JDK version 1.1
replaced by dispatchEvent(AWTEvent).

void

remove

​(

MenuComponent

comp)

Removes the specified menu component from the menu.

---

#### Method Summary

Returns the font in use by this container.

Deprecated.

As of JDK version 1.1
replaced by dispatchEvent(AWTEvent).

Removes the specified menu component from the menu.

============ METHOD DETAIL ==========

- Method Detail

- getFont

```java
Font
getFont()
```

Returns the font in use by this container.

**Returns:** the menu font

- remove

```java
void remove​(
MenuComponent
comp)
```

Removes the specified menu component from the menu.

**Parameters:** comp

- the menu component to remove

- postEvent

```java
@Deprecated

boolean postEvent​(
Event
evt)
```

Deprecated.

As of JDK version 1.1
replaced by dispatchEvent(AWTEvent).

Posts an event to the listeners.

**Parameters:** evt

- the event to dispatch
**Returns:** the results of posting the event

Method Detail

- getFont

```java
Font
getFont()
```

Returns the font in use by this container.

**Returns:** the menu font

- remove

```java
void remove​(
MenuComponent
comp)
```

Removes the specified menu component from the menu.

**Parameters:** comp

- the menu component to remove

- postEvent

```java
@Deprecated

boolean postEvent​(
Event
evt)
```

Deprecated.

As of JDK version 1.1
replaced by dispatchEvent(AWTEvent).

Posts an event to the listeners.

**Parameters:** evt

- the event to dispatch
**Returns:** the results of posting the event

---

#### Method Detail

getFont

```java
Font
getFont()
```

Returns the font in use by this container.

**Returns:** the menu font

---

#### getFont

Font

getFont()

Returns the font in use by this container.

remove

```java
void remove​(
MenuComponent
comp)
```

Removes the specified menu component from the menu.

**Parameters:** comp

- the menu component to remove

---

#### remove

void remove​(

MenuComponent

comp)

Removes the specified menu component from the menu.

postEvent

```java
@Deprecated

boolean postEvent​(
Event
evt)
```

Deprecated.

As of JDK version 1.1
replaced by dispatchEvent(AWTEvent).

Posts an event to the listeners.

**Parameters:** evt

- the event to dispatch
**Returns:** the results of posting the event

---

#### postEvent

@Deprecated

boolean postEvent​(

Event

evt)

Posts an event to the listeners.

---

