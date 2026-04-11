# Class MetalFileChooserUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalFileChooserUI.html`

### Class Description

```java
public class
MetalFileChooserUI

extends
BasicFileChooserUI
```

Metal L&F implementation of a FileChooser.

---

### Field Details

*No entries found.*

### Constructor Details

#### public MetalFileChooserUI​(
JFileChooser
filechooser)

Constructs a new instance of

MetalFileChooserUI

.

**Parameters:**
- filechooser

- a

JFileChooser

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Constructs a new instance of

MetalFileChooserUI

.

**Parameters:**
- c

- a component

**Returns:**
- a new instance of

MetalFileChooserUI

---

#### protected
JPanel
getButtonPanel()

Returns the button panel.

**Returns:**
- the button panel

---

#### protected
JPanel
getBottomPanel()

Returns the bottom panel.

**Returns:**
- the bottom panel

---

#### protected
ActionMap
getActionMap()

Returns an instance of

ActionMap

.

**Returns:**
- an instance of

ActionMap

---

#### protected
ActionMap
createActionMap()

Constructs an instance of

ActionMap

.

**Returns:**
- an instance of

ActionMap

---

#### protected
JPanel
createList​(
JFileChooser
fc)

Constructs a details view.

**Parameters:**
- fc

- a

JFileChooser

**Returns:**
- the list

---

#### protected
JPanel
createDetailsView​(
JFileChooser
fc)

Constructs a details view.

**Parameters:**
- fc

- a

JFileChooser

**Returns:**
- the details view

---

#### public
ListSelectionListener
createListSelectionListener​(
JFileChooser
fc)

Creates a selection listener for the list of files and directories.

**Overrides:**
- createListSelectionListener

in class

BasicFileChooserUI

**Parameters:**
- fc

- a

JFileChooser

**Returns:**
- a

ListSelectionListener

---

#### public
Dimension
getPreferredSize​(
JComponent
c)

Returns the preferred size of the specified

JFileChooser

.
The preferred size is at least as large,
in both height and width,
as the preferred size recommended
by the file chooser's layout manager.

**Overrides:**
- getPreferredSize

in class

ComponentUI

**Parameters:**
- c

- a

JFileChooser

**Returns:**
- a

Dimension

specifying the preferred
width and height of the file chooser

**See Also:**
- JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### public
Dimension
getMinimumSize​(
JComponent
c)

Returns the minimum size of the

JFileChooser

.

**Overrides:**
- getMinimumSize

in class

ComponentUI

**Parameters:**
- c

- a

JFileChooser

**Returns:**
- a

Dimension

specifying the minimum
width and height of the file chooser

**See Also:**
- JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

---

#### public
Dimension
getMaximumSize​(
JComponent
c)

Returns the maximum size of the

JFileChooser

.

**Overrides:**
- getMaximumSize

in class

ComponentUI

**Parameters:**
- c

- a

JFileChooser

**Returns:**
- a

Dimension

specifying the maximum
width and height of the file chooser

**See Also:**
- JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### protected void removeControlButtons()

Removes control buttons from bottom panel.

---

#### protected void addControlButtons()

Adds control buttons to bottom panel.

---

#### protected void setDirectorySelected​(boolean directorySelected)

Property to remember whether a directory is currently selected in the UI.
This is normally called by the UI on a selection event.

**Overrides:**
- setDirectorySelected

in class

BasicFileChooserUI

**Parameters:**
- directorySelected

- if a directory is currently selected.

**Since:**
- 1.4

---

#### public
String
getDirectoryName()

Returns the directory name.

**Overrides:**
- getDirectoryName

in class

BasicFileChooserUI

**Returns:**
- the directory name

---

#### public void setDirectoryName​(
String
dirname)

Sets the directory name.

**Overrides:**
- setDirectoryName

in class

BasicFileChooserUI

**Parameters:**
- dirname

- the directory name

---

#### protected
MetalFileChooserUI.DirectoryComboBoxModel
createDirectoryComboBoxModel​(
JFileChooser
fc)

Constructs a new instance of

DataModel

for

DirectoryComboBox

.

**Parameters:**
- fc

- a

JFileChooser

**Returns:**
- a new instance of

DataModel

for

DirectoryComboBox

---

#### protected
MetalFileChooserUI.FilterComboBoxRenderer
createFilterComboBoxRenderer()

Constructs a

Renderer

for types

ComboBox

.

**Returns:**
- a

Renderer

for types

ComboBox

---

#### protected
MetalFileChooserUI.FilterComboBoxModel
createFilterComboBoxModel()

