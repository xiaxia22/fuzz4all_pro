# Class BasicFileChooserUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicFileChooserUI.html`

### Class Description

```java
public class
BasicFileChooserUI

extends
FileChooserUI
```

Basic L&F implementation of a FileChooser.

**Direct Known Subclasses:** MetalFileChooserUI

---

### Field Details

#### protected
Icon
directoryIcon

Directory icon

---

#### protected
Icon
fileIcon

File icon

---

#### protected
Icon
computerIcon

Computer icon

---

#### protected
Icon
hardDriveIcon

Hard drive icon

---

#### protected
Icon
floppyDriveIcon

Floppy drive icon

---

#### protected
Icon
newFolderIcon

New folder icon

---

#### protected
Icon
upFolderIcon

Up folder icon

---

#### protected
Icon
homeFolderIcon

Home folder icon

---

#### protected
Icon
listViewIcon

List view icon

---

#### protected
Icon
detailsViewIcon

Details view icon

---

#### protected
Icon
viewMenuIcon

View menu icon

---

#### protected int saveButtonMnemonic

Save button mnemonic

---

#### protected int openButtonMnemonic

Open button mnemonic

---

#### protected int cancelButtonMnemonic

Cancel button mnemonic

---

#### protected int updateButtonMnemonic

Update button mnemonic

---

#### protected int helpButtonMnemonic

Help button mnemonic

---

#### protected int directoryOpenButtonMnemonic

The mnemonic keycode used for the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

**Since:**
- 1.4

---

#### protected
String
saveButtonText

Save button text

---

#### protected
String
openButtonText

Open button text

---

#### protected
String
cancelButtonText

Cancel button text

---

#### protected
String
updateButtonText

Update button text

---

#### protected
String
helpButtonText

Help button text

---

#### protected
String
directoryOpenButtonText

The label text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

**Since:**
- 1.4

---

#### protected
String
saveButtonToolTipText

Save button tool tip text

---

#### protected
String
openButtonToolTipText

Open button tool tip text

---

#### protected
String
cancelButtonToolTipText

Cancel button tool tip text

---

#### protected
String
updateButtonToolTipText

Update button tool tip text

---

#### protected
String
helpButtonToolTipText

Help button tool tip text

---

#### protected
String
directoryOpenButtonToolTipText

The tooltip text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

**Since:**
- 1.4

---

### Constructor Details

#### public BasicFileChooserUI​(
JFileChooser
b)

Constructs a

BasicFileChooserUI

.

**Parameters:**
- b

- file chooser

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Creates a

BasicFileChooserUI

implementation
for the specified component. By default
the

BasicLookAndFeel

class uses

createUI

methods of all basic UIs classes
to instantiate UIs.

**Parameters:**
- c

- the

JFileChooser

which needs a UI

**Returns:**
- the

BasicFileChooserUI

object

**See Also:**
- UIDefaults.getUI(JComponent)

**Since:**
- 1.7

---

#### public void installUI​(
JComponent
c)

Installs the UI.

**Overrides:**
- installUI

in class

ComponentUI

**Parameters:**
- c

- the component

**See Also:**
- ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

---

#### public void uninstallUI​(
JComponent
c)

Uninstalls the UI.

**Overrides:**
- uninstallUI

in class

ComponentUI

**Parameters:**
- c

- the component

**See Also:**
- ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

---

#### public void installComponents​(
JFileChooser
fc)

Installs the components.

**Parameters:**
- fc

- the file chooser

---

#### public void uninstallComponents​(
JFileChooser
fc)

Uninstalls the components.

**Parameters:**
- fc

- the file chooser

---

#### protected void installListeners​(
JFileChooser
fc)

Installs the listeners.

**Parameters:**
- fc

- the file chooser

---

#### protected void uninstallListeners​(
JFileChooser
fc)

Uninstalls the listeners.

**Parameters:**
- fc

- the file chooser

---

#### protected void installDefaults​(
JFileChooser
fc)

Installs the defaults.

**Parameters:**
- fc

- the file chooser

---

#### protected void installIcons​(
JFileChooser
fc)

Installs the icons.

**Parameters:**
- fc

- the file chooser

---

#### protected void installStrings​(
JFileChooser
fc)

Installs the strings.

**Parameters:**
- fc

- the file chooser

---

#### protected void uninstallDefaults​(
JFileChooser
fc)

Uninstalls the defaults.

**Parameters:**
- fc

- the file chooser

---

#### protected void uninstallIcons​(
JFileChooser
fc)

Uninstalls the icons.

**Parameters:**
- fc

- the file chooser

---

#### protected void uninstallStrings​(
JFileChooser
fc)

Uninstalls the strings.

**Parameters:**
- fc

- the file chooser

---

#### protected void createModel()

Creates the model.

---

#### public
BasicDirectoryModel
getModel()

Returns the model.

**Returns:**
- the model

---

#### public
PropertyChangeListener
createPropertyChangeListener​(
JFileChooser
fc)

Creates the property change listener.

**Parameters:**
- fc

- the file chooser

**Returns:**
- the property change listener

---

#### public
String
getFileName()

Returns the file name.

**Returns:**
- the file name

---

#### public
String
getDirectoryName()

Returns the directory name.

**Returns:**
- the directory name

---

#### public void setFileName​(
String
filename)

Sets the file name.

**Parameters:**
- filename

- the file name

---

#### public void setDirectoryName​(
String
dirname)

Sets the directory name.

**Parameters:**
- dirname

- the file name

---

#### public
JFileChooser
getFileChooser()

Returns the file chooser.

**Returns:**
- the file chooser

---

#### public
JPanel
getAccessoryPanel()

Returns the accessory panel.

**Returns:**
- the accessory panel

---

#### protected
JButton
getApproveButton​(
JFileChooser
fc)

Returns the approve button.

**Parameters:**
- fc

- the file chooser

**Returns:**
- the approve button

---

#### public
String
getApproveButtonToolTipText​(
JFileChooser
fc)

Returns the approve button tool tip.

**Parameters:**
- fc

- the file chooser

**Returns:**
- the approve button tool tip

---

#### public void clearIconCache()

Clears the icon cache.

---

#### protected
MouseListener
createDoubleClickListener​(
JFileChooser
fc,

JList
<?> list)

Creates a double click listener.

**Parameters:**
- fc

- the file chooser
- list

- the list

**Returns:**
- a double click listener

---

#### public
ListSelectionListener
createListSelectionListener​(
JFileChooser
fc)

Creates a list selection listener.

**Parameters:**
- fc

- the file chooser

**Returns:**
- a list selection listener

---

#### protected boolean isDirectorySelected()

Property to remember whether a directory is currently selected in the UI.

**Returns:**
- true

iff a directory is currently selected.

**Since:**
- 1.4

---

#### protected void setDirectorySelected​(boolean b)

Property to remember whether a directory is currently selected in the UI.
This is normally called by the UI on a selection event.

**Parameters:**
- b

- iff a directory is currently selected.

**Since:**
- 1.4

---

#### protected
File
getDirectory()

Property to remember the directory that is currently selected in the UI.

**Returns:**
- the value of the

directory

property

**See Also:**
- setDirectory(java.io.File)

**Since:**
- 1.4

---

#### protected void setDirectory​(
File
f)

Property to remember the directory that is currently selected in the UI.
This is normally called by the UI on a selection event.

**Parameters:**
- f

- the

File

object representing the directory that is
currently selected

**Since:**
- 1.4

---

