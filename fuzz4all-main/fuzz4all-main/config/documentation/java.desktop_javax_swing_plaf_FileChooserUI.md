# Class FileChooserUI

**Source:** `java.desktop\javax\swing\plaf\FileChooserUI.html`

### Class Description

```java
public abstract class
FileChooserUI

extends
ComponentUI
```

Pluggable look and feel interface for

JFileChooser

.

**Direct Known Subclasses:** BasicFileChooserUI

,

MultiFileChooserUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public FileChooserUI()

*No description found.*

---

### Method Details

#### public abstract
FileFilter
getAcceptAllFileFilter​(
JFileChooser
fc)

Returns an accept-all file filter.

**Parameters:**
- fc

- the file chooser

**Returns:**
- an accept-all file filter

---

#### public abstract
FileView
getFileView​(
JFileChooser
fc)

Returns a file view.

**Parameters:**
- fc

- the file chooser

**Returns:**
- a file view

---

#### public abstract
String
getApproveButtonText​(
JFileChooser
fc)

Returns approve button text.

**Parameters:**
- fc

- the file chooser

**Returns:**
- approve button text.

---

#### public abstract
String
getDialogTitle​(
JFileChooser
fc)

Returns the dialog title.

**Parameters:**
- fc

- the file chooser

**Returns:**
- the dialog title.

---

#### public abstract void rescanCurrentDirectory​(
JFileChooser
fc)

Rescan the current directory.

**Parameters:**
- fc

- the file chooser

---

#### public abstract void ensureFileIsVisible​(
JFileChooser
fc,

File
f)

Ensure the file in question is visible.

**Parameters:**
- fc

- the file chooser
- f

- the file

---

#### public
JButton
getDefaultButton​(
JFileChooser
fc)

Returns default button for current

LookAndFeel

.

JFileChooser

will use this button as default button
for dialog windows.

**Parameters:**
- fc

- the

JFileChooser

whose default button is requested

**Returns:**
- the default JButton for current look and feel

**Since:**
- 1.7

---

### Additional Sections

#### Class FileChooserUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.FileChooserUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.FileChooserUI

javax.swing.plaf.FileChooserUI

**Direct Known Subclasses:** BasicFileChooserUI

,

MultiFileChooserUI

```java
public abstract class
FileChooserUI

extends
ComponentUI
```

Pluggable look and feel interface for

JFileChooser

.

public abstract class

FileChooserUI

extends

ComponentUI

Pluggable look and feel interface for

JFileChooser

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FileChooserUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

ensureFileIsVisible

​(

JFileChooser

fc,

File

f)

Ensure the file in question is visible.

abstract

FileFilter

getAcceptAllFileFilter

​(

JFileChooser

fc)

Returns an accept-all file filter.

abstract

String

getApproveButtonText

​(

JFileChooser

fc)

Returns approve button text.

JButton

getDefaultButton

​(

JFileChooser

fc)

Returns default button for current

LookAndFeel

.

abstract

String

getDialogTitle

​(

JFileChooser

fc)

Returns the dialog title.

abstract

FileView

getFileView

​(

JFileChooser

fc)

Returns a file view.

abstract void

rescanCurrentDirectory

​(

JFileChooser

fc)

Rescan the current directory.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

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

Constructor Summary

Constructors

Constructor

Description

FileChooserUI

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

ensureFileIsVisible

​(

JFileChooser

fc,

File

f)

Ensure the file in question is visible.

abstract

FileFilter

getAcceptAllFileFilter

​(

JFileChooser

fc)

Returns an accept-all file filter.

abstract

String

getApproveButtonText

​(

JFileChooser

fc)

Returns approve button text.

JButton

getDefaultButton

​(

JFileChooser

fc)

Returns default button for current

LookAndFeel

.

abstract

String

getDialogTitle

​(

JFileChooser

fc)

Returns the dialog title.

abstract

FileView

getFileView

​(

JFileChooser

fc)

Returns a file view.

abstract void

rescanCurrentDirectory

​(

JFileChooser

fc)

Rescan the current directory.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

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

Ensure the file in question is visible.

Returns an accept-all file filter.

Returns approve button text.

Returns default button for current

LookAndFeel

.

Returns the dialog title.

Returns a file view.

Rescan the current directory.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

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

- FileChooserUI

```java
public FileChooserUI()
```

============ METHOD DETAIL ==========

- Method Detail

- getAcceptAllFileFilter

```java
public abstract
FileFilter
getAcceptAllFileFilter​(
JFileChooser
fc)
```

Returns an accept-all file filter.

**Parameters:** fc

- the file chooser
**Returns:** an accept-all file filter

- getFileView

```java
public abstract
FileView
getFileView​(
JFileChooser
fc)
```

Returns a file view.

**Parameters:** fc

- the file chooser
**Returns:** a file view

- getApproveButtonText

```java
public abstract
String
getApproveButtonText​(
JFileChooser
fc)
```

Returns approve button text.

**Parameters:** fc

- the file chooser
**Returns:** approve button text.

- getDialogTitle

```java
public abstract
String
getDialogTitle​(
JFileChooser
fc)
```

Returns the dialog title.

**Parameters:** fc

- the file chooser
**Returns:** the dialog title.

- rescanCurrentDirectory