Constructs a

DataModel

for types

ComboBox

.

**Returns:**
- a

DataModel

for types

ComboBox

---

#### public void valueChanged​(
ListSelectionEvent
e)

Invokes when

ListSelectionEvent

occurs.

**Parameters:**
- e

- an instance of

ListSelectionEvent

---

### Additional Sections

#### Class MetalFileChooserUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.FileChooserUI
- - javax.swing.plaf.basic.BasicFileChooserUI
- - javax.swing.plaf.metal.MetalFileChooserUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.FileChooserUI
- - javax.swing.plaf.basic.BasicFileChooserUI
- - javax.swing.plaf.metal.MetalFileChooserUI

javax.swing.plaf.FileChooserUI

- javax.swing.plaf.basic.BasicFileChooserUI
- - javax.swing.plaf.metal.MetalFileChooserUI

javax.swing.plaf.basic.BasicFileChooserUI

- javax.swing.plaf.metal.MetalFileChooserUI

javax.swing.plaf.metal.MetalFileChooserUI

```java
public class
MetalFileChooserUI

extends
BasicFileChooserUI
```

Metal L&F implementation of a FileChooser.

public class

MetalFileChooserUI

extends

BasicFileChooserUI

Metal L&F implementation of a FileChooser.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

MetalFileChooserUI.DirectoryComboBoxAction

Acts when DirectoryComboBox has changed the selected item.

protected class

MetalFileChooserUI.DirectoryComboBoxModel

Data model for a type-face selection combo-box.

protected class

MetalFileChooserUI.FileRenderer

Deprecated.

As of JDK version 9.

protected class

MetalFileChooserUI.FilterComboBoxModel

Data model for a type-face selection combo-box.

class

MetalFileChooserUI.FilterComboBoxRenderer

Render different type sizes and styles.

protected class

MetalFileChooserUI.SingleClickListener

Deprecated.

As of JDK version 9.

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicFileChooserUI

BasicFileChooserUI.AcceptAllFileFilter

,

BasicFileChooserUI.ApproveSelectionAction

,

BasicFileChooserUI.BasicFileView

,

BasicFileChooserUI.CancelSelectionAction

,

BasicFileChooserUI.ChangeToParentDirectoryAction

,

BasicFileChooserUI.DoubleClickListener

,

BasicFileChooserUI.GoHomeAction

,

BasicFileChooserUI.NewFolderAction

,

BasicFileChooserUI.SelectionListener

,

BasicFileChooserUI.UpdateAction

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicFileChooserUI

cancelButtonMnemonic

,

cancelButtonText

,

cancelButtonToolTipText

,

computerIcon

,

detailsViewIcon

,

directoryIcon

,

directoryOpenButtonMnemonic

,

directoryOpenButtonText

,

directoryOpenButtonToolTipText

,

fileIcon

,

floppyDriveIcon

,

hardDriveIcon

,

helpButtonMnemonic

,

helpButtonText

,

helpButtonToolTipText

,

homeFolderIcon

,

listViewIcon

,

newFolderIcon

,

openButtonMnemonic

,

openButtonText

,

openButtonToolTipText

,

saveButtonMnemonic

,

saveButtonText

,

saveButtonToolTipText

,

updateButtonMnemonic

,

updateButtonText

,

updateButtonToolTipText

,

upFolderIcon

,

viewMenuIcon

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MetalFileChooserUI

​(

JFileChooser

filechooser)

Constructs a new instance of

MetalFileChooserUI

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addControlButtons

()

Adds control buttons to bottom panel.

protected

ActionMap

createActionMap

()

Constructs an instance of

ActionMap

.

protected

JPanel

createDetailsView

​(

JFileChooser

fc)

Constructs a details view.

protected

MetalFileChooserUI.DirectoryComboBoxModel

createDirectoryComboBoxModel

​(

JFileChooser

fc)

Constructs a new instance of

DataModel

for

DirectoryComboBox

.

protected

MetalFileChooserUI.FilterComboBoxModel

createFilterComboBoxModel

()

Constructs a

DataModel

for types

ComboBox

.

protected

MetalFileChooserUI.FilterComboBoxRenderer

createFilterComboBoxRenderer

()

Constructs a

Renderer

for types

ComboBox

.

protected

JPanel

createList

​(

JFileChooser

fc)

Constructs a details view.

ListSelectionListener

createListSelectionListener

​(

JFileChooser

fc)

Creates a selection listener for the list of files and directories.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new instance of

MetalFileChooserUI

.

protected