#### public
FileFilter
getAcceptAllFileFilter​(
JFileChooser
fc)

Returns the default accept all file filter

**Specified by:**
- getAcceptAllFileFilter

in class

FileChooserUI

**Parameters:**
- fc

- the file chooser

**Returns:**
- an accept-all file filter

---

#### public
String
getDialogTitle​(
JFileChooser
fc)

Returns the title of this dialog

**Specified by:**
- getDialogTitle

in class

FileChooserUI

**Parameters:**
- fc

- the file chooser

**Returns:**
- the title of this dialog

---

#### public int getApproveButtonMnemonic​(
JFileChooser
fc)

Returns the approve button mnemonic.

**Parameters:**
- fc

- the file chooser

**Returns:**
- the approve button mnemonic

---

#### public
Action
getNewFolderAction()

Returns a new folder action.

**Returns:**
- a new folder action

---

#### public
Action
getGoHomeAction()

Returns a go home action.

**Returns:**
- a go home action

---

#### public
Action
getChangeToParentDirectoryAction()

Returns a change to parent directory action.

**Returns:**
- a change to parent directory action

---

#### public
Action
getApproveSelectionAction()

Returns an approve selection action.

**Returns:**
- an approve selection action

---

#### public
Action
getCancelSelectionAction()

Returns a cancel selection action.

**Returns:**
- a cancel selection action

---

#### public
Action
getUpdateAction()

Returns an update action.

**Returns:**
- an update action

---

### Additional Sections

#### Class BasicFileChooserUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.FileChooserUI
- - javax.swing.plaf.basic.BasicFileChooserUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.FileChooserUI
- - javax.swing.plaf.basic.BasicFileChooserUI

javax.swing.plaf.FileChooserUI

- javax.swing.plaf.basic.BasicFileChooserUI

javax.swing.plaf.basic.BasicFileChooserUI

**Direct Known Subclasses:** MetalFileChooserUI

```java
public class
BasicFileChooserUI

extends
FileChooserUI
```

Basic L&F implementation of a FileChooser.

public class

BasicFileChooserUI

extends

FileChooserUI

Basic L&F implementation of a FileChooser.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

BasicFileChooserUI.AcceptAllFileFilter

Accept all file filter.

protected class

BasicFileChooserUI.ApproveSelectionAction

Responds to an Open or Save request

protected class

BasicFileChooserUI.BasicFileView

A basic file view.

protected class

BasicFileChooserUI.CancelSelectionAction

Responds to a cancel request.

protected class

BasicFileChooserUI.ChangeToParentDirectoryAction

Change to parent directory action.

protected class

BasicFileChooserUI.DoubleClickListener

A double click listener.

protected class

BasicFileChooserUI.GoHomeAction

Acts on the "home" key event or equivalent event.

protected class

BasicFileChooserUI.NewFolderAction

Creates a new folder.

protected class

BasicFileChooserUI.SelectionListener

A selection listener.

protected class

BasicFileChooserUI.UpdateAction

Rescans the files in the current directory

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

cancelButtonMnemonic

Cancel button mnemonic

protected

String

cancelButtonText

Cancel button text

protected

String

cancelButtonToolTipText

Cancel button tool tip text

protected

Icon

computerIcon

Computer icon

protected

Icon

detailsViewIcon

Details view icon

protected

Icon

directoryIcon

Directory icon

protected int

directoryOpenButtonMnemonic

The mnemonic keycode used for the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

protected

String

directoryOpenButtonText

The label text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

protected

String

directoryOpenButtonToolTipText

The tooltip text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

protected

Icon

fileIcon

File icon

protected

Icon

floppyDriveIcon

Floppy drive icon

protected

Icon

hardDriveIcon

Hard drive icon

protected int

helpButtonMnemonic

Help button mnemonic

protected

String

helpButtonText

Help button text

protected

String

helpButtonToolTipText

Help button tool tip text

protected

Icon

homeFolderIcon

Home folder icon

protected

Icon

listViewIcon

List view icon

protected

Icon

newFolderIcon

New folder icon

protected int

openButtonMnemonic

Open button mnemonic

protected

String

openButtonText

Open button text

protected

String

openButtonToolTipText

Open button tool tip text

protected int

saveButtonMnemonic

Save button mnemonic

protected

String

saveButtonText

Save button text

protected

String

saveButtonToolTipText

Save button tool tip text

protected int

updateButtonMnemonic

Update button mnemonic

protected

String

updateButtonText

Update button text

protected

String

updateButtonToolTipText

Update button tool tip text

protected

Icon

upFolderIcon

Up folder icon

protected

Icon

viewMenuIcon

View menu icon

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicFileChooserUI

​(

JFileChooser

b)

Constructs a

BasicFileChooserUI

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

void

clearIconCache

()

Clears the icon cache.

protected

MouseListener

createDoubleClickListener

​(

JFileChooser

fc,

JList

<?> list)

Creates a double click listener.

ListSelectionListener

createListSelectionListener

​(

JFileChooser

fc)

Creates a list selection listener.

protected void

createModel

()

Creates the model.

PropertyChangeListener

createPropertyChangeListener

​(

JFileChooser

fc)

Creates the property change listener.

static

ComponentUI

createUI

​(

JComponent

c)

Creates a

BasicFileChooserUI

implementation
for the specified component.

FileFilter

getAcceptAllFileFilter

​(

JFileChooser

fc)

Returns the default accept all file filter

JPanel

getAccessoryPanel

()

Returns the accessory panel.

protected

JButton

getApproveButton

​(

JFileChooser

fc)

Returns the approve button.

int

getApproveButtonMnemonic

​(

JFileChooser

fc)

Returns the approve button mnemonic.

String

getApproveButtonToolTipText

​(

JFileChooser

fc)

Returns the approve button tool tip.

Action

getApproveSelectionAction

()

Returns an approve selection action.

Action

getCancelSelectionAction

()

Returns a cancel selection action.

Action

getChangeToParentDirectoryAction

()

Returns a change to parent directory action.

String

getDialogTitle

​(

JFileChooser

fc)

Returns the title of this dialog

protected

File

getDirectory

()

Property to remember the directory that is currently selected in the UI.

String

getDirectoryName

()

Returns the directory name.

JFileChooser

getFileChooser

()

Returns the file chooser.

String

getFileName

()

Returns the file name.

Action

getGoHomeAction

()

Returns a go home action.

BasicDirectoryModel

getModel

()

Returns the model.

Action

getNewFolderAction

()

Returns a new folder action.

Action

getUpdateAction

()

Returns an update action.

void

installComponents

​(

JFileChooser

fc)

Installs the components.

protected void

installDefaults

​(

JFileChooser

fc)

Installs the defaults.

protected void

installIcons

​(

JFileChooser

fc)

Installs the icons.

protected void

installListeners

​(

JFileChooser

fc)

Installs the listeners.

protected void

installStrings

​(

JFileChooser

fc)

Installs the strings.

void

installUI

​(

JComponent

c)

Installs the UI.

protected boolean

isDirectorySelected

()

Property to remember whether a directory is currently selected in the UI.

protected void

setDirectory

​(

File

f)

Property to remember the directory that is currently selected in the UI.

void

setDirectoryName

​(

String

dirname)

Sets the directory name.

protected void

setDirectorySelected

​(boolean b)

Property to remember whether a directory is currently selected in the UI.

void

setFileName

​(

String

filename)

Sets the file name.

void

uninstallComponents

​(

JFileChooser

fc)

Uninstalls the components.

protected void

uninstallDefaults

