# Class DefaultCaret

**Source:** `java.desktop\javax\swing\text\DefaultCaret.html`

### Class Description

```java
public class
DefaultCaret

extends
Rectangle

implements
Caret
,
FocusListener
,
MouseListener
,
MouseMotionListener
```

A default implementation of Caret. The caret is rendered as
a vertical line in the color specified by the CaretColor property
of the associated JTextComponent. It can blink at the rate specified
by the BlinkRate property.

This implementation expects two sources of asynchronous notification.
The timer thread fires asynchronously, and causes the caret to simply
repaint the most recent bounding box. The caret also tracks change
as the document is modified. Typically this will happen on the
event dispatch thread as a result of some mouse or keyboard event.
The caret behavior on both synchronous and asynchronous documents updates
is controlled by

UpdatePolicy

property. The repaint of the
new caret location will occur on the event thread in any case, as calls to

modelToView

are only safe on the event thread.

The caret acts as a mouse and focus listener on the text component
it has been installed in, and defines the caret semantics based upon
those events. The listener methods can be reimplemented to change the
semantics.
By default, the first mouse button will be used to set focus and caret
position. Dragging the mouse pointer with the first mouse button will
sweep out a selection that is contiguous in the model. If the associated
text component is editable, the caret will become visible when focus
is gained, and invisible when focus is lost.

The Highlighter bound to the associated text component is used to
render the selection by default.
Selection appearance can be customized by supplying a
painter to use for the highlights. By default a painter is used that
will render a solid color as specified in the associated text component
in the

SelectionColor

property. This can easily be changed
by reimplementing the

getSelectionPainter

method.

A customized caret appearance can be achieved by reimplementing
the paint method. If the paint method is changed, the damage method
should also be reimplemented to cause a repaint for the area needed
to render the caret. The caret extends the Rectangle class which
is used to hold the bounding box for where the caret was last rendered.
This enables the caret to repaint in a thread-safe manner when the
caret moves without making a call to modelToView which is unstable
between model updates and view repair (i.e. the order of delivery
to DocumentListeners is not guaranteed).

The magic caret position is set to null when the caret position changes.
A timer is used to determine the new location (after the caret change).
When the timer fires, if the magic caret position is still null it is
reset to the current caret position. Any actions that change
the caret position and want the magic caret position to remain the
same, must remember the magic caret position, change the cursor, and
then set the magic caret position to its original value. This has the
benefit that only actions that want the magic caret position to persist
(such as open/down) need to know about it.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** FocusListener

,

MouseListener

,

MouseMotionListener

,

Shape

,

Serializable

,

Cloneable

,

EventListener

,

Caret

---

### Field Details

#### public static final int UPDATE_WHEN_ON_EDT

Indicates that the caret position is to be updated only when
document changes are performed on the Event Dispatching Thread.

**See Also:**
- setUpdatePolicy(int)

,

getUpdatePolicy()

,

Constant Field Values

**Since:**
- 1.5

---

#### public static final int NEVER_UPDATE

Indicates that the caret should remain at the same
absolute position in the document regardless of any document
updates, except when the document length becomes less than
the current caret position due to removal. In that case the caret
position is adjusted to the end of the document.

**See Also:**
- setUpdatePolicy(int)

,

getUpdatePolicy()

,

Constant Field Values

**Since:**
- 1.5

---

#### public static final int ALWAYS_UPDATE

Indicates that the caret position is to be

always

updated accordingly to the document changes regardless whether
the document updates are performed on the Event Dispatching Thread
or not.

**See Also:**
- setUpdatePolicy(int)

,

getUpdatePolicy()

,

Constant Field Values

**Since:**
- 1.5

---

#### protected
EventListenerList
listenerList

The event listener list.

---

#### protected transient
ChangeEvent
changeEvent

The change event for the model.
Only one ChangeEvent is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

---

### Constructor Details

#### public DefaultCaret()

Constructs a default caret.

---

### Method Details

#### public void setUpdatePolicy​(int policy)

Sets the caret movement policy on the document updates. Normally
the caret updates its absolute position within the document on
insertions occurred before or at the caret position and
on removals before the caret position. 'Absolute position'
means here the position relative to the start of the document.
For example if
a character is typed within editable text component it is inserted
at the caret position and the caret moves to the next absolute
position within the document due to insertion and if

BACKSPACE

is typed then caret decreases its absolute
position due to removal of a character before it. Sometimes
it may be useful to turn off the caret position updates so that
the caret stays at the same absolute position within the
document position regardless of any document updates.

The following update policies are allowed:

- NEVER_UPDATE

: the caret stays at the same
absolute position in the document regardless of any document
updates, except when document length becomes less than
the current caret position due to removal. In that case caret
position is adjusted to the end of the document.
The caret doesn't try to keep itself visible by scrolling
the associated view when using this policy.
- ALWAYS_UPDATE

: the caret always tracks document
changes. For regular changes it increases its position
if an insertion occurs before or at its current position,
and decreases position if a removal occurs before
its current position. For undo/redo updates it is always
moved to the position where update occurred. The caret
also tries to keep itself visible by calling

adjustVisibility

method.
- UPDATE_WHEN_ON_EDT

: acts like

ALWAYS_UPDATE

if the document updates are performed on the Event Dispatching Thread
and like

NEVER_UPDATE

if updates are performed on
other thread.

The default property value is

UPDATE_WHEN_ON_EDT

.

**Parameters:**
- policy

- one of the following values :

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE

**Throws:**
- IllegalArgumentException

- if invalid value is passed

**See Also:**
- getUpdatePolicy()

,

adjustVisibility(java.awt.Rectangle)

,

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE

**Since:**
- 1.5

---

#### public int getUpdatePolicy()

Gets the caret movement policy on document updates.

**Returns:**
- one of the following values :

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE

**See Also:**
- setUpdatePolicy(int)

,

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE

**Since:**
- 1.5

---

#### protected final
JTextComponent
getComponent()

Gets the text editor component that this caret is
is bound to.

**Returns:**
- the component

---

#### protected final void repaint()

Cause the caret to be painted. The repaint
area is the bounding box of the caret (i.e.
the caret rectangle or

this

).

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

---

#### protected void damage​(
Rectangle
r)

Damages the area surrounding the caret to cause
it to be repainted in a new location. If paint()
is reimplemented, this method should also be
reimplemented. This method should update the
caret bounds (x, y, width, and height).

**Parameters:**
- r

- the current location of the caret

**See Also:**
- paint(java.awt.Graphics)

---

#### protected void adjustVisibility​(
Rectangle
nloc)

Scrolls the associated view (if necessary) to make
the caret visible. Since how this should be done
is somewhat of a policy, this method can be
reimplemented to change the behavior. By default
the scrollRectToVisible method is called on the
associated component.

**Parameters:**
- nloc

- the new position to scroll to

---

#### protected
Highlighter.HighlightPainter
getSelectionPainter()

Gets the painter for the Highlighter.

**Returns:**
- the painter

---

#### protected void positionCaret​(
MouseEvent
e)

Tries to set the position of the caret from
the coordinates of a mouse event, using viewToModel().

**Parameters:**
- e

- the mouse event

---

#### protected void moveCaret​(
MouseEvent
e)

Tries to move the position of the caret from
the coordinates of a mouse event, using viewToModel().
This will cause a selection if the dot and mark
are different.

**Parameters:**
- e

- the mouse event

---

#### public void focusGained​(
FocusEvent
e)

Called when the component containing the caret gains
focus. This is implemented to set the caret to visible
if the component is editable.

**Specified by:**
- focusGained

in interface

FocusListener

**Parameters:**
- e

- the focus event

**See Also:**
- FocusListener.focusGained(java.awt.event.FocusEvent)

---

#### public void focusLost​(
FocusEvent
e)

Called when the component containing the caret loses
focus. This is implemented to set the caret to visibility
to false.

**Specified by:**
- focusLost

in interface

FocusListener

**Parameters:**
- e

- the focus event

**See Also:**
- FocusListener.focusLost(java.awt.event.FocusEvent)

---

#### public void mouseClicked​(
MouseEvent
e)

Called when the mouse is clicked. If the click was generated
from button1, a double click selects a word,
and a triple click the current line.

**Specified by:**
- mouseClicked

in interface

MouseListener

**Parameters:**
- e

- the mouse event

**See Also:**
- MouseListener.mouseClicked(java.awt.event.MouseEvent)

---

#### public void mousePressed​(
MouseEvent
e)

If button 1 is pressed, this is implemented to
request focus on the associated text component,
and to set the caret position. If the shift key is held down,
the caret will be moved, potentially resulting in a selection,
otherwise the
caret position will be set to the new location. If the component
is not enabled, there will be no request for focus.

**Specified by:**
- mousePressed

in interface

MouseListener

**Parameters:**
- e

- the mouse event

**See Also:**
- MouseListener.mousePressed(java.awt.event.MouseEvent)

---

#### public void mouseReleased​(
MouseEvent
e)

Called when the mouse is released.

**Specified by:**
- mouseReleased

in interface

MouseListener

**Parameters:**
- e

- the mouse event

**See Also:**
- MouseListener.mouseReleased(java.awt.event.MouseEvent)

---

#### public void mouseEntered​(
MouseEvent
e)

Called when the mouse enters a region.

**Specified by:**
- mouseEntered

in interface

MouseListener

**Parameters:**
- e

- the mouse event

**See Also:**
- MouseListener.mouseEntered(java.awt.event.MouseEvent)

---

#### public void mouseExited​(
MouseEvent
e)

Called when the mouse exits a region.

**Specified by:**
- mouseExited

in interface

MouseListener

**Parameters:**
- e

- the mouse event

**See Also:**
- MouseListener.mouseExited(java.awt.event.MouseEvent)

---

#### public void mouseDragged​(
MouseEvent
e)

Moves the caret position
according to the mouse pointer's current
location. This effectively extends the
selection. By default, this is only done
for mouse button 1.

**Specified by:**
- mouseDragged

in interface

MouseMotionListener

**Parameters:**
- e

- the mouse event

**See Also:**
- MouseMotionListener.mouseDragged(java.awt.event.MouseEvent)

---

#### public void mouseMoved​(
MouseEvent
e)

Called when the mouse is moved.

**Specified by:**
- mouseMoved

in interface

MouseMotionListener

**Parameters:**
- e

- the mouse event

**See Also:**
- MouseMotionListener.mouseMoved(java.awt.event.MouseEvent)

---

#### public void paint​(
Graphics
g)

Renders the caret as a vertical line. If this is reimplemented
the damage method should also be reimplemented as it assumes the
shape of the caret is a vertical line. Sets the caret color to
the value returned by getCaretColor().

If there are multiple text directions present in the associated
document, a flag indicating the caret bias will be rendered.
This will occur only if the associated document is a subclass
of AbstractDocument and there are multiple bidi levels present
in the bidi element structure (i.e. the text has multiple
directions associated with it).

**Specified by:**
- paint

in interface

Caret

**Parameters:**
- g

- the graphics context

**See Also:**
- damage(java.awt.Rectangle)

---

#### public void install​(
JTextComponent
c)

Called when the UI is being installed into the
interface of a JTextComponent. This can be used
to gain access to the model that is being navigated
by the implementation of this interface. Sets the dot
and mark to 0, and establishes document, property change,
focus, mouse, and mouse motion listeners.

**Specified by:**
- install

in interface

Caret

**Parameters:**
- c

- the component

**See Also:**
- Caret.install(javax.swing.text.JTextComponent)

---

#### public void deinstall​(
JTextComponent
c)

Called when the UI is being removed from the
interface of a JTextComponent. This is used to
unregister any listeners that were attached.

**Specified by:**
- deinstall

in interface

Caret

**Parameters:**
- c

- the component

**See Also:**
- Caret.deinstall(javax.swing.text.JTextComponent)

---

#### public void addChangeListener​(
ChangeListener
l)

Adds a listener to track whenever the caret position has
been changed.

**Specified by:**
- addChangeListener

in interface

Caret

**Parameters:**
- l

- the listener

**See Also:**
- Caret.addChangeListener(javax.swing.event.ChangeListener)

---

#### public void removeChangeListener​(
ChangeListener
l)

Removes a listener that was tracking caret position changes.

**Specified by:**
- removeChangeListener

in interface

Caret

**Parameters:**
- l

- the listener

**See Also:**
- Caret.removeChangeListener(javax.swing.event.ChangeListener)

---

#### public
ChangeListener
[] getChangeListeners()

Returns an array of all the change listeners
registered on this caret.

**Returns:**
- all of this caret's

ChangeListener

s
or an empty
array if no change listeners are currently registered

**See Also:**
- addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

**Since:**
- 1.4

---

#### protected void fireStateChanged()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method. The listener list is processed last to first.

**See Also:**
- EventListenerList

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this caret.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a

DefaultCaret

c