ActionMap

getActionMap

()

Returns an instance of

ActionMap

.

protected

JPanel

getBottomPanel

()

Returns the bottom panel.

protected

JPanel

getButtonPanel

()

Returns the button panel.

String

getDirectoryName

()

Returns the directory name.

Dimension

getMaximumSize

​(

JComponent

c)

Returns the maximum size of the

JFileChooser

.

Dimension

getMinimumSize

​(

JComponent

c)

Returns the minimum size of the

JFileChooser

.

Dimension

getPreferredSize

​(

JComponent

c)

Returns the preferred size of the specified

JFileChooser

.

protected void

removeControlButtons

()

Removes control buttons from bottom panel.

void

setDirectoryName

​(

String

dirname)

Sets the directory name.

protected void

setDirectorySelected

​(boolean directorySelected)

Property to remember whether a directory is currently selected in the UI.

void

valueChanged

​(

ListSelectionEvent

e)

Invokes when

ListSelectionEvent

occurs.

- Methods declared in class javax.swing.plaf.basic.

BasicFileChooserUI

clearIconCache

,

createDoubleClickListener

,

createModel

,

createPropertyChangeListener

,

getAcceptAllFileFilter

,

getAccessoryPanel

,

getApproveButton

,

getApproveButtonMnemonic

,

getApproveButtonToolTipText

,

getApproveSelectionAction

,

getCancelSelectionAction

,

getChangeToParentDirectoryAction

,

getDialogTitle

,

getDirectory

,

getFileChooser

,

getFileName

,

getGoHomeAction

,

getModel

,

getNewFolderAction

,

getUpdateAction

,

installComponents

,

installDefaults

,

installIcons

,

installListeners

,

installStrings

,

installUI

,

isDirectorySelected

,

setDirectory

,

setFileName

,

uninstallComponents

,

uninstallDefaults

,

uninstallIcons

,

uninstallListeners

,

uninstallStrings

,

uninstallUI

- Methods declared in class javax.swing.plaf.

FileChooserUI

ensureFileIsVisible

,

getApproveButtonText

,

getDefaultButton

,

getFileView

,

rescanCurrentDirectory

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

paint

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

protected class

MetalFileChooserUI.DirectoryComboBoxAction

Acts when DirectoryComboBox has changed the selected item.

protected class

MetalFileChooserUI.DirectoryComboBoxModel

Data model for a type-face selection combo-box.

protected class

MetalFileChooserUI.FileRenderer

Deprecated.

As of JDK version 9.

protected class

MetalFileChooserUI.FilterComboBoxModel

Data model for a type-face selection combo-box.

class

MetalFileChooserUI.FilterComboBoxRenderer

Render different type sizes and styles.

protected class

MetalFileChooserUI.SingleClickListener

Deprecated.

As of JDK version 9.

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicFileChooserUI

BasicFileChooserUI.AcceptAllFileFilter

,

BasicFileChooserUI.ApproveSelectionAction

,

BasicFileChooserUI.BasicFileView

,

BasicFileChooserUI.CancelSelectionAction

,

BasicFileChooserUI.ChangeToParentDirectoryAction

,

BasicFileChooserUI.DoubleClickListener

,

BasicFileChooserUI.GoHomeAction

,

BasicFileChooserUI.NewFolderAction

,

BasicFileChooserUI.SelectionListener

,

BasicFileChooserUI.UpdateAction

---

#### Nested Class Summary

Acts when DirectoryComboBox has changed the selected item.

Data model for a type-face selection combo-box.

Deprecated.

As of JDK version 9.

Render different type sizes and styles.

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicFileChooserUI

BasicFileChooserUI.AcceptAllFileFilter

,

BasicFileChooserUI.ApproveSelectionAction

,

BasicFileChooserUI.BasicFileView

,

BasicFileChooserUI.CancelSelectionAction

,

BasicFileChooserUI.ChangeToParentDirectoryAction

,

BasicFileChooserUI.DoubleClickListener

,

BasicFileChooserUI.GoHomeAction

,

BasicFileChooserUI.NewFolderAction

,

BasicFileChooserUI.SelectionListener

,

BasicFileChooserUI.UpdateAction

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicFileChooserUI

Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicFileChooserUI

cancelButtonMnemonic

,

cancelButtonText

,

cancelButtonToolTipText

,

computerIcon

,

detailsViewIcon

,

directoryIcon

,

directoryOpenButtonMnemonic

,

directoryOpenButtonText

,

directoryOpenButtonToolTipText

,

fileIcon

,