​(

JFileChooser

fc)

Uninstalls the defaults.

protected void

uninstallIcons

​(

JFileChooser

fc)

Uninstalls the icons.

protected void

uninstallListeners

​(

JFileChooser

fc)

Uninstalls the listeners.

protected void

uninstallStrings

​(

JFileChooser

fc)

Uninstalls the strings.

void

uninstallUI

​(

JComponent

c)

Uninstalls the UI.

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

getMaximumSize

,

getMinimumSize

,

getPreferredSize

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

BasicFileChooserUI.AcceptAllFileFilter

Accept all file filter.

protected class

BasicFileChooserUI.ApproveSelectionAction

Responds to an Open or Save request

protected class

BasicFileChooserUI.BasicFileView

A basic file view.

protected class

BasicFileChooserUI.CancelSelectionAction

Responds to a cancel request.

protected class

BasicFileChooserUI.ChangeToParentDirectoryAction

Change to parent directory action.

protected class

BasicFileChooserUI.DoubleClickListener

A double click listener.

protected class

BasicFileChooserUI.GoHomeAction

Acts on the "home" key event or equivalent event.

protected class

BasicFileChooserUI.NewFolderAction

Creates a new folder.

protected class

BasicFileChooserUI.SelectionListener

A selection listener.

protected class

BasicFileChooserUI.UpdateAction

Rescans the files in the current directory

---

#### Nested Class Summary

Accept all file filter.

Responds to an Open or Save request

A basic file view.

Responds to a cancel request.

Change to parent directory action.

A double click listener.

Acts on the "home" key event or equivalent event.

Creates a new folder.

A selection listener.

Rescans the files in the current directory

Field Summary

Fields

Modifier and Type

Field

Description

protected int

cancelButtonMnemonic

Cancel button mnemonic

protected

String

cancelButtonText

Cancel button text

protected

String

cancelButtonToolTipText

Cancel button tool tip text

protected

Icon

computerIcon

Computer icon

protected

Icon

detailsViewIcon

Details view icon

protected

Icon

directoryIcon

Directory icon

protected int

directoryOpenButtonMnemonic

The mnemonic keycode used for the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

protected

String

directoryOpenButtonText

The label text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

protected

String

directoryOpenButtonToolTipText

The tooltip text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

protected

Icon

fileIcon

File icon

protected

Icon

floppyDriveIcon

Floppy drive icon

protected

Icon

hardDriveIcon

Hard drive icon

protected int

helpButtonMnemonic

Help button mnemonic

protected

String

helpButtonText

Help button text

protected

String

helpButtonToolTipText

Help button tool tip text

protected

Icon

homeFolderIcon

Home folder icon

protected

Icon

listViewIcon

List view icon

protected

Icon

newFolderIcon

New folder icon

protected int

openButtonMnemonic

Open button mnemonic

protected

String

openButtonText

Open button text

protected

String

openButtonToolTipText

Open button tool tip text

protected int

saveButtonMnemonic

Save button mnemonic

protected

String

saveButtonText

Save button text

protected

String

saveButtonToolTipText

Save button tool tip text

protected int

updateButtonMnemonic

Update button mnemonic

protected

String

updateButtonText

Update button text

protected

String

updateButtonToolTipText

Update button tool tip text

protected

Icon

upFolderIcon

Up folder icon

protected

Icon

viewMenuIcon

View menu icon

---

#### Field Summary

Cancel button mnemonic

Cancel button text

Cancel button tool tip text

Computer icon

Details view icon

Directory icon

The mnemonic keycode used for the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

The label text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

The tooltip text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

File icon

Floppy drive icon

Hard drive icon

Help button mnemonic

Help button text

Help button tool tip text

Home folder icon

List view icon

New folder icon

Open button mnemonic

Open button text

Open button tool tip text

Save button mnemonic

Save button text

Save button tool tip text

Update button mnemonic

Update button text

Update button tool tip text

Up folder icon

View menu icon

Constructor Summary

Constructors

Constructor

Description

BasicFileChooserUI

​(

JFileChooser

b)

Constructs a

BasicFileChooserUI

.

---

#### Constructor Summary

Constructs a

BasicFileChooserUI

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clearIconCache

()

Clears the icon cache.

protected

MouseListener

createDoubleClickListener

​(

JFileChooser

fc,

JList

<?> list)

Creates a double click listener.

ListSelectionListener

createListSelectionListener

​(

JFileChooser

fc)

Creates a list selection listener.

protected void

createModel

()

Creates the model.

PropertyChangeListener

createPropertyChangeListener

​(

JFileChooser

fc)

Creates the property change listener.

static

ComponentUI

createUI

​(

JComponent

c)

Creates a

BasicFileChooserUI

implementation
for the specified component.

FileFilter

getAcceptAllFileFilter

​(

JFileChooser

fc)

Returns the default accept all file filter

JPanel

getAccessoryPanel

()

Returns the accessory panel.

protected

JButton

getApproveButton

​(

JFileChooser

fc)

Returns the approve button.

int

getApproveButtonMnemonic

​(

JFileChooser

fc)

Returns the approve button mnemonic.

String

getApproveButtonToolTipText

​(

JFileChooser

fc)

Returns the approve button tool tip.

Action

getApproveSelectionAction

()

Returns an approve selection action.

Action

getCancelSelectionAction

()

Returns a cancel selection action.

Action

getChangeToParentDirectoryAction

()

Returns a change to parent directory action.

String

getDialogTitle

​(

JFileChooser

fc)

Returns the title of this dialog

protected

File

getDirectory

()

Property to remember the directory that is currently selected in the UI.

String

getDirectoryName

()

Returns the directory name.

JFileChooser

getFileChooser

()

Returns the file chooser.

String

getFileName

()

Returns the file name.

Action

getGoHomeAction

()

Returns a go home action.

BasicDirectoryModel

getModel

()

Returns the model.

Action

getNewFolderAction

()

Returns a new folder action.

Action

getUpdateAction

()

Returns an update action.

void

installComponents

​(

JFileChooser

fc)

Installs the components.

protected void

installDefaults

​(

JFileChooser

fc)

Installs the defaults.

protected void

installIcons

​(

JFileChooser

fc)

Installs the icons.

protected void

installListeners

​(

JFileChooser

fc)

Installs the listeners.

protected void

installStrings

​(

JFileChooser

fc)

Installs the strings.

void

installUI

​(

JComponent

c)

Installs the UI.

protected boolean

isDirectorySelected

()

Property to remember whether a directory is currently selected in the UI.

protected void

setDirectory

​(

File

f)

Property to remember the directory that is currently selected in the UI.

void

setDirectoryName

​(

String

dirname)

Sets the directory name.

protected void

setDirectorySelected

​(boolean b)

Property to remember whether a directory is currently selected in the UI.

void

setFileName

​(

String

filename)

Sets the file name.

void

uninstallComponents

​(

JFileChooser

fc)

Uninstalls the components.

protected void

uninstallDefaults

​(

JFileChooser

fc)

Uninstalls the defaults.

protected void

uninstallIcons

​(

JFileChooser

fc)

Uninstalls the icons.

protected void

uninstallListeners

​(

JFileChooser

fc)

Uninstalls the listeners.

protected void

uninstallStrings

​(

JFileChooser

fc)

Uninstalls the strings.

void

uninstallUI

​(

JComponent

c)

Uninstalls the UI.

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

getMaximumSize

,

getMinimumSize

,

getPreferredSize

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

Clears the icon cache.

Creates a double click listener.

