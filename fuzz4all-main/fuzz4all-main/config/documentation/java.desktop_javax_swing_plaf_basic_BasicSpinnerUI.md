# Class BasicSpinnerUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicSpinnerUI.html`

### Class Description

```java
public class
BasicSpinnerUI

extends
SpinnerUI
```

The default Spinner UI delegate.

**Direct Known Subclasses:** SynthSpinnerUI

---

### Field Details

#### protected
JSpinner
spinner

The spinner that we're a UI delegate for. Initialized by
the

installUI

method, and reset to null
by

uninstallUI

.

**See Also:**
- installUI(javax.swing.JComponent)

,

uninstallUI(javax.swing.JComponent)

---

### Constructor Details

#### public BasicSpinnerUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Returns a new instance of BasicSpinnerUI. SpinnerListUI
delegates are allocated one per JSpinner.

**Parameters:**
- c

- the JSpinner (not used)

**Returns:**
- a new BasicSpinnerUI object

**See Also:**
- ComponentUI.createUI(javax.swing.JComponent)

---

#### public void installUI​(
JComponent
c)

Calls

installDefaults

,

installListeners

,
and then adds the components returned by

createNextButton

,

createPreviousButton

, and

createEditor

.

**Overrides:**
- installUI

in class

ComponentUI

**Parameters:**
- c

- the JSpinner

**See Also:**
- installDefaults()

,

installListeners()

,

createNextButton()

,

createPreviousButton()

,

createEditor()

---

#### public void uninstallUI​(
JComponent
c)

Calls

uninstallDefaults

,

uninstallListeners

,
and then removes all of the spinners children.

**Overrides:**
- uninstallUI

in class

ComponentUI

**Parameters:**
- c

- the JSpinner (not used)

**See Also:**
- ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

---

#### protected void installListeners()

Initializes

PropertyChangeListener

with
a shared object that delegates interesting PropertyChangeEvents
to protected methods.

This method is called by

installUI

.

**See Also:**
- replaceEditor(javax.swing.JComponent, javax.swing.JComponent)

,

uninstallListeners()

---

#### protected void uninstallListeners()

Removes the

PropertyChangeListener

added
by installListeners.

This method is called by

uninstallUI

.

**See Also:**
- installListeners()

---

#### protected void installDefaults()

Initialize the

JSpinner

border

,

foreground

, and

background

, properties
based on the corresponding "Spinner.*" properties from defaults table.
The

JSpinners

layout is set to the value returned by

createLayout

. This method is called by

installUI

.

**See Also:**
- uninstallDefaults()

,

installUI(javax.swing.JComponent)

,

createLayout()

,

LookAndFeel.installBorder(javax.swing.JComponent, java.lang.String)

,

LookAndFeel.installColors(javax.swing.JComponent, java.lang.String, java.lang.String)

---

#### protected void uninstallDefaults()

Sets the

JSpinner's

layout manager to null. This
method is called by

uninstallUI

.

**See Also:**
- installDefaults()

,

uninstallUI(javax.swing.JComponent)

---

#### protected void installNextButtonListeners​(
Component
c)

Installs the necessary listeners on the next button,

c

,
to update the

JSpinner

in response to a user gesture.

**Parameters:**
- c

- Component to install the listeners on

**Throws:**
- NullPointerException

- if

c

is null.

**See Also:**
- createNextButton()

**Since:**
- 1.5

---

#### protected void installPreviousButtonListeners​(
Component
c)

Installs the necessary listeners on the previous button,

c

,
to update the

JSpinner

in response to a user gesture.

**Parameters:**
- c

- Component to install the listeners on.

**Throws:**
- NullPointerException

- if

c

is null.

**See Also:**
- createPreviousButton()

**Since:**
- 1.5

---

#### protected
LayoutManager
createLayout()

Creates a

LayoutManager

that manages the

editor

,

nextButton

, and

previousButton

children of the JSpinner. These three children must be
added with a constraint that identifies their role:
"Editor", "Next", and "Previous". The default layout manager
can handle the absence of any of these children.

**Returns:**
- a LayoutManager for the editor, next button, and previous button.

**See Also:**
- createNextButton()

,

createPreviousButton()

,

createEditor()

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Creates a

PropertyChangeListener

that can be
added to the JSpinner itself. Typically, this listener
will call replaceEditor when the "editor" property changes,
since it's the

SpinnerUI's

responsibility to
add the editor to the JSpinner (and remove the old one).
This method is called by

installListeners

.

**Returns:**
- A PropertyChangeListener for the JSpinner itself

**See Also:**
- installListeners()

---

#### protected
Component
createPreviousButton()

Creates a decrement button, i.e. component that replaces the spinner
value with the object returned by

spinner.getPreviousValue

.
By default the

previousButton

is a