floppyDriveIcon

,

hardDriveIcon

,

helpButtonMnemonic

,

helpButtonText

,

helpButtonToolTipText

,

homeFolderIcon

,

listViewIcon

,

newFolderIcon

,

openButtonMnemonic

,

openButtonText

,

openButtonToolTipText

,

saveButtonMnemonic

,

saveButtonText

,

saveButtonToolTipText

,

updateButtonMnemonic

,

updateButtonText

,

updateButtonToolTipText

,

upFolderIcon

,

viewMenuIcon

---

#### Field Summary

Fields declared in class javax.swing.plaf.basic.

BasicFileChooserUI

cancelButtonMnemonic

,

cancelButtonText

,

cancelButtonToolTipText

,

computerIcon

,

detailsViewIcon

,

directoryIcon

,

directoryOpenButtonMnemonic

,

directoryOpenButtonText

,

directoryOpenButtonToolTipText

,

fileIcon

,

floppyDriveIcon

,

hardDriveIcon

,

helpButtonMnemonic

,

helpButtonText

,

helpButtonToolTipText

,

homeFolderIcon

,

listViewIcon

,

newFolderIcon

,

openButtonMnemonic

,

openButtonText

,

openButtonToolTipText

,

saveButtonMnemonic

,

saveButtonText

,

saveButtonToolTipText

,

updateButtonMnemonic

,

updateButtonText

,

updateButtonToolTipText

,

upFolderIcon

,

viewMenuIcon

---

#### Fields declared in class javax.swing.plaf.basic. BasicFileChooserUI

Constructor Summary

Constructors

Constructor

Description

MetalFileChooserUI

​(

JFileChooser

filechooser)

Constructs a new instance of

MetalFileChooserUI

.

---

#### Constructor Summary

Constructs a new instance of

MetalFileChooserUI

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addControlButtons

()

Adds control buttons to bottom panel.

protected

ActionMap

createActionMap

()

Constructs an instance of

ActionMap

.

protected

JPanel

createDetailsView

​(

JFileChooser

fc)

Constructs a details view.

protected

MetalFileChooserUI.DirectoryComboBoxModel

createDirectoryComboBoxModel

​(

JFileChooser

fc)

Constructs a new instance of

DataModel

for

DirectoryComboBox

.

protected

MetalFileChooserUI.FilterComboBoxModel

createFilterComboBoxModel

()

Constructs a

DataModel

for types

ComboBox

.

protected

MetalFileChooserUI.FilterComboBoxRenderer

createFilterComboBoxRenderer

()

Constructs a

Renderer

for types

ComboBox

.

protected

JPanel

createList

​(

JFileChooser

fc)

Constructs a details view.

ListSelectionListener

createListSelectionListener

​(

JFileChooser

fc)

Creates a selection listener for the list of files and directories.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new instance of

MetalFileChooserUI

.

protected

ActionMap

getActionMap

()

Returns an instance of

ActionMap

.

protected

JPanel

getBottomPanel

()

Returns the bottom panel.

protected

JPanel

getButtonPanel

()

Returns the button panel.

String

getDirectoryName

()

Returns the directory name.

Dimension

getMaximumSize

​(

JComponent

c)

Returns the maximum size of the

JFileChooser

.

Dimension

getMinimumSize

​(

JComponent

c)

Returns the minimum size of the

JFileChooser

.

Dimension

getPreferredSize

​(

JComponent

c)

Returns the preferred size of the specified

JFileChooser

.

protected void

removeControlButtons

()

Removes control buttons from bottom panel.

void

setDirectoryName

​(

String

dirname)

Sets the directory name.

protected void

setDirectorySelected

​(boolean directorySelected)

Property to remember whether a directory is currently selected in the UI.

void

valueChanged

​(

ListSelectionEvent

e)

Invokes when

ListSelectionEvent

occurs.

- Methods declared in class javax.swing.plaf.basic.

BasicFileChooserUI

clearIconCache

,

createDoubleClickListener

,

createModel

,

createPropertyChangeListener

,

getAcceptAllFileFilter

,

getAccessoryPanel

,

getApproveButton

,

getApproveButtonMnemonic

,

getApproveButtonToolTipText

,

getApproveSelectionAction

,

getCancelSelectionAction

,

getChangeToParentDirectoryAction

,

getDialogTitle

,

getDirectory

,

getFileChooser

,

getFileName

,

getGoHomeAction

,

getModel

,

getNewFolderAction

,

getUpdateAction

,

installComponents

,

installDefaults

,

installIcons

,

installListeners