Creates a list selection listener.

Creates the model.

Creates the property change listener.

Creates a

BasicFileChooserUI

implementation
for the specified component.

Returns the default accept all file filter

Returns the accessory panel.

Returns the approve button.

Returns the approve button mnemonic.

Returns the approve button tool tip.

Returns an approve selection action.

Returns a cancel selection action.

Returns a change to parent directory action.

Returns the title of this dialog

Property to remember the directory that is currently selected in the UI.

Returns the directory name.

Returns the file chooser.

Returns the file name.

Returns a go home action.

Returns the model.

Returns a new folder action.

Returns an update action.

Installs the components.

Installs the defaults.

Installs the icons.

Installs the listeners.

Installs the strings.

Installs the UI.

Property to remember whether a directory is currently selected in the UI.

Sets the directory name.

Sets the file name.

Uninstalls the components.

Uninstalls the defaults.

Uninstalls the icons.

Uninstalls the listeners.

Uninstalls the strings.

Uninstalls the UI.

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

getMaximumSize

,

getMinimumSize

,

getPreferredSize

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

============ FIELD DETAIL ===========

- Field Detail

- directoryIcon

```java
protected
Icon
directoryIcon
```

Directory icon

- fileIcon

```java
protected
Icon
fileIcon
```

File icon

- computerIcon

```java
protected
Icon
computerIcon
```

Computer icon

- hardDriveIcon

```java
protected
Icon
hardDriveIcon
```

Hard drive icon

- floppyDriveIcon

```java
protected
Icon
floppyDriveIcon
```

Floppy drive icon

- newFolderIcon

```java
protected
Icon
newFolderIcon
```

New folder icon

- upFolderIcon

```java
protected
Icon
upFolderIcon
```

Up folder icon

- homeFolderIcon

```java
protected
Icon
homeFolderIcon
```

Home folder icon

- listViewIcon

```java
protected
Icon
listViewIcon
```

List view icon

- detailsViewIcon

```java
protected
Icon
detailsViewIcon
```

Details view icon

- viewMenuIcon

```java
protected
Icon
viewMenuIcon
```

View menu icon

- saveButtonMnemonic

```java
protected int saveButtonMnemonic
```

Save button mnemonic

- openButtonMnemonic

```java
protected int openButtonMnemonic
```

Open button mnemonic

- cancelButtonMnemonic

```java
protected int cancelButtonMnemonic
```

Cancel button mnemonic

- updateButtonMnemonic

```java
protected int updateButtonMnemonic
```

Update button mnemonic

- helpButtonMnemonic

```java
protected int helpButtonMnemonic
```

Help button mnemonic

- directoryOpenButtonMnemonic

```java
protected int directoryOpenButtonMnemonic
```

The mnemonic keycode used for the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

**Since:** 1.4

- saveButtonText

```java
protected
String
saveButtonText
```

Save button text

- openButtonText

```java
protected
String
openButtonText
```

Open button text

- cancelButtonText

```java
protected
String
cancelButtonText
```

Cancel button text

- updateButtonText

```java
protected
String
updateButtonText
```

Update button text

- helpButtonText

```java
protected
String
helpButtonText
```

Help button text

- directoryOpenButtonText

```java
protected
String
directoryOpenButtonText
```

The label text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

**Since:** 1.4

- saveButtonToolTipText

```java
protected
String
saveButtonToolTipText
```

Save button tool tip text

- openButtonToolTipText

```java
protected
String
openButtonToolTipText
```

Open button tool tip text

- cancelButtonToolTipText

```java
protected
String
cancelButtonToolTipText
```

Cancel button tool tip text

- updateButtonToolTipText

```java
protected
String
updateButtonToolTipText
```

Update button tool tip text

- helpButtonToolTipText

```java
protected
String
helpButtonToolTipText
```

Help button tool tip text

- directoryOpenButtonToolTipText

```java
protected
String
directoryOpenButtonToolTipText
```

The tooltip text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

**Since:** 1.4

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicFileChooserUI

```java
public BasicFileChooserUI​(
JFileChooser
b)
```

Constructs a

BasicFileChooserUI

.

**Parameters:** b

- file chooser

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

Creates a

BasicFileChooserUI

implementation
for the specified component. By default
the

BasicLookAndFeel

class uses

createUI

methods of all basic UIs classes
to instantiate UIs.

**Parameters:** c

- the

JFileChooser

which needs a UI
**Returns:** the

BasicFileChooserUI

object
**Since:** 1.7
**See Also:** UIDefaults.getUI(JComponent)

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Uninstalls the UI.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

- installComponents

```java
public void installComponents​(
JFileChooser
fc)
```

Installs the components.

**Parameters:** fc

- the file chooser

- uninstallComponents

```java
public void uninstallComponents​(
JFileChooser
fc)
```

Uninstalls the components.

**Parameters:** fc

- the file chooser

- installListeners

```java
protected void installListeners​(
JFileChooser
fc)
```

Installs the listeners.

**Parameters:** fc

- the file chooser

- uninstallListeners

```java
protected void uninstallListeners​(
JFileChooser
fc)
```

Uninstalls the listeners.

**Parameters:** fc

- the file chooser

- installDefaults

```java
protected void installDefaults​(
JFileChooser
fc)
```

Installs the defaults.

**Parameters:** fc

- the file chooser

- installIcons

```java
protected void installIcons​(
JFileChooser
fc)
```

Installs the icons.

**Parameters:** fc

- the file chooser

- installStrings

```java
protected void installStrings​(
JFileChooser
fc)
```

Installs the strings.

**Parameters:** fc

- the file chooser

- uninstallDefaults

```java
protected void uninstallDefaults​(
JFileChooser
fc)
```

Uninstalls the defaults.

**Parameters:** fc

- the file chooser

- uninstallIcons

```java
protected void uninstallIcons​(
JFileChooser
fc)
```

Uninstalls the icons.

**Parameters:** fc

- the file chooser

- uninstallStrings

```java
protected void uninstallStrings​(
JFileChooser
fc)
```

Uninstalls the strings.

**Parameters:** fc

- the file chooser

- createModel

```java
protected void createModel()
```

Creates the model.

- getModel

```java
public
BasicDirectoryModel
getModel()
```

Returns the model.

**Returns:** the model

- createPropertyChangeListener

```java
public
PropertyChangeListener
createPropertyChangeListener​(
JFileChooser
fc)
```

Creates the property change listener.

**Parameters:** fc

- the file chooser
**Returns:** the property change listener

- getFileName

```java
public
String
getFileName()
```

Returns the file name.

**Returns:** the file name

- getDirectoryName

```java
public
String
getDirectoryName()
```

Returns the directory name.

**Returns:** the directory name

- setFileName

```java
public void setFileName​(
String
filename)
```

Sets the file name.

**Parameters:** filename

- the file name

- setDirectoryName

```java
public void setDirectoryName​(
String
dirname)
```

Sets the directory name.

**Parameters:** dirname

- the file name

- getFileChooser

```java
public
JFileChooser
getFileChooser()
```

Returns the file chooser.

**Returns:** the file chooser

- getAccessoryPanel

```java
public
JPanel
getAccessoryPanel()
```

Returns the accessory panel.

**Returns:** the accessory panel

- getApproveButton

```java
protected
JButton
getApproveButton​(
JFileChooser
fc)
```

Returns the approve button.

**Parameters:** fc

- the file chooser
**Returns:** the approve button

- getApproveButtonToolTipText

