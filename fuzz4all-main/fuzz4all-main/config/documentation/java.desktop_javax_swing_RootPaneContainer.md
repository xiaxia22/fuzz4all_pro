# Interface RootPaneContainer

**Source:** `java.desktop\javax\swing\RootPaneContainer.html`

### Class Description

```java
public interface
RootPaneContainer
```

This interface is implemented by components that have a single
JRootPane child: JDialog, JFrame, JWindow, JApplet, JInternalFrame.
The methods in this interface are just

covers

for the JRootPane
properties, e.g.

getContentPane()

is generally implemented
like this:

```java
public Container getContentPane() {
return getRootPane().getContentPane();
}
```

This interface serves as a

marker

for Swing GUI builders
that need to treat components like JFrame, that contain a
single JRootPane, specially. For example in a GUI builder,
dropping a component on a RootPaneContainer would be interpreted
as

frame.getContentPane().add(child)

.

As a convenience, the standard classes that implement this interface
(such as

JFrame

,

JDialog

,

JWindow

,

JApplet

,
and

JInternalFrame

) have their

add

,

remove

,
and

setLayout

methods overridden, so that they delegate calls
to the corresponding methods of the

ContentPane

.
For example, you can add a child component to a frame as follows:

```java
frame.add(child);
```

instead of:

```java
frame.getContentPane().add(child);
```

The behavior of the

add

and

setLayout

methods for

JFrame

,

JDialog

,

JWindow

,

JApplet

and

JInternalFrame

is controlled by
the

rootPaneCheckingEnabled

property. If this property is
true (the default), then calls to these methods are
forwarded to the

contentPane

; if false, these
methods operate directly on the

RootPaneContainer

. This
property is only intended for subclasses, and is therefore protected.

**All Known Implementing Classes:** JApplet

,

JDialog

,

JFrame

,

JInternalFrame

,

JWindow

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### JRootPane
getRootPane()

Return this component's single JRootPane child. A conventional
implementation of this interface will have all of the other
methods indirect through this one. The rootPane has two
children: the glassPane and the layeredPane.

**Returns:**
- this components single JRootPane child.

**See Also:**
- JRootPane

---

#### void setContentPane​(
Container
contentPane)

The "contentPane" is the primary container for application
specific components. Applications should add children to
the contentPane, set its layout manager, and so on.

The contentPane may not be null.

Generally implemented with

getRootPane().setContentPane(contentPane);

**Parameters:**
- contentPane

- the Container to use for the contents of this
JRootPane

**Throws:**
- IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is null

**See Also:**
- JRootPane.getContentPane()

,

getContentPane()

---

#### Container
getContentPane()

Returns the contentPane.

**Returns:**
- the value of the contentPane property.

**See Also:**
- setContentPane(java.awt.Container)

---

#### void setLayeredPane​(
JLayeredPane
layeredPane)

A Container that manages the contentPane and in some cases a menu bar.
The layeredPane can be used by descendants that want to add a child
to the RootPaneContainer that isn't layout managed. For example
an internal dialog or a drag and drop effect component.

The layeredPane may not be null.

Generally implemented with

```java
getRootPane().setLayeredPane(layeredPane);
```

**Parameters:**
- layeredPane

- the layered pane

**Throws:**
- IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is null

**See Also:**
- getLayeredPane()

,

JRootPane.getLayeredPane()

---

#### JLayeredPane
getLayeredPane()

Returns the layeredPane.

**Returns:**
- the value of the layeredPane property.

**See Also:**
- setLayeredPane(javax.swing.JLayeredPane)

---

#### void setGlassPane​(
Component
glassPane)

The glassPane is always the first child of the rootPane
and the rootPanes layout manager ensures that it's always
as big as the rootPane. By default it's transparent and
not visible. It can be used to temporarily grab all keyboard
and mouse input by adding listeners and then making it visible.
by default it's not visible.

The glassPane may not be null.

Generally implemented with

getRootPane().setGlassPane(glassPane);

**Parameters:**
- glassPane

- the glass pane

**See Also:**
- getGlassPane()

