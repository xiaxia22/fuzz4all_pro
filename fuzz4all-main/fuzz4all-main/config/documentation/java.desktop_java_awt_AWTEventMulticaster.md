# Class AWTEventMulticaster

**Source:** `java.desktop\java\awt\AWTEventMulticaster.html`

### Class Description

```java
public class
AWTEventMulticaster

extends
Object

implements
ComponentListener
,
ContainerListener
,
FocusListener
,
KeyListener
,
MouseListener
,
MouseMotionListener
,
WindowListener
,
WindowFocusListener
,
WindowStateListener
,
ActionListener
,
ItemListener
,
AdjustmentListener
,
TextListener
,
InputMethodListener
,
HierarchyListener
,
HierarchyBoundsListener
,
MouseWheelListener
```

AWTEventMulticaster

implements efficient and thread-safe multi-cast
event dispatching for the AWT events defined in the

java.awt.event

package.

The following example illustrates how to use this class:

```java
public myComponent extends Component {
ActionListener actionListener = null;

public synchronized void addActionListener(ActionListener l) {
actionListener = AWTEventMulticaster.add(actionListener, l);
}
public synchronized void removeActionListener(ActionListener l) {
actionListener = AWTEventMulticaster.remove(actionListener, l);
}
public void processEvent(AWTEvent e) {
// when event occurs which causes "action" semantic
ActionListener listener = actionListener;
if (listener != null) {
listener.actionPerformed(new ActionEvent());
}
}
}
```

The important point to note is the first argument to the

add

and

remove

methods is the field maintaining the
listeners. In addition you must assign the result of the

add

and

remove

methods to the field maintaining the listeners.

AWTEventMulticaster

is implemented as a pair of

EventListeners

that are set at construction time.

AWTEventMulticaster

is immutable. The

add

and

remove

methods do not alter

AWTEventMulticaster

in
anyway. If necessary, a new

AWTEventMulticaster

is
created. In this way it is safe to add and remove listeners during
the process of an event dispatching. However, event listeners
added during the process of an event dispatch operation are not
notified of the event currently being dispatched.

All of the

add

methods allow

null

arguments. If the
first argument is

null

, the second argument is returned. If
the first argument is not

null

and the second argument is

null

, the first argument is returned. If both arguments are

non-null

, a new

AWTEventMulticaster

is created using
the two arguments and returned.

For the

remove

methods that take two arguments, the following is
returned:

- null

, if the first argument is

null

, or
the arguments are equal, by way of

==

.

the first argument, if the first argument is not an instance of

AWTEventMulticaster

.

result of invoking

remove(EventListener)

on the
first argument, supplying the second argument to the

remove(EventListener)

method.

Swing makes use of

EventListenerList

for
similar logic. Refer to it for details.

**All Implemented Interfaces:** ActionListener

,

AdjustmentListener

,

ComponentListener

,

ContainerListener

,

FocusListener

,

HierarchyBoundsListener

,

HierarchyListener

,

InputMethodListener

,

ItemListener

,

KeyListener

,

MouseListener

,

MouseMotionListener

,

MouseWheelListener

,

TextListener

,

WindowFocusListener

,

WindowListener

,

WindowStateListener

,

EventListener

---

### Field Details

#### protected final
EventListener
a

A variable in the event chain (listener-a)

---

#### protected final
EventListener
b

A variable in the event chain (listener-b)

---

### Constructor Details

#### protected AWTEventMulticaster​(
EventListener
a,

EventListener
b)

Creates an event multicaster instance which chains listener-a
with listener-b. Input parameters

a

and

b

should not be

null

, though implementations may vary in
choosing whether or not to throw

NullPointerException

in that case.

**Parameters:**
- a

- listener-a
- b

- listener-b

---

### Method Details

#### protected
EventListener
remove​(
EventListener
oldl)

Removes a listener from this multicaster.

The returned multicaster contains all the listeners in this
multicaster with the exception of all occurrences of

oldl

.
If the resulting multicaster contains only one regular listener
the regular listener may be returned. If the resulting multicaster
is empty, then

null

may be returned instead.

No exception is thrown if

oldl

is

null

.

**Parameters:**
- oldl

- the listener to be removed

**Returns:**
- resulting listener

---

#### public void componentResized​(
ComponentEvent
e)

Handles the componentResized event by invoking the
componentResized methods on listener-a and listener-b.

**Specified by:**
- componentResized

in interface

ComponentListener

**Parameters:**
- e

- the component event

---

#### public void componentMoved​(
ComponentEvent
e)

Handles the componentMoved event by invoking the
componentMoved methods on listener-a and listener-b.

**Specified by:**
- componentMoved

in interface

ComponentListener

**Parameters:**
- e

- the component event

---

#### public void componentShown​(
ComponentEvent
e)

Handles the componentShown event by invoking the
componentShown methods on listener-a and listener-b.

**Specified by:**
- componentShown

in interface

ComponentListener

**Parameters:**
- e

- the component event

---

#### public void componentHidden​(
ComponentEvent
e)

Handles the componentHidden event by invoking the
componentHidden methods on listener-a and listener-b.

**Specified by:**
- componentHidden

in interface

ComponentListener

**Parameters:**
- e

- the component event

---

#### public void componentAdded​(
ContainerEvent
e)

Handles the componentAdded container event by invoking the
componentAdded methods on listener-a and listener-b.

**Specified by:**
- componentAdded

in interface

ContainerListener

**Parameters:**
- e

- the component event

---

#### public void componentRemoved​(
ContainerEvent
e)

Handles the componentRemoved container event by invoking the
componentRemoved methods on listener-a and listener-b.

**Specified by:**
- componentRemoved

in interface

ContainerListener

**Parameters:**
- e

- the component event

---

#### public void focusGained​(
FocusEvent
e)

Handles the focusGained event by invoking the
focusGained methods on listener-a and listener-b.

**Specified by:**
- focusGained

in interface

FocusListener

**Parameters:**
- e

- the focus event

---

#### public void focusLost​(
FocusEvent
e)

Handles the focusLost event by invoking the
focusLost methods on listener-a and listener-b.

**Specified by:**
- focusLost

in interface

FocusListener

**Parameters:**
- e

- the focus event

---

#### public void keyTyped​(
KeyEvent
e)

Handles the keyTyped event by invoking the
keyTyped methods on listener-a and listener-b.

**Specified by:**
- keyTyped

in interface

KeyListener

**Parameters:**
- e

- the key event

---

#### public void keyPressed​(
KeyEvent
e)

Handles the keyPressed event by invoking the
keyPressed methods on listener-a and listener-b.

**Specified by:**
- keyPressed

in interface

KeyListener

**Parameters:**
- e

- the key event

---

#### public void keyReleased​(
KeyEvent
e)

Handles the keyReleased event by invoking the
keyReleased methods on listener-a and listener-b.

**Specified by:**
- keyReleased

in interface

KeyListener

**Parameters:**
- e

- the key event

---

#### public void mouseClicked​(
MouseEvent
e)

Handles the mouseClicked event by invoking the
mouseClicked methods on listener-a and listener-b.

**Specified by:**
- mouseClicked

in interface

MouseListener

**Parameters:**
- e

- the mouse event

---

#### public void mousePressed​(
MouseEvent
e)

Handles the mousePressed event by invoking the
mousePressed methods on listener-a and listener-b.

**Specified by:**
- mousePressed

in interface

MouseListener

**Parameters:**
- e

- the mouse event

---

#### public void mouseReleased​(
MouseEvent
e)

Handles the mouseReleased event by invoking the
mouseReleased methods on listener-a and listener-b.

**Specified by:**
- mouseReleased

in interface

MouseListener

**Parameters:**
- e

- the mouse event

---

#### public void mouseEntered​(
MouseEvent
e)

Handles the mouseEntered event by invoking the
mouseEntered methods on listener-a and listener-b.

**Specified by:**
- mouseEntered

in interface

MouseListener

**Parameters:**
- e

- the mouse event

---

#### public void mouseExited​(
MouseEvent
e)

Handles the mouseExited event by invoking the
mouseExited methods on listener-a and listener-b.

**Specified by:**
- mouseExited

in interface

MouseListener

**Parameters:**
- e

- the mouse event

---

#### public void mouseDragged​(
MouseEvent
e)

Handles the mouseDragged event by invoking the
mouseDragged methods on listener-a and listener-b.

**Specified by:**
- mouseDragged

in interface

MouseMotionListener

**Parameters:**
- e

- the mouse event

---

#### public void mouseMoved​(
MouseEvent
e)

Handles the mouseMoved event by invoking the
mouseMoved methods on listener-a and listener-b.

**Specified by:**
- mouseMoved

in interface

MouseMotionListener

**Parameters:**
- e

- the mouse event

---

#### public void windowOpened​(
WindowEvent
e)

Handles the windowOpened event by invoking the
windowOpened methods on listener-a and listener-b.

**Specified by:**
- windowOpened

in interface

WindowListener

**Parameters:**
- e

- the window event

---

#### public void windowClosing​(
WindowEvent
e)

Handles the windowClosing event by invoking the
windowClosing methods on listener-a and listener-b.

**Specified by:**
- windowClosing

in interface

WindowListener

**Parameters:**
- e

- the window event

---

#### public void windowClosed​(
WindowEvent
e)

Handles the windowClosed event by invoking the
windowClosed methods on listener-a and listener-b.

**Specified by:**
- windowClosed

in interface

WindowListener

**Parameters:**
- e

- the window event

---

#### public void windowIconified​(
WindowEvent
e)

Handles the windowIconified event by invoking the
windowIconified methods on listener-a and listener-b.

**Specified by:**
- windowIconified

in interface

WindowListener

**Parameters:**
- e

- the window event

**See Also:**
- Window.setIconImage(java.awt.Image)

---

#### public void windowDeiconified​(
WindowEvent
e)

Handles the windowDeiconified event by invoking the
windowDeiconified methods on listener-a and listener-b.

**Specified by:**
- windowDeiconified

in interface

WindowListener

**Parameters:**
- e

- the window event

---

#### public void windowActivated​(
WindowEvent
e)

Handles the windowActivated event by invoking the
windowActivated methods on listener-a and listener-b.

**Specified by:**
- windowActivated

in interface

WindowListener

**Parameters:**
- e

- the window event

---

#### public void windowDeactivated​(
WindowEvent
e)

Handles the windowDeactivated event by invoking the
windowDeactivated methods on listener-a and listener-b.

**Specified by:**
- windowDeactivated

in interface

WindowListener

**Parameters:**
- e

- the window event

---

#### public void windowStateChanged​(
WindowEvent
e)

Handles the windowStateChanged event by invoking the
windowStateChanged methods on listener-a and listener-b.

**Specified by:**
- windowStateChanged

in interface

WindowStateListener

**Parameters:**
- e

- the window event

**Since:**
- 1.4

---

#### public void windowGainedFocus​(
WindowEvent
e)

Handles the windowGainedFocus event by invoking the windowGainedFocus
methods on listener-a and listener-b.

**Specified by:**
- windowGainedFocus

in interface

WindowFocusListener

**Parameters:**
- e

- the window event

**Since:**
- 1.4

---

#### public void windowLostFocus​(
WindowEvent
e)

Handles the windowLostFocus event by invoking the windowLostFocus
methods on listener-a and listener-b.

**Specified by:**
- windowLostFocus

in interface

WindowFocusListener

**Parameters:**
- e

- the window event

**Since:**
- 1.4

---

#### public void actionPerformed​(
ActionEvent
e)

Handles the actionPerformed event by invoking the
actionPerformed methods on listener-a and listener-b.

**Specified by:**
- actionPerformed

in interface

ActionListener

**Parameters:**
- e

- the action event

---

#### public void itemStateChanged​(
ItemEvent
e)

Handles the itemStateChanged event by invoking the
itemStateChanged methods on listener-a and listener-b.

**Specified by:**
- itemStateChanged

in interface

ItemListener

**Parameters:**
- e

- the item event

---

#### public void adjustmentValueChanged​(
AdjustmentEvent
e)

Handles the adjustmentValueChanged event by invoking the
adjustmentValueChanged methods on listener-a and listener-b.

**Specified by:**
- adjustmentValueChanged

in interface

AdjustmentListener

**Parameters:**
- e

- the adjustment event

---

#### public void inputMethodTextChanged​(
InputMethodEvent
e)

Handles the inputMethodTextChanged event by invoking the
inputMethodTextChanged methods on listener-a and listener-b.

**Specified by:**
- inputMethodTextChanged

in interface

InputMethodListener

**Parameters:**
- e

- the item event

---

#### public void caretPositionChanged​(
InputMethodEvent
e)

Handles the caretPositionChanged event by invoking the
caretPositionChanged methods on listener-a and listener-b.

**Specified by:**
- caretPositionChanged

in interface

InputMethodListener

**Parameters:**
- e

- the item event

---

#### public void hierarchyChanged​(
HierarchyEvent
e)

Handles the hierarchyChanged event by invoking the
hierarchyChanged methods on listener-a and listener-b.

**Specified by:**
- hierarchyChanged

in interface

HierarchyListener

**Parameters:**
- e

- the item event

**See Also:**
- HierarchyEvent.getChangeFlags()

**Since:**
- 1.3

---

#### public void ancestorMoved​(
HierarchyEvent
e)

Handles the ancestorMoved event by invoking the
ancestorMoved methods on listener-a and listener-b.

**Specified by:**
- ancestorMoved

in interface

HierarchyBoundsListener

**Parameters:**
- e

- the item event

**Since:**
- 1.3

---

#### public void ancestorResized​(
HierarchyEvent
e)

Handles the ancestorResized event by invoking the
ancestorResized methods on listener-a and listener-b.

**Specified by:**
- ancestorResized

in interface

HierarchyBoundsListener

**Parameters:**
- e

- the item event

**Since:**
- 1.3

---

#### public void mouseWheelMoved​(
MouseWheelEvent
e)

Handles the mouseWheelMoved event by invoking the
mouseWheelMoved methods on listener-a and listener-b.

**Specified by:**
- mouseWheelMoved

in interface

MouseWheelListener

**Parameters:**
- e

- the mouse event

**See Also:**
- MouseWheelEvent

**Since:**
- 1.4

---

#### public static
ComponentListener
add​(
ComponentListener
a,

ComponentListener
b)

Adds component-listener-a with component-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- component-listener-a
- b

- component-listener-b

**Returns:**
- the resulting listener

---

#### public static
ContainerListener
add​(
ContainerListener
a,

ContainerListener
b)

Adds container-listener-a with container-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- container-listener-a
- b

- container-listener-b

**Returns:**
- the resulting listener

---

#### public static
FocusListener
add​(
FocusListener
a,

FocusListener
b)

Adds focus-listener-a with focus-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- focus-listener-a
- b

- focus-listener-b

**Returns:**
- the resulting listener

---

#### public static
KeyListener
add​(
KeyListener
a,

KeyListener
b)

Adds key-listener-a with key-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- key-listener-a
- b

- key-listener-b

**Returns:**
- the resulting listener

---

#### public static
MouseListener
add​(
MouseListener
a,

MouseListener
b)

Adds mouse-listener-a with mouse-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- mouse-listener-a
- b

- mouse-listener-b

**Returns:**
- the resulting listener

---

#### public static
MouseMotionListener
add​(
MouseMotionListener
a,

MouseMotionListener
b)

Adds mouse-motion-listener-a with mouse-motion-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- mouse-motion-listener-a
- b

- mouse-motion-listener-b

**Returns:**
- the resulting listener

---

#### public static
WindowListener
add​(
WindowListener
a,

WindowListener
b)

Adds window-listener-a with window-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- window-listener-a
- b

- window-listener-b

**Returns:**
- the resulting listener

---

#### public static
WindowStateListener
add​(
WindowStateListener
a,

WindowStateListener
b)

Adds window-state-listener-a with window-state-listener-b
and returns the resulting multicast listener.

**Parameters:**
- a

- window-state-listener-a
- b

- window-state-listener-b

**Returns:**
- the resulting listener

**Since:**
- 1.4

---

#### public static
WindowFocusListener
add​(
WindowFocusListener
a,

WindowFocusListener
b)

Adds window-focus-listener-a with window-focus-listener-b
and returns the resulting multicast listener.

**Parameters:**
- a

- window-focus-listener-a
- b

- window-focus-listener-b

**Returns:**
- the resulting listener

**Since:**
- 1.4

---

#### public static
ActionListener
add​(
ActionListener
a,

ActionListener
b)

Adds action-listener-a with action-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- action-listener-a
- b

- action-listener-b

**Returns:**
- the resulting listener

---

#### public static
ItemListener
add​(
ItemListener
a,

ItemListener
b)

Adds item-listener-a with item-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- item-listener-a
- b

- item-listener-b

**Returns:**
- the resulting listener

---

#### public static
AdjustmentListener
add​(
AdjustmentListener
a,

AdjustmentListener
b)

Adds adjustment-listener-a with adjustment-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- adjustment-listener-a
- b

- adjustment-listener-b

**Returns:**
- the resulting listener

---

#### public static
TextListener
add​(
TextListener
a,

TextListener
b)

Adds text-listener-a with text-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- text-listener-a
- b

- text-listener-b

**Returns:**
- the resulting listener

---

#### public static
InputMethodListener
add​(
InputMethodListener
a,

InputMethodListener
b)

Adds input-method-listener-a with input-method-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- input-method-listener-a
- b

- input-method-listener-b

**Returns:**
- the resulting listener

---

#### public static
HierarchyListener
add​(
HierarchyListener
a,

HierarchyListener
b)

Adds hierarchy-listener-a with hierarchy-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- hierarchy-listener-a
- b

- hierarchy-listener-b

**Returns:**
- the resulting listener

**Since:**
- 1.3

---

#### public static
HierarchyBoundsListener
add​(
HierarchyBoundsListener
a,

HierarchyBoundsListener
b)

Adds hierarchy-bounds-listener-a with hierarchy-bounds-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- hierarchy-bounds-listener-a
- b

- hierarchy-bounds-listener-b

**Returns:**
- the resulting listener

**Since:**
- 1.3

---

#### public static
MouseWheelListener
add​(
MouseWheelListener
a,

MouseWheelListener
b)

Adds mouse-wheel-listener-a with mouse-wheel-listener-b and
returns the resulting multicast listener.

**Parameters:**
- a

- mouse-wheel-listener-a
- b

- mouse-wheel-listener-b

**Returns:**
- the resulting listener

**Since:**
- 1.4

---

#### public static
ComponentListener
remove​(
ComponentListener
l,

ComponentListener
oldl)

Removes the old component-listener from component-listener-l and
returns the resulting multicast listener.

**Parameters:**
- l

- component-listener-l
- oldl

- the component-listener being removed

**Returns:**
- the resulting listener

---

#### public static
ContainerListener
remove​(
ContainerListener
l,

ContainerListener
oldl)

Removes the old container-listener from container-listener-l and
returns the resulting multicast listener.

**Parameters:**
- l

- container-listener-l
- oldl

- the container-listener being removed

**Returns:**
- the resulting listener

---

#### public static
FocusListener
remove​(
FocusListener
l,

FocusListener
oldl)