```java
public
String
getApproveButtonToolTipText​(
JFileChooser
fc)
```

Returns the approve button tool tip.

**Parameters:** fc

- the file chooser
**Returns:** the approve button tool tip

- clearIconCache

```java
public void clearIconCache()
```

Clears the icon cache.

- createDoubleClickListener

```java
protected
MouseListener
createDoubleClickListener​(
JFileChooser
fc,

JList
<?> list)
```

Creates a double click listener.

**Parameters:** fc

- the file chooser
**Parameters:** list

- the list
**Returns:** a double click listener

- createListSelectionListener

```java
public
ListSelectionListener
createListSelectionListener​(
JFileChooser
fc)
```

Creates a list selection listener.

**Parameters:** fc

- the file chooser
**Returns:** a list selection listener

- isDirectorySelected

```java
protected boolean isDirectorySelected()
```

Property to remember whether a directory is currently selected in the UI.

**Returns:** true

iff a directory is currently selected.
**Since:** 1.4

- setDirectorySelected

```java
protected void setDirectorySelected​(boolean b)
```

Property to remember whether a directory is currently selected in the UI.
This is normally called by the UI on a selection event.

**Parameters:** b

- iff a directory is currently selected.
**Since:** 1.4

- getDirectory

```java
protected
File
getDirectory()
```

Property to remember the directory that is currently selected in the UI.

**Returns:** the value of the

directory

property
**Since:** 1.4
**See Also:** setDirectory(java.io.File)

- setDirectory

```java
protected void setDirectory​(
File
f)
```

Property to remember the directory that is currently selected in the UI.
This is normally called by the UI on a selection event.

**Parameters:** f

- the

File

object representing the directory that is
currently selected
**Since:** 1.4

- getAcceptAllFileFilter

```java
public
FileFilter
getAcceptAllFileFilter​(
JFileChooser
fc)
```

Returns the default accept all file filter

**Specified by:** getAcceptAllFileFilter

in class

FileChooserUI
**Parameters:** fc

- the file chooser
**Returns:** an accept-all file filter

- getDialogTitle

```java
public
String
getDialogTitle​(
JFileChooser
fc)
```

Returns the title of this dialog

**Specified by:** getDialogTitle

in class

FileChooserUI
**Parameters:** fc

- the file chooser
**Returns:** the title of this dialog

- getApproveButtonMnemonic

```java
public int getApproveButtonMnemonic​(
JFileChooser
fc)
```

Returns the approve button mnemonic.

**Parameters:** fc

- the file chooser
**Returns:** the approve button mnemonic

- getNewFolderAction

```java
public
Action
getNewFolderAction()
```

Returns a new folder action.

**Returns:** a new folder action

- getGoHomeAction

```java
public
Action
getGoHomeAction()
```

Returns a go home action.

**Returns:** a go home action

- getChangeToParentDirectoryAction

```java
public
Action
getChangeToParentDirectoryAction()
```

Returns a change to parent directory action.

**Returns:** a change to parent directory action

- getApproveSelectionAction

```java
public
Action
getApproveSelectionAction()
```

Returns an approve selection action.

**Returns:** an approve selection action

- getCancelSelectionAction

```java
public
Action
getCancelSelectionAction()
```

Returns a cancel selection action.

**Returns:** a cancel selection action

- getUpdateAction

```java
public
Action
getUpdateAction()
```

Returns an update action.

**Returns:** an update action

Field Detail

- directoryIcon

```java
protected
Icon
directoryIcon
```

Directory icon

- fileIcon

```java
protected
Icon
fileIcon
```

File icon

- computerIcon

```java
protected
Icon
computerIcon
```

Computer icon

- hardDriveIcon

```java
protected
Icon
hardDriveIcon
```

Hard drive icon

- floppyDriveIcon

```java
protected
Icon
floppyDriveIcon
```

Floppy drive icon

- newFolderIcon

```java
protected
Icon
newFolderIcon
```

New folder icon

- upFolderIcon

```java
protected
Icon
upFolderIcon
```

Up folder icon

- homeFolderIcon

```java
protected
Icon
homeFolderIcon
```

Home folder icon

- listViewIcon

```java
protected
Icon
listViewIcon
```

List view icon

- detailsViewIcon

```java
protected
Icon
detailsViewIcon
```

Details view icon

- viewMenuIcon

```java
protected
Icon
viewMenuIcon
```

View menu icon

- saveButtonMnemonic

```java
protected int saveButtonMnemonic
```

Save button mnemonic

- openButtonMnemonic

```java
protected int openButtonMnemonic
```

Open button mnemonic

- cancelButtonMnemonic

```java
protected int cancelButtonMnemonic
```

Cancel button mnemonic

- updateButtonMnemonic

```java
protected int updateButtonMnemonic
```

Update button mnemonic

- helpButtonMnemonic

```java
protected int helpButtonMnemonic
```

Help button mnemonic

- directoryOpenButtonMnemonic

```java
protected int directoryOpenButtonMnemonic
```

The mnemonic keycode used for the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

**Since:** 1.4

- saveButtonText

```java
protected
String
saveButtonText
```

Save button text

- openButtonText

```java
protected
String
openButtonText
```

Open button text

- cancelButtonText

```java
protected
String
cancelButtonText
```

Cancel button text

- updateButtonText

```java
protected
String
updateButtonText
```

Update button text

- helpButtonText

```java
protected
String
helpButtonText
```

Help button text

- directoryOpenButtonText

```java
protected
String
directoryOpenButtonText
```

The label text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

**Since:** 1.4

- saveButtonToolTipText

```java
protected
String
saveButtonToolTipText
```

Save button tool tip text

- openButtonToolTipText

```java
protected
String
openButtonToolTipText
```

Open button tool tip text

- cancelButtonToolTipText

```java
protected
String
cancelButtonToolTipText
```

Cancel button tool tip text

- updateButtonToolTipText

```java
protected
String
updateButtonToolTipText
```

Update button tool tip text

- helpButtonToolTipText

```java
protected
String
helpButtonToolTipText
```

Help button tool tip text

- directoryOpenButtonToolTipText

```java
protected
String
directoryOpenButtonToolTipText
```

The tooltip text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

**Since:** 1.4

---

#### Field Detail

directoryIcon

```java
protected
Icon
directoryIcon
```

Directory icon

---

#### directoryIcon

protected

Icon

directoryIcon

Directory icon

fileIcon

```java
protected
Icon
fileIcon
```

File icon

---

#### fileIcon

protected

Icon

fileIcon

File icon

computerIcon

```java
protected
Icon
computerIcon
```

Computer icon

---

#### computerIcon

protected

Icon

computerIcon

Computer icon

hardDriveIcon

```java
protected
Icon
hardDriveIcon
```

Hard drive icon

---

#### hardDriveIcon

protected

Icon

hardDriveIcon

Hard drive icon

floppyDriveIcon

```java
protected
Icon
floppyDriveIcon
```

Floppy drive icon

---

#### floppyDriveIcon

protected

Icon

floppyDriveIcon

Floppy drive icon

newFolderIcon

```java
protected
Icon
newFolderIcon
```

New folder icon

---

#### newFolderIcon

protected

Icon

newFolderIcon

New folder icon

upFolderIcon

```java
protected
Icon
upFolderIcon
```

Up folder icon

---

#### upFolderIcon

protected

Icon

upFolderIcon

Up folder icon

homeFolderIcon

```java
protected
Icon
homeFolderIcon
```

Home folder icon

---

#### homeFolderIcon

protected

Icon

