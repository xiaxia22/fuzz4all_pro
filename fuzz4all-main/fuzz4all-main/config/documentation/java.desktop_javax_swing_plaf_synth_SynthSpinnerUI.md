# Class SynthSpinnerUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthSpinnerUI.html`

### Class Description

```java
public class
SynthSpinnerUI

extends
BasicSpinnerUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JSpinner

.

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthSpinnerUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Returns a new instance of SynthSpinnerUI.

**Parameters:**
- c

- the JSpinner (not used)

**Returns:**
- a new SynthSpinnerUI object

**See Also:**
- ComponentUI.createUI(javax.swing.JComponent)

---

#### protected void installDefaults()

Initializes the

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

**Overrides:**
- installDefaults

in class

BasicSpinnerUI

**See Also:**
- uninstallDefaults()

,

BasicSpinnerUI.installUI(javax.swing.JComponent)

,

BasicSpinnerUI.createLayout()

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

**Overrides:**
- uninstallDefaults

in class

BasicSpinnerUI

**See Also:**
- installDefaults()

,

BasicSpinnerUI.uninstallUI(javax.swing.JComponent)

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

**Overrides:**
- createEditor

in class

BasicSpinnerUI

**Returns:**
- the JSpinners editor JComponent, spinner.getEditor() by default

**See Also:**
- BasicSpinnerUI.installUI(javax.swing.JComponent)

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

**Overrides:**
- replaceEditor

in class

BasicSpinnerUI

**Parameters:**
- oldEditor

- an old instance of editor
- newEditor

- a new instance of editor

**See Also:**
- createEditor()

,

BasicSpinnerUI.createPropertyChangeListener()

---

#### public void update​(
Graphics
g,

JComponent
c)

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:**
- update

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

object used for painting
- c

- the component being painted

**See Also:**
- paint(SynthContext,Graphics)

---

#### public void paint​(
Graphics
g,

JComponent
c)

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:**
- paint

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

object used for painting
- c

- the component being painted

**See Also:**
- paint(SynthContext,Graphics)

---

#### protected void paint​(
SynthContext
context,

Graphics
g)

Paints the specified component. This implementation does nothing.

**Parameters:**
- context

- context for the component being painted
- g

- the

Graphics

object used for painting

**See Also:**
- update(Graphics,JComponent)

---

### Additional Sections

#### Class SynthSpinnerUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.SpinnerUI
- - javax.swing.plaf.basic.BasicSpinnerUI
- - javax.swing.plaf.synth.SynthSpinnerUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.SpinnerUI
- - javax.swing.plaf.basic.BasicSpinnerUI
- - javax.swing.plaf.synth.SynthSpinnerUI

javax.swing.plaf.SpinnerUI

- javax.swing.plaf.basic.BasicSpinnerUI
- - javax.swing.plaf.synth.SynthSpinnerUI

javax.swing.plaf.basic.BasicSpinnerUI

- javax.swing.plaf.synth.SynthSpinnerUI

javax.swing.plaf.synth.SynthSpinnerUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

```java
public class
SynthSpinnerUI

extends
BasicSpinnerUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JSpinner

.

**Since:** 1.7

public class

SynthSpinnerUI

extends

BasicSpinnerUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JSpinner

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicSpinnerUI

spinner

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

SynthSpinnerUI

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

static

ComponentUI

createUI

​(

JComponent

c)

Returns a new instance of SynthSpinnerUI.

protected void

installDefaults

()

Initializes the

JSpinner

border

,

foreground

, and

background

, properties
based on the corresponding "Spinner.*" properties from defaults table.

void

paint

​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the specified component.

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

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicSpinnerUI

createLayout

,

createNextButton

,

createPreviousButton

,

createPropertyChangeListener

,

getBaseline

,

getBaselineResizeBehavior

,

installKeyboardActions

,

installListeners

,

installNextButtonListeners

,

installPreviousButtonListeners

,

installUI

,

uninstallListeners

,

uninstallUI

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

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicSpinnerUI

spinner

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

Fields declared in class javax.swing.plaf.basic.

BasicSpinnerUI

spinner

---

#### Fields declared in class javax.swing.plaf.basic. BasicSpinnerUI

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

SynthSpinnerUI

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

static

ComponentUI

createUI

​(

JComponent

c)

Returns a new instance of SynthSpinnerUI.

protected void

installDefaults

()

Initializes the

JSpinner

border

,

foreground

, and

background

, properties
based on the corresponding "Spinner.*" properties from defaults table.

void

paint

​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the specified component.

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

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicSpinnerUI

createLayout

,

createNextButton

,

createPreviousButton

,

createPropertyChangeListener

,

getBaseline

,

getBaselineResizeBehavior

,

installKeyboardActions

,

installListeners

,

installNextButtonListeners

,

installPreviousButtonListeners

,

installUI

,

uninstallListeners

,

uninstallUI

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

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Method Summary

This method is called by installUI to get the editor component
of the

JSpinner

.

Returns a new instance of SynthSpinnerUI.

Initializes the

JSpinner

border

,

foreground

, and

background

, properties
based on the corresponding "Spinner.*" properties from defaults table.

Paints the specified component according to the Look and Feel.

Paints the specified component.

Called by the

PropertyChangeListener

when the

JSpinner

editor property changes.

Sets the

JSpinner's

layout manager to null.

Notifies this UI delegate to repaint the specified component.