,

installStrings

,

installUI

,

isDirectorySelected

,

setDirectory

,

setFileName

,

uninstallComponents

,

uninstallDefaults

,

uninstallIcons

,

uninstallListeners

,

uninstallStrings

,

uninstallUI

- Methods declared in class javax.swing.plaf.

FileChooserUI

ensureFileIsVisible

,

getApproveButtonText

,

getDefaultButton

,

getFileView

,

rescanCurrentDirectory

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

paint

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

Adds control buttons to bottom panel.

Constructs an instance of

ActionMap

.

Constructs a details view.

Constructs a new instance of

DataModel

for

DirectoryComboBox

.

Constructs a

DataModel

for types

ComboBox

.

Constructs a

Renderer

for types

ComboBox

.

Creates a selection listener for the list of files and directories.

Constructs a new instance of

MetalFileChooserUI

.

Returns an instance of

ActionMap

.

Returns the bottom panel.

Returns the button panel.

Returns the directory name.

Returns the maximum size of the

JFileChooser

.

Returns the minimum size of the

JFileChooser

.

Returns the preferred size of the specified

JFileChooser

.

Removes control buttons from bottom panel.

Sets the directory name.

Property to remember whether a directory is currently selected in the UI.

Invokes when

ListSelectionEvent

occurs.

Methods declared in class javax.swing.plaf.basic.

BasicFileChooserUI

clearIconCache

,

createDoubleClickListener

,

createModel

,

createPropertyChangeListener

,

getAcceptAllFileFilter

,

getAccessoryPanel

,

getApproveButton

,

getApproveButtonMnemonic

,

getApproveButtonToolTipText

,

getApproveSelectionAction

,

getCancelSelectionAction

,

getChangeToParentDirectoryAction

,

getDialogTitle

,

getDirectory

,

getFileChooser

,

getFileName

,

getGoHomeAction

,

getModel

,

getNewFolderAction

,

getUpdateAction

,

installComponents

,

installDefaults

,

installIcons

,

installListeners

,

installStrings

,

installUI

,

isDirectorySelected

,

setDirectory

,

setFileName

,

uninstallComponents

,

uninstallDefaults

,

uninstallIcons

,

uninstallListeners

,

uninstallStrings

,

uninstallUI

---

#### Methods declared in class javax.swing.plaf.basic. BasicFileChooserUI

Methods declared in class javax.swing.plaf.

FileChooserUI

ensureFileIsVisible

,

getApproveButtonText

,

getDefaultButton

,

getFileView

,

rescanCurrentDirectory

---

#### Methods declared in class javax.swing.plaf. FileChooserUI

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

paint

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

- MetalFileChooserUI

```java
public MetalFileChooserUI​(
JFileChooser
filechooser)
```

Constructs a new instance of

MetalFileChooserUI

.

**Parameters:** filechooser

- a

JFileChooser

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

Constructs a new instance of

MetalFileChooserUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

MetalFileChooserUI

- getButtonPanel

```java
protected
JPanel
getButtonPanel()
```

Returns the button panel.

**Returns:** the button panel

- getBottomPanel

```java
protected
JPanel
getBottomPanel()
```

Returns the bottom panel.

**Returns:** the bottom panel

- getActionMap

```java
protected
ActionMap
getActionMap()
```

Returns an instance of

ActionMap

.

**Returns:** an instance of

ActionMap

- createActionMap

```java
protected
ActionMap
createActionMap()
```

Constructs an instance of

ActionMap

.

**Returns:** an instance of

ActionMap

- createList

```java
protected
JPanel
createList​(
JFileChooser
fc)
```

Constructs a details view.

**Parameters:** fc

- a

JFileChooser
**Returns:** the list

- createDetailsView

```java
protected
JPanel
createDetailsView​(
JFileChooser
fc)
```

Constructs a details view.

**Parameters:** fc

- a

JFileChooser
**Returns:** the details view

- createListSelectionListener

```java
public
ListSelectionListener
createListSelectionListener​(
JFileChooser
fc)
```

Creates a selection listener for the list of files and directories.

**Overrides:** createListSelectionListener

in class

BasicFileChooserUI
**Parameters:** fc

- a

JFileChooser
**Returns:** a

ListSelectionListener

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Returns the preferred size of the specified

JFileChooser

.
The preferred size is at least as large,
in both height and width,
as the preferred size recommended
by the file chooser's layout manager.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- a

JFileChooser
**Returns:** a

Dimension

specifying the preferred
width and height of the file chooser
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

Returns the minimum size of the