for its change listeners with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(c.getListeners(ChangeListener.class));
```

If no such listeners exist, this method returns an empty array.

**Parameters:**
- listenerType

- the type of listeners requested

**Returns:**
- an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener

**See Also:**
- getChangeListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the listener type

---

#### public void setSelectionVisible​(boolean vis)

Changes the selection visibility.

**Specified by:**
- setSelectionVisible

in interface

Caret

**Parameters:**
- vis

- the new visibility

---

#### public boolean isSelectionVisible()

Checks whether the current selection is visible.

**Specified by:**
- isSelectionVisible

in interface

Caret

**Returns:**
- true if the selection is visible

---

#### public boolean isActive()

Determines if the caret is currently active.

This method returns whether or not the

Caret

is currently in a blinking state. It does not provide
information as to whether it is currently blinked on or off.
To determine if the caret is currently painted use the

isVisible

method.

**Returns:**
- true

if active else

false

**See Also:**
- isVisible()

**Since:**
- 1.5

---

#### public boolean isVisible()

Indicates whether or not the caret is currently visible. As the
caret flashes on and off the return value of this will change
between true, when the caret is painted, and false, when the
caret is not painted.

isActive

indicates whether
or not the caret is in a blinking state, such that it

can

be visible, and

isVisible

indicates whether or not
the caret

is

actually visible.

Subclasses that wish to render a different flashing caret
should override paint and only paint the caret if this method
returns true.

**Specified by:**
- isVisible

in interface

Caret

**Returns:**
- true if visible else false

**See Also:**
- Caret.isVisible()

,

isActive()

---

#### public void setVisible​(boolean e)

Sets the caret visibility, and repaints the caret.
It is important to understand the relationship between this method,

isVisible

and

isActive

.
Calling this method with a value of

true

activates the
caret blinking. Setting it to

false

turns it completely off.
To determine whether the blinking is active, you should call

isActive

. In effect,

isActive

is an
appropriate corresponding "getter" method for this one.

isVisible

can be used to fetch the current
visibility status of the caret, meaning whether or not it is currently
painted. This status will change as the caret blinks on and off.

Here's a list showing the potential return values of both

isActive

and

isVisible

after calling this method:

setVisible(true)

:

- isActive(): true
- isVisible(): true or false depending on whether
or not the caret is blinked on or off

setVisible(false)

:

- isActive(): false
- isVisible(): false

**Specified by:**
- setVisible

in interface

Caret

**Parameters:**
- e

- the visibility specifier

**See Also:**
- isActive()

,

Caret.setVisible(boolean)

---

#### public void setBlinkRate​(int rate)

Sets the caret blink rate.

**Specified by:**
- setBlinkRate

in interface

Caret

**Parameters:**
- rate

- the rate in milliseconds, 0 to stop blinking

**See Also:**
- Caret.setBlinkRate(int)

---

#### public int getBlinkRate()

Gets the caret blink rate.

**Specified by:**
- getBlinkRate

in interface

Caret

**Returns:**
- the delay in milliseconds. If this is
zero the caret will not blink.

**See Also:**
- Caret.getBlinkRate()

---

#### public int getDot()

Fetches the current position of the caret.

**Specified by:**
- getDot

in interface

Caret

**Returns:**
- the position >= 0

**See Also:**
- Caret.getDot()

---

#### public int getMark()

Fetches the current position of the mark. If there is a selection,
the dot and mark will not be the same.

**Specified by:**
- getMark

in interface

Caret

**Returns:**
- the position >= 0

**See Also:**
- Caret.getMark()

---

#### public void setDot​(int dot)

Sets the caret position and mark to the specified position,
with a forward bias. This implicitly sets the
selection range to zero.

**Specified by:**
- setDot

in interface

Caret

**Parameters:**
- dot

- the position >= 0

**See Also:**
- setDot(int, Position.Bias)

,

Caret.setDot(int)

---

#### public void moveDot​(int dot)

Moves the caret position to the specified position,
with a forward bias.

**Specified by:**
- moveDot

in interface

Caret

**Parameters:**
- dot

- the position >= 0

**See Also:**
- moveDot(int, javax.swing.text.Position.Bias)

,

Caret.moveDot(int)

---

#### public void moveDot​(int dot,

Position.Bias
dotBias)

Moves the caret position to the specified position, with the
specified bias.

**Parameters:**
- dot

- the position >= 0
- dotBias

- the bias for this position, not

null

**Throws:**
- IllegalArgumentException

- if the bias is

null

**See Also:**
- Caret.moveDot(int)

**Since:**
- 1.6

---

#### public void setDot​(int dot,

Position.Bias
dotBias)

Sets the caret position and mark to the specified position, with the
specified bias. This implicitly sets the selection range
to zero.

**Parameters:**
- dot

- the position >= 0
- dotBias

- the bias for this position, not

null

**Throws:**
- IllegalArgumentException

- if the bias is

null

**See Also:**
- Caret.setDot(int)

**Since:**
- 1.6

---

#### public
Position.Bias
getDotBias()

Returns the bias of the caret position.

**Returns:**
- the bias of the caret position

**Since:**
- 1.6

---

#### public
Position.Bias
getMarkBias()

Returns the bias of the mark.

**Returns:**
- the bias of the mark

**Since:**
- 1.6

---

#### public void setMagicCaretPosition​(
Point
p)

Saves the current caret position. This is used when
caret up/down actions occur, moving between lines
that have uneven end positions.

**Specified by:**
- setMagicCaretPosition

in interface

Caret

**Parameters:**
- p

- the position

**See Also:**
- getMagicCaretPosition()

---

#### public
Point
getMagicCaretPosition()

Gets the saved caret position.

**Specified by:**
- getMagicCaretPosition

in interface

Caret

**Returns:**
- the position
see #setMagicCaretPosition

**See Also:**
- Caret.setMagicCaretPosition(java.awt.Point)

---

#### public boolean equals​(
Object
obj)

Compares this object to the specified object.
The superclass behavior of comparing rectangles
is not desired, so this is changed to the Object
behavior.

**Overrides:**
- equals

in class

Rectangle

**Parameters:**
- obj

- the object to compare this font with

**Returns:**
- true

if the objects are equal;

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class DefaultCaret

java.lang.Object

- java.awt.geom.RectangularShape
- - java.awt.geom.Rectangle2D
- - java.awt.Rectangle
- - javax.swing.text.DefaultCaret

java.awt.geom.RectangularShape

- java.awt.geom.Rectangle2D
- - java.awt.Rectangle
- - javax.swing.text.DefaultCaret

java.awt.geom.Rectangle2D

- java.awt.Rectangle
- - javax.swing.text.DefaultCaret

java.awt.Rectangle

- javax.swing.text.DefaultCaret

javax.swing.text.DefaultCaret

**All Implemented Interfaces:** FocusListener

,

MouseListener

,

MouseMotionListener

,

Shape

,

Serializable

,

Cloneable

,

EventListener

,

Caret

**Direct Known Subclasses:** BasicTextUI.BasicCaret

```java
public class
DefaultCaret

extends
Rectangle

