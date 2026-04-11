# Interface DesktopManager

**Source:** `java.desktop\javax\swing\DesktopManager.html`

### Class Description

```java
public interface
DesktopManager
```

DesktopManager objects are owned by a JDesktopPane object. They are responsible
for implementing L&F specific behaviors for the JDesktopPane. JInternalFrame
implementations should delegate specific behaviors to the DesktopManager. For
instance, if a JInternalFrame was asked to iconify, it should try:

```java
getDesktopPane().getDesktopManager().iconifyFrame(frame);
```

This delegation allows each L&F to provide custom behaviors for desktop-specific
actions. (For example, how and where the internal frame's icon would appear.)

This class provides a policy for the various JInternalFrame methods, it is not
meant to be called directly rather the various JInternalFrame methods will call
into the DesktopManager.

**All Known Implementing Classes:** DefaultDesktopManager

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void openFrame​(
JInternalFrame
f)

If possible, display this frame in an appropriate location.
Normally, this is not called, as the creator of the JInternalFrame
will add the frame to the appropriate parent.

**Parameters:**
- f

- the

JInternalFrame

to be displayed

---

#### void closeFrame​(
JInternalFrame
f)

Generally, this call should remove the frame from its parent.

**Parameters:**
- f

- the

JInternalFrame

to be removed

---

#### void maximizeFrame​(
JInternalFrame
f)

Generally, the frame should be resized to match its parents bounds.

**Parameters:**
- f

- the

JInternalFrame

to be resized

---

#### void minimizeFrame​(
JInternalFrame
f)

Generally, this indicates that the frame should be restored to its
size and position prior to a maximizeFrame() call.

**Parameters:**
- f

- the

JInternalFrame

to be restored

---

#### void iconifyFrame​(
JInternalFrame
f)

Generally, remove this frame from its parent and add an iconic representation.

**Parameters:**
- f

- the

JInternalFrame

to be iconified

---

#### void deiconifyFrame​(
JInternalFrame
f)

Generally, remove any iconic representation that is present and restore the
frame to it's original size and location.

**Parameters:**
- f

- the

JInternalFrame

to be de-iconified

---

#### void activateFrame​(
JInternalFrame
f)

Generally, indicate that this frame has focus. This is usually called after
the JInternalFrame's IS_SELECTED_PROPERTY has been set to true.

**Parameters:**
- f

- the

JInternalFrame

to be activated

---

#### void deactivateFrame​(
JInternalFrame
f)

Generally, indicate that this frame has lost focus. This is usually called
after the JInternalFrame's IS_SELECTED_PROPERTY has been set to false.

**Parameters:**
- f

- the

JInternalFrame

to be deactivated

---

#### void beginDraggingFrame​(
JComponent
f)

This method is normally called when the user has indicated that
they will begin dragging a component around. This method should be called
prior to any dragFrame() calls to allow the DesktopManager to prepare any
necessary state. Normally

f

will be a JInternalFrame.

**Parameters:**
- f

- the

JComponent

being dragged

---

#### void dragFrame​(
JComponent
f,
int newX,
int newY)

The user has moved the frame. Calls to this method will be preceded by calls
to beginDraggingFrame().
Normally

f

will be a JInternalFrame.

**Parameters:**
- f

- the

JComponent

being dragged
- newX

- the new x-coordinate
- newY

- the new y-coordinate

---

#### void endDraggingFrame​(
JComponent
f)

This method signals the end of the dragging session. Any state maintained by
the DesktopManager can be removed here. Normally

f

will be a JInternalFrame.

**Parameters:**
- f

- the

JComponent

being dragged

---

#### void beginResizingFrame​(
JComponent
f,
int direction)

This method is normally called when the user has indicated that
they will begin resizing the frame. This method should be called
prior to any resizeFrame() calls to allow the DesktopManager to prepare any
necessary state. Normally

f

will be a JInternalFrame.

**Parameters:**
- f

- the

JComponent

being resized
- direction

- the direction

---

#### void resizeFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)

The user has resized the component. Calls to this method will be preceded by calls
to beginResizingFrame().
Normally

f

will be a JInternalFrame.

**Parameters:**
- f

- the

JComponent

being resized
- newX