homeFolderIcon

Home folder icon

listViewIcon

```java
protected
Icon
listViewIcon
```

List view icon

---

#### listViewIcon

protected

Icon

listViewIcon

List view icon

detailsViewIcon

```java
protected
Icon
detailsViewIcon
```

Details view icon

---

#### detailsViewIcon

protected

Icon

detailsViewIcon

Details view icon

viewMenuIcon

```java
protected
Icon
viewMenuIcon
```

View menu icon

---

#### viewMenuIcon

protected

Icon

viewMenuIcon

View menu icon

saveButtonMnemonic

```java
protected int saveButtonMnemonic
```

Save button mnemonic

---

#### saveButtonMnemonic

protected int saveButtonMnemonic

Save button mnemonic

openButtonMnemonic

```java
protected int openButtonMnemonic
```

Open button mnemonic

---

#### openButtonMnemonic

protected int openButtonMnemonic

Open button mnemonic

cancelButtonMnemonic

```java
protected int cancelButtonMnemonic
```

Cancel button mnemonic

---

#### cancelButtonMnemonic

protected int cancelButtonMnemonic

Cancel button mnemonic

updateButtonMnemonic

```java
protected int updateButtonMnemonic
```

Update button mnemonic

---

#### updateButtonMnemonic

protected int updateButtonMnemonic

Update button mnemonic

helpButtonMnemonic

```java
protected int helpButtonMnemonic
```

Help button mnemonic

---

#### helpButtonMnemonic

protected int helpButtonMnemonic

Help button mnemonic

directoryOpenButtonMnemonic

```java
protected int directoryOpenButtonMnemonic
```

The mnemonic keycode used for the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

**Since:** 1.4

---

#### directoryOpenButtonMnemonic

protected int directoryOpenButtonMnemonic

The mnemonic keycode used for the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

saveButtonText

```java
protected
String
saveButtonText
```

Save button text

---

#### saveButtonText

protected

String

saveButtonText

Save button text

openButtonText

```java
protected
String
openButtonText
```

Open button text

---

#### openButtonText

protected

String

openButtonText

Open button text

cancelButtonText

```java
protected
String
cancelButtonText
```

Cancel button text

---

#### cancelButtonText

protected

String

cancelButtonText

Cancel button text

updateButtonText

```java
protected
String
updateButtonText
```

Update button text

---

#### updateButtonText

protected

String

updateButtonText

Update button text

helpButtonText

```java
protected
String
helpButtonText
```

Help button text

---

#### helpButtonText

protected

String

helpButtonText

Help button text

directoryOpenButtonText

```java
protected
String
directoryOpenButtonText
```

The label text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

**Since:** 1.4

---

#### directoryOpenButtonText

protected

String

directoryOpenButtonText

The label text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

saveButtonToolTipText

```java
protected
String
saveButtonToolTipText
```

Save button tool tip text

---

#### saveButtonToolTipText

protected

String

saveButtonToolTipText

Save button tool tip text

openButtonToolTipText

```java
protected
String
openButtonToolTipText
```

Open button tool tip text

---

#### openButtonToolTipText

protected

String

openButtonToolTipText

Open button tool tip text

cancelButtonToolTipText

```java
protected
String
cancelButtonToolTipText
```

Cancel button tool tip text

---

#### cancelButtonToolTipText

protected

String

cancelButtonToolTipText

Cancel button tool tip text

updateButtonToolTipText

```java
protected
String
updateButtonToolTipText
```

Update button tool tip text

---

#### updateButtonToolTipText

protected

String

updateButtonToolTipText

Update button tool tip text

helpButtonToolTipText

```java
protected
String
helpButtonToolTipText
```

Help button tool tip text

---

#### helpButtonToolTipText

protected

String

helpButtonToolTipText

Help button tool tip text

directoryOpenButtonToolTipText

```java
protected
String
directoryOpenButtonToolTipText
```

The tooltip text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

**Since:** 1.4

---

#### directoryOpenButtonToolTipText

protected

String

directoryOpenButtonToolTipText

The tooltip text displayed on the approve button when a directory
is selected and the current selection mode is FILES_ONLY.

Constructor Detail

- BasicFileChooserUI

```java
public BasicFileChooserUI​(
JFileChooser
b)
```

Constructs a

BasicFileChooserUI

.

**Parameters:** b

- file chooser

---

#### Constructor Detail

BasicFileChooserUI

```java
public BasicFileChooserUI​(
JFileChooser
b)
```

Constructs a

BasicFileChooserUI

.

**Parameters:** b

- file chooser

---

#### BasicFileChooserUI

public BasicFileChooserUI​(

JFileChooser

b)

Constructs a

BasicFileChooserUI

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

Creates a

BasicFileChooserUI

implementation
for the specified component. By default
the

BasicLookAndFeel

class uses

createUI

methods of all basic UIs classes
to instantiate UIs.

**Parameters:** c

- the

JFileChooser

which needs a UI
**Returns:** the

BasicFileChooserUI

object
**Since:** 1.7
**See Also:** UIDefaults.getUI(JComponent)

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Uninstalls the UI.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

- installComponents

```java
public void installComponents​(
JFileChooser
fc)
```

Installs the components.

**Parameters:** fc

- the file chooser

- uninstallComponents

```java
public void uninstallComponents​(
JFileChooser
fc)
```

Uninstalls the components.

**Parameters:** fc

- the file chooser

- installListeners

```java
protected void installListeners​(
JFileChooser
fc)
```

Installs the listeners.

**Parameters:** fc

- the file chooser

- uninstallListeners

```java
protected void uninstallListeners​(
JFileChooser
fc)
```

Uninstalls the listeners.

**Parameters:** fc

- the file chooser

- installDefaults

```java
protected void installDefaults​(
JFileChooser
fc)
```

Installs the defaults.

**Parameters:** fc

- the file chooser

- installIcons

```java
protected void installIcons​(
JFileChooser
fc)
```

Installs the icons.

**Parameters:** fc

- the file chooser

- installStrings

```java
protected void installStrings​(
JFileChooser
fc)
```

Installs the strings.

**Parameters:** fc

- the file chooser

- uninstallDefaults

```java
protected void uninstallDefaults​(
JFileChooser
fc)
```

Uninstalls the defaults.

**Parameters:** fc

- the file chooser

- uninstallIcons

```java
protected void uninstallIcons​(
JFileChooser
fc)
```

Uninstalls the icons.

**Parameters:** fc

- the file chooser

- uninstallStrings

```java
protected void uninstallStrings​(
JFileChooser
fc)
```

Uninstalls the strings.

**Parameters:** fc

- the file chooser

- createModel

```java
protected void createModel()
```

Creates the model.

- getModel

```java
public
BasicDirectoryModel
getModel()
```

Returns the model.

**Returns:** the model

- createPropertyChangeListener

```java
public
PropertyChangeListener
createPropertyChangeListener​(
JFileChooser
fc)
```

Creates the property change listener.

**Parameters:** fc

- the file chooser
**Returns:** the property change listener

- getFileName

```java
public
String
getFileName()
```

Returns the file name.

**Returns:** the file name

- getDirectoryName

```java
public
String
getDirectoryName()
```

Returns the directory name.

**Returns:** the directory name

- setFileName

```java
public void setFileName​(
String
filename)
```

Sets the file name.

**Parameters:** filename

- the file name

- setDirectoryName

```java
public void setDirectoryName​(
String
dirname)
```

Sets the directory name.

**Parameters:** dirname

- the file name

- getFileChooser