implements
Caret
,
FocusListener
,
MouseListener
,
MouseMotionListener
```

A default implementation of Caret. The caret is rendered as
a vertical line in the color specified by the CaretColor property
of the associated JTextComponent. It can blink at the rate specified
by the BlinkRate property.

This implementation expects two sources of asynchronous notification.
The timer thread fires asynchronously, and causes the caret to simply
repaint the most recent bounding box. The caret also tracks change
as the document is modified. Typically this will happen on the
event dispatch thread as a result of some mouse or keyboard event.
The caret behavior on both synchronous and asynchronous documents updates
is controlled by

UpdatePolicy

property. The repaint of the
new caret location will occur on the event thread in any case, as calls to

modelToView

are only safe on the event thread.

The caret acts as a mouse and focus listener on the text component
it has been installed in, and defines the caret semantics based upon
those events. The listener methods can be reimplemented to change the
semantics.
By default, the first mouse button will be used to set focus and caret
position. Dragging the mouse pointer with the first mouse button will
sweep out a selection that is contiguous in the model. If the associated
text component is editable, the caret will become visible when focus
is gained, and invisible when focus is lost.

The Highlighter bound to the associated text component is used to
render the selection by default.
Selection appearance can be customized by supplying a
painter to use for the highlights. By default a painter is used that
will render a solid color as specified in the associated text component
in the

SelectionColor

property. This can easily be changed
by reimplementing the

getSelectionPainter

method.

A customized caret appearance can be achieved by reimplementing
the paint method. If the paint method is changed, the damage method
should also be reimplemented to cause a repaint for the area needed
to render the caret. The caret extends the Rectangle class which
is used to hold the bounding box for where the caret was last rendered.
This enables the caret to repaint in a thread-safe manner when the
caret moves without making a call to modelToView which is unstable
between model updates and view repair (i.e. the order of delivery
to DocumentListeners is not guaranteed).

The magic caret position is set to null when the caret position changes.
A timer is used to determine the new location (after the caret change).
When the timer fires, if the magic caret position is still null it is
reset to the current caret position. Any actions that change
the caret position and want the magic caret position to remain the
same, must remember the magic caret position, change the cursor, and
then set the magic caret position to its original value. This has the
benefit that only actions that want the magic caret position to persist
(such as open/down) need to know about it.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** Caret

,

Serialized Form

public class

DefaultCaret

extends

Rectangle

implements

Caret

,

FocusListener

,

MouseListener

,

MouseMotionListener

A default implementation of Caret. The caret is rendered as
a vertical line in the color specified by the CaretColor property
of the associated JTextComponent. It can blink at the rate specified
by the BlinkRate property.

This implementation expects two sources of asynchronous notification.
The timer thread fires asynchronously, and causes the caret to simply
repaint the most recent bounding box. The caret also tracks change
as the document is modified. Typically this will happen on the
event dispatch thread as a result of some mouse or keyboard event.
The caret behavior on both synchronous and asynchronous documents updates
is controlled by

UpdatePolicy

property. The repaint of the
new caret location will occur on the event thread in any case, as calls to

modelToView

are only safe on the event thread.

The caret acts as a mouse and focus listener on the text component
it has been installed in, and defines the caret semantics based upon
those events. The listener methods can be reimplemented to change the
semantics.
By default, the first mouse button will be used to set focus and caret
position. Dragging the mouse pointer with the first mouse button will
sweep out a selection that is contiguous in the model. If the associated
text component is editable, the caret will become visible when focus
is gained, and invisible when focus is lost.

The Highlighter bound to the associated text component is used to
render the selection by default.
Selection appearance can be customized by supplying a
painter to use for the highlights. By default a painter is used that
will render a solid color as specified in the associated text component
in the

SelectionColor

property. This can easily be changed
by reimplementing the

getSelectionPainter

method.

A customized caret appearance can be achieved by reimplementing
the paint method. If the paint method is changed, the damage method
should also be reimplemented to cause a repaint for the area needed
to render the caret. The caret extends the Rectangle class which
is used to hold the bounding box for where the caret was last rendered.
This enables the caret to repaint in a thread-safe manner when the
caret moves without making a call to modelToView which is unstable
between model updates and view repair (i.e. the order of delivery
to DocumentListeners is not guaranteed).

The magic caret position is set to null when the caret position changes.
A timer is used to determine the new location (after the caret change).
When the timer fires, if the magic caret position is still null it is
reset to the current caret position. Any actions that change
the caret position and want the magic caret position to remain the
same, must remember the magic caret position, change the cursor, and
then set the magic caret position to its original value. This has the
benefit that only actions that want the magic caret position to persist
(such as open/down) need to know about it.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

This implementation expects two sources of asynchronous notification.
The timer thread fires asynchronously, and causes the caret to simply
repaint the most recent bounding box. The caret also tracks change
as the document is modified. Typically this will happen on the
event dispatch thread as a result of some mouse or keyboard event.
The caret behavior on both synchronous and asynchronous documents updates
is controlled by

UpdatePolicy

property. The repaint of the
new caret location will occur on the event thread in any case, as calls to

modelToView

are only safe on the event thread.

The caret acts as a mouse and focus listener on the text component
it has been installed in, and defines the caret semantics based upon
those events. The listener methods can be reimplemented to change the
semantics.
By default, the first mouse button will be used to set focus and caret
position. Dragging the mouse pointer with the first mouse button will
sweep out a selection that is contiguous in the model. If the associated
text component is editable, the caret will become visible when focus
is gained, and invisible when focus is lost.

The Highlighter bound to the associated text component is used to
render the selection by default.
Selection appearance can be customized by supplying a
painter to use for the highlights. By default a painter is used that
will render a solid color as specified in the associated text component
in the

SelectionColor

property. This can easily be changed
by reimplementing the

getSelectionPainter

method.

A customized caret appearance can be achieved by reimplementing
the paint method. If the paint method is changed, the damage method
should also be reimplemented to cause a repaint for the area needed
to render the caret. The caret extends the Rectangle class which
is used to hold the bounding box for where the caret was last rendered.
This enables the caret to repaint in a thread-safe manner when the
caret moves without making a call to modelToView which is unstable
between model updates and view repair (i.e. the order of delivery
to DocumentListeners is not guaranteed).

The magic caret position is set to null when the caret position changes.
A timer is used to determine the new location (after the caret change).
When the timer fires, if the magic caret position is still null it is
reset to the current caret position. Any actions that change
the caret position and want the magic caret position to remain the
same, must remember the magic caret position, change the cursor, and
then set the magic caret position to its original value. This has the
benefit that only actions that want the magic caret position to persist
(such as open/down) need to know about it.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

The caret acts as a mouse and focus listener on the text component
it has been installed in, and defines the caret semantics based upon
those events. The listener methods can be reimplemented to change the
semantics.
By default, the first mouse button will be used to set focus and caret
position. Dragging the mouse pointer with the first mouse button will
sweep out a selection that is contiguous in the model. If the associated
text component is editable, the caret will become visible when focus
is gained, and invisible when focus is lost.

The Highlighter bound to the associated text component is used to
render the selection by default.
Selection appearance can be customized by supplying a
painter to use for the highlights. By default a painter is used that
will render a solid color as specified in the associated text component
in the

SelectionColor

property. This can easily be changed
by reimplementing the

getSelectionPainter

method.

A customized caret appearance can be achieved by reimplementing
the paint method. If the paint method is changed, the damage method
should also be reimplemented to cause a repaint for the area needed
to render the caret. The caret extends the Rectangle class which
is used to hold the bounding box for where the caret was last rendered.
This enables the caret to repaint in a thread-safe manner when the
caret moves without making a call to modelToView which is unstable
between model updates and view repair (i.e. the order of delivery
to DocumentListeners is not guaranteed).

The magic caret position is set to null when the caret position changes.
A timer is used to determine the new location (after the caret change).
When the timer fires, if the magic caret position is still null it is
reset to the current caret position. Any actions that change
the caret position and want the magic caret position to remain the
same, must remember the magic caret position, change the cursor, and
then set the magic caret position to its original value. This has the
benefit that only actions that want the magic caret position to persist
(such as open/down) need to know about it.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

The Highlighter bound to the associated text component is used to
render the selection by default.
Selection appearance can be customized by supplying a
painter to use for the highlights. By default a painter is used that
will render a solid color as specified in the associated text component
in the

SelectionColor

property. This can easily be changed
by reimplementing the

getSelectionPainter

method.

A customized caret appearance can be achieved by reimplementing
the paint method. If the paint method is changed, the damage method
should also be reimplemented to cause a repaint for the area needed
to render the caret. The caret extends the Rectangle class which
is used to hold the bounding box for where the caret was last rendered.
This enables the caret to repaint in a thread-safe manner when the
caret moves without making a call to modelToView which is unstable
between model updates and view repair (i.e. the order of delivery
to DocumentListeners is not guaranteed).

The magic caret position is set to null when the caret position changes.
A timer is used to determine the new location (after the caret change).
When the timer fires, if the magic caret position is still null it is
reset to the current caret position. Any actions that change
the caret position and want the magic caret position to remain the
same, must remember the magic caret position, change the cursor, and
then set the magic caret position to its original value. This has the
benefit that only actions that want the magic caret position to persist
(such as open/down) need to know about it.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

A customized caret appearance can be achieved by reimplementing
the paint method. If the paint method is changed, the damage method
should also be reimplemented to cause a repaint for the area needed
to render the caret. The caret extends the Rectangle class which
is used to hold the bounding box for where the caret was last rendered.
This enables the caret to repaint in a thread-safe manner when the
caret moves without making a call to modelToView which is unstable
between model updates and view repair (i.e. the order of delivery
to DocumentListeners is not guaranteed).

The magic caret position is set to null when the caret position changes.
A timer is used to determine the new location (after the caret change).
When the timer fires, if the magic caret position is still null it is
reset to the current caret position. Any actions that change
the caret position and want the magic caret position to remain the
same, must remember the magic caret position, change the cursor, and
then set the magic caret position to its original value. This has the
benefit that only actions that want the magic caret position to persist
(such as open/down) need to know about it.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

The magic caret position is set to null when the caret position changes.
A timer is used to determine the new location (after the caret change).
When the timer fires, if the magic caret position is still null it is
reset to the current caret position. Any actions that change
the caret position and want the magic caret position to remain the
same, must remember the magic caret position, change the cursor, and
then set the magic caret position to its original value. This has the
benefit that only actions that want the magic caret position to persist
(such as open/down) need to know about it.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.awt.geom.

Rectangle2D

Rectangle2D.Double

,

Rectangle2D.Float

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ALWAYS_UPDATE

Indicates that the caret position is to be

always

updated accordingly to the document changes regardless whether
the document updates are performed on the Event Dispatching Thread
or not.

protected

ChangeEvent

changeEvent

The change event for the model.

protected

EventListenerList

listenerList

The event listener list.

static int

NEVER_UPDATE

Indicates that the caret should remain at the same
absolute position in the document regardless of any document
updates, except when the document length becomes less than
the current caret position due to removal.

static int

UPDATE_WHEN_ON_EDT

Indicates that the caret position is to be updated only when
document changes are performed on the Event Dispatching Thread.

- Fields declared in class java.awt.

Rectangle

height

,

width

,

x

,

y

- Fields declared in class java.awt.geom.

Rectangle2D

OUT_BOTTOM

,

OUT_LEFT

,

OUT_RIGHT

,

OUT_TOP

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultCaret

()

Constructs a default caret.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

l)

Adds a listener to track whenever the caret position has
been changed.

protected void

adjustVisibility

​(

Rectangle

nloc)

Scrolls the associated view (if necessary) to make
the caret visible.

protected void

damage

​(

Rectangle

r)

Damages the area surrounding the caret to cause
it to be repainted in a new location.

void

deinstall

​(

JTextComponent

c)

Called when the UI is being removed from the
interface of a JTextComponent.

boolean

equals

​(

Object

obj)

Compares this object to the specified object.

protected void

fireStateChanged

()

Notifies all listeners that have registered interest for
notification on this event type.

void

focusGained

​(

FocusEvent

e)

Called when the component containing the caret gains
focus.

void

focusLost

​(

FocusEvent

e)

Called when the component containing the caret loses
focus.

int

getBlinkRate

()

Gets the caret blink rate.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the change listeners
registered on this caret.

protected

JTextComponent

getComponent

()

Gets the text editor component that this caret is
is bound to.

int

getDot

()

Fetches the current position of the caret.

Position.Bias

getDotBias

()

Returns the bias of the caret position.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this caret.

Point

getMagicCaretPosition

()

Gets the saved caret position.

int

getMark

()

Fetches the current position of the mark.

Position.Bias

getMarkBias

()

Returns the bias of the mark.

protected

Highlighter.HighlightPainter

getSelectionPainter

()

Gets the painter for the Highlighter.

int

getUpdatePolicy

()

Gets the caret movement policy on document updates.

void

install

​(

JTextComponent

c)

Called when the UI is being installed into the
interface of a JTextComponent.

boolean

isActive

()

Determines if the caret is currently active.

boolean

isSelectionVisible

()

Checks whether the current selection is visible.

boolean

isVisible

()

Indicates whether or not the caret is currently visible.

void

mouseClicked

​(

MouseEvent

e)

Called when the mouse is clicked.

void

mouseDragged

​(

MouseEvent

e)

Moves the caret position
according to the mouse pointer's current
location.

void

mouseEntered

​(

MouseEvent

e)

Called when the mouse enters a region.

void

mouseExited

​(

MouseEvent

e)

Called when the mouse exits a region.

void

mouseMoved

​(

MouseEvent

e)

Called when the mouse is moved.

void

mousePressed

​(

MouseEvent

e)

If button 1 is pressed, this is implemented to
request focus on the associated text component,
and to set the caret position.

void

mouseReleased

​(

MouseEvent

e)

Called when the mouse is released.

protected void

moveCaret

​(

MouseEvent

e)

Tries to move the position of the caret from
the coordinates of a mouse event, using viewToModel().

void

moveDot

​(int dot)

Moves the caret position to the specified position,
with a forward bias.

void

moveDot

​(int dot,

Position.Bias

dotBias)

Moves the caret position to the specified position, with the
specified bias.

void

paint

​(

Graphics

g)

Renders the caret as a vertical line.

protected void

positionCaret

​(

MouseEvent

e)

Tries to set the position of the caret from
the coordinates of a mouse event, using viewToModel().

void

removeChangeListener

​(

ChangeListener

l)

Removes a listener that was tracking caret position changes.

protected void

repaint

()

Cause the caret to be painted.

void

setBlinkRate

​(int rate)

Sets the caret blink rate.

void

setDot

​(int dot)

Sets the caret position and mark to the specified position,
with a forward bias.

void

setDot

​(int dot,

Position.Bias

dotBias)

Sets the caret position and mark to the specified position, with the
specified bias.

void

setMagicCaretPosition

​(

Point

p)

Saves the current caret position.

void

setSelectionVisible

​(boolean vis)

Changes the selection visibility.

void

setUpdatePolicy

​(int policy)

Sets the caret movement policy on the document updates.

void

setVisible

​(boolean e)

Sets the caret visibility, and repaints the caret.

- Methods declared in class java.awt.

Rectangle

add

,

add

,

add

,

contains

,

contains

,

contains

,

contains

,

createIntersection

,

createUnion

,

getBounds

,

getBounds2D

,

getHeight

,

getLocation

,

getSize

,

getWidth

,

getX

,

getY

,

grow

,

inside

,

intersection

,

intersects

,

isEmpty

,

move

,

outcode

,

reshape

,

resize

,

setBounds

,

setBounds

,

setLocation

,

setLocation

,

setRect

,

setSize

,

setSize

,

toString

,

translate

,

union

- Methods declared in class java.awt.geom.

Rectangle2D

add

,

add

,

add

,

contains

,

contains

,

getPathIterator

,

getPathIterator

,

hashCode

,

intersect

,

intersects

,

intersectsLine

,

intersectsLine

,

outcode

,

setFrame

,

setRect

,

union

- Methods declared in class java.awt.geom.

RectangularShape

clone

,

contains

,

contains

,

getCenterX

,

getCenterY

,

getFrame

,

getMaxX

,

getMaxY

,

getMinX

,

getMinY

,

intersects

,

setFrame

,

setFrame

,

setFrameFromCenter

,

setFrameFromCenter

,

setFrameFromDiagonal

,

setFrameFromDiagonal

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

- Methods declared in interface java.awt.

Shape

contains

,

contains

,

contains

,

contains

,

getPathIterator

,

getPathIterator

,

intersects

,

intersects

Nested Class Summary

- Nested classes/interfaces declared in class java.awt.geom.

Rectangle2D

Rectangle2D.Double

,

Rectangle2D.Float

---

#### Nested Class Summary

Nested classes/interfaces declared in class java.awt.geom.

Rectangle2D

Rectangle2D.Double

,

Rectangle2D.Float

---

#### Nested classes/interfaces declared in class java.awt.geom. Rectangle2D

Field Summary

Fields

Modifier and Type

Field

Description

static int

ALWAYS_UPDATE

Indicates that the caret position is to be

always

updated accordingly to the document changes regardless whether
the document updates are performed on the Event Dispatching Thread
or not.

protected

ChangeEvent

changeEvent

The change event for the model.

protected

EventListenerList

listenerList

The event listener list.

static int

NEVER_UPDATE

Indicates that the caret should remain at the same
absolute position in the document regardless of any document
updates, except when the document length becomes less than
the current caret position due to removal.

static int

UPDATE_WHEN_ON_EDT

Indicates that the caret position is to be updated only when
document changes are performed on the Event Dispatching Thread.

- Fields declared in class java.awt.

Rectangle

height

,

width

,

x

,

y

- Fields declared in class java.awt.geom.

Rectangle2D

OUT_BOTTOM

,

OUT_LEFT

,

OUT_RIGHT

,

OUT_TOP

---

#### Field Summary

Indicates that the caret position is to be

always

updated accordingly to the document changes regardless whether
the document updates are performed on the Event Dispatching Thread
or not.

The change event for the model.

The event listener list.

Indicates that the caret should remain at the same
absolute position in the document regardless of any document
updates, except when the document length becomes less than
the current caret position due to removal.

Indicates that the caret position is to be updated only when
document changes are performed on the Event Dispatching Thread.

Fields declared in class java.awt.

Rectangle

height

,

width

,

x

,

y

---

#### Fields declared in class java.awt. Rectangle

Fields declared in class java.awt.geom.

Rectangle2D

OUT_BOTTOM

,

OUT_LEFT

,

OUT_RIGHT

,

OUT_TOP

---

#### Fields declared in class java.awt.geom. Rectangle2D

Constructor Summary

Constructors

Constructor

Description

DefaultCaret

()

Constructs a default caret.

---

#### Constructor Summary

Constructs a default caret.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

l)

Adds a listener to track whenever the caret position has
been changed.

protected void

adjustVisibility

​(

Rectangle

nloc)

Scrolls the associated view (if necessary) to make
the caret visible.

protected void

damage

​(

Rectangle

r)

Damages the area surrounding the caret to cause
it to be repainted in a new location.

void

deinstall

​(

JTextComponent

c)

Called when the UI is being removed from the
interface of a JTextComponent.

boolean

equals

​(

Object

obj)

Compares this object to the specified object.

protected void

fireStateChanged

()

Notifies all listeners that have registered interest for
notification on this event type.

void

focusGained

​(

FocusEvent

e)

Called when the component containing the caret gains
focus.

void

focusLost

​(

FocusEvent

e)

Called when the component containing the caret loses
focus.

int

getBlinkRate

()

Gets the caret blink rate.

ChangeListener

[]

getChangeListeners

()

Returns an array of all the change listeners
registered on this caret.

protected

JTextComponent

getComponent

()

Gets the text editor component that this caret is
is bound to.

int

getDot

()

Fetches the current position of the caret.

Position.Bias

getDotBias

()

Returns the bias of the caret position.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this caret.

Point

getMagicCaretPosition

()

Gets the saved caret position.

int

getMark

()

Fetches the current position of the mark.

Position.Bias

getMarkBias

()

Returns the bias of the mark.

protected

Highlighter.HighlightPainter

getSelectionPainter

()

Gets the painter for the Highlighter.

int

getUpdatePolicy

()

Gets the caret movement policy on document updates.

void

install

​(

JTextComponent

c)

Called when the UI is being installed into the
interface of a JTextComponent.

boolean

isActive

()

Determines if the caret is currently active.

boolean

isSelectionVisible

()

Checks whether the current selection is visible.

boolean

isVisible

()

Indicates whether or not the caret is currently visible.

void

mouseClicked

​(

MouseEvent

e)

Called when the mouse is clicked.

void

mouseDragged

​(

MouseEvent

e)

Moves the caret position
according to the mouse pointer's current
location.

void

mouseEntered

​(

MouseEvent

e)

Called when the mouse enters a region.

void

mouseExited

​(

MouseEvent

e)

Called when the mouse exits a region.

void

mouseMoved

​(

MouseEvent

e)

Called when the mouse is moved.

void

mousePressed

​(

MouseEvent

e)

If button 1 is pressed, this is implemented to
request focus on the associated text component,
and to set the caret position.

void

mouseReleased

​(

MouseEvent

e)

Called when the mouse is released.

protected void

moveCaret

​(

MouseEvent

e)

Tries to move the position of the caret from
the coordinates of a mouse event, using viewToModel().

void

moveDot

​(int dot)

Moves the caret position to the specified position,
with a forward bias.

void

moveDot

​(int dot,

Position.Bias

dotBias)

Moves the caret position to the specified position, with the
specified bias.

void

paint

​(

Graphics

g)

Renders the caret as a vertical line.

protected void

positionCaret

​(

MouseEvent

e)

Tries to set the position of the caret from
the coordinates of a mouse event, using viewToModel().

void

removeChangeListener

​(

ChangeListener

l)

Removes a listener that was tracking caret position changes.

protected void

repaint

()

Cause the caret to be painted.

void

setBlinkRate

​(int rate)

Sets the caret blink rate.

void

setDot

​(int dot)

Sets the caret position and mark to the specified position,
with a forward bias.

void

setDot

​(int dot,

Position.Bias

dotBias)

Sets the caret position and mark to the specified position, with the
specified bias.

void

setMagicCaretPosition

​(

Point

p)

Saves the current caret position.

void

setSelectionVisible

​(boolean vis)

Changes the selection visibility.

void

setUpdatePolicy

​(int policy)

Sets the caret movement policy on the document updates.

void

setVisible

​(boolean e)

Sets the caret visibility, and repaints the caret.

- Methods declared in class java.awt.

Rectangle

add

,

add

,

add

,

contains

,

contains

,

contains

,

contains

,

createIntersection

,

createUnion

,

getBounds

,

getBounds2D

,

getHeight

,

getLocation

,

getSize

,

getWidth

,

getX

,

getY

,

grow

,

inside

,

intersection

,

intersects

,

isEmpty

,

move

,

outcode

,

reshape

,

resize

,

setBounds

,

setBounds

,

setLocation

,

setLocation

,

setRect

,

setSize

,

setSize

,

toString

,

translate

,

union

- Methods declared in class java.awt.geom.

Rectangle2D

add

,

add

,

add

,

contains

,

contains

,

getPathIterator

,

getPathIterator

,

hashCode

,

intersect

,

intersects

,

intersectsLine

,

intersectsLine

,

outcode

,

setFrame

,

setRect

,

union

- Methods declared in class java.awt.geom.

RectangularShape

clone

,

contains

,

contains

,

getCenterX

,

getCenterY

,

getFrame

,

getMaxX

,

getMaxY

,

getMinX

,

getMinY

,

intersects

,

setFrame

,

setFrame

,

setFrameFromCenter

,

setFrameFromCenter

,

setFrameFromDiagonal

,

setFrameFromDiagonal

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

- Methods declared in interface java.awt.

Shape

contains

,

contains

,

contains

,

contains

,

getPathIterator

,

getPathIterator

,

intersects

,

intersects

---

#### Method Summary

Adds a listener to track whenever the caret position has
been changed.

Scrolls the associated view (if necessary) to make
the caret visible.

Damages the area surrounding the caret to cause
it to be repainted in a new location.

Called when the UI is being removed from the
interface of a JTextComponent.

Compares this object to the specified object.

Notifies all listeners that have registered interest for
notification on this event type.

Called when the component containing the caret gains
focus.

Called when the component containing the caret loses
focus.

Gets the caret blink rate.

Returns an array of all the change listeners
registered on this caret.

Gets the text editor component that this caret is
is bound to.

Fetches the current position of the caret.

Returns the bias of the caret position.

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this caret.

Gets the saved caret position.

Fetches the current position of the mark.

Returns the bias of the mark.

Gets the painter for the Highlighter.

Gets the caret movement policy on document updates.

Called when the UI is being installed into the
interface of a JTextComponent.

Determines if the caret is currently active.

Checks whether the current selection is visible.

Indicates whether or not the caret is currently visible.

Called when the mouse is clicked.

Moves the caret position
according to the mouse pointer's current
location.

Called when the mouse enters a region.

Called when the mouse exits a region.

Called when the mouse is moved.

If button 1 is pressed, this is implemented to
request focus on the associated text component,
and to set the caret position.

Called when the mouse is released.

Tries to move the position of the caret from
the coordinates of a mouse event, using viewToModel().

Moves the caret position to the specified position,
with a forward bias.

Moves the caret position to the specified position, with the
specified bias.

Renders the caret as a vertical line.

Tries to set the position of the caret from
the coordinates of a mouse event, using viewToModel().

Removes a listener that was tracking caret position changes.

Cause the caret to be painted.

Sets the caret blink rate.

Sets the caret position and mark to the specified position,
with a forward bias.

Sets the caret position and mark to the specified position, with the
specified bias.

Saves the current caret position.

Changes the selection visibility.

Sets the caret movement policy on the document updates.

Sets the caret visibility, and repaints the caret.

Methods declared in class java.awt.

Rectangle

add

,

add

,

add

,

contains

,

contains

,

contains

,

contains

,

createIntersection

,

createUnion

,

getBounds

,

getBounds2D

,

getHeight

,

getLocation

,

getSize

,

getWidth

,

getX

,

getY

,

grow

,

inside

,

intersection

,

intersects

,

isEmpty

,

move

,

outcode

,

reshape

,

resize

,

setBounds

,

setBounds

,

setLocation

,

setLocation

,

setRect

,

setSize

,

setSize

,

toString

,

translate

,

union

---

#### Methods declared in class java.awt. Rectangle

Methods declared in class java.awt.geom.

Rectangle2D

add

,

add

,

add

,

contains

,

contains

,

getPathIterator

,

getPathIterator

,

hashCode

,

intersect

,

intersects

,

intersectsLine

,

intersectsLine

,

outcode

,

setFrame

,

setRect

,

union

---

#### Methods declared in class java.awt.geom. Rectangle2D

Methods declared in class java.awt.geom.

RectangularShape

clone

,

contains

,

contains

,

getCenterX

,

getCenterY

,

getFrame

,

getMaxX

,

getMaxY

,

getMinX

,

getMinY

,

intersects

,

setFrame

,

setFrame

,

setFrameFromCenter

,

setFrameFromCenter

,

setFrameFromDiagonal

,

setFrameFromDiagonal

---

#### Methods declared in class java.awt.geom. RectangularShape

Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.awt.

Shape

contains

,

contains

,

contains

,

contains

,

getPathIterator

,

getPathIterator

,

intersects

,

intersects

---

#### Methods declared in interface java.awt. Shape

============ FIELD DETAIL ===========

- Field Detail

- UPDATE_WHEN_ON_EDT

```java
public static final int UPDATE_WHEN_ON_EDT
```

Indicates that the caret position is to be updated only when
document changes are performed on the Event Dispatching Thread.

**Since:** 1.5
**See Also:** setUpdatePolicy(int)

,

getUpdatePolicy()

,

Constant Field Values

- NEVER_UPDATE

```java
public static final int NEVER_UPDATE
```

Indicates that the caret should remain at the same
absolute position in the document regardless of any document
updates, except when the document length becomes less than
the current caret position due to removal. In that case the caret
position is adjusted to the end of the document.

**Since:** 1.5
**See Also:** setUpdatePolicy(int)

,

getUpdatePolicy()

,

Constant Field Values

- ALWAYS_UPDATE

```java
public static final int ALWAYS_UPDATE
```

Indicates that the caret position is to be

always

updated accordingly to the document changes regardless whether
the document updates are performed on the Event Dispatching Thread
or not.

**Since:** 1.5
**See Also:** setUpdatePolicy(int)

,

getUpdatePolicy()

,

Constant Field Values

- listenerList

```java
protected
EventListenerList
listenerList
```

The event listener list.

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

The change event for the model.
Only one ChangeEvent is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultCaret

```java
public DefaultCaret()
```

Constructs a default caret.

============ METHOD DETAIL ==========

- Method Detail

- setUpdatePolicy

```java
public void setUpdatePolicy​(int policy)
```

Sets the caret movement policy on the document updates. Normally
the caret updates its absolute position within the document on
insertions occurred before or at the caret position and
on removals before the caret position. 'Absolute position'
means here the position relative to the start of the document.
For example if
a character is typed within editable text component it is inserted
at the caret position and the caret moves to the next absolute
position within the document due to insertion and if

BACKSPACE

is typed then caret decreases its absolute
position due to removal of a character before it. Sometimes
it may be useful to turn off the caret position updates so that
the caret stays at the same absolute position within the
document position regardless of any document updates.

The following update policies are allowed:

- NEVER_UPDATE

: the caret stays at the same
absolute position in the document regardless of any document
updates, except when document length becomes less than
the current caret position due to removal. In that case caret
position is adjusted to the end of the document.
The caret doesn't try to keep itself visible by scrolling
the associated view when using this policy.
- ALWAYS_UPDATE

: the caret always tracks document
changes. For regular changes it increases its position
if an insertion occurs before or at its current position,
and decreases position if a removal occurs before
its current position. For undo/redo updates it is always
moved to the position where update occurred. The caret
also tries to keep itself visible by calling

adjustVisibility

method.
- UPDATE_WHEN_ON_EDT

: acts like

ALWAYS_UPDATE

if the document updates are performed on the Event Dispatching Thread
and like

NEVER_UPDATE

if updates are performed on
other thread.

The default property value is

UPDATE_WHEN_ON_EDT

.

**Parameters:** policy

- one of the following values :

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE
**Throws:** IllegalArgumentException

- if invalid value is passed
**Since:** 1.5
**See Also:** getUpdatePolicy()

,

adjustVisibility(java.awt.Rectangle)

,

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE

- getUpdatePolicy

```java
public int getUpdatePolicy()
```

Gets the caret movement policy on document updates.

**Returns:** one of the following values :

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE
**Since:** 1.5
**See Also:** setUpdatePolicy(int)

,

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE

- getComponent

```java
protected final
JTextComponent
getComponent()
```

Gets the text editor component that this caret is
is bound to.

**Returns:** the component

- repaint

```java
protected final void repaint()
```

Cause the caret to be painted. The repaint
area is the bounding box of the caret (i.e.
the caret rectangle or

this

).

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

- damage

```java
protected void damage​(
Rectangle
r)
```

Damages the area surrounding the caret to cause
it to be repainted in a new location. If paint()
is reimplemented, this method should also be
reimplemented. This method should update the
caret bounds (x, y, width, and height).

**Parameters:** r

- the current location of the caret
**See Also:** paint(java.awt.Graphics)

- adjustVisibility

```java
protected void adjustVisibility​(
Rectangle
nloc)
```

Scrolls the associated view (if necessary) to make
the caret visible. Since how this should be done
is somewhat of a policy, this method can be
reimplemented to change the behavior. By default
the scrollRectToVisible method is called on the
associated component.

**Parameters:** nloc

- the new position to scroll to

- getSelectionPainter

```java
protected
Highlighter.HighlightPainter
getSelectionPainter()
```

Gets the painter for the Highlighter.

**Returns:** the painter

- positionCaret

```java
protected void positionCaret​(
MouseEvent
e)
```

Tries to set the position of the caret from
the coordinates of a mouse event, using viewToModel().

**Parameters:** e

- the mouse event

- moveCaret

```java
protected void moveCaret​(
MouseEvent
e)
```

Tries to move the position of the caret from
the coordinates of a mouse event, using viewToModel().
This will cause a selection if the dot and mark
are different.

**Parameters:** e

- the mouse event

- focusGained

```java
public void focusGained​(
FocusEvent
e)
```

Called when the component containing the caret gains
focus. This is implemented to set the caret to visible
if the component is editable.

**Specified by:** focusGained

in interface

FocusListener
**Parameters:** e

- the focus event
**See Also:** FocusListener.focusGained(java.awt.event.FocusEvent)

- focusLost

```java
public void focusLost​(
FocusEvent
e)
```

Called when the component containing the caret loses
focus. This is implemented to set the caret to visibility
to false.

**Specified by:** focusLost

in interface

FocusListener
**Parameters:** e

- the focus event
**See Also:** FocusListener.focusLost(java.awt.event.FocusEvent)

- mouseClicked

```java
public void mouseClicked​(
MouseEvent
e)
```

Called when the mouse is clicked. If the click was generated
from button1, a double click selects a word,
and a triple click the current line.

**Specified by:** mouseClicked

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseClicked(java.awt.event.MouseEvent)

- mousePressed

```java
public void mousePressed​(
MouseEvent
e)
```

If button 1 is pressed, this is implemented to
request focus on the associated text component,
and to set the caret position. If the shift key is held down,
the caret will be moved, potentially resulting in a selection,
otherwise the
caret position will be set to the new location. If the component
is not enabled, there will be no request for focus.

**Specified by:** mousePressed

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mousePressed(java.awt.event.MouseEvent)

- mouseReleased

```java
public void mouseReleased​(
MouseEvent
e)
```

Called when the mouse is released.

**Specified by:** mouseReleased

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseReleased(java.awt.event.MouseEvent)

- mouseEntered

```java
public void mouseEntered​(
MouseEvent
e)
```

Called when the mouse enters a region.

**Specified by:** mouseEntered

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseEntered(java.awt.event.MouseEvent)

- mouseExited

```java
public void mouseExited​(
MouseEvent
e)
```

Called when the mouse exits a region.

**Specified by:** mouseExited

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseExited(java.awt.event.MouseEvent)

- mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Moves the caret position
according to the mouse pointer's current
location. This effectively extends the
selection. By default, this is only done
for mouse button 1.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the mouse event
**See Also:** MouseMotionListener.mouseDragged(java.awt.event.MouseEvent)

- mouseMoved

```java
public void mouseMoved​(
MouseEvent
e)
```

Called when the mouse is moved.

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Parameters:** e

- the mouse event
**See Also:** MouseMotionListener.mouseMoved(java.awt.event.MouseEvent)

- paint

```java
public void paint​(
Graphics
g)
```

Renders the caret as a vertical line. If this is reimplemented
the damage method should also be reimplemented as it assumes the
shape of the caret is a vertical line. Sets the caret color to
the value returned by getCaretColor().

If there are multiple text directions present in the associated
document, a flag indicating the caret bias will be rendered.
This will occur only if the associated document is a subclass
of AbstractDocument and there are multiple bidi levels present
in the bidi element structure (i.e. the text has multiple
directions associated with it).

**Specified by:** paint

in interface

Caret
**Parameters:** g

- the graphics context
**See Also:** damage(java.awt.Rectangle)

- install

```java
public void install​(
JTextComponent
c)
```

Called when the UI is being installed into the
interface of a JTextComponent. This can be used
to gain access to the model that is being navigated
by the implementation of this interface. Sets the dot
and mark to 0, and establishes document, property change,
focus, mouse, and mouse motion listeners.

**Specified by:** install

in interface

Caret
**Parameters:** c

- the component
**See Also:** Caret.install(javax.swing.text.JTextComponent)

- deinstall

```java
public void deinstall​(
JTextComponent
c)
```

Called when the UI is being removed from the
interface of a JTextComponent. This is used to
unregister any listeners that were attached.

**Specified by:** deinstall

in interface

Caret
**Parameters:** c

- the component
**See Also:** Caret.deinstall(javax.swing.text.JTextComponent)

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a listener to track whenever the caret position has
been changed.

**Specified by:** addChangeListener

in interface

Caret
**Parameters:** l

- the listener
**See Also:** Caret.addChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a listener that was tracking caret position changes.

**Specified by:** removeChangeListener

in interface

Caret
**Parameters:** l

- the listener
**See Also:** Caret.removeChangeListener(javax.swing.event.ChangeListener)

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the change listeners
registered on this caret.

**Returns:** all of this caret's

ChangeListener

s
or an empty
array if no change listeners are currently registered
**Since:** 1.4
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

- fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method. The listener list is processed last to first.

**See Also:** EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this caret.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a

DefaultCaret

c

for its change listeners with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(c.getListeners(ChangeListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getChangeListeners()

- setSelectionVisible

```java
public void setSelectionVisible​(boolean vis)
```

Changes the selection visibility.

**Specified by:** setSelectionVisible

in interface

Caret
**Parameters:** vis

- the new visibility

- isSelectionVisible

```java
public boolean isSelectionVisible()
```

Checks whether the current selection is visible.

**Specified by:** isSelectionVisible

in interface

Caret
**Returns:** true if the selection is visible

- isActive

```java
public boolean isActive()
```

Determines if the caret is currently active.

This method returns whether or not the

Caret

is currently in a blinking state. It does not provide
information as to whether it is currently blinked on or off.
To determine if the caret is currently painted use the

isVisible

method.

**Returns:** true

if active else

false
**Since:** 1.5
**See Also:** isVisible()

- isVisible

```java
public boolean isVisible()
```

Indicates whether or not the caret is currently visible. As the
caret flashes on and off the return value of this will change
between true, when the caret is painted, and false, when the
caret is not painted.

isActive

indicates whether
or not the caret is in a blinking state, such that it

can

be visible, and

isVisible

indicates whether or not
the caret

is

actually visible.

Subclasses that wish to render a different flashing caret
should override paint and only paint the caret if this method
returns true.

**Specified by:** isVisible

in interface

Caret
**Returns:** true if visible else false
**See Also:** Caret.isVisible()

,

isActive()

- setVisible

```java
public void setVisible​(boolean e)
```

Sets the caret visibility, and repaints the caret.
It is important to understand the relationship between this method,

isVisible

and

isActive

.
Calling this method with a value of

true

activates the
caret blinking. Setting it to

false

turns it completely off.
To determine whether the blinking is active, you should call

isActive

. In effect,

isActive

is an
appropriate corresponding "getter" method for this one.

isVisible

can be used to fetch the current
visibility status of the caret, meaning whether or not it is currently
painted. This status will change as the caret blinks on and off.

Here's a list showing the potential return values of both

isActive

and

isVisible

after calling this method:

setVisible(true)

:

- isActive(): true
- isVisible(): true or false depending on whether
or not the caret is blinked on or off

setVisible(false)

:

- isActive(): false
- isVisible(): false

**Specified by:** setVisible

in interface

Caret
**Parameters:** e

- the visibility specifier
**See Also:** isActive()

,

Caret.setVisible(boolean)

- setBlinkRate

```java
public void setBlinkRate​(int rate)
```

Sets the caret blink rate.

**Specified by:** setBlinkRate

in interface

Caret
**Parameters:** rate

- the rate in milliseconds, 0 to stop blinking
**See Also:** Caret.setBlinkRate(int)

- getBlinkRate

```java
public int getBlinkRate()
```

Gets the caret blink rate.

**Specified by:** getBlinkRate

in interface

Caret
**Returns:** the delay in milliseconds. If this is
zero the caret will not blink.
**See Also:** Caret.getBlinkRate()

- getDot

```java
public int getDot()
```

Fetches the current position of the caret.

**Specified by:** getDot

in interface

Caret
**Returns:** the position >= 0
**See Also:** Caret.getDot()

- getMark

```java
public int getMark()
```

Fetches the current position of the mark. If there is a selection,
the dot and mark will not be the same.

**Specified by:** getMark

in interface

Caret
**Returns:** the position >= 0
**See Also:** Caret.getMark()

- setDot

```java
public void setDot​(int dot)
```

Sets the caret position and mark to the specified position,
with a forward bias. This implicitly sets the
selection range to zero.

**Specified by:** setDot

in interface

Caret
**Parameters:** dot

- the position >= 0
**See Also:** setDot(int, Position.Bias)

,

Caret.setDot(int)

- moveDot

```java
public void moveDot​(int dot)
```

Moves the caret position to the specified position,
with a forward bias.

**Specified by:** moveDot

in interface

Caret
**Parameters:** dot

- the position >= 0
**See Also:** moveDot(int, javax.swing.text.Position.Bias)

,

Caret.moveDot(int)

- moveDot

```java
public void moveDot​(int dot,

Position.Bias
dotBias)
```

Moves the caret position to the specified position, with the
specified bias.

**Parameters:** dot

- the position >= 0
**Parameters:** dotBias

- the bias for this position, not

null
**Throws:** IllegalArgumentException

- if the bias is

null
**Since:** 1.6
**See Also:** Caret.moveDot(int)

- setDot

```java
public void setDot​(int dot,

Position.Bias
dotBias)
```

Sets the caret position and mark to the specified position, with the
specified bias. This implicitly sets the selection range
to zero.

**Parameters:** dot

- the position >= 0
**Parameters:** dotBias

- the bias for this position, not

null
**Throws:** IllegalArgumentException

- if the bias is

null
**Since:** 1.6
**See Also:** Caret.setDot(int)

- getDotBias

```java
public
Position.Bias
getDotBias()
```

Returns the bias of the caret position.

**Returns:** the bias of the caret position
**Since:** 1.6

- getMarkBias

```java
public
Position.Bias
getMarkBias()
```

Returns the bias of the mark.

**Returns:** the bias of the mark
**Since:** 1.6

- setMagicCaretPosition

```java
public void setMagicCaretPosition​(
Point
p)
```

Saves the current caret position. This is used when
caret up/down actions occur, moving between lines
that have uneven end positions.

**Specified by:** setMagicCaretPosition

in interface

Caret
**Parameters:** p

- the position
**See Also:** getMagicCaretPosition()

- getMagicCaretPosition

```java
public
Point
getMagicCaretPosition()
```

Gets the saved caret position.

**Specified by:** getMagicCaretPosition

in interface

Caret
**Returns:** the position
see #setMagicCaretPosition
**See Also:** Caret.setMagicCaretPosition(java.awt.Point)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this object to the specified object.
The superclass behavior of comparing rectangles
is not desired, so this is changed to the Object
behavior.

**Overrides:** equals

in class

Rectangle
**Parameters:** obj

- the object to compare this font with
**Returns:** true

if the objects are equal;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

Field Detail

- UPDATE_WHEN_ON_EDT

```java
public static final int UPDATE_WHEN_ON_EDT
```

Indicates that the caret position is to be updated only when
document changes are performed on the Event Dispatching Thread.

**Since:** 1.5
**See Also:** setUpdatePolicy(int)

,

getUpdatePolicy()

,

Constant Field Values

- NEVER_UPDATE

```java
public static final int NEVER_UPDATE
```

Indicates that the caret should remain at the same
absolute position in the document regardless of any document
updates, except when the document length becomes less than
the current caret position due to removal. In that case the caret
position is adjusted to the end of the document.

**Since:** 1.5
**See Also:** setUpdatePolicy(int)

,

getUpdatePolicy()

,

Constant Field Values

- ALWAYS_UPDATE

```java
public static final int ALWAYS_UPDATE
```

Indicates that the caret position is to be

always

updated accordingly to the document changes regardless whether
the document updates are performed on the Event Dispatching Thread
or not.

**Since:** 1.5
**See Also:** setUpdatePolicy(int)

,

getUpdatePolicy()

,

Constant Field Values

- listenerList

```java
protected
EventListenerList
listenerList
```

The event listener list.

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

The change event for the model.
Only one ChangeEvent is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

---

#### Field Detail

UPDATE_WHEN_ON_EDT

```java
public static final int UPDATE_WHEN_ON_EDT
```

Indicates that the caret position is to be updated only when
document changes are performed on the Event Dispatching Thread.

**Since:** 1.5
**See Also:** setUpdatePolicy(int)

,

getUpdatePolicy()

,

Constant Field Values

---

#### UPDATE_WHEN_ON_EDT

public static final int UPDATE_WHEN_ON_EDT

Indicates that the caret position is to be updated only when
document changes are performed on the Event Dispatching Thread.

NEVER_UPDATE

```java
public static final int NEVER_UPDATE
```

Indicates that the caret should remain at the same
absolute position in the document regardless of any document
updates, except when the document length becomes less than
the current caret position due to removal. In that case the caret
position is adjusted to the end of the document.

**Since:** 1.5
**See Also:** setUpdatePolicy(int)

,

getUpdatePolicy()

,

Constant Field Values

---

#### NEVER_UPDATE

public static final int NEVER_UPDATE

Indicates that the caret should remain at the same
absolute position in the document regardless of any document
updates, except when the document length becomes less than
the current caret position due to removal. In that case the caret
position is adjusted to the end of the document.

ALWAYS_UPDATE

```java
public static final int ALWAYS_UPDATE
```

Indicates that the caret position is to be

always

updated accordingly to the document changes regardless whether
the document updates are performed on the Event Dispatching Thread
or not.

**Since:** 1.5
**See Also:** setUpdatePolicy(int)

,

getUpdatePolicy()

,

Constant Field Values

---

#### ALWAYS_UPDATE

public static final int ALWAYS_UPDATE

Indicates that the caret position is to be

always

updated accordingly to the document changes regardless whether
the document updates are performed on the Event Dispatching Thread
or not.

listenerList

```java
protected
EventListenerList
listenerList
```

The event listener list.

---

#### listenerList

protected

EventListenerList

listenerList

The event listener list.

changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

The change event for the model.
Only one ChangeEvent is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

---

#### changeEvent

protected transient

ChangeEvent

changeEvent

The change event for the model.
Only one ChangeEvent is needed per model instance since the
event's only (read-only) state is the source property. The source
of events generated here is always "this".

Constructor Detail

- DefaultCaret

```java
public DefaultCaret()
```

Constructs a default caret.

---

#### Constructor Detail

DefaultCaret

```java
public DefaultCaret()
```

Constructs a default caret.

---

#### DefaultCaret

public DefaultCaret()

Constructs a default caret.

Method Detail

- setUpdatePolicy

```java
public void setUpdatePolicy​(int policy)
```

Sets the caret movement policy on the document updates. Normally
the caret updates its absolute position within the document on
insertions occurred before or at the caret position and
on removals before the caret position. 'Absolute position'
means here the position relative to the start of the document.
For example if
a character is typed within editable text component it is inserted
at the caret position and the caret moves to the next absolute
position within the document due to insertion and if

BACKSPACE

is typed then caret decreases its absolute
position due to removal of a character before it. Sometimes
it may be useful to turn off the caret position updates so that
the caret stays at the same absolute position within the
document position regardless of any document updates.

The following update policies are allowed:

- NEVER_UPDATE

: the caret stays at the same
absolute position in the document regardless of any document
updates, except when document length becomes less than
the current caret position due to removal. In that case caret
position is adjusted to the end of the document.
The caret doesn't try to keep itself visible by scrolling
the associated view when using this policy.
- ALWAYS_UPDATE

: the caret always tracks document
changes. For regular changes it increases its position
if an insertion occurs before or at its current position,
and decreases position if a removal occurs before
its current position. For undo/redo updates it is always
moved to the position where update occurred. The caret
also tries to keep itself visible by calling

adjustVisibility

method.
- UPDATE_WHEN_ON_EDT

: acts like

ALWAYS_UPDATE

if the document updates are performed on the Event Dispatching Thread
and like

NEVER_UPDATE

if updates are performed on
other thread.

The default property value is

UPDATE_WHEN_ON_EDT

.

**Parameters:** policy

- one of the following values :

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE
**Throws:** IllegalArgumentException

- if invalid value is passed
**Since:** 1.5
**See Also:** getUpdatePolicy()

,

adjustVisibility(java.awt.Rectangle)

,

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE

- getUpdatePolicy

```java
public int getUpdatePolicy()
```

Gets the caret movement policy on document updates.

**Returns:** one of the following values :

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE
**Since:** 1.5
**See Also:** setUpdatePolicy(int)

,

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE

- getComponent

```java
protected final
JTextComponent
getComponent()
```

Gets the text editor component that this caret is
is bound to.

**Returns:** the component

- repaint

```java
protected final void repaint()
```

Cause the caret to be painted. The repaint
area is the bounding box of the caret (i.e.
the caret rectangle or

this

).

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

- damage

```java
protected void damage​(
Rectangle
r)
```

Damages the area surrounding the caret to cause
it to be repainted in a new location. If paint()
is reimplemented, this method should also be
reimplemented. This method should update the
caret bounds (x, y, width, and height).

**Parameters:** r

- the current location of the caret
**See Also:** paint(java.awt.Graphics)

- adjustVisibility

```java
protected void adjustVisibility​(
Rectangle
nloc)
```

Scrolls the associated view (if necessary) to make
the caret visible. Since how this should be done
is somewhat of a policy, this method can be
reimplemented to change the behavior. By default
the scrollRectToVisible method is called on the
associated component.

**Parameters:** nloc

- the new position to scroll to

- getSelectionPainter

```java
protected
Highlighter.HighlightPainter
getSelectionPainter()
```

Gets the painter for the Highlighter.

**Returns:** the painter

- positionCaret

```java
protected void positionCaret​(
MouseEvent
e)
```

Tries to set the position of the caret from
the coordinates of a mouse event, using viewToModel().

**Parameters:** e

- the mouse event

- moveCaret

```java
protected void moveCaret​(
MouseEvent
e)
```

Tries to move the position of the caret from
the coordinates of a mouse event, using viewToModel().
This will cause a selection if the dot and mark
are different.

**Parameters:** e

- the mouse event

- focusGained

```java
public void focusGained​(
FocusEvent
e)
```

Called when the component containing the caret gains
focus. This is implemented to set the caret to visible
if the component is editable.

**Specified by:** focusGained

in interface

FocusListener
**Parameters:** e

- the focus event
**See Also:** FocusListener.focusGained(java.awt.event.FocusEvent)

- focusLost

```java
public void focusLost​(
FocusEvent
e)
```

Called when the component containing the caret loses
focus. This is implemented to set the caret to visibility
to false.

**Specified by:** focusLost

in interface

FocusListener
**Parameters:** e

- the focus event
**See Also:** FocusListener.focusLost(java.awt.event.FocusEvent)

- mouseClicked

```java
public void mouseClicked​(
MouseEvent
e)
```

Called when the mouse is clicked. If the click was generated
from button1, a double click selects a word,
and a triple click the current line.

**Specified by:** mouseClicked

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseClicked(java.awt.event.MouseEvent)

- mousePressed

```java
public void mousePressed​(
MouseEvent
e)
```

If button 1 is pressed, this is implemented to
request focus on the associated text component,
and to set the caret position. If the shift key is held down,
the caret will be moved, potentially resulting in a selection,
otherwise the
caret position will be set to the new location. If the component
is not enabled, there will be no request for focus.

**Specified by:** mousePressed

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mousePressed(java.awt.event.MouseEvent)

- mouseReleased

```java
public void mouseReleased​(
MouseEvent
e)
```

Called when the mouse is released.

**Specified by:** mouseReleased

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseReleased(java.awt.event.MouseEvent)

- mouseEntered

```java
public void mouseEntered​(
MouseEvent
e)
```

Called when the mouse enters a region.

**Specified by:** mouseEntered

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseEntered(java.awt.event.MouseEvent)

- mouseExited

```java
public void mouseExited​(
MouseEvent
e)
```

Called when the mouse exits a region.

**Specified by:** mouseExited

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseExited(java.awt.event.MouseEvent)

- mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Moves the caret position
according to the mouse pointer's current
location. This effectively extends the
selection. By default, this is only done
for mouse button 1.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the mouse event
**See Also:** MouseMotionListener.mouseDragged(java.awt.event.MouseEvent)

- mouseMoved

```java
public void mouseMoved​(
MouseEvent
e)
```

Called when the mouse is moved.

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Parameters:** e

- the mouse event
**See Also:** MouseMotionListener.mouseMoved(java.awt.event.MouseEvent)

- paint

```java
public void paint​(
Graphics
g)
```

Renders the caret as a vertical line. If this is reimplemented
the damage method should also be reimplemented as it assumes the
shape of the caret is a vertical line. Sets the caret color to
the value returned by getCaretColor().

If there are multiple text directions present in the associated
document, a flag indicating the caret bias will be rendered.
This will occur only if the associated document is a subclass
of AbstractDocument and there are multiple bidi levels present
in the bidi element structure (i.e. the text has multiple
directions associated with it).

**Specified by:** paint

in interface

Caret
**Parameters:** g

- the graphics context
**See Also:** damage(java.awt.Rectangle)

- install

```java
public void install​(
JTextComponent
c)
```

Called when the UI is being installed into the
interface of a JTextComponent. This can be used
to gain access to the model that is being navigated
by the implementation of this interface. Sets the dot
and mark to 0, and establishes document, property change,
focus, mouse, and mouse motion listeners.

**Specified by:** install

in interface

Caret
**Parameters:** c

- the component
**See Also:** Caret.install(javax.swing.text.JTextComponent)

- deinstall

```java
public void deinstall​(
JTextComponent
c)
```

Called when the UI is being removed from the
interface of a JTextComponent. This is used to
unregister any listeners that were attached.

**Specified by:** deinstall

in interface

Caret
**Parameters:** c

- the component
**See Also:** Caret.deinstall(javax.swing.text.JTextComponent)

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a listener to track whenever the caret position has
been changed.

**Specified by:** addChangeListener

in interface

Caret
**Parameters:** l

- the listener
**See Also:** Caret.addChangeListener(javax.swing.event.ChangeListener)

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a listener that was tracking caret position changes.

**Specified by:** removeChangeListener

in interface

Caret
**Parameters:** l

- the listener
**See Also:** Caret.removeChangeListener(javax.swing.event.ChangeListener)

- getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the change listeners
registered on this caret.

**Returns:** all of this caret's

ChangeListener

s
or an empty
array if no change listeners are currently registered
**Since:** 1.4
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

- fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method. The listener list is processed last to first.

**See Also:** EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this caret.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a

DefaultCaret

c

for its change listeners with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(c.getListeners(ChangeListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getChangeListeners()

- setSelectionVisible

```java
public void setSelectionVisible​(boolean vis)
```

Changes the selection visibility.

**Specified by:** setSelectionVisible

in interface

Caret
**Parameters:** vis

- the new visibility

- isSelectionVisible

```java
public boolean isSelectionVisible()
```

Checks whether the current selection is visible.

**Specified by:** isSelectionVisible

in interface

Caret
**Returns:** true if the selection is visible

- isActive

```java
public boolean isActive()
```

Determines if the caret is currently active.

This method returns whether or not the

Caret

is currently in a blinking state. It does not provide
information as to whether it is currently blinked on or off.
To determine if the caret is currently painted use the

isVisible

method.

**Returns:** true

if active else

false
**Since:** 1.5
**See Also:** isVisible()

- isVisible

```java
public boolean isVisible()
```

Indicates whether or not the caret is currently visible. As the
caret flashes on and off the return value of this will change
between true, when the caret is painted, and false, when the
caret is not painted.

isActive

indicates whether
or not the caret is in a blinking state, such that it

can

be visible, and

isVisible

indicates whether or not
the caret

is

actually visible.

Subclasses that wish to render a different flashing caret
should override paint and only paint the caret if this method
returns true.

**Specified by:** isVisible

in interface

Caret
**Returns:** true if visible else false
**See Also:** Caret.isVisible()

,

isActive()

- setVisible

```java
public void setVisible​(boolean e)
```

Sets the caret visibility, and repaints the caret.
It is important to understand the relationship between this method,

isVisible

and

isActive

.
Calling this method with a value of

true

activates the
caret blinking. Setting it to

false

turns it completely off.
To determine whether the blinking is active, you should call

isActive

. In effect,

isActive

is an
appropriate corresponding "getter" method for this one.

isVisible

can be used to fetch the current
visibility status of the caret, meaning whether or not it is currently
painted. This status will change as the caret blinks on and off.

Here's a list showing the potential return values of both

isActive

and

isVisible

after calling this method:

setVisible(true)

:

- isActive(): true
- isVisible(): true or false depending on whether
or not the caret is blinked on or off

setVisible(false)

:

- isActive(): false
- isVisible(): false

**Specified by:** setVisible

in interface

Caret
**Parameters:** e

- the visibility specifier
**See Also:** isActive()

,

Caret.setVisible(boolean)

- setBlinkRate

```java
public void setBlinkRate​(int rate)
```

Sets the caret blink rate.

**Specified by:** setBlinkRate

in interface

Caret
**Parameters:** rate

- the rate in milliseconds, 0 to stop blinking
**See Also:** Caret.setBlinkRate(int)

- getBlinkRate

```java
public int getBlinkRate()
```

Gets the caret blink rate.

**Specified by:** getBlinkRate

in interface

Caret
**Returns:** the delay in milliseconds. If this is
zero the caret will not blink.
**See Also:** Caret.getBlinkRate()

- getDot

```java
public int getDot()
```

Fetches the current position of the caret.

**Specified by:** getDot

in interface

Caret
**Returns:** the position >= 0
**See Also:** Caret.getDot()

- getMark

```java
public int getMark()
```

Fetches the current position of the mark. If there is a selection,
the dot and mark will not be the same.

**Specified by:** getMark

in interface

Caret
**Returns:** the position >= 0
**See Also:** Caret.getMark()

- setDot

```java
public void setDot​(int dot)
```

Sets the caret position and mark to the specified position,
with a forward bias. This implicitly sets the
selection range to zero.

**Specified by:** setDot

in interface

Caret
**Parameters:** dot

- the position >= 0
**See Also:** setDot(int, Position.Bias)

,

Caret.setDot(int)

- moveDot

```java
public void moveDot​(int dot)
```

Moves the caret position to the specified position,
with a forward bias.

**Specified by:** moveDot

in interface

Caret
**Parameters:** dot

- the position >= 0
**See Also:** moveDot(int, javax.swing.text.Position.Bias)

,

Caret.moveDot(int)

- moveDot

```java
public void moveDot​(int dot,

Position.Bias
dotBias)
```

Moves the caret position to the specified position, with the
specified bias.

**Parameters:** dot

- the position >= 0
**Parameters:** dotBias

- the bias for this position, not

null
**Throws:** IllegalArgumentException

- if the bias is

null
**Since:** 1.6
**See Also:** Caret.moveDot(int)

- setDot

```java
public void setDot​(int dot,

Position.Bias
dotBias)
```

Sets the caret position and mark to the specified position, with the
specified bias. This implicitly sets the selection range
to zero.

**Parameters:** dot

- the position >= 0
**Parameters:** dotBias

- the bias for this position, not

null
**Throws:** IllegalArgumentException

- if the bias is

null
**Since:** 1.6
**See Also:** Caret.setDot(int)

- getDotBias

```java
public
Position.Bias
getDotBias()
```

Returns the bias of the caret position.

**Returns:** the bias of the caret position
**Since:** 1.6

- getMarkBias

```java
public
Position.Bias
getMarkBias()
```

Returns the bias of the mark.

**Returns:** the bias of the mark
**Since:** 1.6

- setMagicCaretPosition

```java
public void setMagicCaretPosition​(
Point
p)
```

Saves the current caret position. This is used when
caret up/down actions occur, moving between lines
that have uneven end positions.

**Specified by:** setMagicCaretPosition

in interface

Caret
**Parameters:** p

- the position
**See Also:** getMagicCaretPosition()

- getMagicCaretPosition

```java
public
Point
getMagicCaretPosition()
```

Gets the saved caret position.

**Specified by:** getMagicCaretPosition

in interface

Caret
**Returns:** the position
see #setMagicCaretPosition
**See Also:** Caret.setMagicCaretPosition(java.awt.Point)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this object to the specified object.
The superclass behavior of comparing rectangles
is not desired, so this is changed to the Object
behavior.

**Overrides:** equals

in class

Rectangle
**Parameters:** obj

- the object to compare this font with
**Returns:** true

if the objects are equal;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

setUpdatePolicy

```java
public void setUpdatePolicy​(int policy)
```

Sets the caret movement policy on the document updates. Normally
the caret updates its absolute position within the document on
insertions occurred before or at the caret position and
on removals before the caret position. 'Absolute position'
means here the position relative to the start of the document.
For example if
a character is typed within editable text component it is inserted
at the caret position and the caret moves to the next absolute
position within the document due to insertion and if

BACKSPACE

is typed then caret decreases its absolute
position due to removal of a character before it. Sometimes
it may be useful to turn off the caret position updates so that
the caret stays at the same absolute position within the
document position regardless of any document updates.

The following update policies are allowed:

- NEVER_UPDATE

: the caret stays at the same
absolute position in the document regardless of any document
updates, except when document length becomes less than
the current caret position due to removal. In that case caret
position is adjusted to the end of the document.
The caret doesn't try to keep itself visible by scrolling
the associated view when using this policy.
- ALWAYS_UPDATE

: the caret always tracks document
changes. For regular changes it increases its position
if an insertion occurs before or at its current position,
and decreases position if a removal occurs before
its current position. For undo/redo updates it is always
moved to the position where update occurred. The caret
also tries to keep itself visible by calling

adjustVisibility

method.
- UPDATE_WHEN_ON_EDT

: acts like

ALWAYS_UPDATE

if the document updates are performed on the Event Dispatching Thread
and like

NEVER_UPDATE

if updates are performed on
other thread.

The default property value is

UPDATE_WHEN_ON_EDT

.

**Parameters:** policy

- one of the following values :

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE
**Throws:** IllegalArgumentException

- if invalid value is passed
**Since:** 1.5
**See Also:** getUpdatePolicy()

,

adjustVisibility(java.awt.Rectangle)

,

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE

---

#### setUpdatePolicy

public void setUpdatePolicy​(int policy)

Sets the caret movement policy on the document updates. Normally
the caret updates its absolute position within the document on
insertions occurred before or at the caret position and
on removals before the caret position. 'Absolute position'
means here the position relative to the start of the document.
For example if
a character is typed within editable text component it is inserted
at the caret position and the caret moves to the next absolute
position within the document due to insertion and if

BACKSPACE

is typed then caret decreases its absolute
position due to removal of a character before it. Sometimes
it may be useful to turn off the caret position updates so that
the caret stays at the same absolute position within the
document position regardless of any document updates.

The following update policies are allowed:

- NEVER_UPDATE

: the caret stays at the same
absolute position in the document regardless of any document
updates, except when document length becomes less than
the current caret position due to removal. In that case caret
position is adjusted to the end of the document.
The caret doesn't try to keep itself visible by scrolling
the associated view when using this policy.
- ALWAYS_UPDATE

: the caret always tracks document
changes. For regular changes it increases its position
if an insertion occurs before or at its current position,
and decreases position if a removal occurs before
its current position. For undo/redo updates it is always
moved to the position where update occurred. The caret
also tries to keep itself visible by calling

adjustVisibility

method.
- UPDATE_WHEN_ON_EDT

: acts like

ALWAYS_UPDATE

if the document updates are performed on the Event Dispatching Thread
and like

NEVER_UPDATE

if updates are performed on
other thread.

The default property value is

UPDATE_WHEN_ON_EDT

.

The following update policies are allowed:

- NEVER_UPDATE

: the caret stays at the same
absolute position in the document regardless of any document
updates, except when document length becomes less than
the current caret position due to removal. In that case caret
position is adjusted to the end of the document.
The caret doesn't try to keep itself visible by scrolling
the associated view when using this policy.
- ALWAYS_UPDATE

: the caret always tracks document
changes. For regular changes it increases its position
if an insertion occurs before or at its current position,
and decreases position if a removal occurs before
its current position. For undo/redo updates it is always
moved to the position where update occurred. The caret
also tries to keep itself visible by calling

adjustVisibility

method.
- UPDATE_WHEN_ON_EDT

: acts like

ALWAYS_UPDATE

if the document updates are performed on the Event Dispatching Thread
and like

NEVER_UPDATE

if updates are performed on
other thread.

The default property value is

UPDATE_WHEN_ON_EDT

.

NEVER_UPDATE

: the caret stays at the same
absolute position in the document regardless of any document
updates, except when document length becomes less than
the current caret position due to removal. In that case caret
position is adjusted to the end of the document.
The caret doesn't try to keep itself visible by scrolling
the associated view when using this policy.

ALWAYS_UPDATE

: the caret always tracks document
changes. For regular changes it increases its position
if an insertion occurs before or at its current position,
and decreases position if a removal occurs before
its current position. For undo/redo updates it is always
moved to the position where update occurred. The caret
also tries to keep itself visible by calling

adjustVisibility

method.

UPDATE_WHEN_ON_EDT

: acts like

ALWAYS_UPDATE

if the document updates are performed on the Event Dispatching Thread
and like

NEVER_UPDATE

if updates are performed on
other thread.

The default property value is

UPDATE_WHEN_ON_EDT

.

getUpdatePolicy

```java
public int getUpdatePolicy()
```

Gets the caret movement policy on document updates.

**Returns:** one of the following values :

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE
**Since:** 1.5
**See Also:** setUpdatePolicy(int)

,

UPDATE_WHEN_ON_EDT

,

NEVER_UPDATE

,

ALWAYS_UPDATE

---

#### getUpdatePolicy

public int getUpdatePolicy()

Gets the caret movement policy on document updates.

getComponent

```java
protected final
JTextComponent
getComponent()
```

Gets the text editor component that this caret is
is bound to.

**Returns:** the component

---

#### getComponent

protected final

JTextComponent

getComponent()

Gets the text editor component that this caret is
is bound to.

repaint

```java
protected final void repaint()
```

Cause the caret to be painted. The repaint
area is the bounding box of the caret (i.e.
the caret rectangle or

this

).

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

---

#### repaint

protected final void repaint()

Cause the caret to be painted. The repaint
area is the bounding box of the caret (i.e.
the caret rectangle or

this

).

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

This method is thread safe, although most Swing methods
are not. Please see

Concurrency
in Swing

for more information.

damage

```java
protected void damage​(
Rectangle
r)
```

Damages the area surrounding the caret to cause
it to be repainted in a new location. If paint()
is reimplemented, this method should also be
reimplemented. This method should update the
caret bounds (x, y, width, and height).

**Parameters:** r

- the current location of the caret
**See Also:** paint(java.awt.Graphics)

---

#### damage

protected void damage​(

Rectangle

r)

Damages the area surrounding the caret to cause
it to be repainted in a new location. If paint()
is reimplemented, this method should also be
reimplemented. This method should update the
caret bounds (x, y, width, and height).

adjustVisibility

```java
protected void adjustVisibility​(
Rectangle
nloc)
```

Scrolls the associated view (if necessary) to make
the caret visible. Since how this should be done
is somewhat of a policy, this method can be
reimplemented to change the behavior. By default
the scrollRectToVisible method is called on the
associated component.

**Parameters:** nloc

- the new position to scroll to

---

#### adjustVisibility

protected void adjustVisibility​(

Rectangle

nloc)

Scrolls the associated view (if necessary) to make
the caret visible. Since how this should be done
is somewhat of a policy, this method can be
reimplemented to change the behavior. By default
the scrollRectToVisible method is called on the
associated component.

getSelectionPainter

```java
protected
Highlighter.HighlightPainter
getSelectionPainter()
```

Gets the painter for the Highlighter.

**Returns:** the painter

---

#### getSelectionPainter

protected

Highlighter.HighlightPainter

getSelectionPainter()

Gets the painter for the Highlighter.

positionCaret

```java
protected void positionCaret​(
MouseEvent
e)
```

Tries to set the position of the caret from
the coordinates of a mouse event, using viewToModel().

**Parameters:** e

- the mouse event

---

#### positionCaret

protected void positionCaret​(

MouseEvent

e)

Tries to set the position of the caret from
the coordinates of a mouse event, using viewToModel().

moveCaret

```java
protected void moveCaret​(
MouseEvent
e)
```

Tries to move the position of the caret from
the coordinates of a mouse event, using viewToModel().
This will cause a selection if the dot and mark
are different.

**Parameters:** e

- the mouse event

---

#### moveCaret

protected void moveCaret​(

MouseEvent

e)

Tries to move the position of the caret from
the coordinates of a mouse event, using viewToModel().
This will cause a selection if the dot and mark
are different.

focusGained

```java
public void focusGained​(
FocusEvent
e)
```

Called when the component containing the caret gains
focus. This is implemented to set the caret to visible
if the component is editable.

**Specified by:** focusGained

in interface

FocusListener
**Parameters:** e

- the focus event
**See Also:** FocusListener.focusGained(java.awt.event.FocusEvent)

---

#### focusGained

public void focusGained​(

FocusEvent

e)

Called when the component containing the caret gains
focus. This is implemented to set the caret to visible
if the component is editable.

focusLost

```java
public void focusLost​(
FocusEvent
e)
```

Called when the component containing the caret loses
focus. This is implemented to set the caret to visibility
to false.

**Specified by:** focusLost

in interface

FocusListener
**Parameters:** e

- the focus event
**See Also:** FocusListener.focusLost(java.awt.event.FocusEvent)

---

#### focusLost

public void focusLost​(

FocusEvent

e)

Called when the component containing the caret loses
focus. This is implemented to set the caret to visibility
to false.

mouseClicked

```java
public void mouseClicked​(
MouseEvent
e)
```

Called when the mouse is clicked. If the click was generated
from button1, a double click selects a word,
and a triple click the current line.

**Specified by:** mouseClicked

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseClicked(java.awt.event.MouseEvent)

---

#### mouseClicked

public void mouseClicked​(

MouseEvent

e)

Called when the mouse is clicked. If the click was generated
from button1, a double click selects a word,
and a triple click the current line.

mousePressed

```java
public void mousePressed​(
MouseEvent
e)
```

If button 1 is pressed, this is implemented to
request focus on the associated text component,
and to set the caret position. If the shift key is held down,
the caret will be moved, potentially resulting in a selection,
otherwise the
caret position will be set to the new location. If the component
is not enabled, there will be no request for focus.

**Specified by:** mousePressed

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mousePressed(java.awt.event.MouseEvent)

---

#### mousePressed

public void mousePressed​(

MouseEvent

e)

If button 1 is pressed, this is implemented to
request focus on the associated text component,
and to set the caret position. If the shift key is held down,
the caret will be moved, potentially resulting in a selection,
otherwise the
caret position will be set to the new location. If the component
is not enabled, there will be no request for focus.

mouseReleased

```java
public void mouseReleased​(
MouseEvent
e)
```

Called when the mouse is released.

**Specified by:** mouseReleased

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseReleased(java.awt.event.MouseEvent)

---

#### mouseReleased

public void mouseReleased​(

MouseEvent

e)

Called when the mouse is released.

mouseEntered

```java
public void mouseEntered​(
MouseEvent
e)
```

Called when the mouse enters a region.

**Specified by:** mouseEntered

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseEntered(java.awt.event.MouseEvent)

---

#### mouseEntered

public void mouseEntered​(

MouseEvent

e)

Called when the mouse enters a region.

mouseExited

```java
public void mouseExited​(
MouseEvent
e)
```

Called when the mouse exits a region.

**Specified by:** mouseExited

in interface

MouseListener
**Parameters:** e

- the mouse event
**See Also:** MouseListener.mouseExited(java.awt.event.MouseEvent)

---

#### mouseExited

public void mouseExited​(

MouseEvent

e)

Called when the mouse exits a region.

mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Moves the caret position
according to the mouse pointer's current
location. This effectively extends the
selection. By default, this is only done
for mouse button 1.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the mouse event
**See Also:** MouseMotionListener.mouseDragged(java.awt.event.MouseEvent)

---

#### mouseDragged

public void mouseDragged​(

MouseEvent

e)

Moves the caret position
according to the mouse pointer's current
location. This effectively extends the
selection. By default, this is only done
for mouse button 1.

mouseMoved

```java
public void mouseMoved​(
MouseEvent
e)
```

Called when the mouse is moved.

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Parameters:** e

- the mouse event
**See Also:** MouseMotionListener.mouseMoved(java.awt.event.MouseEvent)

---

#### mouseMoved

public void mouseMoved​(

MouseEvent

e)

Called when the mouse is moved.

paint

```java
public void paint​(
Graphics
g)
```

Renders the caret as a vertical line. If this is reimplemented
the damage method should also be reimplemented as it assumes the
shape of the caret is a vertical line. Sets the caret color to
the value returned by getCaretColor().

If there are multiple text directions present in the associated
document, a flag indicating the caret bias will be rendered.
This will occur only if the associated document is a subclass
of AbstractDocument and there are multiple bidi levels present
in the bidi element structure (i.e. the text has multiple
directions associated with it).

**Specified by:** paint

in interface

Caret
**Parameters:** g

- the graphics context
**See Also:** damage(java.awt.Rectangle)

---

#### paint

public void paint​(

Graphics

g)

Renders the caret as a vertical line. If this is reimplemented
the damage method should also be reimplemented as it assumes the
shape of the caret is a vertical line. Sets the caret color to
the value returned by getCaretColor().

If there are multiple text directions present in the associated
document, a flag indicating the caret bias will be rendered.
This will occur only if the associated document is a subclass
of AbstractDocument and there are multiple bidi levels present
in the bidi element structure (i.e. the text has multiple
directions associated with it).

If there are multiple text directions present in the associated
document, a flag indicating the caret bias will be rendered.
This will occur only if the associated document is a subclass
of AbstractDocument and there are multiple bidi levels present
in the bidi element structure (i.e. the text has multiple
directions associated with it).

install

```java
public void install​(
JTextComponent
c)
```

Called when the UI is being installed into the
interface of a JTextComponent. This can be used
to gain access to the model that is being navigated
by the implementation of this interface. Sets the dot
and mark to 0, and establishes document, property change,
focus, mouse, and mouse motion listeners.

**Specified by:** install

in interface

Caret
**Parameters:** c

- the component
**See Also:** Caret.install(javax.swing.text.JTextComponent)

---

#### install

public void install​(

JTextComponent

c)

Called when the UI is being installed into the
interface of a JTextComponent. This can be used
to gain access to the model that is being navigated
by the implementation of this interface. Sets the dot
and mark to 0, and establishes document, property change,
focus, mouse, and mouse motion listeners.

deinstall

```java
public void deinstall​(
JTextComponent
c)
```

Called when the UI is being removed from the
interface of a JTextComponent. This is used to
unregister any listeners that were attached.

**Specified by:** deinstall

in interface

Caret
**Parameters:** c

- the component
**See Also:** Caret.deinstall(javax.swing.text.JTextComponent)

---

#### deinstall

public void deinstall​(

JTextComponent

c)

Called when the UI is being removed from the
interface of a JTextComponent. This is used to
unregister any listeners that were attached.

addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a listener to track whenever the caret position has
been changed.

**Specified by:** addChangeListener

in interface

Caret
**Parameters:** l

- the listener
**See Also:** Caret.addChangeListener(javax.swing.event.ChangeListener)

---

#### addChangeListener

public void addChangeListener​(

ChangeListener

l)

Adds a listener to track whenever the caret position has
been changed.

removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a listener that was tracking caret position changes.

**Specified by:** removeChangeListener

in interface

Caret
**Parameters:** l

- the listener
**See Also:** Caret.removeChangeListener(javax.swing.event.ChangeListener)

---

#### removeChangeListener

public void removeChangeListener​(

ChangeListener

l)

Removes a listener that was tracking caret position changes.

getChangeListeners

```java
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the change listeners
registered on this caret.