,

JRootPane.setGlassPane(java.awt.Component)

---

#### Component
getGlassPane()

Returns the glassPane.

**Returns:**
- the value of the glassPane property.

**See Also:**
- setGlassPane(java.awt.Component)

---

### Additional Sections

#### Interface RootPaneContainer

**All Known Implementing Classes:** JApplet

,

JDialog

,

JFrame

,

JInternalFrame

,

JWindow

```java
public interface
RootPaneContainer
```

This interface is implemented by components that have a single
JRootPane child: JDialog, JFrame, JWindow, JApplet, JInternalFrame.
The methods in this interface are just

covers

for the JRootPane
properties, e.g.

getContentPane()

is generally implemented
like this:

```java
public Container getContentPane() {
return getRootPane().getContentPane();
}
```

This interface serves as a

marker

for Swing GUI builders
that need to treat components like JFrame, that contain a
single JRootPane, specially. For example in a GUI builder,
dropping a component on a RootPaneContainer would be interpreted
as

frame.getContentPane().add(child)

.

As a convenience, the standard classes that implement this interface
(such as

JFrame

,

JDialog

,

JWindow

,

JApplet

,
and

JInternalFrame

) have their

add

,

remove

,
and

setLayout

methods overridden, so that they delegate calls
to the corresponding methods of the

ContentPane

.
For example, you can add a child component to a frame as follows:

```java
frame.add(child);
```

instead of:

```java
frame.getContentPane().add(child);
```

The behavior of the

add

and

setLayout

methods for

JFrame

,

JDialog

,

JWindow

,

JApplet

and

JInternalFrame

is controlled by
the

rootPaneCheckingEnabled

property. If this property is
true (the default), then calls to these methods are
forwarded to the

contentPane

; if false, these
methods operate directly on the

RootPaneContainer

. This
property is only intended for subclasses, and is therefore protected.

**Since:** 1.2
**See Also:** JRootPane

,

JFrame

,

JDialog

,

JWindow

,

JApplet

,

JInternalFrame

public interface

RootPaneContainer

This interface is implemented by components that have a single
JRootPane child: JDialog, JFrame, JWindow, JApplet, JInternalFrame.
The methods in this interface are just

covers

for the JRootPane
properties, e.g.

getContentPane()

is generally implemented
like this:

```java
public Container getContentPane() {
return getRootPane().getContentPane();
}
```

This interface serves as a

marker

for Swing GUI builders
that need to treat components like JFrame, that contain a
single JRootPane, specially. For example in a GUI builder,
dropping a component on a RootPaneContainer would be interpreted
as

frame.getContentPane().add(child)

.

As a convenience, the standard classes that implement this interface
(such as

JFrame

,

JDialog

,

JWindow

,

JApplet

,
and

JInternalFrame

) have their

add

,

remove

,
and

setLayout

methods overridden, so that they delegate calls
to the corresponding methods of the

ContentPane

.
For example, you can add a child component to a frame as follows:

```java
frame.add(child);
```

instead of:

```java
frame.getContentPane().add(child);
```

The behavior of the

add

and

setLayout

methods for

JFrame

,

JDialog

,

JWindow

,

JApplet

and

JInternalFrame

is controlled by
the

rootPaneCheckingEnabled

property. If this property is
true (the default), then calls to these methods are
forwarded to the

contentPane

; if false, these
methods operate directly on the

RootPaneContainer

. This
property is only intended for subclasses, and is therefore protected.

public Container getContentPane() {
return getRootPane().getContentPane();
}

As a convenience, the standard classes that implement this interface
(such as

JFrame

,

JDialog

,

JWindow

,

JApplet

,
and

JInternalFrame

) have their

add

,

remove

,
and

setLayout

methods overridden, so that they delegate calls
to the corresponding methods of the

ContentPane

.
For example, you can add a child component to a frame as follows:

```java
frame.add(child);
```

instead of:

```java
frame.getContentPane().add(child);
```

The behavior of the

add

and

setLayout

methods for

JFrame

,

JDialog

,

JWindow

,

JApplet

and