```java
public
JFileChooser
getFileChooser()
```

Returns the file chooser.

**Returns:** the file chooser

- getAccessoryPanel

```java
public
JPanel
getAccessoryPanel()
```

Returns the accessory panel.

**Returns:** the accessory panel

- getApproveButton

```java
protected
JButton
getApproveButton​(
JFileChooser
fc)
```

Returns the approve button.

**Parameters:** fc

- the file chooser
**Returns:** the approve button

- getApproveButtonToolTipText

```java
public
String
getApproveButtonToolTipText​(
JFileChooser
fc)
```

Returns the approve button tool tip.

**Parameters:** fc

- the file chooser
**Returns:** the approve button tool tip

- clearIconCache

```java
public void clearIconCache()
```

Clears the icon cache.

- createDoubleClickListener

```java
protected
MouseListener
createDoubleClickListener​(
JFileChooser
fc,

JList
<?> list)
```

Creates a double click listener.

**Parameters:** fc

- the file chooser
**Parameters:** list

- the list
**Returns:** a double click listener

- createListSelectionListener

```java
public
ListSelectionListener
createListSelectionListener​(
JFileChooser
fc)
```

Creates a list selection listener.

**Parameters:** fc

- the file chooser
**Returns:** a list selection listener

- isDirectorySelected

```java
protected boolean isDirectorySelected()
```

Property to remember whether a directory is currently selected in the UI.

**Returns:** true

iff a directory is currently selected.
**Since:** 1.4

- setDirectorySelected

```java
protected void setDirectorySelected​(boolean b)
```

Property to remember whether a directory is currently selected in the UI.
This is normally called by the UI on a selection event.

**Parameters:** b

- iff a directory is currently selected.
**Since:** 1.4

- getDirectory

```java
protected
File
getDirectory()
```

Property to remember the directory that is currently selected in the UI.

**Returns:** the value of the

directory

property
**Since:** 1.4
**See Also:** setDirectory(java.io.File)

- setDirectory

```java
protected void setDirectory​(
File
f)
```

Property to remember the directory that is currently selected in the UI.
This is normally called by the UI on a selection event.

**Parameters:** f

- the

File

object representing the directory that is
currently selected
**Since:** 1.4

- getAcceptAllFileFilter

```java
public
FileFilter
getAcceptAllFileFilter​(
JFileChooser
fc)
```

Returns the default accept all file filter

**Specified by:** getAcceptAllFileFilter

in class

FileChooserUI
**Parameters:** fc

- the file chooser
**Returns:** an accept-all file filter

- getDialogTitle

```java
public
String
getDialogTitle​(
JFileChooser
fc)
```

Returns the title of this dialog

**Specified by:** getDialogTitle

in class

FileChooserUI
**Parameters:** fc

- the file chooser
**Returns:** the title of this dialog

- getApproveButtonMnemonic

```java
public int getApproveButtonMnemonic​(
JFileChooser
fc)
```

Returns the approve button mnemonic.

**Parameters:** fc

- the file chooser
**Returns:** the approve button mnemonic

- getNewFolderAction

```java
public
Action
getNewFolderAction()
```

Returns a new folder action.

**Returns:** a new folder action

- getGoHomeAction

```java
public
Action
getGoHomeAction()
```

Returns a go home action.

**Returns:** a go home action

- getChangeToParentDirectoryAction

```java
public
Action
getChangeToParentDirectoryAction()
```

Returns a change to parent directory action.

**Returns:** a change to parent directory action

- getApproveSelectionAction

```java
public
Action
getApproveSelectionAction()
```

Returns an approve selection action.

**Returns:** an approve selection action

- getCancelSelectionAction

```java
public
Action
getCancelSelectionAction()
```

Returns a cancel selection action.

**Returns:** a cancel selection action

- getUpdateAction

```java
public
Action
getUpdateAction()
```

Returns an update action.

**Returns:** an update action

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

Creates a

BasicFileChooserUI

implementation
for the specified component. By default
the

BasicLookAndFeel

class uses

createUI

methods of all basic UIs classes
to instantiate UIs.

**Parameters:** c

- the

JFileChooser

which needs a UI
**Returns:** the

BasicFileChooserUI

object
**Since:** 1.7
**See Also:** UIDefaults.getUI(JComponent)

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Creates a

BasicFileChooserUI

implementation
for the specified component. By default
the

BasicLookAndFeel

class uses

createUI

methods of all basic UIs classes
to instantiate UIs.

installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

---

#### installUI

public void installUI​(

JComponent

c)

Installs the UI.

uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Uninstalls the UI.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

---

#### uninstallUI

public void uninstallUI​(

JComponent

c)

Uninstalls the UI.

installComponents

```java
public void installComponents​(
JFileChooser
fc)
```

Installs the components.

**Parameters:** fc

- the file chooser

---

#### installComponents

public void installComponents​(

JFileChooser

fc)

Installs the components.

uninstallComponents

```java
public void uninstallComponents​(
JFileChooser
fc)
```

Uninstalls the components.

**Parameters:** fc

- the file chooser

---

#### uninstallComponents

public void uninstallComponents​(

JFileChooser

fc)

Uninstalls the components.

installListeners

```java
protected void installListeners​(
JFileChooser
fc)
```

Installs the listeners.

**Parameters:** fc

- the file chooser

---

#### installListeners

protected void installListeners​(

JFileChooser

fc)

Installs the listeners.

uninstallListeners

```java
protected void uninstallListeners​(
JFileChooser
fc)
```

Uninstalls the listeners.

**Parameters:** fc

- the file chooser

---

#### uninstallListeners

protected void uninstallListeners​(

JFileChooser

fc)

Uninstalls the listeners.

installDefaults

```java
protected void installDefaults​(
JFileChooser
fc)
```

Installs the defaults.

**Parameters:** fc

- the file chooser

---

#### installDefaults

protected void installDefaults​(

JFileChooser

fc)

Installs the defaults.

installIcons

```java
protected void installIcons​(
JFileChooser
fc)
```

Installs the icons.

**Parameters:** fc

- the file chooser

---

#### installIcons

protected void installIcons​(

JFileChooser

fc)

Installs the icons.

installStrings

```java
protected void installStrings​(
JFileChooser
fc)
```

Installs the strings.

**Parameters:** fc

- the file chooser

---

#### installStrings

protected void installStrings​(

JFileChooser

fc)

Installs the strings.

uninstallDefaults

```java
protected void uninstallDefaults​(
JFileChooser
fc)
```

Uninstalls the defaults.

**Parameters:** fc

- the file chooser

---

#### uninstallDefaults

protected void uninstallDefaults​(

JFileChooser

fc)

Uninstalls the defaults.

uninstallIcons

```java
protected void uninstallIcons​(
JFileChooser
fc)
```

Uninstalls the icons.

**Parameters:** fc

- the file chooser

---

#### uninstallIcons

protected void uninstallIcons​(

JFileChooser

fc)

Uninstalls the icons.

uninstallStrings

```java
protected void uninstallStrings​(
JFileChooser
fc)
```

Uninstalls the strings.

**Parameters:** fc

- the file chooser

---

#### uninstallStrings

protected void uninstallStrings​(

JFileChooser

fc)

Uninstalls the strings.

createModel

```java
protected void createModel()
```

Creates the model.

---

#### createModel

protected void createModel()

Creates the model.

getModel

```java
public
BasicDirectoryModel
getModel()
```

Returns the model.

**Returns:** the model

---

#### getModel

public

BasicDirectoryModel