JButton

. If the
decrement button is not needed this method should return

null

.

**Returns:**
- a component that will replace the spinner's value with the
previous value in the sequence, or

null

**See Also:**
- installUI(javax.swing.JComponent)

,

createNextButton()

,

installPreviousButtonListeners(java.awt.Component)

---

#### protected
Component
createNextButton()

Creates an increment button, i.e. component that replaces the spinner
value with the object returned by

spinner.getNextValue

.
By default the

nextButton

is a

JButton

. If the
increment button is not needed this method should return

null

.

**Returns:**
- a component that will replace the spinner's value with the
next value in the sequence, or

null

**See Also:**
- installUI(javax.swing.JComponent)

,

createPreviousButton()

,

installNextButtonListeners(java.awt.Component)

---

#### protected
JComponent
createEditor()

This method is called by installUI to get the editor component
of the

JSpinner

. By default it just returns

JSpinner.getEditor()

. Subclasses can override

createEditor

to return a component that contains
the spinner's editor or null, if they're going to handle adding
the editor to the

JSpinner

in an

installUI

override.

Typically this method would be overridden to wrap the editor
with a container with a custom border, since one can't assume
that the editors border can be set directly.

The

replaceEditor

method is called when the spinners
editor is changed with

JSpinner.setEditor

. If you've
overriden this method, then you'll probably want to override

replaceEditor

as well.

**Returns:**
- the JSpinners editor JComponent, spinner.getEditor() by default

**See Also:**
- installUI(javax.swing.JComponent)

,

replaceEditor(javax.swing.JComponent, javax.swing.JComponent)

,

JSpinner.getEditor()

---

#### protected void replaceEditor​(
JComponent
oldEditor,

JComponent
newEditor)

Called by the

PropertyChangeListener

when the

JSpinner

editor property changes. It's the responsibility
of this method to remove the old editor and add the new one. By
default this operation is just:

```java
spinner.remove(oldEditor);
spinner.add(newEditor, "Editor");
```

The implementation of

replaceEditor

should be coordinated
with the

createEditor

method.

**Parameters:**
- oldEditor

- an old instance of editor
- newEditor

- a new instance of editor

**See Also:**
- createEditor()

,

createPropertyChangeListener()

---

#### protected void installKeyboardActions()

Installs the keyboard Actions onto the JSpinner.

**Since:**
- 1.5

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

#### Class BasicSpinnerUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.SpinnerUI
- - javax.swing.plaf.basic.BasicSpinnerUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.SpinnerUI
- - javax.swing.plaf.basic.BasicSpinnerUI

javax.swing.plaf.SpinnerUI

- javax.swing.plaf.basic.BasicSpinnerUI

javax.swing.plaf.basic.BasicSpinnerUI

**Direct Known Subclasses:** SynthSpinnerUI

```java
public class
BasicSpinnerUI

extends
SpinnerUI
```

The default Spinner UI delegate.

**Since:** 1.4

public class

BasicSpinnerUI

extends

SpinnerUI

The default Spinner UI delegate.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

JSpinner

spinner

The spinner that we're a UI delegate for.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicSpinnerUI

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

protected

JComponent

createEditor

()

This method is called by installUI to get the editor component
of the

JSpinner

.

protected

LayoutManager

createLayout

()

Creates a

LayoutManager

that manages the

editor

,

nextButton

, and

previousButton

children of the JSpinner.

protected

Component

createNextButton

()

Creates an increment button, i.e. component that replaces the spinner
value with the object returned by

spinner.getNextValue

.

protected

Component

createPreviousButton

()

Creates a decrement button, i.e. component that replaces the spinner
value with the object returned by

spinner.getPreviousValue

.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a

PropertyChangeListener

that can be
added to the JSpinner itself.

static

ComponentUI

createUI

​(

JComponent

c)

Returns a new instance of BasicSpinnerUI.

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

protected void

installDefaults

()

Initialize the

JSpinner

border

,

foreground

, and

background

, properties
based on the corresponding "Spinner.*" properties from defaults table.

protected void

installKeyboardActions

()

Installs the keyboard Actions onto the JSpinner.

protected void

installListeners

()

Initializes

PropertyChangeListener

with
a shared object that delegates interesting PropertyChangeEvents
to protected methods.

protected void

installNextButtonListeners

​(

Component

c)

Installs the necessary listeners on the next button,

c

,
to update the

JSpinner

in response to a user gesture.

protected void

installPreviousButtonListeners

​(

Component

c)

Installs the necessary listeners on the previous button,

c

,
to update the

JSpinner

in response to a user gesture.

void

installUI

​(

JComponent

c)

Calls

installDefaults

,

installListeners

,
and then adds the components returned by

createNextButton

,

createPreviousButton

, and

createEditor

.

protected void

replaceEditor