JInternalFrame

is controlled by
the

rootPaneCheckingEnabled

property. If this property is
true (the default), then calls to these methods are
forwarded to the

contentPane

; if false, these
methods operate directly on the

RootPaneContainer

. This
property is only intended for subclasses, and is therefore protected.

frame.add(child);

frame.getContentPane().add(child);

The behavior of the

add

and

setLayout

methods for

JFrame

,

JDialog

,

JWindow

,

JApplet

and

JInternalFrame

is controlled by
the

rootPaneCheckingEnabled

property. If this property is
true (the default), then calls to these methods are
forwarded to the

contentPane

; if false, these
methods operate directly on the

RootPaneContainer

. This
property is only intended for subclasses, and is therefore protected.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Container

getContentPane

()

Returns the contentPane.

Component

getGlassPane

()

Returns the glassPane.

JLayeredPane

getLayeredPane

()

Returns the layeredPane.

JRootPane

getRootPane

()

Return this component's single JRootPane child.

void

setContentPane

​(

Container

contentPane)

The "contentPane" is the primary container for application
specific components.

void

setGlassPane

​(

Component

glassPane)

The glassPane is always the first child of the rootPane
and the rootPanes layout manager ensures that it's always
as big as the rootPane.

void

setLayeredPane

​(

JLayeredPane

layeredPane)

A Container that manages the contentPane and in some cases a menu bar.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Container

getContentPane

()

Returns the contentPane.

Component

getGlassPane

()

Returns the glassPane.

JLayeredPane

getLayeredPane

()

Returns the layeredPane.

JRootPane

getRootPane

()

Return this component's single JRootPane child.

void

setContentPane

​(

Container

contentPane)

The "contentPane" is the primary container for application
specific components.

void

setGlassPane

​(

Component

glassPane)

The glassPane is always the first child of the rootPane
and the rootPanes layout manager ensures that it's always
as big as the rootPane.

void

setLayeredPane

​(

JLayeredPane

layeredPane)

A Container that manages the contentPane and in some cases a menu bar.

---

#### Method Summary

Returns the contentPane.

Returns the glassPane.

Returns the layeredPane.

Return this component's single JRootPane child.

The "contentPane" is the primary container for application
specific components.

The glassPane is always the first child of the rootPane
and the rootPanes layout manager ensures that it's always
as big as the rootPane.

A Container that manages the contentPane and in some cases a menu bar.

============ METHOD DETAIL ==========

- Method Detail

- getRootPane

```java
JRootPane
getRootPane()
```

Return this component's single JRootPane child. A conventional
implementation of this interface will have all of the other
methods indirect through this one. The rootPane has two
children: the glassPane and the layeredPane.

**Returns:** this components single JRootPane child.
**See Also:** JRootPane

- setContentPane

```java
void setContentPane​(
Container
contentPane)
```

The "contentPane" is the primary container for application
specific components. Applications should add children to
the contentPane, set its layout manager, and so on.

The contentPane may not be null.

Generally implemented with

getRootPane().setContentPane(contentPane);

**Parameters:** contentPane

- the Container to use for the contents of this
JRootPane
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is null
**See Also:** JRootPane.getContentPane()

,

getContentPane()

- getContentPane

```java
Container
getContentPane()
```

Returns the contentPane.

**Returns:** the value of the contentPane property.
**See Also:** setContentPane(java.awt.Container)

- setLayeredPane

```java
void setLayeredPane​(
JLayeredPane
layeredPane)
```

A Container that manages the contentPane and in some cases a menu bar.
The layeredPane can be used by descendants that want to add a child
to the RootPaneContainer that isn't layout managed. For example
an internal dialog or a drag and drop effect component.

The layeredPane may not be null.

Generally implemented with

```java
getRootPane().setLayeredPane(layeredPane);
```

**Parameters:** layeredPane

- the layered pane
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is null
**See Also:** getLayeredPane()

,

JRootPane.getLayeredPane()

- getLayeredPane

```java
JLayeredPane
getLayeredPane()
```

Returns the layeredPane.

