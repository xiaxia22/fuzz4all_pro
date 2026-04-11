# Class BasicInternalFrameUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicInternalFrameUI.html`

### Class Description

```java
public class
BasicInternalFrameUI

extends
InternalFrameUI
```

A basic L&F implementation of JInternalFrame.

**Direct Known Subclasses:** MetalInternalFrameUI

,

SynthInternalFrameUI

---

### Field Details

#### protected
JInternalFrame
frame

frame

---

#### protected
MouseInputAdapter
borderListener

Border listener

---

#### protected
PropertyChangeListener
propertyChangeListener

Property change listener

---

#### protected
LayoutManager
internalFrameLayout

Internal frame layout

---

#### protected
ComponentListener
componentListener

Component listener

---

#### protected
MouseInputListener
glassPaneDispatcher

Glass pane dispatcher

---

#### protected
JComponent
northPane

North pane

---

#### protected
JComponent
southPane

South pane

---

#### protected
JComponent
westPane

West pane

---

#### protected
JComponent
eastPane

East pane

---

#### protected
BasicInternalFrameTitlePane
titlePane

Title pane

---

#### @Deprecated

protected
KeyStroke
openMenuKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

### Constructor Details

#### public BasicInternalFrameUI​(
JInternalFrame
b)

Constructs a

BasicInternalFrameUI

.

**Parameters:**
- b

- the internal frame

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
b)

Returns a component UI.

**Parameters:**
- b

- a component

**Returns:**
- a component UI

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

#### protected void installDefaults()

Installs the defaults.

---

#### protected void installKeyboardActions()

Installs the keyboard actions.

---

#### protected void installComponents()

Installs the components.

---

#### protected void installListeners()

Installs the listeners.

**Since:**
- 1.3

---

#### protected void uninstallDefaults()

Uninstalls the defaults.

---

#### protected void uninstallComponents()

Uninstalls the components.

---

#### protected void uninstallListeners()

Uninstalls the listeners.

**Since:**
- 1.3

---

#### protected void uninstallKeyboardActions()

Uninstalls the keyboard actions.

---

#### protected
LayoutManager
createLayoutManager()

Creates the layout manager.

**Returns:**
- the layout manager

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Creates the property change listener.

**Returns:**
- the property change listener

---

#### public
Dimension
getPreferredSize​(
JComponent
x)

Returns the preferred size.

**Overrides:**
- getPreferredSize

in class

ComponentUI

**Parameters:**
- x

- the component

**Returns:**
- the preferred size

**See Also:**
- JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### public
Dimension
getMinimumSize​(
JComponent
x)

Returns the minimum size.

**Overrides:**
- getMinimumSize

in class

ComponentUI

**Parameters:**
- x

- the component

**Returns:**
- the minimum size

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
x)

Returns the maximum size.

**Overrides:**
- getMaximumSize

in class

ComponentUI

**Parameters:**
- x

- the component

**Returns:**
- the maximum size

**See Also:**
- JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### protected void replacePane​(
JComponent
currentPane,

JComponent
newPane)

Installs necessary mouse handlers on

newPane

and adds it to the frame.
Reverse process for the

currentPane

.

**Parameters:**
- currentPane

- this

Jcomponent

is the current pane being
viewed that has mouse handlers installed
- newPane

- this

Jcomponent

is the pane which will be added
and have mouse handlers installed

---

#### protected void deinstallMouseHandlers​(
JComponent
c)

Deinstalls the mouse handlers.

**Parameters:**
- c

- the component

---

#### protected void installMouseHandlers​(
JComponent
c)

Installs the mouse handlers.

**Parameters:**
- c

- the component

---

#### protected
JComponent
createNorthPane​(
JInternalFrame
w)

Creates the north pane.

**Parameters:**
- w

- the internal frame

**Returns:**
- the north pane

---

#### protected
JComponent
createSouthPane​(
JInternalFrame
w)

Creates the north pane.

**Parameters:**
- w

- the internal frame

**Returns:**
- the north pane

---

#### protected
JComponent
createWestPane​(
JInternalFrame
w)

Creates the west pane.

**Parameters:**
- w

- the internal frame

**Returns:**
- the west pane

---

#### protected
JComponent
createEastPane​(
JInternalFrame
w)

Creates the east pane.

**Parameters:**
- w

- the internal frame

**Returns:**
- the east pane

---

#### protected
MouseInputAdapter
createBorderListener​(
JInternalFrame
w)

Creates the border listener.

**Parameters:**
- w

- the internal frame

**Returns:**
- the border listener

---

#### protected void createInternalFrameListener()

Creates the internal frame listener.

---

#### protected final boolean isKeyBindingRegistered()

Returns whether or no the key binding is registered.

**Returns:**
- whether or no the key binding is registered

---

#### protected final void setKeyBindingRegistered​(boolean b)

Sets the key binding registration.

**Parameters:**
- b

- new value for key binding registration

---

#### public final boolean isKeyBindingActive()

Returns whether or no the key binding is active.

**Returns:**
- whether or no the key binding is active

---

#### protected final void setKeyBindingActive​(boolean b)

Sets the key binding activity.

**Parameters:**
- b

- new value for key binding activity

---

#### protected void setupMenuOpenKey()

Setup the menu open key.

---

#### protected void setupMenuCloseKey()

Setup the menu close key.

---

#### public
JComponent
getNorthPane()

Returns the north pane.

**Returns:**
- the north pane

---

#### public void setNorthPane​(
JComponent
c)

Sets the north pane.

**Parameters:**
- c

- the new north pane

---

#### public
JComponent
getSouthPane()

Returns the south pane.

**Returns:**
- the south pane

---

#### public void setSouthPane​(
JComponent
c)

Sets the south pane.

**Parameters:**
- c

- the new south pane

---

#### public
JComponent
getWestPane()

Returns the west pane.

**Returns:**
- the west pane

---

#### public void setWestPane​(
JComponent
c)

Sets the west pane.

**Parameters:**
- c

- the new west pane

---

#### public
JComponent
getEastPane()

Returns the east pane.

**Returns:**
- the east pane

---

#### public void setEastPane​(
JComponent
c)

Sets the east pane.

**Parameters:**
- c

- the new east pane

---

#### protected
DesktopManager
getDesktopManager()

Returns the proper DesktopManager. Calls getDesktopPane() to
find the JDesktop component and returns the desktopManager from
it. If this fails, it will return a default DesktopManager that
should work in arbitrary parents.

**Returns:**
- the proper DesktopManager

---

#### protected
DesktopManager
createDesktopManager()