JFileChooser

.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- a

JFileChooser
**Returns:** a

Dimension

specifying the minimum
width and height of the file chooser
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Returns the maximum size of the

JFileChooser

.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- a

JFileChooser
**Returns:** a

Dimension

specifying the maximum
width and height of the file chooser
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- removeControlButtons

```java
protected void removeControlButtons()
```

Removes control buttons from bottom panel.

- addControlButtons

```java
protected void addControlButtons()
```

Adds control buttons to bottom panel.

- setDirectorySelected

```java
protected void setDirectorySelected​(boolean directorySelected)
```

Property to remember whether a directory is currently selected in the UI.
This is normally called by the UI on a selection event.

**Overrides:** setDirectorySelected

in class

BasicFileChooserUI
**Parameters:** directorySelected

- if a directory is currently selected.
**Since:** 1.4

- getDirectoryName

```java
public
String
getDirectoryName()
```

Returns the directory name.

**Overrides:** getDirectoryName

in class

BasicFileChooserUI
**Returns:** the directory name

- setDirectoryName

```java
public void setDirectoryName​(
String
dirname)
```

Sets the directory name.

**Overrides:** setDirectoryName

in class

BasicFileChooserUI
**Parameters:** dirname

- the directory name

- createDirectoryComboBoxModel

```java
protected
MetalFileChooserUI.DirectoryComboBoxModel
createDirectoryComboBoxModel​(
JFileChooser
fc)
```

Constructs a new instance of

DataModel

for

DirectoryComboBox

.

**Parameters:** fc

- a

JFileChooser
**Returns:** a new instance of

DataModel

for

DirectoryComboBox

- createFilterComboBoxRenderer

```java
protected
MetalFileChooserUI.FilterComboBoxRenderer
createFilterComboBoxRenderer()
```

Constructs a

Renderer

for types

ComboBox

.

**Returns:** a

Renderer

for types

ComboBox

- createFilterComboBoxModel

```java
protected
MetalFileChooserUI.FilterComboBoxModel
createFilterComboBoxModel()
```

Constructs a

DataModel

for types

ComboBox

.

**Returns:** a

DataModel

for types

ComboBox

- valueChanged

```java
public void valueChanged​(
ListSelectionEvent
e)
```

Invokes when

ListSelectionEvent

occurs.

**Parameters:** e

- an instance of

ListSelectionEvent

Constructor Detail

- MetalFileChooserUI

```java
public MetalFileChooserUI​(
JFileChooser
filechooser)
```

Constructs a new instance of

MetalFileChooserUI

.

**Parameters:** filechooser

- a

JFileChooser

---

#### Constructor Detail

MetalFileChooserUI

```java
public MetalFileChooserUI​(
JFileChooser
filechooser)
```

Constructs a new instance of

MetalFileChooserUI

.

**Parameters:** filechooser

- a

JFileChooser

---

#### MetalFileChooserUI

public MetalFileChooserUI​(

JFileChooser

filechooser)

Constructs a new instance of

MetalFileChooserUI

.

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs a new instance of

MetalFileChooserUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

MetalFileChooserUI

- getButtonPanel

```java
protected
JPanel
getButtonPanel()
```

Returns the button panel.

**Returns:** the button panel

- getBottomPanel

```java
protected
JPanel
getBottomPanel()
```

Returns the bottom panel.

**Returns:** the bottom panel

- getActionMap

```java
protected
ActionMap
getActionMap()
```

Returns an instance of

ActionMap

.

**Returns:** an instance of

ActionMap

- createActionMap

```java
protected
ActionMap
createActionMap()
```

Constructs an instance of

ActionMap

.

**Returns:** an instance of

ActionMap

- createList

```java
protected
JPanel
createList​(
JFileChooser
fc)
```

Constructs a details view.

**Parameters:** fc

- a

JFileChooser
**Returns:** the list

- createDetailsView

```java
protected
JPanel
createDetailsView​(
JFileChooser
fc)
```

Constructs a details view.

**Parameters:** fc

- a

JFileChooser
**Returns:** the details view

- createListSelectionListener

```java
public
ListSelectionListener
createListSelectionListener​(
JFileChooser
fc)
```

Creates a selection listener for the list of files and directories.

**Overrides:** createListSelectionListener

in class

BasicFileChooserUI
**Parameters:** fc

- a

JFileChooser
**Returns:** a

ListSelectionListener

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Returns the preferred size of the specified

JFileChooser

.
The preferred size is at least as large,
in both height and width,
as the preferred size recommended
by the file chooser's layout manager.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- a