Methods declared in class javax.swing.plaf.basic.

BasicSpinnerUI

createLayout

,

createNextButton

,

createPreviousButton

,

createPropertyChangeListener

,

getBaseline

,

getBaselineResizeBehavior

,

installKeyboardActions

,

installListeners

,

installNextButtonListeners

,

installPreviousButtonListeners

,

installUI

,

uninstallListeners

,

uninstallUI

---

#### Methods declared in class javax.swing.plaf.basic. BasicSpinnerUI

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

Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Methods declared in interface java.beans. PropertyChangeListener

Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Methods declared in interface javax.swing.plaf.synth. SynthUI

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SynthSpinnerUI

```java
public SynthSpinnerUI()
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

Returns a new instance of SynthSpinnerUI.

**Parameters:** c

- the JSpinner (not used)
**Returns:** a new SynthSpinnerUI object
**See Also:** ComponentUI.createUI(javax.swing.JComponent)

- installDefaults

```java
protected void installDefaults()
```

Initializes the

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

**Overrides:** installDefaults

in class

BasicSpinnerUI
**See Also:** uninstallDefaults()

,

BasicSpinnerUI.installUI(javax.swing.JComponent)

,

BasicSpinnerUI.createLayout()

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

**Overrides:** uninstallDefaults

in class

BasicSpinnerUI
**See Also:** installDefaults()

,

BasicSpinnerUI.uninstallUI(javax.swing.JComponent)

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

**Overrides:** createEditor

in class

BasicSpinnerUI
**Returns:** the JSpinners editor JComponent, spinner.getEditor() by default
**See Also:** BasicSpinnerUI.installUI(javax.swing.JComponent)

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

**Overrides:** replaceEditor

in class

BasicSpinnerUI
**Parameters:** oldEditor

- an old instance of editor
**Parameters:** newEditor

- a new instance of editor
**See Also:** createEditor()

,

BasicSpinnerUI.createPropertyChangeListener()

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component. This implementation does nothing.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

Constructor Detail

- SynthSpinnerUI

```java
public SynthSpinnerUI()
```

---

#### Constructor Detail

SynthSpinnerUI

```java
public SynthSpinnerUI()
```

---

#### SynthSpinnerUI

public SynthSpinnerUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of SynthSpinnerUI.

**Parameters:** c

- the JSpinner (not used)
**Returns:** a new SynthSpinnerUI object
**See Also:** ComponentUI.createUI(javax.swing.JComponent)

- installDefaults

```java
protected void installDefaults()
```

Initializes the

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

**Overrides:** installDefaults

in class

BasicSpinnerUI
**See Also:** uninstallDefaults()

,

BasicSpinnerUI.installUI(javax.swing.JComponent)

,

BasicSpinnerUI.createLayout()

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

**Overrides:** uninstallDefaults

in class

BasicSpinnerUI
**See Also:** installDefaults()

,

BasicSpinnerUI.uninstallUI(javax.swing.JComponent)

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

**Overrides:** createEditor

in class

BasicSpinnerUI
**Returns:** the JSpinners editor JComponent, spinner.getEditor() by default
**See Also:** BasicSpinnerUI.installUI(javax.swing.JComponent)

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

**Overrides:** replaceEditor

in class

BasicSpinnerUI
**Parameters:** oldEditor

- an old instance of editor
**Parameters:** newEditor

- a new instance of editor
**See Also:** createEditor()

,

BasicSpinnerUI.createPropertyChangeListener()

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component. This implementation does nothing.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

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

Returns a new instance of SynthSpinnerUI.

**Parameters:** c

- the JSpinner (not used)
**Returns:** a new SynthSpinnerUI object
**See Also:** ComponentUI.createUI(javax.swing.JComponent)

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Returns a new instance of SynthSpinnerUI.

installDefaults

```java
protected void installDefaults()
```

Initializes the

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

**Overrides:** installDefaults

in class

BasicSpinnerUI
**See Also:** uninstallDefaults()

,

BasicSpinnerUI.installUI(javax.swing.JComponent)

,

BasicSpinnerUI.createLayout()

,

LookAndFeel.installBorder(javax.swing.JComponent, java.lang.String)

,

LookAndFeel.installColors(javax.swing.JComponent, java.lang.String, java.lang.String)

---

#### installDefaults

protected void installDefaults()

Initializes the

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

**Overrides:** uninstallDefaults

in class

BasicSpinnerUI
**See Also:** installDefaults()

,

BasicSpinnerUI.uninstallUI(javax.swing.JComponent)

---

#### uninstallDefaults

protected void uninstallDefaults()

Sets the

JSpinner's

layout manager to null. This
method is called by

uninstallUI

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

**Overrides:** createEditor

in class

BasicSpinnerUI
**Returns:** the JSpinners editor JComponent, spinner.getEditor() by default
**See Also:** BasicSpinnerUI.installUI(javax.swing.JComponent)

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

**Overrides:** replaceEditor

in class

BasicSpinnerUI
**Parameters:** oldEditor

- an old instance of editor
**Parameters:** newEditor

- a new instance of editor
**See Also:** createEditor()

,

BasicSpinnerUI.createPropertyChangeListener()

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

update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

---

#### update

public void update​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

---

#### paint

public void paint​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component. This implementation does nothing.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

---

#### paint

protected void paint​(

SynthContext

context,

Graphics

g)

Paints the specified component. This implementation does nothing.

---