Creates the desktop manager.

**Returns:**
- the desktop manager

---

#### protected void closeFrame​(
JInternalFrame
f)

This method is called when the user wants to close the frame.
The

playCloseSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:**
- f

- the

JInternalFrame

being viewed

---

#### protected void maximizeFrame​(
JInternalFrame
f)

This method is called when the user wants to maximize the frame.
The

playMaximizeSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:**
- f

- the

JInternalFrame

being viewed

---

#### protected void minimizeFrame​(
JInternalFrame
f)

This method is called when the user wants to minimize the frame.
The

playRestoreDownSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:**
- f

- the

JInternalFrame

being viewed

---

#### protected void iconifyFrame​(
JInternalFrame
f)

This method is called when the user wants to iconify the frame.
The

playMinimizeSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:**
- f

- the

JInternalFrame

being viewed

---

#### protected void deiconifyFrame​(
JInternalFrame
f)

This method is called when the user wants to deiconify the frame.
The

playRestoreUpSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:**
- f

- the

JInternalFrame

being viewed

---

#### protected void activateFrame​(
JInternalFrame
f)

This method is called when the frame becomes selected.
This action is delegated to the desktopManager.

**Parameters:**
- f

- the

JInternalFrame

being viewed

---

#### protected void deactivateFrame​(
JInternalFrame
f)

This method is called when the frame is no longer selected.
This action is delegated to the desktopManager.

**Parameters:**
- f

- the

JInternalFrame

being viewed

---

#### protected
ComponentListener
createComponentListener()

Creates a component listener.

**Returns:**
- a component listener

---

#### protected
MouseInputListener
createGlassPaneDispatcher()

Creates a

GlassPaneDispatcher

.

**Returns:**
- a

GlassPaneDispatcher

---

### Additional Sections

#### Class BasicInternalFrameUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.InternalFrameUI
- - javax.swing.plaf.basic.BasicInternalFrameUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.InternalFrameUI
- - javax.swing.plaf.basic.BasicInternalFrameUI

javax.swing.plaf.InternalFrameUI

- javax.swing.plaf.basic.BasicInternalFrameUI

javax.swing.plaf.basic.BasicInternalFrameUI

**Direct Known Subclasses:** MetalInternalFrameUI

,

SynthInternalFrameUI

```java
public class
BasicInternalFrameUI

extends
InternalFrameUI
```

A basic L&F implementation of JInternalFrame.

public class

BasicInternalFrameUI

extends

InternalFrameUI

A basic L&F implementation of JInternalFrame.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

BasicInternalFrameUI.BasicInternalFrameListener

Basic internal frame listener.

protected class

BasicInternalFrameUI.BorderListener

Listens for border adjustments.

protected class

BasicInternalFrameUI.ComponentHandler

Component handler.

protected class

BasicInternalFrameUI.GlassPaneDispatcher

Glass pane dispatcher.

class

BasicInternalFrameUI.InternalFrameLayout

Internal frame layout.

class

BasicInternalFrameUI.InternalFramePropertyChangeListener

Internal frame property change listener.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

MouseInputAdapter

borderListener

Border listener

protected

ComponentListener

componentListener

Component listener

protected

JComponent

eastPane

East pane

protected

JInternalFrame

frame

frame

protected

MouseInputListener

glassPaneDispatcher

Glass pane dispatcher

protected

LayoutManager

internalFrameLayout

Internal frame layout

protected

JComponent

northPane

North pane

protected

KeyStroke

openMenuKey

Deprecated.

As of Java 2 platform v1.3.

protected

PropertyChangeListener

propertyChangeListener

Property change listener

protected

JComponent

southPane

South pane

protected

BasicInternalFrameTitlePane

titlePane

Title pane

protected

JComponent

westPane

West pane

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicInternalFrameUI

​(

JInternalFrame

b)

Constructs a

BasicInternalFrameUI

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

activateFrame

​(

JInternalFrame

f)

This method is called when the frame becomes selected.

protected void

closeFrame

​(

JInternalFrame

f)

This method is called when the user wants to close the frame.

protected

MouseInputAdapter

createBorderListener

​(

JInternalFrame

w)

Creates the border listener.

protected

ComponentListener

createComponentListener

()

Creates a component listener.

protected

DesktopManager

createDesktopManager

()

Creates the desktop manager.

protected

JComponent

createEastPane

​(

JInternalFrame

w)

Creates the east pane.

protected

MouseInputListener

createGlassPaneDispatcher

()

Creates a

GlassPaneDispatcher

.

protected void

createInternalFrameListener

()

Creates the internal frame listener.

protected

LayoutManager

createLayoutManager

()

Creates the layout manager.

protected

JComponent

createNorthPane

​(

JInternalFrame

w)

Creates the north pane.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates the property change listener.

protected

JComponent

createSouthPane

​(

JInternalFrame

w)

Creates the north pane.

static

ComponentUI

createUI

​(

JComponent

b)

Returns a component UI.

protected

JComponent

createWestPane

​(

JInternalFrame

w)

Creates the west pane.

protected void

deactivateFrame

​(

JInternalFrame

f)

This method is called when the frame is no longer selected.

protected void

deiconifyFrame

​(

JInternalFrame

f)

This method is called when the user wants to deiconify the frame.

protected void

deinstallMouseHandlers

​(

JComponent

c)

Deinstalls the mouse handlers.

protected

DesktopManager

getDesktopManager

()

Returns the proper DesktopManager.

JComponent

getEastPane

()

Returns the east pane.

Dimension

getMaximumSize

​(

JComponent

x)

Returns the maximum size.

Dimension

getMinimumSize

​(

JComponent

x)

Returns the minimum size.

JComponent

getNorthPane

()

Returns the north pane.

Dimension

getPreferredSize

​(

JComponent

x)

Returns the preferred size.

JComponent

getSouthPane

()

Returns the south pane.

JComponent

getWestPane

()

Returns the west pane.

protected void

iconifyFrame

​(

JInternalFrame

f)

This method is called when the user wants to iconify the frame.

protected void

installComponents

()

Installs the components.

protected void

installDefaults

()

Installs the defaults.

protected void

installKeyboardActions

()

Installs the keyboard actions.

protected void

installListeners

()

Installs the listeners.

protected void

installMouseHandlers

​(

JComponent

c)

Installs the mouse handlers.

void

installUI

​(

JComponent

c)

Installs the UI.

boolean

isKeyBindingActive

()

Returns whether or no the key binding is active.

protected boolean

isKeyBindingRegistered