Removes the old focus-listener from focus-listener-l and
returns the resulting multicast listener.

**Parameters:**
- l

- focus-listener-l
- oldl

- the focus-listener being removed

**Returns:**
- the resulting listener

---

#### public static
KeyListener
remove​(
KeyListener
l,

KeyListener
oldl)

Removes the old key-listener from key-listener-l and
returns the resulting multicast listener.

**Parameters:**
- l

- key-listener-l
- oldl

- the key-listener being removed

**Returns:**
- the resulting listener

---

#### public static
MouseListener
remove​(
MouseListener
l,

MouseListener
oldl)

Removes the old mouse-listener from mouse-listener-l and
returns the resulting multicast listener.

**Parameters:**
- l

- mouse-listener-l
- oldl

- the mouse-listener being removed

**Returns:**
- the resulting listener

---

#### public static
MouseMotionListener
remove​(
MouseMotionListener
l,

MouseMotionListener
oldl)

Removes the old mouse-motion-listener from mouse-motion-listener-l
and returns the resulting multicast listener.

**Parameters:**
- l

- mouse-motion-listener-l
- oldl

- the mouse-motion-listener being removed

**Returns:**
- the resulting listener

---

#### public static
WindowListener
remove​(
WindowListener
l,

WindowListener
oldl)

Removes the old window-listener from window-listener-l and
returns the resulting multicast listener.

**Parameters:**
- l

- window-listener-l
- oldl

- the window-listener being removed

**Returns:**
- the resulting listener

---

#### public static
WindowStateListener
remove​(
WindowStateListener
l,

WindowStateListener
oldl)

Removes the old window-state-listener from window-state-listener-l
and returns the resulting multicast listener.

**Parameters:**
- l

- window-state-listener-l
- oldl

- the window-state-listener being removed

**Returns:**
- the resulting listener

**Since:**
- 1.4

---

#### public static
WindowFocusListener
remove​(
WindowFocusListener
l,

WindowFocusListener
oldl)

Removes the old window-focus-listener from window-focus-listener-l
and returns the resulting multicast listener.

**Parameters:**
- l

- window-focus-listener-l
- oldl

- the window-focus-listener being removed

**Returns:**
- the resulting listener

**Since:**
- 1.4

---

#### public static
ActionListener
remove​(
ActionListener
l,

ActionListener
oldl)

Removes the old action-listener from action-listener-l and
returns the resulting multicast listener.

**Parameters:**
- l

- action-listener-l
- oldl

- the action-listener being removed

**Returns:**
- the resulting listener

---

#### public static
ItemListener
remove​(
ItemListener
l,

ItemListener
oldl)

Removes the old item-listener from item-listener-l and
returns the resulting multicast listener.

**Parameters:**
- l

- item-listener-l
- oldl

- the item-listener being removed

**Returns:**
- the resulting listener

---

#### public static
AdjustmentListener
remove​(
AdjustmentListener
l,

AdjustmentListener
oldl)

Removes the old adjustment-listener from adjustment-listener-l and
returns the resulting multicast listener.

**Parameters:**
- l

- adjustment-listener-l
- oldl

- the adjustment-listener being removed

**Returns:**
- the resulting listener

---

#### public static
TextListener
remove​(
TextListener
l,

TextListener
oldl)

Removes the old text-listener from text-listener-l and
returns the resulting multicast listener.

**Parameters:**
- l

- text-listener-l
- oldl

- the text-listener being removed

**Returns:**
- the resulting listener

---

#### public static
InputMethodListener
remove​(
InputMethodListener
l,

InputMethodListener
oldl)

Removes the old input-method-listener from input-method-listener-l and
returns the resulting multicast listener.

**Parameters:**
- l

- input-method-listener-l
- oldl

- the input-method-listener being removed

**Returns:**
- the resulting listener

---

#### public static
HierarchyListener
remove​(
HierarchyListener
l,

HierarchyListener
oldl)

Removes the old hierarchy-listener from hierarchy-listener-l and
returns the resulting multicast listener.

**Parameters:**
- l

- hierarchy-listener-l
- oldl

- the hierarchy-listener being removed

**Returns:**
- the resulting listener

**Since:**
- 1.3

---

#### public static
HierarchyBoundsListener
remove​(
HierarchyBoundsListener
l,

HierarchyBoundsListener
oldl)

Removes the old hierarchy-bounds-listener from
hierarchy-bounds-listener-l and returns the resulting multicast
listener.

**Parameters:**
- l

- hierarchy-bounds-listener-l
- oldl

- the hierarchy-bounds-listener being removed

**Returns:**
- the resulting listener

**Since:**
- 1.3

---

#### public static
MouseWheelListener
remove​(
MouseWheelListener
l,

MouseWheelListener
oldl)

Removes the old mouse-wheel-listener from mouse-wheel-listener-l
and returns the resulting multicast listener.

**Parameters:**
- l

- mouse-wheel-listener-l
- oldl

- the mouse-wheel-listener being removed

**Returns:**
- the resulting listener

**Since:**
- 1.4

---

#### protected static
EventListener
addInternal​(
EventListener
a,

EventListener
b)

Returns the resulting multicast listener from adding listener-a
and listener-b together.
If listener-a is null, it returns listener-b;
If listener-b is null, it returns listener-a
If neither are null, then it creates and returns
a new AWTEventMulticaster instance which chains a with b.

**Parameters:**
- a

- event listener-a
- b

- event listener-b

**Returns:**
- the resulting listener

---

#### protected static
EventListener
removeInternal​(
EventListener
l,

EventListener
oldl)

Returns the resulting multicast listener after removing the
old listener from listener-l.
If listener-l equals the old listener OR listener-l is null,
returns null.
Else if listener-l is an instance of AWTEventMulticaster,
then it removes the old listener from it.
Else, returns listener l.

**Parameters:**
- l

- the listener being removed from
- oldl

- the listener being removed

**Returns:**
- the resulting listener

---

#### protected void saveInternal​(
ObjectOutputStream
s,

String
k)
throws
IOException

Serialization support. Saves all Serializable listeners
to a serialization stream.

**Parameters:**
- s

- the stream to save to
- k

- a prefix stream to put before each serializable listener

**Throws:**
- IOException

- if serialization fails

---

#### protected static void save​(
ObjectOutputStream
s,

String
k,

EventListener
l)
throws
IOException

Saves a Serializable listener chain to a serialization stream.

**Parameters:**
- s

- the stream to save to
- k

- a prefix stream to put before each serializable listener
- l

- the listener chain to save

**Throws:**
- IOException

- if serialization fails

---

#### public static <T extends
EventListener
> T[] getListeners​(
EventListener
l,

Class
<T> listenerType)

Returns an array of all the objects chained as

Foo

Listener

s by the specified

java.util.EventListener

.

Foo

Listener

s are chained by the

AWTEventMulticaster

using the

add

Foo

Listener

method.
If a

null

listener is specified, this method returns an
empty array. If the specified listener is not an instance of

AWTEventMulticaster

, this method returns an array which
contains only the specified listener. If no such listeners are chained,
this method returns an empty array.

**Parameters:**
- l

- the specified

java.util.EventListener
- listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener

**Returns:**
- an array of all objects chained as

Foo

Listener

s by the specified multicast
listener, or an empty array if no such listeners have been
chained by the specified multicast listener

**Throws:**
- NullPointerException

- if the specified

listenertype

parameter is

null
- ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener

**Since:**
- 1.4

**Type Parameters:**
- T

- the listener type

---

### Additional Sections

#### Class AWTEventMulticaster

java.lang.Object

- java.awt.AWTEventMulticaster

java.awt.AWTEventMulticaster

**All Implemented Interfaces:** ActionListener

,

AdjustmentListener

,

ComponentListener

,

ContainerListener

,

FocusListener

,

HierarchyBoundsListener

,

HierarchyListener

,

InputMethodListener

,

ItemListener

,

KeyListener

,

MouseListener

,

MouseMotionListener

,

MouseWheelListener

,

TextListener

,

WindowFocusListener

,

WindowListener

,

WindowStateListener

,

EventListener

```java
public class
AWTEventMulticaster

extends
Object

implements
ComponentListener
,
ContainerListener
,
FocusListener
,
KeyListener
,
MouseListener
,
MouseMotionListener
,
WindowListener
,
WindowFocusListener
,
WindowStateListener
,
ActionListener
,
ItemListener
,
AdjustmentListener
,
TextListener
,
InputMethodListener
,
HierarchyListener
,
HierarchyBoundsListener
,
MouseWheelListener
```

AWTEventMulticaster

implements efficient and thread-safe multi-cast
event dispatching for the AWT events defined in the

java.awt.event

package.

The following example illustrates how to use this class:

```java
public myComponent extends Component {
ActionListener actionListener = null;

public synchronized void addActionListener(ActionListener l) {
actionListener = AWTEventMulticaster.add(actionListener, l);
}
public synchronized void removeActionListener(ActionListener l) {
actionListener = AWTEventMulticaster.remove(actionListener, l);
}
public void processEvent(AWTEvent e) {
// when event occurs which causes "action" semantic
ActionListener listener = actionListener;
if (listener != null) {
listener.actionPerformed(new ActionEvent());
}
}
}
```

The important point to note is the first argument to the

add

and

remove

methods is the field maintaining the
listeners. In addition you must assign the result of the

add

and

remove

methods to the field maintaining the listeners.

AWTEventMulticaster

is implemented as a pair of

EventListeners

that are set at construction time.

AWTEventMulticaster

is immutable. The

add

and

remove

methods do not alter

AWTEventMulticaster

in
anyway. If necessary, a new

AWTEventMulticaster

is
created. In this way it is safe to add and remove listeners during
the process of an event dispatching. However, event listeners
added during the process of an event dispatch operation are not
notified of the event currently being dispatched.

All of the

add

methods allow

null

arguments. If the
first argument is

null

, the second argument is returned. If
the first argument is not

null

and the second argument is

null

, the first argument is returned. If both arguments are

non-null

, a new

AWTEventMulticaster

is created using
the two arguments and returned.

For the

remove

methods that take two arguments, the following is
returned:

- null

, if the first argument is

null

, or
the arguments are equal, by way of

==

.

the first argument, if the first argument is not an instance of

AWTEventMulticaster

.

result of invoking

remove(EventListener)

on the
first argument, supplying the second argument to the

remove(EventListener)

method.

Swing makes use of

EventListenerList

for
similar logic. Refer to it for details.

**Since:** 1.1
**See Also:** EventListenerList

public class

AWTEventMulticaster

extends

Object

implements

ComponentListener

,

ContainerListener

,

FocusListener

,

KeyListener

,

MouseListener

,

MouseMotionListener

,

WindowListener

,

WindowFocusListener

,

WindowStateListener

,

ActionListener

,

ItemListener

,

AdjustmentListener

,

TextListener

,

InputMethodListener

,

HierarchyListener

,

HierarchyBoundsListener

,

MouseWheelListener

AWTEventMulticaster

implements efficient and thread-safe multi-cast
event dispatching for the AWT events defined in the

java.awt.event

package.

The following example illustrates how to use this class:

```java
public myComponent extends Component {
ActionListener actionListener = null;

public synchronized void addActionListener(ActionListener l) {
actionListener = AWTEventMulticaster.add(actionListener, l);
}
public synchronized void removeActionListener(ActionListener l) {
actionListener = AWTEventMulticaster.remove(actionListener, l);
}
public void processEvent(AWTEvent e) {
// when event occurs which causes "action" semantic
ActionListener listener = actionListener;
if (listener != null) {
listener.actionPerformed(new ActionEvent());
}
}
}
```

The important point to note is the first argument to the

add

and

remove

methods is the field maintaining the
listeners. In addition you must assign the result of the

add

and

remove

methods to the field maintaining the listeners.

AWTEventMulticaster

is implemented as a pair of

EventListeners

that are set at construction time.

AWTEventMulticaster

is immutable. The

add

and

remove

methods do not alter

AWTEventMulticaster

in
anyway. If necessary, a new

AWTEventMulticaster

is
created. In this way it is safe to add and remove listeners during
the process of an event dispatching. However, event listeners
added during the process of an event dispatch operation are not
notified of the event currently being dispatched.

All of the

add

methods allow

null

arguments. If the
first argument is

null

, the second argument is returned. If
the first argument is not

null

and the second argument is

null

, the first argument is returned. If both arguments are

non-null

, a new

AWTEventMulticaster

is created using
the two arguments and returned.

For the

remove

methods that take two arguments, the following is
returned:

- null

, if the first argument is

null

, or
the arguments are equal, by way of

==

.

the first argument, if the first argument is not an instance of

AWTEventMulticaster

.

result of invoking

remove(EventListener)

on the
first argument, supplying the second argument to the

remove(EventListener)

method.

Swing makes use of

EventListenerList

for
similar logic. Refer to it for details.

The following example illustrates how to use this class:

```java
public myComponent extends Component {
ActionListener actionListener = null;

public synchronized void addActionListener(ActionListener l) {
actionListener = AWTEventMulticaster.add(actionListener, l);
}
public synchronized void removeActionListener(ActionListener l) {
actionListener = AWTEventMulticaster.remove(actionListener, l);
}
public void processEvent(AWTEvent e) {
// when event occurs which causes "action" semantic
ActionListener listener = actionListener;
if (listener != null) {
listener.actionPerformed(new ActionEvent());
}
}
}
```

The important point to note is the first argument to the

add

and

remove

methods is the field maintaining the
listeners. In addition you must assign the result of the

add

and

remove

methods to the field maintaining the listeners.

AWTEventMulticaster

is implemented as a pair of

EventListeners

that are set at construction time.

AWTEventMulticaster

is immutable. The

add

and

remove

methods do not alter

AWTEventMulticaster

in
anyway. If necessary, a new

AWTEventMulticaster

is
created. In this way it is safe to add and remove listeners during
the process of an event dispatching. However, event listeners
added during the process of an event dispatch operation are not
notified of the event currently being dispatched.

All of the

add

methods allow

null

arguments. If the
first argument is

null

, the second argument is returned. If
the first argument is not

null

and the second argument is

null

, the first argument is returned. If both arguments are

non-null

, a new

AWTEventMulticaster

is created using
the two arguments and returned.

For the

remove

methods that take two arguments, the following is
returned:

- null

, if the first argument is

null

, or
the arguments are equal, by way of

==

.

the first argument, if the first argument is not an instance of

AWTEventMulticaster

.

result of invoking

remove(EventListener)

on the
first argument, supplying the second argument to the

remove(EventListener)

method.

Swing makes use of

EventListenerList

for
similar logic. Refer to it for details.

public myComponent extends Component {
ActionListener actionListener = null;

public synchronized void addActionListener(ActionListener l) {
actionListener = AWTEventMulticaster.add(actionListener, l);
}
public synchronized void removeActionListener(ActionListener l) {
actionListener = AWTEventMulticaster.remove(actionListener, l);
}
public void processEvent(AWTEvent e) {
// when event occurs which causes "action" semantic
ActionListener listener = actionListener;
if (listener != null) {
listener.actionPerformed(new ActionEvent());
}
}
}

AWTEventMulticaster

is implemented as a pair of

EventListeners

that are set at construction time.

AWTEventMulticaster

is immutable. The

add

and

remove

methods do not alter

AWTEventMulticaster

in
anyway. If necessary, a new

AWTEventMulticaster

is
created. In this way it is safe to add and remove listeners during
the process of an event dispatching. However, event listeners
added during the process of an event dispatch operation are not
notified of the event currently being dispatched.

All of the

add

methods allow

null

arguments. If the
first argument is

null

, the second argument is returned. If
the first argument is not

null

and the second argument is

null

, the first argument is returned. If both arguments are

non-null

, a new

AWTEventMulticaster

is created using
the two arguments and returned.

For the

remove

methods that take two arguments, the following is
returned:

- null

, if the first argument is

null

, or
the arguments are equal, by way of

==

.

the first argument, if the first argument is not an instance of

AWTEventMulticaster

.

result of invoking

remove(EventListener)

on the
first argument, supplying the second argument to the

remove(EventListener)

method.

Swing makes use of

EventListenerList

for
similar logic. Refer to it for details.

All of the

add

methods allow

null

arguments. If the
first argument is

null

, the second argument is returned. If
the first argument is not

null

and the second argument is

null

, the first argument is returned. If both arguments are

non-null

, a new

AWTEventMulticaster

is created using
the two arguments and returned.

For the

remove

methods that take two arguments, the following is
returned:

- null

, if the first argument is

null

, or
the arguments are equal, by way of

==

.

the first argument, if the first argument is not an instance of

AWTEventMulticaster

.

result of invoking

remove(EventListener)

on the
first argument, supplying the second argument to the

remove(EventListener)

method.

Swing makes use of

EventListenerList

for
similar logic. Refer to it for details.

For the

remove

methods that take two arguments, the following is
returned:

- null

, if the first argument is

null

, or
the arguments are equal, by way of

==

.

the first argument, if the first argument is not an instance of

AWTEventMulticaster

.

result of invoking

remove(EventListener)

on the
first argument, supplying the second argument to the

remove(EventListener)

method.

Swing makes use of

EventListenerList

for
similar logic. Refer to it for details.

null

, if the first argument is

null

, or
the arguments are equal, by way of

==

.

the first argument, if the first argument is not an instance of

AWTEventMulticaster

.

result of invoking

remove(EventListener)

on the
first argument, supplying the second argument to the

remove(EventListener)

method.

Swing makes use of

EventListenerList

for
similar logic. Refer to it for details.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

EventListener

a

A variable in the event chain (listener-a)

protected

EventListener

b

A variable in the event chain (listener-b)

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AWTEventMulticaster

​(

EventListener

a,

EventListener

b)

Creates an event multicaster instance which chains listener-a
with listener-b.

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

actionPerformed

​(

ActionEvent

e)

Handles the actionPerformed event by invoking the
actionPerformed methods on listener-a and listener-b.

static

ActionListener

add

​(

ActionListener

a,

ActionListener

b)

Adds action-listener-a with action-listener-b and
returns the resulting multicast listener.

static

AdjustmentListener

add

​(

AdjustmentListener

a,

AdjustmentListener

b)

Adds adjustment-listener-a with adjustment-listener-b and
returns the resulting multicast listener.

static

ComponentListener

add

​(

ComponentListener

a,

ComponentListener

b)

Adds component-listener-a with component-listener-b and
returns the resulting multicast listener.

static

ContainerListener

add

​(

ContainerListener

a,

ContainerListener

b)

Adds container-listener-a with container-listener-b and
returns the resulting multicast listener.

static

FocusListener

add

​(

FocusListener

a,

FocusListener

b)

Adds focus-listener-a with focus-listener-b and
returns the resulting multicast listener.

static

HierarchyBoundsListener

add

​(

HierarchyBoundsListener

a,

HierarchyBoundsListener

b)

Adds hierarchy-bounds-listener-a with hierarchy-bounds-listener-b and
returns the resulting multicast listener.

static

HierarchyListener

add

​(

HierarchyListener

a,

HierarchyListener

b)