```java
public abstract void rescanCurrentDirectory​(
JFileChooser
fc)
```

Rescan the current directory.

**Parameters:** fc

- the file chooser

- ensureFileIsVisible

```java
public abstract void ensureFileIsVisible​(
JFileChooser
fc,

File
f)
```

Ensure the file in question is visible.

**Parameters:** fc

- the file chooser
**Parameters:** f

- the file

- getDefaultButton

```java
public
JButton
getDefaultButton​(
JFileChooser
fc)
```

Returns default button for current

LookAndFeel

.

JFileChooser

will use this button as default button
for dialog windows.

**Parameters:** fc

- the

JFileChooser

whose default button is requested
**Returns:** the default JButton for current look and feel
**Since:** 1.7

Constructor Detail

- FileChooserUI

```java
public FileChooserUI()
```

---

#### Constructor Detail

FileChooserUI

```java
public FileChooserUI()
```

---

#### FileChooserUI

public FileChooserUI()

Method Detail

- getAcceptAllFileFilter

```java
public abstract
FileFilter
getAcceptAllFileFilter​(
JFileChooser
fc)
```

Returns an accept-all file filter.

**Parameters:** fc

- the file chooser
**Returns:** an accept-all file filter

- getFileView

```java
public abstract
FileView
getFileView​(
JFileChooser
fc)
```

Returns a file view.

**Parameters:** fc

- the file chooser
**Returns:** a file view

- getApproveButtonText

```java
public abstract
String
getApproveButtonText​(
JFileChooser
fc)
```

Returns approve button text.

**Parameters:** fc

- the file chooser
**Returns:** approve button text.

- getDialogTitle

```java
public abstract
String
getDialogTitle​(
JFileChooser
fc)
```

Returns the dialog title.

**Parameters:** fc

- the file chooser
**Returns:** the dialog title.

- rescanCurrentDirectory

```java
public abstract void rescanCurrentDirectory​(
JFileChooser
fc)
```

Rescan the current directory.

**Parameters:** fc

- the file chooser

- ensureFileIsVisible

```java
public abstract void ensureFileIsVisible​(
JFileChooser
fc,

File
f)
```

Ensure the file in question is visible.

**Parameters:** fc

- the file chooser
**Parameters:** f

- the file

- getDefaultButton

```java
public
JButton
getDefaultButton​(
JFileChooser
fc)
```

Returns default button for current

LookAndFeel

.

JFileChooser

will use this button as default button
for dialog windows.

**Parameters:** fc

- the

JFileChooser

whose default button is requested
**Returns:** the default JButton for current look and feel
**Since:** 1.7

---

#### Method Detail

getAcceptAllFileFilter

```java
public abstract
FileFilter
getAcceptAllFileFilter​(
JFileChooser
fc)
```

Returns an accept-all file filter.

**Parameters:** fc

- the file chooser
**Returns:** an accept-all file filter

---

#### getAcceptAllFileFilter

public abstract

FileFilter

getAcceptAllFileFilter​(

JFileChooser

fc)

Returns an accept-all file filter.

getFileView

```java
public abstract
FileView
getFileView​(
JFileChooser
fc)
```

Returns a file view.

**Parameters:** fc

- the file chooser
**Returns:** a file view

---

#### getFileView

public abstract

FileView

getFileView​(

JFileChooser

fc)

Returns a file view.

getApproveButtonText

```java
public abstract
String
getApproveButtonText​(
JFileChooser
fc)
```

Returns approve button text.

**Parameters:** fc

- the file chooser
**Returns:** approve button text.

---

#### getApproveButtonText

public abstract

String

getApproveButtonText​(

JFileChooser

fc)

Returns approve button text.

getDialogTitle

```java
public abstract
String
getDialogTitle​(
JFileChooser
fc)
```

Returns the dialog title.

**Parameters:** fc

- the file chooser
**Returns:** the dialog title.

---

#### getDialogTitle

public abstract

String

getDialogTitle​(

JFileChooser

fc)

Returns the dialog title.

rescanCurrentDirectory

```java
public abstract void rescanCurrentDirectory​(
JFileChooser
fc)
```

Rescan the current directory.

**Parameters:** fc

- the file chooser

---

#### rescanCurrentDirectory

public abstract void rescanCurrentDirectory​(

JFileChooser

fc)

Rescan the current directory.

ensureFileIsVisible

```java
public abstract void ensureFileIsVisible​(
JFileChooser
fc,

File
f)
```

Ensure the file in question is visible.

**Parameters:** fc

- the file chooser
**Parameters:** f

- the file

---

#### ensureFileIsVisible

public abstract void ensureFileIsVisible​(

JFileChooser

fc,

File

f)

Ensure the file in question is visible.

getDefaultButton

```java
public
JButton
getDefaultButton​(
JFileChooser
fc)
```

Returns default button for current

LookAndFeel

.

JFileChooser

will use this button as default button
for dialog windows.

**Parameters:** fc

- the

JFileChooser

whose default button is requested
**Returns:** the default JButton for current look and feel
**Since:** 1.7

---

#### getDefaultButton

public

JButton

getDefaultButton​(

JFileChooser

fc)

Returns default button for current

LookAndFeel

.

JFileChooser

will use this button as default button
for dialog windows.

---