​(

JComponent

oldEditor,

JComponent

newEditor)

Called by the

PropertyChangeListener

when the

JSpinner

editor property changes.

protected void

uninstallDefaults

()

Sets the

JSpinner's

layout manager to null.

protected void

uninstallListeners

()

Removes the

PropertyChangeListener

added
by installListeners.

void

uninstallUI

​(

JComponent

c)

Calls

uninstallDefaults

,

uninstallListeners

,
and then removes all of the spinners children.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

JSpinner

spinner

The spinner that we're a UI delegate for.

---

#### Field Summary

The spinner that we're a UI delegate for.

Constructor Summary

Constructors

Constructor

Description

BasicSpinnerUI

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

protected

JComponent

createEditor

()

This method is called by installUI to get the editor component
of the

JSpinner

.

protected

LayoutManager

createLayout

()

Creates a

LayoutManager

that manages the

editor

,

nextButton

, and

previousButton

children of the JSpinner.

protected

Component

createNextButton

()

Creates an increment button, i.e. component that replaces the spinner
value with the object returned by

spinner.getNextValue

.

protected

Component

createPreviousButton

()

Creates a decrement button, i.e. component that replaces the spinner
value with the object returned by

spinner.getPreviousValue

.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a

PropertyChangeListener

that can be
added to the JSpinner itself.

static

ComponentUI

createUI

​(

JComponent

c)

Returns a new instance of BasicSpinnerUI.

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

protected void

installDefaults

()

Initialize the

JSpinner

border

,

foreground

, and

background

, properties
based on the corresponding "Spinner.*" properties from defaults table.

protected void

installKeyboardActions

()

Installs the keyboard Actions onto the JSpinner.

protected void

installListeners

()

Initializes

PropertyChangeListener

with
a shared object that delegates interesting PropertyChangeEvents
to protected methods.

protected void

installNextButtonListeners

​(

Component

c)

Installs the necessary listeners on the next button,

c

,
to update the

JSpinner

in response to a user gesture.

protected void

installPreviousButtonListeners

​(

Component

c)

Installs the necessary listeners on the previous button,

c

,
to update the

JSpinner

in response to a user gesture.

void

installUI

​(

JComponent

c)

Calls

installDefaults

,

installListeners

,
and then adds the components returned by

createNextButton

,

createPreviousButton

, and

createEditor

.

protected void

replaceEditor

​(

JComponent

oldEditor,

JComponent

newEditor)

Called by the

PropertyChangeListener

when the

JSpinner

editor property changes.

protected void

uninstallDefaults

()

Sets the

JSpinner's

layout manager to null.

protected void

uninstallListeners

()

Removes the

PropertyChangeListener

added
by installListeners.

void

uninstallUI

​(

JComponent

c)

Calls

uninstallDefaults

,

uninstallListeners

,
and then removes all of the spinners children.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

This method is called by installUI to get the editor component
of the

JSpinner

.

Creates a

LayoutManager

that manages the

editor

,

nextButton

, and

previousButton

children of the JSpinner.

Creates an increment button, i.e. component that replaces the spinner
value with the object returned by

spinner.getNextValue

.

Creates a decrement button, i.e. component that replaces the spinner
value with the object returned by

spinner.getPreviousValue

.

Creates a

PropertyChangeListener

that can be
added to the JSpinner itself.

Returns a new instance of BasicSpinnerUI.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Initialize the

JSpinner

border

,

foreground

, and

background

, properties
based on the corresponding "Spinner.*" properties from defaults table.

Installs the keyboard Actions onto the JSpinner.

Initializes

PropertyChangeListener

with
a shared object that delegates interesting PropertyChangeEvents
to protected methods.

Installs the necessary listeners on the next button,

c

,
to update the

JSpinner

in response to a user gesture.

Installs the necessary listeners on the previous button,

c

,
to update the

JSpinner

in response to a user gesture.

Calls

installDefaults

,

installListeners

,
and then adds the components returned by

createNextButton

,

createPreviousButton

, and

createEditor

.

Called by the

PropertyChangeListener

when the

JSpinner

editor property changes.

Sets the

JSpinner's

layout manager to null.

Removes the

PropertyChangeListener

added
by installListeners.

Calls

uninstallDefaults

,

uninstallListeners

,
and then removes all of the spinners children.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

- spinner

```java
protected
JSpinner
spinner
```

The spinner that we're a UI delegate for. Initialized by
the

installUI

method, and reset to null
by

uninstallUI

.

**See Also:** installUI(javax.swing.JComponent)

,

uninstallUI(javax.swing.JComponent)

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicSpinnerUI

```java
public BasicSpinnerUI()
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

Returns a new instance of BasicSpinnerUI. SpinnerListUI
delegates are allocated one per JSpinner.

**Parameters:** c

- the JSpinner (not used)
**Returns:** a new BasicSpinnerUI object
**See Also:** ComponentUI.createUI(javax.swing.JComponent)

- installUI

```java
public void installUI​(
JComponent
c)
```

Calls

installDefaults

,

installListeners

,
and then adds the components returned by

createNextButton

,

createPreviousButton

, and

createEditor

.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the JSpinner
**See Also:** installDefaults()

,

installListeners()

,

createNextButton()

,

createPreviousButton()

,

createEditor()

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Calls

uninstallDefaults

,

uninstallListeners

,
and then removes all of the spinners children.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the JSpinner (not used)
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

- installListeners

```java
protected void installListeners()
```

Initializes

PropertyChangeListener

with
a shared object that delegates interesting PropertyChangeEvents
to protected methods.

This method is called by

installUI

.

**See Also:** replaceEditor(javax.swing.JComponent, javax.swing.JComponent)

,

uninstallListeners()

- uninstallListeners

```java
protected void uninstallListeners()
```

Removes the

PropertyChangeListener

added
by installListeners.

This method is called by

uninstallUI

.

**See Also:** installListeners()

- installDefaults

```java
protected void installDefaults()
```

Initialize the

JSpinner

border

,

foreground

, and

background

, properties
based on the corresponding "Spinner.*" properties from defaults table.
The

JSpinners

layout is set to the value returned by

createLayout

. This method is called by

installUI

.

**See Also:** uninstallDefaults()

,

installUI(javax.swing.JComponent)

,

createLayout()

,

LookAndFeel.installBorder(javax.swing.JComponent, java.lang.String)

,

LookAndFeel.installColors(javax.swing.JComponent, java.lang.String, java.lang.String)

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Sets the

JSpinner's

layout manager to null. This
method is called by

uninstallUI

.

**See Also:** installDefaults()

,

uninstallUI(javax.swing.JComponent)

- installNextButtonListeners

```java
protected void installNextButtonListeners​(
Component
c)
```

Installs the necessary listeners on the next button,

c

,
to update the

JSpinner

in response to a user gesture.

**Parameters:** c

- Component to install the listeners on
**Throws:** NullPointerException

- if

c

is null.
**Since:** 1.5
**See Also:** createNextButton()

- installPreviousButtonListeners

```java
protected void installPreviousButtonListeners​(
Component
c)
```

Installs the necessary listeners on the previous button,

c

,
to update the

JSpinner

in response to a user gesture.

**Parameters:** c

- Component to install the listeners on.
**Throws:** NullPointerException

- if

c

is null.
**Since:** 1.5
**See Also:** createPreviousButton()

- createLayout

```java
protected
LayoutManager
createLayout()
```

Creates a

LayoutManager

that manages the

editor

,

nextButton

, and

previousButton

children of the JSpinner. These three children must be
added with a constraint that identifies their role:
"Editor", "Next", and "Previous". The default layout manager
can handle the absence of any of these children.

**Returns:** a LayoutManager for the editor, next button, and previous button.
**See Also:** createNextButton()

,

createPreviousButton()

,

createEditor()

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a

PropertyChangeListener

that can be
added to the JSpinner itself. Typically, this listener
will call replaceEditor when the "editor" property changes,
since it's the

SpinnerUI's

responsibility to
add the editor to the JSpinner (and remove the old one).
This method is called by

installListeners

.

**Returns:** A PropertyChangeListener for the JSpinner itself
**See Also:** installListeners()

- createPreviousButton

```java
protected
Component
createPreviousButton()
```

Creates a decrement button, i.e. component that replaces the spinner
value with the object returned by

spinner.getPreviousValue

.
By default the

previousButton

is a

JButton

. If the
decrement button is not needed this method should return

null

.

**Returns:** a component that will replace the spinner's value with the
previous value in the sequence, or

null
**See Also:** installUI(javax.swing.JComponent)

,

createNextButton()

,

installPreviousButtonListeners(java.awt.Component)

- createNextButton

```java
protected
Component
createNextButton()
```

Creates an increment button, i.e. component that replaces the spinner
value with the object returned by

spinner.getNextValue

.
By default the

nextButton

is a

JButton

. If the
increment button is not needed this method should return

null

.

**Returns:** a component that will replace the spinner's value with the
next value in the sequence, or

null
**See Also:** installUI(javax.swing.JComponent)

,

createPreviousButton()

,

installNextButtonListeners(java.awt.Component)

- createEditor

```java
protected
JComponent
createEditor()
```

This method is called by installUI to get the editor component
of the

JSpinner

. By default it just returns

JSpinner.getEditor()

. Subclasses can override

createEditor

to return a component that contains
the spinner's editor or null, if they're going to handle adding
the editor to the

JSpinner

in an

installUI

override.

Typically this method would be overridden to wrap the editor
with a container with a custom border, since one can't assume
that the editors border can be set directly.

The

replaceEditor

method is called when the spinners
editor is changed with

JSpinner.setEditor

. If you've
overriden this method, then you'll probably want to override

replaceEditor

as well.

**Returns:** the JSpinners editor JComponent, spinner.getEditor() by default
**See Also:** installUI(javax.swing.JComponent)

,

replaceEditor(javax.swing.JComponent, javax.swing.JComponent)

,

JSpinner.getEditor()

- replaceEditor

```java
protected void replaceEditor​(
JComponent
oldEditor,

JComponent
newEditor)
```

Called by the

PropertyChangeListener

when the

JSpinner

editor property changes. It's the responsibility
of this method to remove the old editor and add the new one. By
default this operation is just:

```java
spinner.remove(oldEditor);
spinner.add(newEditor, "Editor");
```

The implementation of

replaceEditor

should be coordinated
with the

createEditor

method.

**Parameters:** oldEditor

- an old instance of editor
**Parameters:** newEditor

- a new instance of editor
**See Also:** createEditor()

,

createPropertyChangeListener()

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs the keyboard Actions onto the JSpinner.

**Since:** 1.5

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

Field Detail

- spinner

```java
protected
JSpinner
spinner
```

The spinner that we're a UI delegate for. Initialized by
the

installUI

method, and reset to null
by

uninstallUI

.

**See Also:** installUI(javax.swing.JComponent)

,

uninstallUI(javax.swing.JComponent)

---

#### Field Detail

spinner

```java
protected
JSpinner
spinner
```

The spinner that we're a UI delegate for. Initialized by
the

installUI

method, and reset to null
by

uninstallUI

.

**See Also:** installUI(javax.swing.JComponent)

,

uninstallUI(javax.swing.JComponent)

---

#### spinner

protected

JSpinner

spinner

The spinner that we're a UI delegate for. Initialized by
the

installUI

method, and reset to null
by

uninstallUI

.

Constructor Detail

- BasicSpinnerUI

```java
public BasicSpinnerUI()
```

---

#### Constructor Detail

BasicSpinnerUI

```java
public BasicSpinnerUI()
```

---

#### BasicSpinnerUI

public BasicSpinnerUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of BasicSpinnerUI. SpinnerListUI
delegates are allocated one per JSpinner.

**Parameters:** c

- the JSpinner (not used)
**Returns:** a new BasicSpinnerUI object
**See Also:** ComponentUI.createUI(javax.swing.JComponent)

- installUI

```java
public void installUI​(
JComponent
c)
```

Calls

installDefaults

,

installListeners

,
and then adds the components returned by

createNextButton

,

createPreviousButton

, and

createEditor

.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the JSpinner
**See Also:** installDefaults()

,

installListeners()

,

createNextButton()

,

createPreviousButton()

,

createEditor()

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Calls

uninstallDefaults

,

uninstallListeners

,
and then removes all of the spinners children.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the JSpinner (not used)
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

- installListeners

```java
protected void installListeners()
```

Initializes

PropertyChangeListener

with
a shared object that delegates interesting PropertyChangeEvents
to protected methods.

This method is called by

installUI

.

**See Also:** replaceEditor(javax.swing.JComponent, javax.swing.JComponent)

,

uninstallListeners()

- uninstallListeners

```java
protected void uninstallListeners()
```

Removes the

PropertyChangeListener

added
by installListeners.

This method is called by

uninstallUI

.

**See Also:** installListeners()

- installDefaults

```java
protected void installDefaults()
```

Initialize the

JSpinner

border

,

foreground

, and

background

, properties
based on the corresponding "Spinner.*" properties from defaults table.
The

JSpinners

layout is set to the value returned by

createLayout

. This method is called by

installUI

.

**See Also:** uninstallDefaults()

,

installUI(javax.swing.JComponent)

,

createLayout()

,

LookAndFeel.installBorder(javax.swing.JComponent, java.lang.String)

,

LookAndFeel.installColors(javax.swing.JComponent, java.lang.String, java.lang.String)

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Sets the

JSpinner's

layout manager to null. This
method is called by

uninstallUI

.

**See Also:** installDefaults()

,

uninstallUI(javax.swing.JComponent)

- installNextButtonListeners

```java
protected void installNextButtonListeners​(
Component
c)
```

Installs the necessary listeners on the next button,

c

,
to update the

JSpinner

in response to a user gesture.

**Parameters:** c

- Component to install the listeners on
**Throws:** NullPointerException

- if

c

is null.
**Since:** 1.5
**See Also:** createNextButton()

- installPreviousButtonListeners

```java
protected void installPreviousButtonListeners​(
Component
c)
```

Installs the necessary listeners on the previous button,

c

,
to update the

JSpinner

in response to a user gesture.

**Parameters:** c

- Component to install the listeners on.
**Throws:** NullPointerException

- if

c

is null.
**Since:** 1.5
**See Also:** createPreviousButton()

- createLayout

```java
protected
LayoutManager
createLayout()
```

Creates a

LayoutManager

that manages the

editor

,

nextButton

, and

previousButton

children of the JSpinner. These three children must be
added with a constraint that identifies their role:
"Editor", "Next", and "Previous". The default layout manager
can handle the absence of any of these children.

**Returns:** a LayoutManager for the editor, next button, and previous button.
**See Also:** createNextButton()

,

createPreviousButton()

,

createEditor()

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a

PropertyChangeListener

that can be
added to the JSpinner itself. Typically, this listener
will call replaceEditor when the "editor" property changes,
since it's the

SpinnerUI's

responsibility to
add the editor to the JSpinner (and remove the old one).
This method is called by

installListeners

.

**Returns:** A PropertyChangeListener for the JSpinner itself
**See Also:** installListeners()

- createPreviousButton

```java
protected
Component
createPreviousButton()
```

Creates a decrement button, i.e. component that replaces the spinner
value with the object returned by

spinner.getPreviousValue

.
By default the

previousButton

is a

JButton

. If the
decrement button is not needed this method should return

null

.

**Returns:** a component that will replace the spinner's value with the
previous value in the sequence, or

null
**See Also:** installUI(javax.swing.JComponent)

,

createNextButton()

,

installPreviousButtonListeners(java.awt.Component)

- createNextButton

```java
protected
Component
createNextButton()
```

Creates an increment button, i.e. component that replaces the spinner
value with the object returned by

spinner.getNextValue

.
By default the

nextButton

is a

JButton

. If the
increment button is not needed this method should return

null

.

**Returns:** a component that will replace the spinner's value with the
next value in the sequence, or

null
**See Also:** installUI(javax.swing.JComponent)

,

createPreviousButton()

,

installNextButtonListeners(java.awt.Component)

- createEditor

```java
protected
JComponent
createEditor()
```

This method is called by installUI to get the editor component
of the

JSpinner

. By default it just returns

JSpinner.getEditor()

. Subclasses can override

createEditor

to return a component that contains
the spinner's editor or null, if they're going to handle adding
the editor to the

JSpinner

in an

installUI

override.

Typically this method would be overridden to wrap the editor
with a container with a custom border, since one can't assume
that the editors border can be set directly.

The

replaceEditor

method is called when the spinners
editor is changed with

JSpinner.setEditor

. If you've
overriden this method, then you'll probably want to override

replaceEditor

as well.

**Returns:** the JSpinners editor JComponent, spinner.getEditor() by default
**See Also:** installUI(javax.swing.JComponent)

,

replaceEditor(javax.swing.JComponent, javax.swing.JComponent)

,

JSpinner.getEditor()

- replaceEditor

```java
protected void replaceEditor​(
JComponent
oldEditor,

JComponent
newEditor)
```

Called by the

PropertyChangeListener

when the

JSpinner

editor property changes. It's the responsibility
of this method to remove the old editor and add the new one. By
default this operation is just:

```java
spinner.remove(oldEditor);
spinner.add(newEditor, "Editor");
```

The implementation of

replaceEditor

should be coordinated
with the

createEditor

method.

**Parameters:** oldEditor

- an old instance of editor
**Parameters:** newEditor

- a new instance of editor
**See Also:** createEditor()

,

createPropertyChangeListener()

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs the keyboard Actions onto the JSpinner.

**Since:** 1.5

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

Returns a new instance of BasicSpinnerUI. SpinnerListUI
delegates are allocated one per JSpinner.

**Parameters:** c

- the JSpinner (not used)
**Returns:** a new BasicSpinnerUI object
**See Also:** ComponentUI.createUI(javax.swing.JComponent)

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Returns a new instance of BasicSpinnerUI. SpinnerListUI
delegates are allocated one per JSpinner.

installUI

```java
public void installUI​(
JComponent
c)
```

Calls

installDefaults

,

installListeners

,
and then adds the components returned by

createNextButton

,

createPreviousButton

, and

createEditor

.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the JSpinner
**See Also:** installDefaults()

,

installListeners()

,

createNextButton()

,

createPreviousButton()

,

createEditor()

---

#### installUI

public void installUI​(

JComponent

c)

Calls

installDefaults

,

installListeners

,
and then adds the components returned by

createNextButton

,

createPreviousButton

, and

createEditor

.

uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Calls

uninstallDefaults

,

uninstallListeners

,
and then removes all of the spinners children.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the JSpinner (not used)
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

---

#### uninstallUI

public void uninstallUI​(

JComponent

c)

Calls

uninstallDefaults

,

uninstallListeners

,
and then removes all of the spinners children.

installListeners

```java
protected void installListeners()
```

Initializes

PropertyChangeListener

with
a shared object that delegates interesting PropertyChangeEvents
to protected methods.

This method is called by

installUI

.

**See Also:** replaceEditor(javax.swing.JComponent, javax.swing.JComponent)

,

uninstallListeners()

---

#### installListeners

protected void installListeners()

Initializes

PropertyChangeListener

with
a shared object that delegates interesting PropertyChangeEvents
to protected methods.

This method is called by

installUI

.

This method is called by

installUI

.

uninstallListeners

```java
protected void uninstallListeners()
```

Removes the

PropertyChangeListener

added
by installListeners.

This method is called by

uninstallUI

.

**See Also:** installListeners()

---

#### uninstallListeners

protected void uninstallListeners()

Removes the

PropertyChangeListener

added
by installListeners.

This method is called by

uninstallUI

.

This method is called by

uninstallUI

.

installDefaults

```java
protected void installDefaults()
```

Initialize the

JSpinner

border

,

foreground

, and

background

, properties
based on the corresponding "Spinner.*" properties from defaults table.
The

JSpinners

layout is set to the value returned by

createLayout

. This method is called by

installUI

.

**See Also:** uninstallDefaults()

,

installUI(javax.swing.JComponent)

,

createLayout()

,

LookAndFeel.installBorder(javax.swing.JComponent, java.lang.String)

,

LookAndFeel.installColors(javax.swing.JComponent, java.lang.String, java.lang.String)

---

#### installDefaults

protected void installDefaults()

Initialize the

JSpinner

border

,

foreground

, and

background

, properties
based on the corresponding "Spinner.*" properties from defaults table.
The

JSpinners

layout is set to the value returned by

createLayout

. This method is called by

installUI

.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Sets the

JSpinner's

layout manager to null. This
method is called by

uninstallUI

.

**See Also:** installDefaults()

,

uninstallUI(javax.swing.JComponent)

---

#### uninstallDefaults

protected void uninstallDefaults()

Sets the

JSpinner's

layout manager to null. This
method is called by

uninstallUI

.

installNextButtonListeners

```java
protected void installNextButtonListeners​(
Component
c)
```

Installs the necessary listeners on the next button,

c

,
to update the

JSpinner

in response to a user gesture.

**Parameters:** c

- Component to install the listeners on
**Throws:** NullPointerException

- if

c

is null.
**Since:** 1.5
**See Also:** createNextButton()

---

#### installNextButtonListeners

protected void installNextButtonListeners​(

Component

c)

Installs the necessary listeners on the next button,

c

,
to update the

JSpinner

in response to a user gesture.

installPreviousButtonListeners

```java
protected void installPreviousButtonListeners​(
Component
c)
```

Installs the necessary listeners on the previous button,

c

,
to update the

JSpinner

in response to a user gesture.

**Parameters:** c

- Component to install the listeners on.
**Throws:** NullPointerException

- if

c

is null.
**Since:** 1.5
**See Also:** createPreviousButton()

---

#### installPreviousButtonListeners

protected void installPreviousButtonListeners​(

Component

c)

Installs the necessary listeners on the previous button,

c

,
to update the

JSpinner

in response to a user gesture.

createLayout

```java
protected
LayoutManager
createLayout()
```

Creates a

LayoutManager

that manages the

editor

,

nextButton

, and

previousButton

children of the JSpinner. These three children must be
added with a constraint that identifies their role:
"Editor", "Next", and "Previous". The default layout manager
can handle the absence of any of these children.

**Returns:** a LayoutManager for the editor, next button, and previous button.
**See Also:** createNextButton()

,

createPreviousButton()

,

createEditor()

---

#### createLayout

protected

LayoutManager

createLayout()

Creates a

LayoutManager

that manages the

editor

,

nextButton

, and

previousButton

children of the JSpinner. These three children must be
added with a constraint that identifies their role:
"Editor", "Next", and "Previous". The default layout manager
can handle the absence of any of these children.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a

PropertyChangeListener

that can be
added to the JSpinner itself. Typically, this listener
will call replaceEditor when the "editor" property changes,
since it's the

SpinnerUI's

responsibility to
add the editor to the JSpinner (and remove the old one).
This method is called by

installListeners

.

**Returns:** A PropertyChangeListener for the JSpinner itself
**See Also:** installListeners()

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener()

Creates a

PropertyChangeListener

that can be
added to the JSpinner itself. Typically, this listener
will call replaceEditor when the "editor" property changes,
since it's the

SpinnerUI's

responsibility to
add the editor to the JSpinner (and remove the old one).
This method is called by

installListeners

.

createPreviousButton

```java
protected
Component
createPreviousButton()
```

Creates a decrement button, i.e. component that replaces the spinner
value with the object returned by

spinner.getPreviousValue

.
By default the

previousButton

is a

JButton

. If the
decrement button is not needed this method should return

null

.

**Returns:** a component that will replace the spinner's value with the
previous value in the sequence, or

null
**See Also:** installUI(javax.swing.JComponent)

,

createNextButton()

,

installPreviousButtonListeners(java.awt.Component)

---

#### createPreviousButton

protected

Component

createPreviousButton()

Creates a decrement button, i.e. component that replaces the spinner
value with the object returned by

spinner.getPreviousValue

.
By default the

previousButton

is a

JButton

. If the
decrement button is not needed this method should return

null

.

createNextButton

```java
protected
Component
createNextButton()
```

Creates an increment button, i.e. component that replaces the spinner
value with the object returned by

spinner.getNextValue

.
By default the

nextButton

is a

JButton

. If the
increment button is not needed this method should return

null

.

**Returns:** a component that will replace the spinner's value with the
next value in the sequence, or

null
**See Also:** installUI(javax.swing.JComponent)

,

createPreviousButton()

,

installNextButtonListeners(java.awt.Component)

---

#### createNextButton

protected

Component

createNextButton()

Creates an increment button, i.e. component that replaces the spinner
value with the object returned by

spinner.getNextValue

.
By default the

nextButton

is a

JButton

. If the
increment button is not needed this method should return

null

.

createEditor

```java
protected
JComponent
createEditor()
```

This method is called by installUI to get the editor component
of the

JSpinner

. By default it just returns

JSpinner.getEditor()

. Subclasses can override

createEditor

to return a component that contains
the spinner's editor or null, if they're going to handle adding
the editor to the

JSpinner

in an

installUI

override.

Typically this method would be overridden to wrap the editor
with a container with a custom border, since one can't assume
that the editors border can be set directly.

The

replaceEditor

method is called when the spinners
editor is changed with

JSpinner.setEditor

. If you've
overriden this method, then you'll probably want to override

replaceEditor

as well.

**Returns:** the JSpinners editor JComponent, spinner.getEditor() by default
**See Also:** installUI(javax.swing.JComponent)

,

replaceEditor(javax.swing.JComponent, javax.swing.JComponent)

,

JSpinner.getEditor()

---

#### createEditor

protected

JComponent

createEditor()

This method is called by installUI to get the editor component
of the

JSpinner

. By default it just returns

JSpinner.getEditor()

. Subclasses can override

createEditor

to return a component that contains
the spinner's editor or null, if they're going to handle adding
the editor to the

JSpinner

in an

installUI

override.

Typically this method would be overridden to wrap the editor
with a container with a custom border, since one can't assume
that the editors border can be set directly.

The

replaceEditor

method is called when the spinners
editor is changed with

JSpinner.setEditor

. If you've
overriden this method, then you'll probably want to override

replaceEditor

as well.

Typically this method would be overridden to wrap the editor
with a container with a custom border, since one can't assume
that the editors border can be set directly.

The

replaceEditor

method is called when the spinners
editor is changed with

JSpinner.setEditor

. If you've
overriden this method, then you'll probably want to override

replaceEditor

as well.

The

replaceEditor

method is called when the spinners
editor is changed with

JSpinner.setEditor

. If you've
overriden this method, then you'll probably want to override

replaceEditor

as well.

replaceEditor

```java
protected void replaceEditor​(
JComponent
oldEditor,

JComponent
newEditor)
```

Called by the

PropertyChangeListener

when the

JSpinner

editor property changes. It's the responsibility
of this method to remove the old editor and add the new one. By
default this operation is just:

```java
spinner.remove(oldEditor);
spinner.add(newEditor, "Editor");
```

The implementation of

replaceEditor

should be coordinated
with the

createEditor

method.

**Parameters:** oldEditor

- an old instance of editor
**Parameters:** newEditor

- a new instance of editor
**See Also:** createEditor()

,

createPropertyChangeListener()

---

#### replaceEditor

protected void replaceEditor​(

JComponent

oldEditor,

JComponent

newEditor)

Called by the

PropertyChangeListener

when the

JSpinner

editor property changes. It's the responsibility
of this method to remove the old editor and add the new one. By
default this operation is just:

```java
spinner.remove(oldEditor);
spinner.add(newEditor, "Editor");
```

The implementation of

replaceEditor

should be coordinated
with the

createEditor

method.

spinner.remove(oldEditor);
spinner.add(newEditor, "Editor");

installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs the keyboard Actions onto the JSpinner.

**Since:** 1.5

---

#### installKeyboardActions

protected void installKeyboardActions()

Installs the keyboard Actions onto the JSpinner.

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