JFileChooser
**Returns:** a

Dimension

specifying the preferred
width and height of the file chooser
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

Returns the minimum size of the

JFileChooser

.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- a

JFileChooser
**Returns:** a

Dimension

specifying the minimum
width and height of the file chooser
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Returns the maximum size of the

JFileChooser

.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- a

JFileChooser
**Returns:** a

Dimension

specifying the maximum
width and height of the file chooser
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- removeControlButtons

```java
protected void removeControlButtons()
```

Removes control buttons from bottom panel.

- addControlButtons

```java
protected void addControlButtons()
```

Adds control buttons to bottom panel.

- setDirectorySelected

```java
protected void setDirectorySelected​(boolean directorySelected)
```

Property to remember whether a directory is currently selected in the UI.
This is normally called by the UI on a selection event.

**Overrides:** setDirectorySelected

in class

BasicFileChooserUI
**Parameters:** directorySelected

- if a directory is currently selected.
**Since:** 1.4

- getDirectoryName

```java
public
String
getDirectoryName()
```

Returns the directory name.

**Overrides:** getDirectoryName

in class

BasicFileChooserUI
**Returns:** the directory name

- setDirectoryName

```java
public void setDirectoryName​(
String
dirname)
```

Sets the directory name.

**Overrides:** setDirectoryName

in class

BasicFileChooserUI
**Parameters:** dirname

- the directory name

- createDirectoryComboBoxModel

```java
protected
MetalFileChooserUI.DirectoryComboBoxModel
createDirectoryComboBoxModel​(
JFileChooser
fc)
```

Constructs a new instance of

DataModel

for

DirectoryComboBox

.

**Parameters:** fc

- a

JFileChooser
**Returns:** a new instance of

DataModel

for

DirectoryComboBox

- createFilterComboBoxRenderer

```java
protected
MetalFileChooserUI.FilterComboBoxRenderer
createFilterComboBoxRenderer()
```

Constructs a

Renderer

for types

ComboBox

.

**Returns:** a

Renderer

for types

ComboBox

- createFilterComboBoxModel

```java
protected
MetalFileChooserUI.FilterComboBoxModel
createFilterComboBoxModel()
```

Constructs a

DataModel

for types

ComboBox

.

**Returns:** a

DataModel

for types

ComboBox

- valueChanged

```java
public void valueChanged​(
ListSelectionEvent
e)
```

Invokes when

ListSelectionEvent

occurs.

**Parameters:** e

- an instance of

ListSelectionEvent

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

Constructs a new instance of

MetalFileChooserUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

MetalFileChooserUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Constructs a new instance of

MetalFileChooserUI

.

getButtonPanel

```java
protected
JPanel
getButtonPanel()
```

Returns the button panel.

**Returns:** the button panel

---

#### getButtonPanel

protected

JPanel

getButtonPanel()

Returns the button panel.

getBottomPanel

```java
protected
JPanel
getBottomPanel()
```

Returns the bottom panel.

**Returns:** the bottom panel

---

#### getBottomPanel

protected

JPanel

getBottomPanel()

Returns the bottom panel.

getActionMap

```java
protected
ActionMap
getActionMap()
```

Returns an instance of

ActionMap

.

**Returns:** an instance of

ActionMap

---

#### getActionMap

protected

ActionMap

getActionMap()

Returns an instance of

ActionMap

.

createActionMap

```java
protected
ActionMap
createActionMap()
```

Constructs an instance of

ActionMap

.

**Returns:** an instance of

ActionMap

---

#### createActionMap

protected

ActionMap

createActionMap()

Constructs an instance of

ActionMap

.

createList

```java
protected
JPanel
createList​(
JFileChooser
fc)
```

Constructs a details view.

**Parameters:** fc

- a

JFileChooser
**Returns:** the list

---

#### createList

protected

JPanel

createList​(

JFileChooser

fc)

Constructs a details view.

createDetailsView

```java
protected
JPanel
createDetailsView​(
JFileChooser
fc)
```

Constructs a details view.

**Parameters:** fc

- a

JFileChooser
**Returns:** the details view

---

#### createDetailsView

protected

JPanel

createDetailsView​(

JFileChooser

fc)

Constructs a details view.

createListSelectionListener

```java
public
ListSelectionListener
createListSelectionListener​(
JFileChooser
fc)
```

Creates a selection listener for the list of files and directories.

**Overrides:** createListSelectionListener

in class

BasicFileChooserUI
**Parameters:** fc

- a

JFileChooser
**Returns:** a