()

Returns whether or no the key binding is registered.

protected void

maximizeFrame

​(

JInternalFrame

f)

This method is called when the user wants to maximize the frame.

protected void

minimizeFrame

​(

JInternalFrame

f)

This method is called when the user wants to minimize the frame.

protected void

replacePane

​(

JComponent

currentPane,

JComponent

newPane)

Installs necessary mouse handlers on

newPane

and adds it to the frame.

void

setEastPane

​(

JComponent

c)

Sets the east pane.

protected void

setKeyBindingActive

​(boolean b)

Sets the key binding activity.

protected void

setKeyBindingRegistered

​(boolean b)

Sets the key binding registration.

void

setNorthPane

​(

JComponent

c)

Sets the north pane.

void

setSouthPane

​(

JComponent

c)

Sets the south pane.

protected void

setupMenuCloseKey

()

Setup the menu close key.

protected void

setupMenuOpenKey

()

Setup the menu open key.

void

setWestPane

​(

JComponent

c)

Sets the west pane.

protected void

uninstallComponents

()

Uninstalls the components.

protected void

uninstallDefaults

()

Uninstalls the defaults.

protected void

uninstallKeyboardActions

()

Uninstalls the keyboard actions.

protected void

uninstallListeners

()

Uninstalls the listeners.

void

uninstallUI

​(

JComponent

c)

Uninstalls the UI.

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

BasicInternalFrameUI.BasicInternalFrameListener

Basic internal frame listener.

protected class

BasicInternalFrameUI.BorderListener

Listens for border adjustments.

protected class

BasicInternalFrameUI.ComponentHandler

Component handler.

protected class

BasicInternalFrameUI.GlassPaneDispatcher

Glass pane dispatcher.

class

BasicInternalFrameUI.InternalFrameLayout

Internal frame layout.

class

BasicInternalFrameUI.InternalFramePropertyChangeListener

Internal frame property change listener.

---

#### Nested Class Summary

Basic internal frame listener.

Listens for border adjustments.

Component handler.

Glass pane dispatcher.

Internal frame layout.

Internal frame property change listener.

Field Summary

Fields

Modifier and Type

Field

Description

protected

MouseInputAdapter

borderListener

Border listener

protected

ComponentListener

componentListener

Component listener

protected

JComponent

eastPane

East pane

protected

JInternalFrame

frame

frame

protected

MouseInputListener

glassPaneDispatcher

Glass pane dispatcher

protected

LayoutManager

internalFrameLayout

Internal frame layout

protected

JComponent

northPane

North pane

protected

KeyStroke

openMenuKey

Deprecated.

As of Java 2 platform v1.3.

protected

PropertyChangeListener

propertyChangeListener

Property change listener

protected

JComponent

southPane

South pane

protected

BasicInternalFrameTitlePane

titlePane

Title pane

protected

JComponent

westPane

West pane

---

#### Field Summary

Border listener

Component listener

East pane

frame

Glass pane dispatcher

Internal frame layout

North pane

Deprecated.

As of Java 2 platform v1.3.

Property change listener

South pane

Title pane

West pane

Constructor Summary

Constructors

Constructor

Description

BasicInternalFrameUI

​(

JInternalFrame

b)

Constructs a

BasicInternalFrameUI

.

---

#### Constructor Summary

Constructs a

BasicInternalFrameUI

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

activateFrame

​(

JInternalFrame

f)

This method is called when the frame becomes selected.

protected void

closeFrame

​(

JInternalFrame

f)

This method is called when the user wants to close the frame.

protected

MouseInputAdapter

createBorderListener

​(

JInternalFrame

w)

Creates the border listener.

protected

ComponentListener

createComponentListener

()

Creates a component listener.

protected

DesktopManager

createDesktopManager

()

Creates the desktop manager.

protected

JComponent

createEastPane

​(

JInternalFrame

w)

Creates the east pane.

protected

MouseInputListener

createGlassPaneDispatcher

()

Creates a

GlassPaneDispatcher

.

protected void

createInternalFrameListener

()

Creates the internal frame listener.

protected

LayoutManager

createLayoutManager

()

Creates the layout manager.

protected

JComponent

createNorthPane

​(

JInternalFrame

w)

Creates the north pane.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates the property change listener.

protected

JComponent

createSouthPane

​(

JInternalFrame

w)

Creates the north pane.

static

ComponentUI

createUI

​(

JComponent

b)

Returns a component UI.

protected

JComponent

createWestPane

​(

JInternalFrame

w)

Creates the west pane.

protected void

deactivateFrame

​(

JInternalFrame

f)

This method is called when the frame is no longer selected.

protected void

deiconifyFrame

​(

JInternalFrame

f)

This method is called when the user wants to deiconify the frame.

protected void

deinstallMouseHandlers

​(

JComponent

c)

Deinstalls the mouse handlers.

protected

DesktopManager

getDesktopManager

()

Returns the proper DesktopManager.

JComponent

getEastPane

()

Returns the east pane.

Dimension

getMaximumSize

​(

JComponent

x)

Returns the maximum size.

Dimension

getMinimumSize

​(

JComponent

x)

Returns the minimum size.

JComponent

getNorthPane

()

Returns the north pane.

Dimension

getPreferredSize

​(

JComponent

x)

Returns the preferred size.

JComponent

getSouthPane

()

Returns the south pane.

JComponent

getWestPane

()

Returns the west pane.

protected void

iconifyFrame

​(

JInternalFrame

f)

This method is called when the user wants to iconify the frame.

protected void

installComponents

()

Installs the components.

protected void

installDefaults

()

Installs the defaults.

protected void

installKeyboardActions

()

Installs the keyboard actions.

protected void

installListeners

()

Installs the listeners.

protected void

installMouseHandlers

​(

JComponent

c)

Installs the mouse handlers.

void

installUI

​(

JComponent

c)

Installs the UI.

boolean

isKeyBindingActive

()

Returns whether or no the key binding is active.

protected boolean

isKeyBindingRegistered

()

Returns whether or no the key binding is registered.

protected void

maximizeFrame

​(

JInternalFrame

f)

This method is called when the user wants to maximize the frame.

protected void

minimizeFrame

​(

JInternalFrame

f)

This method is called when the user wants to minimize the frame.

protected void

replacePane

​(

JComponent

currentPane,

JComponent

newPane)

Installs necessary mouse handlers on

newPane

and adds it to the frame.

void

setEastPane

​(

JComponent

c)

Sets the east pane.

protected void

setKeyBindingActive

​(boolean b)