Adds hierarchy-listener-a with hierarchy-listener-b and
returns the resulting multicast listener.

static

InputMethodListener

add

​(

InputMethodListener

a,

InputMethodListener

b)

Adds input-method-listener-a with input-method-listener-b and
returns the resulting multicast listener.

static

ItemListener

add

​(

ItemListener

a,

ItemListener

b)

Adds item-listener-a with item-listener-b and
returns the resulting multicast listener.

static

KeyListener

add

​(

KeyListener

a,

KeyListener

b)

Adds key-listener-a with key-listener-b and
returns the resulting multicast listener.

static

MouseListener

add

​(

MouseListener

a,

MouseListener

b)

Adds mouse-listener-a with mouse-listener-b and
returns the resulting multicast listener.

static

MouseMotionListener

add

​(

MouseMotionListener

a,

MouseMotionListener

b)

Adds mouse-motion-listener-a with mouse-motion-listener-b and
returns the resulting multicast listener.

static

MouseWheelListener

add

​(

MouseWheelListener

a,

MouseWheelListener

b)

Adds mouse-wheel-listener-a with mouse-wheel-listener-b and
returns the resulting multicast listener.

static

TextListener

add

​(

TextListener

a,

TextListener

b)

Adds text-listener-a with text-listener-b and
returns the resulting multicast listener.

static

WindowFocusListener

add

​(

WindowFocusListener

a,

WindowFocusListener

b)

Adds window-focus-listener-a with window-focus-listener-b
and returns the resulting multicast listener.

static

WindowListener

add

​(

WindowListener

a,

WindowListener

b)

Adds window-listener-a with window-listener-b and
returns the resulting multicast listener.

static

WindowStateListener

add

​(

WindowStateListener

a,

WindowStateListener

b)

Adds window-state-listener-a with window-state-listener-b
and returns the resulting multicast listener.

protected static

EventListener

addInternal

​(

EventListener

a,

EventListener

b)

Returns the resulting multicast listener from adding listener-a
and listener-b together.

void

adjustmentValueChanged

​(

AdjustmentEvent

e)

Handles the adjustmentValueChanged event by invoking the
adjustmentValueChanged methods on listener-a and listener-b.

void

ancestorMoved

​(

HierarchyEvent

e)

Handles the ancestorMoved event by invoking the
ancestorMoved methods on listener-a and listener-b.

void

ancestorResized

​(

HierarchyEvent

e)

Handles the ancestorResized event by invoking the
ancestorResized methods on listener-a and listener-b.

void

caretPositionChanged

​(

InputMethodEvent

e)

Handles the caretPositionChanged event by invoking the
caretPositionChanged methods on listener-a and listener-b.

void

componentAdded

​(

ContainerEvent

e)

Handles the componentAdded container event by invoking the
componentAdded methods on listener-a and listener-b.

void

componentHidden

​(

ComponentEvent

e)

Handles the componentHidden event by invoking the
componentHidden methods on listener-a and listener-b.

void

componentMoved

​(

ComponentEvent

e)

Handles the componentMoved event by invoking the
componentMoved methods on listener-a and listener-b.

void

componentRemoved

​(

ContainerEvent

e)

Handles the componentRemoved container event by invoking the
componentRemoved methods on listener-a and listener-b.

void

componentResized

​(

ComponentEvent

e)

Handles the componentResized event by invoking the
componentResized methods on listener-a and listener-b.

void

componentShown

​(

ComponentEvent

e)

Handles the componentShown event by invoking the
componentShown methods on listener-a and listener-b.

void

focusGained

​(

FocusEvent

e)

Handles the focusGained event by invoking the
focusGained methods on listener-a and listener-b.

void

focusLost

​(

FocusEvent

e)

Handles the focusLost event by invoking the
focusLost methods on listener-a and listener-b.

static <T extends

EventListener

>

T[]

getListeners

​(

EventListener

l,

Class

<T> listenerType)

Returns an array of all the objects chained as

Foo

Listener

s by the specified

java.util.EventListener

.

void

hierarchyChanged

​(

HierarchyEvent

e)

Handles the hierarchyChanged event by invoking the
hierarchyChanged methods on listener-a and listener-b.

void

inputMethodTextChanged

​(

InputMethodEvent

e)

Handles the inputMethodTextChanged event by invoking the
inputMethodTextChanged methods on listener-a and listener-b.

void

itemStateChanged

​(

ItemEvent

e)

Handles the itemStateChanged event by invoking the
itemStateChanged methods on listener-a and listener-b.

void

keyPressed

​(

KeyEvent

e)

Handles the keyPressed event by invoking the
keyPressed methods on listener-a and listener-b.

void

keyReleased

​(

KeyEvent

e)

Handles the keyReleased event by invoking the
keyReleased methods on listener-a and listener-b.

void

keyTyped

​(

KeyEvent

e)

Handles the keyTyped event by invoking the
keyTyped methods on listener-a and listener-b.

void

mouseClicked

​(

MouseEvent

e)

Handles the mouseClicked event by invoking the
mouseClicked methods on listener-a and listener-b.

void

mouseDragged

​(

MouseEvent

e)

Handles the mouseDragged event by invoking the
mouseDragged methods on listener-a and listener-b.

void

mouseEntered

​(

MouseEvent

e)

Handles the mouseEntered event by invoking the
mouseEntered methods on listener-a and listener-b.

void

mouseExited

​(

MouseEvent

e)

Handles the mouseExited event by invoking the
mouseExited methods on listener-a and listener-b.

void

mouseMoved

​(

MouseEvent

e)

Handles the mouseMoved event by invoking the
mouseMoved methods on listener-a and listener-b.

void

mousePressed

​(

MouseEvent

e)

Handles the mousePressed event by invoking the
mousePressed methods on listener-a and listener-b.

void

mouseReleased

​(

MouseEvent

e)

Handles the mouseReleased event by invoking the
mouseReleased methods on listener-a and listener-b.

void

mouseWheelMoved

​(

MouseWheelEvent

e)

Handles the mouseWheelMoved event by invoking the
mouseWheelMoved methods on listener-a and listener-b.

static

ActionListener

remove

​(

ActionListener

l,

ActionListener

oldl)

Removes the old action-listener from action-listener-l and
returns the resulting multicast listener.

static

AdjustmentListener

remove

​(

AdjustmentListener

l,

AdjustmentListener

oldl)

Removes the old adjustment-listener from adjustment-listener-l and
returns the resulting multicast listener.

static

ComponentListener

remove

​(

ComponentListener

l,

ComponentListener

oldl)

Removes the old component-listener from component-listener-l and
returns the resulting multicast listener.

static

ContainerListener

remove

​(

ContainerListener

l,

ContainerListener

oldl)

Removes the old container-listener from container-listener-l and
returns the resulting multicast listener.

static

FocusListener

remove

​(

FocusListener

l,

FocusListener

oldl)

Removes the old focus-listener from focus-listener-l and
returns the resulting multicast listener.

static

HierarchyBoundsListener

remove

​(

HierarchyBoundsListener

l,

HierarchyBoundsListener

oldl)

Removes the old hierarchy-bounds-listener from
hierarchy-bounds-listener-l and returns the resulting multicast
listener.

static

HierarchyListener

remove

​(

HierarchyListener

l,

HierarchyListener

oldl)

Removes the old hierarchy-listener from hierarchy-listener-l and
returns the resulting multicast listener.

static

InputMethodListener

remove

​(

InputMethodListener

l,

InputMethodListener

oldl)

Removes the old input-method-listener from input-method-listener-l and
returns the resulting multicast listener.

static

ItemListener

remove

​(

ItemListener

l,

ItemListener

oldl)

Removes the old item-listener from item-listener-l and
returns the resulting multicast listener.

static

KeyListener

remove

​(

KeyListener

l,

KeyListener

oldl)

Removes the old key-listener from key-listener-l and
returns the resulting multicast listener.

static

MouseListener

remove

​(

MouseListener

l,

MouseListener

oldl)

Removes the old mouse-listener from mouse-listener-l and
returns the resulting multicast listener.

static

MouseMotionListener

remove

​(

MouseMotionListener

l,

MouseMotionListener

oldl)

Removes the old mouse-motion-listener from mouse-motion-listener-l
and returns the resulting multicast listener.

static

MouseWheelListener

remove

​(

MouseWheelListener

l,

MouseWheelListener

oldl)

Removes the old mouse-wheel-listener from mouse-wheel-listener-l
and returns the resulting multicast listener.

static

TextListener

remove

​(

TextListener

l,

TextListener

oldl)

Removes the old text-listener from text-listener-l and
returns the resulting multicast listener.

static

WindowFocusListener

remove

​(

WindowFocusListener

l,

WindowFocusListener

oldl)

Removes the old window-focus-listener from window-focus-listener-l
and returns the resulting multicast listener.

static

WindowListener

remove

​(

WindowListener

l,

WindowListener

oldl)

Removes the old window-listener from window-listener-l and
returns the resulting multicast listener.

static

WindowStateListener

remove

​(

WindowStateListener

l,

WindowStateListener

oldl)

Removes the old window-state-listener from window-state-listener-l
and returns the resulting multicast listener.

protected

EventListener

remove

​(

EventListener

oldl)

Removes a listener from this multicaster.

protected static

EventListener

removeInternal

​(

EventListener

l,

EventListener

oldl)

Returns the resulting multicast listener after removing the
old listener from listener-l.

protected static void

save

​(

ObjectOutputStream

s,

String

k,

EventListener

l)

Saves a Serializable listener chain to a serialization stream.

protected void

saveInternal

​(

ObjectOutputStream

s,

String

k)

Serialization support.

void

windowActivated

​(

WindowEvent

e)

Handles the windowActivated event by invoking the
windowActivated methods on listener-a and listener-b.

void

windowClosed

​(

WindowEvent

e)

Handles the windowClosed event by invoking the
windowClosed methods on listener-a and listener-b.

void

windowClosing

​(

WindowEvent

e)

Handles the windowClosing event by invoking the
windowClosing methods on listener-a and listener-b.

void

windowDeactivated

​(

WindowEvent

e)

Handles the windowDeactivated event by invoking the
windowDeactivated methods on listener-a and listener-b.

void

windowDeiconified

​(

WindowEvent

e)

Handles the windowDeiconified event by invoking the
windowDeiconified methods on listener-a and listener-b.

void

windowGainedFocus

​(

WindowEvent

e)

Handles the windowGainedFocus event by invoking the windowGainedFocus
methods on listener-a and listener-b.

void

windowIconified

​(

WindowEvent

e)

Handles the windowIconified event by invoking the
windowIconified methods on listener-a and listener-b.

void

windowLostFocus

​(

WindowEvent

e)

Handles the windowLostFocus event by invoking the windowLostFocus
methods on listener-a and listener-b.

void

windowOpened

​(

WindowEvent

e)

Handles the windowOpened event by invoking the
windowOpened methods on listener-a and listener-b.

void

windowStateChanged

​(

WindowEvent

e)

Handles the windowStateChanged event by invoking the
windowStateChanged methods on listener-a and listener-b.

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

- Methods declared in interface java.awt.event.

TextListener

textValueChanged

Field Summary

Fields

Modifier and Type

Field

Description

protected

EventListener

a

A variable in the event chain (listener-a)

protected

EventListener

b

A variable in the event chain (listener-b)

---

#### Field Summary

A variable in the event chain (listener-a)

A variable in the event chain (listener-b)

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AWTEventMulticaster

​(

EventListener

a,

EventListener

b)

Creates an event multicaster instance which chains listener-a
with listener-b.

---

#### Constructor Summary

Creates an event multicaster instance which chains listener-a
with listener-b.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

e)

Handles the actionPerformed event by invoking the
actionPerformed methods on listener-a and listener-b.

static

ActionListener

add

​(

ActionListener

a,

ActionListener

b)

Adds action-listener-a with action-listener-b and
returns the resulting multicast listener.

static

AdjustmentListener

add

​(

AdjustmentListener

a,

AdjustmentListener

b)

Adds adjustment-listener-a with adjustment-listener-b and
returns the resulting multicast listener.

static

ComponentListener

add

​(

ComponentListener

a,

ComponentListener

b)

Adds component-listener-a with component-listener-b and
returns the resulting multicast listener.

static

ContainerListener

add

​(

ContainerListener

a,

ContainerListener

b)

Adds container-listener-a with container-listener-b and
returns the resulting multicast listener.

static

FocusListener

add

​(

FocusListener

a,

FocusListener

b)

Adds focus-listener-a with focus-listener-b and
returns the resulting multicast listener.

static

HierarchyBoundsListener

add

​(

HierarchyBoundsListener

a,

HierarchyBoundsListener

b)

Adds hierarchy-bounds-listener-a with hierarchy-bounds-listener-b and
returns the resulting multicast listener.

static

HierarchyListener

add

​(

HierarchyListener

a,

HierarchyListener

b)

Adds hierarchy-listener-a with hierarchy-listener-b and
returns the resulting multicast listener.

static

InputMethodListener

add

​(

InputMethodListener

a,

InputMethodListener

b)

Adds input-method-listener-a with input-method-listener-b and
returns the resulting multicast listener.

static

ItemListener

add

​(

ItemListener

a,

ItemListener

b)

Adds item-listener-a with item-listener-b and
returns the resulting multicast listener.

static

KeyListener

add

​(

KeyListener

a,

KeyListener

b)

Adds key-listener-a with key-listener-b and
returns the resulting multicast listener.

static

MouseListener

add

​(

MouseListener

a,

MouseListener

b)

Adds mouse-listener-a with mouse-listener-b and
returns the resulting multicast listener.

static

MouseMotionListener

add

​(

MouseMotionListener

a,

MouseMotionListener

b)

Adds mouse-motion-listener-a with mouse-motion-listener-b and
returns the resulting multicast listener.

static

MouseWheelListener

add

​(

MouseWheelListener

a,

MouseWheelListener

b)

Adds mouse-wheel-listener-a with mouse-wheel-listener-b and
returns the resulting multicast listener.

static

TextListener

add

​(

TextListener

a,

TextListener

b)

Adds text-listener-a with text-listener-b and
returns the resulting multicast listener.

static

WindowFocusListener

add

​(

WindowFocusListener

a,

WindowFocusListener

b)

Adds window-focus-listener-a with window-focus-listener-b
and returns the resulting multicast listener.

static

WindowListener

add

​(

WindowListener

a,

WindowListener

b)

Adds window-listener-a with window-listener-b and
returns the resulting multicast listener.

static

WindowStateListener

add

​(

WindowStateListener

a,

WindowStateListener

b)

Adds window-state-listener-a with window-state-listener-b
and returns the resulting multicast listener.

protected static

EventListener

addInternal

​(

EventListener

a,

EventListener

b)

Returns the resulting multicast listener from adding listener-a
and listener-b together.

void

adjustmentValueChanged

​(

AdjustmentEvent

e)

Handles the adjustmentValueChanged event by invoking the
adjustmentValueChanged methods on listener-a and listener-b.

void

ancestorMoved

​(

HierarchyEvent

e)

Handles the ancestorMoved event by invoking the
ancestorMoved methods on listener-a and listener-b.

void

ancestorResized

​(

HierarchyEvent

e)

Handles the ancestorResized event by invoking the
ancestorResized methods on listener-a and listener-b.

void

caretPositionChanged

​(

InputMethodEvent

e)

Handles the caretPositionChanged event by invoking the
caretPositionChanged methods on listener-a and listener-b.

void

componentAdded

​(

ContainerEvent

e)

Handles the componentAdded container event by invoking the
componentAdded methods on listener-a and listener-b.

void

componentHidden

​(

ComponentEvent

e)

Handles the componentHidden event by invoking the
componentHidden methods on listener-a and listener-b.

void

componentMoved

​(

ComponentEvent

e)

Handles the componentMoved event by invoking the
componentMoved methods on listener-a and listener-b.

void

componentRemoved

​(

ContainerEvent

e)

Handles the componentRemoved container event by invoking the
componentRemoved methods on listener-a and listener-b.

void

componentResized

​(

ComponentEvent

e)

Handles the componentResized event by invoking the
componentResized methods on listener-a and listener-b.

void

componentShown

​(

ComponentEvent

e)

Handles the componentShown event by invoking the
componentShown methods on listener-a and listener-b.

void

focusGained

​(

FocusEvent

e)

Handles the focusGained event by invoking the
focusGained methods on listener-a and listener-b.

void

focusLost

​(

FocusEvent

e)

Handles the focusLost event by invoking the
focusLost methods on listener-a and listener-b.

static <T extends

EventListener

>

T[]

getListeners

​(

EventListener

l,

Class

<T> listenerType)

Returns an array of all the objects chained as

Foo

Listener

s by the specified

java.util.EventListener

.

void

hierarchyChanged

​(

HierarchyEvent

e)

Handles the hierarchyChanged event by invoking the
hierarchyChanged methods on listener-a and listener-b.

void

inputMethodTextChanged

​(

InputMethodEvent

e)

Handles the inputMethodTextChanged event by invoking the
inputMethodTextChanged methods on listener-a and listener-b.

void

itemStateChanged

​(

ItemEvent

e)

Handles the itemStateChanged event by invoking the
itemStateChanged methods on listener-a and listener-b.

void

keyPressed

​(

KeyEvent

e)

Handles the keyPressed event by invoking the
keyPressed methods on listener-a and listener-b.

void

keyReleased

​(

KeyEvent

e)

Handles the keyReleased event by invoking the
keyReleased methods on listener-a and listener-b.

void

keyTyped

​(

KeyEvent

e)

Handles the keyTyped event by invoking the
keyTyped methods on listener-a and listener-b.

void

mouseClicked

​(

MouseEvent

e)

Handles the mouseClicked event by invoking the
mouseClicked methods on listener-a and listener-b.

void

mouseDragged

​(

MouseEvent

e)

Handles the mouseDragged event by invoking the
mouseDragged methods on listener-a and listener-b.

void

mouseEntered

​(

MouseEvent

e)

Handles the mouseEntered event by invoking the
mouseEntered methods on listener-a and listener-b.

void

mouseExited

​(

MouseEvent

e)

Handles the mouseExited event by invoking the
mouseExited methods on listener-a and listener-b.

void

mouseMoved

​(

MouseEvent

e)

Handles the mouseMoved event by invoking the
mouseMoved methods on listener-a and listener-b.

void

mousePressed

​(

MouseEvent

e)

Handles the mousePressed event by invoking the
mousePressed methods on listener-a and listener-b.

void

mouseReleased

​(

MouseEvent

e)

Handles the mouseReleased event by invoking the
mouseReleased methods on listener-a and listener-b.

void

mouseWheelMoved

​(

MouseWheelEvent

e)

Handles the mouseWheelMoved event by invoking the
mouseWheelMoved methods on listener-a and listener-b.

static

ActionListener

remove

​(

ActionListener

l,

ActionListener

oldl)

Removes the old action-listener from action-listener-l and
returns the resulting multicast listener.

static

AdjustmentListener

remove

​(

AdjustmentListener

l,

AdjustmentListener

oldl)

Removes the old adjustment-listener from adjustment-listener-l and
returns the resulting multicast listener.