**Returns:** the value of the layeredPane property.
**See Also:** setLayeredPane(javax.swing.JLayeredPane)

- setGlassPane

```java
void setGlassPane​(
Component
glassPane)
```

The glassPane is always the first child of the rootPane
and the rootPanes layout manager ensures that it's always
as big as the rootPane. By default it's transparent and
not visible. It can be used to temporarily grab all keyboard
and mouse input by adding listeners and then making it visible.
by default it's not visible.

The glassPane may not be null.

Generally implemented with

getRootPane().setGlassPane(glassPane);

**Parameters:** glassPane

- the glass pane
**See Also:** getGlassPane()

,

JRootPane.setGlassPane(java.awt.Component)

- getGlassPane

```java
Component
getGlassPane()
```

Returns the glassPane.

**Returns:** the value of the glassPane property.
**See Also:** setGlassPane(java.awt.Component)

Method Detail

- getRootPane

```java
JRootPane
getRootPane()
```

Return this component's single JRootPane child. A conventional
implementation of this interface will have all of the other
methods indirect through this one. The rootPane has two
children: the glassPane and the layeredPane.

**Returns:** this components single JRootPane child.
**See Also:** JRootPane

- setContentPane

```java
void setContentPane​(
Container
contentPane)
```

The "contentPane" is the primary container for application
specific components. Applications should add children to
the contentPane, set its layout manager, and so on.

The contentPane may not be null.

Generally implemented with

getRootPane().setContentPane(contentPane);

**Parameters:** contentPane

- the Container to use for the contents of this
JRootPane
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is null
**See Also:** JRootPane.getContentPane()

,

getContentPane()

- getContentPane

```java
Container
getContentPane()
```

Returns the contentPane.

**Returns:** the value of the contentPane property.
**See Also:** setContentPane(java.awt.Container)

- setLayeredPane

```java
void setLayeredPane​(
JLayeredPane
layeredPane)
```

A Container that manages the contentPane and in some cases a menu bar.
The layeredPane can be used by descendants that want to add a child
to the RootPaneContainer that isn't layout managed. For example
an internal dialog or a drag and drop effect component.

The layeredPane may not be null.

Generally implemented with

```java
getRootPane().setLayeredPane(layeredPane);
```

**Parameters:** layeredPane

- the layered pane
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is null
**See Also:** getLayeredPane()

,

JRootPane.getLayeredPane()

- getLayeredPane

```java
JLayeredPane
getLayeredPane()
```

Returns the layeredPane.

**Returns:** the value of the layeredPane property.
**See Also:** setLayeredPane(javax.swing.JLayeredPane)

- setGlassPane

```java
void setGlassPane​(
Component
glassPane)
```

The glassPane is always the first child of the rootPane
and the rootPanes layout manager ensures that it's always
as big as the rootPane. By default it's transparent and
not visible. It can be used to temporarily grab all keyboard
and mouse input by adding listeners and then making it visible.
by default it's not visible.

The glassPane may not be null.

Generally implemented with

getRootPane().setGlassPane(glassPane);

**Parameters:** glassPane

- the glass pane
**See Also:** getGlassPane()

,

JRootPane.setGlassPane(java.awt.Component)

- getGlassPane

```java
Component
getGlassPane()
```

Returns the glassPane.

**Returns:** the value of the glassPane property.
**See Also:** setGlassPane(java.awt.Component)

---

#### Method Detail

getRootPane

```java
JRootPane
getRootPane()
```

Return this component's single JRootPane child. A conventional
implementation of this interface will have all of the other
methods indirect through this one. The rootPane has two
children: the glassPane and the layeredPane.

**Returns:** this components single JRootPane child.
**See Also:** JRootPane

---

#### getRootPane

JRootPane

getRootPane()

Return this component's single JRootPane child. A conventional
implementation of this interface will have all of the other
methods indirect through this one. The rootPane has two
children: the glassPane and the layeredPane.

setContentPane

```java
void setContentPane​(
Container
contentPane)
```

The "contentPane" is the primary container for application
specific components. Applications should add children to
the contentPane, set its layout manager, and so on.