Sets the key binding activity.

protected void

setKeyBindingRegistered

​(boolean b)

Sets the key binding registration.

void

setNorthPane

​(

JComponent

c)

Sets the north pane.

void

setSouthPane

​(

JComponent

c)

Sets the south pane.

protected void

setupMenuCloseKey

()

Setup the menu close key.

protected void

setupMenuOpenKey

()

Setup the menu open key.

void

setWestPane

​(

JComponent

c)

Sets the west pane.

protected void

uninstallComponents

()

Uninstalls the components.

protected void

uninstallDefaults

()

Uninstalls the defaults.

protected void

uninstallKeyboardActions

()

Uninstalls the keyboard actions.

protected void

uninstallListeners

()

Uninstalls the listeners.

void

uninstallUI

​(

JComponent

c)

Uninstalls the UI.

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

This method is called when the frame becomes selected.

This method is called when the user wants to close the frame.

Creates the border listener.

Creates a component listener.

Creates the desktop manager.

Creates the east pane.

Creates a

GlassPaneDispatcher

.

Creates the internal frame listener.

Creates the layout manager.

Creates the north pane.

Creates the property change listener.

Returns a component UI.

Creates the west pane.

This method is called when the frame is no longer selected.

This method is called when the user wants to deiconify the frame.

Deinstalls the mouse handlers.

Returns the proper DesktopManager.

Returns the east pane.

Returns the maximum size.

Returns the minimum size.

Returns the north pane.

Returns the preferred size.

Returns the south pane.

Returns the west pane.

This method is called when the user wants to iconify the frame.

Installs the components.

Installs the defaults.

Installs the keyboard actions.

Installs the listeners.

Installs the mouse handlers.

Installs the UI.

Returns whether or no the key binding is active.

Returns whether or no the key binding is registered.

This method is called when the user wants to maximize the frame.

This method is called when the user wants to minimize the frame.

Installs necessary mouse handlers on

newPane

and adds it to the frame.

Sets the east pane.

Sets the key binding activity.

Sets the key binding registration.

Sets the north pane.

Sets the south pane.

Setup the menu close key.

Setup the menu open key.

Sets the west pane.

Uninstalls the components.

Uninstalls the defaults.

Uninstalls the keyboard actions.

Uninstalls the listeners.

Uninstalls the UI.

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

============ FIELD DETAIL ===========

- Field Detail

- frame

```java
protected
JInternalFrame
frame
```

frame

- borderListener

```java
protected
MouseInputAdapter
borderListener
```

Border listener

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Property change listener

- internalFrameLayout

```java
protected
LayoutManager
internalFrameLayout
```

Internal frame layout

- componentListener

```java
protected
ComponentListener
componentListener
```

Component listener

- glassPaneDispatcher

```java
protected
MouseInputListener
glassPaneDispatcher
```

Glass pane dispatcher

- northPane

```java
protected
JComponent
northPane
```

North pane

- southPane

```java
protected
JComponent
southPane
```

South pane

- westPane

```java
protected
JComponent
westPane
```

West pane

- eastPane

```java
protected
JComponent
eastPane
```

East pane

- titlePane

```java
protected
BasicInternalFrameTitlePane
titlePane
```

Title pane

- openMenuKey

```java
@Deprecated

protected
KeyStroke
openMenuKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicInternalFrameUI

```java
public BasicInternalFrameUI​(
JInternalFrame
b)
```

Constructs a

BasicInternalFrameUI

.

**Parameters:** b

- the internal frame

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
b)
```

Returns a component UI.

**Parameters:** b

- a component
**Returns:** a component UI

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

- installDefaults

```java
protected void installDefaults()
```

Installs the defaults.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs the keyboard actions.

- installComponents

```java
protected void installComponents()
```

Installs the components.

- installListeners

```java
protected void installListeners()
```

Installs the listeners.

**Since:** 1.3

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the defaults.

- uninstallComponents

```java
protected void uninstallComponents()
```

Uninstalls the components.

- uninstallListeners

```java
protected void uninstallListeners()
```

Uninstalls the listeners.

**Since:** 1.3

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Uninstalls the keyboard actions.

- createLayoutManager

```java
protected
LayoutManager
createLayoutManager()
```

Creates the layout manager.

**Returns:** the layout manager

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates the property change listener.

**Returns:** the property change listener

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
x)
```

Returns the preferred size.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** x

- the component
**Returns:** the preferred size
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
x)
```

Returns the minimum size.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** x