static

ComponentListener

remove

​(

ComponentListener

l,

ComponentListener

oldl)

Removes the old component-listener from component-listener-l and
returns the resulting multicast listener.

static

ContainerListener

remove

​(

ContainerListener

l,

ContainerListener

oldl)

Removes the old container-listener from container-listener-l and
returns the resulting multicast listener.

static

FocusListener

remove

​(

FocusListener

l,

FocusListener

oldl)

Removes the old focus-listener from focus-listener-l and
returns the resulting multicast listener.

static

HierarchyBoundsListener

remove

​(

HierarchyBoundsListener

l,

HierarchyBoundsListener

oldl)

Removes the old hierarchy-bounds-listener from
hierarchy-bounds-listener-l and returns the resulting multicast
listener.

static

HierarchyListener

remove

​(

HierarchyListener

l,

HierarchyListener

oldl)

Removes the old hierarchy-listener from hierarchy-listener-l and
returns the resulting multicast listener.

static

InputMethodListener

remove

​(

InputMethodListener

l,

InputMethodListener

oldl)

Removes the old input-method-listener from input-method-listener-l and
returns the resulting multicast listener.

static

ItemListener

remove

​(

ItemListener

l,

ItemListener

oldl)

Removes the old item-listener from item-listener-l and
returns the resulting multicast listener.

static

KeyListener

remove

​(

KeyListener

l,

KeyListener

oldl)

Removes the old key-listener from key-listener-l and
returns the resulting multicast listener.

static

MouseListener

remove

​(

MouseListener

l,

MouseListener

oldl)

Removes the old mouse-listener from mouse-listener-l and
returns the resulting multicast listener.

static

MouseMotionListener

remove

​(

MouseMotionListener

l,

MouseMotionListener

oldl)

Removes the old mouse-motion-listener from mouse-motion-listener-l
and returns the resulting multicast listener.

static

MouseWheelListener

remove

​(

MouseWheelListener

l,

MouseWheelListener

oldl)

Removes the old mouse-wheel-listener from mouse-wheel-listener-l
and returns the resulting multicast listener.

static

TextListener

remove

​(

TextListener

l,

TextListener

oldl)

Removes the old text-listener from text-listener-l and
returns the resulting multicast listener.

static

WindowFocusListener

remove

​(

WindowFocusListener

l,

WindowFocusListener

oldl)

Removes the old window-focus-listener from window-focus-listener-l
and returns the resulting multicast listener.

static

WindowListener

remove

​(

WindowListener

l,

WindowListener

oldl)

Removes the old window-listener from window-listener-l and
returns the resulting multicast listener.

static

WindowStateListener

remove

​(

WindowStateListener

l,

WindowStateListener

oldl)

Removes the old window-state-listener from window-state-listener-l
and returns the resulting multicast listener.

protected

EventListener

remove

​(

EventListener

oldl)

Removes a listener from this multicaster.

protected static

EventListener

removeInternal

​(

EventListener

l,

EventListener

oldl)

Returns the resulting multicast listener after removing the
old listener from listener-l.

protected static void

save

​(

ObjectOutputStream

s,

String

k,

EventListener

l)

Saves a Serializable listener chain to a serialization stream.

protected void

saveInternal

​(

ObjectOutputStream

s,

String

k)

Serialization support.

void

windowActivated

​(

WindowEvent

e)

Handles the windowActivated event by invoking the
windowActivated methods on listener-a and listener-b.

void

windowClosed

​(

WindowEvent

e)

Handles the windowClosed event by invoking the
windowClosed methods on listener-a and listener-b.

void

windowClosing

​(

WindowEvent

e)

Handles the windowClosing event by invoking the
windowClosing methods on listener-a and listener-b.

void

windowDeactivated

​(

WindowEvent

e)

Handles the windowDeactivated event by invoking the
windowDeactivated methods on listener-a and listener-b.

void

windowDeiconified

​(

WindowEvent

e)

Handles the windowDeiconified event by invoking the
windowDeiconified methods on listener-a and listener-b.

void

windowGainedFocus

​(

WindowEvent

e)

Handles the windowGainedFocus event by invoking the windowGainedFocus
methods on listener-a and listener-b.

void

windowIconified

​(

WindowEvent

e)

Handles the windowIconified event by invoking the
windowIconified methods on listener-a and listener-b.

void

windowLostFocus

​(

WindowEvent

e)

Handles the windowLostFocus event by invoking the windowLostFocus
methods on listener-a and listener-b.

void

windowOpened

​(

WindowEvent

e)

Handles the windowOpened event by invoking the
windowOpened methods on listener-a and listener-b.

void

windowStateChanged

​(

WindowEvent

e)

Handles the windowStateChanged event by invoking the
windowStateChanged methods on listener-a and listener-b.

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

- Methods declared in interface java.awt.event.

TextListener

textValueChanged

---

#### Method Summary

Handles the actionPerformed event by invoking the
actionPerformed methods on listener-a and listener-b.

Adds action-listener-a with action-listener-b and
returns the resulting multicast listener.

Adds adjustment-listener-a with adjustment-listener-b and
returns the resulting multicast listener.

Adds component-listener-a with component-listener-b and
returns the resulting multicast listener.

Adds container-listener-a with container-listener-b and
returns the resulting multicast listener.

Adds focus-listener-a with focus-listener-b and
returns the resulting multicast listener.

Adds hierarchy-bounds-listener-a with hierarchy-bounds-listener-b and
returns the resulting multicast listener.

Adds hierarchy-listener-a with hierarchy-listener-b and
returns the resulting multicast listener.

Adds input-method-listener-a with input-method-listener-b and
returns the resulting multicast listener.

Adds item-listener-a with item-listener-b and
returns the resulting multicast listener.

Adds key-listener-a with key-listener-b and
returns the resulting multicast listener.

Adds mouse-listener-a with mouse-listener-b and
returns the resulting multicast listener.

Adds mouse-motion-listener-a with mouse-motion-listener-b and
returns the resulting multicast listener.

Adds mouse-wheel-listener-a with mouse-wheel-listener-b and
returns the resulting multicast listener.

Adds text-listener-a with text-listener-b and
returns the resulting multicast listener.

Adds window-focus-listener-a with window-focus-listener-b
and returns the resulting multicast listener.

Adds window-listener-a with window-listener-b and
returns the resulting multicast listener.

Adds window-state-listener-a with window-state-listener-b
and returns the resulting multicast listener.

Returns the resulting multicast listener from adding listener-a
and listener-b together.

Handles the adjustmentValueChanged event by invoking the
adjustmentValueChanged methods on listener-a and listener-b.

Handles the ancestorMoved event by invoking the
ancestorMoved methods on listener-a and listener-b.

Handles the ancestorResized event by invoking the
ancestorResized methods on listener-a and listener-b.

Handles the caretPositionChanged event by invoking the
caretPositionChanged methods on listener-a and listener-b.

Handles the componentAdded container event by invoking the
componentAdded methods on listener-a and listener-b.

Handles the componentHidden event by invoking the
componentHidden methods on listener-a and listener-b.

Handles the componentMoved event by invoking the
componentMoved methods on listener-a and listener-b.

Handles the componentRemoved container event by invoking the
componentRemoved methods on listener-a and listener-b.

Handles the componentResized event by invoking the
componentResized methods on listener-a and listener-b.

Handles the componentShown event by invoking the
componentShown methods on listener-a and listener-b.

Handles the focusGained event by invoking the
focusGained methods on listener-a and listener-b.

Handles the focusLost event by invoking the
focusLost methods on listener-a and listener-b.

Returns an array of all the objects chained as

Foo

Listener

s by the specified

java.util.EventListener

.

Handles the hierarchyChanged event by invoking the
hierarchyChanged methods on listener-a and listener-b.

Handles the inputMethodTextChanged event by invoking the
inputMethodTextChanged methods on listener-a and listener-b.

Handles the itemStateChanged event by invoking the
itemStateChanged methods on listener-a and listener-b.

Handles the keyPressed event by invoking the
keyPressed methods on listener-a and listener-b.

Handles the keyReleased event by invoking the
keyReleased methods on listener-a and listener-b.

Handles the keyTyped event by invoking the
keyTyped methods on listener-a and listener-b.

Handles the mouseClicked event by invoking the
mouseClicked methods on listener-a and listener-b.

Handles the mouseDragged event by invoking the
mouseDragged methods on listener-a and listener-b.

Handles the mouseEntered event by invoking the
mouseEntered methods on listener-a and listener-b.

Handles the mouseExited event by invoking the
mouseExited methods on listener-a and listener-b.

Handles the mouseMoved event by invoking the
mouseMoved methods on listener-a and listener-b.

Handles the mousePressed event by invoking the
mousePressed methods on listener-a and listener-b.

Handles the mouseReleased event by invoking the
mouseReleased methods on listener-a and listener-b.

Handles the mouseWheelMoved event by invoking the
mouseWheelMoved methods on listener-a and listener-b.

Removes the old action-listener from action-listener-l and
returns the resulting multicast listener.

Removes the old adjustment-listener from adjustment-listener-l and
returns the resulting multicast listener.

Removes the old component-listener from component-listener-l and
returns the resulting multicast listener.

Removes the old container-listener from container-listener-l and
returns the resulting multicast listener.

Removes the old focus-listener from focus-listener-l and
returns the resulting multicast listener.

Removes the old hierarchy-bounds-listener from
hierarchy-bounds-listener-l and returns the resulting multicast
listener.

Removes the old hierarchy-listener from hierarchy-listener-l and
returns the resulting multicast listener.

Removes the old input-method-listener from input-method-listener-l and
returns the resulting multicast listener.

Removes the old item-listener from item-listener-l and
returns the resulting multicast listener.

Removes the old key-listener from key-listener-l and
returns the resulting multicast listener.

Removes the old mouse-listener from mouse-listener-l and
returns the resulting multicast listener.

Removes the old mouse-motion-listener from mouse-motion-listener-l
and returns the resulting multicast listener.

Removes the old mouse-wheel-listener from mouse-wheel-listener-l
and returns the resulting multicast listener.

Removes the old text-listener from text-listener-l and
returns the resulting multicast listener.

Removes the old window-focus-listener from window-focus-listener-l
and returns the resulting multicast listener.

Removes the old window-listener from window-listener-l and
returns the resulting multicast listener.

Removes the old window-state-listener from window-state-listener-l
and returns the resulting multicast listener.

Removes a listener from this multicaster.

Returns the resulting multicast listener after removing the
old listener from listener-l.

Saves a Serializable listener chain to a serialization stream.

Serialization support.

Handles the windowActivated event by invoking the
windowActivated methods on listener-a and listener-b.

Handles the windowClosed event by invoking the
windowClosed methods on listener-a and listener-b.

Handles the windowClosing event by invoking the
windowClosing methods on listener-a and listener-b.

Handles the windowDeactivated event by invoking the
windowDeactivated methods on listener-a and listener-b.

Handles the windowDeiconified event by invoking the
windowDeiconified methods on listener-a and listener-b.

Handles the windowGainedFocus event by invoking the windowGainedFocus
methods on listener-a and listener-b.

Handles the windowIconified event by invoking the
windowIconified methods on listener-a and listener-b.

Handles the windowLostFocus event by invoking the windowLostFocus
methods on listener-a and listener-b.

Handles the windowOpened event by invoking the
windowOpened methods on listener-a and listener-b.

Handles the windowStateChanged event by invoking the
windowStateChanged methods on listener-a and listener-b.

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

Methods declared in interface java.awt.event.

TextListener

textValueChanged

---

#### Methods declared in interface java.awt.event. TextListener

============ FIELD DETAIL ===========

- Field Detail

- a

```java
protected final
EventListener
a
```

A variable in the event chain (listener-a)

- b

```java
protected final
EventListener
b
```

A variable in the event chain (listener-b)

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AWTEventMulticaster

```java
protected AWTEventMulticaster​(
EventListener
a,

EventListener
b)
```

Creates an event multicaster instance which chains listener-a
with listener-b. Input parameters

a

and

b

should not be

null

, though implementations may vary in
choosing whether or not to throw

NullPointerException

in that case.

**Parameters:** a

- listener-a
**Parameters:** b

- listener-b

============ METHOD DETAIL ==========

- Method Detail

- remove

```java
protected
EventListener
remove​(
EventListener
oldl)
```

Removes a listener from this multicaster.

The returned multicaster contains all the listeners in this
multicaster with the exception of all occurrences of

oldl

.
If the resulting multicaster contains only one regular listener
the regular listener may be returned. If the resulting multicaster
is empty, then

null

may be returned instead.

No exception is thrown if

oldl

is

null

.

**Parameters:** oldl

- the listener to be removed
**Returns:** resulting listener

- componentResized

```java
public void componentResized​(
ComponentEvent
e)
```

Handles the componentResized event by invoking the
componentResized methods on listener-a and listener-b.

**Specified by:** componentResized

in interface

ComponentListener
**Parameters:** e

- the component event

- componentMoved

```java
public void componentMoved​(
ComponentEvent
e)
```

Handles the componentMoved event by invoking the
componentMoved methods on listener-a and listener-b.

**Specified by:** componentMoved

in interface

ComponentListener
**Parameters:** e

- the component event

- componentShown

```java
public void componentShown​(
ComponentEvent
e)
```

Handles the componentShown event by invoking the
componentShown methods on listener-a and listener-b.

**Specified by:** componentShown

in interface

ComponentListener
**Parameters:** e

- the component event

- componentHidden

```java
public void componentHidden​(
ComponentEvent
e)
```

Handles the componentHidden event by invoking the
componentHidden methods on listener-a and listener-b.

**Specified by:** componentHidden

in interface

ComponentListener
**Parameters:** e

- the component event

- componentAdded

```java
public void componentAdded​(
ContainerEvent
e)
```

Handles the componentAdded container event by invoking the
componentAdded methods on listener-a and listener-b.

**Specified by:** componentAdded

in interface

ContainerListener
**Parameters:** e

- the component event

- componentRemoved

```java
public void componentRemoved​(
ContainerEvent
e)
```

Handles the componentRemoved container event by invoking the
componentRemoved methods on listener-a and listener-b.

**Specified by:** componentRemoved

in interface

ContainerListener
**Parameters:** e

- the component event

- focusGained

```java
public void focusGained​(
FocusEvent
e)
```

Handles the focusGained event by invoking the
focusGained methods on listener-a and listener-b.

**Specified by:** focusGained

in interface

FocusListener
**Parameters:** e

- the focus event

- focusLost

```java
public void focusLost​(
FocusEvent
e)
```

Handles the focusLost event by invoking the
focusLost methods on listener-a and listener-b.

**Specified by:** focusLost

in interface

FocusListener
**Parameters:** e

- the focus event

- keyTyped

```java
public void keyTyped​(
KeyEvent
e)
```

Handles the keyTyped event by invoking the
keyTyped methods on listener-a and listener-b.

**Specified by:** keyTyped

in interface

KeyListener
**Parameters:** e

- the key event

- keyPressed

```java
public void keyPressed​(
KeyEvent
e)
```

Handles the keyPressed event by invoking the
keyPressed methods on listener-a and listener-b.

**Specified by:** keyPressed

in interface

KeyListener
**Parameters:** e

- the key event

- keyReleased

```java
public void keyReleased​(
KeyEvent
e)
```

Handles the keyReleased event by invoking the
keyReleased methods on listener-a and listener-b.

**Specified by:** keyReleased

in interface

KeyListener
**Parameters:** e

- the key event

- mouseClicked

```java
public void mouseClicked​(
MouseEvent
e)
```

Handles the mouseClicked event by invoking the
mouseClicked methods on listener-a and listener-b.

**Specified by:** mouseClicked

in interface

MouseListener
**Parameters:** e

- the mouse event

- mousePressed

```java
public void mousePressed​(
MouseEvent
e)
```

Handles the mousePressed event by invoking the
mousePressed methods on listener-a and listener-b.

**Specified by:** mousePressed

in interface

MouseListener
**Parameters:** e

- the mouse event

- mouseReleased

```java
public void mouseReleased​(
MouseEvent
e)
```

Handles the mouseReleased event by invoking the
mouseReleased methods on listener-a and listener-b.

**Specified by:** mouseReleased

in interface

MouseListener
**Parameters:** e

- the mouse event

- mouseEntered

```java
public void mouseEntered​(
MouseEvent
e)
```

Handles the mouseEntered event by invoking the
mouseEntered methods on listener-a and listener-b.

**Specified by:** mouseEntered

in interface

MouseListener
**Parameters:** e

- the mouse event

- mouseExited

```java
public void mouseExited​(
MouseEvent
e)
```

Handles the mouseExited event by invoking the
mouseExited methods on listener-a and listener-b.

**Specified by:** mouseExited

in interface

MouseListener
**Parameters:** e

- the mouse event

- mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Handles the mouseDragged event by invoking the
mouseDragged methods on listener-a and listener-b.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the mouse event

- mouseMoved

```java
public void mouseMoved​(
MouseEvent
e)
```

Handles the mouseMoved event by invoking the
mouseMoved methods on listener-a and listener-b.

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Parameters:** e

- the mouse event

- windowOpened

```java
public void windowOpened​(
WindowEvent
e)
```

Handles the windowOpened event by invoking the
windowOpened methods on listener-a and listener-b.

**Specified by:** windowOpened

in interface

WindowListener
**Parameters:** e

- the window event

- windowClosing

```java
public void windowClosing​(
WindowEvent
e)
```

Handles the windowClosing event by invoking the
windowClosing methods on listener-a and listener-b.

**Specified by:** windowClosing

in interface

WindowListener
**Parameters:** e

- the window event

- windowClosed

```java
public void windowClosed​(
WindowEvent
e)
```

Handles the windowClosed event by invoking the
windowClosed methods on listener-a and listener-b.

**Specified by:** windowClosed

in interface

WindowListener
**Parameters:** e

- the window event

- windowIconified

```java
public void windowIconified​(
WindowEvent
e)
```

Handles the windowIconified event by invoking the
windowIconified methods on listener-a and listener-b.

**Specified by:** windowIconified

in interface

WindowListener
**Parameters:** e

- the window event
**See Also:** Window.setIconImage(java.awt.Image)

- windowDeiconified

```java
public void windowDeiconified​(
WindowEvent
e)
```

Handles the windowDeiconified event by invoking the
windowDeiconified methods on listener-a and listener-b.

**Specified by:** windowDeiconified

in interface

WindowListener
**Parameters:** e

- the window event

- windowActivated

```java
public void windowActivated​(
WindowEvent
e)
```

Handles the windowActivated event by invoking the
windowActivated methods on listener-a and listener-b.

**Specified by:** windowActivated

in interface

WindowListener
**Parameters:** e

- the window event

- windowDeactivated

```java
public void windowDeactivated​(
WindowEvent
e)
```

Handles the windowDeactivated event by invoking the
windowDeactivated methods on listener-a and listener-b.

**Specified by:** windowDeactivated

in interface

WindowListener
**Parameters:** e

- the window event

- windowStateChanged

```java
public void windowStateChanged​(
WindowEvent
e)
```