The contentPane may not be null.

Generally implemented with

getRootPane().setContentPane(contentPane);

**Parameters:** contentPane

- the Container to use for the contents of this
JRootPane
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the content pane parameter is null
**See Also:** JRootPane.getContentPane()

,

getContentPane()

---

#### setContentPane

void setContentPane​(

Container

contentPane)

The "contentPane" is the primary container for application
specific components. Applications should add children to
the contentPane, set its layout manager, and so on.

The contentPane may not be null.

Generally implemented with

getRootPane().setContentPane(contentPane);

The contentPane may not be null.

Generally implemented with

getRootPane().setContentPane(contentPane);

Generally implemented with

getRootPane().setContentPane(contentPane);

getContentPane

```java
Container
getContentPane()
```

Returns the contentPane.

**Returns:** the value of the contentPane property.
**See Also:** setContentPane(java.awt.Container)

---

#### getContentPane

Container

getContentPane()

Returns the contentPane.

setLayeredPane

```java
void setLayeredPane​(
JLayeredPane
layeredPane)
```

A Container that manages the contentPane and in some cases a menu bar.
The layeredPane can be used by descendants that want to add a child
to the RootPaneContainer that isn't layout managed. For example
an internal dialog or a drag and drop effect component.

The layeredPane may not be null.

Generally implemented with

```java
getRootPane().setLayeredPane(layeredPane);
```

**Parameters:** layeredPane

- the layered pane
**Throws:** IllegalComponentStateException

- (a runtime
exception) if the layered pane parameter is null
**See Also:** getLayeredPane()

,

JRootPane.getLayeredPane()

---

#### setLayeredPane

void setLayeredPane​(

JLayeredPane

layeredPane)

A Container that manages the contentPane and in some cases a menu bar.
The layeredPane can be used by descendants that want to add a child
to the RootPaneContainer that isn't layout managed. For example
an internal dialog or a drag and drop effect component.

The layeredPane may not be null.

Generally implemented with

```java
getRootPane().setLayeredPane(layeredPane);
```

The layeredPane may not be null.

Generally implemented with

```java
getRootPane().setLayeredPane(layeredPane);
```

Generally implemented with

```java
getRootPane().setLayeredPane(layeredPane);
```

getRootPane().setLayeredPane(layeredPane);

getLayeredPane

```java
JLayeredPane
getLayeredPane()
```

Returns the layeredPane.

**Returns:** the value of the layeredPane property.
**See Also:** setLayeredPane(javax.swing.JLayeredPane)

---

#### getLayeredPane

JLayeredPane

getLayeredPane()

Returns the layeredPane.

setGlassPane

```java
void setGlassPane​(
Component
glassPane)
```

The glassPane is always the first child of the rootPane
and the rootPanes layout manager ensures that it's always
as big as the rootPane. By default it's transparent and
not visible. It can be used to temporarily grab all keyboard
and mouse input by adding listeners and then making it visible.
by default it's not visible.

The glassPane may not be null.

Generally implemented with

getRootPane().setGlassPane(glassPane);

**Parameters:** glassPane

- the glass pane
**See Also:** getGlassPane()

,

JRootPane.setGlassPane(java.awt.Component)

---

#### setGlassPane

void setGlassPane​(

Component

glassPane)

The glassPane is always the first child of the rootPane
and the rootPanes layout manager ensures that it's always
as big as the rootPane. By default it's transparent and
not visible. It can be used to temporarily grab all keyboard
and mouse input by adding listeners and then making it visible.
by default it's not visible.

The glassPane may not be null.

Generally implemented with

getRootPane().setGlassPane(glassPane);

The glassPane may not be null.

Generally implemented with

getRootPane().setGlassPane(glassPane);

Generally implemented with

getRootPane().setGlassPane(glassPane);

getGlassPane

```java
Component
getGlassPane()
```

Returns the glassPane.

**Returns:** the value of the glassPane property.
**See Also:** setGlassPane(java.awt.Component)

---

#### getGlassPane

Component

getGlassPane()

Returns the glassPane.

---