- the component
**Returns:** the minimum size
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
x)
```

Returns the maximum size.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** x

- the component
**Returns:** the maximum size
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- replacePane

```java
protected void replacePane​(
JComponent
currentPane,

JComponent
newPane)
```

Installs necessary mouse handlers on

newPane

and adds it to the frame.
Reverse process for the

currentPane

.

**Parameters:** currentPane

- this

Jcomponent

is the current pane being
viewed that has mouse handlers installed
**Parameters:** newPane

- this

Jcomponent

is the pane which will be added
and have mouse handlers installed

- deinstallMouseHandlers

```java
protected void deinstallMouseHandlers​(
JComponent
c)
```

Deinstalls the mouse handlers.

**Parameters:** c

- the component

- installMouseHandlers

```java
protected void installMouseHandlers​(
JComponent
c)
```

Installs the mouse handlers.

**Parameters:** c

- the component

- createNorthPane

```java
protected
JComponent
createNorthPane​(
JInternalFrame
w)
```

Creates the north pane.

**Parameters:** w

- the internal frame
**Returns:** the north pane

- createSouthPane

```java
protected
JComponent
createSouthPane​(
JInternalFrame
w)
```

Creates the north pane.

**Parameters:** w

- the internal frame
**Returns:** the north pane

- createWestPane

```java
protected
JComponent
createWestPane​(
JInternalFrame
w)
```

Creates the west pane.

**Parameters:** w

- the internal frame
**Returns:** the west pane

- createEastPane

```java
protected
JComponent
createEastPane​(
JInternalFrame
w)
```

Creates the east pane.

**Parameters:** w

- the internal frame
**Returns:** the east pane

- createBorderListener

```java
protected
MouseInputAdapter
createBorderListener​(
JInternalFrame
w)
```

Creates the border listener.

**Parameters:** w

- the internal frame
**Returns:** the border listener

- createInternalFrameListener

```java
protected void createInternalFrameListener()
```

Creates the internal frame listener.

- isKeyBindingRegistered

```java
protected final boolean isKeyBindingRegistered()
```

Returns whether or no the key binding is registered.

**Returns:** whether or no the key binding is registered

- setKeyBindingRegistered

```java
protected final void setKeyBindingRegistered​(boolean b)
```

Sets the key binding registration.

**Parameters:** b

- new value for key binding registration

- isKeyBindingActive

```java
public final boolean isKeyBindingActive()
```

Returns whether or no the key binding is active.

**Returns:** whether or no the key binding is active

- setKeyBindingActive

```java
protected final void setKeyBindingActive​(boolean b)
```

Sets the key binding activity.

**Parameters:** b

- new value for key binding activity

- setupMenuOpenKey

```java
protected void setupMenuOpenKey()
```

Setup the menu open key.

- setupMenuCloseKey

```java
protected void setupMenuCloseKey()
```

Setup the menu close key.

- getNorthPane

```java
public
JComponent
getNorthPane()
```

Returns the north pane.

**Returns:** the north pane

- setNorthPane

```java
public void setNorthPane​(
JComponent
c)
```

Sets the north pane.

**Parameters:** c

- the new north pane

- getSouthPane

```java
public
JComponent
getSouthPane()
```

Returns the south pane.

**Returns:** the south pane

- setSouthPane

```java
public void setSouthPane​(
JComponent
c)
```

Sets the south pane.

**Parameters:** c

- the new south pane

- getWestPane

```java
public
JComponent
getWestPane()
```

Returns the west pane.

**Returns:** the west pane

- setWestPane

```java
public void setWestPane​(
JComponent
c)
```

Sets the west pane.

**Parameters:** c

- the new west pane

- getEastPane

```java
public
JComponent
getEastPane()
```

Returns the east pane.

**Returns:** the east pane

- setEastPane

```java
public void setEastPane​(
JComponent
c)
```

Sets the east pane.

**Parameters:** c

- the new east pane

- getDesktopManager

```java
protected
DesktopManager
getDesktopManager()
```

Returns the proper DesktopManager. Calls getDesktopPane() to
find the JDesktop component and returns the desktopManager from
it. If this fails, it will return a default DesktopManager that
should work in arbitrary parents.

**Returns:** the proper DesktopManager

- createDesktopManager

```java
protected
DesktopManager
createDesktopManager()
```

Creates the desktop manager.

**Returns:** the desktop manager

- closeFrame

```java
protected void closeFrame​(
JInternalFrame
f)
```

This method is called when the user wants to close the frame.
The

playCloseSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- maximizeFrame

```java
protected void maximizeFrame​(
JInternalFrame
f)
```

This method is called when the user wants to maximize the frame.
The

playMaximizeSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- minimizeFrame

```java
protected void minimizeFrame​(
JInternalFrame
f)
```

This method is called when the user wants to minimize the frame.
The

playRestoreDownSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- iconifyFrame

```java
protected void iconifyFrame​(
JInternalFrame
f)
```

This method is called when the user wants to iconify the frame.
The

playMinimizeSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- deiconifyFrame

```java
protected void deiconifyFrame​(
JInternalFrame
f)
```

This method is called when the user wants to deiconify the frame.
The

playRestoreUpSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- activateFrame

```java
protected void activateFrame​(
JInternalFrame
f)
```

This method is called when the frame becomes selected.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- deactivateFrame

```java
protected void deactivateFrame​(
JInternalFrame
f)
```

This method is called when the frame is no longer selected.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- createComponentListener

```java
protected
ComponentListener
createComponentListener()
```

Creates a component listener.

**Returns:** a component listener

- createGlassPaneDispatcher

```java
protected
MouseInputListener
createGlassPaneDispatcher()
```

Creates a

GlassPaneDispatcher

.

**Returns:** a

GlassPaneDispatcher

Field Detail

- frame

```java
protected
JInternalFrame
frame
```

frame

- borderListener

```java
protected
MouseInputAdapter
borderListener
```

Border listener

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Property change listener

- internalFrameLayout

```java
protected
LayoutManager
internalFrameLayout
```

Internal frame layout

- componentListener

```java
protected
ComponentListener
componentListener
```

Component listener

- glassPaneDispatcher

```java
protected
MouseInputListener
glassPaneDispatcher
```

Glass pane dispatcher

- northPane

```java
protected
JComponent
northPane
```

North pane

- southPane

```java
protected
JComponent
southPane
```

South pane

- westPane

```java
protected
JComponent
westPane
```

West pane

- eastPane

```java
protected
JComponent
eastPane
```

East pane

- titlePane

```java
protected
BasicInternalFrameTitlePane
titlePane
```

Title pane

- openMenuKey

```java
@Deprecated

protected
KeyStroke
openMenuKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### Field Detail

frame

```java
protected
JInternalFrame
frame
```

frame

---

#### frame

protected

JInternalFrame

frame

frame

borderListener

```java
protected
MouseInputAdapter
borderListener
```

Border listener

---

#### borderListener

protected

MouseInputAdapter

borderListener

Border listener

propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Property change listener

---

#### propertyChangeListener

protected

PropertyChangeListener

propertyChangeListener

Property change listener

internalFrameLayout

```java
protected
LayoutManager
internalFrameLayout
```

Internal frame layout

---

#### internalFrameLayout

protected

LayoutManager

internalFrameLayout

Internal frame layout

componentListener

```java
protected
ComponentListener
componentListener
```

Component listener

---

#### componentListener

protected

ComponentListener

componentListener

Component listener

glassPaneDispatcher

```java
protected
MouseInputListener
glassPaneDispatcher
```

Glass pane dispatcher

---

#### glassPaneDispatcher

protected

MouseInputListener

glassPaneDispatcher

Glass pane dispatcher

northPane

```java
protected
JComponent
northPane
```

North pane

---

#### northPane

protected

JComponent

northPane

North pane

southPane

```java
protected
JComponent
southPane
```

South pane

---

#### southPane

protected

JComponent

southPane

South pane

westPane

```java
protected
JComponent
westPane
```

West pane

---

#### westPane

protected

JComponent

westPane

West pane

eastPane

```java
protected
JComponent
eastPane
```

East pane

---

#### eastPane

protected

JComponent

eastPane

East pane

titlePane

```java
protected
BasicInternalFrameTitlePane
titlePane
```

Title pane

---

#### titlePane

protected

BasicInternalFrameTitlePane

titlePane

Title pane

openMenuKey