- the new x-coordinate
- newY

- the new y-coordinate
- newWidth

- the new width
- newHeight

- the new height

---

#### void endResizingFrame​(
JComponent
f)

This method signals the end of the resize session. Any state maintained by
the DesktopManager can be removed here. Normally

f

will be a JInternalFrame.

**Parameters:**
- f

- the

JComponent

being resized

---

#### void setBoundsForFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)

This is a primitive reshape method.

**Parameters:**
- f

- the

JComponent

being moved or resized
- newX

- the new x-coordinate
- newY

- the new y-coordinate
- newWidth

- the new width
- newHeight

- the new height

---

### Additional Sections

#### Interface DesktopManager

**All Known Implementing Classes:** DefaultDesktopManager

```java
public interface
DesktopManager
```

DesktopManager objects are owned by a JDesktopPane object. They are responsible
for implementing L&F specific behaviors for the JDesktopPane. JInternalFrame
implementations should delegate specific behaviors to the DesktopManager. For
instance, if a JInternalFrame was asked to iconify, it should try:

```java
getDesktopPane().getDesktopManager().iconifyFrame(frame);
```

This delegation allows each L&F to provide custom behaviors for desktop-specific
actions. (For example, how and where the internal frame's icon would appear.)

This class provides a policy for the various JInternalFrame methods, it is not
meant to be called directly rather the various JInternalFrame methods will call
into the DesktopManager.

**Since:** 1.2
**See Also:** JDesktopPane

,

JInternalFrame

,

JInternalFrame.JDesktopIcon

public interface

DesktopManager

DesktopManager objects are owned by a JDesktopPane object. They are responsible
for implementing L&F specific behaviors for the JDesktopPane. JInternalFrame
implementations should delegate specific behaviors to the DesktopManager. For
instance, if a JInternalFrame was asked to iconify, it should try:

```java
getDesktopPane().getDesktopManager().iconifyFrame(frame);
```

This delegation allows each L&F to provide custom behaviors for desktop-specific
actions. (For example, how and where the internal frame's icon would appear.)

This class provides a policy for the various JInternalFrame methods, it is not
meant to be called directly rather the various JInternalFrame methods will call
into the DesktopManager.

getDesktopPane().getDesktopManager().iconifyFrame(frame);

This class provides a policy for the various JInternalFrame methods, it is not
meant to be called directly rather the various JInternalFrame methods will call
into the DesktopManager.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

activateFrame

​(

JInternalFrame

f)

Generally, indicate that this frame has focus.

void

beginDraggingFrame

​(

JComponent

f)

This method is normally called when the user has indicated that
they will begin dragging a component around.

void

beginResizingFrame

​(

JComponent

f,
int direction)

This method is normally called when the user has indicated that
they will begin resizing the frame.

void

closeFrame

​(

JInternalFrame

f)

Generally, this call should remove the frame from its parent.

void

deactivateFrame

​(

JInternalFrame

f)

Generally, indicate that this frame has lost focus.

void

deiconifyFrame

​(

JInternalFrame

f)

Generally, remove any iconic representation that is present and restore the
frame to it's original size and location.

void

dragFrame

​(

JComponent

f,
int newX,
int newY)

The user has moved the frame.

void

endDraggingFrame

​(

JComponent

f)

This method signals the end of the dragging session.

void

endResizingFrame

​(

JComponent

f)

This method signals the end of the resize session.

void

iconifyFrame

​(

JInternalFrame

f)

Generally, remove this frame from its parent and add an iconic representation.

void

maximizeFrame

​(

JInternalFrame

f)

Generally, the frame should be resized to match its parents bounds.

void

minimizeFrame

​(

JInternalFrame

f)

Generally, this indicates that the frame should be restored to its
size and position prior to a maximizeFrame() call.

void

openFrame

​(

JInternalFrame

f)

If possible, display this frame in an appropriate location.

void

resizeFrame

​(

JComponent

f,
int newX,
int newY,
int newWidth,
int newHeight)

The user has resized the component.

void

setBoundsForFrame

​(

JComponent

f,
int newX,
int newY,
int newWidth,
int newHeight)

This is a primitive reshape method.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

activateFrame

​(

JInternalFrame

f)

Generally, indicate that this frame has focus.

void

beginDraggingFrame

​(

JComponent

f)

This method is normally called when the user has indicated that
they will begin dragging a component around.

void

beginResizingFrame

​(

JComponent

f,
int direction)

This method is normally called when the user has indicated that
they will begin resizing the frame.

void

closeFrame

​(

JInternalFrame

f)

Generally, this call should remove the frame from its parent.

void

deactivateFrame

​(

JInternalFrame

f)

Generally, indicate that this frame has lost focus.

void

deiconifyFrame

​(

JInternalFrame

f)

Generally, remove any iconic representation that is present and restore the
frame to it's original size and location.

void

dragFrame

​(

JComponent

f,
int newX,
int newY)

The user has moved the frame.

void

endDraggingFrame

​(

JComponent

f)

This method signals the end of the dragging session.

void

endResizingFrame

​(

JComponent

f)

This method signals the end of the resize session.

void

iconifyFrame

​(

JInternalFrame

f)

Generally, remove this frame from its parent and add an iconic representation.

void

maximizeFrame

​(

JInternalFrame

f)

Generally, the frame should be resized to match its parents bounds.

void

minimizeFrame

​(

JInternalFrame

f)

Generally, this indicates that the frame should be restored to its
size and position prior to a maximizeFrame() call.

void

openFrame

​(

JInternalFrame

f)

If possible, display this frame in an appropriate location.

void

resizeFrame

​(

JComponent

f,
int newX,
int newY,
int newWidth,
int newHeight)

The user has resized the component.

void

setBoundsForFrame

​(

JComponent

f,
int newX,
int newY,
int newWidth,
int newHeight)

This is a primitive reshape method.

---

#### Method Summary

Generally, indicate that this frame has focus.

This method is normally called when the user has indicated that
they will begin dragging a component around.

This method is normally called when the user has indicated that
they will begin resizing the frame.

Generally, this call should remove the frame from its parent.

Generally, indicate that this frame has lost focus.

Generally, remove any iconic representation that is present and restore the
frame to it's original size and location.

The user has moved the frame.

This method signals the end of the dragging session.

This method signals the end of the resize session.

Generally, remove this frame from its parent and add an iconic representation.

Generally, the frame should be resized to match its parents bounds.

Generally, this indicates that the frame should be restored to its
size and position prior to a maximizeFrame() call.

If possible, display this frame in an appropriate location.

The user has resized the component.

This is a primitive reshape method.

============ METHOD DETAIL ==========

- Method Detail

- openFrame

```java
void openFrame​(
JInternalFrame
f)
```

If possible, display this frame in an appropriate location.
Normally, this is not called, as the creator of the JInternalFrame
will add the frame to the appropriate parent.

**Parameters:** f

- the

JInternalFrame

to be displayed

- closeFrame

```java
void closeFrame​(
JInternalFrame
f)
```

Generally, this call should remove the frame from its parent.

**Parameters:** f

- the

JInternalFrame

to be removed

- maximizeFrame

```java
void maximizeFrame​(
JInternalFrame
f)
```

Generally, the frame should be resized to match its parents bounds.

**Parameters:** f

- the

JInternalFrame

to be resized

- minimizeFrame

```java
void minimizeFrame​(
JInternalFrame
f)
```

Generally, this indicates that the frame should be restored to its
size and position prior to a maximizeFrame() call.

**Parameters:** f

- the

JInternalFrame

to be restored

- iconifyFrame

```java
void iconifyFrame​(
JInternalFrame
f)
```

Generally, remove this frame from its parent and add an iconic representation.

**Parameters:** f

- the

JInternalFrame

to be iconified

- deiconifyFrame

```java
void deiconifyFrame​(
JInternalFrame
f)
```

Generally, remove any iconic representation that is present and restore the
frame to it's original size and location.

**Parameters:** f

- the

JInternalFrame

to be de-iconified

- activateFrame

```java
void activateFrame​(
JInternalFrame
f)
```

Generally, indicate that this frame has focus. This is usually called after
the JInternalFrame's IS_SELECTED_PROPERTY has been set to true.

**Parameters:** f

- the

JInternalFrame

to be activated

- deactivateFrame

```java
void deactivateFrame​(
JInternalFrame
f)
```

Generally, indicate that this frame has lost focus. This is usually called
after the JInternalFrame's IS_SELECTED_PROPERTY has been set to false.

**Parameters:** f

- the

JInternalFrame

to be deactivated

- beginDraggingFrame

```java
void beginDraggingFrame​(
JComponent
f)
```

This method is normally called when the user has indicated that
they will begin dragging a component around. This method should be called
prior to any dragFrame() calls to allow the DesktopManager to prepare any
necessary state. Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being dragged

- dragFrame

```java
void dragFrame​(
JComponent
f,
int newX,
int newY)
```

The user has moved the frame. Calls to this method will be preceded by calls
to beginDraggingFrame().
Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being dragged
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate

- endDraggingFrame

```java
void endDraggingFrame​(
JComponent
f)
```

This method signals the end of the dragging session. Any state maintained by
the DesktopManager can be removed here. Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being dragged

- beginResizingFrame

```java
void beginResizingFrame​(
JComponent
f,
int direction)
```

This method is normally called when the user has indicated that
they will begin resizing the frame. This method should be called
prior to any resizeFrame() calls to allow the DesktopManager to prepare any
necessary state. Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being resized
**Parameters:** direction

- the direction

- resizeFrame

```java
void resizeFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)
```

The user has resized the component. Calls to this method will be preceded by calls
to beginResizingFrame().
Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being resized
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate
**Parameters:** newWidth

- the new width
**Parameters:** newHeight

- the new height

- endResizingFrame

```java
void endResizingFrame​(
JComponent
f)
```

This method signals the end of the resize session. Any state maintained by
the DesktopManager can be removed here. Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being resized

- setBoundsForFrame

```java
void setBoundsForFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)
```

This is a primitive reshape method.

**Parameters:** f

- the

JComponent

being moved or resized
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate
**Parameters:** newWidth

- the new width
**Parameters:** newHeight

- the new height

Method Detail

- openFrame

```java
void openFrame​(
JInternalFrame
f)
```

If possible, display this frame in an appropriate location.
Normally, this is not called, as the creator of the JInternalFrame
will add the frame to the appropriate parent.

**Parameters:** f

- the

JInternalFrame

to be displayed

- closeFrame

```java
void closeFrame​(
JInternalFrame
f)
```

Generally, this call should remove the frame from its parent.

**Parameters:** f

- the

JInternalFrame

to be removed

- maximizeFrame

```java
void maximizeFrame​(
JInternalFrame
f)
```

Generally, the frame should be resized to match its parents bounds.

**Parameters:** f

- the

JInternalFrame

to be resized

- minimizeFrame

```java
void minimizeFrame​(
JInternalFrame
f)
```

Generally, this indicates that the frame should be restored to its
size and position prior to a maximizeFrame() call.

**Parameters:** f

- the

JInternalFrame

to be restored

- iconifyFrame

```java
void iconifyFrame​(
JInternalFrame
f)
```

Generally, remove this frame from its parent and add an iconic representation.

**Parameters:** f

- the

JInternalFrame

to be iconified

- deiconifyFrame

```java
void deiconifyFrame​(
JInternalFrame
f)
```

Generally, remove any iconic representation that is present and restore the
frame to it's original size and location.

**Parameters:** f

- the

JInternalFrame

to be de-iconified

- activateFrame

```java
void activateFrame​(
JInternalFrame
f)
```

Generally, indicate that this frame has focus. This is usually called after
the JInternalFrame's IS_SELECTED_PROPERTY has been set to true.

**Parameters:** f

- the

JInternalFrame

to be activated

- deactivateFrame

```java
void deactivateFrame​(
JInternalFrame
f)
```

Generally, indicate that this frame has lost focus. This is usually called
after the JInternalFrame's IS_SELECTED_PROPERTY has been set to false.

**Parameters:** f

- the

JInternalFrame

to be deactivated

- beginDraggingFrame

```java
void beginDraggingFrame​(
JComponent
f)
```

This method is normally called when the user has indicated that
they will begin dragging a component around. This method should be called
prior to any dragFrame() calls to allow the DesktopManager to prepare any
necessary state. Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being dragged

- dragFrame

```java
void dragFrame​(
JComponent
f,
int newX,
int newY)
```

The user has moved the frame. Calls to this method will be preceded by calls
to beginDraggingFrame().
Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being dragged
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate

- endDraggingFrame

```java
void endDraggingFrame​(
JComponent
f)
```

This method signals the end of the dragging session. Any state maintained by
the DesktopManager can be removed here. Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being dragged

- beginResizingFrame

```java
void beginResizingFrame​(
JComponent
f,
int direction)
```

This method is normally called when the user has indicated that
they will begin resizing the frame. This method should be called
prior to any resizeFrame() calls to allow the DesktopManager to prepare any
necessary state. Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being resized
**Parameters:** direction

- the direction

- resizeFrame

```java
void resizeFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)
```

The user has resized the component. Calls to this method will be preceded by calls
to beginResizingFrame().
Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being resized
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate
**Parameters:** newWidth

- the new width
**Parameters:** newHeight

- the new height

- endResizingFrame

```java
void endResizingFrame​(
JComponent
f)
```

This method signals the end of the resize session. Any state maintained by
the DesktopManager can be removed here. Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being resized

- setBoundsForFrame

```java
void setBoundsForFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)
```

This is a primitive reshape method.

**Parameters:** f

- the

JComponent

being moved or resized
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate
**Parameters:** newWidth

- the new width
**Parameters:** newHeight

- the new height

---

#### Method Detail

openFrame

```java
void openFrame​(
JInternalFrame
f)
```

If possible, display this frame in an appropriate location.
Normally, this is not called, as the creator of the JInternalFrame
will add the frame to the appropriate parent.

**Parameters:** f

- the

JInternalFrame

to be displayed

---

#### openFrame

void openFrame​(

JInternalFrame

f)

If possible, display this frame in an appropriate location.
Normally, this is not called, as the creator of the JInternalFrame
will add the frame to the appropriate parent.

closeFrame

```java
void closeFrame​(
JInternalFrame
f)
```

Generally, this call should remove the frame from its parent.

**Parameters:** f

- the

JInternalFrame

to be removed

---

#### closeFrame

void closeFrame​(

JInternalFrame

f)

Generally, this call should remove the frame from its parent.

maximizeFrame

```java
void maximizeFrame​(
JInternalFrame
f)
```

Generally, the frame should be resized to match its parents bounds.

**Parameters:** f

- the

JInternalFrame

to be resized

---

#### maximizeFrame

void maximizeFrame​(

JInternalFrame

f)

Generally, the frame should be resized to match its parents bounds.

minimizeFrame

```java
void minimizeFrame​(
JInternalFrame
f)
```

Generally, this indicates that the frame should be restored to its
size and position prior to a maximizeFrame() call.

**Parameters:** f

- the

JInternalFrame

to be restored

---

#### minimizeFrame

void minimizeFrame​(

JInternalFrame

f)

Generally, this indicates that the frame should be restored to its
size and position prior to a maximizeFrame() call.

iconifyFrame

```java
void iconifyFrame​(
JInternalFrame
f)
```

Generally, remove this frame from its parent and add an iconic representation.

**Parameters:** f

- the

JInternalFrame

to be iconified

---

#### iconifyFrame

void iconifyFrame​(

JInternalFrame

f)

Generally, remove this frame from its parent and add an iconic representation.

deiconifyFrame

```java
void deiconifyFrame​(
JInternalFrame
f)
```

Generally, remove any iconic representation that is present and restore the
frame to it's original size and location.

**Parameters:** f

- the

JInternalFrame

to be de-iconified

---

#### deiconifyFrame

void deiconifyFrame​(

JInternalFrame

f)

Generally, remove any iconic representation that is present and restore the
frame to it's original size and location.

activateFrame

```java
void activateFrame​(
JInternalFrame
f)
```

Generally, indicate that this frame has focus. This is usually called after
the JInternalFrame's IS_SELECTED_PROPERTY has been set to true.

**Parameters:** f

- the

JInternalFrame

to be activated

---

#### activateFrame

void activateFrame​(

JInternalFrame

f)

Generally, indicate that this frame has focus. This is usually called after
the JInternalFrame's IS_SELECTED_PROPERTY has been set to true.

deactivateFrame

```java
void deactivateFrame​(
JInternalFrame
f)
```

Generally, indicate that this frame has lost focus. This is usually called
after the JInternalFrame's IS_SELECTED_PROPERTY has been set to false.

**Parameters:** f

- the

JInternalFrame

to be deactivated

---

#### deactivateFrame

void deactivateFrame​(

JInternalFrame

f)

Generally, indicate that this frame has lost focus. This is usually called
after the JInternalFrame's IS_SELECTED_PROPERTY has been set to false.

beginDraggingFrame

```java
void beginDraggingFrame​(
JComponent
f)
```

This method is normally called when the user has indicated that
they will begin dragging a component around. This method should be called
prior to any dragFrame() calls to allow the DesktopManager to prepare any
necessary state. Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being dragged

---

#### beginDraggingFrame

void beginDraggingFrame​(

JComponent

f)

This method is normally called when the user has indicated that
they will begin dragging a component around. This method should be called
prior to any dragFrame() calls to allow the DesktopManager to prepare any
necessary state. Normally

f

will be a JInternalFrame.

dragFrame

```java
void dragFrame​(
JComponent
f,
int newX,
int newY)
```

The user has moved the frame. Calls to this method will be preceded by calls
to beginDraggingFrame().
Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being dragged
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate

---

#### dragFrame

void dragFrame​(

JComponent

f,
int newX,
int newY)

The user has moved the frame. Calls to this method will be preceded by calls
to beginDraggingFrame().
Normally

f

will be a JInternalFrame.

endDraggingFrame

```java
void endDraggingFrame​(
JComponent
f)
```

This method signals the end of the dragging session. Any state maintained by
the DesktopManager can be removed here. Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being dragged

---

#### endDraggingFrame

void endDraggingFrame​(

JComponent

f)

This method signals the end of the dragging session. Any state maintained by
the DesktopManager can be removed here. Normally

f

will be a JInternalFrame.

beginResizingFrame

```java
void beginResizingFrame​(
JComponent
f,
int direction)
```

This method is normally called when the user has indicated that
they will begin resizing the frame. This method should be called
prior to any resizeFrame() calls to allow the DesktopManager to prepare any
necessary state. Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being resized
**Parameters:** direction

- the direction

---

#### beginResizingFrame

void beginResizingFrame​(

JComponent

f,
int direction)

This method is normally called when the user has indicated that
they will begin resizing the frame. This method should be called
prior to any resizeFrame() calls to allow the DesktopManager to prepare any
necessary state. Normally

f

will be a JInternalFrame.

resizeFrame

```java
void resizeFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)
```

The user has resized the component. Calls to this method will be preceded by calls
to beginResizingFrame().
Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being resized
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate
**Parameters:** newWidth

- the new width
**Parameters:** newHeight

- the new height

---

#### resizeFrame

void resizeFrame​(

JComponent

f,
int newX,
int newY,
int newWidth,
int newHeight)

The user has resized the component. Calls to this method will be preceded by calls
to beginResizingFrame().
Normally

f

will be a JInternalFrame.

endResizingFrame

```java
void endResizingFrame​(
JComponent
f)
```

This method signals the end of the resize session. Any state maintained by
the DesktopManager can be removed here. Normally

f

will be a JInternalFrame.

**Parameters:** f

- the

JComponent

being resized

---

#### endResizingFrame

void endResizingFrame​(

JComponent

f)

This method signals the end of the resize session. Any state maintained by
the DesktopManager can be removed here. Normally

f

will be a JInternalFrame.

setBoundsForFrame

```java
void setBoundsForFrame​(
JComponent
f,
int newX,
int newY,
int newWidth,
int newHeight)
```

This is a primitive reshape method.

**Parameters:** f

- the

JComponent

being moved or resized
**Parameters:** newX

- the new x-coordinate
**Parameters:** newY

- the new y-coordinate
**Parameters:** newWidth

- the new width
**Parameters:** newHeight

- the new height

---

#### setBoundsForFrame

void setBoundsForFrame​(

JComponent

f,
int newX,
int newY,
int newWidth,
int newHeight)

This is a primitive reshape method.

---