**Returns:** all of this caret's

ChangeListener

s
or an empty
array if no change listeners are currently registered
**Since:** 1.4
**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

---

#### getChangeListeners

public

ChangeListener

[] getChangeListeners()

Returns an array of all the change listeners
registered on this caret.

fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method. The listener list is processed last to first.

**See Also:** EventListenerList

---

#### fireStateChanged

protected void fireStateChanged()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the parameters passed into
the fire method. The listener list is processed last to first.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this caret.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a

DefaultCaret

c

for its change listeners with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(c.getListeners(ChangeListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getChangeListeners()

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this caret.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a

DefaultCaret

c

for its change listeners with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(c.getListeners(ChangeListener.class));
```

If no such listeners exist, this method returns an empty array.

You can specify the

listenerType

argument
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a

DefaultCaret

c

for its change listeners with the following code:

```java
ChangeListener[] cls = (ChangeListener[])(c.getListeners(ChangeListener.class));
```

If no such listeners exist, this method returns an empty array.

ChangeListener[] cls = (ChangeListener[])(c.getListeners(ChangeListener.class));

setSelectionVisible

```java
public void setSelectionVisible​(boolean vis)
```

Changes the selection visibility.

**Specified by:** setSelectionVisible

in interface

Caret
**Parameters:** vis

- the new visibility

---

#### setSelectionVisible

public void setSelectionVisible​(boolean vis)

Changes the selection visibility.

isSelectionVisible

```java
public boolean isSelectionVisible()
```

Checks whether the current selection is visible.

**Specified by:** isSelectionVisible

in interface

Caret
**Returns:** true if the selection is visible

---

#### isSelectionVisible

public boolean isSelectionVisible()

Checks whether the current selection is visible.

isActive

```java
public boolean isActive()
```

Determines if the caret is currently active.

This method returns whether or not the

Caret

is currently in a blinking state. It does not provide
information as to whether it is currently blinked on or off.
To determine if the caret is currently painted use the

isVisible

method.

**Returns:** true

if active else

false
**Since:** 1.5
**See Also:** isVisible()

---

#### isActive

public boolean isActive()

Determines if the caret is currently active.

This method returns whether or not the

Caret

is currently in a blinking state. It does not provide
information as to whether it is currently blinked on or off.
To determine if the caret is currently painted use the

isVisible

method.

This method returns whether or not the

Caret

is currently in a blinking state. It does not provide
information as to whether it is currently blinked on or off.
To determine if the caret is currently painted use the

isVisible

method.

isVisible

```java
public boolean isVisible()
```

Indicates whether or not the caret is currently visible. As the
caret flashes on and off the return value of this will change
between true, when the caret is painted, and false, when the
caret is not painted.

isActive

indicates whether
or not the caret is in a blinking state, such that it

can

be visible, and

isVisible

indicates whether or not
the caret

is

actually visible.

Subclasses that wish to render a different flashing caret
should override paint and only paint the caret if this method
returns true.

**Specified by:** isVisible

in interface

Caret
**Returns:** true if visible else false
**See Also:** Caret.isVisible()

,

isActive()

---

#### isVisible

public boolean isVisible()

Indicates whether or not the caret is currently visible. As the
caret flashes on and off the return value of this will change
between true, when the caret is painted, and false, when the
caret is not painted.

isActive

indicates whether
or not the caret is in a blinking state, such that it

can

be visible, and

isVisible

indicates whether or not
the caret

is

actually visible.

Subclasses that wish to render a different flashing caret
should override paint and only paint the caret if this method
returns true.

Subclasses that wish to render a different flashing caret
should override paint and only paint the caret if this method
returns true.

setVisible

```java
public void setVisible​(boolean e)
```

Sets the caret visibility, and repaints the caret.
It is important to understand the relationship between this method,

isVisible

and

isActive

.
Calling this method with a value of

true

activates the
caret blinking. Setting it to

false

turns it completely off.
To determine whether the blinking is active, you should call

isActive

. In effect,

isActive

is an
appropriate corresponding "getter" method for this one.

isVisible

can be used to fetch the current
visibility status of the caret, meaning whether or not it is currently
painted. This status will change as the caret blinks on and off.

Here's a list showing the potential return values of both

isActive

and

isVisible

after calling this method:

setVisible(true)

:

- isActive(): true
- isVisible(): true or false depending on whether
or not the caret is blinked on or off

setVisible(false)

:

- isActive(): false
- isVisible(): false

**Specified by:** setVisible

in interface

Caret
**Parameters:** e

- the visibility specifier
**See Also:** isActive()

,

Caret.setVisible(boolean)

---

#### setVisible

public void setVisible​(boolean e)

Sets the caret visibility, and repaints the caret.
It is important to understand the relationship between this method,

isVisible

and

isActive

.
Calling this method with a value of

true

activates the
caret blinking. Setting it to

false

turns it completely off.
To determine whether the blinking is active, you should call

isActive

. In effect,

isActive

is an
appropriate corresponding "getter" method for this one.

isVisible

can be used to fetch the current
visibility status of the caret, meaning whether or not it is currently
painted. This status will change as the caret blinks on and off.

Here's a list showing the potential return values of both

isActive

and

isVisible

after calling this method:

setVisible(true)

:

- isActive(): true
- isVisible(): true or false depending on whether
or not the caret is blinked on or off

setVisible(false)

:

- isActive(): false
- isVisible(): false

Here's a list showing the potential return values of both

isActive

and

isVisible

after calling this method:

setVisible(true)

:

- isActive(): true
- isVisible(): true or false depending on whether
or not the caret is blinked on or off

setVisible(false)

:

- isActive(): false
- isVisible(): false

setVisible(true)

:

- isActive(): true
- isVisible(): true or false depending on whether
or not the caret is blinked on or off

setVisible(false)

:

- isActive(): false
- isVisible(): false

isActive(): true

isVisible(): true or false depending on whether
or not the caret is blinked on or off

setVisible(false)

:

- isActive(): false
- isVisible(): false

isActive(): false

isVisible(): false

setBlinkRate

```java
public void setBlinkRate​(int rate)
```

Sets the caret blink rate.

**Specified by:** setBlinkRate

in interface

Caret
**Parameters:** rate

- the rate in milliseconds, 0 to stop blinking
**See Also:** Caret.setBlinkRate(int)

---

#### setBlinkRate

public void setBlinkRate​(int rate)

Sets the caret blink rate.

getBlinkRate

```java
public int getBlinkRate()
```

Gets the caret blink rate.

**Specified by:** getBlinkRate

in interface

Caret
**Returns:** the delay in milliseconds. If this is
zero the caret will not blink.
**See Also:** Caret.getBlinkRate()

---

#### getBlinkRate

public int getBlinkRate()

Gets the caret blink rate.

getDot

```java
public int getDot()
```

Fetches the current position of the caret.

**Specified by:** getDot

in interface

Caret
**Returns:** the position >= 0
**See Also:** Caret.getDot()

---

#### getDot

public int getDot()

Fetches the current position of the caret.

getMark

```java
public int getMark()
```

Fetches the current position of the mark. If there is a selection,
the dot and mark will not be the same.

**Specified by:** getMark

in interface

Caret
**Returns:** the position >= 0
**See Also:** Caret.getMark()

---

#### getMark

public int getMark()

Fetches the current position of the mark. If there is a selection,
the dot and mark will not be the same.

setDot

```java
public void setDot​(int dot)
```

Sets the caret position and mark to the specified position,
with a forward bias. This implicitly sets the
selection range to zero.

**Specified by:** setDot

in interface

Caret
**Parameters:** dot

- the position >= 0
**See Also:** setDot(int, Position.Bias)

,

Caret.setDot(int)

---

#### setDot

public void setDot​(int dot)

Sets the caret position and mark to the specified position,
with a forward bias. This implicitly sets the
selection range to zero.

moveDot

```java
public void moveDot​(int dot)
```

Moves the caret position to the specified position,
with a forward bias.

**Specified by:** moveDot

in interface

Caret
**Parameters:** dot

- the position >= 0
**See Also:** moveDot(int, javax.swing.text.Position.Bias)

,

Caret.moveDot(int)

---

#### moveDot

public void moveDot​(int dot)

Moves the caret position to the specified position,
with a forward bias.

moveDot

```java
public void moveDot​(int dot,

Position.Bias
dotBias)
```

Moves the caret position to the specified position, with the
specified bias.

**Parameters:** dot

- the position >= 0
**Parameters:** dotBias

- the bias for this position, not

null
**Throws:** IllegalArgumentException

- if the bias is

null
**Since:** 1.6
**See Also:** Caret.moveDot(int)

---

#### moveDot

public void moveDot​(int dot,

Position.Bias

dotBias)

Moves the caret position to the specified position, with the
specified bias.

setDot

```java
public void setDot​(int dot,

Position.Bias
dotBias)
```

Sets the caret position and mark to the specified position, with the
specified bias. This implicitly sets the selection range
to zero.

**Parameters:** dot

- the position >= 0
**Parameters:** dotBias

- the bias for this position, not

null
**Throws:** IllegalArgumentException

- if the bias is

null
**Since:** 1.6
**See Also:** Caret.setDot(int)

---

#### setDot

public void setDot​(int dot,

Position.Bias

dotBias)

Sets the caret position and mark to the specified position, with the
specified bias. This implicitly sets the selection range
to zero.

getDotBias

```java
public
Position.Bias
getDotBias()
```

Returns the bias of the caret position.

**Returns:** the bias of the caret position
**Since:** 1.6

---

#### getDotBias

public

Position.Bias

getDotBias()

Returns the bias of the caret position.

getMarkBias

```java
public
Position.Bias
getMarkBias()
```

Returns the bias of the mark.

**Returns:** the bias of the mark
**Since:** 1.6

---

#### getMarkBias

public

Position.Bias

getMarkBias()

Returns the bias of the mark.

setMagicCaretPosition

```java
public void setMagicCaretPosition​(
Point
p)
```

Saves the current caret position. This is used when
caret up/down actions occur, moving between lines
that have uneven end positions.

**Specified by:** setMagicCaretPosition

in interface

Caret
**Parameters:** p

- the position
**See Also:** getMagicCaretPosition()

---

#### setMagicCaretPosition

public void setMagicCaretPosition​(

Point

p)

Saves the current caret position. This is used when
caret up/down actions occur, moving between lines
that have uneven end positions.

getMagicCaretPosition

```java
public
Point
getMagicCaretPosition()
```

Gets the saved caret position.

**Specified by:** getMagicCaretPosition

in interface

Caret
**Returns:** the position
see #setMagicCaretPosition
**See Also:** Caret.setMagicCaretPosition(java.awt.Point)

---

#### getMagicCaretPosition

public

Point

getMagicCaretPosition()

Gets the saved caret position.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this object to the specified object.
The superclass behavior of comparing rectangles
is not desired, so this is changed to the Object
behavior.

**Overrides:** equals

in class

Rectangle
**Parameters:** obj

- the object to compare this font with
**Returns:** true

if the objects are equal;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this object to the specified object.
The superclass behavior of comparing rectangles
is not desired, so this is changed to the Object
behavior.

---