```java
@Deprecated

protected
KeyStroke
openMenuKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### openMenuKey

@Deprecated

protected

KeyStroke

openMenuKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

Constructor Detail

- BasicInternalFrameUI

```java
public BasicInternalFrameUI​(
JInternalFrame
b)
```

Constructs a

BasicInternalFrameUI

.

**Parameters:** b

- the internal frame

---

#### Constructor Detail

BasicInternalFrameUI

```java
public BasicInternalFrameUI​(
JInternalFrame
b)
```

Constructs a

BasicInternalFrameUI

.

**Parameters:** b

- the internal frame

---

#### BasicInternalFrameUI

public BasicInternalFrameUI​(

JInternalFrame

b)

Constructs a

BasicInternalFrameUI

.

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
b)
```

Returns a component UI.

**Parameters:** b

- a component
**Returns:** a component UI

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

- installDefaults

```java
protected void installDefaults()
```

Installs the defaults.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs the keyboard actions.

- installComponents

```java
protected void installComponents()
```

Installs the components.

- installListeners

```java
protected void installListeners()
```

Installs the listeners.

**Since:** 1.3

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the defaults.

- uninstallComponents

```java
protected void uninstallComponents()
```

Uninstalls the components.

- uninstallListeners

```java
protected void uninstallListeners()
```

Uninstalls the listeners.

**Since:** 1.3

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Uninstalls the keyboard actions.

- createLayoutManager

```java
protected
LayoutManager
createLayoutManager()
```

Creates the layout manager.

**Returns:** the layout manager

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates the property change listener.

**Returns:** the property change listener

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
x)
```

Returns the preferred size.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** x

- the component
**Returns:** the preferred size
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
x)
```

Returns the minimum size.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** x

- the component
**Returns:** the minimum size
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
x)
```

Returns the maximum size.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** x

- the component
**Returns:** the maximum size
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- replacePane

```java
protected void replacePane​(
JComponent
currentPane,

JComponent
newPane)
```

Installs necessary mouse handlers on

newPane

and adds it to the frame.
Reverse process for the

currentPane

.

**Parameters:** currentPane

- this

Jcomponent

is the current pane being
viewed that has mouse handlers installed
**Parameters:** newPane

- this

Jcomponent

is the pane which will be added
and have mouse handlers installed

- deinstallMouseHandlers

```java
protected void deinstallMouseHandlers​(
JComponent
c)
```

Deinstalls the mouse handlers.

**Parameters:** c

- the component

- installMouseHandlers

```java
protected void installMouseHandlers​(
JComponent
c)
```

Installs the mouse handlers.

**Parameters:** c

- the component

- createNorthPane

```java
protected
JComponent
createNorthPane​(
JInternalFrame
w)
```

Creates the north pane.

**Parameters:** w

- the internal frame
**Returns:** the north pane

- createSouthPane

```java
protected
JComponent
createSouthPane​(
JInternalFrame
w)
```

Creates the north pane.

**Parameters:** w

- the internal frame
**Returns:** the north pane

- createWestPane

```java
protected
JComponent
createWestPane​(
JInternalFrame
w)
```

Creates the west pane.

**Parameters:** w

- the internal frame
**Returns:** the west pane

- createEastPane

```java
protected
JComponent
createEastPane​(
JInternalFrame
w)
```

Creates the east pane.

**Parameters:** w

- the internal frame
**Returns:** the east pane

- createBorderListener

```java
protected
MouseInputAdapter
createBorderListener​(
JInternalFrame
w)
```

Creates the border listener.

**Parameters:** w

- the internal frame
**Returns:** the border listener

- createInternalFrameListener

```java
protected void createInternalFrameListener()
```

Creates the internal frame listener.

- isKeyBindingRegistered

```java
protected final boolean isKeyBindingRegistered()
```

Returns whether or no the key binding is registered.

**Returns:** whether or no the key binding is registered

- setKeyBindingRegistered

```java
protected final void setKeyBindingRegistered​(boolean b)
```

Sets the key binding registration.

**Parameters:** b

- new value for key binding registration

- isKeyBindingActive

```java
public final boolean isKeyBindingActive()
```

Returns whether or no the key binding is active.

**Returns:** whether or no the key binding is active

- setKeyBindingActive

```java
protected final void setKeyBindingActive​(boolean b)
```

Sets the key binding activity.

**Parameters:** b

- new value for key binding activity

- setupMenuOpenKey

```java
protected void setupMenuOpenKey()
```

Setup the menu open key.

- setupMenuCloseKey

```java
protected void setupMenuCloseKey()
```

Setup the menu close key.

- getNorthPane

```java
public
JComponent
getNorthPane()
```

Returns the north pane.

**Returns:** the north pane

- setNorthPane

```java
public void setNorthPane​(
JComponent
c)
```

Sets the north pane.

**Parameters:** c

- the new north pane

- getSouthPane

```java
public
JComponent
getSouthPane()
```

Returns the south pane.

**Returns:** the south pane

- setSouthPane

```java
public void setSouthPane​(
JComponent
c)
```

Sets the south pane.

**Parameters:** c

- the new south pane

- getWestPane

```java
public
JComponent
getWestPane()
```

Returns the west pane.

**Returns:** the west pane

- setWestPane

```java
public void setWestPane​(
JComponent
c)
```

Sets the west pane.

**Parameters:** c

- the new west pane

- getEastPane

```java
public
JComponent
getEastPane()
```

Returns the east pane.

**Returns:** the east pane

- setEastPane

```java
public void setEastPane​(
JComponent
c)
```

Sets the east pane.

**Parameters:** c

- the new east pane

- getDesktopManager

```java
protected
DesktopManager
getDesktopManager()
```

Returns the proper DesktopManager. Calls getDesktopPane() to
find the JDesktop component and returns the desktopManager from
it. If this fails, it will return a default DesktopManager that
should work in arbitrary parents.

**Returns:** the proper DesktopManager

- createDesktopManager

```java
protected
DesktopManager
createDesktopManager()
```

Creates the desktop manager.

**Returns:** the desktop manager

- closeFrame

```java
protected void closeFrame​(
JInternalFrame
f)
```

This method is called when the user wants to close the frame.
The

playCloseSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- maximizeFrame

```java
protected void maximizeFrame​(
JInternalFrame
f)
```

This method is called when the user wants to maximize the frame.
The

playMaximizeSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- minimizeFrame

```java
protected void minimizeFrame​(
JInternalFrame
f)
```

This method is called when the user wants to minimize the frame.
The

playRestoreDownSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- iconifyFrame

```java
protected void iconifyFrame​(
JInternalFrame
f)
```

This method is called when the user wants to iconify the frame.
The

playMinimizeSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- deiconifyFrame

```java
protected void deiconifyFrame​(
JInternalFrame
f)
```

This method is called when the user wants to deiconify the frame.
The

playRestoreUpSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- activateFrame

```java
protected void activateFrame​(
JInternalFrame
f)
```

This method is called when the frame becomes selected.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- deactivateFrame

```java
protected void deactivateFrame​(
JInternalFrame
f)
```

This method is called when the frame is no longer selected.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

- createComponentListener

```java
protected
ComponentListener
createComponentListener()
```

Creates a component listener.

**Returns:** a component listener

- createGlassPaneDispatcher

```java
protected
MouseInputListener
createGlassPaneDispatcher()
```

Creates a

GlassPaneDispatcher

.

**Returns:** a

GlassPaneDispatcher

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
b)
```