ListSelectionListener

---

#### createListSelectionListener

public

ListSelectionListener

createListSelectionListener​(

JFileChooser

fc)

Creates a selection listener for the list of files and directories.

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Returns the preferred size of the specified

JFileChooser

.
The preferred size is at least as large,
in both height and width,
as the preferred size recommended
by the file chooser's layout manager.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- a

JFileChooser
**Returns:** a

Dimension

specifying the preferred
width and height of the file chooser
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

Returns the preferred size of the specified

JFileChooser

.
The preferred size is at least as large,
in both height and width,
as the preferred size recommended
by the file chooser's layout manager.

getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Returns the minimum size of the

JFileChooser

.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- a

JFileChooser
**Returns:** a

Dimension

specifying the minimum
width and height of the file chooser
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

Returns the minimum size of the

JFileChooser

.

getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Returns the maximum size of the

JFileChooser

.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- a

JFileChooser
**Returns:** a

Dimension

specifying the maximum
width and height of the file chooser
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### getMaximumSize

public

Dimension

getMaximumSize​(

JComponent

c)

Returns the maximum size of the

JFileChooser

.

removeControlButtons

```java
protected void removeControlButtons()
```

Removes control buttons from bottom panel.

---

#### removeControlButtons

protected void removeControlButtons()

Removes control buttons from bottom panel.

addControlButtons

```java
protected void addControlButtons()
```

Adds control buttons to bottom panel.

---

#### addControlButtons

protected void addControlButtons()

Adds control buttons to bottom panel.

setDirectorySelected

```java
protected void setDirectorySelected​(boolean directorySelected)
```

Property to remember whether a directory is currently selected in the UI.
This is normally called by the UI on a selection event.

**Overrides:** setDirectorySelected

in class

BasicFileChooserUI
**Parameters:** directorySelected

- if a directory is currently selected.
**Since:** 1.4

---

#### setDirectorySelected

protected void setDirectorySelected​(boolean directorySelected)

Property to remember whether a directory is currently selected in the UI.
This is normally called by the UI on a selection event.

getDirectoryName

```java
public
String
getDirectoryName()
```

Returns the directory name.

**Overrides:** getDirectoryName

in class

BasicFileChooserUI
**Returns:** the directory name

---

#### getDirectoryName

public

String

getDirectoryName()

Returns the directory name.

setDirectoryName

```java
public void setDirectoryName​(
String
dirname)
```

Sets the directory name.

**Overrides:** setDirectoryName

in class

BasicFileChooserUI
**Parameters:** dirname

- the directory name

---

#### setDirectoryName

public void setDirectoryName​(

String

dirname)

Sets the directory name.

createDirectoryComboBoxModel

```java
protected
MetalFileChooserUI.DirectoryComboBoxModel
createDirectoryComboBoxModel​(
JFileChooser
fc)
```

Constructs a new instance of

DataModel

for

DirectoryComboBox

.

**Parameters:** fc

- a

JFileChooser
**Returns:** a new instance of

DataModel

for

DirectoryComboBox

---

#### createDirectoryComboBoxModel

protected

MetalFileChooserUI.DirectoryComboBoxModel

createDirectoryComboBoxModel​(

JFileChooser

fc)

Constructs a new instance of

DataModel

for

DirectoryComboBox

.

createFilterComboBoxRenderer

```java
protected
MetalFileChooserUI.FilterComboBoxRenderer
createFilterComboBoxRenderer()
```

Constructs a

Renderer

for types

ComboBox

.

**Returns:** a

Renderer

for types

ComboBox

---

#### createFilterComboBoxRenderer

protected

MetalFileChooserUI.FilterComboBoxRenderer

createFilterComboBoxRenderer()

Constructs a

Renderer

for types

ComboBox

.

createFilterComboBoxModel

```java
protected
MetalFileChooserUI.FilterComboBoxModel
createFilterComboBoxModel()
```

Constructs a

DataModel

for types

ComboBox

.

**Returns:** a

DataModel

for types

ComboBox

---

#### createFilterComboBoxModel

protected

MetalFileChooserUI.FilterComboBoxModel

createFilterComboBoxModel()

Constructs a

DataModel

for types

ComboBox

.

valueChanged

```java
public void valueChanged​(
ListSelectionEvent
e)
```

Invokes when

ListSelectionEvent

occurs.

**Parameters:** e

- an instance of

ListSelectionEvent

---

#### valueChanged

public void valueChanged​(

ListSelectionEvent

e)

Invokes when

ListSelectionEvent

occurs.

---