Handles the windowStateChanged event by invoking the
windowStateChanged methods on listener-a and listener-b.

**Specified by:** windowStateChanged

in interface

WindowStateListener
**Parameters:** e

- the window event
**Since:** 1.4

- windowGainedFocus

```java
public void windowGainedFocus​(
WindowEvent
e)
```

Handles the windowGainedFocus event by invoking the windowGainedFocus
methods on listener-a and listener-b.

**Specified by:** windowGainedFocus

in interface

WindowFocusListener
**Parameters:** e

- the window event
**Since:** 1.4

- windowLostFocus

```java
public void windowLostFocus​(
WindowEvent
e)
```

Handles the windowLostFocus event by invoking the windowLostFocus
methods on listener-a and listener-b.

**Specified by:** windowLostFocus

in interface

WindowFocusListener
**Parameters:** e

- the window event
**Since:** 1.4

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

Handles the actionPerformed event by invoking the
actionPerformed methods on listener-a and listener-b.

**Specified by:** actionPerformed

in interface

ActionListener
**Parameters:** e

- the action event

- itemStateChanged

```java
public void itemStateChanged​(
ItemEvent
e)
```

Handles the itemStateChanged event by invoking the
itemStateChanged methods on listener-a and listener-b.

**Specified by:** itemStateChanged

in interface

ItemListener
**Parameters:** e

- the item event

- adjustmentValueChanged

```java
public void adjustmentValueChanged​(
AdjustmentEvent
e)
```

Handles the adjustmentValueChanged event by invoking the
adjustmentValueChanged methods on listener-a and listener-b.

**Specified by:** adjustmentValueChanged

in interface

AdjustmentListener
**Parameters:** e

- the adjustment event

- inputMethodTextChanged

```java
public void inputMethodTextChanged​(
InputMethodEvent
e)
```

Handles the inputMethodTextChanged event by invoking the
inputMethodTextChanged methods on listener-a and listener-b.

**Specified by:** inputMethodTextChanged

in interface

InputMethodListener
**Parameters:** e

- the item event

- caretPositionChanged

```java
public void caretPositionChanged​(
InputMethodEvent
e)
```

Handles the caretPositionChanged event by invoking the
caretPositionChanged methods on listener-a and listener-b.

**Specified by:** caretPositionChanged

in interface

InputMethodListener
**Parameters:** e

- the item event

- hierarchyChanged

```java
public void hierarchyChanged​(
HierarchyEvent
e)
```

Handles the hierarchyChanged event by invoking the
hierarchyChanged methods on listener-a and listener-b.

**Specified by:** hierarchyChanged

in interface

HierarchyListener
**Parameters:** e

- the item event
**Since:** 1.3
**See Also:** HierarchyEvent.getChangeFlags()

- ancestorMoved

```java
public void ancestorMoved​(
HierarchyEvent
e)
```

Handles the ancestorMoved event by invoking the
ancestorMoved methods on listener-a and listener-b.

**Specified by:** ancestorMoved

in interface

HierarchyBoundsListener
**Parameters:** e

- the item event
**Since:** 1.3

- ancestorResized

```java
public void ancestorResized​(
HierarchyEvent
e)
```

Handles the ancestorResized event by invoking the
ancestorResized methods on listener-a and listener-b.

**Specified by:** ancestorResized

in interface

HierarchyBoundsListener
**Parameters:** e

- the item event
**Since:** 1.3

- mouseWheelMoved

```java
public void mouseWheelMoved​(
MouseWheelEvent
e)
```

Handles the mouseWheelMoved event by invoking the
mouseWheelMoved methods on listener-a and listener-b.

**Specified by:** mouseWheelMoved

in interface

MouseWheelListener
**Parameters:** e

- the mouse event
**Since:** 1.4
**See Also:** MouseWheelEvent

- add

```java
public static
ComponentListener
add​(
ComponentListener
a,

ComponentListener
b)
```

Adds component-listener-a with component-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- component-listener-a
**Parameters:** b

- component-listener-b
**Returns:** the resulting listener

- add

```java
public static
ContainerListener
add​(
ContainerListener
a,

ContainerListener
b)
```

Adds container-listener-a with container-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- container-listener-a
**Parameters:** b

- container-listener-b
**Returns:** the resulting listener

- add

```java
public static
FocusListener
add​(
FocusListener
a,

FocusListener
b)
```

Adds focus-listener-a with focus-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- focus-listener-a
**Parameters:** b

- focus-listener-b
**Returns:** the resulting listener

- add

```java
public static
KeyListener
add​(
KeyListener
a,

KeyListener
b)
```

Adds key-listener-a with key-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- key-listener-a
**Parameters:** b

- key-listener-b
**Returns:** the resulting listener

- add

```java
public static
MouseListener
add​(
MouseListener
a,

MouseListener
b)
```

Adds mouse-listener-a with mouse-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- mouse-listener-a
**Parameters:** b

- mouse-listener-b
**Returns:** the resulting listener

- add

```java
public static
MouseMotionListener
add​(
MouseMotionListener
a,

MouseMotionListener
b)
```

Adds mouse-motion-listener-a with mouse-motion-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- mouse-motion-listener-a
**Parameters:** b

- mouse-motion-listener-b
**Returns:** the resulting listener

- add

```java
public static
WindowListener
add​(
WindowListener
a,

WindowListener
b)
```

Adds window-listener-a with window-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- window-listener-a
**Parameters:** b

- window-listener-b
**Returns:** the resulting listener

- add

```java
public static
WindowStateListener
add​(
WindowStateListener
a,

WindowStateListener
b)
```

Adds window-state-listener-a with window-state-listener-b
and returns the resulting multicast listener.

**Parameters:** a

- window-state-listener-a
**Parameters:** b

- window-state-listener-b
**Returns:** the resulting listener
**Since:** 1.4

- add

```java
public static
WindowFocusListener
add​(
WindowFocusListener
a,

WindowFocusListener
b)
```

Adds window-focus-listener-a with window-focus-listener-b
and returns the resulting multicast listener.

**Parameters:** a

- window-focus-listener-a
**Parameters:** b

- window-focus-listener-b
**Returns:** the resulting listener
**Since:** 1.4

- add

```java
public static
ActionListener
add​(
ActionListener
a,

ActionListener
b)
```

Adds action-listener-a with action-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- action-listener-a
**Parameters:** b

- action-listener-b
**Returns:** the resulting listener

- add

```java
public static
ItemListener
add​(
ItemListener
a,

ItemListener
b)
```

Adds item-listener-a with item-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- item-listener-a
**Parameters:** b

- item-listener-b
**Returns:** the resulting listener

- add

```java
public static
AdjustmentListener
add​(
AdjustmentListener
a,

AdjustmentListener
b)
```

Adds adjustment-listener-a with adjustment-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- adjustment-listener-a
**Parameters:** b

- adjustment-listener-b
**Returns:** the resulting listener

- add

```java
public static
TextListener
add​(
TextListener
a,

TextListener
b)
```

Adds text-listener-a with text-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- text-listener-a
**Parameters:** b

- text-listener-b
**Returns:** the resulting listener

- add

```java
public static
InputMethodListener
add​(
InputMethodListener
a,

InputMethodListener
b)
```

Adds input-method-listener-a with input-method-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- input-method-listener-a
**Parameters:** b

- input-method-listener-b
**Returns:** the resulting listener

- add

```java
public static
HierarchyListener
add​(
HierarchyListener
a,

HierarchyListener
b)
```

Adds hierarchy-listener-a with hierarchy-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- hierarchy-listener-a
**Parameters:** b

- hierarchy-listener-b
**Returns:** the resulting listener
**Since:** 1.3

- add

```java
public static
HierarchyBoundsListener
add​(
HierarchyBoundsListener
a,

HierarchyBoundsListener
b)
```

Adds hierarchy-bounds-listener-a with hierarchy-bounds-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- hierarchy-bounds-listener-a
**Parameters:** b

- hierarchy-bounds-listener-b
**Returns:** the resulting listener
**Since:** 1.3

- add

```java
public static
MouseWheelListener
add​(
MouseWheelListener
a,

MouseWheelListener
b)
```

Adds mouse-wheel-listener-a with mouse-wheel-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- mouse-wheel-listener-a
**Parameters:** b

- mouse-wheel-listener-b
**Returns:** the resulting listener
**Since:** 1.4

- remove

```java
public static
ComponentListener
remove​(
ComponentListener
l,

ComponentListener
oldl)
```

Removes the old component-listener from component-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- component-listener-l
**Parameters:** oldl

- the component-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
ContainerListener
remove​(
ContainerListener
l,

ContainerListener
oldl)
```

Removes the old container-listener from container-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- container-listener-l
**Parameters:** oldl

- the container-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
FocusListener
remove​(
FocusListener
l,

FocusListener
oldl)
```

Removes the old focus-listener from focus-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- focus-listener-l
**Parameters:** oldl

- the focus-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
KeyListener
remove​(
KeyListener
l,

KeyListener
oldl)
```

Removes the old key-listener from key-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- key-listener-l
**Parameters:** oldl

- the key-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
MouseListener
remove​(
MouseListener
l,

MouseListener
oldl)
```

Removes the old mouse-listener from mouse-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- mouse-listener-l
**Parameters:** oldl

- the mouse-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
MouseMotionListener
remove​(
MouseMotionListener
l,

MouseMotionListener
oldl)
```

Removes the old mouse-motion-listener from mouse-motion-listener-l
and returns the resulting multicast listener.

**Parameters:** l

- mouse-motion-listener-l
**Parameters:** oldl

- the mouse-motion-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
WindowListener
remove​(
WindowListener
l,

WindowListener
oldl)
```

Removes the old window-listener from window-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- window-listener-l
**Parameters:** oldl

- the window-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
WindowStateListener
remove​(
WindowStateListener
l,

WindowStateListener
oldl)
```

Removes the old window-state-listener from window-state-listener-l
and returns the resulting multicast listener.

**Parameters:** l

- window-state-listener-l
**Parameters:** oldl

- the window-state-listener being removed
**Returns:** the resulting listener
**Since:** 1.4

- remove

```java
public static
WindowFocusListener
remove​(
WindowFocusListener
l,

WindowFocusListener
oldl)
```

Removes the old window-focus-listener from window-focus-listener-l
and returns the resulting multicast listener.

**Parameters:** l

- window-focus-listener-l
**Parameters:** oldl

- the window-focus-listener being removed
**Returns:** the resulting listener
**Since:** 1.4

- remove

```java
public static
ActionListener
remove​(
ActionListener
l,

ActionListener
oldl)
```

Removes the old action-listener from action-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- action-listener-l
**Parameters:** oldl

- the action-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
ItemListener
remove​(
ItemListener
l,

ItemListener
oldl)
```

Removes the old item-listener from item-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- item-listener-l
**Parameters:** oldl

- the item-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
AdjustmentListener
remove​(
AdjustmentListener
l,

AdjustmentListener
oldl)
```

Removes the old adjustment-listener from adjustment-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- adjustment-listener-l
**Parameters:** oldl

- the adjustment-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
TextListener
remove​(
TextListener
l,

TextListener
oldl)
```

Removes the old text-listener from text-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- text-listener-l
**Parameters:** oldl

- the text-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
InputMethodListener
remove​(
InputMethodListener
l,

InputMethodListener
oldl)
```

Removes the old input-method-listener from input-method-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- input-method-listener-l
**Parameters:** oldl

- the input-method-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
HierarchyListener
remove​(
HierarchyListener
l,

HierarchyListener
oldl)
```

Removes the old hierarchy-listener from hierarchy-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- hierarchy-listener-l
**Parameters:** oldl

- the hierarchy-listener being removed
**Returns:** the resulting listener
**Since:** 1.3

- remove

```java
public static
HierarchyBoundsListener
remove​(
HierarchyBoundsListener
l,

HierarchyBoundsListener
oldl)
```

Removes the old hierarchy-bounds-listener from
hierarchy-bounds-listener-l and returns the resulting multicast
listener.

**Parameters:** l

- hierarchy-bounds-listener-l
**Parameters:** oldl

- the hierarchy-bounds-listener being removed
**Returns:** the resulting listener
**Since:** 1.3

- remove

```java
public static
MouseWheelListener
remove​(
MouseWheelListener
l,

MouseWheelListener
oldl)
```

Removes the old mouse-wheel-listener from mouse-wheel-listener-l
and returns the resulting multicast listener.

**Parameters:** l

- mouse-wheel-listener-l
**Parameters:** oldl

- the mouse-wheel-listener being removed
**Returns:** the resulting listener
**Since:** 1.4

- addInternal

```java
protected static
EventListener
addInternal​(
EventListener
a,

EventListener
b)
```

Returns the resulting multicast listener from adding listener-a
and listener-b together.
If listener-a is null, it returns listener-b;
If listener-b is null, it returns listener-a
If neither are null, then it creates and returns
a new AWTEventMulticaster instance which chains a with b.

**Parameters:** a

- event listener-a
**Parameters:** b

- event listener-b
**Returns:** the resulting listener

- removeInternal

```java
protected static
EventListener
removeInternal​(
EventListener
l,

EventListener
oldl)
```

Returns the resulting multicast listener after removing the
old listener from listener-l.
If listener-l equals the old listener OR listener-l is null,
returns null.
Else if listener-l is an instance of AWTEventMulticaster,
then it removes the old listener from it.
Else, returns listener l.

**Parameters:** l

- the listener being removed from
**Parameters:** oldl

- the listener being removed
**Returns:** the resulting listener

- saveInternal

```java
protected void saveInternal​(
ObjectOutputStream
s,

String
k)
throws
IOException
```

Serialization support. Saves all Serializable listeners
to a serialization stream.

**Parameters:** s

- the stream to save to
**Parameters:** k

- a prefix stream to put before each serializable listener
**Throws:** IOException

- if serialization fails

- save

```java
protected static void save​(
ObjectOutputStream
s,

String
k,

EventListener
l)
throws
IOException
```

Saves a Serializable listener chain to a serialization stream.

**Parameters:** s

- the stream to save to
**Parameters:** k

- a prefix stream to put before each serializable listener
**Parameters:** l

- the listener chain to save
**Throws:** IOException

- if serialization fails

- getListeners

```java
public static <T extends
EventListener
> T[] getListeners​(
EventListener
l,

Class
<T> listenerType)
```

Returns an array of all the objects chained as

Foo

Listener

s by the specified

java.util.EventListener

.

Foo

Listener

s are chained by the

AWTEventMulticaster

using the

add

Foo

Listener

method.
If a

null

listener is specified, this method returns an
empty array. If the specified listener is not an instance of

AWTEventMulticaster

, this method returns an array which
contains only the specified listener. If no such listeners are chained,
this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** l

- the specified

java.util.EventListener
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects chained as

Foo

Listener

s by the specified multicast
listener, or an empty array if no such listeners have been
chained by the specified multicast listener
**Throws:** NullPointerException

- if the specified

listenertype

parameter is

null
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.4

Field Detail

- a

```java
protected final
EventListener
a
```

A variable in the event chain (listener-a)

- b

```java
protected final
EventListener
b
```

A variable in the event chain (listener-b)

---

#### Field Detail

a

```java
protected final
EventListener
a
```

A variable in the event chain (listener-a)

---

#### a

protected final

EventListener

a

A variable in the event chain (listener-a)

b

```java
protected final
EventListener
b
```

A variable in the event chain (listener-b)

---

#### b

protected final

EventListener

b

A variable in the event chain (listener-b)

Constructor Detail

- AWTEventMulticaster

```java
protected AWTEventMulticaster​(
EventListener
a,

EventListener
b)
```

Creates an event multicaster instance which chains listener-a
with listener-b. Input parameters

a

and

b

should not be

null

, though implementations may vary in
choosing whether or not to throw

NullPointerException

in that case.

**Parameters:** a

- listener-a
**Parameters:** b

- listener-b

---

#### Constructor Detail

AWTEventMulticaster

```java
protected AWTEventMulticaster​(
EventListener
a,

EventListener
b)
```

Creates an event multicaster instance which chains listener-a
with listener-b. Input parameters

a

and

b

should not be

null

, though implementations may vary in
choosing whether or not to throw

NullPointerException

in that case.

**Parameters:** a

- listener-a
**Parameters:** b

- listener-b

---

#### AWTEventMulticaster

protected AWTEventMulticaster​(

EventListener

a,

EventListener

b)

Creates an event multicaster instance which chains listener-a
with listener-b. Input parameters

a

and

b

should not be

null

, though implementations may vary in
choosing whether or not to throw

NullPointerException

in that case.

Method Detail

- remove

```java
protected
EventListener
remove​(
EventListener
oldl)
```

Removes a listener from this multicaster.

The returned multicaster contains all the listeners in this
multicaster with the exception of all occurrences of

oldl

.
If the resulting multicaster contains only one regular listener
the regular listener may be returned. If the resulting multicaster
is empty, then

null

may be returned instead.

No exception is thrown if

oldl

is

null

.

**Parameters:** oldl

- the listener to be removed
**Returns:** resulting listener

- componentResized

```java
public void componentResized​(
ComponentEvent
e)
```

Handles the componentResized event by invoking the
componentResized methods on listener-a and listener-b.

**Specified by:** componentResized

in interface

ComponentListener
**Parameters:** e

- the component event

- componentMoved

```java
public void componentMoved​(
ComponentEvent
e)
```

Handles the componentMoved event by invoking the
componentMoved methods on listener-a and listener-b.

**Specified by:** componentMoved

in interface

ComponentListener
**Parameters:** e

- the component event

- componentShown

```java
public void componentShown​(
ComponentEvent
e)
```

Handles the componentShown event by invoking the
componentShown methods on listener-a and listener-b.

**Specified by:** componentShown

in interface

ComponentListener
**Parameters:** e

- the component event

- componentHidden

```java
public void componentHidden​(
ComponentEvent
e)
```

Handles the componentHidden event by invoking the
componentHidden methods on listener-a and listener-b.

**Specified by:** componentHidden

in interface

ComponentListener
**Parameters:** e

- the component event

- componentAdded

```java
public void componentAdded​(
ContainerEvent
e)
```

Handles the componentAdded container event by invoking the
componentAdded methods on listener-a and listener-b.

**Specified by:** componentAdded

in interface

ContainerListener
**Parameters:** e

- the component event

- componentRemoved

```java
public void componentRemoved​(
ContainerEvent
e)
```

Handles the componentRemoved container event by invoking the
componentRemoved methods on listener-a and listener-b.

**Specified by:** componentRemoved

in interface

ContainerListener
**Parameters:** e

- the component event

- focusGained

```java
public void focusGained​(
FocusEvent
e)
```

Handles the focusGained event by invoking the
focusGained methods on listener-a and listener-b.

**Specified by:** focusGained

in interface

FocusListener
**Parameters:** e

- the focus event

- focusLost

```java
public void focusLost​(
FocusEvent
e)
```

Handles the focusLost event by invoking the
focusLost methods on listener-a and listener-b.

**Specified by:** focusLost

in interface

FocusListener
**Parameters:** e

- the focus event

- keyTyped

```java
public void keyTyped​(
KeyEvent
e)
```