Returns a component UI.

**Parameters:** b

- a component
**Returns:** a component UI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

b)

Returns a component UI.

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

installDefaults

```java
protected void installDefaults()
```

Installs the defaults.

---

#### installDefaults

protected void installDefaults()

Installs the defaults.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs the keyboard actions.

---

#### installKeyboardActions

protected void installKeyboardActions()

Installs the keyboard actions.

installComponents

```java
protected void installComponents()
```

Installs the components.

---

#### installComponents

protected void installComponents()

Installs the components.

installListeners

```java
protected void installListeners()
```

Installs the listeners.

**Since:** 1.3

---

#### installListeners

protected void installListeners()

Installs the listeners.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the defaults.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls the defaults.

uninstallComponents

```java
protected void uninstallComponents()
```

Uninstalls the components.

---

#### uninstallComponents

protected void uninstallComponents()

Uninstalls the components.

uninstallListeners

```java
protected void uninstallListeners()
```

Uninstalls the listeners.

**Since:** 1.3

---

#### uninstallListeners

protected void uninstallListeners()

Uninstalls the listeners.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Uninstalls the keyboard actions.

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Uninstalls the keyboard actions.

createLayoutManager

```java
protected
LayoutManager
createLayoutManager()
```

Creates the layout manager.

**Returns:** the layout manager

---

#### createLayoutManager

protected

LayoutManager

createLayoutManager()

Creates the layout manager.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates the property change listener.

**Returns:** the property change listener

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener()

Creates the property change listener.

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
x)
```

Returns the preferred size.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** x

- the component
**Returns:** the preferred size
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### getPreferredSize

public

Dimension

getPreferredSize​(

JComponent

x)

Returns the preferred size.

getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
x)
```

Returns the minimum size.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** x

- the component
**Returns:** the minimum size
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

x)

Returns the minimum size.

getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
x)
```

Returns the maximum size.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** x

- the component
**Returns:** the maximum size
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### getMaximumSize

public

Dimension

getMaximumSize​(

JComponent

x)

Returns the maximum size.

replacePane

```java
protected void replacePane​(
JComponent
currentPane,

JComponent
newPane)
```

Installs necessary mouse handlers on

newPane

and adds it to the frame.
Reverse process for the

currentPane

.

**Parameters:** currentPane

- this

Jcomponent

is the current pane being
viewed that has mouse handlers installed
**Parameters:** newPane

- this

Jcomponent

is the pane which will be added
and have mouse handlers installed

---

#### replacePane

protected void replacePane​(

JComponent

currentPane,

JComponent

newPane)

Installs necessary mouse handlers on

newPane

and adds it to the frame.
Reverse process for the

currentPane

.

deinstallMouseHandlers

```java
protected void deinstallMouseHandlers​(
JComponent
c)
```

Deinstalls the mouse handlers.

**Parameters:** c

- the component

---

#### deinstallMouseHandlers

protected void deinstallMouseHandlers​(

JComponent

c)

Deinstalls the mouse handlers.

installMouseHandlers

```java
protected void installMouseHandlers​(
JComponent
c)
```

Installs the mouse handlers.

**Parameters:** c

- the component

---

#### installMouseHandlers

protected void installMouseHandlers​(

JComponent

c)

Installs the mouse handlers.

createNorthPane

```java
protected
JComponent
createNorthPane​(
JInternalFrame
w)
```

Creates the north pane.

**Parameters:** w

- the internal frame
**Returns:** the north pane

---

#### createNorthPane

protected

JComponent

createNorthPane​(

JInternalFrame

w)

Creates the north pane.

createSouthPane

```java
protected
JComponent
createSouthPane​(
JInternalFrame
w)
```

Creates the north pane.

**Parameters:** w

- the internal frame
**Returns:** the north pane

---

#### createSouthPane

protected

JComponent

createSouthPane​(

JInternalFrame

w)

Creates the north pane.

createWestPane

```java
protected
JComponent
createWestPane​(
JInternalFrame
w)
```

Creates the west pane.

**Parameters:** w

- the internal frame
**Returns:** the west pane

---

#### createWestPane

protected

JComponent

createWestPane​(

JInternalFrame

w)

Creates the west pane.

createEastPane

```java
protected
JComponent
createEastPane​(
JInternalFrame
w)
```

Creates the east pane.

**Parameters:** w

- the internal frame
**Returns:** the east pane

---

#### createEastPane

protected

JComponent

createEastPane​(

JInternalFrame

w)

Creates the east pane.

createBorderListener

```java
protected
MouseInputAdapter
createBorderListener​(
JInternalFrame
w)
```

Creates the border listener.

**Parameters:** w

- the internal frame
**Returns:** the border listener

---

#### createBorderListener

protected

MouseInputAdapter

createBorderListener​(

JInternalFrame

w)

Creates the border listener.

createInternalFrameListener

```java
protected void createInternalFrameListener()
```

Creates the internal frame listener.

---

#### createInternalFrameListener

protected void createInternalFrameListener()

Creates the internal frame listener.

isKeyBindingRegistered

```java
protected final boolean isKeyBindingRegistered()
```

Returns whether or no the key binding is registered.

**Returns:** whether or no the key binding is registered

---

#### isKeyBindingRegistered

protected final boolean isKeyBindingRegistered()

Returns whether or no the key binding is registered.

setKeyBindingRegistered

```java
protected final void setKeyBindingRegistered​(boolean b)
```

Sets the key binding registration.

**Parameters:** b

- new value for key binding registration

---

#### setKeyBindingRegistered

protected final void setKeyBindingRegistered​(boolean b)

Sets the key binding registration.

isKeyBindingActive

```java
public final boolean isKeyBindingActive()
```

Returns whether or no the key binding is active.

**Returns:** whether or no the key binding is active

---

#### isKeyBindingActive

public final boolean isKeyBindingActive()

Returns whether or no the key binding is active.

setKeyBindingActive

```java
protected final void setKeyBindingActive​(boolean b)
```

Sets the key binding activity.

**Parameters:** b

- new value for key binding activity

---

#### setKeyBindingActive

protected final void setKeyBindingActive​(boolean b)

Sets the key binding activity.

setupMenuOpenKey

```java
protected void setupMenuOpenKey()
```

Setup the menu open key.

---

#### setupMenuOpenKey

protected void setupMenuOpenKey()

Setup the menu open key.

setupMenuCloseKey

```java
protected void setupMenuCloseKey()
```

Setup the menu close key.

---

#### setupMenuCloseKey

protected void setupMenuCloseKey()

Setup the menu close key.

getNorthPane

```java
public
JComponent
getNorthPane()
```

Returns the north pane.

**Returns:** the north pane

---

#### getNorthPane

public

JComponent

getNorthPane()

Returns the north pane.

setNorthPane

```java
public void setNorthPane​(
JComponent
c)
```

Sets the north pane.

**Parameters:** c

- the new north pane

---

#### setNorthPane

public void setNorthPane​(

JComponent

c)

Sets the north pane.

getSouthPane

```java
public
JComponent
getSouthPane()
```

Returns the south pane.

**Returns:** the south pane

---

#### getSouthPane

public

JComponent

getSouthPane()

Returns the south pane.

setSouthPane

```java
public void setSouthPane​(
JComponent
c)
```

Sets the south pane.

**Parameters:** c

- the new south pane

---

#### setSouthPane

public void setSouthPane​(

JComponent

c)

Sets the south pane.

getWestPane

```java
public
JComponent
getWestPane()
```

Returns the west pane.

**Returns:** the west pane

---

#### getWestPane

public

JComponent

getWestPane()

Returns the west pane.

setWestPane

```java
public void setWestPane​(
JComponent
c)
```

Sets the west pane.

**Parameters:** c

- the new west pane

---

#### setWestPane

public void setWestPane​(

JComponent

c)

Sets the west pane.

getEastPane

```java
public
JComponent
getEastPane()
```

Returns the east pane.

**Returns:** the east pane

---

#### getEastPane

public

JComponent

getEastPane()

Returns the east pane.

setEastPane

```java
public void setEastPane​(
JComponent
c)
```

Sets the east pane.

**Parameters:** c

- the new east pane

---

#### setEastPane

public void setEastPane​(

JComponent

c)

Sets the east pane.

getDesktopManager

```java
protected
DesktopManager
getDesktopManager()
```

Returns the proper DesktopManager. Calls getDesktopPane() to
find the JDesktop component and returns the desktopManager from
it. If this fails, it will return a default DesktopManager that
should work in arbitrary parents.

**Returns:** the proper DesktopManager

---

#### getDesktopManager

protected

DesktopManager

getDesktopManager()

Returns the proper DesktopManager. Calls getDesktopPane() to
find the JDesktop component and returns the desktopManager from
it. If this fails, it will return a default DesktopManager that
should work in arbitrary parents.

createDesktopManager

```java
protected
DesktopManager
createDesktopManager()
```

Creates the desktop manager.

**Returns:** the desktop manager

---

#### createDesktopManager

protected

DesktopManager

createDesktopManager()

Creates the desktop manager.

closeFrame

```java
protected void closeFrame​(
JInternalFrame
f)
```

This method is called when the user wants to close the frame.
The

playCloseSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

---

#### closeFrame

protected void closeFrame​(

JInternalFrame

f)

This method is called when the user wants to close the frame.
The

playCloseSound

Action is fired.
This action is delegated to the desktopManager.

maximizeFrame

```java
protected void maximizeFrame​(
JInternalFrame
f)
```

This method is called when the user wants to maximize the frame.
The

playMaximizeSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

---

#### maximizeFrame

protected void maximizeFrame​(

JInternalFrame

f)

This method is called when the user wants to maximize the frame.
The

playMaximizeSound

Action is fired.
This action is delegated to the desktopManager.

minimizeFrame

```java
protected void minimizeFrame​(
JInternalFrame
f)
```

This method is called when the user wants to minimize the frame.
The

playRestoreDownSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

---

#### minimizeFrame

protected void minimizeFrame​(

JInternalFrame

f)

This method is called when the user wants to minimize the frame.
The

playRestoreDownSound

Action is fired.
This action is delegated to the desktopManager.

iconifyFrame

```java
protected void iconifyFrame​(
JInternalFrame
f)
```

This method is called when the user wants to iconify the frame.
The

playMinimizeSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

---

#### iconifyFrame

protected void iconifyFrame​(

JInternalFrame

f)

This method is called when the user wants to iconify the frame.
The

playMinimizeSound

Action is fired.
This action is delegated to the desktopManager.

deiconifyFrame

```java
protected void deiconifyFrame​(
JInternalFrame
f)
```

This method is called when the user wants to deiconify the frame.
The

playRestoreUpSound

Action is fired.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

---

#### deiconifyFrame

protected void deiconifyFrame​(

JInternalFrame

f)

This method is called when the user wants to deiconify the frame.
The

playRestoreUpSound

Action is fired.
This action is delegated to the desktopManager.

activateFrame

```java
protected void activateFrame​(
JInternalFrame
f)
```

This method is called when the frame becomes selected.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

---

#### activateFrame

protected void activateFrame​(

JInternalFrame

f)

This method is called when the frame becomes selected.
This action is delegated to the desktopManager.

deactivateFrame

```java
protected void deactivateFrame​(
JInternalFrame
f)
```

This method is called when the frame is no longer selected.
This action is delegated to the desktopManager.

**Parameters:** f

- the

JInternalFrame

being viewed

---

#### deactivateFrame

protected void deactivateFrame​(

JInternalFrame

f)

This method is called when the frame is no longer selected.
This action is delegated to the desktopManager.

createComponentListener

```java
protected
ComponentListener
createComponentListener()
```

Creates a component listener.

**Returns:** a component listener

---

#### createComponentListener

protected

ComponentListener

createComponentListener()

Creates a component listener.

createGlassPaneDispatcher

```java
protected
MouseInputListener
createGlassPaneDispatcher()
```

Creates a

GlassPaneDispatcher

.

**Returns:** a

GlassPaneDispatcher

---

#### createGlassPaneDispatcher

protected

MouseInputListener

createGlassPaneDispatcher()

Creates a

GlassPaneDispatcher

.

---