getModel()

Returns the model.

createPropertyChangeListener

```java
public
PropertyChangeListener
createPropertyChangeListener​(
JFileChooser
fc)
```

Creates the property change listener.

**Parameters:** fc

- the file chooser
**Returns:** the property change listener

---

#### createPropertyChangeListener

public

PropertyChangeListener

createPropertyChangeListener​(

JFileChooser

fc)

Creates the property change listener.

getFileName

```java
public
String
getFileName()
```

Returns the file name.

**Returns:** the file name

---

#### getFileName

public

String

getFileName()

Returns the file name.

getDirectoryName

```java
public
String
getDirectoryName()
```

Returns the directory name.

**Returns:** the directory name

---

#### getDirectoryName

public

String

getDirectoryName()

Returns the directory name.

setFileName

```java
public void setFileName​(
String
filename)
```

Sets the file name.

**Parameters:** filename

- the file name

---

#### setFileName

public void setFileName​(

String

filename)

Sets the file name.

setDirectoryName

```java
public void setDirectoryName​(
String
dirname)
```

Sets the directory name.

**Parameters:** dirname

- the file name

---

#### setDirectoryName

public void setDirectoryName​(

String

dirname)

Sets the directory name.

getFileChooser

```java
public
JFileChooser
getFileChooser()
```

Returns the file chooser.

**Returns:** the file chooser

---

#### getFileChooser

public

JFileChooser

getFileChooser()

Returns the file chooser.

getAccessoryPanel

```java
public
JPanel
getAccessoryPanel()
```

Returns the accessory panel.

**Returns:** the accessory panel

---

#### getAccessoryPanel

public

JPanel

getAccessoryPanel()

Returns the accessory panel.

getApproveButton

```java
protected
JButton
getApproveButton​(
JFileChooser
fc)
```

Returns the approve button.

**Parameters:** fc

- the file chooser
**Returns:** the approve button

---

#### getApproveButton

protected

JButton

getApproveButton​(

JFileChooser

fc)

Returns the approve button.

getApproveButtonToolTipText

```java
public
String
getApproveButtonToolTipText​(
JFileChooser
fc)
```

Returns the approve button tool tip.

**Parameters:** fc

- the file chooser
**Returns:** the approve button tool tip

---

#### getApproveButtonToolTipText

public

String

getApproveButtonToolTipText​(

JFileChooser

fc)

Returns the approve button tool tip.

clearIconCache

```java
public void clearIconCache()
```

Clears the icon cache.

---

#### clearIconCache

public void clearIconCache()

Clears the icon cache.

createDoubleClickListener

```java
protected
MouseListener
createDoubleClickListener​(
JFileChooser
fc,

JList
<?> list)
```

Creates a double click listener.

**Parameters:** fc

- the file chooser
**Parameters:** list

- the list
**Returns:** a double click listener

---

#### createDoubleClickListener

protected

MouseListener

createDoubleClickListener​(

JFileChooser

fc,

JList

<?> list)

Creates a double click listener.

createListSelectionListener

```java
public
ListSelectionListener
createListSelectionListener​(
JFileChooser
fc)
```

Creates a list selection listener.

**Parameters:** fc

- the file chooser
**Returns:** a list selection listener

---

#### createListSelectionListener

public

ListSelectionListener

createListSelectionListener​(

JFileChooser

fc)

Creates a list selection listener.

isDirectorySelected

```java
protected boolean isDirectorySelected()
```

Property to remember whether a directory is currently selected in the UI.

**Returns:** true

iff a directory is currently selected.
**Since:** 1.4

---

#### isDirectorySelected

protected boolean isDirectorySelected()

Property to remember whether a directory is currently selected in the UI.

setDirectorySelected

```java
protected void setDirectorySelected​(boolean b)
```

Property to remember whether a directory is currently selected in the UI.
This is normally called by the UI on a selection event.

**Parameters:** b

- iff a directory is currently selected.
**Since:** 1.4

---

#### setDirectorySelected

protected void setDirectorySelected​(boolean b)

Property to remember whether a directory is currently selected in the UI.
This is normally called by the UI on a selection event.

getDirectory

```java
protected
File
getDirectory()
```

Property to remember the directory that is currently selected in the UI.

**Returns:** the value of the

directory

property
**Since:** 1.4
**See Also:** setDirectory(java.io.File)

---

#### getDirectory

protected

File

getDirectory()

Property to remember the directory that is currently selected in the UI.

setDirectory

```java
protected void setDirectory​(
File
f)
```

Property to remember the directory that is currently selected in the UI.
This is normally called by the UI on a selection event.

**Parameters:** f

- the

File

object representing the directory that is
currently selected
**Since:** 1.4

---

#### setDirectory

protected void setDirectory​(

File

f)

Property to remember the directory that is currently selected in the UI.
This is normally called by the UI on a selection event.

getAcceptAllFileFilter

```java
public
FileFilter
getAcceptAllFileFilter​(
JFileChooser
fc)
```

Returns the default accept all file filter

**Specified by:** getAcceptAllFileFilter

in class

FileChooserUI
**Parameters:** fc

- the file chooser
**Returns:** an accept-all file filter

---

#### getAcceptAllFileFilter

public

FileFilter

getAcceptAllFileFilter​(

JFileChooser

fc)

Returns the default accept all file filter

getDialogTitle

```java
public
String
getDialogTitle​(
JFileChooser
fc)
```

Returns the title of this dialog

**Specified by:** getDialogTitle

in class

FileChooserUI
**Parameters:** fc

- the file chooser
**Returns:** the title of this dialog

---

#### getDialogTitle

public

String

getDialogTitle​(

JFileChooser

fc)

Returns the title of this dialog

getApproveButtonMnemonic

```java
public int getApproveButtonMnemonic​(
JFileChooser
fc)
```

Returns the approve button mnemonic.

**Parameters:** fc

- the file chooser
**Returns:** the approve button mnemonic

---

#### getApproveButtonMnemonic

public int getApproveButtonMnemonic​(

JFileChooser

fc)

Returns the approve button mnemonic.

getNewFolderAction

```java
public
Action
getNewFolderAction()
```

Returns a new folder action.

**Returns:** a new folder action

---

#### getNewFolderAction

public

Action

getNewFolderAction()

Returns a new folder action.

getGoHomeAction

```java
public
Action
getGoHomeAction()
```

Returns a go home action.

**Returns:** a go home action

---

#### getGoHomeAction

public

Action

getGoHomeAction()

Returns a go home action.

getChangeToParentDirectoryAction

```java
public
Action
getChangeToParentDirectoryAction()
```

Returns a change to parent directory action.

**Returns:** a change to parent directory action

---

#### getChangeToParentDirectoryAction

public

Action

getChangeToParentDirectoryAction()

Returns a change to parent directory action.

getApproveSelectionAction

```java
public
Action
getApproveSelectionAction()
```

Returns an approve selection action.

**Returns:** an approve selection action

---

#### getApproveSelectionAction

public

Action

getApproveSelectionAction()

Returns an approve selection action.

getCancelSelectionAction

```java
public
Action
getCancelSelectionAction()
```

Returns a cancel selection action.

**Returns:** a cancel selection action

---

#### getCancelSelectionAction

public

Action

getCancelSelectionAction()

Returns a cancel selection action.

getUpdateAction

```java
public
Action
getUpdateAction()
```

Returns an update action.

**Returns:** an update action

---

#### getUpdateAction

public

Action

getUpdateAction()

Returns an update action.

---