Handles the keyTyped event by invoking the
keyTyped methods on listener-a and listener-b.

**Specified by:** keyTyped

in interface

KeyListener
**Parameters:** e

- the key event

- keyPressed

```java
public void keyPressed​(
KeyEvent
e)
```

Handles the keyPressed event by invoking the
keyPressed methods on listener-a and listener-b.

**Specified by:** keyPressed

in interface

KeyListener
**Parameters:** e

- the key event

- keyReleased

```java
public void keyReleased​(
KeyEvent
e)
```

Handles the keyReleased event by invoking the
keyReleased methods on listener-a and listener-b.

**Specified by:** keyReleased

in interface

KeyListener
**Parameters:** e

- the key event

- mouseClicked

```java
public void mouseClicked​(
MouseEvent
e)
```

Handles the mouseClicked event by invoking the
mouseClicked methods on listener-a and listener-b.

**Specified by:** mouseClicked

in interface

MouseListener
**Parameters:** e

- the mouse event

- mousePressed

```java
public void mousePressed​(
MouseEvent
e)
```

Handles the mousePressed event by invoking the
mousePressed methods on listener-a and listener-b.

**Specified by:** mousePressed

in interface

MouseListener
**Parameters:** e

- the mouse event

- mouseReleased

```java
public void mouseReleased​(
MouseEvent
e)
```

Handles the mouseReleased event by invoking the
mouseReleased methods on listener-a and listener-b.

**Specified by:** mouseReleased

in interface

MouseListener
**Parameters:** e

- the mouse event

- mouseEntered

```java
public void mouseEntered​(
MouseEvent
e)
```

Handles the mouseEntered event by invoking the
mouseEntered methods on listener-a and listener-b.

**Specified by:** mouseEntered

in interface

MouseListener
**Parameters:** e

- the mouse event

- mouseExited

```java
public void mouseExited​(
MouseEvent
e)
```

Handles the mouseExited event by invoking the
mouseExited methods on listener-a and listener-b.

**Specified by:** mouseExited

in interface

MouseListener
**Parameters:** e

- the mouse event

- mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Handles the mouseDragged event by invoking the
mouseDragged methods on listener-a and listener-b.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the mouse event

- mouseMoved

```java
public void mouseMoved​(
MouseEvent
e)
```

Handles the mouseMoved event by invoking the
mouseMoved methods on listener-a and listener-b.

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Parameters:** e

- the mouse event

- windowOpened

```java
public void windowOpened​(
WindowEvent
e)
```

Handles the windowOpened event by invoking the
windowOpened methods on listener-a and listener-b.

**Specified by:** windowOpened

in interface

WindowListener
**Parameters:** e

- the window event

- windowClosing

```java
public void windowClosing​(
WindowEvent
e)
```

Handles the windowClosing event by invoking the
windowClosing methods on listener-a and listener-b.

**Specified by:** windowClosing

in interface

WindowListener
**Parameters:** e

- the window event

- windowClosed

```java
public void windowClosed​(
WindowEvent
e)
```

Handles the windowClosed event by invoking the
windowClosed methods on listener-a and listener-b.

**Specified by:** windowClosed

in interface

WindowListener
**Parameters:** e

- the window event

- windowIconified

```java
public void windowIconified​(
WindowEvent
e)
```

Handles the windowIconified event by invoking the
windowIconified methods on listener-a and listener-b.

**Specified by:** windowIconified

in interface

WindowListener
**Parameters:** e

- the window event
**See Also:** Window.setIconImage(java.awt.Image)

- windowDeiconified

```java
public void windowDeiconified​(
WindowEvent
e)
```

Handles the windowDeiconified event by invoking the
windowDeiconified methods on listener-a and listener-b.

**Specified by:** windowDeiconified

in interface

WindowListener
**Parameters:** e

- the window event

- windowActivated

```java
public void windowActivated​(
WindowEvent
e)
```

Handles the windowActivated event by invoking the
windowActivated methods on listener-a and listener-b.

**Specified by:** windowActivated

in interface

WindowListener
**Parameters:** e

- the window event

- windowDeactivated

```java
public void windowDeactivated​(
WindowEvent
e)
```

Handles the windowDeactivated event by invoking the
windowDeactivated methods on listener-a and listener-b.

**Specified by:** windowDeactivated

in interface

WindowListener
**Parameters:** e

- the window event

- windowStateChanged

```java
public void windowStateChanged​(
WindowEvent
e)
```

Handles the windowStateChanged event by invoking the
windowStateChanged methods on listener-a and listener-b.

**Specified by:** windowStateChanged

in interface

WindowStateListener
**Parameters:** e

- the window event
**Since:** 1.4

- windowGainedFocus

```java
public void windowGainedFocus​(
WindowEvent
e)
```

Handles the windowGainedFocus event by invoking the windowGainedFocus
methods on listener-a and listener-b.

**Specified by:** windowGainedFocus

in interface

WindowFocusListener
**Parameters:** e

- the window event
**Since:** 1.4

- windowLostFocus

```java
public void windowLostFocus​(
WindowEvent
e)
```

Handles the windowLostFocus event by invoking the windowLostFocus
methods on listener-a and listener-b.

**Specified by:** windowLostFocus

in interface

WindowFocusListener
**Parameters:** e

- the window event
**Since:** 1.4

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

Handles the actionPerformed event by invoking the
actionPerformed methods on listener-a and listener-b.

**Specified by:** actionPerformed

in interface

ActionListener
**Parameters:** e

- the action event

- itemStateChanged

```java
public void itemStateChanged​(
ItemEvent
e)
```

Handles the itemStateChanged event by invoking the
itemStateChanged methods on listener-a and listener-b.

**Specified by:** itemStateChanged

in interface

ItemListener
**Parameters:** e

- the item event

- adjustmentValueChanged

```java
public void adjustmentValueChanged​(
AdjustmentEvent
e)
```

Handles the adjustmentValueChanged event by invoking the
adjustmentValueChanged methods on listener-a and listener-b.

**Specified by:** adjustmentValueChanged

in interface

AdjustmentListener
**Parameters:** e

- the adjustment event

- inputMethodTextChanged

```java
public void inputMethodTextChanged​(
InputMethodEvent
e)
```

Handles the inputMethodTextChanged event by invoking the
inputMethodTextChanged methods on listener-a and listener-b.

**Specified by:** inputMethodTextChanged

in interface

InputMethodListener
**Parameters:** e

- the item event

- caretPositionChanged

```java
public void caretPositionChanged​(
InputMethodEvent
e)
```

Handles the caretPositionChanged event by invoking the
caretPositionChanged methods on listener-a and listener-b.

**Specified by:** caretPositionChanged

in interface

InputMethodListener
**Parameters:** e

- the item event

- hierarchyChanged

```java
public void hierarchyChanged​(
HierarchyEvent
e)
```

Handles the hierarchyChanged event by invoking the
hierarchyChanged methods on listener-a and listener-b.

**Specified by:** hierarchyChanged

in interface

HierarchyListener
**Parameters:** e

- the item event
**Since:** 1.3
**See Also:** HierarchyEvent.getChangeFlags()

- ancestorMoved

```java
public void ancestorMoved​(
HierarchyEvent
e)
```

Handles the ancestorMoved event by invoking the
ancestorMoved methods on listener-a and listener-b.

**Specified by:** ancestorMoved

in interface

HierarchyBoundsListener
**Parameters:** e

- the item event
**Since:** 1.3

- ancestorResized

```java
public void ancestorResized​(
HierarchyEvent
e)
```

Handles the ancestorResized event by invoking the
ancestorResized methods on listener-a and listener-b.

**Specified by:** ancestorResized

in interface

HierarchyBoundsListener
**Parameters:** e

- the item event
**Since:** 1.3

- mouseWheelMoved

```java
public void mouseWheelMoved​(
MouseWheelEvent
e)
```

Handles the mouseWheelMoved event by invoking the
mouseWheelMoved methods on listener-a and listener-b.

**Specified by:** mouseWheelMoved

in interface

MouseWheelListener
**Parameters:** e

- the mouse event
**Since:** 1.4
**See Also:** MouseWheelEvent

- add

```java
public static
ComponentListener
add​(
ComponentListener
a,

ComponentListener
b)
```

Adds component-listener-a with component-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- component-listener-a
**Parameters:** b

- component-listener-b
**Returns:** the resulting listener

- add

```java
public static
ContainerListener
add​(
ContainerListener
a,

ContainerListener
b)
```

Adds container-listener-a with container-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- container-listener-a
**Parameters:** b

- container-listener-b
**Returns:** the resulting listener

- add

```java
public static
FocusListener
add​(
FocusListener
a,

FocusListener
b)
```

Adds focus-listener-a with focus-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- focus-listener-a
**Parameters:** b

- focus-listener-b
**Returns:** the resulting listener

- add

```java
public static
KeyListener
add​(
KeyListener
a,

KeyListener
b)
```

Adds key-listener-a with key-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- key-listener-a
**Parameters:** b

- key-listener-b
**Returns:** the resulting listener

- add

```java
public static
MouseListener
add​(
MouseListener
a,

MouseListener
b)
```

Adds mouse-listener-a with mouse-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- mouse-listener-a
**Parameters:** b

- mouse-listener-b
**Returns:** the resulting listener

- add

```java
public static
MouseMotionListener
add​(
MouseMotionListener
a,

MouseMotionListener
b)
```

Adds mouse-motion-listener-a with mouse-motion-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- mouse-motion-listener-a
**Parameters:** b

- mouse-motion-listener-b
**Returns:** the resulting listener

- add

```java
public static
WindowListener
add​(
WindowListener
a,

WindowListener
b)
```

Adds window-listener-a with window-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- window-listener-a
**Parameters:** b

- window-listener-b
**Returns:** the resulting listener

- add

```java
public static
WindowStateListener
add​(
WindowStateListener
a,

WindowStateListener
b)
```

Adds window-state-listener-a with window-state-listener-b
and returns the resulting multicast listener.

**Parameters:** a

- window-state-listener-a
**Parameters:** b

- window-state-listener-b
**Returns:** the resulting listener
**Since:** 1.4

- add

```java
public static
WindowFocusListener
add​(
WindowFocusListener
a,

WindowFocusListener
b)
```

Adds window-focus-listener-a with window-focus-listener-b
and returns the resulting multicast listener.

**Parameters:** a

- window-focus-listener-a
**Parameters:** b

- window-focus-listener-b
**Returns:** the resulting listener
**Since:** 1.4

- add

```java
public static
ActionListener
add​(
ActionListener
a,

ActionListener
b)
```

Adds action-listener-a with action-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- action-listener-a
**Parameters:** b

- action-listener-b
**Returns:** the resulting listener

- add

```java
public static
ItemListener
add​(
ItemListener
a,

ItemListener
b)
```

Adds item-listener-a with item-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- item-listener-a
**Parameters:** b

- item-listener-b
**Returns:** the resulting listener

- add

```java
public static
AdjustmentListener
add​(
AdjustmentListener
a,

AdjustmentListener
b)
```

Adds adjustment-listener-a with adjustment-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- adjustment-listener-a
**Parameters:** b

- adjustment-listener-b
**Returns:** the resulting listener

- add

```java
public static
TextListener
add​(
TextListener
a,

TextListener
b)
```

Adds text-listener-a with text-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- text-listener-a
**Parameters:** b

- text-listener-b
**Returns:** the resulting listener

- add

```java
public static
InputMethodListener
add​(
InputMethodListener
a,

InputMethodListener
b)
```

Adds input-method-listener-a with input-method-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- input-method-listener-a
**Parameters:** b

- input-method-listener-b
**Returns:** the resulting listener

- add

```java
public static
HierarchyListener
add​(
HierarchyListener
a,

HierarchyListener
b)
```

Adds hierarchy-listener-a with hierarchy-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- hierarchy-listener-a
**Parameters:** b

- hierarchy-listener-b
**Returns:** the resulting listener
**Since:** 1.3

- add

```java
public static
HierarchyBoundsListener
add​(
HierarchyBoundsListener
a,

HierarchyBoundsListener
b)
```

Adds hierarchy-bounds-listener-a with hierarchy-bounds-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- hierarchy-bounds-listener-a
**Parameters:** b

- hierarchy-bounds-listener-b
**Returns:** the resulting listener
**Since:** 1.3

- add

```java
public static
MouseWheelListener
add​(
MouseWheelListener
a,

MouseWheelListener
b)
```

Adds mouse-wheel-listener-a with mouse-wheel-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- mouse-wheel-listener-a
**Parameters:** b

- mouse-wheel-listener-b
**Returns:** the resulting listener
**Since:** 1.4

- remove

```java
public static
ComponentListener
remove​(
ComponentListener
l,

ComponentListener
oldl)
```

Removes the old component-listener from component-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- component-listener-l
**Parameters:** oldl

- the component-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
ContainerListener
remove​(
ContainerListener
l,

ContainerListener
oldl)
```

Removes the old container-listener from container-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- container-listener-l
**Parameters:** oldl

- the container-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
FocusListener
remove​(
FocusListener
l,

FocusListener
oldl)
```

Removes the old focus-listener from focus-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- focus-listener-l
**Parameters:** oldl

- the focus-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
KeyListener
remove​(
KeyListener
l,

KeyListener
oldl)
```

Removes the old key-listener from key-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- key-listener-l
**Parameters:** oldl

- the key-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
MouseListener
remove​(
MouseListener
l,

MouseListener
oldl)
```

Removes the old mouse-listener from mouse-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- mouse-listener-l
**Parameters:** oldl

- the mouse-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
MouseMotionListener
remove​(
MouseMotionListener
l,

MouseMotionListener
oldl)
```

Removes the old mouse-motion-listener from mouse-motion-listener-l
and returns the resulting multicast listener.

**Parameters:** l

- mouse-motion-listener-l
**Parameters:** oldl

- the mouse-motion-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
WindowListener
remove​(
WindowListener
l,

WindowListener
oldl)
```

Removes the old window-listener from window-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- window-listener-l
**Parameters:** oldl

- the window-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
WindowStateListener
remove​(
WindowStateListener
l,

WindowStateListener
oldl)
```

Removes the old window-state-listener from window-state-listener-l
and returns the resulting multicast listener.

**Parameters:** l

- window-state-listener-l
**Parameters:** oldl

- the window-state-listener being removed
**Returns:** the resulting listener
**Since:** 1.4

- remove

```java
public static
WindowFocusListener
remove​(
WindowFocusListener
l,

WindowFocusListener
oldl)
```

Removes the old window-focus-listener from window-focus-listener-l
and returns the resulting multicast listener.

**Parameters:** l

- window-focus-listener-l
**Parameters:** oldl

- the window-focus-listener being removed
**Returns:** the resulting listener
**Since:** 1.4

- remove

```java
public static
ActionListener
remove​(
ActionListener
l,

ActionListener
oldl)
```

Removes the old action-listener from action-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- action-listener-l
**Parameters:** oldl

- the action-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
ItemListener
remove​(
ItemListener
l,

ItemListener
oldl)
```

Removes the old item-listener from item-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- item-listener-l
**Parameters:** oldl

- the item-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
AdjustmentListener
remove​(
AdjustmentListener
l,

AdjustmentListener
oldl)
```

Removes the old adjustment-listener from adjustment-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- adjustment-listener-l
**Parameters:** oldl

- the adjustment-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
TextListener
remove​(
TextListener
l,

TextListener
oldl)
```

Removes the old text-listener from text-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- text-listener-l
**Parameters:** oldl

- the text-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
InputMethodListener
remove​(
InputMethodListener
l,

InputMethodListener
oldl)
```

Removes the old input-method-listener from input-method-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- input-method-listener-l
**Parameters:** oldl

- the input-method-listener being removed
**Returns:** the resulting listener

- remove

```java
public static
HierarchyListener
remove​(
HierarchyListener
l,

HierarchyListener
oldl)
```

Removes the old hierarchy-listener from hierarchy-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- hierarchy-listener-l
**Parameters:** oldl

- the hierarchy-listener being removed
**Returns:** the resulting listener
**Since:** 1.3

- remove

```java
public static
HierarchyBoundsListener
remove​(
HierarchyBoundsListener
l,

HierarchyBoundsListener
oldl)
```

Removes the old hierarchy-bounds-listener from
hierarchy-bounds-listener-l and returns the resulting multicast
listener.

**Parameters:** l

- hierarchy-bounds-listener-l
**Parameters:** oldl

- the hierarchy-bounds-listener being removed
**Returns:** the resulting listener
**Since:** 1.3

- remove

```java
public static
MouseWheelListener
remove​(
MouseWheelListener
l,

MouseWheelListener
oldl)
```

Removes the old mouse-wheel-listener from mouse-wheel-listener-l
and returns the resulting multicast listener.

**Parameters:** l

- mouse-wheel-listener-l
**Parameters:** oldl

- the mouse-wheel-listener being removed
**Returns:** the resulting listener
**Since:** 1.4

- addInternal

```java
protected static
EventListener
addInternal​(
EventListener
a,

EventListener
b)
```

Returns the resulting multicast listener from adding listener-a
and listener-b together.
If listener-a is null, it returns listener-b;
If listener-b is null, it returns listener-a
If neither are null, then it creates and returns
a new AWTEventMulticaster instance which chains a with b.

**Parameters:** a

- event listener-a
**Parameters:** b

- event listener-b
**Returns:** the resulting listener

- removeInternal

```java
protected static
EventListener
removeInternal​(
EventListener
l,

EventListener
oldl)
```

Returns the resulting multicast listener after removing the
old listener from listener-l.
If listener-l equals the old listener OR listener-l is null,
returns null.
Else if listener-l is an instance of AWTEventMulticaster,
then it removes the old listener from it.
Else, returns listener l.

**Parameters:** l

- the listener being removed from
**Parameters:** oldl

- the listener being removed
**Returns:** the resulting listener

- saveInternal

```java
protected void saveInternal​(
ObjectOutputStream
s,

String
k)
throws
IOException
```

Serialization support. Saves all Serializable listeners
to a serialization stream.

**Parameters:** s

- the stream to save to
**Parameters:** k

- a prefix stream to put before each serializable listener
**Throws:** IOException

- if serialization fails

- save

```java
protected static void save​(
ObjectOutputStream
s,

String
k,

EventListener
l)
throws
IOException
```

Saves a Serializable listener chain to a serialization stream.

**Parameters:** s

- the stream to save to
**Parameters:** k

- a prefix stream to put before each serializable listener
**Parameters:** l

- the listener chain to save
**Throws:** IOException

- if serialization fails

- getListeners

```java
public static <T extends
EventListener
> T[] getListeners​(
EventListener
l,

Class
<T> listenerType)
```

Returns an array of all the objects chained as

Foo

Listener

s by the specified

java.util.EventListener

.

Foo

Listener

s are chained by the

AWTEventMulticaster

using the

add

Foo

Listener

method.
If a

null

listener is specified, this method returns an
empty array. If the specified listener is not an instance of

AWTEventMulticaster

, this method returns an array which
contains only the specified listener. If no such listeners are chained,
this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** l

- the specified

java.util.EventListener
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects chained as

Foo

Listener

s by the specified multicast
listener, or an empty array if no such listeners have been
chained by the specified multicast listener
**Throws:** NullPointerException

- if the specified

listenertype

parameter is

null
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.4

---

#### Method Detail

remove

```java
protected
EventListener
remove​(
EventListener
oldl)
```

Removes a listener from this multicaster.

The returned multicaster contains all the listeners in this
multicaster with the exception of all occurrences of

oldl

.
If the resulting multicaster contains only one regular listener
the regular listener may be returned. If the resulting multicaster
is empty, then

null

may be returned instead.

No exception is thrown if

oldl

is

null

.

**Parameters:** oldl

- the listener to be removed
**Returns:** resulting listener

---

#### remove

protected

EventListener

remove​(

EventListener

oldl)

Removes a listener from this multicaster.

The returned multicaster contains all the listeners in this
multicaster with the exception of all occurrences of

oldl

.
If the resulting multicaster contains only one regular listener
the regular listener may be returned. If the resulting multicaster
is empty, then

null

may be returned instead.

No exception is thrown if

oldl

is

null

.

The returned multicaster contains all the listeners in this
multicaster with the exception of all occurrences of

oldl

.
If the resulting multicaster contains only one regular listener
the regular listener may be returned. If the resulting multicaster
is empty, then

null

may be returned instead.

No exception is thrown if

oldl

is

null

.

No exception is thrown if

oldl

is

null

.

componentResized

```java
public void componentResized​(
ComponentEvent
e)
```

Handles the componentResized event by invoking the
componentResized methods on listener-a and listener-b.

**Specified by:** componentResized

in interface

ComponentListener
**Parameters:** e

- the component event

---

#### componentResized

public void componentResized​(

ComponentEvent

e)

Handles the componentResized event by invoking the
componentResized methods on listener-a and listener-b.

componentMoved

```java
public void componentMoved​(
ComponentEvent
e)
```

Handles the componentMoved event by invoking the
componentMoved methods on listener-a and listener-b.

**Specified by:** componentMoved

in interface

ComponentListener
**Parameters:** e

- the component event

---

#### componentMoved

public void componentMoved​(

ComponentEvent

e)

Handles the componentMoved event by invoking the
componentMoved methods on listener-a and listener-b.

componentShown

```java
public void componentShown​(
ComponentEvent
e)
```

Handles the componentShown event by invoking the
componentShown methods on listener-a and listener-b.

**Specified by:** componentShown

in interface

ComponentListener
**Parameters:** e

- the component event

---

#### componentShown

public void componentShown​(

ComponentEvent

e)

Handles the componentShown event by invoking the
componentShown methods on listener-a and listener-b.

componentHidden

```java
public void componentHidden​(
ComponentEvent
e)
```

Handles the componentHidden event by invoking the
componentHidden methods on listener-a and listener-b.

**Specified by:** componentHidden

in interface

ComponentListener
**Parameters:** e

- the component event

---

#### componentHidden

public void componentHidden​(

ComponentEvent

e)

Handles the componentHidden event by invoking the
componentHidden methods on listener-a and listener-b.

componentAdded

```java
public void componentAdded​(
ContainerEvent
e)
```

Handles the componentAdded container event by invoking the
componentAdded methods on listener-a and listener-b.

**Specified by:** componentAdded

in interface

ContainerListener
**Parameters:** e

- the component event

---

#### componentAdded

public void componentAdded​(

ContainerEvent

e)

Handles the componentAdded container event by invoking the
componentAdded methods on listener-a and listener-b.

componentRemoved

```java
public void componentRemoved​(
ContainerEvent
e)
```

Handles the componentRemoved container event by invoking the
componentRemoved methods on listener-a and listener-b.

**Specified by:** componentRemoved

in interface

ContainerListener
**Parameters:** e

- the component event

---

#### componentRemoved

public void componentRemoved​(

ContainerEvent

e)

Handles the componentRemoved container event by invoking the
componentRemoved methods on listener-a and listener-b.

focusGained

```java
public void focusGained​(
FocusEvent
e)
```

Handles the focusGained event by invoking the
focusGained methods on listener-a and listener-b.

**Specified by:** focusGained

in interface

FocusListener
**Parameters:** e

- the focus event

---

#### focusGained

public void focusGained​(

FocusEvent

e)

Handles the focusGained event by invoking the
focusGained methods on listener-a and listener-b.

focusLost

```java
public void focusLost​(
FocusEvent
e)
```

Handles the focusLost event by invoking the
focusLost methods on listener-a and listener-b.

**Specified by:** focusLost

in interface

FocusListener
**Parameters:** e

- the focus event

---

#### focusLost

public void focusLost​(

FocusEvent

e)

Handles the focusLost event by invoking the
focusLost methods on listener-a and listener-b.

keyTyped

```java
public void keyTyped​(
KeyEvent
e)
```

Handles the keyTyped event by invoking the
keyTyped methods on listener-a and listener-b.

**Specified by:** keyTyped

in interface

KeyListener
**Parameters:** e

- the key event

---

#### keyTyped

public void keyTyped​(

KeyEvent

e)

Handles the keyTyped event by invoking the
keyTyped methods on listener-a and listener-b.

keyPressed

```java
public void keyPressed​(
KeyEvent
e)
```

Handles the keyPressed event by invoking the
keyPressed methods on listener-a and listener-b.

**Specified by:** keyPressed

in interface

KeyListener
**Parameters:** e

- the key event

---

#### keyPressed

public void keyPressed​(

KeyEvent

e)

Handles the keyPressed event by invoking the
keyPressed methods on listener-a and listener-b.

keyReleased

```java
public void keyReleased​(
KeyEvent
e)
```

Handles the keyReleased event by invoking the
keyReleased methods on listener-a and listener-b.

**Specified by:** keyReleased

in interface

KeyListener
**Parameters:** e

- the key event

---

#### keyReleased

public void keyReleased​(

KeyEvent

e)

Handles the keyReleased event by invoking the
keyReleased methods on listener-a and listener-b.

mouseClicked

```java
public void mouseClicked​(
MouseEvent
e)
```

Handles the mouseClicked event by invoking the
mouseClicked methods on listener-a and listener-b.

**Specified by:** mouseClicked

in interface

MouseListener
**Parameters:** e

- the mouse event

---

#### mouseClicked

public void mouseClicked​(

MouseEvent

e)

Handles the mouseClicked event by invoking the
mouseClicked methods on listener-a and listener-b.

mousePressed

```java
public void mousePressed​(
MouseEvent
e)
```

Handles the mousePressed event by invoking the
mousePressed methods on listener-a and listener-b.

**Specified by:** mousePressed

in interface

MouseListener
**Parameters:** e

- the mouse event

---

#### mousePressed

public void mousePressed​(

MouseEvent

e)

Handles the mousePressed event by invoking the
mousePressed methods on listener-a and listener-b.

mouseReleased

```java
public void mouseReleased​(
MouseEvent
e)
```

Handles the mouseReleased event by invoking the
mouseReleased methods on listener-a and listener-b.

**Specified by:** mouseReleased

in interface

MouseListener
**Parameters:** e

- the mouse event

---

#### mouseReleased

public void mouseReleased​(

MouseEvent

e)

Handles the mouseReleased event by invoking the
mouseReleased methods on listener-a and listener-b.

mouseEntered

```java
public void mouseEntered​(
MouseEvent
e)
```

Handles the mouseEntered event by invoking the
mouseEntered methods on listener-a and listener-b.

**Specified by:** mouseEntered

in interface

MouseListener
**Parameters:** e

- the mouse event

---

#### mouseEntered

public void mouseEntered​(

MouseEvent

e)

Handles the mouseEntered event by invoking the
mouseEntered methods on listener-a and listener-b.

mouseExited

```java
public void mouseExited​(
MouseEvent
e)
```

Handles the mouseExited event by invoking the
mouseExited methods on listener-a and listener-b.

**Specified by:** mouseExited

in interface

MouseListener
**Parameters:** e

- the mouse event

---

#### mouseExited

public void mouseExited​(

MouseEvent

e)

Handles the mouseExited event by invoking the
mouseExited methods on listener-a and listener-b.

mouseDragged

```java
public void mouseDragged​(
MouseEvent
e)
```

Handles the mouseDragged event by invoking the
mouseDragged methods on listener-a and listener-b.

**Specified by:** mouseDragged

in interface

MouseMotionListener
**Parameters:** e

- the mouse event

---

#### mouseDragged

public void mouseDragged​(

MouseEvent

e)

Handles the mouseDragged event by invoking the
mouseDragged methods on listener-a and listener-b.

mouseMoved

```java
public void mouseMoved​(
MouseEvent
e)
```

Handles the mouseMoved event by invoking the
mouseMoved methods on listener-a and listener-b.

**Specified by:** mouseMoved

in interface

MouseMotionListener
**Parameters:** e

- the mouse event

---

#### mouseMoved

public void mouseMoved​(

MouseEvent

e)

Handles the mouseMoved event by invoking the
mouseMoved methods on listener-a and listener-b.

windowOpened

```java
public void windowOpened​(
WindowEvent
e)
```

Handles the windowOpened event by invoking the
windowOpened methods on listener-a and listener-b.

**Specified by:** windowOpened

in interface

WindowListener
**Parameters:** e

- the window event

---

#### windowOpened

public void windowOpened​(

WindowEvent

e)

Handles the windowOpened event by invoking the
windowOpened methods on listener-a and listener-b.

windowClosing

```java
public void windowClosing​(
WindowEvent
e)
```

Handles the windowClosing event by invoking the
windowClosing methods on listener-a and listener-b.

**Specified by:** windowClosing

in interface

WindowListener
**Parameters:** e

- the window event

---

#### windowClosing

public void windowClosing​(

WindowEvent

e)

Handles the windowClosing event by invoking the
windowClosing methods on listener-a and listener-b.

windowClosed

```java
public void windowClosed​(
WindowEvent
e)
```

Handles the windowClosed event by invoking the
windowClosed methods on listener-a and listener-b.

**Specified by:** windowClosed

in interface

WindowListener
**Parameters:** e

- the window event

---

#### windowClosed

public void windowClosed​(

WindowEvent

e)

Handles the windowClosed event by invoking the
windowClosed methods on listener-a and listener-b.

windowIconified

```java
public void windowIconified​(
WindowEvent
e)
```

Handles the windowIconified event by invoking the
windowIconified methods on listener-a and listener-b.

**Specified by:** windowIconified

in interface

WindowListener
**Parameters:** e

- the window event
**See Also:** Window.setIconImage(java.awt.Image)

---

#### windowIconified

public void windowIconified​(

WindowEvent

e)

Handles the windowIconified event by invoking the
windowIconified methods on listener-a and listener-b.

windowDeiconified

```java
public void windowDeiconified​(
WindowEvent
e)
```

Handles the windowDeiconified event by invoking the
windowDeiconified methods on listener-a and listener-b.

**Specified by:** windowDeiconified

in interface

WindowListener
**Parameters:** e

- the window event

---

#### windowDeiconified

public void windowDeiconified​(

WindowEvent

e)

Handles the windowDeiconified event by invoking the
windowDeiconified methods on listener-a and listener-b.

windowActivated

```java
public void windowActivated​(
WindowEvent
e)
```

Handles the windowActivated event by invoking the
windowActivated methods on listener-a and listener-b.

**Specified by:** windowActivated

in interface

WindowListener
**Parameters:** e

- the window event

---

#### windowActivated

public void windowActivated​(

WindowEvent

e)

Handles the windowActivated event by invoking the
windowActivated methods on listener-a and listener-b.

windowDeactivated

```java
public void windowDeactivated​(
WindowEvent
e)
```

Handles the windowDeactivated event by invoking the
windowDeactivated methods on listener-a and listener-b.

**Specified by:** windowDeactivated

in interface

WindowListener
**Parameters:** e

- the window event

---

#### windowDeactivated

public void windowDeactivated​(

WindowEvent

e)

Handles the windowDeactivated event by invoking the
windowDeactivated methods on listener-a and listener-b.

windowStateChanged

```java
public void windowStateChanged​(
WindowEvent
e)
```

Handles the windowStateChanged event by invoking the
windowStateChanged methods on listener-a and listener-b.

**Specified by:** windowStateChanged

in interface

WindowStateListener
**Parameters:** e

- the window event
**Since:** 1.4

---

#### windowStateChanged

public void windowStateChanged​(

WindowEvent

e)

Handles the windowStateChanged event by invoking the
windowStateChanged methods on listener-a and listener-b.

windowGainedFocus

```java
public void windowGainedFocus​(
WindowEvent
e)
```

Handles the windowGainedFocus event by invoking the windowGainedFocus
methods on listener-a and listener-b.

**Specified by:** windowGainedFocus

in interface

WindowFocusListener
**Parameters:** e

- the window event
**Since:** 1.4

---

#### windowGainedFocus

public void windowGainedFocus​(

WindowEvent

e)

Handles the windowGainedFocus event by invoking the windowGainedFocus
methods on listener-a and listener-b.

windowLostFocus

```java
public void windowLostFocus​(
WindowEvent
e)
```

Handles the windowLostFocus event by invoking the windowLostFocus
methods on listener-a and listener-b.

**Specified by:** windowLostFocus

in interface

WindowFocusListener
**Parameters:** e

- the window event
**Since:** 1.4

---

#### windowLostFocus

public void windowLostFocus​(

WindowEvent

e)

Handles the windowLostFocus event by invoking the windowLostFocus
methods on listener-a and listener-b.

actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

Handles the actionPerformed event by invoking the
actionPerformed methods on listener-a and listener-b.

**Specified by:** actionPerformed

in interface

ActionListener
**Parameters:** e

- the action event

---

#### actionPerformed

public void actionPerformed​(

ActionEvent

e)

Handles the actionPerformed event by invoking the
actionPerformed methods on listener-a and listener-b.

itemStateChanged

```java
public void itemStateChanged​(
ItemEvent
e)
```

Handles the itemStateChanged event by invoking the
itemStateChanged methods on listener-a and listener-b.

**Specified by:** itemStateChanged

in interface

ItemListener
**Parameters:** e

- the item event

---

#### itemStateChanged

public void itemStateChanged​(

ItemEvent

e)

Handles the itemStateChanged event by invoking the
itemStateChanged methods on listener-a and listener-b.

adjustmentValueChanged

```java
public void adjustmentValueChanged​(
AdjustmentEvent
e)
```

Handles the adjustmentValueChanged event by invoking the
adjustmentValueChanged methods on listener-a and listener-b.

**Specified by:** adjustmentValueChanged

in interface

AdjustmentListener
**Parameters:** e

- the adjustment event

---

#### adjustmentValueChanged

public void adjustmentValueChanged​(

AdjustmentEvent

e)

Handles the adjustmentValueChanged event by invoking the
adjustmentValueChanged methods on listener-a and listener-b.

inputMethodTextChanged

```java
public void inputMethodTextChanged​(
InputMethodEvent
e)
```

Handles the inputMethodTextChanged event by invoking the
inputMethodTextChanged methods on listener-a and listener-b.

**Specified by:** inputMethodTextChanged

in interface

InputMethodListener
**Parameters:** e

- the item event

---

#### inputMethodTextChanged

public void inputMethodTextChanged​(

InputMethodEvent

e)

Handles the inputMethodTextChanged event by invoking the
inputMethodTextChanged methods on listener-a and listener-b.

caretPositionChanged

```java
public void caretPositionChanged​(
InputMethodEvent
e)
```

Handles the caretPositionChanged event by invoking the
caretPositionChanged methods on listener-a and listener-b.

**Specified by:** caretPositionChanged

in interface

InputMethodListener
**Parameters:** e

- the item event

---

#### caretPositionChanged

public void caretPositionChanged​(

InputMethodEvent

e)

Handles the caretPositionChanged event by invoking the
caretPositionChanged methods on listener-a and listener-b.

hierarchyChanged

```java
public void hierarchyChanged​(
HierarchyEvent
e)
```

Handles the hierarchyChanged event by invoking the
hierarchyChanged methods on listener-a and listener-b.

**Specified by:** hierarchyChanged

in interface

HierarchyListener
**Parameters:** e

- the item event
**Since:** 1.3
**See Also:** HierarchyEvent.getChangeFlags()

---

#### hierarchyChanged

public void hierarchyChanged​(

HierarchyEvent

e)

Handles the hierarchyChanged event by invoking the
hierarchyChanged methods on listener-a and listener-b.

ancestorMoved

```java
public void ancestorMoved​(
HierarchyEvent
e)
```

Handles the ancestorMoved event by invoking the
ancestorMoved methods on listener-a and listener-b.

**Specified by:** ancestorMoved

in interface

HierarchyBoundsListener
**Parameters:** e

- the item event
**Since:** 1.3

---

#### ancestorMoved

public void ancestorMoved​(

HierarchyEvent

e)

Handles the ancestorMoved event by invoking the
ancestorMoved methods on listener-a and listener-b.

ancestorResized

```java
public void ancestorResized​(
HierarchyEvent
e)
```

Handles the ancestorResized event by invoking the
ancestorResized methods on listener-a and listener-b.

**Specified by:** ancestorResized

in interface

HierarchyBoundsListener
**Parameters:** e

- the item event
**Since:** 1.3

---

#### ancestorResized

public void ancestorResized​(

HierarchyEvent

e)

Handles the ancestorResized event by invoking the
ancestorResized methods on listener-a and listener-b.

mouseWheelMoved

```java
public void mouseWheelMoved​(
MouseWheelEvent
e)
```

Handles the mouseWheelMoved event by invoking the
mouseWheelMoved methods on listener-a and listener-b.

**Specified by:** mouseWheelMoved

in interface

MouseWheelListener
**Parameters:** e

- the mouse event
**Since:** 1.4
**See Also:** MouseWheelEvent

---

#### mouseWheelMoved

public void mouseWheelMoved​(

MouseWheelEvent

e)

Handles the mouseWheelMoved event by invoking the
mouseWheelMoved methods on listener-a and listener-b.

add

```java
public static
ComponentListener
add​(
ComponentListener
a,

ComponentListener
b)
```

Adds component-listener-a with component-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- component-listener-a
**Parameters:** b

- component-listener-b
**Returns:** the resulting listener

---

#### add

public static

ComponentListener

add​(

ComponentListener

a,

ComponentListener

b)

Adds component-listener-a with component-listener-b and
returns the resulting multicast listener.

add

```java
public static
ContainerListener
add​(
ContainerListener
a,

ContainerListener
b)
```

Adds container-listener-a with container-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- container-listener-a
**Parameters:** b

- container-listener-b
**Returns:** the resulting listener

---

#### add

public static

ContainerListener

add​(

ContainerListener

a,

ContainerListener

b)

Adds container-listener-a with container-listener-b and
returns the resulting multicast listener.

add

```java
public static
FocusListener
add​(
FocusListener
a,

FocusListener
b)
```

Adds focus-listener-a with focus-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- focus-listener-a
**Parameters:** b

- focus-listener-b
**Returns:** the resulting listener

---

#### add

public static

FocusListener

add​(

FocusListener

a,

FocusListener

b)

Adds focus-listener-a with focus-listener-b and
returns the resulting multicast listener.

add

```java
public static
KeyListener
add​(
KeyListener
a,

KeyListener
b)
```

Adds key-listener-a with key-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- key-listener-a
**Parameters:** b

- key-listener-b
**Returns:** the resulting listener

---

#### add

public static

KeyListener

add​(

KeyListener

a,

KeyListener

b)

Adds key-listener-a with key-listener-b and
returns the resulting multicast listener.

add

```java
public static
MouseListener
add​(
MouseListener
a,

MouseListener
b)
```

Adds mouse-listener-a with mouse-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- mouse-listener-a
**Parameters:** b

- mouse-listener-b
**Returns:** the resulting listener

---

#### add

public static

MouseListener

add​(

MouseListener

a,

MouseListener

b)

Adds mouse-listener-a with mouse-listener-b and
returns the resulting multicast listener.

add

```java
public static
MouseMotionListener
add​(
MouseMotionListener
a,

MouseMotionListener
b)
```

Adds mouse-motion-listener-a with mouse-motion-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- mouse-motion-listener-a
**Parameters:** b

- mouse-motion-listener-b
**Returns:** the resulting listener

---

#### add

public static

MouseMotionListener

add​(

MouseMotionListener

a,

MouseMotionListener

b)

Adds mouse-motion-listener-a with mouse-motion-listener-b and
returns the resulting multicast listener.

add

```java
public static
WindowListener
add​(
WindowListener
a,

WindowListener
b)
```

Adds window-listener-a with window-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- window-listener-a
**Parameters:** b

- window-listener-b
**Returns:** the resulting listener

---

#### add

public static

WindowListener

add​(

WindowListener

a,

WindowListener

b)

Adds window-listener-a with window-listener-b and
returns the resulting multicast listener.

add

```java
public static
WindowStateListener
add​(
WindowStateListener
a,

WindowStateListener
b)
```

Adds window-state-listener-a with window-state-listener-b
and returns the resulting multicast listener.

**Parameters:** a

- window-state-listener-a
**Parameters:** b

- window-state-listener-b
**Returns:** the resulting listener
**Since:** 1.4

---

#### add

public static

WindowStateListener

add​(

WindowStateListener

a,

WindowStateListener

b)

Adds window-state-listener-a with window-state-listener-b
and returns the resulting multicast listener.

add

```java
public static
WindowFocusListener
add​(
WindowFocusListener
a,

WindowFocusListener
b)
```

Adds window-focus-listener-a with window-focus-listener-b
and returns the resulting multicast listener.

**Parameters:** a

- window-focus-listener-a
**Parameters:** b

- window-focus-listener-b
**Returns:** the resulting listener
**Since:** 1.4

---

#### add

public static

WindowFocusListener

add​(

WindowFocusListener

a,

WindowFocusListener

b)

Adds window-focus-listener-a with window-focus-listener-b
and returns the resulting multicast listener.

add

```java
public static
ActionListener
add​(
ActionListener
a,

ActionListener
b)
```

Adds action-listener-a with action-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- action-listener-a
**Parameters:** b

- action-listener-b
**Returns:** the resulting listener

---

#### add

public static

ActionListener

add​(

ActionListener

a,

ActionListener

b)

Adds action-listener-a with action-listener-b and
returns the resulting multicast listener.

add

```java
public static
ItemListener
add​(
ItemListener
a,

ItemListener
b)
```

Adds item-listener-a with item-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- item-listener-a
**Parameters:** b

- item-listener-b
**Returns:** the resulting listener

---

#### add

public static

ItemListener

add​(

ItemListener

a,

ItemListener

b)

Adds item-listener-a with item-listener-b and
returns the resulting multicast listener.

add

```java
public static
AdjustmentListener
add​(
AdjustmentListener
a,

AdjustmentListener
b)
```

Adds adjustment-listener-a with adjustment-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- adjustment-listener-a
**Parameters:** b

- adjustment-listener-b
**Returns:** the resulting listener

---

#### add

public static

AdjustmentListener

add​(

AdjustmentListener

a,

AdjustmentListener

b)

Adds adjustment-listener-a with adjustment-listener-b and
returns the resulting multicast listener.

add

```java
public static
TextListener
add​(
TextListener
a,

TextListener
b)
```

Adds text-listener-a with text-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- text-listener-a
**Parameters:** b

- text-listener-b
**Returns:** the resulting listener

---

#### add

public static

TextListener

add​(

TextListener

a,

TextListener

b)

Adds text-listener-a with text-listener-b and
returns the resulting multicast listener.

add

```java
public static
InputMethodListener
add​(
InputMethodListener
a,

InputMethodListener
b)
```

Adds input-method-listener-a with input-method-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- input-method-listener-a
**Parameters:** b

- input-method-listener-b
**Returns:** the resulting listener

---

#### add

public static

InputMethodListener

add​(

InputMethodListener

a,

InputMethodListener

b)

Adds input-method-listener-a with input-method-listener-b and
returns the resulting multicast listener.

add

```java
public static
HierarchyListener
add​(
HierarchyListener
a,

HierarchyListener
b)
```

Adds hierarchy-listener-a with hierarchy-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- hierarchy-listener-a
**Parameters:** b

- hierarchy-listener-b
**Returns:** the resulting listener
**Since:** 1.3

---

#### add

public static

HierarchyListener

add​(

HierarchyListener

a,

HierarchyListener

b)

Adds hierarchy-listener-a with hierarchy-listener-b and
returns the resulting multicast listener.

add

```java
public static
HierarchyBoundsListener
add​(
HierarchyBoundsListener
a,

HierarchyBoundsListener
b)
```

Adds hierarchy-bounds-listener-a with hierarchy-bounds-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- hierarchy-bounds-listener-a
**Parameters:** b

- hierarchy-bounds-listener-b
**Returns:** the resulting listener
**Since:** 1.3

---

#### add

public static

HierarchyBoundsListener

add​(

HierarchyBoundsListener

a,

HierarchyBoundsListener

b)

Adds hierarchy-bounds-listener-a with hierarchy-bounds-listener-b and
returns the resulting multicast listener.

add

```java
public static
MouseWheelListener
add​(
MouseWheelListener
a,

MouseWheelListener
b)
```

Adds mouse-wheel-listener-a with mouse-wheel-listener-b and
returns the resulting multicast listener.

**Parameters:** a

- mouse-wheel-listener-a
**Parameters:** b

- mouse-wheel-listener-b
**Returns:** the resulting listener
**Since:** 1.4

---

#### add

public static

MouseWheelListener

add​(

MouseWheelListener

a,

MouseWheelListener

b)

Adds mouse-wheel-listener-a with mouse-wheel-listener-b and
returns the resulting multicast listener.

remove

```java
public static
ComponentListener
remove​(
ComponentListener
l,

ComponentListener
oldl)
```

Removes the old component-listener from component-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- component-listener-l
**Parameters:** oldl

- the component-listener being removed
**Returns:** the resulting listener

---

#### remove

public static

ComponentListener

remove​(

ComponentListener

l,

ComponentListener

oldl)

Removes the old component-listener from component-listener-l and
returns the resulting multicast listener.

remove

```java
public static
ContainerListener
remove​(
ContainerListener
l,

ContainerListener
oldl)
```

Removes the old container-listener from container-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- container-listener-l
**Parameters:** oldl

- the container-listener being removed
**Returns:** the resulting listener

---

#### remove

public static

ContainerListener

remove​(

ContainerListener

l,

ContainerListener

oldl)

Removes the old container-listener from container-listener-l and
returns the resulting multicast listener.

remove

```java
public static
FocusListener
remove​(
FocusListener
l,

FocusListener
oldl)
```

Removes the old focus-listener from focus-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- focus-listener-l
**Parameters:** oldl

- the focus-listener being removed
**Returns:** the resulting listener

---

#### remove

public static

FocusListener

remove​(

FocusListener

l,

FocusListener

oldl)

Removes the old focus-listener from focus-listener-l and
returns the resulting multicast listener.

remove

```java
public static
KeyListener
remove​(
KeyListener
l,

KeyListener
oldl)
```

Removes the old key-listener from key-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- key-listener-l
**Parameters:** oldl

- the key-listener being removed
**Returns:** the resulting listener

---

#### remove

public static

KeyListener

remove​(

KeyListener

l,

KeyListener

oldl)

Removes the old key-listener from key-listener-l and
returns the resulting multicast listener.

remove

```java
public static
MouseListener
remove​(
MouseListener
l,

MouseListener
oldl)
```

Removes the old mouse-listener from mouse-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- mouse-listener-l
**Parameters:** oldl

- the mouse-listener being removed
**Returns:** the resulting listener

---

#### remove

public static

MouseListener

remove​(

MouseListener

l,

MouseListener

oldl)

Removes the old mouse-listener from mouse-listener-l and
returns the resulting multicast listener.

remove

```java
public static
MouseMotionListener
remove​(
MouseMotionListener
l,

MouseMotionListener
oldl)
```

Removes the old mouse-motion-listener from mouse-motion-listener-l
and returns the resulting multicast listener.

**Parameters:** l

- mouse-motion-listener-l
**Parameters:** oldl

- the mouse-motion-listener being removed
**Returns:** the resulting listener

---

#### remove

public static

MouseMotionListener

remove​(

MouseMotionListener

l,

MouseMotionListener

oldl)

Removes the old mouse-motion-listener from mouse-motion-listener-l
and returns the resulting multicast listener.

remove

```java
public static
WindowListener
remove​(
WindowListener
l,

WindowListener
oldl)
```

Removes the old window-listener from window-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- window-listener-l
**Parameters:** oldl

- the window-listener being removed
**Returns:** the resulting listener

---

#### remove

public static

WindowListener

remove​(

WindowListener

l,

WindowListener

oldl)

Removes the old window-listener from window-listener-l and
returns the resulting multicast listener.

remove

```java
public static
WindowStateListener
remove​(
WindowStateListener
l,

WindowStateListener
oldl)
```

Removes the old window-state-listener from window-state-listener-l
and returns the resulting multicast listener.

**Parameters:** l

- window-state-listener-l
**Parameters:** oldl

- the window-state-listener being removed
**Returns:** the resulting listener
**Since:** 1.4

---

#### remove

public static

WindowStateListener

remove​(

WindowStateListener

l,

WindowStateListener

oldl)

Removes the old window-state-listener from window-state-listener-l
and returns the resulting multicast listener.

remove

```java
public static
WindowFocusListener
remove​(
WindowFocusListener
l,

WindowFocusListener
oldl)
```

Removes the old window-focus-listener from window-focus-listener-l
and returns the resulting multicast listener.

**Parameters:** l

- window-focus-listener-l
**Parameters:** oldl

- the window-focus-listener being removed
**Returns:** the resulting listener
**Since:** 1.4

---

#### remove

public static

WindowFocusListener

remove​(

WindowFocusListener

l,

WindowFocusListener

oldl)

Removes the old window-focus-listener from window-focus-listener-l
and returns the resulting multicast listener.

remove

```java
public static
ActionListener
remove​(
ActionListener
l,

ActionListener
oldl)
```

Removes the old action-listener from action-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- action-listener-l
**Parameters:** oldl

- the action-listener being removed
**Returns:** the resulting listener

---

#### remove

public static

ActionListener

remove​(

ActionListener

l,

ActionListener

oldl)

Removes the old action-listener from action-listener-l and
returns the resulting multicast listener.

remove

```java
public static
ItemListener
remove​(
ItemListener
l,

ItemListener
oldl)
```

Removes the old item-listener from item-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- item-listener-l
**Parameters:** oldl

- the item-listener being removed
**Returns:** the resulting listener

---

#### remove

public static

ItemListener

remove​(

ItemListener

l,

ItemListener

oldl)

Removes the old item-listener from item-listener-l and
returns the resulting multicast listener.

remove

```java
public static
AdjustmentListener
remove​(
AdjustmentListener
l,

AdjustmentListener
oldl)
```

Removes the old adjustment-listener from adjustment-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- adjustment-listener-l
**Parameters:** oldl

- the adjustment-listener being removed
**Returns:** the resulting listener

---

#### remove

public static

AdjustmentListener

remove​(

AdjustmentListener

l,

AdjustmentListener

oldl)

Removes the old adjustment-listener from adjustment-listener-l and
returns the resulting multicast listener.

remove

```java
public static
TextListener
remove​(
TextListener
l,

TextListener
oldl)
```

Removes the old text-listener from text-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- text-listener-l
**Parameters:** oldl

- the text-listener being removed
**Returns:** the resulting listener

---

#### remove

public static

TextListener

remove​(

TextListener

l,

TextListener

oldl)

Removes the old text-listener from text-listener-l and
returns the resulting multicast listener.

remove

```java
public static
InputMethodListener
remove​(
InputMethodListener
l,

InputMethodListener
oldl)
```

Removes the old input-method-listener from input-method-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- input-method-listener-l
**Parameters:** oldl

- the input-method-listener being removed
**Returns:** the resulting listener

---

#### remove

public static

InputMethodListener

remove​(

InputMethodListener

l,

InputMethodListener

oldl)

Removes the old input-method-listener from input-method-listener-l and
returns the resulting multicast listener.

remove

```java
public static
HierarchyListener
remove​(
HierarchyListener
l,

HierarchyListener
oldl)
```

Removes the old hierarchy-listener from hierarchy-listener-l and
returns the resulting multicast listener.

**Parameters:** l

- hierarchy-listener-l
**Parameters:** oldl

- the hierarchy-listener being removed
**Returns:** the resulting listener
**Since:** 1.3

---

#### remove

public static

HierarchyListener

remove​(

HierarchyListener

l,

HierarchyListener

oldl)

Removes the old hierarchy-listener from hierarchy-listener-l and
returns the resulting multicast listener.

remove

```java
public static
HierarchyBoundsListener
remove​(
HierarchyBoundsListener
l,

HierarchyBoundsListener
oldl)
```

Removes the old hierarchy-bounds-listener from
hierarchy-bounds-listener-l and returns the resulting multicast
listener.

**Parameters:** l

- hierarchy-bounds-listener-l
**Parameters:** oldl

- the hierarchy-bounds-listener being removed
**Returns:** the resulting listener
**Since:** 1.3

---

#### remove

public static

HierarchyBoundsListener

remove​(

HierarchyBoundsListener

l,

HierarchyBoundsListener

oldl)

Removes the old hierarchy-bounds-listener from
hierarchy-bounds-listener-l and returns the resulting multicast
listener.

remove

```java
public static
MouseWheelListener
remove​(
MouseWheelListener
l,

MouseWheelListener
oldl)
```

Removes the old mouse-wheel-listener from mouse-wheel-listener-l
and returns the resulting multicast listener.

**Parameters:** l

- mouse-wheel-listener-l
**Parameters:** oldl

- the mouse-wheel-listener being removed
**Returns:** the resulting listener
**Since:** 1.4

---

#### remove

public static

MouseWheelListener

remove​(

MouseWheelListener

l,

MouseWheelListener

oldl)

Removes the old mouse-wheel-listener from mouse-wheel-listener-l
and returns the resulting multicast listener.

addInternal

```java
protected static
EventListener
addInternal​(
EventListener
a,

EventListener
b)
```

Returns the resulting multicast listener from adding listener-a
and listener-b together.
If listener-a is null, it returns listener-b;
If listener-b is null, it returns listener-a
If neither are null, then it creates and returns
a new AWTEventMulticaster instance which chains a with b.

**Parameters:** a

- event listener-a
**Parameters:** b

- event listener-b
**Returns:** the resulting listener

---

#### addInternal

protected static

EventListener

addInternal​(

EventListener

a,

EventListener

b)

Returns the resulting multicast listener from adding listener-a
and listener-b together.
If listener-a is null, it returns listener-b;
If listener-b is null, it returns listener-a
If neither are null, then it creates and returns
a new AWTEventMulticaster instance which chains a with b.

removeInternal

```java
protected static
EventListener
removeInternal​(
EventListener
l,

EventListener
oldl)
```

Returns the resulting multicast listener after removing the
old listener from listener-l.
If listener-l equals the old listener OR listener-l is null,
returns null.
Else if listener-l is an instance of AWTEventMulticaster,
then it removes the old listener from it.
Else, returns listener l.

**Parameters:** l

- the listener being removed from
**Parameters:** oldl

- the listener being removed
**Returns:** the resulting listener

---

#### removeInternal

protected static

EventListener

removeInternal​(

EventListener

l,

EventListener

oldl)

Returns the resulting multicast listener after removing the
old listener from listener-l.
If listener-l equals the old listener OR listener-l is null,
returns null.
Else if listener-l is an instance of AWTEventMulticaster,
then it removes the old listener from it.
Else, returns listener l.

saveInternal

```java
protected void saveInternal​(
ObjectOutputStream
s,

String
k)
throws
IOException
```

Serialization support. Saves all Serializable listeners
to a serialization stream.

**Parameters:** s

- the stream to save to
**Parameters:** k

- a prefix stream to put before each serializable listener
**Throws:** IOException

- if serialization fails

---

#### saveInternal

protected void saveInternal​(

ObjectOutputStream

s,

String

k)
throws

IOException

Serialization support. Saves all Serializable listeners
to a serialization stream.

save

```java
protected static void save​(
ObjectOutputStream
s,

String
k,

EventListener
l)
throws
IOException
```

Saves a Serializable listener chain to a serialization stream.

**Parameters:** s

- the stream to save to
**Parameters:** k

- a prefix stream to put before each serializable listener
**Parameters:** l

- the listener chain to save
**Throws:** IOException

- if serialization fails

---

#### save

protected static void save​(

ObjectOutputStream

s,

String

k,

EventListener

l)
throws

IOException

Saves a Serializable listener chain to a serialization stream.

getListeners

```java
public static <T extends
EventListener
> T[] getListeners​(
EventListener
l,

Class
<T> listenerType)
```

Returns an array of all the objects chained as

Foo

Listener

s by the specified

java.util.EventListener

.

Foo

Listener

s are chained by the

AWTEventMulticaster

using the

add

Foo

Listener

method.
If a

null

listener is specified, this method returns an
empty array. If the specified listener is not an instance of

AWTEventMulticaster

, this method returns an array which
contains only the specified listener. If no such listeners are chained,
this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** l

- the specified

java.util.EventListener
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects chained as

Foo

Listener

s by the specified multicast
listener, or an empty array if no such listeners have been
chained by the specified multicast listener
**Throws:** NullPointerException

- if the specified

listenertype

parameter is

null
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.4

---

#### getListeners

public static <T extends

EventListener

> T[] getListeners​(

EventListener

l,

Class

<T> listenerType)

Returns an array of all the objects chained as

Foo

Listener

s by the specified

java.util.EventListener

.

Foo

Listener

s are chained by the

AWTEventMulticaster

using the

add

Foo

Listener

method.
If a

null

listener is specified, this method returns an
empty array. If the specified listener is not an instance of

AWTEventMulticaster

, this method returns an array which
contains only the specified listener. If no such listeners are chained,
this method returns an empty array.

---

